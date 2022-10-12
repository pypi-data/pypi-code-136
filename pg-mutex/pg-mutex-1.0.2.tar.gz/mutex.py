from contextlib import contextmanager
from hashlib import md5
from zlib import crc32

from psycopg2.extensions import connection


@contextmanager
def mutex(pg_connection: connection, keys: list, wait: bool = True):
    func = 'pg_advisory_lock' if wait else 'pg_try_advisory_lock'
    key = md5('/'.join(str(p) for p in tuple(keys)).encode()).hexdigest()
    lock_id = generate_lock_id(key)
    cursor = pg_connection.cursor()
    cursor.execute(f'SELECT {func}(%s)', [lock_id])

    if not wait and not cursor.fetchone()[0]:
        raise Warning('The previous task has not done.')

    try:
        yield
    finally:
        cursor.execute('SELECT pg_advisory_unlock(%s)', [lock_id])
        cursor.close()


def generate_lock_id(key: str) -> int:
    """Generate ID from -2^31 to 2^31 - 1 from text key"""
    pos = crc32(key.encode("utf-8"))
    lock_id = (2 ** 31 - 1) & pos
    if pos & 2 ** 31:
        lock_id -= 2 ** 31

    return lock_id
