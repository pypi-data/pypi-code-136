from sqlalchemy import create_engine


class Database:
    def __init__(self, conn_str):
        self.conn_str = conn_str
        self._test_conn()
        self._conn_ctx = None

    def _test_conn(self):
        engine = create_engine(self.conn_str)
        with engine.connect() as con:
            sql = "select 1"
            con.execute(sql).all()

        self.engine = engine

    def __enter__(self):
        self._conn_ctx = self.engine.connect()
        return self._conn_ctx.__enter__()

    def __exit__(self, *args, **kwargs):
        self._conn_ctx.__exit__(*args, **kwargs)
        self._conn_ctx = None
