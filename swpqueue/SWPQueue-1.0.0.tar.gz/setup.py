from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='SWPQueue',
      version='1.0.0',
      description='基于文件读写实现的简单消息队列',
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
      url='https://gitee.com/w-8/SimpleQueue',
      author='bili:凿寂',
      author_email='mdzzdyxc@163.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=True
     )
#python3 setup.py sdist bdist_wheel
#python3 -m twine upload dist/*