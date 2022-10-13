import sys
import time
from qrunner.utils.log import logger
from qrunner import AndroidDriver, IosDriver, WebDriver, H5Driver
from typing import Union


class Page(object):
    url = None

    def __init__(self, driver: Union[AndroidDriver, IosDriver, WebDriver, H5Driver]):
        self.driver = driver

    @staticmethod
    def sleep(n):
        logger.info(f'休眠 {n} 秒')
        time.sleep(n)

    def open(self):
        try:
            self.driver.open_url(self.url)
        except Exception as e:
            logger.error(f'请设置页面url: {str(e)}')
            sys.exit()



