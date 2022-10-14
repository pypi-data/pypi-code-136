from typing import Callable, List, Tuple
from functools import wraps


def space(func: Callable) -> Callable:
    """Decorator for class methods to print new lines before and after"""

    # wraps decorator needed so space can be applied to class methods
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        print()
        res = func(self, *args, **kwargs)
        print()

        return res

    return wrapped


class Formatter:
    """An API to format statements printed to standard output"""

    # Map available formatting option codes to their string representations
    # key: str = style code
    # value: tuple = (str = style string, int: printed length of style code)
    format_codes_map = {
        "BLUE": ("\033[94m", 5),
        "GREEN": ("\033[92m", 5),
        "RED": ("\033[91m", 5),
        "BOLD": ("\033[1m", 4),
        "END": ("\033[0m", 4),
    }

    def __init__(self, width: int = 78) -> None:

        # The max width for all lines printed
        self.width = width

    def center(
        self,
        msg: str,
        styles: List[str] = [],
        fill_char: str = " ",
        inner_width: int = 0,
        inner_border_char: str = "",
        format_char_count: int = 0,
        end: str = "\n"
    ) -> None:
        """
        Print msg across self.width with optional styling and inner container

        Parameters
        ----------
        msg : str
            The message to be printed
        styles : List[str]
            List of syle codes (see options above) to be applied to msg
        fill_char : str
            Character(s) to be used to fill empty space around msg
        inner_width : int
            The inner width to which msg should be centered
        inner_border_char : str
            The border to be used for the "inner container" containing msg
        format_char_count : int
            The number of printed characters in msg that represent formatting,
            such that len(msg) - fc is the actual printed length of msg
        end : str
            The character(s) passed as the 'end' parameter of 'print'
        """

        # Calculate the actual printed length of msg less formatting characters
        true_len = len(msg) - format_char_count

        # Apply styles to message
        msg, _ = self.apply_formatting(msg, styles)

        # Calculate margin: spaces printed to left of inner container
        margin = self.width - inner_width if inner_width else 0
        left_margin = margin // 2

        # Calculate padding: combined space on each side of msg in container
        padding = self.width - margin - true_len - 2 * len(inner_border_char)
        left_padding = padding // 2

        # Right padding only needed if fill is not ' ' or for inner container
        # Otherwise, nothing needs to be printed to right of msg
        if inner_width or fill_char != " ":
            right_padding = left_padding
            # If total padding is odd, add the extra char to right padding
            if padding % 2 == 1:
                right_padding += 1
        else:
            right_padding = 0

        # Assemble entire formatted_msg
        formatted_msg = (
            f"{' ' * left_margin}{inner_border_char}{fill_char * left_padding}"
            f"{msg}{fill_char * right_padding}{inner_border_char}"
        )

        # Print formatted message with custom end
        print(formatted_msg, end=end)

    def apply_formatting(self, msg: str, styles=["BOLD"]) -> Tuple[str, int]:
        """
        Apply multiple styles to a msg and return the formatted string

        Parameters
        ----------
        msg : str
            The message to be formatted
        styles : List[str]
            List of syle codes (see options above) to be applied to msg
        Return
        ------
        formatted msg : str
            The msg with formatting code prefixes and suffix added
        format character count : int
            The number of characters added to msg (when printed) by formatting
        """

        # Apply styles to msg by adding formatting prefix and suffix
        formatting_prefix = ""
        format_char_count = 0
        for style in styles:

            # Handle invalid style code
            if style not in self.format_codes_map:
                raise NotImplementedError(f'"{style}" is not implemented')

            # Add prefix for current style to formatting_prefix
            formatting_prefix += self.format_codes_map[style][0]

            # Increment count of format characters for style
            format_char_count += self.format_codes_map[style][1]

        # Wrap message with formatting prefix and suffix
        msg = f"{formatting_prefix}{msg}{self.format_codes_map['END'][0]}"

        # Increment count of format characters for suffix
        format_char_count += self.format_codes_map['END'][1]

        # Return formatted string and formatted character count
        return msg, format_char_count

    @space
    def prompt(self, msg: str) -> str:
        """Return user-input with center-aligned user-prompt"""

        # Print message with formatting and no new line character
        self.center(f">> {msg} >>", ["BLUE"], " ", 0, "", -1, "")

        # Request input with cursor immediately following printed message
        return input(" ")
