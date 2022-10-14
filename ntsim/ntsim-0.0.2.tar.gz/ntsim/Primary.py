import abc
import configargparse
import pandas as pd
p = configargparse.get_argument_parser()
p.add_argument('--primary_name',help='primary particle name: numu, muon, g4particle, ...')
p.add_argument('--primary_generator',help='primary particle generator')
p.add_argument('--primary_propagator',nargs='+',help='simulation chain: primary --> photons')

import pkg_resources
available_packages = [pkg.key for pkg in pkg_resources.working_set]

from ntsim.primaryGenerators.CorsikaGVDDataBankReader import *
from ntsim.primaryGenerators.Laser import *
from ntsim.primaryPropagators.muonPropagator import *
from ntsim.photonTransporters.mcPhotonTransporter import *
if 'geant4-pybind' in available_packages:
  from ntsim.primaryPropagators.pyLiGen import *
else:
  log.warning("'geant4_pybind' is not installed; pyLiGen and other Geant4 pythonized packages are not available.")
from ntsim.HitDrawer import *
from ntsim.io.h5Writer import *
from ntsim.io.gEventHeader import gEventHeader

import logging
log = logging.getLogger('Primary')

class Primary(metaclass=abc.ABCMeta):
    def __init__(self):
        self.primary_generator = None
        self.primary_propagator = {}
        self.primary_name = ''
        self.primary_track = []
        self.medium   = None
        self.geometry = None
        self.writer   = None
        self.gEvent   = None
        self.hits = []
        self.tracks = []

    def init_h5Writer(self):
        self.writer = h5Writer()

    def make_event_folder(self,n):
        self.writer.make_event_folder(n)

    def write_photons_bunch(self,photons,bunch_id):
        self.writer.write_photons_bunch(photons,bunch_id)

    def write_event_header(self):
        eventHeader = gEventHeader()
        eventHeader.set_photons_sampling_weight(self.get_photons_sampling_weight())
        eventHeader.set_om_area_weight(self.get_om_area_weight())
        eventHeader.add_vertices(self.get_vertices())
        self.writer.write_event_header(eventHeader)

    @abc.abstractmethod
    def get_photons_sampling_weight(self):
        """
        Primary children must implement this method
        """

    def get_om_area_weight(self):
        return np.power(self.geometry.true_radius/self.geometry.prod_radius,2)

    @abc.abstractmethod
    def get_vertices(self):
        """
        Primary children must implement this method
        """

    def add_hits(self,hits):
        if len(self.hits) == 0:
            self.hits = hits
        else:
#            self.hits = pd.concat([self.hits, hits], ignore_index=True)
            self.hits = np.concatenate((self.hits, hits))


    def write_hits(self):
        self.writer.write_hits(self.hits)

    def write_tracks(self):
        self.writer.write_tracks(self.tracks)

    def write_number_of_bunches(self,bunch,n_photons_total):
        self.writer.write_number_of_bunches(bunch,n_photons_total)

    def clear_hits(self):
        self.hits = []

    def set_medium(self,medium):
        self.medium = medium

    def set_geometry(self,geometry):
        self.geometry = geometry

    def set_gEvent(self,event):
        self.gEvent = event

    @abc.abstractmethod
    def configure(self,opts):
        """
        config objects
        """

    @abc.abstractmethod
    def next(self):
        """
        next objects
        """

def getPrimary(name):
    if name == 'muon':
        from ntsim.primaries.Muon import Muon
        return Muon()
    elif name == 'neutrino':
        from ntsim.primaries.Neutrino import Neutrino
        return Neutrino()
    elif name == 'laser':
        from ntsim.primaries.LaserPrimary import LaserPrimary
        return LaserPrimary()
    elif name == 'g4particle':
        if 'geant4-pybind' in available_packages:
            from ntsim.primaries.G4Particle import G4Particle
            return G4Particle()
        else:
            log.error("'geant4_pybind' is not installed; primary 'g4particle' is not available.")
    else:
        log.error(f'Primary name {name} is unknown')
        return None
    log.info(f'created primary {name}')
