class BaseExceptions(Exception):
	_message: str = None
	_errors: list = []

	def __init__(self, *errors):
		errors = '\n Ref : '.join(errors)
		super().__init__('Exception Occurred.' if self._message is None else f"\n{self._message} :\n{errors}")
		self._errors = errors if isinstance(errors, dict) else list()

	@property
	def message(self):
		return self._message

	@property
	def error_list(self):
		return self._errors


class PyenvException():
	class BaseDirDoesNotExists(BaseExceptions):
		_message = "Root Directory Does Not Exists."

	class ConfigFileDoesNotExist(BaseExceptions):
		_message = "Configuration File Does Not Exists."

	class ConfigurationLoadingFailed(BaseExceptions):
		_message = "Failed To Load Configuration From Config File."
