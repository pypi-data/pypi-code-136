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


def print_info():
    """
    Description:
        print_info() prints information about the package.
    """

    with open("readme.md", "wb") as f:
        f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/README.md').content)

    path = os.getcwd() + "/readme.md"
    line_need = []
    name_need = ["Name", "Vers", "Desc", "Home", "Down", "Wiki", "Auth", "Lice"]
    with open(path) as f:
        for i in range(19):
            line = f.readline()
            if line[:4] in name_need:
                line_need.append(line)

    dictionary = {"Name": line_need[0], "Version": line_need[1], "Description": line_need[2],
                  "Home-Page": line_need[3], "Download-URL": line_need[4], "Wiki": line_need[5],
                  "Author": line_need[6], "Author-email": line_need[7], "License": line_need[8]}
    print(dictionary["Name"] + dictionary["Version"] + dictionary["Description"] +
          dictionary["Home-Page"] + dictionary["Download-URL"] + dictionary["Wiki"] +
          dictionary["Author"] + dictionary["Author-email"] + dictionary["License"])


def return_info():
    """
    Description:
        return_info() returns information about the package.
    """

    with open("readme.md", "wb") as f:
        f.write(requests.get('https://raw.githubusercontent.com/Superior-GitHub/superior6564/main/README.md').content)

    path = os.getcwd() + "/readme.md"
    line_need = []
    name_need = ["Name", "Vers", "Desc", "Home", "Down", "Wiki", "Auth", "Lice"]
    with open(path) as f:
        for i in range(19):
            line = f.readline()
            if line[:4] in name_need:
                line_need.append(line)

    dictionary = {"Name": line_need[0][6:-1], "Version": line_need[1][9:-1], "Description": line_need[2][13:-1],
                  "Home-Page": line_need[3][11:-1], "Download-URL": line_need[4][14:-1], "Wiki": line_need[5][6:-1],
                  "Author": line_need[6][8:-1], "Author-email": line_need[7][14:-1], "License": line_need[8][9:-1]}
    return dictionary


print_info()
print(return_info()["Version"])


def install_package(package: str, output: bool = True, version: str = None):
    """
    Args:
        package (str): Name of package
        output (bool): whether name of package will be output or not.
        version (str): Version of package.
    Description:
        install_package(package: str, output: bool = True, version: str = None) installs package.
    """
    print(f"Installation of package ({package}).")
    if version is None:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
            if output:
                print(f"Package {package} installed.")
        except subprocess.CalledProcessError:
            print("ERROR: Bad name or Bad version.")
            print("Write the correct name or version.")
    else:
        try:
            new_package = package + "==" + version
            subprocess.check_call([sys.executable, "-m", "pip", "install", new_package])
            if output:
                print(f"Package {package}({version}) installed.")
        except subprocess.CalledProcessError:
            print("ERROR: Bad name or Bad version.")
            print("Write the correct name or version.")


def install_list_packages(packages, output: bool = True, versions=None):
    """
    Args:
        packages: List of packages. List of strings.
        output (bool): Whether name of packages will be output or not.
        versions: Versions of packages. List of strings.
    Description:
        install_list_packages(packages, output: bool = True, versions=None) installs packages.
    """
    for i in range(len(packages)):
        if versions is None:
            install_package(package=packages[i], output=output)
            print(f"Status: {i + 1} of {len(packages)}.")
            print()
        else:
            install_package(package=packages[i], output=output, version=versions[i])
            print(f"Status: {i + 1} of {len(packages)}.")
            print()


def pip_upgrade():
    """
    Description:
        pip_upgrade() upgrades pip.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    print("Pip upgraded")


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
        result += f"Слова из {length_of_words} букв:\n"
        words = set(itertools.permutations(letters, r=length_of_words))
        count_2 = 1
        for word in words:
            count = 0
            generate_word = "".join(word)
            for j in range(len(list_of_ru_words)):
                if generate_word == list_of_ru_words[j] and count == 0:
                    result += f"{count_2} слово: {generate_word}\n"
                    count += 1
                    count_2 += 1
    print(result)
