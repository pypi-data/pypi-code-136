#import configparser
import errno
import os
#from agent.internal.proxy import Proxy
from main.pytrace import CommandInvocationError, CommandExecutionError
import sys

USAGE = "run <command> [args...]"

ABOUT = """Run a program with the agent enabled.

Use this command to instrument a Python application. If <command> is not the
path to an executable, the command is looked for in your PATH. The command may
be a Python interpreter or a supported server that embeds Python (like uwsgi
and gunicorn).

For example, if you normally run your application as below commands:

   1) python manage.py runserver --norelaod 10:20.0.117:6062
   2) gunicorn -w 4 -b unix:acme.sock acme.app:app

You can run the same application instrumented by pythonagent with below commands:
    
   1) cavagent run python manage.py runserver --norelaod 10:20.0.117:6062 
   2) cavagent run -- gunicorn -w 4 -b unix:acme.sock acme.app:app


The agent requires the TestRun to be running. If it
is not running, your application will not be start.

"""

OPTION = {
    'cli': 'run in CLI mode',
    
    # 'no-watchdog': 'disable the watchdog when auto-starting proxy',
    
    'config-file': {
        'short': 'c',
        'help': 'the config file to use',
        'value': True,
        'value_help': '<file>',
    },
    
    'app': {
        'short': 'a',
        'help': 'the name of the app',
        'value': True,
        'value_help': '<app>',
    },
    'tier': {
        'short': 't',
        'help': 'the name of the tier',
        'value': True,
        'value_help': '<tier>',
    },
    # 'node': {
    #     'short': 'n',
    #     'help': 'the name of the node',
    #     'value': True,
    #     'value_help': '<node>',
    # },

    # 'controller': {
    #     'short': 'h',
    #     'help': 'the host (and optionally port) of the controller',
    #     'value': True,
    #     'value_help': '<host>[:<port>]',
    # },

    # 'ssl': {
    #     'help': 'pass to use SSL with the controller',
    # },
    #
    # 'no-ssl': {
    #     'help': 'pass to disable SSL with the controller (the default)',
    # },

    'proxyMode': {
        'short': 'pmode',
        'help': 'proxyMode',
        'value': True,
        'value_help': '<proxyMode>  value - [0/1]',
    },

    'proxyConType': {
        'short': 'pctype',
        'help': 'please enter proxy con type ',
        'value': True,
        'value_help': '<proxyConType> value - [0/1]',
    },

    'proxyIP': {
        'short': 'pip',
        'help': 'please enter proxy IP host address',
        'value': True,
        'value_help': '<proxyConType>',
    },

    'proxyPort': {
        'short': 'pport',
        'help': 'please enter proxy port number ',
        'value': True,
        'value_help': '<proxyPort>',
    },

    # Internal / undocumented options

    # 'run-proxy-script': {
    #     'help': False,     # "Path to runProxy script"
    #     'value': True,
    # },
    #
    # 'proxy-args': {
    #     'help': False,  # "Command line arguments to pass to runProxy"
    #     'value': True,
    # },

}


def command(options, args):

    '''
    processname = 'TestRun'
    tmp = os.popen("nsu_show_netstorm").read()
    proccount = tmp.count(processname)

    if proccount > 0:
        print("TestRun is running...")
    else:
        print("ERROR!! TestRun is not running on this machine !!!\nKindly start the TestRun and try again...")
        sys.exit(1)
    '''
    import bootstrap
    pythonpath = [os.path.dirname(bootstrap.__file__), '.']

    if not args:
        raise CommandInvocationError('missing command: run <options> -- <command> [args...]')

    environ = os.environ

    if 'PYTHONPATH' in environ:
        pythonpath.append(environ['PYTHONPATH'])

    environ['PYTHONPATH'] = ':'.join(pythonpath)
    environ['LD_LIBRARY_PATH'] = "/usr/local/lib"
    environ['LD_PRELOAD'] = "/usr/local/lib/libapr-1.so /usr/local/lib/libwebsockets.so /usr/local/lib/libcrypto.so /usr/local/lib/libssl.so"
    #print('ND_HOME set as ',environ.get('ND_HOME'))
    print("ND_HOME Environment variable :", environ.get('ND_HOME'))
    if environ.get('ND_HOME') is None:
        environ['ND_HOME'] = "/opt/cavisson/netdiagnostics"
        environ['NDHOME'] = "/opt/cavisson/netdiagnostics"
        print("Taking Default ND_HOME path",environ.get('ND_HOME'))
    environ['CAV_RUNNING_MODE'] = '0'
    
    if 'config-file' in options:
        environ['CAV_CONFIG_FILE'] = options['config-file']
    if 'app' in options:
        environ['CAV_APP_NAME'] = options['app']
    if 'tier' in options:
        environ['CAV_TIER_NAME'] = options['tier']
    if 'node' in options:
        environ['CAV_NODE_NAME'] = options['node']
    if 'proxyMode' in options:
        environ['CAV_proxyMode'] = options['proxyMode']
    if 'proxyConType' in options:
        environ['CAV_proxyConType'] = options['proxyConType']
    if 'proxyIP' in options:
        environ['CAV_proxyIP'] = options['proxyIP']
    if 'proxyPort' in options:
        environ['CAV_proxyPort'] = options['proxyPort']
    environ['nd_init_done'] = '0'

    # if 'ssl' in options:
    #     environ['APPD_SSL_ENABLED'] = 'on'
    # elif 'no-ssl' in options:
    #     environ['APPD_SSL_ENABLED'] = 'off'

    # if 'controller' in options:
    #     value = options['controller']
    #
    #     if ':' in value:
    #         host, port = value.split(':', 1)
    #         environ['APPD_CONTROLLER_HOST'] = host
    #         environ['APPD_CONTROLLER_PORT'] = port
    #     else:
    #         environ['APPD_CONTROLLER_HOST'] = value

    # if 'use-manual-proxy' not in options:
    #     proxy_args = []
    #
    #     if 'no-watchdog' in options:
    #         proxy_args.append('--no-watchdog')
    #
    #     if 'run-proxy-script' in options:
    #         proxy_args.append('--run-proxy-script')
    #         proxy_args.append(options['run-proxy-script'])
    #
    #     if 'proxy-args' in options:
    #         proxy_args.extend(shlex.split(options['proxy-args']))

       # proxy.start(proxy_args)

    try:
        #proxy = Proxy.getInstance()
        #print("Proxy object created in run.py: ",proxy)

        #import bootstrap.sitecustomize
        #import agent.internal.agent as agent
        #agent.Agent().start()
        os.execvpe(args[0], args, environ)


    except OSError as exc:
        if exc.errno == errno.ENOENT:
            raise CommandExecutionError('%s: no such file or directory' % args[0])
        elif exc.errno == errno.EPERM:
            raise CommandExecutionError('%s: permission denied' % args[0])
        raise
