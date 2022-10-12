import os

def filePath(fileName):
    return os.path.join(os.path.dirname(__file__), fileName)

def display():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)
    print(files)
    print('1. bfs 2. state space search')
    choice = int(input())

    if choice == 1:
        with open('bfs.py') as f:
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