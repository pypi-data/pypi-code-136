import imp
import sqlite3
import json
import datetime
from typing import Any, List, Tuple, Optional


class Incrementor:
    _count = 0

    def __init__(self) -> None:
        __class__._count += 1

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value


def _(s: str, lang: str = "en") -> str:
    """Translate a string to another language.
    
    Args:
        s (str): The string to translate.
        lang (str, optional): The language to translate to. Defaults
            to "en".
    
    Returns:
        str: The translated string.
    """
    if lang not in ("en", "es"):
        lang = "en"
    spanish = {
        "Error connecting to database:": 
            "Error al conectar con la base de datos:",
        "Error writing to database:":
            "Error al escribir en la base de datos:",
        "'data' must be a dict instance":
            "'data' debe ser un diccionario",
    }
    if lang == "es":
        return spanish[s]
    else:
        return s


def get_data(obj: object) -> dict:
    """Get the attributes and values of an object."""
    return {k: v for k, v in obj.__dict__.items() if not k.startswith("_")}


def cols(class_: object) -> dict:
    """Helper function to get the columns of a class."""
    types = {
        None: "NULL",
        int: "INTEGER",
        float: "REAL",
        str: "TEXT",
        bytes: "BLOB",
        datetime.date: "TEXT",
    }
    class_attrs = getattr(class_, "__annotations__")
    tmp = {k: types[v] for k, v in class_attrs.items()}
    return ", ".join([f"{k} {v}" for k, v in tmp.items()])


class ProtoSqlite:
    """Simple SqLite wrapper

    Attributes:

        name (str): The name of the database.
        lang (str): The language to translate to.
        check (bool): Whether to check if the thread is the same as the
            one that created the database.
    """
    __slots__ = "name", "conn", "cursor", "lang", "check"

    def __init__(
        self, name: Optional[str] = None,
        lang: Optional[str] = None,
        check: Optional[bool] = None,
    ) -> None:
        self.conn = None
        self.cursor = None
        self.lang = "en" if lang is None else lang
        self.check = False if check is None else check

        if name:
            self.open(name)
    
    def open(self, name: str) -> None:
        try:
            self.conn = sqlite3.connect(name, check_same_thread=self.check)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(_("Error connecting to  database:", lang=self.lang), e)
        
    def close(self) -> None:
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
    
    def create_table(self, table: str, columns=None, pk: str = None):
        if isinstance(columns, str):
            tmp = columns
        else:
            tmp = ""
            for var in cols(columns).split(","):
                if pk in var:
                    tmp += f"{var} PRIMARY KEY"
                else:
                    tmp += var
                tmp += ", "
            tmp = tmp[:-2]
        try:
            query = "CREATE TABLE IF NOT EXISTS {0} ({1});".format(table, tmp)
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(_("Error writing to database:", lang=self.lang), e)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get(self, table: str, columns: str, limit: int = None):
        query = "SELECT {0} from {1};".format(columns, table)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows[len(rows)-limit if limit else 0:]

    def get_pk(self, table: str) -> str:
        query = "SELECT * FROM {0};".format(table)
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def get_all(self, table: str) -> List[Tuple[Any, ...]]:
        query = "SELECT * from {0};".format(table)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_last(
        self, table: str, index: Any = None, value: Any = None,
    ) -> list:
        try:
            data = self.get(table, "*", limit=1)[0]
        except IndexError:
            data = value
        if index and data is not None:
            return data[index]
        return data

    def add(self, table: str, data: dict) -> None:
        if not isinstance(data, dict):
            print(_("'data' must be a dict instance", lang=self.lang))
        try:
            query = "INSERT INTO {0} ({1}) VALUES ({2});".format(
                table, ",".join(data.keys()), ",".join(["?"] * len(data))
            )
            self.cursor.execute(query, list(data.values()))
            self.conn.commit()
        except sqlite3.Error as e:
            print(_("Error writing to database:", lang=self.lang), e)

    def _delete(self, table: str, columns: str) -> None:
        try:
            query = "DELETE FROM {0} WHERE {1};".format(table, columns)
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(_("Error writing to database:", lang=self.lang), e)

    def delete(self, table: str, col:str, pk: str):
        self._delete(table, f"{col} = '{pk}'")

    # TODO: preventing sql injection
    def update(self, table:str, columns: str, condition: str) -> None:
        try:
            query = "UPDATE %s SET %s WHERE %s;" % (table, columns, condition)
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(_("Error writing to database:", lang=self.lang), e)

    def update_(self, table: str, columns: str, condition: str) -> None:
        try:
            query = "UPDATE {0} SET {1} WHERE {2};".format(
                table, columns, condition
            )
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(_("Error writing to database:", lang=self.lang), e)

    def query(self, sql: str) -> None:
        self.cursor.execute(sql)

    @staticmethod
    def summary(rows: Any) -> Any:
        cols = [[r[c] for r in rows] for c in range(len(rows[0]))]
        t = lambda col: "{:.1f}".format((len(rows) - col) / 6.0)
        ret = []
        for c in cols:
            hi = max(c)
            hi_t = t(c.index(hi))
            lo = min(c)
            lo_t = t(c.index(lo))
            avg = sum(c)/len(rows)
            ret.append(((hi,hi_t),(lo,lo_t),avg))
        return ret

    @staticmethod
    def to_csv(data, filename: str = "output.csv"):
        with open(filename, "w") as f:
            for row in data:
                f.write(",".join(str(x) for x in row) + "\n")

    @staticmethod
    def to_json(data, filename: str = "output.json"):
        print(data)
        with open(filename, "w") as f:
            json.dump(data, f)
    
    @staticmethod
    def to_txt(data, filename: str = "output.txt"):
        with open(filename, "w") as f:
            for row in data:
                f.write(", ".join(str(x) for x in row) + "\n")
