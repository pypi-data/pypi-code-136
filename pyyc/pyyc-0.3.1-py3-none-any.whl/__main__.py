import sys

def main():                 # Will be used as entry-point in setup.cfg

    print("Command line arguments:", sys.argv[1:])

if __name__ == '__main__':  # Will be used by `python -m pyyc`

    main()
