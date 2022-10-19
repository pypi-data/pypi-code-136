from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CockroachCloudEditDatabaseUpdateDatabaseRequest")


@attr.s(auto_attribs=True)
class CockroachCloudEditDatabaseUpdateDatabaseRequest:
    """
    Example:
        {'new_name': 'example_new_database_name'}

    Attributes:
        name (str):
        new_name (str):
    """

    name: str
    new_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "new_name": new_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        new_name = d.pop("new_name")

        cockroach_cloud_edit_database_update_database_request = cls(
            name=name,
            new_name=new_name,
        )

        cockroach_cloud_edit_database_update_database_request.additional_properties = d
        return cockroach_cloud_edit_database_update_database_request

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
