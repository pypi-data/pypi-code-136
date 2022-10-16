import setuptools

setuptools.setup(
    name = 'async_get_vedio',
    version = '3.1',
    author = 'WUT_ljs',
    author_email = '3480339804@qq.com',
    url = 'https://github.com/wutljs/async_get_vedio',
    description = 'Get vedio',
    long_description = '在3.0的基础上,对async_get_vedio里面的函数进行进一步封装.减少因为错误调用函数而可能产生的错误'
                       '具体文档请进入:https://github.com/wutljs/async_get_vedio 查看.',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)