# imports for nicer calling of cinnaroll, cinnaroll.rollout() instead of cinnaroll.rollout.rollout()
# and cinnaroll.RolloutConfig instead of cinnaroll.rollout.RolloutConfig
from cinnaroll_internal.rollout import rollout
from cinnaroll_internal.rollout_config import RolloutConfig
from cinnaroll_internal.environment_check import check_environment

check_environment()

# todo: https://appdividend.com/2021/05/09/what-is-python-__all__-and-how-to-use-it/
