import abc
import numpy as np
import ntsim.utils.gen_utils as gen_utils

class RandomVectorBase(metaclass=abc.ABCMeta):
    def __init__(self):
        return

    @abc.abstractmethod
    def pdf(self,mu):
        """
        pdf
        """

    @abc.abstractmethod
    def random_mu(self,sample=1):
        """
        random mu
        """

    @abc.abstractmethod
    def cdf(self,mu):
        """
        cdf
        """

    def cdf_numeric(self,mu,n):
        x = np.linspace(-1,mu,n)
        y = self.pdf(x)
        step = (mu+1)/n
        return np.sum(y)*step

    def random_direction(self,v):
        # v = unit vector axis
        # returns random unit vector v1 with v*v1=t, where t is distributed according to random_mu distribution
        phi_r = 2*np.pi*np.random.uniform(0,1,v.shape[0])
        cosphi_r = np.cos(phi_r)
        sinphi_r = np.sin(phi_r)
        costheta_r = self.random_mu(sample=v.shape[0])
        sintheta_r = np.sqrt(1-costheta_r**2)

        v = gen_utils.unit_vector(v)
        costheta = v[:,2]
        sintheta = np.sqrt(1-costheta**2)
        phi = np.arctan2(v[:,1],v[:,0])
        cosphi = np.cos(phi)
        sinphi = np.sin(phi)
        v1_x = cosphi*(costheta*sintheta_r*cosphi_r+sintheta*costheta_r)-sinphi*sintheta_r*sinphi_r
        v1_y = sinphi*(costheta*sintheta_r*cosphi_r+sintheta*costheta_r)+cosphi*sintheta_r*sinphi_r
        v1_z = -sintheta*sintheta_r*cosphi_r+costheta*costheta_r
#        print(np.array([v1_x,v1_y,v1_z]).T)
        return np.array([v1_x,v1_y,v1_z]).T

    def plot_random_direction(self):
        import matplotlib as mpl
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        pos = [221, 222, 223, 224]
        v = np.array([[0,0,1], [0,1,1], [1,1,1], [1,0,1]])
        sample = 10000
        fig = plt.figure(figsize=plt.figaspect(0.5))

        plt.subplots_adjust(hspace=0.4)
        fig.suptitle('Validate rotations', fontsize=14)
        for i in range(4):
            #plt.subplot(pos[i],projection='3d')
            axis = v[i]
            x = np.zeros(sample,dtype=float)
            y = np.zeros(sample,dtype=float)
            z = np.zeros(sample,dtype=float)
            for s in range(sample):
                v1 = self.random_direction(axis.reshape(1,3))
                x[s] = v1[:,0]
                y[s] = v1[:,1]
                z[s] = v1[:,2]
            #print(x,y,z)
            ax = fig.add_subplot(2, 2, i+1, projection='3d')
            ax.scatter(x,y,z, s=0.05,marker='.')
        plt.show()
