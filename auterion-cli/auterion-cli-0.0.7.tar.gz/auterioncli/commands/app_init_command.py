import requests
from .command_base import CliCommand


class AppInitCommand(CliCommand):
    @staticmethod
    def help():
        return 'Initialize a new Auterion app repository'

    def __init__(self, config):
        pass

    def setup_parser(self, parser):
        pass

    def run(self, args):
      print('Not implemented yet. This will template a new app for you')
