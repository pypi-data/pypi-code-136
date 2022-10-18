from sys import exit, argv

from oak_build.app import App


def main():
    exit(App(argv[1:]).run())


if __name__ == '__main__':
    main()
