from typing import Optional
from dataclasses import dataclass
from enum import Enum


class KeyType(str, Enum):
    function_call = "FunctionCall"
    full_access = "FullAccess"


@dataclass
class KeyInfo:
    public_key: str
    key_type: KeyType
    receiver_id: Optional[str]

    @classmethod
    def from_key(cls, key: dict):
        public_key = key["public_key"]
        permission = key["access_key"]["permission"]
        if "FunctionCall" in permission:
            return cls(
                public_key=public_key,
                key_type=KeyType.function_call,
                receiver_id=permission["FunctionCall"].get("receiver_id")
            )
        return cls(
            public_key=public_key,
            key_type=KeyType.full_access,
            receiver_id=None
        )


@dataclass
class VerificationResult:
    success: bool
    key_info: Optional[KeyInfo]

    @classmethod
    @property       # This is no longer valid from 3.11; See version notes here: https://docs.python.org/3.11/library/functions.html#classmethod
    def failed(cls):
        return cls(False, None)

    @classmethod
    def with_key_info(cls, key_info: KeyInfo):
        return cls(True, key_info)
