from pathlib import Path
from unittest import TestCase

from yw_etl_target_clickhouse.Database import ConnectionConfig, Database


class TestDatabase(TestCase):
    db: Database = None

    @classmethod
    def setUpClass(cls) -> None:
        conf = ConnectionConfig(host='localhost', port=8123, username="", password="")
        cls.db = Database(conf)

        cls.db.command("drop table if exists default.Foo")

        ddl = """
        create table default.Foo(
            a int,
            b text,
            c float
        ) engine MergeTree order by (a)
        """
        cls.db.command(ddl)

    def test_load_csv(self):
        pass
        csv_path = Path(__file__).parent.parent / 'test' / 'Database_test.csv'
        self.db.load_csv(csv_path, 'default.Foo')

        sql = "select * from default.Foo"
        rtn = self.db.query(sql)
        exp = [['1', 'a', '3.2'], ['2', 'b', '3.3']]
        self.assertEqual(exp, list(rtn))
