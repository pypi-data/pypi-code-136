import subprocess
import netifaces
import requests
import _hector
import socket
import uuid
import json
import os

__all__ = [
    "get_mac_address", "get_physical_address", "get_network_profiles", "get_profile_passwords",
    "get_default_gateway_data", "is_valid_ipv6", "get_ipconfig", "get_ipconfig_data", "Network",
    "get_recieve_rate", "get_transmit_rate", "is_connected"
]

def __contains_number(string):
    for c in string:
        if c.isdigit(): return True
    return False

def __get_network_data():
    return [{True: v.strip(), False: v.strip().lower()}[__contains_number(v)] for v in subprocess.check_output("netsh wlan show interfaces").decode("utf8").split(" ") if v != '' and v != " " and v != ":"]

netdata: list = __get_network_data()

def get_mac_address():
    return ':'.join(['{:02x}'.format((uuid.getnode() >> e) & 0xff) for e in range(0,8*6,8)][::-1])

def get_physical_address():
    if "physical" and "address" in netdata:
        l = netdata.index("physical")

        if netdata[l + 1] == "address": return netdata[l + 2]
    return "Couldn't find Physical Address."

def get_network_profiles():
    data, profiles = subprocess.check_output('netsh wlan show profiles').decode('utf-8', errors="backslashreplace").split('\n'), []
    for value in reversed(data):
        if "All User Profile" in value: profiles.append(value.split(":")[1][1:-1])
    return profiles

def get_profile_passwords(profile):
    data = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8', errors="backslashreplace").split('\n')
    return [b.split(":")[1][1:-1] for b in data if "Key Content" in b]

def get_default_gateway_data():
    gateways = netifaces.gateways()
    return [gateways["default"][netifaces.AF_INET][0], gateways["default"][netifaces.AF_INET][1]]

def is_valid_ipv6(address):
    address_list = address.split(':')
    return (
        len(address_list) == 8
        and all(len(current) <= 4 for current in address_list)
        and all(current in 'ABCDEFabcdef:0123456789' for current in address)
    )

def get_ipconfig():
    data = []
    for v in [v for v in subprocess.check_output("ipconfig").decode("utf-8").split(" ") if v != "" and v != "." and v !=":"]:
        if "\r" in v: v = v.replace("\r", "")
        if "\n" in v: v = v.split("\n")
        if v == "": continue
        
        if isinstance(v, list):
            for x in v:
                if x in ["", " "]: continue
                data.append(x)
            continue
        data.append(v)
    
    w = data[2][13:]
    data = data[3:]
    data.insert(0, w)

    return data

def indexEachOf(elements: list, _list: list):
    indexes = {e: [] for e in elements}
    for i, v in enumerate(_list):
        if v in elements: indexes[v].append(i)
    return indexes

def get_ipconfig_data(ignore_disconnected=False):
    ipconfig = get_ipconfig()
    indexes = indexEachOf(["Wireless", "Ethernet"], ipconfig)
    indexes = [*indexes["Wireless"], *indexes["Ethernet"]]
    indexes.sort()

    data = {}
    for i, index in enumerate(indexes):
        try: _data = ipconfig[index:indexes[i + 1]]
        except: _data = ipconfig[index:-1]

        if "Media" in _data:
            if ignore_disconnected: continue
            y = _data.index("Media")
            title = " ".join(_data[:y])[:-1]
            info = _data[y:]
        else:
            y = _data.index("Connection-specific")
            title = " ".join(_data[:y])[:-1]
            info = _data[y:]

        data[title] = info

    for key, v in data.items():
        if "disconnected" in v and not ignore_disconnected:
            data[key] = [f"{v[0]} {v[1]}", f"{v[2]} {v[3]}", *data[key][4:]]
            continue
        
        data[key] = data[key][3:]
        data[key] = {
            "IPv6 Address": data[key][3], 
            "IPv4 Address": data[key][6], 
            "Subnet Mask": data[key][9],
            "Default Gateway": data[key][12:]
        }
    
    return data

def get_recieve_rate():
    if "receive" and "rate" in netdata:
        l = netdata.index('receive')

        if netdata[l + 1] == "rate":
            return netdata[l + 2], netdata[l + 3]
    return "Couldn't get Receive Rate."

def get_transmit_rate():
    if "transmit" and "rate" in netdata:
        l = netdata.index('transmit')

        if netdata[l + 1] == "rate":
            return netdata[l + 2], netdata[l + 3]
    return "Couldn't get Transmit Rate."

def is_connected() -> bool:
    return {"connected": True, "disconnected": False}[netdata[netdata.index('state') + 1]]

class Network:
    NOT_CONNECTED = "Not Connected"

    def __init__(self):
        self.connected = is_connected()

        # Doesn't Require WiFi Connection
        self.phyiscal_address = get_physical_address()
        self.mac_address = get_mac_address()
        self.GUID = netdata[netdata.index("guid") + 1]
        self.profiles = get_network_profiles()
        self.passwords = {profile: get_profile_passwords(profile) for profile in self.profiles}
        self.ipconfig = get_ipconfig_data(ignore_disconnected=True)

        # Requires WiFi Connection
        self.default_gateway = {}
        self.public_ips = {}
        self.private_ip = self.NOT_CONNECTED
        self.suspected_vpn = False

        self.SSID = self.NOT_CONNECTED
        self.BSSID = self.NOT_CONNECTED
        self.recieve_rate = self.NOT_CONNECTED
        self.transmit_rate = self.NOT_CONNECTED

        if self.connected:
            gateway_data = get_default_gateway_data()
            self.default_gateway = {
                "ipv4": gateway_data[0],
                "ipv6": gateway_data[1][1:-1]
            }

            try:
                self.public_ips = {
                    "ifconfig.me": subprocess.check_output("curl -s ifconfig.me", shell=True).decode("utf-8"),
                    "ipify": requests.get('https://api.ipify.org').text,
                    "seeip": requests.get('https://ip.seeip.org/jsonip?').json()["ip"]
                }

                self.suspected_vpn = self.public_ips["ipify"] != self.public_ips["seeip"]
            except: pass

            self.private_ip = socket.gethostbyname(socket.gethostname())

            self.SSID = netdata[netdata.index("ssid") + 1]
            self.BSSID = netdata[netdata.index("bssid") + 1]
            self.recieve_rate = get_recieve_rate()
            self.transmit_rate = get_transmit_rate()
    
    def to_json(self, filename, dir="./", override=True, ignore_errors=False, pretty=False, hexify=False, hex_glue=None):
        path = os.path.join(dir, filename)

        if os.path.exists(path):
            if not override: 
                if not ignore_errors: raise FileExistsError((
                    f"Unable to convert network data to json file {filename}.",
                    "Either provide a new path that doesn't exist or enable override.",
                ))
                return f"Unable to create json file."
        
        with open(path, "wb") as json_file:
            json_dict = {
                "connected": self.connected,
                "physical address": self.phyiscal_address,
                "guid": self.GUID,
                "profiles": self.profiles,
                "passwords": self.passwords,

                "default gateway": self.default_gateway,
                "public ips": self.public_ips,
                "private ip": self.private_ip,
                "suspected vpn": self.suspected_vpn,
                
                "ssid": self.SSID,
                "bssid": self.BSSID,
                "recieve rate": self.recieve_rate,
                "transmite rate": self.transmit_rate,

                "ipconfig": self.ipconfig
            }

            if hexify:
                if hex_glue is None: raise ValueError("Hexify is set to True. A 'raw' or 'normal' string must be provided for the 'hex_glue' parameter.")
                json_file.write(_hector.dumps(_hector.to_hex(json_dict, hex_glue), pretty=pretty).encode()); return
                
            json_file.write(json.dumps(json_dict, index=4).encode() if pretty else json.dumps(json_dict).encode())