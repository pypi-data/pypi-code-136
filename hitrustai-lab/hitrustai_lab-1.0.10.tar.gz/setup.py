from setuptools import setup
import os
import subprocess

p = subprocess.Popen(args='pip install -r requirements.txt', shell=True)

def get_all_dir(rootdir):
    list_file = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d) and "__pycache__" not in d:
            print(d)
            try:
                list_file.append(d.split("./")[1])
            except Exception:
                list_file.append(d.split("./")[0])
    return list_file


list_file = []
rootdir = './hitrustai_lab'
for i in get_all_dir(rootdir):
    list_file.append(i)
    list_r = get_all_dir(i)
    if len(list_r) > 0:
        for ii in list_r:
            list_file.append(ii)

setup(
    name='hitrustai_lab',
    version='1.0.10',

    url='https://gitlab.hitrustai.com/bruce60108010204/hitrustai-lab',
    author='Bruce Tsai',
    author_email='brcue60108010204@gmail.com',
    packages=list_file,
)
