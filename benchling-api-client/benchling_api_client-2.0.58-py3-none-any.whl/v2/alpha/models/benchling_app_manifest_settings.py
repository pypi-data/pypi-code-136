from typing import Any, cast, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..extensions import NotPresentError
from ..models.benchling_app_manifest_settings_lifecycle_management import (
    BenchlingAppManifestSettingsLifecycleManagement,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BenchlingAppManifestSettings")


@attr.s(auto_attribs=True, repr=False)
class BenchlingAppManifestSettings:
    """  """

    _lifecycle_management: Union[Unset, BenchlingAppManifestSettingsLifecycleManagement] = UNSET
    _webhook_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def __repr__(self):
        fields = []
        fields.append("lifecycle_management={}".format(repr(self._lifecycle_management)))
        fields.append("webhook_url={}".format(repr(self._webhook_url)))
        fields.append("additional_properties={}".format(repr(self.additional_properties)))
        return "BenchlingAppManifestSettings({})".format(", ".join(fields))

    def to_dict(self) -> Dict[str, Any]:
        lifecycle_management: Union[Unset, int] = UNSET
        if not isinstance(self._lifecycle_management, Unset):
            lifecycle_management = self._lifecycle_management.value

        webhook_url = self._webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        # Allow the model to serialize even if it was created outside of the constructor, circumventing validation
        if lifecycle_management is not UNSET:
            field_dict["lifecycleManagement"] = lifecycle_management
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any], strict: bool = False) -> T:
        d = src_dict.copy()

        def get_lifecycle_management() -> Union[Unset, BenchlingAppManifestSettingsLifecycleManagement]:
            lifecycle_management = UNSET
            _lifecycle_management = d.pop("lifecycleManagement")
            if _lifecycle_management is not None and _lifecycle_management is not UNSET:
                try:
                    lifecycle_management = BenchlingAppManifestSettingsLifecycleManagement(
                        _lifecycle_management
                    )
                except ValueError:
                    lifecycle_management = BenchlingAppManifestSettingsLifecycleManagement.of_unknown(
                        _lifecycle_management
                    )

            return lifecycle_management

        try:
            lifecycle_management = get_lifecycle_management()
        except KeyError:
            if strict:
                raise
            lifecycle_management = cast(Union[Unset, BenchlingAppManifestSettingsLifecycleManagement], UNSET)

        def get_webhook_url() -> Union[Unset, str]:
            webhook_url = d.pop("webhookUrl")
            return webhook_url

        try:
            webhook_url = get_webhook_url()
        except KeyError:
            if strict:
                raise
            webhook_url = cast(Union[Unset, str], UNSET)

        benchling_app_manifest_settings = cls(
            lifecycle_management=lifecycle_management,
            webhook_url=webhook_url,
        )

        benchling_app_manifest_settings.additional_properties = d
        return benchling_app_manifest_settings

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

    def get(self, key, default=None) -> Optional[Any]:
        return self.additional_properties.get(key, default)

    @property
    def lifecycle_management(self) -> BenchlingAppManifestSettingsLifecycleManagement:
        """Specify whether app will be activated automatically or manually. If automatic is specified, a webhook url is required."""
        if isinstance(self._lifecycle_management, Unset):
            raise NotPresentError(self, "lifecycle_management")
        return self._lifecycle_management

    @lifecycle_management.setter
    def lifecycle_management(self, value: BenchlingAppManifestSettingsLifecycleManagement) -> None:
        self._lifecycle_management = value

    @lifecycle_management.deleter
    def lifecycle_management(self) -> None:
        self._lifecycle_management = UNSET

    @property
    def webhook_url(self) -> str:
        """URL that Benchling sends app interaction payloads to. This destination should be backed by an endpoint owned by your application."""
        if isinstance(self._webhook_url, Unset):
            raise NotPresentError(self, "webhook_url")
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, value: str) -> None:
        self._webhook_url = value

    @webhook_url.deleter
    def webhook_url(self) -> None:
        self._webhook_url = UNSET
