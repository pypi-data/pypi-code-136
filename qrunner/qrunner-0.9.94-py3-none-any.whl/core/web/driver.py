import logging
import os
import sys
import time
import allure
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import EdgeOptions
from qrunner.utils.webdriver_manager_extend import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from qrunner.utils.log import logger
from qrunner.utils.config import conf
from urllib import parse
from selenium.webdriver.remote.remote_connection import LOGGER
from qrunner.utils.exceptions import ScreenFailException
from selenium.webdriver.firefox.service import Service as fService
from selenium.webdriver.ie.service import Service as iService
from selenium.webdriver.edge.service import Service as eService
from selenium.webdriver.chrome.service import Service as cService

LOGGER.setLevel(logging.WARNING)


class ChromeConfig:
    headless = False
    options = None
    command_executor = ""


class FirefoxConfig:
    headless = False
    options = None
    command_executor = ""


class IEConfig:
    command_executor = ""


class EdgeConfig:
    headless = False
    options = None
    command_executor = ""


class SafariConfig:
    executable_path = "/usr/bin/safaridriver"
    command_executor = ""


class Browser(object):
    """
    根据关键词初始化浏览器操作句柄，
    如'chrome、google chrome、gc'代表chrome浏览器，
    如'firefox、ff'代表火狐浏览器，
    如'internet explorer、ie、IE'代表IE浏览器，
    如'edge'代表edge浏览器，
    如'safari'代表safari浏览器
    """
    name = None

    def __new__(cls, name=None):
        cls.name = name

        if (cls.name is None) or (cls.name in ["chrome", "google chrome", "gc"]):
            return cls.chrome()
        elif cls.name in ['internet explorer', 'ie', 'IE']:
            return cls.ie()
        elif cls.name in ['firefox', 'ff']:
            return cls.firefox()
        elif cls.name == 'edge':
            return cls.edge()
        elif cls.name == 'safari':
            return cls.safari()
        raise NameError(f"Not found {cls.name} browser")

    @staticmethod
    def chrome():
        logger.debug(ChromeConfig.headless)
        if ChromeConfig.options is None:
            chrome_options = ChromeOptions()
        else:
            chrome_options = ChromeConfig.options

        if ChromeConfig.headless is True:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument(
                f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')

        is_grid = False
        if ChromeConfig.command_executor == "":
            driver = webdriver.Chrome(options=chrome_options,
                                      service=cService(ChromeDriverManager().install()))
        elif ChromeConfig.command_executor[:4] == "http":
            is_grid = True
            driver = webdriver.Remote(options=chrome_options,
                                      command_executor=ChromeConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.CHROME.copy())
        else:
            driver = webdriver.Chrome(options=chrome_options,
                                      executable_path=ChromeConfig.command_executor)

        if is_grid is False:
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                            })"""
            })

        return driver

    @staticmethod
    def firefox():
        if FirefoxConfig.options is None:
            firefox_options = FirefoxOptions()
        else:
            firefox_options = FirefoxConfig.options

        if FirefoxConfig.headless is True:
            firefox_options.add_argument('-headless')
            firefox_options.add_argument(
                f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')

        if FirefoxConfig.command_executor == "":
            driver = webdriver.Firefox(options=firefox_options,
                                       service=fService(GeckoDriverManager().install()))
        elif FirefoxConfig.command_executor[:4] == "http":
            driver = webdriver.Remote(options=firefox_options,
                                      command_executor=FirefoxConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        else:
            driver = webdriver.Firefox(options=firefox_options,
                                       executable_path=FirefoxConfig.command_executor)

        return driver

    @staticmethod
    def ie():
        if IEConfig.command_executor == "":
            driver = webdriver.Ie(service=iService(IEDriverManager().install()))
        elif IEConfig.command_executor[:4] == "http":
            driver = webdriver.Remote(command_executor=IEConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.INTERNETEXPLORER.copy())
        else:
            driver = webdriver.Ie(executable_path=IEConfig.command_executor)

        return driver

    @staticmethod
    def edge():
        if EdgeConfig.options is None:
            edge_options = EdgeOptions()
        else:
            edge_options = EdgeConfig.options

        if EdgeConfig.headless is True:
            edge_options.headless = True

        if EdgeConfig.command_executor == "":
            driver = webdriver.Edge(options=edge_options,
                                    service=eService(EdgeChromiumDriverManager().install()))
        elif EdgeConfig.command_executor[:4] == "http":
            driver = webdriver.Remote(options=edge_options,
                                      command_executor=EdgeConfig.command_executor,
                                      desired_capabilities=DesiredCapabilities.EDGE.copy())
        else:
            driver = webdriver.Edge(options=edge_options,
                                    executable_path=EdgeConfig.command_executor)

        return driver

    @staticmethod
    def safari():
        if SafariConfig.command_executor != "" and SafariConfig.command_executor[:4] == "http":
            return webdriver.Remote(command_executor=SafariConfig.command_executor,
                                    desired_capabilities=DesiredCapabilities.SAFARI.copy())
        return webdriver.Safari(executable_path=SafariConfig.executable_path)


class WebDriver(object):
    _instance = {}

    def __new__(cls, browser_name=None):
        if browser_name not in cls._instance:
            cls._instance[browser_name] = super().__new__(cls)
        return cls._instance[browser_name]

    def __init__(self, browser_name=None):
        self.d = Browser(browser_name)
        timeout = conf.get_item('common', 'timeout')
        self.d.set_page_load_timeout(timeout)
        if ChromeConfig.headless:
            self.d.set_window_size(1920, 1080)
        else:
            self.d.maximize_window()

    @classmethod
    def get_instance(cls, browser_name=None):
        """Create singleton"""
        if browser_name not in cls._instance:
            logger.info(f'[{browser_name}] Create web driver singleton')
            return WebDriver(browser_name)
        return WebDriver._instance[browser_name]

    def open_url(self, url=None, login=True):
        if url is None:
            base_url = conf.get_item('common', 'base_url')
            if not base_url:
                logger.debug('请设置base_url')
                sys.exit()
            url = base_url
        else:
            if 'http' not in url:
                base_url = conf.get_item('common', 'base_url')
                if not base_url:
                    logger.debug('请设置base_url')
                    sys.exit()
                url = parse.urljoin(base_url, url)
        logger.info(f'访问: {url}')
        self.d.get(url)
        # 把默认请求头添加到cookie中
        if login:
            headers = conf.get_item('common', 'login_headers')
            logger.debug(headers)
            cookies = []
            if headers:
                for k, v in headers.items():
                    cookies.append({"name": k, "value": v})
                self.add_cookies(cookies)
                self.refresh()

    def back(self):
        logger.info('返回上一页')
        self.d.back()

    def screenshot(self, file_name):
        """
        截图并保存到预定路径
        @param file_name: foo.png or fool
        @return:
        """
        try:
            # 把文件名处理成test.png的样式
            if '.' in file_name:
                file_name = file_name.split(r'.')[0]
            # 截图并保存到当前目录的images文件夹中
            img_dir = os.path.join(os.getcwd(), 'images')
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
            file_path = os.path.join(img_dir, f'{time_str}-{file_name}.png')
            self.d.save_screenshot(file_path)
            # 上传allure报告
            allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG, name=f'{file_name}.png')
            return file_path
        except Exception as e:
            raise ScreenFailException(f'{file_name} 截图失败\n{str(e)}')

    # def screenshot_and_mark(self, file_name, rect):
    #     """给图片指定范围画上红框
    #     rect: [x, y, width, height]
    #     x: 左上坐标x
    #     y：左上角坐标y
    #     width：矩形宽度
    #     height：矩形高度
    #     """
    #     # 把文件名处理成test.png的样式
    #     if '.' in file_name:
    #         file_name = file_name.split(r'.')[0]
    #     # 截图并保存到当前目录的images文件夹中
    #     img_dir = os.path.join(os.getcwd(), 'images')
    #     if os.path.exists(img_dir) is False:
    #         os.mkdir(img_dir)
    #     time_str = time.strftime('%Y年%m月%d日 %H时%M分%S秒')
    #     file_path = os.path.join(img_dir, f'{time_str}-{file_name}.png')
    #     self.d.save_screenshot(file_path)
    #     # 画框
    #     ImageRecognition.mark(file_path, rect)
    #     # 上传allure报告
    #     allure.attach.file(file_path, attachment_type=allure.attachment_type.PNG, name=f'{file_name}.png')
    #     return file_path

    @property
    def page_content(self):
        page_source = self.d.page_source
        logger.info(f'获取页面内容: \n{page_source}')
        return page_source

    # @property
    # def rect(self):
    #     logger.info('获取窗口的坐标及宽高')
    #     return self.d.get_window_position()

    def max_window(self):
        logger.info('窗口设置全屏')
        self.d.maximize_window()

    def set_window(self, width, height):
        logger.info('设置窗口长宽')
        self.d.set_window_size(width, height)

    def get_windows(self):
        logger.info(f'获取当前打开的窗口列表')
        return self.d.window_handles

    def switch_window(self, old_windows):
        logger.info('切换到最新的window')
        current_windows = self.d.window_handles
        newest_window = [window for window in current_windows if window not in old_windows][0]
        self.d.switch_to.window(newest_window)

    def window_scroll(self, width, height):
        logger.info(f'设置scroll bar的宽高')
        js = "window.scrollTo({w},{h});".format(w=str(width), h=str(height))
        self.d.execute_script(js)

    def switch_to_frame(self, frame_id):
        logger.info(f'切换到frame {frame_id}')
        self.d.switch_to.frame(frame_id)

    def switch_to_frame_out(self):
        logger.info('从frame中切出来')
        self.d.switch_to.default_content()

    def execute_js(self, script, *args):
        logger.info(f'执行js脚本: \n{script}')
        self.d.execute_script(script, *args)

    def click(self, element):
        logger.info(f'点击元素: {element}')
        self.d.execute_script('arguments[0].click();', element)

    def quit(self):
        logger.info('退出浏览器')
        self.d.quit()

    def close(self):
        logger.info('关闭当前页签')
        self.d.close()

    def add_cookies(self, cookies: list):
        for cookie in cookies:
            self.d.add_cookie(cookie)

    def get_cookies(self):
        logger.info('获取cookies')
        cookies = self.d.get_cookies()
        logger.info(cookies)
        return cookies

    def get_cookie(self, name):
        logger.info(f'获取cookie: {name}')
        cookie = self.d.get_cookie(name)
        logger.info(cookie)
        return cookie

    def delete_all_cookies(self):
        logger.info('删除所有cookie')
        self.d.delete_all_cookies()

    def delete_cookie(self, name):
        logger.info(f'删除cookie: {name}')
        self.d.delete_cookie(name)

    def refresh(self):
        logger.info(f'刷新当前页')
        self.d.refresh()

    def get_title(self):
        logger.info('获取页面标题')
        title = self.d.title
        logger.info(title)
        return title

    def get_url(self):
        logger.info('获取页面url')
        url = self.d.current_url
        logger.info(url)
        return url

    def get_alert_text(self):
        logger.info('获取alert的文本')
        alert_text = self.d.switch_to.alert.text
        logger.info(alert_text)
        return alert_text

    def accept_alert(self):
        logger.info('同意确认框')
        self.d.switch_to.alert.accept()

    def dismiss_alert(self):
        logger.info('取消确认框')
        self.d.switch_to.alert.dismiss()


