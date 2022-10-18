# -*- coding: utf-8 -*-
"""
Automatic tests for module ldap0.msad
"""

# from Python's standard lib
import unittest
import uuid
from binascii import unhexlify

from ldap0.msad import sid2sddl, sddl2sid


class Test001Functions(unittest.TestCase):

    test_vectors = (
        (
            b'\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00\xbaZ\x17^U\xdf\x83a)XU\x0eP\x04\x00\x00',
            'S-1-5-21-1578588858-1636032341-240474153-1104'
        ),
        (
            b'\x01\x04\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00\xbaZ\x17^U\xdf\x83a)XU\x0e',
            'S-1-5-21-1578588858-1636032341-240474153'
        ),
    )

    def test001_sid2sddl(self):
        for sid_b, sddl_s in self.test_vectors:
            self.assertEqual(sid2sddl(sid_b), sddl_s)

    def test002_sddl2sid(self):
        for sid_b, sddl_s in self.test_vectors:
            self.assertEqual(sddl2sid(sddl_s), sid_b)

    def test003_inverse(self):
        for sid_b, sddl_s in self.test_vectors:
            self.assertEqual(sid2sddl(sddl2sid(sddl_s)), sddl_s)
            self.assertEqual(sddl2sid(sid2sddl(sid_b)), sid_b)


class Test002ObjectGUID(unittest.TestCase):
    """
    test whether uuid.UUID(bytes_le=...) generates the same UUID string
    representations like displayed by ADSI-Edit
    """

    test_vectors = (
        (
            unhexlify('17:98:44:30:D2:D6:FA:4D:98:34:C6:E4:11:A2:83:FC'.replace(':', '')),
            '30449817-d6d2-4dfa-9834-c6e411a283fc',
        ),
        (
            unhexlify('F8:5F:48:1B:41:A8:77:47:85:3C:9A:63:58:71:1B:6A'.replace(':', '')),
            '1b485ff8-a841-4777-853c-9a6358711b6a',
        ),
    )

    def test001(self):
        for id_b, uuid_s in self.test_vectors:
            self.assertEqual(str(uuid.UUID(bytes_le=id_b)), uuid_s)


if __name__ == '__main__':
    unittest.main()
