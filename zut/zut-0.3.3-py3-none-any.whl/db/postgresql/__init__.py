import re, logging
from pathlib import Path
from .. import get_connection

_pg_msg_re = re.compile(r"^(?P<pglevel>[A-Z]+)\:\s(?P<message>.+(?:\r?\n.*)*)$", re.MULTILINE)

class PgLogHandler:
    """
    Usage example:
    ```
    from django.apps import AppConfig
    from django.db.backends.signals import connection_created
    from zut.db.postgresql import PgLogHandler

    def connection_created_receiver(sender, connection, **kwargs):
        if connection.alias == "default":
            connection.connection.notices = PgLogHandler(connection.alias)

    class MainConfig(AppConfig):
        default_auto_field = "django.db.models.BigAutoField"
        name = "main"
        
        def ready(self):
            connection_created.connect(connection_created_receiver)
    ```
    """
    def __init__(self, alias: str):
        self.logger = logging.getLogger(f"pg:{alias}")
    
    def append(self, fullmsg: str):
        fullmsg = fullmsg.strip()
        m = _pg_msg_re.match(fullmsg)
        if not m:
            self.logger.warning(fullmsg)
            return

        message = m.group("message").strip()
        pglevel = m.group("pglevel")
        if pglevel == "EXCEPTION":
            level = logging.ERROR
        elif pglevel == "WARNING":
            level = logging.WARNING
        else:
            level = logging.INFO

        if level <= logging.INFO and message.endswith("\" does not exist, skipping"):
            return

        self.logger.log(level, message)


_pg_reserved_words = None

def get_pg_reserved_words(connection = None) -> list[str]:
    global _pg_reserved_words
    
    connection = get_connection(connection=connection)

    if _pg_reserved_words is None:
        with connection.cursor() as cursor:
            cursor.execute("select word from pg_get_keywords() where catcode = 'R'")
            _pg_reserved_words = [row[0] for row in cursor.fetchall()]
    return _pg_reserved_words


_pg_types = None

def get_pg_types(connection = None) -> dict[int, str]:
    global _pg_types

    connection = get_connection(connection=connection)

    if _pg_types is None:
        with connection.cursor() as cursor:
            cursor.execute("select oid, typname from pg_type")
            _pg_types = {row[0]: row[1] for row in cursor.fetchall()}
    return _pg_types


# TODO/FIXME: does not seem to work
# def upgrade_sequence_values(connection: connection, start_with=1001, prefix=None, suffix="_id_seq"):
#     name_like = (prefix if prefix else '') + "%" + (suffix if suffix else '')
#     sequence_names = []
#     with connection.cursor() as cursor:
#         cursor.execute(SQL("select sequencename from pg_sequences where sequencename like {} and start_value = 1 and coalesce(last_value, 0) < {}").format(Literal(name_like), Literal(start_with)))
#         for record in cursor:
#             sequence_names.append(record[0])

#     for sequence_name in sequence_names:
#         with connection.cursor() as cursor:
#             cursor.execute(SQL("alter sequence {} start with {} restart with {}").format(Identifier(sequence_name), Literal(start_with), Literal(start_with)))
