from ntsim.photonTransporters.mcPhotonTransport.RandomVectorBase import RandomVectorBase
import numpy as np

class DiffuserExponential(RandomVectorBase):
    def __init__(self,sigma=1):
        self.sigma = sigma
        print('create DiffuserExponential')

    def diff(self,mu):
        return np.exp(mu/self.sigma) - np.exp(-1/self.sigma)

    def pdf(self,mu):
        return np.exp(mu/self.sigma)/(self.diff(1.)*self.sigma)

    def random_mu(self,sample=1):
        p = np.random.uniform(0.,1.,sample)
        return self.sigma*np.log(np.exp(-1/self.sigma) + p*(self.diff(1.)))

    def cdf(self,mu):
        return self.diff(mu)/self.diff(1.)

class DiffuserCone(RandomVectorBase):
    def __init__(self,cone_angle=30.):
        self.cone_angle = cone_angle
        print('create DiffuserCone')


    def pdf(self,mu):
        return 0.

    def random_mu(self,sample=1):
        p = np.random.uniform(0.,1.,sample)
        return np.cos(np.deg2rad(self.cone_angle))

    def cdf(self,mu):
        return 0.
