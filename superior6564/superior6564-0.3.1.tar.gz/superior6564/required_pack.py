"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564
"""
import subprocess
import sys


def install():
    """
    Description:
        install() installs required packages.
    """
    def install_process(package: str, version_need: str, version_now: str = None):
        if version_now is None:
            print()
            print(f"Package {package} not found.")
            print(f"Installation of package ({package}).")
            new_package = package + "==" + version_need
            subprocess.check_call([sys.executable, "-m", "pip", "install", new_package])
            print(f"Package {package}({version_need}) installed.")
            print()
        else:
            print()
            print(f"Version of {package} is {version_now}.")
            version_need_change = int(version_need.replace(".", ""))
            version_now_change = int(version_now.replace(".", ""))
            if version_now_change >= version_need_change:
                print(f"It is ok :)")
            elif version_now_change < version_need_change:
                print(f"Updating of package ({package}).")
                new_package = package + "==" + version_need
                subprocess.check_call([sys.executable, "-m", "pip", "install", new_package])
                print(f"Package {package}({version_need}) installed.")
            print()

    package_name = "requests"
    package_version = "2.28.1"
    try:
        import requests
        install_process(package=package_name, version_need=package_version, version_now=requests.__version__)
    except ModuleNotFoundError:
        install_process(package=package_name, version_need=package_version)

    package_name = "ipython"
    package_version = "7.9.0"
    try:
        import IPython
        install_process(package=package_name, version_need=package_version, version_now=IPython.__version__)
    except ModuleNotFoundError:
        install_process(package=package_name, version_need=package_version)

    package_name = "dearpygui"
    package_version = "1.7.1"
    try:
        import dearpygui
        install_process(package=package_name, version_need=package_version, version_now=dearpygui.__version__)
    except ModuleNotFoundError:
        install_process(package=package_name, version_need=package_version)
