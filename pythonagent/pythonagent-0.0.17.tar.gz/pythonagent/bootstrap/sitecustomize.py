"""Trick Python into loading the agent.

"""

from __future__ import unicode_literals
import logging
import os
import sys

try:
    sys.path.remove(os.path.dirname(__file__))
except ValueError:  # directory not in sys.path
    pass

try:
    import pythonagent.agent as agent
    #agent.Agent.start()
    agent.configure()
    agent.bootstrap()
except:
    logger = logging.getLogger('pythonagent.agent')
    logger.exception('Exception in agent startup.')
finally: 
    pass
    #appdynamics.agent.load_sitecustomize()
