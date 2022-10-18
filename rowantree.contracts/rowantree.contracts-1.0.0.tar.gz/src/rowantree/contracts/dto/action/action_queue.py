""" Command Queue Definition """

from ..base_model import BaseModel
from .action import Action


class ActionQueue(BaseModel):
    """
    Command Queue DTO
    Used to hold a list of Actions (commands)

    TODO: this needs to move to a more loosely couple solution even though this is temporary...

    Attributes
    ----------
    queue: list[Action]
        A list of Actions.
    """

    queue: list[Action]
