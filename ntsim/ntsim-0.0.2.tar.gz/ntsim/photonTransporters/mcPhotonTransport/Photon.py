import click
from ntsim.utils.gen_utils import searchsorted2d
from ntsim.photonTransporters.mcPhotonTransport.utils import position_numba
import numpy as np

import logging
logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO)

class Photon():
    def __init__(self):
        self.n_tracks = 0
        return

    def init(self,n_tracks,n_steps,r,t,dir,wavelength,ta=[],ts=[]):
        self.n_tracks = n_tracks
        self.n_steps  = n_steps
        self.r        = r
        self.t        = t
        self.dir      = dir
        self.wavelength = wavelength
        if len(ta):
            self.ta = ta
        else:
            self.ta       = np.zeros_like(self.wavelength)
        if len(ts):
            self.ts = ts
        else:
            self.ts       = np.zeros_like(self.wavelength)
        self.print_info()
        self.print_memory()

    def print_memory(self):
        data_memory = ( self.r.nbytes+self.t.nbytes+self.dir.nbytes
                       +self.wavelength.nbytes)/1e6
        logger.debug(f"\t - data structure occupies {data_memory} Mb in memory")
        logger.debug(f"\t - shape information:")
        logger.debug(f"\t - r.shape={self.r.shape}")
        logger.debug(f"\t - dir.shape={self.dir.shape}")
        logger.debug(f"\t - t.shape={self.t.shape}")
        logger.debug(f"\t - wavelength.shape={self.wavelength.shape}")

    def add_absorption_time(self,ta):
        self.ta = ta # filled later by ptMC.random_trajectories

    def add_scattering_time(self,ts):
        self.ts = ts # filled later by ptMC.random_trajectories

    def print_info(self):
        logger.debug(f"Photon: Created with {self.n_tracks} photons with {self.n_steps} steps")

    def interpolate(self,x, xp, fp):
        from numpy.core.multiarray import interp as compiled_interp
        result = np.concatenate([compiled_interp(x, xp[i], fp[i], left=np.nan, right=np.nan) for i in range(fp.shape[0])])
        result = np.reshape(result,(fp.shape[0],x.shape[0]))
        return result

    def position_numpy(self,t):
        X = self.r[:,:,0].T
        Y = self.r[:,:,1].T
        Z = self.r[:,:,2].T
        T = self.t.T
        x = self.interpolate(x=t,xp=T,fp=X)
        y = self.interpolate(x=t,xp=T,fp=Y)
        z = self.interpolate(x=t,xp=T,fp=Z)
        return x,y,z

    def position(self,t):
        return position_numba(self.r,self.t,t)

    def direction(self,t):
        indices = np.apply_along_axis(np.searchsorted,axis=0,arr=self.t,v=t,side='left') -1
        mask_beg = (indices != -1)
        mask_end = (indices < self.t.shape[0])
        indices[~mask_beg] = 0                   # assign allowed values. Filter later
        indices[~mask_end] = self.t.shape[0]-1   # assign allowed values. Filter later
        dir_x = np.take_along_axis(self.dir[:,:,0],indices,axis=0).T
        dir_y = np.take_along_axis(self.dir[:,:,1],indices,axis=0).T
        dir_z = np.take_along_axis(self.dir[:,:,2],indices,axis=0).T

        return dir_x,dir_y,dir_z



    def dump(self):
        for step in np.arange(self.n_steps):
            print(f" step {step} pos=")
            print(f"{self.r[step,0:1,:],self.dir[step,0:1]}")

    def add_photons(self,photons):
        if not self.n_tracks:
            return photons
        # if object exists, let us update it adding new photons
        # check if the number of steps is the same
        assert self.n_steps == photons.n_steps, 'Can not merge Photon objects with different number of steps'
        new_photons = Photon()
        n_tracks   = self.n_tracks+photons.n_tracks
        n_steps    = self.n_steps
        r          = np.concatenate((self.r,photons.r),axis=1)
        t          = np.concatenate((self.t,photons.t),axis=1)
        dir        = np.concatenate((self.dir,photons.dir),axis=1)
        wavelength = np.concatenate((self.wavelength,photons.wavelength),axis=0)
        ta = np.concatenate((self.ta,photons.ta),axis=0)
        ts = np.concatenate((self.ts,photons.ts),axis=0)
        new_photons.init(n_tracks,n_steps,r,t,dir,wavelength,ta,ts)
        return new_photons
