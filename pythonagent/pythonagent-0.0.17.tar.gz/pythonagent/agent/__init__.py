
from pythonagent import config
from pythonagent.agent.internal.logs import configure_logging
from pythonagent.agent.probes.Instrumentation.parser import create_method_array,create_method_json
from pythonagent.agent.probes.Instrumentation.parser import create_method_array,create_method_json
import os
from pythonagent.lang import reload

'''
import os
path = os.path.dirname(config.__file__)
#print("Module path", path)
#os.chdir(path)
#print("Current working dir ==========================================",path)

f = open(os.path.join(path, 'agent/internal/intercept_module.py'), "a+")
f.truncate(0)
#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

infile =  open(r'/tmp/CavAgent/interceptor_points.txt')
outfile = open(os.path.join(path, './test.py'))
temp = []
for x in infile:
    if x.startswith('#'):
        temp.append(x.lstrip('#').rstrip('\n'))

for line in outfile:
    count=0
    for y in temp:
        if y in line and 'from' not in line:
            f.write('#'+line)
            count = 1
    if count==0:
        f.write(line)


infile.close()
outfile.close()
f.close()
'''


def entry_point_refresh():
    #import os
    path = os.path.dirname(config.__file__)
    #print("Module path", path)
    #os.chdir(path)
    #print("Current working dir ==========================================",path)

    try:
        f = open(os.path.join(path, 'agent/internal/intercept_module.py'), "a+")
        #f.truncate(0)
    #cwd = os.getcwd()  # Get the current working directory (cwd)
    #files = os.listdir(cwd)  # Get all the files in that directory
    #print("Files in %r: %s" % (cwd, files))
    
        infile =  open(os.environ.get('ND_HOME') + '/python/CavAgent/interceptor_points.txt')
        outfile = open(os.path.join(path, './test.py'))
        temp = []
        for x in infile:
            if x.startswith('#'):
                temp.append(x.lstrip('#').rstrip('\n'))

        for line in outfile:
            count=0
            for y in temp:
                if y in line and 'from' not in line:
                    f.write('#'+line)
                    count = 1
            if count==0:
                f.write(line)


        infile.close()
        outfile.close()
        f.close()
    except:
        pass
    return 0




from pythonagent.agent.probes import add_hook, Instrumentation
import logging



_agent = None
#RUNNING_MODE = 0
from pythonagent.agent.internal.agent import Agent

def configure(environ=None):
    agent_config = config.parse_environ()
    if environ:
        agent_config.update(config.parse_environ(environ))

    config.merge(agent_config)
    configure_logging()

    return config.validate_config(agent_config)

all_module_names = list()

try:
    # import configparser
    # configParser = configparser.RawConfigParser()
    # configParser.read(r'config.txt')
    # path_for_insProfile = configParser.get('SO_PATH', 'path_profile')

    import os

    path = os.environ.get('ND_HOME')
    path = path + '/config/ndsettings.conf'
    myvars = {}
    with open(path) as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = var
    try:
        path_for_insProfile = myvars.get('path_profile').strip('\n')
    except:
        path_for_insProfile = os.environ.get('ND_HOME') + "/python/CavAgent/instrumentationprofile.json"


    custom_methods_to_instrument_json = create_method_json(path_for_insProfile)["modules"]
    #all_module_names = list()

    for module in custom_methods_to_instrument_json:
        all_module_names.append(module["moduleName"])
except:
    pass

def bootstrap(agent=None):
    print("AGENT BOOTSTRAP")
    entry_point_refresh()
    import pythonagent.agent.internal.intercept_module
    reload(pythonagent.agent.internal.intercept_module)
    from pythonagent.agent.internal.intercept_module import BT
    BT_INTERCEPTORS = BT
    try:
        global _agent

        _agent = agent or Agent()
        hook = add_hook(_agent)
        #entry_point_refresh()
        #from pythonagent.agent.internal.intercept_module import BT as BT_INTERCEPTORS
        for module, patch in BT_INTERCEPTORS:
            hook.call_on_import(module, patch)

        for module in all_module_names:
            #print("MODULE NAME ", module)
            hook.call_on_import(module, Instrumentation.intercept_instrumented_method)

        _agent.module_interceptor = hook
        return _agent
    except:
        logging.getLogger('pythonagent.agent').exception('Error bootstrapping pythonagent; disabling.')
        return None

def get_agent_instance():
    if _agent is None:
        return bootstrap()
    else:
        return _agent


import time
from watchdog.observers.polling import PollingObserver
from watchdog.events import PatternMatchingEventHandler


def filewatchre(path, _agent):
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = True
    case_sensitive = True
# Creating an event handler using watchdog.events
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_modified(event):
        _agent = get_agent_instance()
        bootstrap(_agent)

    my_event_handler.on_modified = on_modified

    path = path

    go_recursively = True
    my_observer = PollingObserver(timeout=5)
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
filewatchre(os.environ.get('ND_HOME') + "/python/CavAgent/instrumentationprofile.json", _agent)
filewatchre(os.environ.get('ND_HOME') + "/python/CavAgent/interceptor_points.txt", _agent)

