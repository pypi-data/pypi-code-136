from setuptools import setup, find_packages

setup(
    name="PyWebPtt",
    version="0.1",
    license='MIT',
    author="Tomoaki Chen",
    author_email="tomoaki.nccu@gmail.com",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/TomoakiChenSinica/PyWebPtt',
    keywords='使用 python 抓取 Web PTT 資料',
    install_requires=[
    ],
)
