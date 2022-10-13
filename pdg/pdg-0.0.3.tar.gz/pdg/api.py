"""
PDG API top-level class.
"""

import sqlalchemy
import pdg
from pdg.errors import *
from pdg.utils import base_id
from pdg.data import *
from pdg.particle import PdgParticle


# Map PDG data type codes to corresponding classes
DATA_TYPE_MAP = {
    'PART': PdgParticle,
    'M':  PdgParticleMass,
    'BF': PdgBranchingFraction,
    'BF1': PdgBranchingFraction,
    'BF2': PdgBranchingFraction,
    'BF3': PdgBranchingFraction,
    'BF4': PdgBranchingFraction,
    'BF5': PdgBranchingFraction,
    'BFI': PdgBranchingFraction,
    'BFI1': PdgBranchingFraction,
    'BFI2': PdgBranchingFraction,
    'BFI3': PdgBranchingFraction,
    'BFI4': PdgBranchingFraction,
    'BFI5': PdgBranchingFraction
}


class PdgApi:

    def __init__(self, database_url):
        self.database_url = database_url
        self.engine = sqlalchemy.create_engine(self.database_url)
        self.db = sqlalchemy.MetaData(self.engine)
        self.db.reflect()
        self.edition = self.info('edition')

    def __str__(self):
        # FIXME: confirm code license
        s = ['WARNING: THIS VERSION OF THE PDG PACKAGE IS UNDER DEVELOPMENT - DO NOT USE FOR PUBLICATIONS',
             '%s Review of Particle Physics, data release %s, API version %s' %
             (self.info('edition'), self.info('created'), pdg.__version__),
             '%s' % self.info('citation'),
             # '(C) %s, released under the MIT (code) and %s (data) licenses'
             '(C) %s, code license TBD, data released under %s'
             % (self.info('producer'), self.info('license'))]
        return '\n'.join(s)

    def info(self, key):
        """Return metadata info specified by key."""
        pdginfo_table = self.db.tables['pdginfo']
        return select([pdginfo_table.c.value], pdginfo_table.c.name == key).execute().scalar()

    def get(self, pdgid, data_type = None):
        """Return PDG data for given PDG Identifier."""
        if data_type is None:
            pdgid_table = self.db.tables['pdgid']
            baseid = base_id(pdgid)
            try:
                data_type = select([pdgid_table.c.data_type], pdgid_table.c.name == baseid).execute().fetchone()[0]
            except Exception:
                raise PdgApiError('PDG Identifier %s not found' % pdgid)
        try:
            cls = DATA_TYPE_MAP[data_type]
        except Exception:
            cls = PdgData
        return cls(self, pdgid)
