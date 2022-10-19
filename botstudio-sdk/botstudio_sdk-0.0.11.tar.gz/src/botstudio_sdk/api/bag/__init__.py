import os
from .code import get_zip_code_info

from logging import getLogger
logger = getLogger(__name__)

API_KEY = os.getenv("API_KEY_BAG")

# check if the api key is set in the environment variables
if API_KEY is None:
    raise ValueError("The API key for BAG is not set in the environment variables.")


# check if the api key and api are working
def _check_bag_api() -> bool:
    """Check if the api key and api api are working."""

    if get_zip_code_info("3011BH", "154"):
        return True
    else:
        return False


if _check_bag_api() is False:
    raise ValueError("The API key for BAG is not valid.")
else:
    logger.info("The API for BAG is working.")


if __name__ == "__main__":
    pass
