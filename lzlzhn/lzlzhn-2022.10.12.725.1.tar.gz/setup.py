from setuptools import setup, find_packages
setup(
    name='lzlzhn',
    version='2022.10.12.0725.1',
    description="一个很会玩的第三方库,更新版本号与更新/修复个数有关",
    long_description='HELLO! 感谢你下载我的第三方库！十分感谢！',
    include_package_data=True,
    author='24K野生程序员/24K Wild Programmers',
    author_email='liuniandexiaohuo@qq.com',
    license='MIT License',
    url='https://blog.csdn.net/l15668952150/article/details/124575394',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=['pyperclip', 'PyAutoGUI', 'pygame', 'qrcode', 'MyQR','PyQt5'],


)
