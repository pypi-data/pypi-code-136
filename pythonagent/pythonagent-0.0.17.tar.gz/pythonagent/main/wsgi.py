from __future__ import unicode_literals

from pythonagent.agent.probes.frameworks.wsgi import WSGIMiddleware
#from pythonagent import config
#config.WSGI_SCRIPT_ALIAS = input("Enter the absolute path of WSGI application script. (command to get 'readlink -f <script_path.py>') : ")
application = WSGIMiddleware()
