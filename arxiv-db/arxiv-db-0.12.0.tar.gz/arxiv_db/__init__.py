from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine as _create_engine
from sqlalchemy.orm import Session, registry
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql import text

from zoneinfo import ZoneInfo

mapper_registry = registry()

arxiv_business_tz = ZoneInfo('America/New_York')

class Base(metaclass=DeclarativeMeta):
    """Non-dynamic base for better types.

    See
    https://docs.sqlalchemy.org/en/14/orm/declarative_styles.html#creating-an-explicit-base-non-dynamically-for-use-with-mypy-similar
    """
    __abstract__ = True
    registry = mapper_registry
    metadata = mapper_registry.metadata
    __init__ = mapper_registry.constructor

def create_engine(db_uri:str, echo:bool, args:dict):
    if 'sqlite' in db_uri:
        args["check_same_thread"]=False

    return _create_engine(db_uri, echo=echo, connect_args=args)

def init_with_flask_sqlalchemy(db):
    """Takes a flask_sqlalchemy.SQLAlchemy object and uses that as Base.

    This allows the models and tables in this package to be used with
    flask_sqlalchemy.
    """
    global Base
    Base = db


def create_tables(engine: Engine):
    """Create any missing tables and insert the standard rows."""
    from .tables import arxiv_tables
    arxiv_tables.metadata.create_all(bind=engine)
    from .models.tapir_policy_classes import TapirPolicyClasses
    with Session(engine) as session:
        TapirPolicyClasses.insert_policy_classes(session)



def test_load_db_file(engine, test_data: str):
    """Loads the SQL from the `test_data` file into the `engine`"""

    def escape_bind(stmt):
        return stmt.replace(':0', '\\:0')

    with engine.connect() as db:
        cmd_count = 0
        badcmd = False
        print(f"Loading test data from file '{test_data}'...")
        with open(test_data) as sql:
            cmd = ""
            for ln, line in enumerate(map(escape_bind, sql)):
                try:
                    if line.startswith("--"):
                        continue
                    elif line and line.rstrip().endswith(";"):
                        cmd = cmd + line
                        if cmd:
                            #print(f"About to run '{cmd}'")
                            db.execute(text(cmd))
                            cmd_count = cmd_count + 1
                            cmd = ""
                        else:
                            #print("empty command")
                            cmd = ""
                    elif not line and cmd:
                        #print(f"About to run '{cmd}'")
                        db.execute(text(cmd))
                        cmd_count = cmd_count + 1
                        cmd = ""
                    elif not line:
                        continue
                    else:
                        cmd = cmd + line
                except Exception as err:
                    badcmd = f"At line {ln} Running command #{cmd_count}. {err}"
                    break

        if badcmd:
            # moved this out of the except to avoid pytest printing huge stack traces
            raise Exception(badcmd)
        else:
            print(f"Done loading test data. Ran {cmd_count} commands.")
