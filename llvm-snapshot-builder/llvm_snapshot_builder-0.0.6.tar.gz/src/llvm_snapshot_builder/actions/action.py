"""
CoprAction
"""

from abc import ABC, abstractmethod


class CoprAction(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    """ Defines what a CoprAction needs to implement """
    @abstractmethod
    def run(self) -> bool:
        """ Runs the action. """
        pass
