import configparser
import os

CONFIG = configparser.ConfigParser()

if os.path.exists('config.ini'):
    os.remove('config.ini')

IP = '10.157.1.249'
# IP = '10.10.5.108'

# CONFIG CONTENT
CONFIG['URL'] = {}
CONFIG['URL']['URL'] = 'http://{}:8888/'.format(IP)
CONFIG['URL']['API'] = 'api'
CONFIG['URL']['MANUAL'] = 'manual'


CONFIG['SERVICE'] = {}
CONFIG['SERVICE']['tcc'] = 'tcc'
CONFIG['SERVICE']['pro'] = 'pro'
CONFIG['SERVICE']['mm'] = 'mm'
CONFIG['SERVICE']['db'] = 'db'
CONFIG['SERVICE']['dvs'] = 'dvs'


CONFIG['PROTOCOL'] = {}
CONFIG['PROTOCOL']['gw698'] = 'gw698'
CONFIG['PROTOCOL']['dlms'] = 'dlms'
CONFIG['PROTOCOL']['dlt645'] = 'dlt645'


CONFIG['EM'] = {}
CONFIG['EM']['ip'] = '10.10.101.233'
CONFIG['EM']['port'] = '4445'


CONFIG['RABBITMQ'] = {}
CONFIG['RABBITMQ']['host'] = IP
CONFIG['RABBITMQ']['port'] = '5672'
CONFIG['RABBITMQ']['username'] = 'admin'
CONFIG['RABBITMQ']['password'] = 'auto@T0001'


CONFIG['REDIS'] = {}
CONFIG['REDIS']['host'] = IP
CONFIG['REDIS']['password'] = 'auto@T0001'
CONFIG['REDIS']['encoding'] = 'utf-8'
CONFIG['REDIS']['db'] = '0'
CONFIG['REDIS']['max_conn'] = '20'


CONFIG['DB'] = {}
CONFIG['DB']['mysql'] = 'mysql+pymysql://root:autoTT0001@{}:3306/autotest'.format(IP)


with open('config.ini', 'w') as file:
    CONFIG.write(file)