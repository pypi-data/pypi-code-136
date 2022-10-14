import sys
from .mod import read_config

def main():                 # Will be used as entry-point in setup.cfg

    print(" MAIN ".center(50, '-'))
    cfg = read_config()     # will look for config files distributed along pyyc
    print(cfg['DEFAULT']['version'])

    print("Command line arguments:", sys.argv[1:])

if __name__ == '__main__':  # Will be used by `python -m pyyc`

    main()
