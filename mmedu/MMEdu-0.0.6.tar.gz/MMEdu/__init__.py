from .Classification import MMClassification
from .Detection import MMDetection
# from .Generation_Edu import MMGeneration
from .Pose import MMPose
# from .Base_Edu import MMBase
from .version import __version__,__path__

__all__ = [
    'MMClassification',
    'MMDetection',
    'MMPose',
    '__version__',
    '__path__',
    # 'MMGeneration',
    # 'MMBase',
]
