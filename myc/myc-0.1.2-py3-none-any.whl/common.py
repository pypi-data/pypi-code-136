import os
from typing import Optional, List

from myc.build import is_building
from myc.endpoint import PlatformKind


SERVICE_ENV_VAR = 'MYC_SERVICE__'

CURRENT_PLATFORM_OVERRIDE: List[Optional[PlatformKind]] = [None]


def determine_current_platform() -> PlatformKind:
    """
    Determines the platform of the caller.
    """
    if CURRENT_PLATFORM_OVERRIDE[0] is not None:
        return CURRENT_PLATFORM_OVERRIDE[0]

    from myc.awslambda import have_aws_lambda_runtime
    if have_aws_lambda_runtime:
        return PlatformKind.AWS_LAMBDA
    elif is_building[0]:
        return PlatformKind.BUILD
    else:
        return PlatformKind.UNKNOWN


def get_current_service() -> str:
    return os.environ[SERVICE_ENV_VAR]


def set_current_platform(platform: PlatformKind):
    CURRENT_PLATFORM_OVERRIDE[0] = platform
