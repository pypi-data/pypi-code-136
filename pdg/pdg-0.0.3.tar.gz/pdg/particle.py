"""
Definition of particle container class.
"""

from pdg.errors import *
from pdg.data import PdgData, PdgBranchingFraction


class PdgParticle(PdgData):

    def _branching_fractions(self, data_type):
        """Return iterator over given type of branching fractions."""
        if data_type[0:2] != 'BF':
            raise PdgApiError('illegal branching fracation data type %s' % data_type)
        pdgid_table = self.api.db.tables['pdgid']
        pdgdata_table = self.api.db.tables['pdgdata']
        query = pdgid_table.join(pdgdata_table).select()
        query = query.where(pdgid_table.c.name.like('%s.%%' % self.baseid))
        query = query.where(pdgid_table.c.data_type == data_type)
        query = query.where(pdgdata_table.c.edition == self.edition)
        for bf in query.execute():
            if self.edition:
                pdgid = '%s/%s' % (bf.name, self.edition)
            else:
                pdgid = bf.name
            yield PdgBranchingFraction(self.api, pdgid)

    def exclusive_branching_fractions(self):
        """Return iterator over exclusive branching fractions."""
        return self._branching_fractions('BF')

    def inclusive_branching_fractions(self):
        """Return iterator over inclusive branching fractions."""
        return self._branching_fractions('BFI')

    def properties(self):
        """Return iterator over all properties."""
        pdgid_table = self.api.db.tables['pdgid']
        pdgdata_table = self.api.db.tables['pdgdata']
        query = pdgid_table.join(pdgdata_table).select()
        query = query.where(pdgid_table.c.name.like('%s%%' % self.baseid))
        query = query.where(pdgid_table.c.data_type.notlike('BF%'))
        query = query.where(pdgdata_table.c.edition == self.edition)
        seen = set()
        for p in query.execute():
            # Return only single copy of PDG Item, even if there are multiple values (e.g. S042M)
            # FIXME: select only distinct pdgid in above query while keeping data_type to avoid second query
            if p.name in seen:
                continue
            seen.add(p.name)
            if self.edition:
                pdgid = '%s/%s' % (p.name, self.edition)
            else:
                pdgid = p.name
            yield self.api.get(pdgid, p.data_type)
