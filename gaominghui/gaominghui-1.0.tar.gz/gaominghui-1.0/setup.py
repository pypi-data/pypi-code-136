from distutils.core import setup
setup(
    name="gaominghui",
    version="1.0",
    description="这是一个对外发布的模块，测试哦！",
    author="gaominghui",
    author_email="870660019@qq.com",
    py_modules=["demo_1","demo_2"]
)


#python setup.py sdist对外发布模块命令
#python setup.py install#安装包命令
#python setup.py sdist upload


'''
[distutils]
index-servers=pypi

[pypi]
repository=https://upload.pypi.org/legacy/
username=gaominghui
password=Aasd123-
'''