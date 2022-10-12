import os

def filePath(fileName):
    return f"oa_8_queens/src/{fileName}"

def display():
    with open(filePath('code.py')) as f:
        print("===================8 Queens using hill climbing====================")
        for line in f:
            print(line, end='')