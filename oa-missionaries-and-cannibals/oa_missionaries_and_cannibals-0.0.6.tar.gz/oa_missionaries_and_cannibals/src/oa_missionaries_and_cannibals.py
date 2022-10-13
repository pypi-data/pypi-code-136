from fileinput import filename
import os
import sys

def filePath(fileName):
    return fileName

def display():
    print('1. bfs 2. state space search')
    choice = int(input())

    if choice == 1:
        with open(filePath('bfs.py')) as f:
            print("===================BFS====================")
            for line in f:
                print(line, end='')
    elif choice == 2:
        with open(filePath('state_space_search.py')) as f:
            print("===================State Space Search====================")
            for line in f:
                print(line, end='')
    else:
        print("wrong choice")