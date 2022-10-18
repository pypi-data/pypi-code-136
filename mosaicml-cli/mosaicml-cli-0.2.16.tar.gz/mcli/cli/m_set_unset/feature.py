""" mcli modify feature flags functions """
import logging
from typing import Optional

from mcli import config
from mcli.config import MESSAGE, MCLIConfigError
from mcli.utils.utils_interactive import choose_one
from mcli.utils.utils_logging import FAIL, OK, err_console

logger = logging.getLogger(__name__)


def modify_feature_flag(feature: Optional[str], activate: bool = True, **kwargs) -> int:
    del kwargs
    try:
        conf = config.MCLIConfig.load_config()
    except MCLIConfigError:
        err_console.print(MESSAGE.MCLI_NOT_INITIALIZED)
        return 1
    available_features = list(config.FeatureFlag)
    available_features_str = [x.value for x in available_features]
    feature_flag: Optional[config.FeatureFlag] = None
    if feature:
        feature = feature.upper()
        if feature not in available_features_str:
            logger.error(f'{FAIL} Unable to find feature flag: {feature}')
        else:
            feature_flag = config.FeatureFlag[feature]
    if feature_flag is None:
        feature_flag = choose_one(
            f'Which feature would you like to {"enable" if activate else "disable"}?',
            options=available_features,
            formatter=lambda x: x.value,
        )

    assert feature_flag is not None
    conf.feature_flags[feature_flag.value] = activate
    conf.save_config()
    if activate:
        logger.info(f'{OK} Activated Feature: {feature_flag.value}')
    else:
        logger.info(f'{OK} Deactivated Feature: {feature_flag.value}')

    return 0
