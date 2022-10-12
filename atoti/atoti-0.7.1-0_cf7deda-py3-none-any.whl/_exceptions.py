"""Custom atoti exceptions.

They disguise the unhelpful Py4J stack traces occuring when Java throws an exception.
If any other exception is raised by the code inside the custom hook, it is processed normally.
"""

from __future__ import annotations


class AtotiException(Exception):
    """The generic atoti exception class.

    All exceptions which inherit from this class will be treated differently when raised.
    However, this exception is still handled by the default excepthook.
    """


class AtotiJavaException(AtotiException):
    """Exception thrown when Py4J throws a Java exception."""

    def __init__(
        self,
        message: str,
        *,
        java_traceback: str,
        java_exception: Exception,
    ):
        """Create a new AtotiJavaException.

        Args:
            message: The exception message.
            java_traceback: The stack trace of the Java exception, used to build the custom stack trace for atoti.
            java_exception: The exception from the Java code returned by Py4J.
        """
        # Call the base constructor with the parameters it needs
        super().__init__(message)
        self.java_traceback: str = java_traceback
        self.java_exception: Exception = java_exception
