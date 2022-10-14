"""GDN data connector target for C8 collections."""
import pkg_resources
from c8connector import C8Connector
from c8connector import ConfigProperty


class C8CollectionTargetConnector(C8Connector):
    """C8CollectionTargetConnector's C8Connector impl."""

    def name(self) -> str:
        """Returns the name of the connector."""
        return "c8collection"

    def package_name(self) -> str:
        """Returns the package name of the connector (i.e. PyPi package name)."""
        return "c8-target-c8collection"

    def version(self) -> str:
        """Returns the version of the connector."""
        return pkg_resources.get_distribution('c8_target_c8collection').version

    def type(self) -> str:
        """Returns the type of the connector."""
        return "target"

    def description(self) -> str:
        """Returns the description of the connector."""
        return "GDN data connector target for C8 Collections"

    def validate(self, integration: dict) -> bool:
        """Validate given configurations against the connector."""
        return True

    def samples(self, integration: dict) -> list:
        """Fetch sample data using the provided configurations."""
        return []

    def config(self) -> list[ConfigProperty]:
        """Get configuration parameters for the connector."""
        return [
            ConfigProperty('email', 'string', True),
            ConfigProperty('password', 'string', True),
            ConfigProperty('region', 'string', True),
            ConfigProperty('fabric', 'string', True),
            ConfigProperty('tenant', 'string', True),
            ConfigProperty('target_collection', 'string', True),
            ConfigProperty('schemas', 'string', True),
        ]

    def capabilities(self) -> list[str]:
        """Return the capabilities[1] of the connector.
        [1] https://docs.meltano.com/contribute/plugins#how-to-test-a-tap
        """
        return []
