#!/usr/bin/env python3
import sys

__version__ = "1.3.dev0"

from setuptools import setup, find_packages

# We do not support Python <3.8
if sys.version_info < (3, 8):
    print(
        "Unfortunately, your python version is not supported!\n"
        "Please upgrade at least to Python 3.8!",
        file=sys.stderr,
    )
    sys.exit(1)

install_requires = [
    "ddt",
    "pyyaml",
    "websocket_client",
    "requests",
    "future",
    "pyee",
    "typing_extensions"
]

entry_points = {
    "console_scripts": [
        "minitest=minium.framework.loader:main",
        "miniruntest=minium.framework.loader:main",
        "minireport=minium.framework.report:main",
        "miniErrorReport=minium.framework.errorReport:main",
        "mininative=minium.native.nativeapp:start_server",
    ]
}


config_path = "miniprogram/base_driver/version.json"
package_data = {
    "minium": [
        config_path,
        "framework/dist/*",
        "framework/dist/*/*",
        "native/wx_native/*/*",
        "native/qq_native/*/*",
        "native/*/*",
        "native/*/*/*/*",
        "native/*/*/*/*/*",
        "native/*/*/*/*/*/*",
        "utils/js/min/*",
        "utils/js/es5/*",
    ]
}

exclude_package_data = {"": ["*pyc", "readme.md", "build.py", "__pycache__"]}
extras_require = {
    "ios": ["tidevice==0.4.10",]
}

long_description = """
install:
```
pip3 install minium
```
if you use ios devices, you can install with
```
pip3 install minium[ios]
```

See the [document](https://minitest.weixin.qq.com/#/minium/Python/readme) for details
"""

if __name__ == "__main__":
    setup(
        name="minium",
        version=__version__,
        license="MIT",
        url="https://minitest.weixin.qq.com/#/",
        packages=find_packages(),
        description="Minium is the best MiniProgram auto test framework.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        package_data=package_data,
        exclude_package_data=exclude_package_data,
        entry_points=entry_points,
        install_requires=install_requires,
        extras_require=extras_require,
        setup_requires=["setuptools"],
        python_requires=">=3.8",
        author="WeChat-Test",
        author_email="minitest@tencent.com",
        platforms=["MacOS", "Windows"],
        keywords=["minium", "WeApp", "MiniProgram", "Automation", "Test"],
    )
