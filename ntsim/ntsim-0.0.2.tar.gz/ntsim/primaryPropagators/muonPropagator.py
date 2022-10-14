import logging
log = logging.getLogger('muonPropagator')
class muonPropagator():
    def __init__(self,name):
        self.propagator = None
        self.propagate = None
        if name == 'pymum':
            from mum import mum
            self.propagator = mum()
            self.propagator.init() # TODO Check if propagator is initialized
            self.propagate = self.propagate_by_mum
            self.propagate_multithread = self.propagate_by_mum_multithread
        elif name == 'proposal':
            log.debug('proposal to be added yet')
        else:
            log.error(f'unknown muon propagator {name}')

    def propagate_by_mum(self,primaries):
        depth = 1e5 # FIXME should be till the muon surface (in cm)
        if primaries is None:
            log.warning("No primaries to propagate")
            return
        for i,event in enumerate(primaries['event']):
            e_ini = event['energy_mu']
            track = self.propagator.transport(e_ini,depth)
            e_fin = track[-1]['energy_out']
            log.debug(f'transport {e_ini} -> {e_fin}')

    def propagate_by_mum_multithread(self,primaries,jobs=0):
        from multiprocessing.pool import ThreadPool
        from multiprocessing import cpu_count
        if jobs == 0:
            jobs = cpu_count()
        if primaries is None:
            log.warning("No primaries to propagate")
            return
        t = ThreadPool(processes=jobs)
        log.debug("Propagate by mum multithread start")
        t.map(self.propagate_by_mum, primaries)
        t.close()
        log.debug("Propagate by mum multithread done")


    def propagate_by_proposal(self,primaries):
        pass
