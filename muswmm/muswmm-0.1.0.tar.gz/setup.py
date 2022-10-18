# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(name='muswmm',
                 version='0.1.0',
                 description='muswmm是一个可以管理SWMM项目、设计SWMM模拟器、过程实时控制模拟的Python开发工具库。',
                 long_description=open('README.md', encoding='utf-8').read(),
                 long_description_content_type='text/markdown',
                 url='',
                 author='Lei Zhang',
                 author_email='gemini.zhang@qq.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
				 package_data={'':['*.dll'],})