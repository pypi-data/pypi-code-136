'''
## SpeedDB CLI

'''

import argparse

from .database import build_db, destroy_db, get_version
from .database import init as db_init

from .shell import run_shell

version = get_version("__init__.py")

parser = argparse.ArgumentParser("SpeeddDB", description="SpeedDB CLI")

parser.add_argument('-v', '--version', action='version', version=f'SpeedDB {version}', help='Show version')

command = parser.add_subparsers(title='commands', dest='command')

init = command.add_parser("init", help="Initialize a folder that's used to store databases")
init.add_argument("-n", "--name", type=str, help="Folder Name")

build = command.add_parser("build", help="Build new database")
build.add_argument("name", nargs="+", help="Database Name")
build.add_argument("-m", "--model", type=str, help="Database Model (documents/keyval/...)", required=True)

destroy = command.add_parser("destroy", help="Destroy and delete an entire database (can't be undone)")
destroy.add_argument("name", type=str, help="Database Name")

destroy = command.add_parser("shell", help="Run an interactive python shell to manipulate your databases")
destroy.add_argument("-d", "-dbs-path", type=str, help="Databases path")

# destroy = command.add_parser("browser", help="")
# destroy.add_argument("-d", "-dbs-path", type=str, help="Databases path")

def runner():
   main(parser.parse_args())

def main(args: argparse.Namespace):
   if args.command == "init":
      db_init(args.name)

   if args.command == "build":
      result = build_db(*args.name, model=args.model)
      if result:
         parser.error(result)

   if args.command == "destroy":
      destroy_db(args.name)
   
   if args.command == "shell":
      run_shell(args.d)

if __name__ == "__main__":
   runner()