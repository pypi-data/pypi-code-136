'''
Created on Mar 15, 2016

@author: startechm
'''

import configparser
import os
import sys
import traceback
import psycopg2
import getpass

CFG_PATH = 'config/db.cnf'
DB_SECTION = 'xtmigrations'  # main section: later we can have different name


def get_config():
    
    try:
        parser = configparser.RawConfigParser()
        parser.read(f"{os.getcwd()}/{CFG_PATH}")

        # Make sure all fields are present in the config file
        if not parser.has_section(DB_SECTION):
            raise Exception(f"{DB_SECTION} must be in config file")

        required_opts = ['engine', 'host', 'port', 'database', 'schema', 'user']  # password is optional

        config = dict(parser.items(DB_SECTION))
        config_keys = config.keys()

        err = ""
        for opt in required_opts:
            if not opt in config_keys:
                err = f"{err}{opt} option not present in config file under section [{DB_SECTION}]\n"
        
        if err != "":
            raise Exception(err)

        # Checking that postgresql is the only supported engine
        if config['engine'] != 'postgresql':
            raise Exception(f"Engine {config['engine']} not supported.  The only supported engine currently is postgresql")

        return config
    except:
        raise


def get_conn(config):

    try:

        db_pw = config.get('password')
        if not db_pw:
            db_pw = getpass.getpass()

        conn_dict = {
            'host': config['host'],
            'port': config['port'],
            'database': config['database'],
            'user': config['user'],
            'password': db_pw,
            'options': f"-c search_path={config['schema']}"
        }

        # print("Connecting to database\n    ->%s" %(conn_string))
        # conn = psycopg2.connect(conn_string)
        conn = psycopg2.connect(**conn_dict)
        conn.set_session(isolation_level=None, readonly=None, deferrable=None, autocommit=True)

        return conn
    except SystemExit as se:
        raise se
    except:
        # e, tb = sys.exc_info()[0]
        type, val, tb = sys.exc_info()
        raise Exception("Unable to get DB connection.  Check your config file and your network.") from val
