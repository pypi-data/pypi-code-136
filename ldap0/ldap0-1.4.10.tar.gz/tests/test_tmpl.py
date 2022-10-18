# -*- coding: ascii -*-
"""
Automatic tests for module ldap0.tmpl
"""

# from Python's standard lib
import unittest

from ldap0.tmpl import EscapeStrDict, TemplateEntry
import ldap0.dn


class TestEscapeStrDict(unittest.TestCase):
    """
    test ldap0.tmpl.EscapeStrDict
    """

    def test001_escape_dn(self):
        escaped_cn = ldap0.dn.escape_str('Foo=Bar')
        edct1 = EscapeStrDict(ldap0.dn.escape_str, cn='Foo=Bar', mail='theo@example.com')
        self.assertEqual(edct1['cn'], escaped_cn)
        self.assertEqual(edct1['mail'], 'theo@example.com')
        self.assertEqual(sorted(edct1.values()), [escaped_cn, 'theo@example.com'])
        self.assertEqual(sorted(edct1.items()), [('cn', escaped_cn), ('mail', 'theo@example.com')])
        edct2 = EscapeStrDict(ldap0.dn.escape_str, {'cn': 'Foo=Bar'})
        self.assertEqual(edct2['cn'], escaped_cn)
        edct3 = EscapeStrDict(ldap0.dn.escape_str, (('cn', 'Foo=Bar'),))
        self.assertEqual(edct3['cn'], escaped_cn)


class TestTemplateEntry(unittest.TestCase):
    """
    test ldap0.tmpl.TemplateEntry
    """

    def test001_inetorgperson_ascii(self):
        t_dn = 'cn={first_name} {last_name},ou=People,dc=example,dc=com'
        t_entry = {
            'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
            'cn': ['{first_name} {last_name}', '{last_name}, {first_name}'],
            'sn': ['{last_name}'],
            'mail': ['{mail_addr}'],
            'departmentNumber': ['{dept_num:08d}'],
        }
        inet_org_person = TemplateEntry(t_dn=t_dn, t_entry=t_entry)
        self.assertEqual(inet_org_person.t_dn, t_dn)
        self.assertEqual(inet_org_person.t_entry, t_entry)
        self.assertEqual(
            inet_org_person.ldap_entry({
                'first_name': 'Theo',
                'last_name': 'Tester',
                'mail_addr': 'theo.tester@example.com',
                'dept_num': 42,
            }),
            (
                'cn=Theo Tester,ou=People,dc=example,dc=com',
                {
                    'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    'cn': [b'Theo Tester', b'Tester, Theo'],
                    'sn': [b'Tester'],
                    'mail': [b'theo.tester@example.com'],
                    'departmentNumber': [b'00000042'],
                }
            )
        )
        # missing mail_addr
        self.assertEqual(
            inet_org_person.ldap_entry({
                'first_name': 'Theo',
                'last_name': 'T\xe4ster',
            }),
            (
                'cn=Theo T\xe4ster,ou=People,dc=example,dc=com',
                {
                    'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    'cn': [b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
                    'sn': [b'T\xc3\xa4ster'],
                }
            )
        )

    def test002_unicode(self):
        inet_org_person = TemplateEntry(
            t_dn = 'cn={first_name} {last_name},ou=People,dc=example,dc=com',
            t_entry = {
                'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                'cn': ['{first_name} {last_name}', '{last_name}, {first_name}'],
                'sn': ['{last_name}'],
                'mail': ['{mail_addr}'],
                'description': ['T\xe4stuser'],
            },
        )
        self.assertEqual(
            inet_org_person.ldap_entry({
                'first_name': 'Theo',
                'last_name': 'Tester',
                'mail_addr': 'theo.tester@example.com',
            }),
            (
                'cn=Theo Tester,ou=People,dc=example,dc=com',
                {
                    'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    'cn': [b'Theo Tester', b'Tester, Theo'],
                    'sn': [b'Tester'],
                    'mail': [b'theo.tester@example.com'],
                    'description': [b'T\xc3\xa4stuser'],
                }
            )
        )
        # missing mail_addr
        self.assertEqual(
            inet_org_person.ldap_entry({
                'first_name': 'Theo',
                'last_name': 'T\xe4ster',
            }),
            (
                'cn=Theo T\xe4ster,ou=People,dc=example,dc=com',
                {
                    'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    'cn': [b'Theo T\xc3\xa4ster', b'T\xc3\xa4ster, Theo'],
                    'sn': [b'T\xc3\xa4ster'],
                    'description': [b'T\xc3\xa4stuser'],
                }
            )
        )

    def test003_unicode_first_stop(self):
        inet_org_person = TemplateEntry(
            t_dn = 'cn={first_name} {last_name},ou=People,dc=example,dc=com',
            t_entry = {
                'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
                'cn': ['{first_name} {last_name}', '{last_name}, {first_name}'],
                'sn': ['{last_name}'],
                'mail': ['{mail_addr}'],
                'description': ['T\xe4stuser'],
                'departmentNumber': [
                    '{no1}',
                    '{dept_num:08d}',
                ],
                'displayName': [
                    '{no1}',
                    '{first_name} {last_name} ({dept_num:08d})',
                    '{no2}',
                ],
            },
        )
        self.assertEqual(
            inet_org_person.ldap_entry(
                {
                    'first_name': 'Theo',
                    'last_name': 'Tester',
                    'mail_addr': 'theo.tester@example.com',
                    'dept_num': 42,
                },
                first_stop_attrs=('departmentNumber', 'displayName'),
            ),
            (
                'cn=Theo Tester,ou=People,dc=example,dc=com',
                {
                    'objectClass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
                    'cn': [b'Theo Tester', b'Tester, Theo'],
                    'sn': [b'Tester'],
                    'displayName': [b'Theo Tester (00000042)'],
                    'mail': [b'theo.tester@example.com'],
                    'departmentNumber': [b'00000042'],
                    'description': [b'T\xc3\xa4stuser'],
                }
            )
        )

    def test004_escape_dn(self):
        self.assertEqual(
            TemplateEntry(
                t_dn = 'cn={foo},dc=example,dc=com',
                t_entry = {
                    'cn': ['{foo}'],
                }
            ).ldap_entry({'foo': 'Tester, Theo'}),
            (
                'cn=Tester\\, Theo,dc=example,dc=com',
                {'cn': [b'Tester, Theo']},
            ),
        )

    def test005_from_ldif_str(self):
        self.assertEqual(
            TemplateEntry.from_ldif_str((
                b'dn: cn={foo},dc=example,dc=com\n'
                b'cn: {foo}\n'
                b'\n'
            )).ldap_entry({'foo': 'Tester, Theo'}),
            (
                'cn=Tester\\, Theo,dc=example,dc=com',
                {'cn': [b'Tester, Theo']},
            ),
        )

if __name__ == '__main__':
    unittest.main()
