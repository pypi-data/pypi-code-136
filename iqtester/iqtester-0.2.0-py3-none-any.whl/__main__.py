from .session import Session


def main():
    """Start a new session of IQ Tester"""

    s = Session()
    s.start()


if __name__ == "__main__":
    main()
