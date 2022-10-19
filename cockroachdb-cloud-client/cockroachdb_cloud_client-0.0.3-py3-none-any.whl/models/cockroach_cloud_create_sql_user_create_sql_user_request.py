from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CockroachCloudCreateSQLUserCreateSQLUserRequest")


@attr.s(auto_attribs=True)
class CockroachCloudCreateSQLUserCreateSQLUserRequest:
    """
    Example:
        {'name': 'example_username', 'password': 'example_password'}

    Attributes:
        name (str):
        password (str):
    """

    name: str
    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        password = d.pop("password")

        cockroach_cloud_create_sql_user_create_sql_user_request = cls(
            name=name,
            password=password,
        )

        cockroach_cloud_create_sql_user_create_sql_user_request.additional_properties = d
        return cockroach_cloud_create_sql_user_create_sql_user_request

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
