from distutils.core import setup
import setuptools

packages = ['pytool_lh']  # 唯一的包名，自己取名
setup(
      name='pytool_lh',
      version='1.0.0',
      author='LinHan',
      author_email='linhan1208@outlook.com',
      packages=packages,
      package_dir={'requests': 'requests'},
)
