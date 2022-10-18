import sys
import time
from qrunner.utils.log import logger
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.android.element import AndroidElement
from qrunner.core.ios.driver import IosDriver
from qrunner.core.ios.element import IosElement
from qrunner.core.web.driver import WebDriver
from qrunner.core.web.element import WebElement
from qrunner.core.h5.driver import H5Driver
from typing import Union


class Page(object):
    """页面基类，用于pom模式封装"""

    url = None

    def __init__(self, driver: Union[AndroidDriver, IosDriver,
                                     WebDriver, H5Driver]):
        self.driver = driver

    @staticmethod
    def sleep(n):
        """休眠"""
        logger.info(f'休眠 {n} 秒')
        time.sleep(n)

    def open(self):
        """打开页面"""
        try:
            self.driver.open_url(self.url)
        except Exception as e:
            logger.error(f'请设置页面url: {str(e)}')
            sys.exit()

    def elem(self, loc_dict: dict):
        """页面元素封装"""
        if isinstance(self.driver, AndroidDriver):
            return AndroidElement(**loc_dict)
        elif isinstance(self.driver, WebDriver):
            return WebElement(**loc_dict)
        elif isinstance(self.driver, IosDriver):
            return IosElement(**loc_dict)



