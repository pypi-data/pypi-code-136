from Pyro5.api import Daemon, expose

@expose
class Thing:
    items = ['e','b','c','d','a']

    def __dunder__(self):
        print(".dunder")
        return "dunder"

    def __len__(self):
        print(".len")
        return len(self.items)

    def __contains__(self, item):
        print(".contains", item)
        return item in self.items

    def __getitem__(self, item):
        print(".getitem", item)
        return self.items[item]

    def __reversed__(self):
        print(".reversed")
        return reversed(self.items)

    def __iter__(self):
        print(".iter")
        return iter(self.items)

    def __setitem__(self, key, value):
        print(".setitem", key, value)
        self.items[key]=value

    def __delitem__(self, key):
        print(".delitem", key)
        del self.items[key]


if __name__ == "__main__":
    Daemon.serveSimple({
        Thing: "thing"
    })
