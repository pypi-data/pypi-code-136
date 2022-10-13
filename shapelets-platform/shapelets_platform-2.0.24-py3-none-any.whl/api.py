from typing import Optional, overload, TypeVar, Union, Type
from typing_extensions import Literal

import multiprocessing
import os
import time
import requests 
import rodi 
import sys

from .dsl import DataApp
from .svr.model.users import UserAttributes

from . import svr 
from .svr.authn import crypto

EnterpriseLoginType = Literal['azure', 'linkedin', 'google', 'github']

T = TypeVar("T", covariant=True)

def _is_server_up(session: requests.Session, retries: int = 10, wait_seconds: float = 0.1) -> bool:
    """
    Tries to connect with Shapelets Server
    """
    serverUp = False 
    c = 0
    while not serverUp and c < retries:
        try:
            pong_response = session.get("api/ping")
            pong_response.raise_for_status()
            serverUp = pong_response.text == "pong"
        except:
            c += 1  
            time.sleep(wait_seconds)    
            
    return serverUp

def _run_out_of_process():
    """
    Runs an out of process server
    """
    if os.fork() != 0:
        return 
    settings = svr.Settings()
    svr.setup_http_server(settings, True)


class SharedState:
    __slots__ = ('__services', '__local_server', '__authorization')
    
    def __init__(self) -> None:
        self.__services = None 
        self.__local_server = None 
        self.__authorization = None 

    @property 
    def authorization(self) -> str:
        return self.__authorization
    
    @authorization.setter
    def authorization(self, value: str):
        self.__authorization = value 

    @property
    def services(self) -> rodi.Services:
        return self.__services
    
    @services.setter
    def services(self, value: rodi.Services):
        self.__services = value 
    
    @property
    def local_server(self) -> Optional[svr.InProcServer]:
        return self.__local_server
    
    @local_server.setter
    def local_server(self, value: svr.InProcServer):
        self.__local_server = value
        

this = sys.modules[__name__]
this._state: SharedState = SharedState() 
    
def initialize(server_mode: Optional[svr.ServerModeType] = None):
    # resolve settings from files and environment.
    settings = svr.Settings()
    server_mode = server_mode or settings.client.server_mode
    if server_mode == 'out-of-process':
        # now, build a stack of proxies to remote services
        this._state.services = svr.setup_remote_client(settings)
    elif server_mode == 'standalone':
        # run the server in standalone mode, set blocking param to True
        this._state.local_server = svr.setup_http_server(settings, True)
    elif server_mode == 'in-process':
        # make sure the client will point to the in-proc server
        settings.client = settings.client.copy(update={
            'host': settings.server.host,
            'port': settings.server.port
        })
        # run the server in the same process
        this._state.local_server = svr.setup_http_server(settings, False)
        # build the proxies
        this._state.services = svr.setup_remote_client(settings)
    else:
        # run in headless mode
        this._state.services = svr.setup_headless(settings)

    if server_mode != 'headless':
        # Ping the server to ensure it is running
        session = this._state.services.get(requests.Session)

        # check the server is running and reachable
        server_up = _is_server_up(session, 10 if server_mode == 'in-process' else 1)

        if not server_up and server_mode == 'out-of-process':
            # launch new process
            # TODO: Review this as I am not convinced this is the right way
            #       as it uses fork at the function level.  However, spawns
            #       break virtual environment, so... this may not be as 
            #       easy as it looks like.
            process = multiprocessing.Process(target = _run_out_of_process, name='ShapeletsServer')
            process.start()
            server_up = _is_server_up(session)

        if not server_up:
            raise RuntimeError(f"No timely response from {settings.client.server_url}")


def _get_service(desired_type: Union[Type[T], str]) -> T:
    if this._state.services is None:
        initialize()
        
    return this._state.services.get(desired_type)

def _get_service_optional(desired_type: Union[Type[T], str]) -> Optional[T]:
    try:
        return _get_service(desired_type)
    except:
        return None 

def forget_me():
    """
    Forgets credentials stored in configuration files 
    """
    svr.defaults(signed_token = None)

def login(*, 
          authn_provider: Optional[EnterpriseLoginType] = None, 
          user_name: Optional[str] = None, 
          password: Optional[str] = None, 
          remember_me: bool = True):
    
    """
    Login to Shapelets.
    
    This function is quite versatile and provides multiple methods of authentication. 
    
    When `authn_provider` is set, it will take preference over user name / password 
    combinations, even when found in the environment variables.  When login through 
    an external authentication provider for the very first time, a user will be 
    automatically created using the information shared by the authentication
    provider.
    
    If `authn_provider` is left unset, the code will try to log in using an user name 
    and password combination.  This information can be set directly as parameters, 
    through environment variables or by configuration files.  The recommended 
    method is to use environment variables to avoid exposing plain passwords.  Bear 
    in mind the credentials should have been created beforehand.
    
    If no external authentication or no user name / password combination is found, 
    the system will try to login the user using a previous login. 
    
    Parameters
    ----------
    authn_provider: optional, one of `azure`, `linkedin`, `google`, `github`
        Determines which external authentication provider should be used.
    
    user_name: optional, string 
        User name.  The preferred method for setting this value is through 
        the environment variable `SHAPELETS_CLIENT__USERNAME`
        
    password: optional, string 
        Password associated with `user_name`.  The preferred method for 
        setting this value is through the environment variable 
        `SHAPELETS_CLIENT__PASSWORD`
        
    remember_me: optional, bool, defaults to True
        Upon a successful login, stores the credentials in the default 
        user configuration file.  
    
    """
    
    settings = _get_service(svr.Settings)
    auth_svc = _get_service(svr.IAuthService)
    session: svr.PrefixedSession = _get_service_optional(requests.Session)
    
    signed_token: Optional[str] = None 
    
    if authn_provider is not None:
        if not auth_svc.available(authn_provider):
            raise RuntimeError(f"Authentication flow for {authn_provider} is not available at the moment.")
        id = settings.telemetry.id.hex
        addresses = auth_svc.compute_addresses(authn_provider, id)
        gc_principal_id, user_details = svr.gc_flow(addresses)
        signed_principal = auth_svc.auth_token(gc_principal_id, user_details)
        signed_token = signed_principal.to_token()
    
    else:
        user_name: str = user_name if user_name is not None else settings.client.username
        password: str = password if password is not None else settings.client.password
        
        if user_name is not None and password is not None:
            challenge = auth_svc.generate_challenge(user_name)
            token = crypto.sign_challenge(challenge.salt, challenge.nonce, password.encode('ascii'))
            signed_principal = auth_svc.verify_challenge(user_name, challenge.nonce, token)
            signed_token = signed_principal.to_token()
        else: 
            signed_token = settings.client.signed_token 
            if signed_token is not None:
                if not auth_svc.verify(signed_token):
                    svr.defaults(signed_token = None) # Remove it from file
                    raise RuntimeError("Invalid cached credentials.  Please login again.")
                
                
    if signed_token is None:
        raise RuntimeError("No login credentials.")
    
    this._state.authorization = signed_token
    
    if remember_me:
        svr.defaults(signed_token = signed_token)
    
    if session is not None:
        session.set_authorization(signed_token)


def register(user_name: str, password: str, user_details: Optional[UserAttributes] = None, also_login: bool = True, remember_me: bool = True, force:bool = False):
    """
    Registers a new user in Shapelets
    
    Parameters
    ----------
    user_name: str, required
        New user name.  This name should be unique in the system
    
    password: str, required
        Password associated with the new user 

    user_details: UserAttributes, optional
        User profile
                
    also_login: bool, defaults to True 
        Executes a login right after the registration
    
    remember_me: bool, defaults to True 
        Only used if `also_login` is set
    
    force: bool, defaults to False 
        Set this flag to overwrite the user attributes if the user already exists
    """
    auth_svc = _get_service(svr.IAuthService)
    if auth_svc.user_name_exists(user_name):
        if force:
            result = auth_svc.remove_user(user_name)
            if not result:
                raise ValueError("Unable to remove user name")
        else:
            raise ValueError("User name already exists. To force registration with new UserAttributes, set flag force to True.")
    
    salt = crypto.generate_salt()
    pk = crypto.derive_verify_key(salt, password.encode('ascii'))
    if not auth_svc.register(user_name, salt, pk, user_details):
        raise RuntimeError("Unable to register a new user")
    
    if also_login:
        login(user_name=user_name, password=password, remember_me=remember_me)

def defaults(**kwargs) -> None:
    """
    (Un)Sets default values
    
    When parameters are unset, values will be left unchanged; when parameters are 
    set to None, they will be reverted to their default values;  otherwise, the 
    new default values will be set and store at current user's home directory, 
    under the file `~/.shapelets/settings.toml`
    
    Parameters
    ----------
    **kwargs:  Valid keyword arguments are:
    
        - **username**: optional, string
          Default user name 
        
        - **password**: optional, string 
          Password associated with user name.  
        
        - **host**: optional, either a string, bytes, int, IPv4Address or IPv6Address
          Address of the server to connect to.
        
        - **port**: optional, positive int
          Port number on the host where the server can be located.
            
        - **enable_telemetry**: optional, boolean, defaults to None
          Enables or disables the anonymous telemetry metrics.
          
        - **server_mode**: optional, one of `headless`, `in-process`, `out-of-process`, defaults to None 
          Should the server component be hosted within this process or, alternatively, it is to be 
          hosted by an external (usually demonized) process.    
    
    Notes
    -----
    Use this method before starting using Shapelets to ensure new settings 
    will be correctly loaded.  
    
    Whilst it is possible to save user name and password on the configuration file 
    the most convenient way to set up this information is through environment 
    variables.  All variables starting with `SHAPELETS_` will be interpreted as 
    settings;  to set up a default username use `SHAPELETS_CLIENT__USERNAME` and, 
    similarly, password can be set through the environment variable 
    `SHAPELETS_CLIENT__PASSWORD`.  Please note that environment variables are 
    treated in a case insensitive way.
    """
    svr.defaults(**kwargs)


def register_dataapp(dataapp: DataApp):
    dataapp_svc = _get_service(svr.IDataAppsService)
    dataapp_svc.create(dataapp)
