
from __future__ import unicode_literals
import logging
import os
import configparser
cofig= configparser.RawConfigParser()
import sys

from configparser import SafeConfigParser, ConfigParser

try:
    ospath = os.environ.get('ND_HOME')
    path = ospath + '/python/config/ndsettings.conf'
except Exception as e:
    print("ND HOME NOT SET")
    raise e

#print("path of  NDC config : ", path)

#configParser.read(path)
#path_for_insProfile = configParser.get('PYTHON_AGENT', 'path_profile')

myvars = {}
with open(path) as myfile:
    for line in myfile:
        name, var = line.partition("=")[::2]
        myvars[name.strip()] = var
        #print("myvars----------------------->",myvars)
#TIER = myvars['tier'].strip('\n')
#SERVER = myvars['server'].strip('\n')




int_or_none = lambda v: int(v) if v != '' else None
on_off = lambda v: v.lower() in ('on', 'true', 'yes', 'y', 't', '1')
comma_seperated_list = lambda v: v.replace(' ', '').split(',')

keys = lambda d: d.keys()
values = lambda d: d.values()
# Configuration Options

_CONFIG_OPTIONS_BY_SECTION = {

    'agent': {
        'app': ('APP_NAME', None),
        'tier': ('TIER_NAME', None),
        'node': ('NODE_NAME', None),
        'dir': ('DIR', None),
    },

    'wsgi': {
        'script': ('WSGI_SCRIPT_ALIAS', None),
        'callable': ('WSGI_CALLABLE_OBJECT', None),
        'module': ('WSGI_MODULE', None),
    },

    'log': {
        'dir': ('LOGS_DIR', None),
        'level': ('LOGGING_LEVEL', None),
        'debugging': ('DEBUG_LOG', on_off)
    },

    'proxy': {
        'proxymode': ('PROXY_MODE', None),
        'proxycontype': ('PROXY_CON_TYPE', None),
        'proxyip': ('PROXY_IP', None),
        'proxyport': ('PROXY_PORT', None),
        'sopath': ('SO_PATH', None),
       },
}


# Defaults ###########


CONFIG_FILE = ''

# Agent
APP_NAME = 'CavAgent'
#TIER_NAME = 'test_tier'
#NODE_NAME = 'test'
DIR = ospath + '/python/CavAgent'
TIER = myvars['tier'].strip('\n')
SERVER = myvars['server'].strip('\n')


# Logging
LOGS_DIR = ospath+'/python/CavAgent/logs'
print("LOGS_DIR", LOGS_DIR)

if "CAV_APP_AGENT_LoggingLevel" in os.environ:
    LOGGING_LEVEL = os.environ.get('CAV_APP_AGENT_LoggingLevel')
else:
    LOGGING_LEVEL = "WARNING"

DEBUG_LOG = False


# WSGI
WSGI_MODULE = ''
#WSGI_SCRIPT_ALIAS = '/home/cavisson/shop/my-shop/wsgi_example_app.py'
#WSGI_SCRIPT_ALIAS = input("Enter the absolute path of WSGI application script. (command to get 'readlink -f <script_path.py>') : ")
WSGI_SCRIPT_ALIAS = ''
WSGI_CALLABLE_OBJECT = ''

# Controller
CONTROLLER_HOST = '10.20.0.85'
CONTROLLER_PORT = '7892'
SSL_ENABLED = False
ACCOUNT_NAME = ''
ACCOUNT_ACCESS_KEY = ''
HTTP_PROXY_HOST = '10.20.0.79'
HTTP_PROXY_PORT = '1112'
HTTP_PROXY_USER = ''
HTTP_PROXY_PASSWORD_FILE = ''
'''
# Proxy Runtime
PROXY_RUN_DIR = ''

# Proxy Control Service
PROXY_CONTROL_PATH = ''
PROXY_STARTUP_READ_TIMEOUT_MS = 2000
PROXY_STARTUP_INITIAL_RETRY_DELAY_MS = 5000
PROXY_STARTUP_MAX_RETRY_DELAY_MS = 300000

# Config Service
PROXY_CONFIG_SOCKET_NAME = '0'
CONFIG_SERVICE_RELOAD_INTERVAL_MS = 5000
CONFIG_SERVICE_MAX_RETRIES = 3

# Transaction Service
PROXY_INFO_SOCKET_NAME = '0'
PROXY_REPORTING_SOCKET_NAME = '1'
BT_INFO_REQUEST_TIMEOUT_MS = 100

# Snapshot Service
INCLUDE_AGENT_FRAMES = False
SNAPSHOT_PROFILER_INTERVAL_MS = 10
EXIT_CALL_DETAILS_LENGTH = 100
FORCED_SNAPSHOT_INTERVAL = 10

# Transaction Monitor Service
BT_MAX_DURATION_MS = 30 * 60 * 1000
BT_ABANDON_THRESHOLD_MULTIPLIER = 6

# EUM
EUM_DISABLE_COOKIE = False
EUM_USER_AGENT_WHITELIST = ['Mozilla', 'Opera', 'WebKit', 'Nokia']
'''
#RUNNING_MODE = 0

def validate_config(config):
  
    return True


def parse_environ(environ=None, prefix='CAV_'):

    logger = logging.getLogger('pythonagent.agent')
    environ = environ if environ is not None else os.environ

    config = {}
    config_file = environ.get('CAV_CONFIG_FILE')

    if config_file:
        config = parse_config_file(config_file)

    #environ['SO_PATH'] = config['SO_PATH']
    option_descrs = {}

    for options in values(_CONFIG_OPTIONS_BY_SECTION):
        for name, handler in values(options):
            option_descrs[prefix + name] = (name, handler)

    for option in keys(environ):
        if option not in option_descrs:
            continue

        name, handler = option_descrs[option]

        try:
            value = environ[option]
            if handler:
                value = handler(value)
            config[name] = value
        except:
            logger.exception('ignoring %s from environment, parsing value caused exception', option)

    return config


def parse_config_file(filename):
    return None
    logger = logging.getLogger('pythonagent.agent')

    try:
        config = {}
        parser = ConfigParser()

        with open(filename) as fp:
            parser.readfp(fp)

        for section_name in parser.sections():
            try:
                options_map = _CONFIG_OPTIONS_BY_SECTION[section_name]
            except KeyError:  # Unknown section
                logger.warning('%s: skipping unrecognized section [%s]', filename, section_name)
                continue

            for option_name in parser.options(section_name):
                try:
                    env_name, handler = options_map[option_name]

                    value = parser.get(section_name, option_name)
                    if handler:
                        value = handler(value)

                    config[env_name] = value
                except KeyError:  # Unknown option
                    logger.warning('%s: skipping unrecognized option %r of section [%s]',
                                   filename, option_name, section_name)
                except:  # Other errors
                    logger.exception('%s: parsing value for option %r of section [%s] raised exception',
                                     filename, option_name, section_name)

        return config
    except:
        logger.exception('Parsing config file failed.')


def merge(config):

    #mod = globals()
    #mod.update(config)
    update_computed_defaults()


def update_computed_defaults():
    global LOGS_DIR, PROXY_CONTROL_PATH, PROXY_RUN_DIR

    PROXY_RUN_DIR = os.path.join(DIR, 'run')

    #if not PROXY_CONTROL_PATH:
    #    PROXY_CONTROL_PATH = os.path.join(PROXY_RUN_DIR, 'comm')

    if not LOGS_DIR:
        LOGS_DIR = os.path.join(DIR, 'logs')
