from setuptools import setup, find_packages

setup(
    name='zik-client',
    version='0.0.3',
    license='MIT',
    author="TikTzuki",
    author_email='tranphanthanhlong18@gmail.com',
    packages=find_packages(".", include=["zik*"]),
    package_dir={'': '.'},
    url='https://github.com/TikTzuki/zik_client',
    keywords='zik client',
    install_requires=[
    ]
)
