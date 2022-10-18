

import setuptools  #导入工具包



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# 读写README.md 文件

setuptools.setup(
    name="NextTestRunner",  #项目名称
    version="0.0.2", #项目版本
    author="guanfl", #开发者名称
    author_email="gfl13453001@163.com",  #邮箱
    description="新一代，自动化测试执行器",  #描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gfl13453001/NextTestRunner", #github地址
    packages = setuptools.find_packages(),  # 包含所有src中的包
    # package_dir = {'':'NextTestRunner'},
    # 告诉distutils包都在src下

    classifiers=[
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 4 - Beta",
        # "Programming Language :: Python :: 3",
        # 支持的python版本
        # "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], #依赖环境

    # python 依赖版本
    python_requires='>=3.7',

    install_requires = [
        'rich==10.12.0',
        'jinja2',
        'pyyaml',
        'loguru==0.6.0',

    ],#第三方依赖包
    package_data={
            #任何包中含有.txt文件，都包含它
            '': ['*.py','*.py-tpl','*.json','*.html','*.pyc','*.xlsx',"*.*"],
            #包含demo包data文件夹中的 *.dat文件

        },
    keywords = 'sveltest linux python selenium unittest',


    # entry_points={
    #         'console_scripts': [
    #             # 命令 = 包.模块.方法
    #             'slt=sveltest.bin.conf.base.sveltest_main:main'
    #         ],
    #     },

)








