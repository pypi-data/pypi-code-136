import sys
import platform
from pathlib import Path
from typing import Literal

from loguru import logger


def get_system_and_data_dn():
    if platform.system() == "Windows":
        system_dn = "Y:"
    else:
        system_dn = "/mnt/NASGFAT"

    system_dn = Path(system_dn)
    data_dn = Path.joinpath(system_dn, "datos")

    if data_dn.exists():
        return system_dn, data_dn
    else:
        return None, None


# Root Directory (in NASGFAT)  according to operative system

# Set DATA_DN
def set_data_dn(dn):
    """[summary]

    Args:
        dn ([type]): [description]
    """
    dn = Path(dn)
    if dn.is_dir():
        Path(dn)
        logger.info("%s is the new DATA_DN" % dn)
    else:
        logger.error("%s does not exist" % dn)


def set_logger_level(
    level: Literal["TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
) -> None:
    logger.remove()
    logger.add(sys.stderr, level=level)
