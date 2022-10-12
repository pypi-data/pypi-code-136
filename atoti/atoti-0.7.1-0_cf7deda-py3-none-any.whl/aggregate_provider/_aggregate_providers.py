from typing import Callable, Dict, Iterable, Mapping, Optional

from .._aggregate_provider_description import AggregateProviderDescription
from .._delegate_mutable_mapping import DelegateMutableMapping
from .._java_api import JavaApi
from .aggregate_provider import AggregateProvider


class AggregateProviders(DelegateMutableMapping[str, AggregateProvider]):
    def __init__(
        self,
        *,
        cube_name: str,
        get_aggregate_provider: Callable[
            [AggregateProviderDescription], AggregateProvider
        ],
        java_api: JavaApi,
    ):
        self._java_api = java_api
        self._cube_name = cube_name
        self._description_to_provider = get_aggregate_provider

    def _delete_keys(self, keys: Optional[Iterable[str]] = None, /) -> None:
        self._java_api.remove_aggregate_providers(keys, cube_name=self._cube_name)
        self._java_api.refresh()

    def _update(self, other: Mapping[str, AggregateProvider]) -> None:
        self._java_api.add_aggregate_providers(
            {key: value._description for key, value in other.items()},
            cube_name=self._cube_name,
        )
        self._java_api.refresh()

    def __setitem__(self, key: str, value: AggregateProvider) -> None:
        self._update({key: value})

    def _get_underlying(self) -> Dict[str, AggregateProvider]:
        return {
            name: self._description_to_provider(description)
            for (
                name,
                description,
            ) in self._java_api.get_aggregate_providers_attributes(
                self._cube_name
            ).items()
        }
