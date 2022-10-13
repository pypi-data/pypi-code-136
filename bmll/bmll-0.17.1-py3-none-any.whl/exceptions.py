

class AuthenticationError(Exception):
    """The service was unable to authenticate."""
    pass


class LoginError(Exception):
    """An error has occurred when attempting to login to the BMLL Services."""
    pass


class MarketDataError(Exception):
    """Failed to retrieve market data."""
    pass


class RequestTooLarge(Exception):
    """Request content length is too large, the size of the query should be reduced."""


class QuotaReachedError(Exception):
    """User has reached their quota and got a 429 status code."""
