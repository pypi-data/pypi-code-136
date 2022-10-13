from pathlib import Path

import numpy as np


def ghk_output_reader(filepath: Path) -> dict:
    GHK = {
        "GR": None,
        "GT": None,
        "HR": None,
        "HT": None,
        "K1": None,
        "K2": None,
        "K3": None,
        "K4": None,
        "K5": None,
        "K6": None,
        "K7": None,
    }
    if not filepath.is_file():
        raise FileNotFoundError(f"{filepath} not found.")

    f = open(filepath, "r")
    for line in f:
        line = line.strip()
        if line[0:2] == "GR":
            break
    line = f.readline().replace(" ", "").split(",")
    print(line)
    (
        GHK["GR"],
        GHK["GT"],
        GHK["HR"],
        GHK["HT"],
        GHK["K1"],
        GHK["K2"],
        GHK["K3"],
        GHK["K4"],
        GHK["K5"],
        GHK["K6"],
        GHK["K7"],
    ) = np.array(line, "float")
    # print(GR, GT, HR, HT, K1, K2, K3, K4, K5, K6, K7)

    return GHK