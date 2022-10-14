from cooptools.coopEnum import CoopEnum
from dataclasses import dataclass

class DataBaseType(CoopEnum):
    MYSQL = 'mssql'
    SQLSERVER = 'mssql'

class DataBaseConnector(CoopEnum):
    PYODBC = 'pyodbc'

@dataclass
class DbConnectionArgs:
    db_type: DataBaseType
    db_connector: DataBaseConnector
    server_name: str
    db_name: str
    port: int = None
    trusted_connection: bool = True
    driver: str = "ODBC+Driver+17+for+SQL+Server"
    user: str = None
    pw: str = None

    def sqlalchemy_db_connection_string(self, echo: bool = False):

        up_txt = ""
        if not self.trusted_connection:
            if self.user is None or self.pw is None:
                raise ValueError("User and password cannot be None when it is not a trusted connection")
            up_txt = f"{self.user}:{self.pw}"

        trusted_txt = "?TrustedConnection=yes" if self.trusted_connection else ""

        server_txt = f"{self.server_name}:{self.port}" if self.port else f"{self.server_name}"

        driver = self.driver.replace(" ", "+")

        conn_str = f"{self.db_type.value}+{self.db_connector.value}://{up_txt}@{server_txt}/{self.db_name}?driver={driver}{trusted_txt}"

        if echo:
            print(conn_str)

        return conn_str