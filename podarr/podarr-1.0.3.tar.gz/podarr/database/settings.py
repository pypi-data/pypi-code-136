from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import podarr

DATABASE_URL = f'sqlite:///{podarr.Directory.DIR_BASE.as_posix()}/podarr.db'

DATABASE_ENGINE = create_engine(DATABASE_URL, connect_args={
                                "check_same_thread": False})

SESSION_MAKER = sessionmaker(autoflush=False, bind=DATABASE_ENGINE)()

BASE_MODEL = declarative_base()


def create_dependency():
    db_session = SESSION_MAKER
    try:
        yield db_session
    finally:
        db_session.close()
