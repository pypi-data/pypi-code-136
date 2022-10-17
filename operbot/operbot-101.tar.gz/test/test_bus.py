# This file is placed in the Public Domain.


import unittest


from opm.run import Bus, Handler


class Client(Handler):

    gotcha = False

    def announce(self, txt):
        self.gotcha = True

    def raw(self, txt):
        self.gotcha = True


clt = Client()


class TestBus(unittest.TestCase):


    def test_add(self):
        self.assertTrue(clt in Bus.objs)

    def test_announce(self):
        print(Bus.objs)
        Bus.announce("test")
        self.assertTrue(clt.gotcha)

    def test_byorig(self):
        self.assertEqual(Bus.byorig(repr(clt)), clt)

    def test_say(self):
        clt.gotcha = False
        Bus.say(repr(clt), "#test", "test")
        self.assertTrue(clt.gotcha)
