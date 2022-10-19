import argparse

class CliCommand:
    @staticmethod
    def help():
        return None

    def setup_parser(self, parser: argparse.ArgumentParser):
        pass

    def run(self, args):
        pass
