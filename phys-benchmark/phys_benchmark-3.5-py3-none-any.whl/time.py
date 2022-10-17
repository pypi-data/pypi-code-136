from subprocess import call
import time
import subprocess
import os


def time_count():
    def check():
        with open('file.txt') as f:
        #with open(os.path.join(os.path.dirname(__file__), 'file.txt')) as f:
            datafile = f.readlines()
        found = False  # This isn't really necessary
        for line in datafile:
            if ('bingo') in line:
                # found = True # Not necessary
                return True
        return False  # Because you finished the search without finding


    while True:
        if check():
            x=('False')
            subprocess.check_call('squeue -n bingo > file.txt', shell=True)
            time.sleep(10.4)
        else:
            y=('True')
            #subprocess.check_call('squeue -n bingo > file.txt', shell=True)
            break
