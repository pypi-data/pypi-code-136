from psycopg2.extras import execute_values, RealDictCursor

CREATE_AUDIOS = """CREATE TABLE IF NOT EXISTS audios
(id TEXT PRIMARY KEY, name TEXT, src TEXT, uploader TEXT);"""
SELECT_ALL_AUDIOS = "SELECT * FROM audios;"
SELECT_AUDIO = "SELECT * FROM audios WHERE audios.id = %s;"
INSERT_AUDIO = """INSERT INTO audios (id, name, src, uploader) 
VALUES (%s, %s, %s, %s); """
UPDATE_AUDIO = """UPDATE audios SET name = %s WHERE id = %s;"""
DELETE_AUDIO = """DELETE FROM audios WHERE id = %s;"""


def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_AUDIOS)


def get_all(connection):
    with connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(SELECT_ALL_AUDIOS)
            return cursor.fetchall()


def get_audio(connection, audioid):
    with connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(SELECT_AUDIO, (audioid,))
            return cursor.fetchall()


def delete_audio(connection, audioid):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_AUDIO, [audioid])


def create_audio(connection, mediaid, name, src, uploader):
    with connection:
        with connection.cursor() as cursor:
            # try:
            cursor.execute(INSERT_AUDIO, (mediaid, name, src, uploader))
