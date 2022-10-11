import argparse
from pathlib import Path


class PyConfig:
    @classmethod
    def new(cls, name, value):
        """
        Creates a new config variable
        
        Parameters:
        name: Key of your config variable
        value: Value of your config variable
        """
        cls.__create_ignore()
        
        formatted = f"{name} = {value}\n"
        config_path = Path('config.py')
        if config_path.exists():
            with open('config.py', 'r') as data:
                content = data.readlines()
                content.append(formatted)
                with open('config.py', 'w') as config:
                    config.writelines(content)
        else:
            with open("config.py", 'w') as config:
                config.write(formatted)
    
    @classmethod
    def __create_ignore(cls):
        git_ignore_path = Path(".gitignore")
        if not git_ignore_path.exists():
            with open(".gitignore", 'w') as git_ignore:
                git_ignore.write("config.py")


def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    instance = subparser.add_parser('new', help="Create new config variable.")
    instance.add_argument('name', help="Name of the config variable.")
    instance.add_argument('value', help="Value of the config variable.")

    args = parser.parse_args()
    PyConfig.new(args.name, args.value)