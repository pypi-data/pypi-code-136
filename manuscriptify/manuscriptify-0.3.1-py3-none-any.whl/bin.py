# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
invoke the package

"""
import sys, subprocess

def manuscriptify():
    """package the command for setup.py"""
    shell_command = ['python', '-m', 'manuscriptify'] + sys.argv[1:]
    subprocess.run(shell_command)
