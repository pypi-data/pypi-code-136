import argparse

def parser():
	parse = argparse.ArgumentParser()
	parse.add_argument("--gitrepo", "-g", help="repository link", type=str)

	return parse.parse_args()