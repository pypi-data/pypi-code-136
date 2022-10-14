from qrunner.running.runner import main
from qrunner.utils.log import logger
from qrunner.utils.decorate import *
from qrunner.utils.config import conf
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.android.element import AndroidElement
from qrunner.core.android.case import AndroidTestCase
from qrunner.core.h5.driver import H5Driver
from qrunner.core.ios.driver import IosDriver
from qrunner.core.ios.element import IosElement
from qrunner.core.ios.case import IosTestCase
from qrunner.core.web.driver import WebDriver
from qrunner.core.web.element import WebElement
from qrunner.core.web.case import WebTestCase
from qrunner.core.web.driver import ChromeConfig, IEConfig, FirefoxConfig, EdgeConfig, SafariConfig
from qrunner.core.api.request import HttpRequest
from qrunner.core.api.case import TestCase
from qrunner.page import Page
from qrunner.utils.mail import Mail
from qrunner.utils.dingtalk import DingTalk

__version__ = "0.9.96"
__description__ = "全平台自动化测试框架"
