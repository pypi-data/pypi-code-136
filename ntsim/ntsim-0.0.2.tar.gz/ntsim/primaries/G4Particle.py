from ntsim.Primary import *

import time as system_time

class G4Particle(Primary):
    def __init__(self):
        super().__init__()
        self.vertices = []
        self.log = logging.getLogger('G4ParticlePrimary')
        self.primary_propagator = {}

    def configure(self, opts):
        # it will generate primaries and propagate them in the same module
        self.configure_propagator(opts)
        self.log.info('configured')

    def configure_propagator(self, opts):
        for m in opts.primary_propagator:
            if m == 'pyLiGen':
                self.primary_propagator['pyLiGen'] = pyLiGen(m)
                self.primary_propagator['pyLiGen'].configure(opts)
            if m == 'pyCaGen':
                pass
#                self.primary_propagator['pyCaGen'] = pyCaGen(m)
            if m == 'pyCaPar':
                pass
#                self.primary_propagator['pyCaPar'] = pyCaPar(m)
            if m == 'mcPhotonTransporter':
                self.primary_propagator['mcPhotonTransporter'] = mcPhotonTransporter()
            if m == 'NN':
                pass
#                self.primary_propagator['NN'] = NN(m)

    def next(self, thread_id=0):
        time0 = system_time.time()
        photons = None
        self.make_event_folder(self.gEvent.gProductionHeader.n_events)
        if 'pyLiGen' in self.primary_propagator.keys():
            self.vertices, photons, self.tracks = self.primary_propagator['pyLiGen'].propagate()
            self.write_tracks()
            #bunch_id = 0
            #self.write_photons_bunch(photons, bunch_id)
            #self.write_number_of_bunches(bunch_id+1, photons.n_tracks)
            log.info(f"{len(self.tracks)} tracks simulated")
            log.info(f"{photons.n_tracks} photons produced")
        if 'mcPhotonTransporter' in self.primary_propagator.keys():
            self.clear_hits()
            light_propagator = self.primary_propagator['mcPhotonTransporter']
            self.hits = light_propagator.transport(photons,
                                                   self.medium.get_model(photons),
                                                   self.geometry)
            #bunch_id = 0
            #self.write_photons_bunch(photons, bunch_id)
            #self.write_number_of_bunches(bunch_id+1, photons.n_tracks)
            self.write_hits()
            log.info(f"{len(np.unique(self.hits[:,0]))} OMs fired")
            log.info(f"{self.hits.shape[0]} hits detected")
        if 'NN' in self.primary_propagator.keys():
            self.hits = self.primary_propagator['NN'].propagate(self.vertices)
            log.info("Hits produced")
        #
        if photons != None:
            bunch_id = 0
            self.write_photons_bunch(photons, bunch_id)
            self.write_number_of_bunches(bunch_id+1, photons.n_tracks)
        '''
        hd = HitDrawer()
        if self.vertices: hd.AddVertices(self.vertices)
        if photons:       hd.AddPhotons(photons, suppression_factor=100)
        if self.hits:     hd.AddHits(selfhits)
        hd.Show()
        '''
        #
        self.write_event_header()
        log.info(f"All propagated in {(system_time.time() - time0):.2f} seconds")

    def next_multithread(self, n, jobs=0):
#        self.next()
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        t = ThreadPool(processes=jobs)
        t.map(self.next, range(1,n))
        t.close()

    def get_photons_sampling_weight(self):
        return self.primary_propagator['pyLiGen'].ph_fraction

    def get_vertices(self):  #FIXME: do we need vertices?
        return self.vertices
