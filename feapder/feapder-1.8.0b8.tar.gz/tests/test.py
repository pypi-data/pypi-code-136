from feapder.utils.tools import LazyProperty


class C:
    def __init__(self):
        print("c")

    def test(self):
        print("test")


class A:
    b = None

    @LazyProperty
    def test(self):
        print("test")
        return C()

    @property
    def _b(self):
        if not self.__class__.b:
            self.__class__.b = C()
        return self.__class__.b

    def run(self):
        self._b.test()


a = A()
print(a.test)
a = A()
print(a.test)
a = A()
print(a.test)
