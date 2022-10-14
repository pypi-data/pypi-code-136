from pythonagent.find import find
import traceback
import sys

py_ver = sys.version_info[0]

USAGE = "auto discovery to generate instrumentation profile"
ABOUT = "Command to push auto discovery feature of Python Agent"


def command(options, args):
    # Calling auto discovery method to discover and create instrumentation profile
    #print(args[0])
    #if args[0] is None:
    #    raise TypeError("'None' value provided for application path !!")   
    try: 
        find(args[0])
        print('auto discovery called, Instrumentation profile has been generated !!')
    except:
        if py_ver == 3: 
            traceback.print_exc(limit=None, file=None, chain=True)
        else:
            print_exception(sys.exc_type, sys.exc_value, sys.exc_traceback, limit, file)
            print('No path provided for application !!\nPlease provide application path along with commond.')
        
