import pickle
from .architecture import all_archs
import os

def light_read(dname):
    #print(os.getcwd())
    curpath = os.path.dirname(os.path.abspath(__file__))

    f = open("{}/light/{}.bench".format(curpath, dname), "rb")
    bench = pickle.load(f)
    f.close()
    return bench

def read(name):
    f = open(name, "rb")
    bench = pickle.load(f)
    f.close()
    return bench

if __name__ == "__main__":
    read()
