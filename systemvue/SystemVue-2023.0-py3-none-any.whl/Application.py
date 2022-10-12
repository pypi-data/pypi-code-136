import os
import sys
import psutil
import inspect
from .Workspace import Workspace

class Application:
    """
    A class for Application
    ...

    Attributes
    ----------
    current_workspace : str
        workspace object of active workspace
    systemvue_path : str
        path to SystemVue bin directory
    is_internal : bool
        boolean of if application is using SystemVue internal or external

    Methods
    -------
    open_workspace(path : str) -> Workspace
        opens workspace with path and returns workspace object
    create_workspace() -> Workspace
        creates workspace and returns it
    show(value)
        shows value in output window in SystemVue
    """

    # static variables managing initialization
    # __is_initialized = False
    __is_internal = False
    _SystemVue_path = ""
    __externalModuleName = "SystemVue_External.pyd"

    def __init__(self) -> None:
        if sys.version_info[0] != 3 or sys.version_info[1] != 10:
            raise Exception("Need Python 3.10")
        # if not Application.__is_initialized:
        process = psutil.Process(os.getpid())
        if "SystemVue" in process.name() or "Genesys" in process.name():
            Application.__is_internal = True
            import SystemVue_Internal as systemvueapi
            # Application.__is_initialized = True
        
        else:
            # we need a SystemVue to work with. Try the following in order:
            # check if the user has called set_SystemVue_path
            # check if we're in a SystemVue install area by checking if the pyd module is nearby
            # check for a SV install in the registry 
            # fail

             # check static var from set_SystemVue_path
            if Application._SystemVue_path != "":
                if not os.path.exists( os.path.join(Application._SystemVue_path, Application.__externalModuleName )):
                    raise RuntimeError(f"SystemVue path has been set to {Application._SystemVue_path}, but module was not found at this location.")

            else:
                sourceFileDir = os.path.dirname(inspect.getsourcefile(lambda:0))
                systemVueInstallBin = os.path.abspath(os.path.join(sourceFileDir, "../../bin"))
        
                if os.path.exists( os.path.join(systemVueInstallBin, Application.__externalModuleName )):
                    Application._SystemVue_path = systemVueInstallBin

                else:
                    # try the registry
                    import winreg
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Keysight\\SystemVue2023\\System", access=winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
                    path = winreg.QueryValueEx(key, "DefaultPath")
                    if os.path.exists(path[0]):
                        Application._SystemVue_path = path[0] + "Bin"
                    else:
                        # raise exception - can't figure it out
                        raise RuntimeError('Cannot find SystemVue_External.pyd. Make sure the path to the SystemVue bin folder is added to sys.path.') 
                
                
            print(f"\nUsing SystemVue path: {Application._SystemVue_path}")

            sys.path.insert(0, Application._SystemVue_path)
        
            # do a try catch here and explain in the exception *all* the places we looked for the module
            try:
                import SystemVue_External as systemvueapi
                # Application.__is_initialized = True
            except Exception as e:
                print(e)
                exit

        self.app = systemvueapi.Application()
    
    def open_workspace(self, path: str) -> Workspace:
        """
        Opens workspace with path and returns workspace object

        Parameters
        -----------
        path : str
            path to workspace to open
        """
        return Workspace(self.app.open_workspace(path))

    def create_workspace(self) -> Workspace:
        """
        Creates a workspace and returns it
        """
        return Workspace(self.app.create_workspace())
    
    def show(self, value):
        """
        Shows value in output window in SystemVue

        Parameters
        -----------
        value
            value to be shown in output window
        """
        return self.app.show(value)
    
    @property
    def current_workspace(self) -> Workspace:
        """
        Returns workspace object of active workspace
        """
        return Workspace(self.app.current_workspace)

    # Document that this only takes effect if set before the first call to Application()
    # Add runtime error if set after initialization has been done

    @property
    def systemvue_path(self) -> Workspace:
        return Application.__SystemVue_path

    @systemvue_path.setter
    def systemvue_path(self, path):
        Application.__SystemVue_path = path

    # add property: is_internal
