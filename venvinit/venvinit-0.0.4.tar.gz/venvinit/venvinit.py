#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import shutil
import subprocess
import sys
import time
import requests
from configparser import ConfigParser as cp
import curses


####################
# GLOBAL VARIABLES #
####################

CWD = os.getcwd()
CONFIG_PATH = f"{CWD}/.venvinit.config.ini"
VERSION = "0.0.4"

####################
#      COLORS      #
####################
class Colors:
    GREEN = '\033[0;49;32m'
    BLUE = '\033[0;49;34m'
    YELLOW = '\033[0;49;93m'
    RED = '\033[0;49;91m'
    BOLD = '\033[;1m'
    UNDERLINE = '\033[;4m'
    END = '\033[0m'
    GRAY = '\033[0;49;90m'
    WHITE = '\033[0;49;97m'

    curses.initscr()
    SUPPORT_COLORS = curses.has_colors()
    curses.endwin()

    @staticmethod
    def clr(text, color, bold=False):
        if Colors.SUPPORT_COLORS:
            if bold:
                return f"{color}{Colors.BOLD}{text}{Colors.END}"
            else:
                return f"{color}{text}{Colors.END}"
        else:
            return text

    @staticmethod
    def bold(text, color=None):
        if color:
            return Colors.clr(text, color, bold=True)
        else:
            return Colors.clr(text, Colors.WHITE, bold=True)

    @staticmethod
    def underline(text, color=None):
        if not Colors.SUPPORT_COLORS:
            return text
        if color:
            return f"{color}{Colors.UNDERLINE}{text}{Colors.END}"
        else:
            return f"{Colors.UNDERLINE}{text}{Colors.END}"


###############
#   CONFIGS   #
###############

class Config:
    def __init__(self, init=False, venv_name=".venv", pip_path="pip", python_path="python"):
        self.config = cp()
        self.config.read(CONFIG_PATH)
        self.config.sections()
        if init:
            # venv info
            self.config.add_section("venv")
            self.config.set("venv", "name", venv_name)
            self.save()

            # python version
            self.config.add_section("python")
            self.config.set("python", "version", sys.version.split(" ")[0])
            self.config.set("python", "path", python_path)
            self.save()

            # pip
            self.config.add_section("pip")
            self.config.set("pip", "version", subprocess.check_output(["pip", "--version"]).decode("utf-8").split(" ")[1])
            self.config.set("pip", "path", pip_path)
            self.save()

        self.venv_name = self.get("venv", "name")
        self.python_version = self.get("python", "version")
        self.pip_version = self.get("pip", "version")

    def __str__(self):
        return f"venv name: {self.venv_name}\npython version: {self.python_version}\npip version: {self.pip_version}"

    def get(self, section, option):
        return self.config.get(section, option)

    def set(self, section, option, value):
        self.config.set(section, option, value)

    def save(self):
        with open(CONFIG_PATH, "w") as f:
            self.config.write(f)

    def remove(self):
        os.remove(CONFIG_PATH)

        
class GetConfig:
    def __init__(self):
        # check if config file exists
        if not os.path.exists(CONFIG_PATH):
            print(f"venvinit : error : Config file not found. Run {Colors.bold('venvinit create')} first.")
            exit(1)

        # get config
        self.cfg = cp()
        self.cfg.read(CONFIG_PATH)
        self.cfg.sections()

        self.venv_name = self.cfg.get("venv", "name")
        self.python_version = self.cfg.get("python", "version")
        self.pip_version = self.cfg.get("pip", "version")

    def remove(self):
        os.remove(CONFIG_PATH)

    def __str__(self):
        return f"venv name: {self.venv_name}\npython version: {self.python_version}\npip version: {self.pip_version}"

####################
#      VENV        #
####################

class Venv:
    def __init__(self, venv_name=".venv"):
        self.venv_name = venv_name
        self.venv_path = f"{CWD}/{self.venv_name}"
        self.venv_bin = f"{self.venv_path}/bin/python3"
        self.cfg = None

    def __str__(self):
        return f"venv name: {self.venv_name}\nvenv path: {self.venv_path}\nvenv bin: {self.venv_bin}"

    def init(self):
        if not os.path.exists(self.venv_path):
            print(Colors.clr("Creating virtual environment", Colors.GRAY) + f" {Colors.clr(self.venv_name, Colors.WHITE)}")
            if os.name == "nt":
                subprocess.call(["py", "-m", "venv", f"{self.venv_name}"])
                print(Colors.clr("Virtual environment created", Colors.GREEN))
                print(Colors.clr("Config saved to ", Colors.GRAY) +
                      Colors.clr(CONFIG_PATH, Colors.WHITE))
                self.cfg = Config(init=True, venv_name=self.venv_name, pip_path=f"{self.venv_path}/Scripts/pip", python_path=f"{self.venv_path}/Scripts/python")
            else:
                subprocess.call(["python3", "-m", "venv", f"{self.venv_name}"])
                print(Colors.clr("Virtual environment created", Colors.GREEN))
                print(Colors.clr("Config saved to ", Colors.GRAY) +
                      Colors.clr(CONFIG_PATH, Colors.WHITE))
                self.cfg = Config(init=True, venv_name=self.venv_name, pip_path=f"{self.venv_path}/bin/pip", python_path=f"{self.venv_path}/bin/python")
        else:
            print(Colors.clr("Virtual environment already exists", Colors.RED))

    def upgradePip(self):
        print(Colors.clr("Upgrading pip", Colors.GRAY))
        subprocess.call([self.cfg.get("pip", "path"), "install", "--upgrade", "pip"])
        print(Colors.clr("Pip upgraded", Colors.GREEN))
        # update config
        self.cfg.set("pip", "version", subprocess.check_output([self.cfg.get("pip", "path"), "--version"]).decode("utf-8").split(" ")[1])

    def installDeps(self, deps=f"{CWD}/requirements.txt"):
        if deps == "1":
            deps = f"{CWD}/requirements.txt"
        print(Colors.clr("Installing dependencies", Colors.GRAY))
        subprocess.call([self.cfg.get("pip", "path"), "install", "-r", deps])
        with open(deps, "r") as f:
            print(Colors.clr(f"{len(f.readlines())} dependencies installed", Colors.GRAY))

    def remove(self, force=False, name=None):
        self.venv_name = name or GetConfig().venv_name
        self.venv_path = f"{CWD}/{self.venv_name}"
        if os.path.exists(self.venv_path):
            if force:
                shutil.rmtree(self.venv_path)
                print(Colors.clr("Virtual environment removed", Colors.GREEN) + f" {Colors.clr(self.venv_name, Colors.WHITE)}")
                GetConfig().remove()
            else:
                print(Colors.clr("Are you sure you want to remove the virtual environment", Colors.RED) +
                      f" {Colors.clr(self.venv_name, Colors.WHITE)}" +
                      Colors.clr("?", Colors.RED))
                print(Colors.clr("Type", Colors.GRAY) + Colors.clr(" '(y/n)'", Colors.WHITE) +
                      Colors.clr(" to confirm", Colors.GRAY))
                confirm = input()
                if confirm.lower() in ["y", "yes"]:
                    shutil.rmtree(self.venv_path)
                    print(Colors.clr("Virtual environment removed", Colors.GREEN) + f" {Colors.clr(self.venv_name, Colors.WHITE)}")
                    GetConfig().remove()
                else:
                    print(Colors.clr("Virtual environment not removed", Colors.RED))
        else:
            print(Colors.clr("Virtual environment does not exist", Colors.RED))

####################
# VERSION CONTROL  #
####################
class VersionControl:
    """
    check if there is not more recent package of venvinit
    """

    def __init__(self):
        self.venvinit_version = subprocess.check_output(
            ["pip", "show", "venvinit"]).decode("utf-8").split("Version: ")[1].split(" ")[0]

    def check(self):
        self.latest_version = requests.get(
            "https://pypi.org/pypi/venvinit/json").json()["info"]["version"]
        if self.venvinit_version < self.latest_version:
            print(Colors.clr(
                "There is a newer version of venvinit available", Colors.YELLOW))
            print(Colors.clr("Current version: ", Colors.GRAY) +
                  Colors.clr(f"{self.venvinit_version}", Colors.WHITE))
            print(Colors.clr("Latest version: ", Colors.GRAY) +
                  Colors.clr(f"{self.latest_version}", Colors.WHITE))
            print(Colors.clr("Run ", Colors.GRAY) + Colors.clr("pip install --upgrade venvinit",
                  Colors.WHITE) + Colors.clr(" to upgrade", Colors.GRAY))
        else:
            print(Colors.clr("venvinit is up to date", Colors.GREEN))



####################
#    MAIN CLI      #
####################

def main():
    """
    venvint
    =======
    USAGE : venvinit [COMMAND] [ATTR | OPTIONS]

    LIST OF COMMANDS
    ----------------
    create : create a new virtual environement
        venvinit create -y : create a virtual environement with default values
        venvinit create : create step by step a virtual environement
        venvinit create -n [ENV_NAME] : create a virtual environement with the name [ENV_NAME]
        venvinit create [ENV_NAME] -deps : create a virtual environement with the name [ENV_NAME] and install dependencies from requirements.txt
        venvinit create [ENV_NAME] -deps [DEPS_FILE] : create a virtual environement with the name [ENV_NAME] and install dependencies from [DEPS_FILE]

    remove : remove a virtual environement
        venvinit remove : remove the virtual environnement in the '.venvinit.config.ini'
        venvinit -f remove : remove the virtual environnement in the '.venvinit.config.ini' without confirm

    help : show help
    """

    if len(sys.argv) == 1:
        print(main.__doc__)
    elif len(sys.argv) == 2:
        if sys.argv[1] in ["version", "-v", "--version"]:
            print(Colors.clr("venvinit", Colors.WHITE))
            print(f'v{VERSION}')
            print(Colors.clr("MIT LICENSE", Colors.WHITE))
            vc = VersionControl()
            vc.check()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="venvinit", usage="venvinit [COMMAND] [ATTR | OPTIONS]")
    parser.add_argument("command", help="create | remove | help")
    parser.add_argument("attr", help="venv_name | -deps | -f", nargs="?")
    parser.add_argument("-n", "--name", help="name of the virtual environement")
    parser.add_argument("-d", "--dependencies", help="dependencies file or flag")
    parser.add_argument("-f", "--force", help="force remove", action="store_true")
    parser.add_argument("-y", "--yes", help="yes to all", action="store_true")
    parser.add_argument("-v", "--version", help="show version", action="store_true")
    args = parser.parse_args()

    # set start time
    start_time = time.time()

    # create command
    if args.command == "create":
        if args.yes:
            venv = Venv()
            venv.init()
            venv.upgradePip()
            print(Colors.underline(f"{str(time.time() - start_time)} s", Colors.GRAY))
        elif args.name:
            venv = Venv(venv_name=args.name)
            venv.init()
            venv.upgradePip()
            print(Colors.underline(
                f"{str(time.time() - start_time)} s", Colors.GRAY))
        else:
            envName = input(Colors.clr("Enter the name of the virtual environment", Colors.GRAY) + " : ")
            currentTime = time.time()
            start_time = currentTime - start_time
            venv = Venv(venv_name=envName)
            venv.init()
            venv.upgradePip()
            currentEndTime = time.time() - currentTime
            deps = input(Colors.clr("Do you want to install dependencies", Colors.GRAY) + " (y/n) : ")
            if deps.lower() in ["y", "yes"]:
                depsFile = input(Colors.clr("Enter the name of the requirements source ", Colors.GRAY) + Colors.clr("(requirements.txt)", Colors.WHITE) + " : ")
                if depsFile == "":
                    depsFile = "requirements.txt"
                newTime = time.time()
                venv.installDeps(depsFile)
                end_time = time.time() - newTime
                currentEndTime -= end_time

            print(Colors.underline(f"{str(currentEndTime)} s", Colors.GRAY))

        if args.dependencies:
            start_time = time.time()
            venv.installDeps(deps=args.dependencies)
            print(Colors.underline(f"{str(time.time() - start_time)} s", Colors.GRAY))


    # remove command
    elif args.command == "remove":
        if args.force:
            venv = Venv()
            venv.remove(force=True)
        elif args.attr:
            venv = Venv()
            venv.remove(name=args.attr)
        else:
            venv = Venv()
            venv.remove()

    # help command
    elif args.command == "help":
        print(main.__doc__)


if __name__ == "__main__":
    main()
