from ntsim.photonTransporters.mcPhotonTransport.Photon import Photon
from ntsim.primaryGenerators.Diffuser import DiffuserExponential,DiffuserCone
from ntsim.utils.gen_utils import generate_cherenkov_spectrum
import numpy as np

import configargparse
p = configargparse.get_argument_parser()
p.add_argument("--laser_waves",nargs='+',type=float,default=[350,600],help="wavelengths interval")
p.add_argument("--laser_n_photons",type=int,default=10000, help="number of photons to generate")
p.add_argument("--laser_n_bunches",type=int,default=1,help="number of bunches")
#p.add_argument("--laser_n_steps",type=int,default=5,help="number of steps")
p.add_argument("--laser_direction",nargs='+',type=float,default=[0.,0.,1.],help="unit three vector for photons direction")
p.add_argument("--laser_position",nargs='+',type=float,default=[0.,0.,0.],help="three vector for laser position")
p.add_argument("--laser_diffuser",nargs='+',default=('none',0),help="laser diffuser mode: (exp,sigma) or (cone, angle)")

import logging
log = logging.getLogger('Laser')

class Laser():
    def __init__(self):
        self.module_type = 'generator'
        self.diffuser = None

    def configure(self,opts):
        self.waves = opts.laser_waves
        self.n_bunches = opts.laser_n_bunches
        #self.steps = opts.laser_n_steps
        self.steps = 1
        self.n_photons = int(opts.laser_n_photons/opts.laser_n_bunches)
        self.direction = opts.laser_direction
        self.position = opts.laser_position
        if opts.laser_diffuser[0] == 'exp':
            self.diffuser = DiffuserExponential(float(opts.laser_diffuser[1]))
        elif opts.laser_diffuser[0] == 'cone':
            self.diffuser = DiffuserCone(float(opts.laser_diffuser[1]))
        self.photons = Photon()
        log.info('configured')
        return

    def get_direction(self):
        dir0 = np.array(self.direction,dtype=np.float64)
        if not self.diffuser:
            self.dir = np.tile(dir0,(self.steps,self.n_photons,1))
        else:
            dir = np.tile(dir0,(self.n_photons,1))
            dir = self.diffuser.random_direction(dir)
            dir = np.tile(dir,(self.steps))
            dir = np.reshape(dir,(self.n_photons,self.steps,3))
            dir = np.swapaxes(dir, 0, 1)
            self.dir = dir

    def make_photons(self):
        self.get_direction()
        self.r  = np.tile(np.array(self.position,dtype=np.float64), (self.steps,self.n_photons,1))
        self.t = np.tile(np.array([0.],dtype=np.float64),(self.steps,self.n_photons))
        if self.waves[0] == self.waves[1]:
            wavelengths = np.tile(np.array([self.waves[0]],dtype=np.float64),self.n_photons)
        else:
            wavelengths = generate_cherenkov_spectrum(self.waves[0],self.waves[1],self.n_photons)
        self.photons.init(self.n_photons,self.steps,self.r,self.t,self.dir,wavelengths)


    def next(self):
        for i in range(self.n_bunches):
            self.make_photons()
            yield self.photons
