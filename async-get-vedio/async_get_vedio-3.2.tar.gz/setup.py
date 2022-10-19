import setuptools

setuptools.setup(
    name = 'async_get_vedio',
    version = '3.2',
    author = 'WUT_ljs',
    author_email = '3480339804@qq.com',
    url = 'https://github.com/wutljs/async_get_vedio',
    description = 'Get vedio',
    long_description = '修改了3.1中的错误:使用Crypto解密的时候产生的错误'
                       '具体文档请进入:https://github.com/wutljs/async_get_vedio 查看.',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)