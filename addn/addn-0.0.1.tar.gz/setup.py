from distutils.core import setup


packages = ['addn']

setup(
    name='addn',                            # pip list 时显示的包名
    version='0.0.1',                        # 版本号
    author='mirschao',                      # 作者名
    packages=packages,                      # import 时写的名字
    package_dir={'requests': 'requests'}    # 所需的依赖模块
)
