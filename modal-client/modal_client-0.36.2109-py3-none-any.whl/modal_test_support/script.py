from .stub import f, stub

if __name__ == "__main__":
    with stub.run():
        assert f(2, 4) == 20
