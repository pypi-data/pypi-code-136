import numpy as np
import logging
logger = logging.getLogger('gEvent')

class gEvent(object):
    def __init__(self):
        self.gEventHeader            = None
        self.gProductionHeader       = None
        self.gPrimaryHeader          = None
        self.photons                 = 0
        self.hits                    = {}     # uid -> list of photons hits with simulation weights

    def setEventHeader(self,evtHeader):
        self.gEventHeader = evtHeader

    def setProductionHeader(self,prodHeader):
        self.gProductionHeader = prodHeader

    def setPrimaryHeader(self,primHeader):
        self.gPrimaryHeader = primHeader
            
    def add_photons(self,photons):
        self.photons = photons

    def clean_event(self):
        self.hits.clear()
        del self.photons
        self.photons = 0
        self.gEventHeader.clean()

    def print_event(self,ev=0):
#        print(f'event {ev}')
        self.print_event_header()
        self.print_photons()
        self.print_hits()

    def print_event_header(self):
        self.gEventHeader.print()


    def print_photons(self):
        if self.photons:
            logger.info(f'photons: n_tracks={self.photons.n_tracks}, n_steps={self.photons.n_steps}')

    def print_hits(self):
        if self.hits:
            logger.info(f'number of hits: {len(self.hits)}')
#            for uid in self.hits_time:
#                n = len(self.hits_time[uid])
#                print(f'det_id={uid}:'.ljust(20)+f'{n} photons hits,'.rjust(20)+f'charge={np.sum(self.photoelectrons_npe[uid]):6.3E}'.rjust(20))
