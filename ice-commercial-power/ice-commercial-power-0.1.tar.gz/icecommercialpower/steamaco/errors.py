"""
Defines errors raised when integrating with SteamaCo API
"""


class ObtainTokenError(Exception):
    """
    Error in case getting token fails
    """


class CreateTransactionError(Exception):
    """
    An error occurred while creating a transaction.
    """
