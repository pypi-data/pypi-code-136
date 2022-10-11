"""Hello World!
Placeholder module for the data-exhaust-utils package. Still, it can do Math! :)
And a test validator is included.
"""
from cerberus import Validator

TEST_SCHEMA = {
    'num1': {'type': 'integer'},
    'string1': {'type': 'string'},
}

def hello_world():
    """Return a string "Hello World!"."""
    return "Hello World!"

def adder(num1, num2):
    """Add two numbers."""
    return num1 + num2

def substracter(num1, num2):
    """Substract two numbers."""
    return num1 - num2

def multiplier(num1, num2):
    """Multiply two numbers."""
    return num1 * num2

def divider(num1, num2):
    """Divide two numbers."""
    return num1 / num2

def test_validator(test_data):
    """Validate test data."""
    v = Validator()
    return v.validate(test_data, TEST_SCHEMA)
