class PicselliaError(Exception):
    """Base class for exceptions."""

    def __init__(self, message):
        """
        Arguments:
            message (str): Informative message about the exception.
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class AuthenticationError(PicselliaError):
    """Raised when your token does not match to any known token"""

    pass


class UnauthorizedError(PicselliaError):
    """Raised when your token does not match to any known token"""

    pass


class ForbiddenError(PicselliaError):
    """Raised when your token does not match to any known token"""

    pass


class ResourceNotFoundError(PicselliaError):
    """Exception raised when a given resource is not found."""

    pass


class ResourceConflictError(PicselliaError):
    """Exception raised when a given resource already exists."""

    pass


class BadRequestError(PicselliaError):
    """Indicates a malformed or unsupported query. This can be the result of either client
    or server side query validation."""

    pass


class NetworkError(PicselliaError):
    """Raised when an HTTPError occurs."""

    pass


class ApiLimitError(PicselliaError):
    """Raised when the user performs too many requests in a short period
    of time."""

    pass


class ProcessingError(PicselliaError):
    """Raised when an algorithmic error occurs."""

    pass


class InsufficientResourcesError(PicselliaError):
    """Raised when your token does not match to any known token"""

    pass


class NoDataError(PicselliaError):
    """Raised when you try to retrieve data from an empty datalake"""

    pass


class ImpossibleAction(PicselliaError):
    """Raised when an action is impossible"""

    pass


class UndefinedObjectError(PicselliaError):
    """Raised when Dao is initialized without id"""

    pass


class ContextSourceNotDefined(PicselliaError):
    """Raised if experiment or dataset of a ModelContext is not defined"""

    pass


class NoConnectorFound(PicselliaError):
    """Raised if connexion object is not pointed to any organization"""

    pass


class NoBaseModelVersionError(PicselliaError):
    """Raised when exception has no base model"""

    pass


class NoBaseExperimentError(PicselliaError):
    """Raised when exception has no base experiment"""

    pass


class UploadFailed(PicselliaError):
    """Raised when an upload of a file has failed"""

    pass


class BadConfigurationScan(PicselliaError):
    """Raised when scan could not be created"""

    pass


class NoModel(PicselliaError):
    """Raised when there is no model for a deployment"""

    pass


class NoShadowModel(PicselliaError):
    """Raised when there is no shadow model for a deployment"""

    pass


class UnparsableAnnotationFileException(PicselliaError):
    """Raised when annotations file is unparsable"""

    pass


class FileNotFoundException(PicselliaError):
    """Raised when a file is not found"""

    pass


class WaitingAttemptsTimeout(PicselliaError):
    """Raised when a job.wait_for_status is taking too much attempts"""

    pass


class PicselliaOutError(Exception):
    def __init__(self, picsellia_error: PicselliaError) -> None:
        super().__init__(picsellia_error)
        self.message = picsellia_error.message

    def __str__(self) -> str:
        return f"Something went wrong.\n{self.message}."
