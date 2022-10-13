from typing import Optional

from .native import Connection, DatabaseSettings, initialize_db, transaction
from .schema_v1 import BuilderV1


def create_version_table(conn: Connection) -> str:
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER NOT NULL
        );
    """)


def get_schema_version(conn: Connection) -> Optional[int]:
    conn.execute("SELECT version from schema_version LIMIT 1;")
    version = conn.fetch_one()
    return None if version is None else int(version[0])


def update_schema_version(conn: Connection, newVersion: int):
    conn.execute("UPDATE schema_version SET version=?;", [newVersion])


def insert_schema_version(conn: Connection, newVersion: int):
    conn.execute("INSERT INTO schema_version VALUES(?);", [newVersion])


def setup_database(dbSettings: DatabaseSettings):
    # initialize db
    initialize_db(dbSettings)

    # Get a list of builders and sort them 
    # using the version property
    builders = [BuilderV1()]

    # for the future
    # builders.sort(key=lambda x: x.version)

    # ensure the schema and the version table is there 
    with transaction() as conn:
        create_version_table(conn)
        version = get_schema_version(conn)

    # get the 
    if version is None:
        # if there is no version
        # simply go to the latest version (last pos in builders)
        # and execute the script 
        builder = builders[len(builders) - 1]
        with transaction() as conn:
            builder.setup(conn)
            insert_schema_version(conn, builder.version)

    else:
        # if there is a schema in the system 
        # find the first builder above the current 
        # version and start patching
        for builder in builders:
            if builder.version > version:
                with transaction() as conn:
                    builder.patch()
                    update_schema_version(conn, builder.version)


__all__ = ['setup_database']
