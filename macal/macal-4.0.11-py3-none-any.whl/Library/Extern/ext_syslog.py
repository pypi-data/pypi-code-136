# Product:   Macal
# Author:    Marco Caspers
# Date:      28-09-2022
#

import sys
import logging
import macal


class SysLog:
	def __init__(self):
		self.__address__ = 'localhost'
		self.__port__ = 514

		# REF, modified from:
		#   https://stackoverflow.com/a/19367225

		self.__config__ = {
			'version':1,
			'disable_existing_loggers': True,
			'formatters': {
				'verbose': {
					'format': '%(levelname)s %(module)s P%(process)d T%(thread)d %(message)s'
				},
				'simple': {
					'format': '%(levelname)s %(message)s'
				},
			},
			'handlers': {
				'stdout': {
					'class': 'logging.StreamHandler',
					'stream': sys.stdout,
					'formatter': 'simple',
				},
				'syslog0': {
					'class':     'logging.handlers.SysLogHandler',
					"address":   '/dev/log',
					'facility':   "local0",
					'formatter':  'simple',
				},
				'syslogR': {
					'class':     'logging.handlers.SysLogHandler',
					"address":   (self.__address__, self.__port__),
					'formatter':  'simple',
				},
			},
			'loggers': {
				'macal-syslog': {
					'handlers':  ['syslog0', 'stdout'],
					'level':     logging.DEBUG,
					'propagate': True,
				},
				'macal-syslog-remote': {
					'handlers':  ['syslogR'],
					'level':     logging.DEBUG,
					'propagate': False,
				},
			},
		}

		logging.config.dictConfig(self.__config__)

		self.handle   		 = None
		self.debug    		 = None
		self.info     		 = None
		self.warn     		 = None
		self.error    		 = None
		self.critical 		 = None
		
		self.syslog_enabled  = False
		self.remote_enabled  = False



	def SysLogInit(self, remote: bool):
		if (remote is True and self.remote_enabled) or (remote is False and self.syslog_enabled):
			raise Exception("Syslog is already initialized!")
		if remote is True:
			self.remote_enabled = True
			self.handle         = logging.getLogger('macal-syslog-remote')
			self.debug          = self.remote.debug
			self.info           = self.remote.info
			self.warn           = self.remote.warn
			self.error          = self.remote.error
			self.critical       = self.remote.critical
		else:
			self.syslog_enabled = True
			self.handle   		= logging.getLogger('macal-syslog')
			self.debug    		= self.handle.debug
			self.info     		= self.handle.info
			self.warn     		= self.handle.warn
			self.error    		= self.handle.error
			self.critical 		= self.handle.critical
		

		
	def SysLogSetAddress(self, address, port):
		if self.remote_enabled is True or self.syslog_enabled is True:
			raise macal.RuntimeError("Cannot change configuration, syslog was already initialized!", None, None)
		self.__address__ = address
		self.__port__ = port
		logging.config.dictConfig(self.__config__)


SysLogLocal = SysLog()
        
def Syslog(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of Syslog function"""
    macal.validateFunctionArguments(func, scope, filename)
    lvl = scope.getVariable("level")
    level = lvl.getValue()
    message = scope.getVariable("message").getValue()
    if level == "debug":
        SysLogLocal.debug(message)
    elif level == "info" or level == "information":
        SysLogLocal.info(message)
    elif level == "warn" or level == "warning":
        SysLogLocal.warn(message)
    elif level == "error":
        SysLogLocal.error(message)
    elif level == "critical":
        SysLogLocal.critical(message)
    else:
        raise macal.RuntimeError(f"Invalid syslog level given: {level}", lvl.Token.Location, filename)



def SyslogInit(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of SysLog init function"""
    macal.validateFunctionArguments(func, scope, filename)
    remote = scope.getVariable("remote").getValue()
    SysLogLocal.SysLogInit(remote)



def SyslogSetAddress(func:macal.FunctionDefinition, scope: macal.Scope, filename: str) -> None:
    """Implementation of SysLog SetAddress function"""
    macal.validateFunctionArguments(func, scope, filename)
    address = scope.getVariable("address").getValue()
    port = scope.getVariable("port").getValue()
    SysLogLocal.SysLogSetAddress(address, port)
