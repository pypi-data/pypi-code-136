# -*- coding: utf-8 -*-

from .utils import print_json, format_json
# from .prompt import prompt
from .separator import Separator
from .prompts.common import default_style

__version__ = '0.1.0'


class PromptParameterException(ValueError):
    def __init__(self, message, errors=None):

        # Call the base class constructor with the parameters it needs
        super().__init__('You must provide a `%s` value' % message, errors)


# The code below here is here because of backwards-compatibility. Before,
# people were using style_from_dict and importing it from here. It's better to
# use Style.from_dict, as recommended by prompt_toolkit now.
from prompt_toolkit.styles import Style


def style_from_dict(style_dict):
    # Deprecated function. Users should use Style.from_dict instead.
    # Keep this here for backwards-compatibility.
    return Style.from_dict(style_dict)


__all__ = ["PromptParameterException", "style_from_dict"]
