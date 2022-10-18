import sys
import time
import argparse
import colorama
from termcolor import colored
sys.path.append("..")
from robodyno_components_python.interfaces import CanBus
from robodyno_components_python.components import Motor

colorama.init(autoreset=True)

parser = argparse.ArgumentParser(description='Robodyno command line tools.')
parser.add_argument('command', 
                    choices=['enable', 'disable', 'info', 'control', 'config', 'reset'], 
                    help='Operate robodyno motor via command line.')
parser.add_argument('--id', type=str, nargs='*', default=['0x10'],
                    help='robodyno device id filter, dafault [0x10]')
parser.add_argument('-c', '--channel', type=str, default='can0',
                    help='can bus channel')
parser.add_argument('-b', '--bitrate', type=str, default='CAN_1M',
                    help='can bus bitrate')

parser.add_argument('-p', '--pos', type=float,
                    help='motor position setpoint(rad)')
parser.add_argument('-v', '--vel', type=float,
                    help='motor velocity setpoint(rad/s)')
parser.add_argument('-t', '--torque', type=float,
                    help='motor torque setpoint(Nm)')
parser.add_argument('--new-id', type=str,
                    help='change motor id with new id')
parser.add_argument('-s', '--save', action='store_true',
                    help='save motor configuration when set new id')

args = parser.parse_args()

try:
    can = CanBus(bitrate = args.bitrate, channel = args.channel)
except:
    raise ValueError('Wrong can bus configurations.')

def id_to_motor_list(str_list):
    """Parse id list to motor object list.
    
    Args:
        str_list: string id list
    
    Returns:
        robodyno motor object list
    """
    id_list = []
    motor_list = []
    if len(str_list) > 0 and ('all' in str_list):
        id_list = [id for id in range(0x01, 0x40)]
    else:
        id_list = list(map(lambda id_str: int(id_str, 0), str_list))
    for id in id_list:
        try:
            motor_list.append(Motor(can, id))
        except:
            pass
    return motor_list

try:
    motor_list = id_to_motor_list(args.id)
except:
    raise ValueError('Wrong id list.')

if len(motor_list) == 0:
    raise ValueError('No available motor on can bus.')

if args.command == 'enable':
    for motor in motor_list:
        motor.enable()

if args.command == 'disable':
    for motor in motor_list:
        motor.disable()

if args.command == 'info':
    for motor in motor_list:
        time.sleep(1)
        ver = motor.get_version(0.1)
        vbus = motor.get_voltage(0.1)
        temp = motor.get_temperature(0.1)
        pos, vel, torque = motor.get_feedback(0.1)
        state_str = 'mode: ' + colored(motor.mode.name, 'magenta')
        state_str += ', state: '
        if motor.error['error'].value:
            state_str += colored(motor.error['error'].name, 'red')
        else:
            state_str += colored(motor.state.name, 'blue')
        print(colored('[0x{:02X}]'.format(motor.id), 'cyan') + ' ' +
                colored(ver['type'].name, 'green') + ' ' +
                'ver: {}.{}'.format(ver['main_version'], ver['sub_version']))
        print(state_str)
        print('vbus: {:.2f}V, temp: {:.2f}°C'.format(vbus, temp))
        print('pos: {:.4f}, vel: {:.4f}, torque: {:.4f}'.format(pos, vel, torque))

if args.command == 'control':
    for motor in motor_list:
        if args.pos is not None:
            vel_ff = args.vel if args.vel is not None else 0
            torque_ff = args.torque if args.torque is not None else 0
            for motor in motor_list:
                motor.position_filter_mode(5)
                motor.enable()
                motor.set_pos(args.pos, vel_ff, torque_ff)
        elif args.vel is not None:
            torque_ff = args.torque if args.torque is not None else 0
            for motor in motor_list:
                motor.velocity_ramp_mode(5)
                motor.enable()
                motor.set_vel(args.vel, torque_ff)
        elif args.torque is not None:
            for motor in motor_list:
                motor.torque_mode(5)
                motor.enable()
                motor.set_torque(args.torque)

if args.command == 'config':
    if len(motor_list) != 1:
        raise ValueError('Can not set multiple motor ids at the same time.')
    motor = motor_list[0]
    try:
        new_id = int(args.new_id, 0)
        if new_id < 0x01 or new_id >= 0x40:
            raise ValueError()
    except:
        raise ValueError('Wrong motor new id, choose from [0x01,0x40).')
    motor.config_can_bus(new_id, bitrate = args.bitrate)
    time.sleep(0.5)
    motor = Motor(can, new_id)
    if args.save:
        motor.save_configuration()

if args.command == 'reset':
    if len(motor_list) != 1:
        raise ValueError('Can not reset multiple motor at the same time.')
    motor = motor_list[0]
    print('resetting...')
    motor.reset()
    time.sleep(3)
    motor = Motor(can, 0x10)
    print('calibrating...')
    motor.calibrate()
    time.sleep(1)
    while motor.state.value != 1:
        pass
    time.sleep(0.2)
    motor.save_configuration()
    time.sleep(0.5)
    print('finished.')
