#
# Product:   Macal
# Author:    Marco Caspers
# Date:      07-09-2022
#

class SourceLocation:
    """Contains the location in the source code."""
    def __init__(self, line: int, column: int) -> None:
        self.Line: int = line
        self.Column: int = column

    def __repr__(self):
        return f"SourceLocation(line={self.Line}, column={self.Column})"

    def __str__(self):
        return f"@({self.Line}, {self.Column})"

def nullLoc():
    return SourceLocation(-1,-1)