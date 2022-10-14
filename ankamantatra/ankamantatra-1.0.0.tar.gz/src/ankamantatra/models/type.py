from enum import Enum

class Type(Enum):
    """Enum class for the different types of questions"""

    MULTIPLE = "multiple"
    UNIQUE = "unique"
    TEXT = "text"
    NUMBER = "number"
    STRING = "string"