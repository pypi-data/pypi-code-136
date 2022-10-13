from typing import Optional, overload

from sqlalchemy.engine.url import URL

from chalk.client.client_impl import ChalkConfigurationException
from chalk.integrations.named import load_integration_variable
from chalk.sql.base.sql_source import BaseSQLSource


class SnowflakeSource(BaseSQLSource):
    @overload
    def __init__(self, name: str):
        ...

    @overload
    def __init__(self, account_identifier: str, warehouse: str, user: str, password: str, db: str, schema: str):
        ...

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        account_identifier: Optional[str] = None,
        warehouse: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        db: Optional[str] = None,
        schema: Optional[str] = None,
        role: Optional[str] = None,
    ):
        try:
            import snowflake  # noqa
            import snowflake.sqlalchemy  # noqa
        except ModuleNotFoundError:
            raise ChalkConfigurationException(
                "Missing 'chalkpy[snowflake]' pip dependency."
                " Please add 'chalkpy[snowflake]' to your requirements.txt and `pip install`."
            )

        self.account_identifier = account_identifier or load_integration_variable(
            integration_name=name, name="SNOWFLAKE_ACCOUNT_ID"
        )
        self.warehouse = warehouse or load_integration_variable(integration_name=name, name="SNOWFLAKE_WAREHOUSE")
        self.user = user or load_integration_variable(integration_name=name, name="SNOWFLAKE_USER")
        self.password = password or load_integration_variable(integration_name=name, name="SNOWFLAKE_PASSWORD")
        self.db = db or load_integration_variable(integration_name=name, name="SNOWFLAKE_DATABASE")
        self.schema = schema or load_integration_variable(integration_name=name, name="SNOWFLAKE_SCHEMA")
        self.role = role or load_integration_variable(integration_name=name, name="SNOWFLAKE_ROLE")

        super(SnowflakeSource, self).__init__()

    def local_engine_url(self) -> URL:
        query = {
            k: v
            for k, v in (
                {
                    "database": self.db,
                    "schema": self.schema,
                    "warehouse": self.warehouse,
                    "role": self.role,
                }
            ).items()
            if v is not None
        }
        return URL.create(
            drivername="snowflake",
            username=self.user,
            password=self.password,
            host=self.account_identifier,
            query=query,
        )
