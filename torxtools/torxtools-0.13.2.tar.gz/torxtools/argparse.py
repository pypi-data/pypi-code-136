"""
Parser types for command-line options, arguments and sub-commands

Example
-------

.. code-block::

    parser.add_argument(
        "--size", "-s",
        dest="size",
        help="[MB] Minimal size of attachment",
        type=torxtools.argparse.is_int_positive,
        default=100,
    )

"""

from argparse import ArgumentTypeError

__all__ = [
    "is_int_positive",
    "is_int_positive_or_zero",
    "is_int_negative",
    "is_int_negative_or_zero",
]


def is_int_positive(value: int) -> int:
    """
    Verify that argument passed is a positive integer.
    """
    number = int(value)
    if number <= 0:
        raise ArgumentTypeError(f"value '{value}' must be positive")
    return number


def is_int_positive_or_zero(value: int) -> int:
    """
    Verify that argument passed is a positive integer or zero.
    """
    number = int(value)
    if number < 0:
        raise ArgumentTypeError(f"value '{value}' must be positive or zero")
    return number


def is_int_negative(value: int) -> int:
    """
    Verify that argument passed is a negative integer.
    """
    number = int(value)
    if number >= 0:
        raise ArgumentTypeError(f"value '{value}' must be negative")
    return number


def is_int_negative_or_zero(value: int) -> int:
    """
    Verify that argument passed is a negative integer or zero.
    """
    number = int(value)
    if number > 0:
        raise ArgumentTypeError(f"value '{value}' must be negative or zero")
    return number
