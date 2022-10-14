from io import BytesIO, TextIOWrapper
import logging, os, time, sys
from subprocess import PIPE, Popen
from .MakepieLogging import applog
from .Exceptions import MakepieException
from .Config import config

log = logging.getLogger(__name__)

class ShellCommand:
	def __init__(
		self,
		cmd: str,
		logger: logging.Logger,
		stdin=sys.stdin,
		env=os.environ,
		quiet=False,
		timeout: float=None,
		throws: bool=True,
	):
		self.cmd = cmd
		self.env = env
		self.quiet = quiet
		self.timeout = timeout
		self.throws = throws
		self.stdin = stdin

		self.logger = logger
		self.stdout = BytesIO()
		self.stderr = BytesIO()
		self.subprocess: Popen = None
		self.exec_time = None

	def logdata(self, data: bytes, name: str):
		if len(data) == 0:
			return

		text = data.decode(errors="replace")
		if not config("PRINT_STREAM_NAME", False):
			self.logger.info(text)
			return

		# Remove last character if it is a newline
		if text[-1] == "\n":
			text = text[:-1]

		# Insert prefix at the beginning of each line
		prefix = f"{name}> "
		formatted = prefix + text.replace("\n", "\n" + prefix) + "\n"
		self.logger.info(formatted)

	def log_stream(self, name: str):
		outdata = self.subprocess.__getattribute__(name).read(config("MAX_READ_SIZE", 4096))
		if outdata is None:
			return False

		self.__getattribute__(name).write(outdata)
		self.logdata(outdata, "out")
		return outdata != b""

	def log_streams(self):
		a = self.log_stream("stdout")
		b = self.log_stream("stderr")
		return a or b

	# Wait for the process to finish and log its output
	# stdin, process stdout & stderr should be set to non-blocking
	# Logger should have no terminator
	def subprocess_wait_loop(self):
		start = time.time()

		if isinstance(self.stdin, bytes):
			self.subprocess.stdin.write(self.stdin)
			self.subprocess.stdin.close()

		# Wait for command to finish/timeout
		while True:
			if (self.timeout is not None) and (time.time() - start > self.timeout):
				self.subprocess.kill()
				self.subprocess.wait()
				raise MakepieException(f"Command timed out after {self.timeout} seconds")

			if not isinstance(self.stdin, bytes):
				if isinstance(self.stdin, TextIOWrapper):
					data = self.stdin.read(config("MAX_READ_SIZE", 4096)).encode()
				elif isinstance(self.stdin, BytesIO):
					data = self.stdin.read(config("MAX_READ_SIZE", 4096))
				else:
					raise MakepieException("Unknown stdin type")
				self.subprocess.stdin.write(data)

			self.log_streams()

			# Exit condition
			if self.subprocess.poll() is not None:
				self.subprocess.wait()
				break

			time.sleep(config("POLL_INTERVAL", 0.01))

		# Empty streams
		while self.log_streams():
			pass

		self.exec_time = time.time() - start

	def run(self):
		# Not implemented for windows
		if os.name == "nt":
			raise MakepieException("Shell commands are not yet implemented on Windows")

		if not self.quiet:
			self.logger.debug(f"shell> {self.cmd}")

		self.subprocess = Popen(
			self.cmd,
			shell=True,
			stdin=PIPE,
			stdout=PIPE,
			stderr=PIPE,
			env=self.env
		)

		# Trick to avoid handling newline mess of streams
		previous_val = self.logger.handlers[0].terminator
		self.logger.handlers[0].terminator = ""

		# Save blocking state & set PIPES to non-blocking
		(out_no, err_no) = (self.subprocess.stdout.fileno(), self.subprocess.stderr.fileno())
		(b_out, b_err) = (os.get_blocking(out_no), os.get_blocking(err_no))
		(os.set_blocking(out_no, False), os.set_blocking(err_no, False))
		try:
			in_no = self.stdin.fileno()
			b_in = os.get_blocking(in_no)
			os.set_blocking(in_no, False)
		except Exception:
			in_no = None

		try:
			self.subprocess_wait_loop()
		finally:
			# Restore old terminator
			self.logger.handlers[0].terminator = previous_val

			# Restore blocking state
			(os.set_blocking(out_no, b_out), os.set_blocking(err_no, b_err))
			if in_no is not None:
				os.set_blocking(in_no, b_in)

			# Close streams
			self.subprocess.stdin.close()
			self.subprocess.stdout.close()
			self.subprocess.stderr.close()

		# Post execution
		log.info(f"Returned code: {self.subprocess.returncode} after {round(self.exec_time * 1000)} ms")

		if self.throws and self.subprocess.returncode != 0:
			raise MakepieException(f"Command returned error code {self.subprocess.returncode}")

	def results(self):
		return (self.subprocess.returncode, self.stdout.getvalue(), self.stderr.getvalue())

def sh(
	cmd: str,
	logger: logging.Logger = applog,
	stdin=sys.stdin,
	env=os.environ,
	quiet=False,
	timeout: float=None,
	throws: bool=True,
):
	cmd: ShellCommand = ShellCommand(cmd, logger, stdin, env, quiet, timeout, throws)
	cmd.run()
	return cmd
