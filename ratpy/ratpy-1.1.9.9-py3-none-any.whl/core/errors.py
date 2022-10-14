
class RatsError(Exception):
    """Error class to handle errors raised while parsing RATS files"""
    # def __init__(self, message, errors):
    #     # Call the base class constructor with the parameters it needs
    #     super().__init__(message)
    #     self.errors = errors
    pass


class SamplesMissingError(Exception):
    """Error for when data samples are missing from a packet"""
    pass


class CouldNotConstructDataframeError(Exception):
    """Final error to handle failed dataframe creation"""
    pass


class DataframeNotValidError(Exception):
    """Dataframe fails to pass its validation check"""
    pass



