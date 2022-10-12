"""
This file contains bits & pieces that need to be accessed by widely different 
parts of the codebase.

E.g., by the readme-generator & by a parser.
"""


def bx_tool_string_to_name_and_version(bx_tool_string: str) -> (str, str):
    return bx_tool_string.split(":")