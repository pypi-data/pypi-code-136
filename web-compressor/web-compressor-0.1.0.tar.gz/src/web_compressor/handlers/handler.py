import abc
import re
from typing import List, Union


class Handler(metaclass=abc.ABCMeta):
    """
    Base class for handlers
    """

    # Validation rules
    ruleset: Union[re.Pattern, List[str]]

    @abc.abstractmethod
    def is_ready(self) -> bool:
        """
        Checks if everything checks out

        :return: bool Setup status
        """

    def validate(self, mime_type: str) -> bool:
        """
        Validates file & its mediatype against ruleset

        :param mime_type: str Mediatype to be validated
        :return: bool
        """

        # If no ruleset available ..
        if not self.ruleset:
            # .. anything goes
            return True

        # Determine suitable validation method
        # (1) List of allowed mediatypes
        if isinstance(self.ruleset, list):
            return mime_type in self.ruleset

        # (2) Regex of allowed mediatypes
        if isinstance(self.ruleset, re.Pattern):
            return self.ruleset.match(mime_type) is not None

        return False
