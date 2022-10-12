import os

def filePath(fileName):
    return f"oa_tsp/src/{fileName}"

def display():
    with open(filePath('code.py')) as f:
        print("===================TSP using simulated annealing====================")
        for line in f:
            print(line, end='')