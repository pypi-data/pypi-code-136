from neutrinotelescopesimulation.photonTransporters.mcPhotonTransport.utils import ray_tracing_gvd, detector_hits

import logging
log = logging.getLogger('mcPhotonTransporter')
import numpy as np

class mcPhotonTransporter():
    def __init__(self):
        self.module_type = 'generator'

    def configure(self,opts):
        log.info('configured')

    def transport(self,photons,model,geometry, n_steps=5):
        photons.n_steps = n_steps
        n_photons = photons.r.shape[1]
        photons.r = np.concatenate((photons.r, np.zeros((n_steps-1, n_photons, 3))), axis=0)
        photons.dir = np.concatenate((photons.dir, np.zeros((n_steps-1, n_photons, 3))), axis=0)
        photons.t = np.concatenate((photons.t, np.zeros((n_steps-1, n_photons))), axis=0)
        self.random_trajectories(photons,model)
        det_hits = self.ray_tracing(photons,geometry,model)
        #log.debug(f"{[(uid, len(hits)) for uid, hits in det_hits.items()]}")
        return det_hits


    def random_trajectories(self,photons,model):
        for step in range(1,photons.n_steps):
            photons.r[step], t_step = self.random_trajectory_step(photons.r[step-1], photons.dir[step-1],model)
            photons.t[step] = photons.t[step-1]+t_step
            photons.dir[step] = model.random_direction(photons.dir[step-1])
#            import IPython; IPython.embed(colors='neutral')
            photons.add_absorption_time(model.ta)
            photons.add_scattering_time(model.ts)
#            print(photons.r[step],photons.dir[step],photons.dir[step-1])

    def random_trajectory_step(self,r0,omega0,model):
        # make a random trajectory step starting from r0 in direction omega0
        # step length is random according to exp(-t/ts)
        # random time
        t = np.random.exponential(scale=model.ts)
        # make step in space
        dr = omega0*t[:,None]*model.light_velocity_medium[:,None]
        r = r0 + dr
#        print(dr,omega0,t)
        return r,t

    def ray_tracing(self,photons,geometry,model):
        # find intersections of photon tracks with OM spheres
        hits      = ray_tracing_gvd(photons.r,photons.t,
                                    geometry.geom, geometry.bounding_box_cluster,
                                    geometry.bounding_box_strings)
        # calculate expected signal in OMs (using numba)
        det_hits = detector_hits(photons.r,photons.t, geometry.det_normals,
                             hits, model.ta,photons.wavelength)
        return det_hits

# pandas version (hard to add to an open h5File):
#        hits_df = pd.DataFrame(det_hits,
#                               columns=['uid', 'time_ns',
#                                        'w_noabs', 'w_pde', 'w_gel', 'w_angular',
#                                        'x_hit', 'y_hit', 'z_hit',
#                                        'outside_mask', 'trk', 'step_number', 'cluster'])
#        return hits_df
