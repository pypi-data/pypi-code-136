import re
import time
from typing import Union

import jmespath

from qrunner.core.api.request import ResponseResult, HttpRequest
from qrunner.utils.decorate import step
from qrunner.core.web.driver import WebDriver
from qrunner.core.web.element import WebElement
from qrunner.core.h5.driver import H5Driver
from qrunner.core.ios.driver import IosDriver
from qrunner.core.ios.element import IosElement
from qrunner.utils.log import logger
from qrunner.utils.config import config
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.android.element import AndroidElement


class TestCase(HttpRequest):
    """
    测试用例基类，所有测试用例需要继承该类
    """
    driver: Union[AndroidDriver, IosDriver, WebDriver, H5Driver] = None

    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        # 初始化driver
        platform = config.get_platform()
        logger.info(platform)
        if platform == 'android':
            serial_no = config.get_device()
            cls.driver = AndroidDriver(serial_no)
        elif platform == 'web':
            browser = config.get_browser()
            cls.driver = WebDriver(browser)
        elif platform == 'ios':
            serial_no = config.get_device()
            cls.driver = IosDriver(serial_no)
        cls().start_class()

    @classmethod
    def teardown_class(cls):
        if isinstance(cls().driver, WebDriver):
            cls().driver.quit()
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        self.start_time = time.time()
        logger.debug(f"[start_time]: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        # 启动应用
        # self.driver.force_start_app()
        self.start()

    def teardown_method(self):
        self.end()
        # self.driver.screenshot('用例执行完成截图')
        # self.screenshot('用例执行完成截图')
        # 退出应用
        # self.driver.stop_app()
        logger.debug(f"[end_time]: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        take_time = time.time() - self.start_time
        logger.debug("[run_time]: {:.2f} s".format(take_time))

    # 公共方法
    @staticmethod
    def sleep(n: int):
        """休眠"""
        logger.debug(f'等待: {n}s')
        time.sleep(n)

    def screenshot(self, file_name):
        """截图"""
        self.driver.screenshot(file_name)

    def elem(self, **kwargs):
        if isinstance(self.driver, AndroidDriver):
            return AndroidElement(self.driver, **kwargs)
        elif isinstance(self.driver, WebDriver):
            return WebElement(self.driver, **kwargs)
        elif isinstance(self.driver, IosDriver):
            return IosElement(self.driver, **kwargs)

    def assertText(self, expect_value, timeout=5):
        """断言页面包含文本"""
        for _ in range(timeout + 1):
            try:
                page_source = self.driver.get_page_content()
                assert expect_value in page_source, f'页面内容不包含 {expect_value}'
                break
            except AssertionError:
                time.sleep(1)
        else:
            page_source = self.driver.get_page_content()
            assert expect_value in page_source, f'页面内容不包含 {expect_value}'

    def assertNotText(self, expect_value, timeout=5):
        """断言页面不包含文本"""
        for _ in range(timeout + 1):
            try:
                page_source = self.driver.get_page_content()
                assert expect_value not in page_source, f'页面内容不包含 {expect_value}'
                break
            except AssertionError:
                time.sleep(1)
        else:
            page_source = self.driver.get_page_content()
            assert expect_value not in page_source, f'页面内容仍然包含 {expect_value}'

    def assertElement(self, timeout=5, **kwargs):
        """断言元素存在"""
        for _ in range(timeout + 1):
            try:
                element = self.elem(**kwargs)
                assert element.exists(), f'元素 {kwargs} 不存在'
                break
            except AssertionError:
                time.sleep(1)
        else:
            assert self.elem(**kwargs).exists(), f'元素 {kwargs} 不存在'

    def assertNotElement(self, timeout=5, **kwargs):
        """断言元素不存在"""
        for _ in range(timeout + 1):
            try:
                assert not self.elem(**kwargs).exists(), f'元素 {kwargs} 仍然存在'
                break
            except AssertionError:
                time.sleep(1)
        else:
            assert not self.elem(**kwargs).exists(), f'元素 {kwargs} 仍然存在'

    # WEB专用方法
    def switch_frame(self, frame_id: str):
        """切换到iframe中"""
        self.driver.switch_to_frame(frame_id)

    def frame_out(self):
        """从iframe中回到顶层页面"""
        self.driver.switch_to_frame_out()

    def exe_js(self, script: str, *args):
        """执行js语句"""
        self.driver.execute_js(script, *args)

    def click_js(self, **kwargs):
        """正常点击方法失败时使用"""
        elem = self.elem(**kwargs).get_element()
        self.driver.execute_js("$(arguments[0]).click()", elem)

    def assertTitle(self, expect_value=None, timeout=5):
        """断言页面标题等于"""
        for _ in range(timeout + 1):
            try:
                title = self.driver.get_title()
                assert expect_value == title, f'页面标题 {title} 不等于 {expect_value}'
                break
            except AssertionError:
                time.sleep(1)
        else:
            title = self.driver.get_title()
            assert expect_value == title, f'页面标题 {title} 不等于 {expect_value}'

    def assertInTitle(self, expect_value=None, timeout=5):
        """断言页面标题包含"""
        for _ in range(timeout + 1):
            try:
                title = self.driver.get_title()
                assert expect_value in title, f'页面标题 {title} 不包含 {expect_value}'
                break
            except AssertionError:
                time.sleep(1)
        else:
            title = self.driver.get_title()
            assert expect_value in title, f'页面标题 {title} 不包含 {expect_value}'

    def assertUrl(self, expect_value=None, timeout=5):
        """断言页面url等于"""
        for _ in range(timeout + 1):
            try:
                url = self.driver.get_url()
                assert expect_value == url, f'页面url {url} 不等于 {expect_value}'
                break
            except AssertionError:
                time.sleep(1)
        else:
            url = self.driver.get_url()
            assert expect_value == url, f'页面url {url} 不等于 {expect_value}'

    def assertInUrl(self, expect_value=None, timeout=5):
        """断言页面url包含"""
        for _ in range(timeout + 1):
            try:
                url = self.driver.get_url()
                assert expect_value in url, f'页面url {url} 不包含 {expect_value}'
                break
            except AssertionError:
                time.sleep(1)
        else:
            url = self.driver.get_url()
            assert expect_value in url, f'页面url {url} 不包含 {expect_value}'

    def assertAlertText(self, expect_value):
        """断言弹窗文本"""
        alert_text = self.driver.get_alert_text()
        assert expect_value == alert_text, f'弹窗文本 {alert_text} 等于 {expect_value}'

    # APP专用方法
    def install_app(self, url):
        """安装应用"""
        self.driver.install_app(url)

    def new_install_app(self, url, pkg_name=None):
        """先卸载再安装应用"""
        self.driver.new_install_app(url, pkg_name)

    def uninstall_app(self, pkg=None):
        """卸载应用"""
        self.driver.uninstall_app(pkg)

    def start_app(self, pkg=None):
        """强制启动应用"""
        self.driver.force_start_app(pkg)

    def stop_app(self, pkg=None):
        """停止应用"""
        self.driver.stop_app(pkg)

    # API专用方法
    @staticmethod
    def assertStatusCode(status_code):
        """
        断言状态码
        """
        with step(f'断言响应状态码 == {status_code}'):
            actual_code = ResponseResult.status_code
            assert actual_code == status_code, \
                f'status_code {ResponseResult} != {status_code}'

    @staticmethod
    def assertPath(path, value):
        """
        功能同assertEq，用于兼容历史代码
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} == {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert search_value == value, f'{search_value} != {value}'

    @staticmethod
    def assertNotEq(path, value):
        """
        值不等于
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} != {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert search_value != value, f"{search_value} 等于 {value}"

    @staticmethod
    def assertLenEq(path, value):
        """
        断言列表长度等于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 的长度 == {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert len(search_value) == value, f"{search_value} 的长度不等于 {value}"

    @staticmethod
    def assertLenGt(path, value):
        """
        断言列表长度大于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 的长度 > {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert len(search_value) > value, f"{search_value} 的长度不大于 {value}"

    @staticmethod
    def assertLenGtOrEq(path, value):
        """
        断言列表长度大于等于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 的长度 >= {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert len(search_value) >= value, f"{search_value} 的长度不大于 {value}"

    @staticmethod
    def assertLenLt(path, value):
        """
        断言列表长度小于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 的长度 < {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert len(search_value) < value, f"{search_value} 的长度不大于 {value}"

    @staticmethod
    def assertLenLtOrEq(path, value):
        """
        断言列表长度小于等于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 的长度 <= {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert len(search_value) <= value, f"{search_value} 的长度不大于 {value}"

    @staticmethod
    def assertGt(path, value):
        """
        值大于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} > {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert int(search_value) > int(value), f"{search_value} 不大于 {value}"

    @staticmethod
    def assertGtOrEq(path, value):
        """
        值大于等于
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} >= {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            if isinstance(search_value, str):
                search_value = int(search_value)
            assert search_value >= value, f"{search_value} 小于 {value}"

    @staticmethod
    def assertLt(path, value):
        """
        值小于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} < {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert int(search_value) < int(value), f"{search_value} 不大于 {value}"

    @staticmethod
    def assertLtOrEq(path, value):
        """
        值小于等于多少
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} <= {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert int(search_value) <= int(value), f"{search_value} 不大于 {value}"

    @staticmethod
    def assertRange(path, start: int, end: int):
        """值在(start, end)范围内
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 在({start}, {end})范围内'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert (int(search_value) >= start) & (int(search_value) <= end), f'{search_value} 不在[{start}, {end}]范围内'

    @staticmethod
    def assertIn(path, value):
        """
        断言匹配结果被value_list包含
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 被 {value} 包含'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert search_value in value, f"{value} 不包含 {search_value}"

    @staticmethod
    def assertNotIn(path, value):
        """
        断言匹配结果不被value_list包含
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 不被 {value} 包含'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert search_value not in value, f"{value} 包含 {search_value}"

    @staticmethod
    def assertNotExists(path):
        """断言字段不存在"""
        with step(f'断言响应中 {path} 值为None或字段不存在'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert search_value is None, f'仍然包含 {path} 为 {search_value}'

    @staticmethod
    def assertContains(path, value):
        """
        断言匹配结果包含value
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 包含 {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert value in search_value, f"{search_value} 不包含 {value}"

    @staticmethod
    def assertNotContains(path, value):
        """
        断言匹配结果不包含value
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 不包含 {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            assert value not in search_value, f"{search_value} 包含 {value}"

    @staticmethod
    def assertTypeMatch(path, value_type):
        """
        类型匹配
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 的数据类型等于 {value_type}'):
            if not isinstance(value_type, type):
                if value_type == 'int':
                    value_type = int
                elif value_type == 'str':
                    value_type = str
                elif value_type == 'list':
                    value_type = list
                elif value_type == 'dict':
                    value_type = dict
                else:
                    value_type = str

            search_value = jmespath.search(path, ResponseResult.response)
            assert isinstance(search_value, value_type), f'{search_value} 不是 {value_type} 类型'

    @staticmethod
    def assertStartsWith(path, value):
        """
        以什么开头
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 以 {value} 开头'):
            search_value: str = jmespath.search(path, ResponseResult.response)
            assert search_value.startswith(value), f'{search_value} 不以 {value} 开头'

    @staticmethod
    def assertEndsWith(path, value):
        """
        以什么结尾
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 以 {value} 结尾'):
            search_value: str = jmespath.search(path, ResponseResult.response)
            assert search_value.endswith(value), f'{search_value} 不以 {value} 结尾'

    @staticmethod
    def assertRegexMatch(path, value):
        """
        正则匹配
        doc: https://jmespath.org/
        """
        with step(f'断言响应中 {path} 正则匹配表达式 {value}'):
            search_value = jmespath.search(path, ResponseResult.response)
            match_obj = re.match(r'' + value, search_value, flags=re.I)
            assert match_obj is not None, f'结果 {search_value} 匹配失败'
