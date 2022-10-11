from typing import List

from whizbang.domain.manager.az.az_manager_base import AzManagerBase
from whizbang.domain.models.active_directory.ad_group_member import AdGroupMember
from whizbang.domain.repository.az.az_active_directory_repository import IAzActiveDirectoryRepository
from whizbang.domain.shared_types.account_type import AccountType


class AzActiveDirectoryManager(AzManagerBase):
    def __init__(self, repository: IAzActiveDirectoryRepository):
        AzManagerBase.__init__(self, repository)
        self._repository: IAzActiveDirectoryRepository

    def get_object_id(self, account_type: AccountType, lookup_value: str) -> str:
        lookup_type = account_type.value
        return self._repository.get_object_id(lookup_type=lookup_type, lookup_value=lookup_value)

    def get_display_name(self, object_id: str) -> str:
        return self._repository.get_display_name(object_id=object_id)

    def get_group_members(self, group_object_id: str) -> List[AdGroupMember]:
        return self._repository.get_group_members(group_object_id=group_object_id)

    def delete_service_principal(self, service_principal_id: str) -> None:
        self._repository.delete_service_principal(service_principal_id=service_principal_id)

    def delete_app_registration(self, app_registration_id: str) -> None:
        self._repository.delete_app_registration(app_registration_id=app_registration_id)
