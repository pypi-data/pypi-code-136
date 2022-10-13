import subprocess
import os
#from .delete import deleting
import subprocess
import sys
import glob

def wrong():
    with open('md.log', 'w') as f:
        f.write('Performance:       0.00        0.00' + "\n")
        f.close
    
    subprocess.check_call('for i in script_*;do cp -vn md.log ${i}/;done', shell=True)
    my_path=(os.getcwd())
    filenames=glob.glob(my_path + '/*/md.log', recursive=True)
    for f in filenames:
        with open(f, 'r') as original: data = original.read()
        with open(f, 'w') as modified: modified.write("Performance:       0.00        0.00\n" + data)
