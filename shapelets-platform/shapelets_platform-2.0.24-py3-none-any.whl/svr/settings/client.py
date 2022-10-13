from ipaddress import IPv4Address, IPv6Address
import tomlkit

from typing import Optional
from typing_extensions import Literal


from pydantic import BaseModel, IPvAnyAddress, PositiveInt, SecretStr

from ..model import SignedPrincipalId

ServerModeType = Literal['headless', 'in-process', 'out-of-process','standalone']

class ClientSettings(BaseModel):
    """
    Client settings
    """
    
    username: Optional[str] = None 
    """
    Name of the default user
    
    The environment variable `SHAPELETS_CLIENT__USERNAME` may be a good 
    alternative to this setting.    
    """
    
    password: Optional[SecretStr] = None 
    """
    Password of associated with the default user
    
    The environment variable `SHAPELETS_CLIENT__PASSWORD` may be a good 
    alternative to this setting.
    """
    
    signed_token: Optional[str] = None 
    """
    Cached identity that can be persisted to disk.
    """
    
    protocol: Optional[str] = 'https'
    """
    Protocol to connect with the server
    """
    
    host: Optional[IPvAnyAddress] = '127.0.0.1'
    """
    Bind socket to this host. Use `0.0.0.0` to make the application available 
    on your local network. IPv6 addresses are supported, `::`.
    """
    
    port: Optional[PositiveInt] = 4567
    """
    Bind to a socket with this port. 
    """
    
    server_mode: Optional[ServerModeType] = 'out-of-process'
    """
    Determines how the server component of Shapelets is managed, from the 
    perspective of this client.
    
    When set to `out-of-process`, which is the default setting, the 
    server component of Shapelets will be expected to be found at 
    the address determined by `host` and `port`.  
    
    `in-process` and `headless` are two special modes to interact 
    and host the server component; when set to `in-process`, a server 
    component will be launched within this process and, thus, its 
    lifetime will be coupled with this process.  When `in-process` 
    mode is active, host will be set to '127.0.0.1'
    
    In `headless` mode, the lifetime of the server will also be 
    tight to the lifetime of this process, but not HTTP interface 
    will be created; therefore, HTML UI won't be hosted.
    
    In `standalone` mode, only HTTP server is launched. This is really useful 
    for testing environments with remote clients. 
    
    `in-process` and `headless` mode are useful modes when running 
    either on testing environments or when running on isolated 
    environments like computational nodes and isolated worker processes.
    """
    
    @property
    def server_url(self) -> str:
        """
        Utility function that returns the url of the server
        """
        return f'{self.protocol}://{self.host}:{self.port}'
    
def client_defaults(data: tomlkit.TOMLDocument, **kwargs):
    """
    Creates or updates a configuration file with default client connectivity settings
    
    To revert values to their configuration, set the parameter to None; if the value 
    is not included in the call, no changes will be done to such parameter.  If the 
    parameter has a value, it will override existing values and stored them in the desired 
    file.
    
    Parameters
    ----------
    data: required, TOML document
        Where settings are to be stored
    
    username: optional, string
        Default user name 
    
    password: optional, string 
        Password associated with user name.  Please understand this password is 
        stored in plain text on a file.  There are other methods for setting this 
        password, as in an environment variable `shapelets_client__password`
    
    protocol: optional, string
        Protocol to connect with the server
    
    host: optional, either a string, bytes, int, IPv4Address or IPv6Address
        Address of the server to connect to.
    
    port: optional, positive int
        Port number on the host where the server can be located.
    
    server_mode: optional, ServerModeType
        Should the server component be hosted within this process or, alternatively, it is to be 
        hosted by an external (usually demonized) process.        

    """
    
    # go to the section.
    if 'client' not in data: 
        section = tomlkit.table()
        data['client'] = section
    else:
        section = data['client']
    
    if 'server_mode' in kwargs:
        if kwargs['server_mode'] is None:
            if 'server_mode' in section:
                del section['server_mode']
        else:
            section['server_mode'] = kwargs['server_mode']
            
    if 'signed_token' in kwargs:
        if kwargs['signed_token'] is None:
            if 'signed_token' in section:
                del section['signed_token']
        else:
            section['signed_token'] = kwargs['signed_token']            
    
    if 'port' in kwargs:
        if kwargs['port'] is None:
            if 'port' in section:
                del section['port']
        else:
            section['port'] = int(kwargs['port'])
            
    if 'protocol' in kwargs:
        if kwargs['protocol'] is None:
            if 'protocol' in section:
                del section['protocol']
        else:
            section['protocol'] = str(kwargs['protocol'])            

    if 'host' in kwargs:
        if kwargs['host'] is None: 
            if 'host' in section:
                del section['host']
        else:
            userValue = kwargs['host']
            address = IPvAnyAddress.validate(userValue) if isinstance(userValue, (str, bytes, int)) else userValue
            if not isinstance(address, (IPv4Address, IPv6Address)):
                raise ValueError("Invalid host.")
            section['host'] = str(address)

    if 'username' in kwargs:
        if kwargs['username'] is None: 
            if 'username' in section:
                del section['username']
        else:
            section['username'] = str(kwargs['username'])
            
    if 'password' in kwargs:
        if kwargs['password'] is None:
            if 'password' in section: 
                del section['password']
        else:
            section['password'] = str(kwargs['password'])
    

