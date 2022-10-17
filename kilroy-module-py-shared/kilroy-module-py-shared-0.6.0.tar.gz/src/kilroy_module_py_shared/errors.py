class AppError(Exception):
    def __init__(self, code, reason):
        self.code = code
        self.reason = reason
        super().__init__(self.reason)

    def __str__(self):
        return f"{self.code}: {self.reason}"


INTERNAL_SERVER_ERROR = AppError(-1, "Internal server error.")
PARAMETER_GET_ERROR = AppError(1, "Unable to get parameter value.")
PARAMETER_SET_ERROR = AppError(2, "Unable to set parameter value.")
STATE_NOT_READY_ERROR = AppError(3, "State is not ready to be read.")
INVALID_CONFIG_ERROR = AppError(4, "Config is not valid.")
