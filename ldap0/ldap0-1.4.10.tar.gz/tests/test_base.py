# -*- coding: utf-8 -*-
"""
Automatic tests for module ldap0.base
"""

# from Python's standard lib
import unittest

from ldap0.base import decode_list, encode_list, decode_entry_dict, encode_entry_dict


class Test001Functions(unittest.TestCase):

    def test001_decode_list(self):
          self.assertEqual(
              decode_list(
                  [b'foo', b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
              ),
              ['foo', 'Theo Täster', 'Täster, Theo'],
          )

    def test002_decode_entry_dict(self):
          self.assertEqual(
              decode_entry_dict({
                    b'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    b'cn': [b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
                    b'sn': [b'T\xc3\xa4ster'],
                    b'inv\xc3\xa4lid': [],
              }),
              {
                    'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                    'cn': ['Theo Täster', 'Täster, Theo'],
                    'sn': ['Täster'],
                    'invälid': [],
              },
          )
          with self.assertRaises(UnicodeDecodeError):
              decode_entry_dict(
                  {
                        b'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                        b'cn': [b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
                        b'sn': [b'T\xc3\xa4ster'],
                        b'inv\xc3\xa4lid': [],
                  },
                  'ascii'
              )

    def test003_encode_list(self):
          self.assertEqual(
              encode_list(
                  ['foo', 'Theo Täster', 'Täster, Theo'],
              ),
              [b'foo', b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
          )

    def test004_encode_entry_dict(self):
          self.assertEqual(
              encode_entry_dict({
                    'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                    'cn': ['Theo Täster', 'Täster, Theo'],
                    'sn': ['Täster'],
                    'invälid': [],
              }),
              {
                    b'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    b'cn': [b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
                    b'sn': [b'T\xc3\xa4ster'],
                    b'inv\xc3\xa4lid': [],
              },
          )
          with self.assertRaises(UnicodeEncodeError):
              encode_entry_dict(
                  {
                        'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                        'cn': ['Theo Täster', 'Täster, Theo'],
                        'sn': ['Täster'],
                        'invälid': [],
                  },
                  'ascii'
              )


if __name__ == '__main__':
    unittest.main()
