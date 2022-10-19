from mypy import api

if __name__ == "__main__":
    result = api.run(["./tests/mypy/mypy_test.py", "--show-traceback"])

    if result[0]:
        print("\nType checking report:\n")
        print(result[0])  # stdout

    if result[1]:
        print("\nError report:\n")
        print(result[1])  # stderr

    print("\nExit status:", result[2])
