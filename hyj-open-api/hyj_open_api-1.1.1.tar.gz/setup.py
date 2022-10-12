from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(name='hyj_open_api',  # 包名
      version='1.1.1',  # 版本号
      description='HuYujie Python Auto API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='YuJie Hu',
      author_email='871234464@qq.com',
      url='https://github.com/breeze-maple',
      install_requires=[],
      license='MIT License',
      platforms=["all"],
      classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Natural Language :: Chinese (Simplified)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'
            ]
      )
