from typing import Any, Dict, Optional, Union

from sqlalchemy.engine.url import URL

from chalk.client.client_impl import ChalkConfigurationException
from chalk.integrations.named import load_integration_variable
from chalk.sql.base.sql_source import BaseSQLSource, TableIngestMixIn


class MySQLSourceImpl(BaseSQLSource, TableIngestMixIn):
    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[str] = None,
        db: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        name: Optional[str] = None,
    ):
        try:
            import pymysql
        except ModuleNotFoundError:
            raise ChalkConfigurationException.missing_dependency("chalkpy[mysql]")
        self.host = host or load_integration_variable(name="MYSQL_HOST", integration_name=name)
        self.port = port or load_integration_variable(name="MYSQL_TCP_PORT", integration_name=name)
        self.db = db or load_integration_variable(name="MYSQL_DATABASE", integration_name=name)
        self.user = user or load_integration_variable(name="MYSQL_USER", integration_name=name)
        self.password = password or load_integration_variable(name="MYSQL_PWD", integration_name=name)
        self.ingested_tables: Dict[str, Any] = {}
        super(MySQLSourceImpl, self).__init__()

    def local_engine_url(self) -> Union[str, URL]:
        return URL.create(
            drivername="mysql+pymysql",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.db,
        )
