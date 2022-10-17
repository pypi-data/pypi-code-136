import os
import sys
from .clipython import cli

class CommandLine(cli):
    '''Command line interface for running a command in python'''
    
    def __init__(self, cmdline):
        cli.__init__(self, cmdline)
        self.cmdlinedefault = os.system("which $SHELL")
        
    def ls(self):
        self.cmdlist = os.system("ls -lash")
        
    def pwd(self):
        print("The path where you are right now!")
        self.wherepath = os.system("pwd")
        