import os
from typing import Tuple, List


def get_lines(folder: str = "replit_bot") -> Tuple[int, List[Tuple[str, int]]]:
    output = 0
    file_paths = []
    for i in os.walk(folder):
        parent = i[0]
        for j in i[-1]:
            if j.endswith(".py") or j.endswith(".html"):
                current = len(open(parent + "/" + j).read().split("\n"))
                output += current
                file_paths.append((parent + "/" + j, current))
    return output, file_paths
