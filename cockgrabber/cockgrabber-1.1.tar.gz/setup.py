from setuptools import setup

setup(
    name='cockgrabber',
    version='1.1',
    description='grab cocks',
    author='gravitas',
    author_email='yourmom@gmail.com',
    packages=['cockgrabber'],
    install_requires=['undetected-chromedriver', '2captcha-python', 'selenium', 'argparse', 'psycopg2', 'pytesseract']
)