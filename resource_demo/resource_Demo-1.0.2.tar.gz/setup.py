from distutils.core import setup
 
setup(
    name='resource_Demo',  # 对外模块的名字
    version='1.0.2',  # 版本号
    description='测试本地发布模块',  # 描述
    author='hyf',  # 作者
    author_email='huangyufeng@zju.edu.cn',
    py_modules=['resource_Demo.load_data'],  # 要发布的模块
)