# std
from typing import Optional as Opt


class TierException(Exception):
    pass


class TierDryRunException(TierException):
    pass


class TierValidationException(Exception):

    @classmethod
    def expect(
            cls,
            condition: bool,
            msg: str,
            exception_type: Opt[type(TierException)] = None,
    ):
        if not condition:
            if exception_type is None:
                raise TierValidationException(msg)
            else:
                raise exception_type(msg)


class TierVersionError(TierException, ValueError):
    pass


def expect(
        condition: bool,
        msg: str,
        exception_type: Opt[type(TierException)] = None,
):
    TierValidationException.expect(condition, msg, exception_type)
