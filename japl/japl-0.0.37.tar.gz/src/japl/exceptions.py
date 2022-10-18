class EmptyDataFrameException(Exception):
    """
    An error defined when a DataFrame is empty and should have something
    for the process to work fine.

    Args:
        Exception (Exception): The same set of arguments you would pass
        to any normal exception in python.
    """
    def __init__(self, message: str = 'The DataFrame has no data.'):
        super().__init__(message)
class ParameterTypingException(Exception):
    """
    An error defined when a DataFrame is empty and should have something
    for the process to work fine.

    Args:
        Exception (Exception): The same set of arguments you would pass
        to any normal exception in python.
    """
    def __init__(self, variable: str = None, expected_type: str = None, real_type: str = None):
        if variable and expected_type and real_type:
            super().__init__(f"The parameter given for the parameter {variable} should be of type {expected_type}, got {real_type}.")
        elif variable and not expected_type and not real_type:
            super().__init__(f"The parameter given for the parameter {variable} does not match the expected type.")
        else:
            super().__init__("The parameter given for a parameter does not match the expected type.")