from email import message_from_bytes, message_from_string
from email.message import Message


class Email(Message):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> Message:
        try:
            if isinstance(v, str):
                return message_from_string(v)
            elif isinstance(v, bytes):
                return message_from_bytes(v)
        except Exception as e:
            raise ValueError("invalid format.") from e

        if not isinstance(v, Message):
            raise ValueError("invalid format.")

        return v
