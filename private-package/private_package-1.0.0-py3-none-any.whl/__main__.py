#! /usr/bin/env python3

import os
import shutil
import getpass
from os.path import join, dirname, isdir
from .utils.functions import parser
from .utils.Class import Style, Color

ROOT_DIR = dirname(__file__)
REPO_DIR = join(ROOT_DIR, "repo")

def main():
	args = parser()

	gitrepo = args.gitrepo

	if gitrepo:
		if not isdir(REPO_DIR):
			os.mkdir(REPO_DIR)

		print(Color.primary(f"[private-py]: start cloning repository..."))
		os.system(f"git clone {gitrepo} {REPO_DIR}")

		print()

		print(Color.primary(f"[private-py]: start installing package..."))
		os.system(f"pip install {REPO_DIR}")


		# remove repo directory
		shutil.rmtree(REPO_DIR)

		print()
		print(Color.success("++++++++++++++++++++++++"))
		print(Color.success("        SUCCESS         "))
		print(Color.success("++++++++++++++++++++++++"))


if __name__ == '__main__':
	main()