from enum import Enum, unique


@unique
class NotificationEvents(Enum):
    USER_INVITED = "user_invited"
    TABLE_OWNER_ASSIGNED = "table_owner_assigned"

