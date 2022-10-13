"""
Definition of PDG data-specific classes.

All PDG data classes use lazy (on-demand) loading of data from the database.
"""

from sqlalchemy.sql import select
from pdg.errors import *
from pdg.utils import parse_id


class PdgData:
    """Base class for PDG data."""

    def __init__(self, api, pdgid):
        self.api = api
        self.pdgid = pdgid
        self.baseid, self.edition = parse_id(pdgid)
        self.cache = None

    def __str__(self):
        return 'Data for PDG Identifier %s: %s' % (self.pdgid, self.description())

    def _get_cache(self):
        if self.cache is None:
            try:
                cache = dict()
                pdgid_table = self.api.db.tables['pdgid']
                cache['pdgid'] = pdgid_table.select(pdgid_table.c.name == self.baseid).execute().fetchone()
                pdgdata_table = self.api.db.tables['pdgdata']
                q = pdgdata_table.select()
                q = q.where(pdgdata_table.c.pdgid_id == cache['pdgid'].id)
                q = q.where(pdgdata_table.c.edition == self.edition)
                r = q.execute().fetchall()
            except:
                raise PdgApiError('unable to retrieve data for %s', self.pdgid)
            # FIXME: handling of multi-data PDG Identifiers
            if len(r) == 0:
                cache['pdgdata'] = None
            elif len(r) == 1:
                cache['pdgdata'] = r[0]
            else:
                raise PdgApiError('multiple-value summary date not yet supported')
            self.cache = cache

    def _get_data(self, table, what):
        """Data access utility method."""
        self._get_cache()
        try:
            return self.cache[table][what]
        except:
            raise PdgNoDataError('no %s data for %s' % (what, self.pdgid))

    def description(self):
        """Return description of data."""
        return self._get_data('pdgid', 'description')

    def data_type(self):
        """Return type of data."""
        return self._get_data('pdgid', 'data_type')

    def value(self):
        """Get numerical central value."""
        return self._get_data('pdgdata', 'value')

    def value_type(self):
        """Get value type."""
        return self._get_data('pdgdata', 'value_type')

    def value_text(self):
        """Get value and uncertainty in plain text format."""
        return self._get_data('pdgdata', 'value_text')

    def error_positive(self):
        """Get numerical value of positive uncertainty."""
        return self._get_data('pdgdata', 'error_positive')

    def error_negative(self):
        """Get numerical value of negative uncertainty."""
        return self._get_data('pdgdata', 'error_negative')

    def is_limit(self):
        """Return True if value is a limit."""
        return self._get_data('pdgdata', 'confidence_level') is not None

    def confidence_level(self):
        """Return confidence level for limits, None otherwise."""
        return self._get_data('pdgdata', 'confidence_level')

    def unit_power_of_ten(self):
        """Return unit multiplier as power of then the value is to be scaled with."""
        return self._get_data('pdgdata', 'unit_power_of_ten')

    def unit_text(self):
        """Return the unit in text form (without the power of ten scale factor)."""
        return self._get_data('pdgdata', 'unit_text')

    def unit_is_percent(self):
        """True if value should be rendered in percent."""
        return self._get_data('pdgdata', 'unit_is_percent')


class PdgParticleMass(PdgData):
    pass

class PdgBranchingFraction(PdgData):
    pass
