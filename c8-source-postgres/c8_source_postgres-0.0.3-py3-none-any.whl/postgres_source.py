"""GDN data connector source for Postgres."""
import pkg_resources
from c8connector import C8Connector
from c8connector import ConfigProperty


class PostgresSourceConnector(C8Connector):
    """PostgresSourceConnector's C8Connector impl."""

    def name(self) -> str:
        """Returns the name of the connector."""
        return "postgres"

    def package_name(self) -> str:
        """Returns the package name of the connector (i.e. PyPi package name)."""
        return "c8-source-postgres"

    def version(self) -> str:
        """Returns the version of the connector."""
        return pkg_resources.get_distribution('c8_source_postgres').version

    def type(self) -> str:
        """Returns the type of the connector."""
        return "source"

    def description(self) -> str:
        """Returns the description of the connector."""
        return "GDN data connector source for Postgres"

    def validate(self, integration: dict) -> bool:
        """Validate given configurations against the connector."""
        return True

    def samples(self, integration: dict) -> list:
        """Fetch sample data using the provided configurations."""
        return []

    def config(self) -> list[ConfigProperty]:
        """Get configuration parameters for the connector."""
        return [
            ConfigProperty('host', 'string', True),
            ConfigProperty('port', 'integer', True),
            ConfigProperty('user', 'string', True),
            ConfigProperty('password', 'string', True),
            ConfigProperty('dbname', 'string', True),
            ConfigProperty('filter_schemas', 'string', False),
            ConfigProperty('ssl', 'string', False),
            ConfigProperty('logical_poll_total_seconds', 'integer', False),
            ConfigProperty('break_at_end_lsn', 'boolean', False),
            ConfigProperty('max_run_seconds', 'integer', False),
            ConfigProperty('debug_lsn', 'string', False),
            ConfigProperty('tap_id', 'string', False),
            ConfigProperty('itersize', 'integer', False),
            ConfigProperty('default_replication_method', 'string', False),
            ConfigProperty('use_secondary', 'boolean', False),
            ConfigProperty('secondary_host', 'string', False),
            ConfigProperty('secondary_port', 'integer', False),
        ]

    def capabilities(self) -> list[str]:
        """Return the capabilities[1] of the connector.
        [1] https://docs.meltano.com/contribute/plugins#how-to-test-a-tap
        """
        return ['catalog', 'discover', 'state']
