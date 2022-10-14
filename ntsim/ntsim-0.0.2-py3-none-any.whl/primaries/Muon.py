from ntsim.Primary import *
from ntsim.MuonSurface import *
class Muon(Primary):
    def configure(self,opts):
        if opts.primary_generator == 'CorsikaGVDDataBankReader':
            self.primary_generator = CorsikaGVDDataBankReader(opts)
        self.configure_propagator(opts)

    def configure_propagator(self,opts):
        for m in opts.primary_propagator:
            if m == 'pymum' or m == 'proposal':
                self.primary_propagator['muonPropagator'] = muonPropagator(m)

    def next(self):
        primaries = self.primary_generator.next()
        #log.debug(primaries)

        #Calculate the surface for muons entering water based on first muon theta (they go in parallell anyway)
        ms = MuonSurface(self.geometry)
        if primaries is None:
            log.warning("No primaries to propagate")
            return
        oldx_first = 0
        oldy_first = 0
        shift_x = 0
        shift_y = 0
        for i,event in enumerate(primaries['event']):
            if i == 0:
                #calclate the surface only for first muon
                ms.calculateSurface(event['theta_mu'],event['energy_mu'])
                #Generate the entry point on the surface for first muon
                ms.generatePoint()
                #Caluculate shift for other muons in the bundle (based on their positions relative to the first one)
                shift_x = ms.x_firstMu - event['x_mu']
                shift_y = ms.y_firstMu - event['y_mu']
                #Update the event record for the first muon
                event['x_mu'] = ms.x_firstMu
                event['y_mu'] = ms.y_firstMu
            else:
                #If more muons in the bundle, shift the additional ones by the values calculated for the first one
                event['x_mu'] = event['x_mu'] + shift_x
                event['y_mu'] = event['y_mu'] + shift_y

        log.debug(primaries)

        self.primary_propagator['muonPropagator'].propagate(primaries)


    def next_multithread(self,n,jobs=0):
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        primaries_raw = self.primary_generator.next_record_bytes(n)
        t = ThreadPool(processes=jobs)
        primaries = t.map(self.primary_generator.parse_event_record, primaries_raw)
        t.close()
        self.primary_propagator['muonPropagator'].propagate_multithread(primaries)

    def get_photons_sampling_weight(self):
        return 1.

    def get_vertices(self):
        return []
