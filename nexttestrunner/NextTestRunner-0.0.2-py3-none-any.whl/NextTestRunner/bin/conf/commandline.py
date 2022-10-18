
#!/usr/bin/env python
#-*- coding:utf-8 -*-



"""


                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|


"""


"""统一执行测试用例，并生成测试报告"""


import os
import time

from NextTestRunner.bin.conf import settings

from typing import Dict,Optional

from NextTestRunner.support.common import is_dir
from NextTestRunner.components.htmlRunner import HTMLTestRunner
from NextTestRunner.support.system import ZipFile

from NextTestRunner.support.logger_v2 import log_v2
TEST_REPORT = {
    'context_processors':
        {
            'zip':'',
            'html':'',
            'img':'',
        }
}

get_case = getattr(settings, "CASE_SUITE_PATH")


# case_path = os.path.join(get_case,'case')
# guanfl
# v1.0.1
# 20210602
# :TODO :完成第一版 待单元测试
class MainTestSuite(object):
    """

    """
    def __init__(self,report_filename:Optional[str]=None):
        if report_filename is None:self.report_filename = "自动化测试报告"
        else:self.report_filename = report_filename

    #     服务启动
        if getattr(settings, "API_TEST_TEMPLATE") is True:
            pass

    def test_suite_base(self,suites:Optional[list],
                        test_title_name:Optional[str]=None,
                        description:Optional[str]=None,
                        thread_count:Optional[int]=0,
                        save_last_try:Optional[bool]=True,
                        ) -> Dict:
        """
        基本的测试集
        :param test_title_name:
        :param description:
        :return:
        """

        # #测试报告保存的路径
        now = time.strftime('%Y-%m-%d', time.localtime())
        # get_html = getattr(settings, "TEST_REPORT")

        # 如果有配置html报告路径则进行使用配置里的数据、没有将进行使用tank默认的存放路径
        if not settings.TEST_REPORT:
            # get_base= getattr(settings, "BASE_DIR")
            path = os.path.join(settings.BASE_DIR,'report/html',now).replace('\\','/')
        else:
            path = os.path.join(settings.TEST_REPORT["HTML"],now).replace('\\','/')

        # 判断当 report_base 目录是否已存在、如果不存在就进行创建新的目录
        try:
            if os.path.exists(path):
                log_v2.info(path+"已存在，将跳过创建操作")
            else:
                log_v2.warning("测试结果输出存放的目录不存在，正在创建该目录")
                os.makedirs(path,exist_ok=True)
                log_v2.success(f"创建成功，创建的目录路径为："+path)
            # else:
            #     pass

        except Exception as e:
            log_v2.error(e)
        #
        #
        joinPath = os.path.join(path,'%s_%s.html'%(self.report_filename,now)).replace("\\","/")
        #
        fp = open(joinPath, 'wb')

        # 测试过程中的数据流写入到打开的报告中
        runner = HTMLTestRunner(
            stream=fp,
            retry=settings.TEST_CASE_ERROR_RETRY,
            title=test_title_name,
            description=description,
            save_last_try=save_last_try,
            verbosity=settings.LOGGING_VERBOSITY
        )
        #
        text_content = runner.run(suites,max_workers=thread_count)

        if not settings.TEST_REPORT and settings.TEST_REPORT["START_ZIP"] is True:

            if settings.TEST_REPORT["ZIP"]:
                get_base = getattr(settings, "BASE_DIR")
                zip_file_report_path = os.path.join(get_base, 'report/zip/%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")
                zip_path_save = ZipFile()
                path = zip_path_save.zip_file(path=path,zipfile_name=zip_file_report_path)
                log_v2.info("已对目录路径为：{},下的文件进行打包成zip文件,存放路径为：{}".format(path,zip_file_report_path))

        return  text_content

