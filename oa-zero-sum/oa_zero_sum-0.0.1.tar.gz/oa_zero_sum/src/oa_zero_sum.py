import os

def filePath(fileName):
    return f"oa_zero_sum/src/{fileName}"

def display():
    with open(filePath('code.py')) as f:
        print("===================Zero Sum using alpha beta prunning====================")
        for line in f:
            print(line, end='')