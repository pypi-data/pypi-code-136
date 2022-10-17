from energium_protocol_sdk.fields.base import EnergiumField


class SpecimenNumber(EnergiumField, str):
    code = "TS"


class TubeCode(EnergiumField, str):
    code = "TC"


class TubeName(EnergiumField, str):
    code = "TN"


class TubeCount(EnergiumField, str):
    code = "TP"


class SpecimenName(EnergiumField, str):
    code = "TN"
