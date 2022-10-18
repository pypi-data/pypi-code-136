""" Command Queue Action Definition """
from ..base_model import BaseModel


class Action(BaseModel):
    """
    Action DTO
    This DTO defines the command queue action.

    TODO: this needs to move to a more loosely couple solution even though this is temporary...

    Attributes
    ----------
    name: str
        The name of the command (stored procedure name)
    arguments: list
        The arguments to pass to the command.
    """

    name: str
    arguments: list
