import sys
import time
import argparse
import colorama
from termcolor import colored
sys.path.append("..")
from tools.list_devices import list_devices
from tools.monitor import monitor
from robodyno_components_python.interfaces import CanBus
from robodyno_components_python.components import Motor

colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description='Robodyno command line tools.')
parser.add_argument('command', choices=['list', 'monitor', 'motor'], help='''
                        list all robodyno devices
                        / monitor messages on bus
                        / motor basic operations
                    ''')
parser.add_argument('--id', type=str, nargs='*', default=[], 
                    help='robodyno device id filter')
parser.add_argument('-c', '--channel', type=str, default='can0',
                    help='can bus channel')
parser.add_argument('-b', '--bitrate', type=str, default='CAN_1M',
                    help='can bus bitrate')

args = parser.parse_args()

def parse_id(str_list):
    """parse list of hex id from string format
    
    Args:
        str_list: string id list
    
    Returns:
        hex id list
    """
    if len(str_list) > 0 and str_list[0] == 'all':
        return [id for id in range(0x01, 0x40)]
    else:
        return list(map(lambda id_str: int(id_str, 0), str_list))

try:
    can = CanBus(bitrate = args.bitrate, channel = args.channel)
except:
    raise ValueError('Wrong can bus configurations.')

try:
    id_list = parse_id(args.id)
except:
    raise ValueError('Wrong id list.')

if args.command == 'list':
    list_devices(can, id_list)

if args.command == 'monitor':
    monitor(can, id_list)
