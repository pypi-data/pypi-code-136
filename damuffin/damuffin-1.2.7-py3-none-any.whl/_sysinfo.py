from math import ceil
import subprocess
import _hector
import _net
import json
import wmi
import os

__all__ = ["sysinfo", "init", "find_system_info", "get_systeminfo", "System"]

sysinfo = None

def init():
    global sysinfo
    
    if sysinfo is not None:
        raise ValueError((
            'The System Info is already initialized.',
            'This means you already called the init() function more than once.'
        ))

    sysinfo = get_systeminfo()

def check_initialized():
    if sysinfo is None:
        raise ValueError((
            'The System Info has not been Initialized.', 
            'This means that you have not called the init() function yet.'
        ))

def __count_with_indexes(iterable, item):
    return [i for i, v in enumerate(iterable) if v == item]

def __index_list(_list: list, text: list):
    if not all([len(text) > 0, len(_list) > 1, *[t in _list for t in text]]): return "N/A"

    for index in __count_with_indexes(_list, text[0]):
        if all([_list[index + i] == c for i, c in enumerate(text)]):
            return index + (len(text) - 1)

    return "N/A"

def __deep_clean(raw_data):
    unfiltered = [v.strip() for v in raw_data.split("\r") if v not in ["", " ", "\r", "\n"]]

    def remove_end_colon(text):
        if _net.is_valid_ipv6(text): return text
        
        if text[-1] == ":": return text[:-1]
        return text

    filtered = []
    [[filtered.append(remove_end_colon(c.strip())) for c in v.split(" ") if c not in ["", " ", "\r", "\n"]] for v in unfiltered]
    
    return filtered

def get_systeminfo():
    raw_systeminfo = subprocess.check_output("systeminfo").decode('utf-8')
    return __deep_clean(raw_systeminfo)

def find_system_info(info_key: list[str], until=""):
    check_initialized()
    index = __index_list(sysinfo, info_key)
    if index == "N/A": return "N/A"

    try:
        if until != "":
            i = index + 1
            value, text = sysinfo[i], []
            while until != value:
                if i > index + 200: # Max recursion
                    return "N/A"
                text.append(value)
                i += 1
                value = sysinfo[i]
            return " ".join(text).strip()
        return sysinfo[index + 1].strip()
    except: return "N/A"

class System:
    def __init__(self):
        check_initialized()

        computer = wmi.WMI()

        self.username = os.environ["USERNAME"]
        self.hostname = find_system_info(["Host", "Name"])
        
        self.os_name = find_system_info(["OS", "Name"], "OS")
        self.os_version = find_system_info(["OS", "Version"], "OS")
        self.os_manufacturer = find_system_info(["OS", "Manufacturer"], "OS")
        self.os_configuration = find_system_info(["OS", "Configuration"], "OS")
        self.os_build_type = find_system_info(["OS", "Build", "Type"], "Registered")
        
        self.registered_owner = find_system_info(["Registered", "Owner"])
        self.product_id = find_system_info(["Product", "ID"])
        self.orginal_install_date = find_system_info(["Original", "Install", "Date"], "System")
        
        self.system_boot_time = find_system_info(["System", "Boot", "Time"], "System")
        self.system_manufacturer = find_system_info(["System", "Manufacturer"])
        self.system_model = find_system_info(["System", "Model"])
        self.system_type = find_system_info(["System", "Type"], "Processor(s)")

        self.bios_version = find_system_info(["BIOS", "Version"])
        self.windows_directory = find_system_info(["Windows", "Directory"])
        self.system_directory = find_system_info(["System", "Directory"])
        self.boot_device = find_system_info(["Boot", "Device"])
        
        self.system_locale = find_system_info(["System", "Locale"], "Input")
        self.input_locale = find_system_info(["Input", "Locale"], "Time")
        self.time_zone = find_system_info(["Time", "Zone"], "Total")
        
        self.total_phyiscal_memory = find_system_info(["Total", "Physical", "Memory"], "Available")
        self.available_physical_memory = find_system_info(["Available", "Physical", "Memory"], "Virtual")
        self.virtual_memory_max_size = find_system_info(["Virtual", "Memory", "Max", "Size"], "Virtual")
        self.virtual_memory_available = find_system_info(["Virtual", "Memory", "Available"], "Virtual")
        self.virtual_memory_in_use = find_system_info(["Virtual", "Memory", "In", "Use"], "Page")

        self.page_file_location = find_system_info(["Page", "File", "Location(s)"])
        self.domain = find_system_info(["Domain"])
        self.logon_server = find_system_info(["Logon", "Server"])

        self.CPU = [cpu.Name.strip() for cpu in computer.Win32_Processor()]
        self.GPU = [card.Name.strip() for card in computer.Win32_VideoController()]
        self.RAM = ceil(int(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1e+6)
    
    def to_json(self, filename, dir, override=True, ignore_errors=True, pretty=False, hexify=False, hex_glue=None):
        path = os.path.join(dir, filename)

        if os.path.exists(path):
            if not override:
                if not ignore_errors: raise FileExistsError((
                    f"Unable to convert systeminfo data to json file {filename}.",
                    "Either provide a new path that doesn't exist or enable override.",
                ))
                return "Unable to create json file."
            
        with open(path, "wb") as json_file:
            json_dict = {
                "User": self.username,
                "Host Name": self.hostname,
                "CPU": self.CPU,
                "GPU": self.GPU,
                "RAM": self.RAM,
                "OS": {
                    "Name": self.os_name,
                    "Version": self.os_version,
                    "Manufacturer": self.os_manufacturer,
                    "Configuration": self.os_configuration,
                    "Build Type": self.os_build_type
                },
                "Owner": self.registered_owner,
                "Product ID": self.product_id,
                "Install Date": self.orginal_install_date,
                "system": {
                    "Boot Time": self.system_boot_time,
                    "Manufacturer": self.system_manufacturer,
                    "Model": self.system_model,
                    "Type": self.system_type
                },
                "BIOS Version": self.bios_version,
                "Boot Device": self.boot_device,
                "Directories": {
                    "Windows": self.windows_directory,
                    "System": self.system_directory,
                    "Page File": self.page_file_location
                },
                "Time": {
                    "System Locale": self.system_locale,
                    "Input Locale": self.input_locale,
                    "Zone": self.time_zone
                },
                "Memory": {
                    "Total Physical": self.total_phyiscal_memory,
                    "Available Physical": self.available_physical_memory,
                    "Virtual": {
                        "Max Size": self.virtual_memory_max_size,
                        "Available": self.virtual_memory_available,
                        "In Use": self.virtual_memory_in_use
                    }
                },
                "Domain": self.domain,
                "Logon Server": self.logon_server
            }

            if hexify:
                if hex_glue is None: raise ValueError("Hexify is set to True. A 'raw' or 'normal' string must be provided for the 'hex_glue' parameter.")
                json_file.write(_hector.dumps(_hector.to_hex(json_dict, hex_glue), pretty=pretty).encode()); return
            
            json_file.write(json.dumps(json_dict, index=4).encode() if pretty else json.dumps(json_dict).encode())