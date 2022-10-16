"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564
"""
import requests
import os
import subprocess
import sys
from IPython.display import Image, display
import itertools


def get_info(package: str = "superior6564", mode: str = "print"):
    """
    Args:
        package (str): Name of package for getting info.
        mode (str): Mode of getting info ("print", "return" or "all").
    Description:
        get_info() gives information about the package.\n
        Before you can get info about the package, you have to download it.
    """
    package_show = subprocess.run([sys.executable, "-m", "pip", "show", package], capture_output=True, text=True)
    if package_show.stderr.split('\n')[0][:30] != "WARNING: Package(s) not found:":
        lines = package_show.stdout.split('\n')[:-4]
        dictionary = {"Name": lines[0], "Version": lines[1], "Description": "Description:" + lines[2][8:],
                      "Home-Page": lines[3], "Author": lines[4], "Author-email": lines[5], "License": lines[6]}
        if mode == "print" or mode == "return" or mode == "all":
            if mode == "print" or mode == "all":
                for name in dictionary:
                    print(dictionary[name])
            if mode == "return" or mode == "all":
                new_dictionary = {"Name": dictionary["Name"][6:], "Version": dictionary["Version"][9:], "Description": dictionary["Description"][13:],
                                  "Home-Page": dictionary["Home-Page"][11:], "Author": dictionary["Author"][8:],
                                  "Author-email": dictionary["Author-email"][14:], "License": dictionary["License"][9:]}
                return new_dictionary
        else:
            print("Incorrect mode")
    else:
        print("Before you can get info about the package, you have to download it.")


def install_package(package: str, version: str = None, output: bool = True):
    """
    Args:
        package (str): Name of package.
        version (str|None): Version of package.
        output (bool): Info about process will be output or not.
    Description:
        install_package() installs package.
    """
    if version is None:
        if output:
            print(f"Trying to install package {package}.")
        install_output = subprocess.run([sys.executable, "-m", "pip", "install", package], capture_output=True, text=True)
        if install_output.stderr.split('\n')[0][:31] == "ERROR: Could not find a version":
            print("ERROR: Bad name or Bad version.")
            print("Write the correct name or version.")
        else:
            uprade_output = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package], capture_output=True, text=True)
            print(f"Package {package} installed.")
    else:
        if output:
            print(f"Trying to install package {package} with version {version}.")
        new_package = package + "==" + version
        install_output = subprocess.run([sys.executable, "-m", "pip", "install", new_package], capture_output=True, text=True)
        if install_output.stderr.split('\n')[0][:31] == "ERROR: Could not find a version":
            print("ERROR: Bad name or Bad version.")
            print("Write the correct name or version.")
        else:
            if output:
                if install_output.stdout.split('\n')[0][:29] == "Requirement already satisfied":
                    print(f"Package {package} with version {version} is already installed.")
                elif install_output.stdout.split('\n')[0][:10] == "Collecting":
                    print(f"Package {package} with version {version} installed.")


def install_list_packages(packages, versions=None, output: bool = True):
    """
    Args:
        packages (list): List of packages. List of strings.
        versions (list|None): Versions of packages. List of strings.
        output (bool): Info about process will be output or not.
    Description:
        install_list_packages() installs packages.
    """
    for i in range(len(packages)):
        if versions is None:
            install_package(package=packages[i], output=output)
            print(f"Status: {i + 1} of {len(packages)}.")
            print()
        else:
            install_package(package=packages[i], version=versions[i], output=output)
            print(f"Status: {i + 1} of {len(packages)}.")
            print()


def pip_upgrade():
    """
    Description:
        pip_upgrade() upgrades pip.
    """
    pip_version = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True).stdout.split('\n')[0][4:8]
    print(f"Version before checking is {pip_version}.")
    upgrade_pip = subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], capture_output=True, text=True)
    pip_version = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True).stdout.split('\n')[0][4:8]
    print(f"Version after checking and upgrading is {pip_version}.")


def show_degget():
    """
    Description:
        show_degget() shows image of degget.
    """
    with open("degget_elite.jpg", "wb") as f:
        f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/superior6564/degget_elite.jpg').content)

    display(Image(filename="degget_elite.jpg"))


def gen_ru_words():
    """
    Description:
        gen_ru_words() generates RU words.
    """
    with open("russian_nouns.txt", "wb") as f:
        f.write(requests.get(
            'https://raw.githubusercontent.com/Superior-GitHub/Superior6564/main/superior6564/russian_nouns.txt').content)

    print("Write all of letters which do you have")
    letters = input("Write in this line: ")
    print("Write length of words which do you need")
    length_of_words = int(input("Write in this line: "))
    with open('russian_nouns.txt', encoding='utf-8') as f:
        list_of_ru_words = []
        for i in range(51300):
            list_of_ru_words.append(f.readline()[0:-1])
        result = ""
        result += f"Words from {length_of_words} letters:\n"
        words = set(itertools.permutations(letters, r=length_of_words))
        count_2 = 1
        for word in words:
            count = 0
            generate_word = "".join(word)
            for j in range(len(list_of_ru_words)):
                if generate_word == list_of_ru_words[j] and count == 0:
                    result += f"{count_2} word: {generate_word}\n"
                    count += 1
                    count_2 += 1
    print(result)
