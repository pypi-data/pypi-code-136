"""
Update Rollout Manager API [URM-API]

A Decentralized Package Manager.
Made by NoKodaAddictions, NoKoda
"""

from json import load, dump, JSONDecodeError
from operator import le
from os import scandir, mkdir, system, remove
from os.path import dirname, exists, join
from uuid import uuid4, UUID
from requests import get, Response, RequestException
from termcolor import colored

__version__ = "1.0"
__accepted_versions__ = [
    "1.0"
]
__directory__ = dirname(__file__)

class Exceptions:
    """
    Exceptions class
    """
    class UnsupportedPackageError(Exception):
        """
        Raised if 
        - The package config versions do not match the URM-API Version
        """
    
    class PackageConfigError(Exception):
        """
        Raised if
        - The package could not be read correctly
        - The package config is missing essential data
        """

    class UninstalledPackageError(PackageConfigError):
        """
        Raised if
        - The package is not installed
        """

class API:
    """
    Main class for fetching and downloading packages.
    """
    server:str = None
    config:str = None
    response:Response = None
    
    package_data:dict = None
    package_name:str = None
    package_version:str = None
    package_server:str = None
    
    package_data_old:str = None
    package_name_old:str = None
    package_version_old:str = None
    package_server_old:str = None


    def __init__(self, server:str=None, config:str=None):
        self.server = server
        self.config = config
        
        if self.server is None:
            if self.config is None:
                raise TypeError("Please specify a link or config.urmapi.json file.")
                
            else:
                with open(config, 'r', encoding="utf8") as r:
                    self.package_data_old = load(r)
                    self.package_name_old = self.package_data_old["HEAD"]["package"]["name"]
                    self.package_version_old = self.package_data_old["HEAD"]["package"]["version"]
                    self.package_server_old = self.package_data_old["HEAD"]["package"]["package_url"]
                    
                    self.response = get(f"{self.package_server_old}/config.urmapi.json", timeout=10)
                
        else:
            self.response = get(f"{self.server}/config.urmapi.json", timeout=10)
                
        
        if self.response.status_code != 200:
            raise RequestException(f"Error: {self.response.status_code}")

        else:
            self.package_data = self.response.json()
            self.package_name = self.package_data["HEAD"]["package"]["name"]
            self.package_version = self.package_data["HEAD"]["package"]["version"]
            self.package_server = self.package_data["HEAD"]["package"]["package_url"]

    def install(self, location:str=None) -> None:
        """
        Installs the files from the server

        :param: location: string

        :return: None
        """

        ledger = Ledger()

        package_id, package_data = ledger.search_name(self.package_name)

        if package_id is not None:
            print(f"{self.package_name}: Package is already installed.")
        
        else:
            print(f"{self.package_name}: Comparing versions...")
            if self.package_data["HEAD"]["config"]["version"] in __accepted_versions__:
                print(colored(f"{self.package_name}: Package versions match", "green"))
                
                print(f"{self.package_name}: Creating package folder...")
                if location is not None:
                    try:
                        mkdir(join(location, self.package_name))
                        
                    except FileExistsError:
                        pass
                    
                else:
                    raise TypeError("Package install location is required.")

                print(f"{self.package_name}: Downloading package...")
                self.package_data["CONTENT"]["files"].append("config.urmapi.json")
                
                for file in self.package_data["CONTENT"]["files"]:
                    print(f"{file}: Fetching...")
                    
                    frs = get(f"{self.server}/{file}", timeout=10)
                    
                    if frs.status_code == 200:
                        print(colored(f"{file}: Downloading...", "green"))
                        
                        path = dirname(file)
                        
                        if path != "":
                            try:
                                mkdir(join(location, f"{self.package_name}/{path}"))
                            except FileExistsError:
                                pass

                        with open(join(location, f"{self.package_name}/{file}"), "wb") as w:
                            w.write(frs.content)

                    else:
                        print(colored(f"{file}: Could not fetch", "red"))
                
                print("Updating Ledger...")
                ledger = Ledger()
                
                ledger.add(name=self.package_name, location=join(location, self.package_name), version=__version__)
                
                print(colored(f"{self.package_name}: Installed"))
            
            else:
                raise Exceptions.UnsupportedPackageError(f"{self.package_name}: Package versions do not match. This version of URM-API supports {__accepted_versions__}")
            

    def update(self) -> None:
        """
        Compares versions, makes neccessary changes.

        :return: None
        """
        
        if self.package_data_old is not None:
            ledger = Ledger()
            package_id, package_info = ledger.search_name(self.package_name_old)

            if package_id is not None:
                print(colored(f"{self.package_name_old}: Package is verified to be installed", "green"))
                location = package_info["location"]

                if self.package_version_old != self.package_version:
                    print(colored(f"{self.package_name_old}: Update is available"), "green")

                    print(f"{self.package_name}: Comparing versions...")
                    if self.package_data["HEAD"]["config"]["version"] in __accepted_versions__:
                        print(colored(f"{self.package_name_old}: Package versions match", "green"))


                        print(f"{self.package_name_old}: Reading steps...")
                        print(f"{self.package_name_old}: Installing/Updating files...")
                        for file in self.package_data["CONTENT"]["steps"]["install"]:
                            print(f"{file}: Fetching...")

                            frs = get(f"{self.package_server}/{file}", timeout=10)

                            if frs.status_code == 200:
                                print(colored(f"{file}: Downloading...", "green"))

                                path = dirname(file)

                                if path != "":
                                    try:
                                        mkdir(join(location, path))
                                    except FileExistsError:
                                        print("FileExistsError")

                                    with open(join(location, file), "wb") as w:
                                        w.write(frs.content)

                            else:
                                print(colored(f"{file}: Could not fetch", "red"))


                        print(f"{self.package_name_old}: Removing files...")
                        for file in self.package_data["CONTENT"]["steps"]["delete"]:
                            print(f"{file}: Deleting...")
                            try:
                                remove(join(location, f"{file}"))
                                print(colored(f"{file}: Deleted", "green"))
                                
                            except FileNotFoundError:
                                print(colored(f"{file}: Could not delete"))

                        
                        print(f"{self.package_name}: Updating config.urmapi.json...")
                        with open(join(location, "config.urmapi.json"), "w", encoding="utf8") as w:
                            dump(self.package_data, w, indent=4)

                        print(f"{self.package_name}: Updating ledger...")
                        ledger.replace(package_id, self.package_name, location, __version__)

                        print(f"{self.package_name}: Finished")

                    else:
                        raise Exceptions.UnsupportedPackageError(f"{self.package_name_old}: Package versions do not match. This version of URM-API supports {__accepted_versions__}")

                    
                else:
                    print(f"{self.package_name_old}: Is up to date.")

            else:
                raise Exceptions.UninstalledPackageError("Package is not installed. Installed this package first before updating")        
        else:
            raise TypeError("Update function requires a config.urmapi.json file.")

class Ledger:
    """
    Manages the ledger JSON file.
    """
    
    ledger:dict = None
    location:str = None
    
    def __init__(self):
        self.location = join(__directory__, "ledger.json")
        try:
            with open(self.location, 'r', encoding="utf8") as r:
                self.ledger = load(r)
        
        except FileNotFoundError:
            self.ledger = {}
            self.implement()

        except JSONDecodeError:
            self.ledger = {}
            self.implement()

    def search_id(self, uuid:str=None) -> str:
        """
        Returns the package information for the given UUID

        :param: uuid: string
        
        if found
        :return: string, dict

        if not found
        :return: None, None
        """

        if uuid is not None:
            for package in self.ledger:
                if package == uuid:
                    return package, self.ledger[package]

            return None, None

        else:
            raise TypeError("UUID not specified.")

    def search_name(self, name:str=None) -> dict:
        """
        Returns the package information for the given name

        :param: name: string
        
        if found
        :return: string, dict

        if not found
        :return: None, None
        """
        if name is not None:
            for package in self.ledger:
                if self.ledger[package]["name"] == name:
                    return package, self.ledger[package]

            return None, None

        else:
            raise TypeError("Name not specified.")
            
    def add(self, name:str=None, location:str=None, version:str=None) -> None:
        """
        Adds package information to ledger JSON file

        :param: name: string
        :param: location: string
        :param: version: string

        :return: None
        """
        if name is None or location is None or version is None:
            raise TypeError("Some parameters are None.")
        
        else:
            generated = False

            while not generated:
                uuid = str(uuid4())

                if uuid in self.ledger:
                    pass
                else:
                    generated = True
                    
            self.ledger.update({
                uuid:{
                    "name":name,
                    "location":location,
                    "version":version #URMAPI version this was installed in, not the package version
                }
            })
        
        self.implement()

    def remove(self, uuid:str=None) -> None:
        """
        Removes package information from ledger JSON file

        :param: uuid: string

        :return: None
        """
        self.ledger.pop(uuid)
        self.implement()

    def replace(self, uuid:str=None, name:str=None, location:str=None, version:str=None) -> None:
        """
        Replaces package information in ledger JSON file

        :param: uuid: string
        :param: name: string
        :param: location: string
        :param: version: string

        :return: None
        """
        if uuid is None or name is None or location is None or version is None:
            raise TypeError("Some parameters are None.")

        else:
            self.ledger.update({
                uuid:{
                    "name":name,
                    "location":location,
                    "version":version #URMAPI version this was installed in, not the package version
                }
            })
        
            self.implement()

    def scan(self) -> None:
        """
        Verifies that all packages in the ledger are installed

        :return: None
        """
        for package in self.ledger:
            print(f"{package['name']} Scanning...")
            
            if exists(package["location"]) and exists(join(package["location"], "config.urmapi.json")):
                print(colored(f"{package['name']}: Exists", "green"))

            else:
                print(colored(f"{package['name']}: Could not be found. Removing...", "red"))
                self.remove(package)

        print("Scan completed. Implementing changes...")
        self.implement()

    def implement(self) -> None:
        """
        Updates the ledger JSON file

        :return: None
        """
        with open(join(__directory__, "ledger.json"), 'w', encoding="utf8") as w:
            dump(self.ledger, w, indent=4)