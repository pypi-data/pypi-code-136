import requests
import zeroconf
import time
import socket
from .command_base import CliCommand
from tabulate import tabulate


def _find_devices_zeroconf(timeout):
    devices = {}

    class Listener(zeroconf.ServiceListener):
        def add_service(self, zc_inst, service_type, name):
            if name.startswith('Auterion Skynode API'):
                info = zc.get_service_info(service_type, name)
                if b'serial' in info.properties and b'version' in info.properties:
                    serial = info.properties[b'serial'].decode()
                    version = info.properties[b'version'].decode()
                    addresses = {socket.inet_ntoa(a) for a in info.addresses}

                    if serial in devices:
                        devices[serial]['addresses'].update(addresses)
                    else:
                        devices[serial] = {
                            'version': version,
                            'addresses': addresses
                        }

        def remove_service(self, zc_inst, service_type, name):
            pass

        def update_service(self, zc_inst, service_type, name):
            pass

    zc = zeroconf.Zeroconf()
    listener = Listener()
    browser = zeroconf.ServiceBrowser(zc, '_https._tcp.local.', listener)
    time.sleep(timeout)
    zc.close()
    return devices


def _find_devices_address(addresses):
    devices = {}
    for address in addresses:
        url = f"http://{address}/api/sysinfo/v1.0/device"
        try:
            response = requests.get(url, timeout=0.5)
            if response:
                data = response.json()
                if 'uuid' in data:
                    serial = data['uuid']
                    if serial in devices:
                        devices[serial]['addresses'].add(address)
                    else:
                        devices[serial] = {
                            'version': data['release'] if 'release' in data else None,
                            'addresses': {address}
                        }

        except:
            pass
    return devices


class DevicesCommand(CliCommand):
    @staticmethod
    def help():
        return 'Search for reachable Auterion devices'

    def __init__(self, config):
        pass

    def setup_parser(self, parser):
        parser.add_argument('-t', '--timeout', default=1, type=float, help='Zeroconf timeout to wait for answers')

    def _print_devices(self, title, devices):
        print('')
        print(f'{title}:')
        devices_list = [{'serial': serial, **rest} for serial, rest in devices.items()]
        print(tabulate(devices_list, headers='keys'))

    def run(self, args):
        devices_well_known = _find_devices_address(['10.41.1.1', '10.41.2.1'])
        devices_zeroconf = _find_devices_zeroconf(args.timeout)
        self._print_devices('Well known addresses', devices_well_known)
        self._print_devices('Zeroconf avahi', devices_zeroconf)



