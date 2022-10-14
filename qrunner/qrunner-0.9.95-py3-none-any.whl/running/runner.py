import inspect
import os

import pytest
from qrunner.utils.log import logger
from qrunner.utils.config import conf


class TestMain(object):
    """
    Support for app、web、http
    """
    def __init__(self,
                 android_id: str = None,
                 android_pkg: str = None,
                 ios_id: str = None,
                 ios_pkg: str = None,
                 browser: str = 'chrome',
                 case_path: str = None,
                 rerun: int = 0,
                 concurrent: bool = False,
                 base_url: str = None,
                 headers: dict = None,
                 timeout: int = 10,
                 ):
        """

        @param android_id: 安卓设备id，通过adb devices命令获取
        @param android_pkg: 安卓应用包名，通过adb shell pm list packages命令获取
        @param ios_id: IOS设备id，通过tidevice list命令获取
        @param ios_pkg: IOS应用包名，通过tidevice applist命令获取
        @param browser: 浏览器类型，默认chrome，还支持firefox、edge、safari等
        @param case_path: 测试用例路径
        @param rerun: 失败重试次数
        @param concurrent: 是否并发执行用例
        @param base_url: 默认域名
        @param headers: 默认请求头, {
            "login_headers": {},
            "visit_headers": {}
        }
        @param timeout: 超时时间
        """
        # 将数据写入全局变量
        conf.set_item('android', 'serial_no', android_id)
        conf.set_item('android', 'pkg_name', android_pkg)
        conf.set_item('ios', 'serial_no', ios_id)
        conf.set_item('ios', 'pkg_name', ios_pkg)
        conf.set_item('web', 'browser_name', browser)
        conf.set_item('common', 'base_url', base_url)
        if headers is not None:
            login_headers = headers.pop('login_headers', {})
            conf.set_item('common', 'login_headers', login_headers)
            visit_headers = headers.pop('visit_headers', {})
            conf.set_item('common', 'visit_headers', visit_headers)
        conf.set_item('common', 'timeout', timeout)

        # 执行用例
        logger.info('执行用例')
        if case_path is None:
            stack_t = inspect.stack()
            ins = inspect.getframeinfo(stack_t[1][0])
            file_dir = os.path.dirname(os.path.abspath(ins.filename))
            file_path = ins.filename
            if "\\" in file_path:
                this_file = file_path.split("\\")[-1]
            elif "/" in file_path:
                this_file = file_path.split("/")[-1]
            else:
                this_file = file_path
            case_path = os.path.join(file_dir, this_file)
        logger.info(f'用例路径: {case_path}')
        cmd_list = [
            '-sv',
            '--reruns', str(rerun),
            '--alluredir', 'allure-results', '--clean-alluredir'
        ]
        if case_path:
            cmd_list.insert(0, case_path)
        if concurrent:
            """仅支持http接口测试"""
            cmd_list.insert(1, '-n')
            cmd_list.insert(2, 'auto')
            cmd_list.insert(3, '--dist=loadscope')
        logger.info(cmd_list)
        pytest.main(cmd_list)


main = TestMain


if __name__ == '__main__':
    main()

