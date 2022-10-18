#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/9/23

import os
from pathlib import Path
from typing import Optional, Union, List, Dict

from sveltest.bin.conf import settings

from sveltest.components._api._email import SveltestEmail
from sveltest.support.common import ObjectDict



class NextSendEmail(SveltestEmail):
    """
    内置自动化测试使用
    """

    def __init__(self):
        self.conf = ObjectDict(settings.EMAIL_CONFIG)
        super(NextSendEmail, self).__init__(user=self.conf.USERNAME,password=self.conf.PWD,host=self.conf.PORT)

    def test_send(self,content:Optional[str],attachments:Optional[List]=None):
        """

        :param attachments:
        :return:
        """
        # mail_title 标题 count 总用例数 tester 测试人员  case_run_startTime 开始运行时间 case_run_endTime 测试结束时间
        # case_run_time 运行时长 pass_count 测试通过  pass_rate 通过率 fail_count 失败用例  failure_rate 失败率
        # error_count 错误用例 error_rate 错误率 skip_count 跳过用例 skip_rate 跳过率


        if settings.DEBUG is True:
            self.send(
                to=self.conf.LISTS,
                cc=self.conf.CC_LIST if self.conf.CC_LIST else None ,
                subject=self.conf.EMAIL_SUBJECT_PREFIX+self.conf.TITLE,
                bcc=self.conf.CC_LIST,
                contents=[str(content).replace("\n",'')],
                attachments=attachments,
            )


send_email = NextSendEmail
# NextTestRunner
class Email(SveltestEmail):
    """
    可单独使用的邮件API
    """
    def __init__(self,user:Optional[str],password:Optional[str],
                 host:Optional[str]="smtp.163.com",):
        super(Email, self).__init__(user=user,password=password,host=host)



from jinja2 import PackageLoader, Environment,FileSystemLoader


class JinJaTemplate:

    def __init__(self):
        # 创建一个包加载器对象
        self.env = Environment(loader=FileSystemLoader(
            os.path.join(Path(__file__).resolve().parent,"bin\conf\html").replace("\\","/")
        ))



    def get_template(self,t:Optional[str]):
        """

        :param t:
        :return:
        """
        return self.env.get_template(t)

    def send(self,case_run_startTime:Optional[str],
             html_title=Union[str,int],
             case_run_time=Optional[str],
             case_run_endTime=Optional[str],
             count=Union[int,str],
             pass_count=Union[int,str],
             fail_count=Union[int,str],
             error_count=Union[int,str],
             skip_count=Union[int,str],
             description=Union[int,str],
             content_title=Union[int,str],
             tester:Optional[Union[str,int]]="next report tester",
             mail_title:Optional[Union[str,int]]="next report test",
             ):

        EMAIL_HTML_TEMPLATE = '01001'

        send_email().test_send(content=
        self.get_template("email_test_template03.html").render(
            html_title=html_title,tester=tester,mail_title=mail_title,
            case_run_startTime=case_run_startTime,case_run_time=case_run_time,case_run_endTime=case_run_endTime,
            count=count,pass_count=pass_count,fail_count=fail_count,error_count=error_count,skip_count=skip_count,
            description=description,content_title=content_title
        ))


nextEmail = JinJaTemplate

# if __name__ == '__main__':
#     fp = r'F:\interfaceTestng\case\ocr\test_parameter_base64.py'
#     from pathlib import Path
#
#
#     j = JinJaTemplate()
#     z = j.send(html_title="自动化测试",tester="111",mail_title="自动化",
#                                                             case_run_startTime="2022年",case_run_time="18点",case_run_endTime="666",
#                                                             count=100,pass_count=100,fail_count=100,error_count=100,skip_count=10,description="测试测试",
#                                                             content_title="自动化测试执行结果报告")
