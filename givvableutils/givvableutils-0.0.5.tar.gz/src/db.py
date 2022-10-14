import psycopg2
import psycopg2.extras

def get_db_conn(username, password, host, database):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            user=username, password=password, host=host, dbname=database
        )

        print('Connected successfully...')
        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def close_db_conn(conn):
    if conn is not None:
        conn.close()
        print('Database connection closed.')
    else:
        print('Database connection not closed because it doesn\'t exist.')


# # Connect to an existing database
# conn = get_db_conn()

# # Open a cursor to perform database operations
# cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
