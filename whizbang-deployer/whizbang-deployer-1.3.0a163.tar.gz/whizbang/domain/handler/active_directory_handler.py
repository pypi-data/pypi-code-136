from typing import List

from whizbang.config.app_config import AppConfig
from whizbang.domain.handler.handler_base import HandlerBase
from whizbang.domain.manager.az.az_active_directory_manager import AzActiveDirectoryManager
from whizbang.domain.models.active_directory.ad_group_member import AdGroupMember
from whizbang.domain.shared_types.account_type import AccountType


class ActiveDirectoryHandler(HandlerBase):
    def __init__(self, app_config: AppConfig, manager: AzActiveDirectoryManager):
        HandlerBase.__init__(self, app_config=app_config)
        self.manager = manager

    def get_object_id(self, account_type: AccountType, lookup_value: str) -> str:
        return self.manager.get_object_id(account_type=account_type, lookup_value=lookup_value)

    def get_display_name(self, object_id: str) -> str:
        return self.manager.get_display_name(object_id=object_id)

    def get_group_members(self, group_object_id: str) -> List[AdGroupMember]:
        return self.manager.get_group_members(group_object_id=group_object_id)

    def delete_service_principal(self, service_principal_id: str) -> None:
        self.manager.delete_service_principal(service_principal_id=service_principal_id)

    def delete_app_registration(self, app_registration_id: str) -> None:
        self.manager.delete_app_registration(app_registration_id=app_registration_id)
