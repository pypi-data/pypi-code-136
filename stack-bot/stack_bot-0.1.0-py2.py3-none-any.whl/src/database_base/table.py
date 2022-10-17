import ydb
from typing import List, Generic, TypeVar, Type, Callable, Dict

from stack_bot.src.database_base.driver import Driver
from stack_bot.src.database_base.table_row import TableRow

tablesState = {}

T = TypeVar("T", bound='TableRow')


class Table(Generic[T]):

    def __init__(self, driver: Driver, name: str, member_class: Type[T]):
        self.driver = driver
        self.name = name
        self.member_class = member_class

        tablesState[member_class] = self

    def update_credentials(self, get_new_token=False):
        self.driver.update_credentials(get_new_token=get_new_token)

    R = TypeVar('R')

    def __execute(self, function: Callable[[ydb.Session], R]) -> R:
        return self.driver.pool.retry_operation_sync(function)

    def __create_table(self, session: ydb.Session):
        def to_columns(table_row_type: Type[TableRow]) -> List[ydb.Column]:
            primary_key = table_row_type.primary_key()

            columns = []

            for (k, t) in table_row_type.get_columns().items():
                if k == primary_key:
                    columns.append(ydb.Column(k, ydb.OptionalType(ydb.PrimitiveType.Uint64)))
                else:
                    column_type = ydb.PrimitiveType.Json

                    if t == int: column_type = ydb.PrimitiveType.Int32
                    if t == float: column_type = ydb.PrimitiveType.Float
                    if t == bool: column_type = ydb.PrimitiveType.Bool
                    if t == str: column_type = ydb.PrimitiveType.String

                    columns.append(ydb.Column(k, ydb.OptionalType(column_type)))

            return columns

        session.create_table(
            path=self.driver.database + "/" + self.name,
            table_description= \
                ydb.TableDescription() \
                    .with_primary_key(self.member_class.primary_key())
                    .with_columns(
                    *to_columns(self.member_class)
                )
        )

    def __select(self, session: ydb.Session, condition: str = None) -> List[T]:
        result_sets = session \
            .transaction(ydb.SerializableReadWrite()) \
            .execute(
                query=
                """
                    PRAGMA TablePathPrefix("{}");
                    SELECT
                        *
                    FROM {}{}
                    """.format(
                    self.driver.database,
                    self.name,
                    "" if condition is None else " WHERE " + condition
                ),
                commit_tx=True,
            )

        results = []
        for row in result_sets[0].rows:
            obj = self.member_class
            columns = {}
            for column in obj.get_columns():
                if type(row[column]) is bytes:
                    columns[column] = row[column].decode('utf-8')
                else:
                    columns[column] = row[column]
            results.append(obj(**columns))

        return results

    def __size(self, session: ydb.Session) -> int:
        result_sets = session.transaction(ydb.SerializableReadWrite()).execute(
            """
            PRAGMA TablePathPrefix("{}");
            SELECT
                1
            FROM {}
            """.format(
                self.driver.database,
                self.name
            ),
            commit_tx=True,
        )
        results = 0
        for _ in result_sets[0].rows:
            results += 1

        return results

    def __upsert(self, element: T, session: ydb.Session) -> None:

        def to_str(s):
            if s is None:
                return "null"
            elif type(s) == str:
                return "\"" + s + "\""
            else:
                return str(s)

        query = """
            PRAGMA TablePathPrefix("{}");
            UPSERT INTO {} ({}) VALUES
                ({})
            """.format(
            self.driver.database,
            self.name,
            ",".join(list(element.get_columns().keys())),
            ",".join(list(map(to_str, element.values())))
        )

        session.transaction(ydb.SerializableReadWrite()).execute(
            query,
            commit_tx=True,
        )

    def __update(self, session: ydb.Session, field_changes: str, condition: str = None) -> None:

        query = """
            PRAGMA TablePathPrefix("{}");
            UPDATE {}
            SET {}
            {}
            """.format(
            self.driver.database,
            self.name,
            field_changes,
            "WHERE " + condition if condition else ""
        )

        session.transaction(ydb.SerializableReadWrite()).execute(
            query,
            commit_tx=True,
        )

    def __insert(self, session: ydb.Session, columns: str, values: str) -> None:

        query = """
            PRAGMA TablePathPrefix("{}");
            INSERT INTO {} {}
            VALUES {}
            """.format(
            self.driver.database,
            self.name,
            columns,
            values
        )

        session.transaction(ydb.SerializableReadWrite()).execute(
            query,
            commit_tx=True,
        )

    def __delete(self, session: ydb.Session, condition: str = None) -> None:

        query = """
            PRAGMA TablePathPrefix("{}");
            DELETE FROM {}
            {}
            """.format(
            self.driver.database,
            self.name,
            "WHERE " + condition if condition else ""
        )

        session.transaction(ydb.SerializableReadWrite()).execute(
            query,
            commit_tx=True,
        )

    def create_table(self) -> None:
        return self.__execute(lambda s: self.__create_table(s))

    def select(self, condition: str = None) -> List[T]:
        return self.__execute(lambda s: self.__select(s, condition))

    def size(self) -> int:
        return self.__execute(lambda s: self.__size(s))

    def upsert(self, element: T):
        self.__execute(lambda s: self.__upsert(element, s))

    def update(self, field_changes: str, condition: str = None):
        self.__execute(lambda s: self.__update(s, field_changes, condition))

    def insert(self, columns: str, values: str):
        self.__execute(lambda s: self.__insert(s, columns, values))

    def delete(self, condition: str = None):
        self.__execute(lambda s: self.__delete(s, condition))


class Condition:

    @staticmethod
    def IN(column: str, values: List[str]):
        return f"{column} IN ({','.join(values)})"

    @staticmethod
    def AND(conditions: List[str]):
        return " AND ".join(conditions)

    @staticmethod
    def OR(conditions: List[str]):
        return " OR ".join(conditions)

    @staticmethod
    def EQ(column: str, value):
        if type(value) is str:
            return f'{column} = "{value}"'
        else:
            return f'{column} = {value}'
