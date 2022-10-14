#############################################
# File Name: setup.py
# Author: wqrf
# Mail: 1074321997@qq.com
# Created Time:  2022-10-14 12:16:00
#############################################

from setuptools import setup, find_packages

setup(
    name = "django_task_mq",
    version = "1.0.2",
    keywords = ("mq","task","django","django_task_mq"),
    description = "a tool for django which belong mq",
    long_description = "If you need help, please email to 1074321997@qq.com",
    license = "MIT",
    url = "https://github.com/Woqurefan",
    author = "wqrf",
    author_email = "1074321997@qq.com",
    packages = ['django_task_mq'],
)