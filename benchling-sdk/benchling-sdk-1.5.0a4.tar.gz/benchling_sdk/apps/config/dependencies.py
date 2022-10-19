from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, List, Optional, Tuple, Type, TypeVar, Union

from benchling_api_client.v2.alpha.extensions import UnknownType
from benchling_api_client.v2.alpha.models.app_config_item import AppConfigItem
from benchling_api_client.v2.alpha.models.boolean_app_config_item import BooleanAppConfigItem
from benchling_api_client.v2.alpha.models.date_app_config_item import DateAppConfigItem
from benchling_api_client.v2.alpha.models.datetime_app_config_item import DatetimeAppConfigItem
from benchling_api_client.v2.alpha.models.entity_schema_app_config_item import EntitySchemaAppConfigItem
from benchling_api_client.v2.alpha.models.field_app_config_item import FieldAppConfigItem
from benchling_api_client.v2.alpha.models.float_app_config_item import FloatAppConfigItem
from benchling_api_client.v2.alpha.models.generic_app_config_item import GenericAppConfigItem
from benchling_api_client.v2.alpha.models.integer_app_config_item import IntegerAppConfigItem
from benchling_api_client.v2.alpha.models.json_app_config_item import JsonAppConfigItem
from benchling_api_client.v2.alpha.models.secure_text_app_config_item import SecureTextAppConfigItem
from typing_extensions import Protocol

from benchling_sdk.apps.config.decryption_provider import BaseDecryptionProvider
from benchling_sdk.apps.config.scalars import (
    DEFAULT_SCALAR_DEFINITIONS,
    ScalarConfigItemType,
    ScalarDefinition,
    ScalarType,
)
from benchling_sdk.benchling import Benchling


class MissingDependencyError(Exception):
    """
    Missing dependency error.

    Indicates a dependency was missing from app config.
    For instance, no dependency with that name was in the list.
    """

    pass


class UnsupportedDependencyError(Exception):
    """
    Unsupported dependency error.

    The manifest and configuration specified a dependency which the SDK is incapable of handling yet.
    """

    pass


class MissingScalarDefinitionError(Exception):
    """
    Missing scalar definition error.

    The manifest and configuration specified a scalar type which the SDK does not know how to translate
    to Python values yet.
    """

    pass


ConfigItemPath = Tuple[str, ...]

# Everything from AppConfigItem except UnknownType
ConfigurationReference = Union[
    DateAppConfigItem,
    DatetimeAppConfigItem,
    JsonAppConfigItem,
    EntitySchemaAppConfigItem,
    FieldAppConfigItem,
    BooleanAppConfigItem,
    IntegerAppConfigItem,
    FloatAppConfigItem,
    GenericAppConfigItem,
    SecureTextAppConfigItem,
]

D = TypeVar("D", bound="BaseDependencies")


class ConfigProvider(Protocol):
    """
    Config provider.

    Provides a BenchlingAppConfiguration.
    """

    def config(self) -> List[ConfigurationReference]:
        """Implement to provide a Benchling app configuration."""
        ...


class BenchlingConfigProvider(ConfigProvider):
    """
    Benchling Config provider.

    Provides a BenchlingAppConfiguration retrieved from Benchling's API.
    """

    _client: Benchling
    _app_id: str

    def __init__(self, client: Benchling, app_id: str):
        """
        Initialize Benchling Config Provider.

        :param client: A configured Benchling instance for making API calls.
        :param app_id: The app_id from which to retrieve configuration.
        """
        self._client = client
        self._app_id = app_id

    def config(self) -> List[ConfigurationReference]:
        """Provide a Benchling app configuration from Benchling's APIs."""
        app_pages = self._client.v2.alpha.apps.list_app_configuration_items(
            app_id=self._app_id, page_size=100
        )

        # Eager load all config items for now since we don't yet have a way of lazily querying by path
        all_config_pages = list(app_pages)
        # Punt on UnknownType for now as apps using manifests with new types could lead to unpredictable results
        all_config_items = [
            _supported_config_item(config_item) for page in all_config_pages for config_item in page
        ]

        return all_config_items


class StaticConfigProvider(ConfigProvider):
    """
    Static Config provider.

    Provides a BenchlingAppConfiguration from a static declaration. Useful for mocking or testing.
    """

    _configuration_items: List[ConfigurationReference]

    def __init__(self, configuration_items: List[ConfigurationReference]):
        """
        Initialize Static Config Provider.

        :param configuration_items: The configuration items to return.
        """
        self._configuration_items = configuration_items

    def config(self) -> List[ConfigurationReference]:
        """Provide Benchling app configuration items from a static reference."""
        return self._configuration_items


class DependencyLinkStore(object):
    """
    Dependency Link Store.

    Marshalls an app configuration from the configuration provider into an indexable structure.
    Only retrieves app configuration once unless its cache is invalidated.
    """

    _configuration_provider: ConfigProvider
    _configuration: Optional[List[ConfigurationReference]] = None
    _configuration_map: Optional[Dict[ConfigItemPath, ConfigurationReference]] = None

    def __init__(self, configuration_provider: ConfigProvider):
        """
        Initialize Dependency Link Store.

        :param configuration_provider: A ConfigProvider that will be invoked to provide the
        underlying config from which to organize dependency links.
        """
        self._configuration_provider = configuration_provider

    @classmethod
    def from_app(cls, client: Benchling, app_id: str) -> DependencyLinkStore:
        """
        From App.

        Instantiate a DependencyLinkStore from an app_id and a configured Benchling instance. Preferred to
        using the class's constructor.
        """
        config_provider = BenchlingConfigProvider(client, app_id)
        return DependencyLinkStore(config_provider)

    @property
    def configuration(self) -> List[ConfigurationReference]:
        """
        Get the underlying configuration.

        Return the raw, stored configuration. Can be used if the provided accessors are inadequate
        to find particular configuration items.
        """
        if not self._configuration:
            self._configuration = self._configuration_provider.config()
        return self._configuration

    @property
    def configuration_path_map(self) -> Dict[ConfigItemPath, ConfigurationReference]:
        """
        Config links.

        Return a map of configuration item paths to their corresponding configuration items.
        """
        if not self._configuration_map:
            self._configuration_map = {tuple(item.path): item for item in self.configuration}
        return self._configuration_map

    def config_by_path(self, path: List[str]) -> Optional[ConfigurationReference]:
        """
        Config by path.

        Find an app config item by its exact path match, if it exists. Does not search partial paths.
        """
        # Since we eager load all config now, we know that missing path means it's not configured in Benchling
        # Later if we support lazy loading, we'll need to differentiate what's in our cache versus missing
        return self.configuration_path_map.get(tuple(path))

    def invalidate_cache(self) -> None:
        """
        Invalidate Cache.

        Will force retrieval of configuration from the ConfigProvider the next time the link store is accessed.
        """
        self._configuration = None
        self._configuration_map = None


class HasAppConfigItem(Protocol):
    """
    Has App Config Item.

    A mixin for typing to assert that a class has an optional app config item attribute.
    """

    @property
    def path(self) -> str:
        """Return the path requested by the manifest."""
        ...

    @property
    def config_item(self) -> Optional[ConfigurationReference]:
        """Return the underlying app config item, if present."""
        ...


class HasScalarDefinition(Protocol):
    """
    Has Scalar Definition.

    A mixin for typing to assert that a particular class has scalar attributes.
    """

    @property
    def path(self) -> str:
        """Return the path requested by the manifest."""
        ...

    @property
    def config_item(self) -> Optional[ConfigurationReference]:
        """Return the underlying app config item, if present."""
        ...

    @property
    def definition(self) -> Optional[ScalarDefinition]:
        """Return the scalar definition, allowing for conversion to Python types."""
        ...


class HasConfigWithDecryptionProvider(Protocol):
    """
    Has Config With Decryption Provider.

    A mixin for typing to assert that a particular class has a decryption provider and config.
    """

    @property
    def path(self) -> str:
        """Return the path requested by the manifest."""
        ...

    @property
    def config_item(self) -> Optional[ConfigurationReference]:
        """Return the underlying app config item, if present."""
        ...

    @property
    def decryption_provider(self) -> Optional[BaseDecryptionProvider]:
        """Return the decryption provider."""
        ...


class RequiredValueMixin:
    """
    Required Value Mixin.

    A mixin for accessing a value which is required and should always be present. Should
    only be mixed in with HasAppConfigItem or another class that provides the `self.config_item` attribute.
    """

    @property
    def value(self: HasAppConfigItem) -> str:
        """Return the value of the app config item."""
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        return str(self.config_item.value)


class RequiredScalarDependencyMixin(Generic[ScalarType]):
    """
    Require Scalar Config.

    A mixin for accessing a scalar config which is required and should always be present.
    Should only be mixed in with ScalarConfig.
    """

    @property
    def value(self: HasScalarDefinition) -> ScalarType:
        """Return the value of the scalar."""
        if self.definition:
            assert (
                self.config_item is not None and self.config_item.value is not None
            ), f"The app config item {self.path} is not set in Benchling"
            optional_typed_value = self.definition.from_str(value=str(self.config_item.value))
            assert optional_typed_value is not None
            return optional_typed_value
        raise MissingScalarDefinitionError(f"No definition registered for scalar config {self.path}")

    @property
    def value_str(self: HasScalarDefinition) -> str:
        """Return the value of the scalar as a string."""
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        # Booleans are currently specified as str in the spec but are bool at runtime in JSON
        return str(self.config_item.value)


class RequiredSecureTextDependencyMixin(RequiredScalarDependencyMixin[str]):
    """
    Require Secure Text.

    A mixin for accessing a secure text config which is required and should always be present.
    Should only be mixed in with SecureTextConfig.
    """

    def decrypted_value(self: HasConfigWithDecryptionProvider) -> str:
        """
        Decrypted value.

        Decrypts a secure_text dependency's encrypted value into plain text.
        """
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        assert (
            self.decryption_provider is not None
        ), f"The app config item {self.config_item} cannot be decrypted because no DecryptionProvider was set"
        return self.decryption_provider.decrypt(str(self.config_item.value))


@dataclass
class BaseConfigItem:
    """
    Base Config Item.

    The shared set of properties for all config items.
    """

    config_item: Optional[ConfigurationReference]


@dataclass
class ParentConfigItem(BaseConfigItem):
    """
    Parent Config Item.

    A parent config item which may have subdependencies that require context.
    """

    config_context: BaseDependencies


@dataclass
class ConfigItemContainer:
    """
    Config Item Container.

    Does not correspond to a linked app config item. Holds context passed from linked items.
    """

    parent_config: ParentConfigItem


@dataclass
class ScalarConfigItem(BaseConfigItem):
    """
    Scalar Config Item.

    Scalars are values that can be represented outside the Benchling domain.
    """

    definition: Optional[ScalarDefinition]


@dataclass
class SecureTextDependency(ScalarConfigItem):
    """
    SecureText Config.

    A dependency for accessing a secure_text config.
    """

    # This is declared Optional because a decryption provider is not required until attempting
    # to decrypt a value.
    decryption_provider: Optional[BaseDecryptionProvider]


class BaseDependencies:
    """
    A base class for implementing dependencies.

    Used as a facade for the underlying link store, which holds dependency links configured in Benchling.
    """

    _store: DependencyLinkStore
    _scalar_definitions: Dict[ScalarConfigItemType, ScalarDefinition]
    _unknown_scalar_definition: Optional[ScalarDefinition]
    # Will be required at runtime if an app attempts to decrypt a secure_text config
    _decryption_provider: Optional[BaseDecryptionProvider]

    def __init__(
        self,
        store: DependencyLinkStore,
        scalar_definitions: Dict[ScalarConfigItemType, ScalarDefinition] = DEFAULT_SCALAR_DEFINITIONS,
        unknown_scalar_definition: Optional[ScalarDefinition] = None,
        decryption_provider: Optional[BaseDecryptionProvider] = None,
    ):
        """
        Initialize Base Dependencies.

        :param store: The dependency link store to source dependency links from.
        :param scalar_definitions: A map of scalar types from the API definitions to ScalarDefinitions which
        determines how we want map them to concrete Python types and values. Can be overridden to customize
        deserialization behavior or formatting.
        :param unknown_scalar_definition: A scalar definition for handling unknown scalar types from the API. Can be
        used to control behavior for forwards compatibility with new types the SDK does not yet support (e.g.,
        by treating them as strings).
        :param decryption_provider: A decryption provider that can decrypt secrets from app config. If
        dependencies attempt to use a secure_text's decrypted value, a decryption_provider must be specified.
        """
        self._store = store
        self._scalar_definitions = scalar_definitions
        self._unknown_scalar_definition = unknown_scalar_definition
        self._decryption_provider = decryption_provider

    @classmethod
    def from_app(
        cls: Type[D],
        client: Benchling,
        app_id: str,
        decryption_provider: Optional[BaseDecryptionProvider] = None,
    ) -> D:
        """Initialize dependencies from an app_id."""
        link_store = DependencyLinkStore.from_app(client=client, app_id=app_id)
        return cls(link_store, decryption_provider=decryption_provider)

    def invalidate_cache(self) -> None:
        """Invalidate the cache of dependency links and force an update."""
        self._store.invalidate_cache()


def _supported_config_item(config_item: AppConfigItem) -> ConfigurationReference:
    if isinstance(config_item, UnknownType):
        raise UnsupportedDependencyError(
            f"Unable to read app configuration with unsupported type: {config_item}"
        )
    return config_item
