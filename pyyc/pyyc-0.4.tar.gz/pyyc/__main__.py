import sys

def main():                 # Will be used as entry-point in setup.cfg
    """
    Main function of the package.

    Read arguments from `sys.argv[1:]`.

    .. Note:: Will be used as `pyyc` entry-point in :ref:`setup.cfg`,
              and as the main script (`python -m pyyc`).
    """

    print("Command line arguments:", sys.argv[1:])


def main_addition():
    """
    Another entry point of the package.

    Read arguments from `sys.argv[1:]`.

    .. Note:: Will be used as `pyyc_addition` entry-point in
              :ref:`setup.cfg`.
    """

    try:
        iargs = [ int(arg) for arg in sys.argv[1:] ]
    except ValueError:
        print("Only integers accepted as command-line arguments:", sys.argv[1:])

    print(" + ".join([ str(arg) for arg in iargs ]), "=", sum(iargs))


if __name__ == '__main__':  # Will be used by `python -m pyyc`

    main()
