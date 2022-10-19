#!/bin/env python3
"""A command-line interface for LADOK 3"""

import appdirs
import argcomplete, argparse
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass
import json
import keyring
import os
import pickle
import re
import sys
import traceback

import ladok3.data
import ladok3.report

dirs = appdirs.AppDirs("ladok", "dbosk@kth.se")

def err(rc, msg):
  print(f"{sys.argv[0]}: error: {msg}", file=sys.stderr)
  traceback.print_exc(file=sys.stderr)
  sys.exit(rc)

def warn(msg):
  print(f"{sys.argv[0]}: {msg}", file=sys.stderr)
def store_ladok_session(ls, credentials):
  if not os.path.isdir(dirs.user_cache_dir):
    os.mkdir(dirs.user_cache_dir)

  file_path = dirs.user_cache_dir + "/LadokSession"

  pickled_ls = pickle.dumps(ls)
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=credentials[0].encode("utf-8"),
    iterations=100000
  )
  key = base64.urlsafe_b64encode(kdf.derive(credentials[1].encode("utf-8")))

  fernet_protocol = Fernet(key)
  encrypted_ls = fernet_protocol.encrypt(pickled_ls)

  with open(file_path, "wb") as file:
    file.write(encrypted_ls)
  
def restore_ladok_session(credentials):
  file_path = dirs.user_cache_dir + "/LadokSession"

  if os.path.isfile(file_path):
    with open(file_path, "rb") as file:
      encrypted_ls = file.read()
      kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=credentials[0].encode("utf-8"),
        iterations=100000
      )
      key = base64.urlsafe_b64encode(kdf.derive(credentials[1].encode("utf-8")))

      fernet_protocol = Fernet(key)
      try:
        pickled_ls = fernet_protocol.decrypt(encrypted_ls)
      except Exception as err:
        warn(f"cache was corrupted, cannot decrypt: {err}")
        pickled_ls = None
      return pickle.loads(pickled_ls)

  return None
def update_credentials_in_keyring(ls, args):
  user = input("LADOK username: ")
  passwd = getpass.getpass("LADOK password: [input is hidden]")

  keyring.set_password("ladok3", "username", user)
  keyring.set_password("ladok3", "password", passwd)

  clear_cache(ls, args)
def load_credentials(filename="config.json"):
  """Load credentials from environment or file named filename"""
  try:
    user = keyring.get_password("ladok3", "username")
    passwd = keyring.get_password("ladok3", "password")
    if user and passwd:
      return user, passwd
  except:
    pass

  try:
    user = os.environ["LADOK_USER"]
    passwd = os.environ["LADOK_PASS"]
    return user, passwd
  except:
    pass

  try:
    with open(filename) as conf_file:
      config = json.load(conf_file)
    return config["username"], config["password"]
  except:
    pass

  return None, None
def clear_cache(ls, args):
  try:
    os.remove(dirs.user_cache_dir + "/LadokSession")
  except FileNotFoundError as err:
    pass

  sys.exit(0)
def main():
  """Run the command-line interface for the ladok command"""
  argp = argparse.ArgumentParser(
    description="This is a CLI-ification of LADOK3's web GUI.",
    epilog="Web: https://github.com/dbosk/ladok3"
  )
  argp.add_argument("-f", "--config-file",
    default=f"{dirs.user_config_dir}/config.json",
    help="Path to configuration file "
      f"(default: {dirs.user_config_dir}/config.json) "
      "or set LADOK_USER and LADOK_PASS environment variables.")
  subp = argp.add_subparsers(
    title="commands",
    dest="command",
    required=True
  )
  login_parser = subp.add_parser("login",
    help="Manage login credentials",
    description="""
  Manages the user's LADOK login credentials (only credentials at KTH supported 
  right now). There are three ways to supply the login credentials, in order of 
  priority:

  1) Through the system keyring: Just run `ladok login` and you'll be asked to 
     enter the credentials and they will be stored in the keyring.

  2) Through the environment: Just set the environment variables LADOK_USER and 
     LADOK_PASS.

  3) Through the configuration file: Just write

        {
          "username": "the actual username",
          "password": "the actual password"
        }

     to the file """ + dirs.user_config_dir + """/config.json (default, or use 
     the -f option).
  """
  )
  login_parser.set_defaults(func=update_credentials_in_keyring)
  cache_parser = subp.add_parser("cache",
    help="Manage cache",
    description="Manages the cache of LADOK data"
  )
  cache_subp = cache_parser.add_subparsers(
    title="subcommands",
    dest="subcommand",
    required=True
  )
  cache_clear = cache_subp.add_parser("clear",
    help="Clear the cache",
    description="Clears everything from the cache"
  )
  cache_clear.set_defaults(func=clear_cache)
  ladok3.data.add_command_options(subp)
  ladok3.report.add_command_options(subp)
  argcomplete.autocomplete(argp)
  args = argp.parse_args()
  LADOK_USER, LADOK_PASS = load_credentials(args.config_file)
  ls = restore_ladok_session([LADOK_USER, LADOK_PASS])
  if not ls:
    ls = ladok3.LadokSessionKTH(LADOK_USER, LADOK_PASS)
  if "func" in args:
    args.func(ls, args)
  store_ladok_session(ls, [LADOK_USER, LADOK_PASS])

if __name__ == "__main__":
  try:
    main()
    sys.exit(0)
  except Exception as e:
    err(-1, e)
