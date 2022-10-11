from enum import Enum


class AccountType(Enum):
    OBJECTID = "objectid"
    EMAIL = "email"
    GROUP = "group"
    SERVICEPRINCIPAL = "serviceprincipal"
    APPREGISTRATION = "appregistration"
    SELF = "self"

