from setuptools import find_packages
import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

setuptools.setup(name='notion_md',  # 包名
                 version='2.1.1',  # 版本号
                 description='A package for notion2md',
                 long_description=long_description,
                 author='qxxiao',
                 author_email='1063064004@qq.com',
                 url='https://github.com/qxxiao/notion2md',
                 install_requires=["bs4", "notion_client"],
                 license='MIT',
                 packages=find_packages('src'),
                 package_dir={'': 'src'},
                 platforms=["all"],

                 entry_points={
                     'console_scripts': ['notion_md=notion_md.main:main'],
                 },
                 classifiers=[
                     'Natural Language :: Chinese (Simplified)',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.8',
                 ],
                 )
