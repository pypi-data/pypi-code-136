from ntsim.Primary import *
class LaserPrimary(Primary):
    import numpy as np

    def configure(self,opts):
        if opts.primary_generator == 'Laser':
            self.primary_generator = Laser()
            self.primary_generator.configure(opts)
            self.primary_name = 'Laser'
            track = np.array(self.primary_generator.position)
            self.primary_track = track.reshape(track.shape[0],1)
        log.info('configured')
        self.configure_propagator(opts)

    def configure_propagator(self,opts):
        for m in opts.primary_propagator:
            if m == 'mcPhotonTransporter':
                self.primary_propagator['mcPhotonTransporter'] = mcPhotonTransporter()
                self.primary_propagator['mcPhotonTransporter'].configure(opts)

    def next(self):
        primaries = self.primary_generator.next()
        self.make_event_folder(self.gEvent.gProductionHeader.n_events)
        bunch = 0
        n_photons_total = 0
        while True:
            try:
                photons = next(primaries)
                hits = self.primary_propagator['mcPhotonTransporter'].transport(photons,self.medium.get_model(photons),self.geometry)
                self.write_photons_bunch(photons,bunch)
#                print(photons.r,photons.dir)
                self.add_hits(hits)
                bunch+=1
                n_photons_total += photons.n_tracks
            except StopIteration:
                break
        self.write_number_of_bunches(bunch,n_photons_total)
        self.write_hits()
        self.clear_hits()
        self.write_event_header()

    def get_photons_sampling_weight(self):
        return 1.

    def get_vertices(self):
        return []
