# -*- coding: utf-8 -*-
# Desc: 封装发送邮件模块
#
import email.utils
from smtplib import SMTP_SSL, SMTP, SMTPException
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import random
import os


class EmailTools(object):
    def __init__(self, subject, user, password, smtp,to_list, cc_list, port):
        self.Subject = subject
        self.USER = user
        self.FROM = ''
        self.PW = password
        self.SMTP = smtp
        self.PORT = port
        self.TO_LIST = to_list
        self.CC_LIST = cc_list
        self.init()

    def init(self):
        self.str = ""
        self.images = {}
        self.attr = []
        self.init_static()

    def init_static(self):
        self.str = """<html>
        <head>
        <style type="text/css">
            table.table-otl
        {
            border-collapse: collapse;
            margin: 0 auto;
            text-align: center;
        }
        table.table-otl  td, table.table-otl  th
        {
            border: 1px solid #cad9ea;
            color: #666666;
            height: 30px;
        }
        table.table-otl  thead th
        {
            background-color: #CCE8EB;
            width: 100px;
        }
        table.table-otl  tr:nth-child(odd)
        {
            background: #ffffff;
        }
        table.table-otl  tr:nth-child(even)
        {
            background: #F5FAFA;
        }
    </style></head>
    <body>
        """


    def add_str(self, s):
        """
        添加文本
        :param s:
        :return:
        """
        if not isinstance(s, str): raise TypeError ("s must be str or int, but gave {}".format(type(s)))
        self.str += ''' {} <br>'''.format(s)

    def add_image(self, image):
        """
        添加图片
        :param image:
        :return:
        """
        _cid = "image{}".format(random.randint(0, 999))
        self.add_str("""<img src="cid:{}">""".format(_cid))
        self.images[_cid] = image

    def add_attr(self, attr):
        """
        添加附件
        :param attr:
        :return:
        """
        self.attr.append(attr)

    def add_table(self, data, **kwargs):
        """
        添加表格
        :param: data 表格数据 格式：[[1, 2, 3, 4], [a, b, c, d]]
        :param: title 表格标题  非必须
        :return:
        """
        title = kwargs['title'] if 'title' in kwargs.keys() else None

        msg = """<table class="table-otl">"""
        if not isinstance(data, list): raise TypeError ("data must be [ list ], give {}".format(type(data)))
        if title:
            msg += """<caption> <h2> {} </h2></caption>""".format(title)

        head = data.pop(0)
        if head:
            msg += """<thead><tr>"""
            for h in head:
                msg += """<th>{}</th>""".format(h)
            msg += """</tr></thead>"""

        for i in data:
            msg += """<tr>"""
            for d in i:
                msg += """<td>{}</td>""".format(d)
            msg += """</tr>"""
        msg += """</table>"""
        self.add_str(msg)

    def add_strong_str(self, s):
        if not isinstance(s, str): raise TypeError ("s must be str or int, but give {}".format(type(s)))
        self.str += '''<strong> {} </strong><br>'''.format(s)

    def _set_from(self, _from):
        self.FROM = _from

    def __get_str(self):
        return self.str

    def __get_image(self, cid, image):
        with open(image, 'rb') as fp:
            i = MIMEImage(fp.read(), _subtype='octet-stream')
            i.add_header('Content-ID', cid)
        return i

    def __get_file(self, file):
        with open(file, 'rb') as fp:
            i = MIMEText(fp.read(), 'base64', 'utf-8')
            i.add_header('Content-Type', 'application/octet-stream')
            i.add_header('Content-Disposition', 'attachment; filename=' + os.path.basename(file))

        return i

    def send_email(self):
        msgAlternative = MIMEMultipart()
        msgAlternative['From'] = self.USER
        msgAlternative['Subject'] = Header(self.Subject)
        msgAlternative['To'] = ",".join(self.TO_LIST)
        msgAlternative['Message-id'] = email.utils.make_msgid()
        if self.CC_LIST:
            msgAlternative['Cc'] = Header(",".join(self.CC_LIST))

        # 设定纯文本信息
        msgHtml = MIMEText(self.__get_str(), 'html', 'utf-8')
        msgAlternative.attach(msgHtml)

        # 设定内置图片信息
        if self.images:
            for cid in self.images.keys():
                i = self.__get_image(cid, self.images[cid])
                msgAlternative.attach(i)

        # 设定附件
        if self.attr:
            for file in self.attr:
                i = self.__get_file(file)
                msgAlternative.attach(i)
        if self.PORT == 25:
            try:
                smtp_obj = SMTP(self.SMTP, self.PORT)
                smtp_obj.connect(self.SMTP, self.PORT)
                smtp_obj.login(self.USER, self.PW)
                smtp_obj.sendmail(self.USER, self.TO_LIST + self.CC_LIST, msgAlternative.as_string())
                smtp_obj.close()
                return True, "邮件发送成功"
            except SMTPException as e:
                return False, "邮件发送失败: {}".format(e)
        elif self.PORT == 465:
            smtp_obj = SMTP_SSL(self.SMTP, self.PORT)
            try:
                smtp_obj.login(self.USER, self.PW)
                smtp_obj.sendmail(self.USER, self.TO_LIST + self.CC_LIST, msgAlternative.as_string())
                return True, "邮件发送成功"
            except SMTPException as e:
                return False, "邮件发送失败: {}".format(e)
            finally:
                smtp_obj.quit()


class EmailApi(object):
    def __init__(self, config):
        self.config = config
        if not isinstance(self.config, dict):
            raise Exception('config type Error: {}, need [dict]'.format(type(self.config)))
        self.apps = {}
        self.init_app()

    def init_app(self):
        for k in self.config.keys():
            self.apps[k] = EmailTools(
                self.config[k]['name'],
                self.config[k]['user'],
                self.config[k]['password'],
                self.config[k]['smtp'],
                self.config[k]['to_list'],
                self.config[k]['cc_list'],
                self.config[k]['port'],
            )

    def __getattr__(self, item) -> EmailTools:
        return self.apps.get(item)


