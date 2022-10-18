import setuptools
try:
    long_description = open("README.rst",encoding='utf8').read()
except:
    raise ValueError("未成功打包md")

#注意：这是上一次的版本，请记得更新下面的数据！！！

setuptools.setup(name='GNavbar',
                 version='1.0.221019',
                 author='LAOGUObest',
                 author_email='LAOGUOszyyds1804@qq.com',
                 url='https://laoguobest.com',
                 readme = 'README.md',
                 long_description = long_description,
                 description='Navigation bar expansion package based on PyQt5 and PySide2.(x64 bit os only)',
                 classifiers=[
                     "Programming Language :: Python",
                     "Programming Language :: Python :: 3.10",],
                 packages=setuptools.find_packages(),
                 include_package_data=True,
                 )
