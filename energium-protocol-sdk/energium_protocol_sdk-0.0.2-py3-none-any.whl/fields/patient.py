from energium_protocol_sdk.fields.base import EnergiumField


class Id(EnergiumField, str):
    code = "PI"


class Name(EnergiumField, str):
    code = "PN"


class Sex(EnergiumField, str):
    code = "PS"


class Age(EnergiumField, str):
    code = "PA"


class Room(EnergiumField, str):
    code = "PR"
