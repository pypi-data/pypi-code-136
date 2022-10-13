from abc import ABC, abstractmethod

class CommunityManager(ABC):
  @abstractmethod
  def create_profiles_after_strategy(self, *args):
    """
    This function should be implemented in a class which inherits from this one.
    The goal is to define how the profiles will be updated after the implemented strategy.
    For instance, when applying a load shifting approach, since the loads were sifthed, it is necessary to create new consumption profiles with this new load, in order to allow to compare it before and after applying the strategy.
    Hint: The consumption profiles should be copied to another folder, and then updated based on the new appliances schedule.

    Args:
      args: can have as many arguments as you want
    """
    pass

  @abstractmethod
  def execute(self, *args):
    """
    This function should be implemented in a class which inherits from this one.
    This goal is to define all the steps necessary to implement the provided strategy which will allow to do a good management of the renewable resources of the community.

    Args:
      args: can have as many arguments as you want
    """
    pass

