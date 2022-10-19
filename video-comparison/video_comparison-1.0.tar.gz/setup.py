from setuptools import setup

from video_compare import __version__

install_requires=[
    'streamlit',
    'PIL',
    'base64',
    'io',
    'uuid'
],


setup(
    name='video_comparison',
    version=__version__,

    url='https://github.vimeows.com/yedidya-hyams/video_comparison',
    author='Yedidya Hyams',
    author_email='yedidya.hyams@vimeo.com',

    py_modules=['video_compare'],
)