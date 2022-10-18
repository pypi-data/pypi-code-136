# -*- coding: ascii -*-
"""
ldap0.tmpl - templating
"""

from typing import Optional, Tuple
from collections import UserDict
from io import BytesIO

from .typehints import EntryMixed, EntryStr
from .base import decode_entry_dict
from .dn import escape_str as escape_dn_str
from .ldif import LDIFParser


class EscapeStrDict(UserDict):
    """
    dict drop-in replacement which applies a function
    before returning a dict value
    """

    def __init__(self, func, *args, **kwargs):
        UserDict.__init__(self, *args, **kwargs)
        self._func = func

    def __getitem__(self, key) -> str:
        return self._func(str(UserDict.__getitem__(self, key)))


class TemplateEntry:
    """
    Base class typically not directly used
    """
    t_dn: Optional[str] = None
    t_entry: Optional[EntryStr] = None

    def __init__(self, t_dn: str, t_entry: EntryStr):
        self.t_dn = t_dn
        self.t_entry = t_entry

    @classmethod
    def from_ldif_file(cls, fileobj, encoding: str = 'utf-8'):
        """
        create instance by reading LDIF from file-like object
        """
        t_dn, t_entry = LDIFParser(fileobj).list_entry_records()[0]
        return cls(
            t_dn.decode(encoding),
            decode_entry_dict(t_entry, encoding=encoding),
        )

    @classmethod
    def from_ldif_str(cls, buf):
        return cls.from_ldif_file(BytesIO(buf))

    def ldap_entry(
            self,
            data_dict,
            encoding: str = 'utf-8',
            first_stop_attrs = None,
        ) -> Tuple[str, EntryMixed]:
        """
        returns 2-tuple (dn, entry) derived from
        string-keyed, single-valued :data_dict:
        """
        ldap_entry = {}
        first_stop_attrs = set(first_stop_attrs or [])
        for attr_type in self.t_entry:
            attr_values = []
            attr_value_set = set()
            for av_template in self.t_entry[attr_type]:
                try:
                    attr_value = av_template.format(**data_dict).encode(encoding)
                except KeyError:
                    continue
                if attr_value and attr_value not in attr_value_set:
                    attr_values.append(attr_value)
                    attr_value_set.add(attr_value)
                if attr_type in first_stop_attrs:
                    break
            if attr_values:
                ldap_entry[attr_type] = attr_values
        dn_data_dict = EscapeStrDict(escape_dn_str, data_dict)
        ldap_dn = self.t_dn.format(**dn_data_dict)
        return (ldap_dn, ldap_entry)
