import os
import signal

def createPidFile(filename="pidfile.pid", killOldProcess=True):
	"""Writes the process ID of the running Python process to the PID-file. If a pidfile exists it kills the running process if wanted.
	:param filename: The name of the PID-File. 'pidfile.pid' by default.
	:param killOldProcess: Stops the process with the process ID found in the pidfile. True by default.
	"""
	if killOldProcess:
		try:
			with open(filename, "r") as pidfile:
				pid = pidfile.read()
				os.kill(int(pid), signal.SIGTERM)
		except FileNotFoundError:
			pass
		except PermissionError:
			pass
		except OSError:
			pass
	with open(filename, "w") as pidfile:
		pidfile.write(str(os.getpid()))
	