from setuptools import setup, find_packages
setup(
    name="sapt",
    version="1.5.2",
    description="aptコマンド支援ツール",
    author="sonyakun",
    packages=find_packages(),
    install_requires="requests",
    entry_points={
        "console_scripts": [
            "sapt = aptUtil:sapt",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ]
)