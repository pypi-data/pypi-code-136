import numpy as np
import ntsim.utils.systemofunits as units
from time import time
import abc
from ntsim.photonTransporters.mcPhotonTransport.RandomVectorBase import RandomVectorBase

class ScatteringModel(RandomVectorBase):
    def __init__(self, name, mua, mus, refractive_index, g):
        self.name = name
        self.mua = mua
        self.mus = mus
        self.n   = refractive_index
        self.g   = g
        self.light_velocity_medium = units.light_velocity_vacuum/self.n
        self.ta  = 1/(self.mua*self.light_velocity_medium)
        self.ts  = 1/(self.mus*self.light_velocity_medium)
        self.t_tot = 1/( (mua+mus)*self.light_velocity_medium )
        return


class HenyeyGreenstein(ScatteringModel):

    def plot_pdf(self):
        import scipy.integrate as integrate
        g = [0.99,0.9,0.5,0.0]
        pos = [221, 222, 223, 224]
        for ig in g:
            self.g = ig
            result = integrate.quad(lambda x: self.pdf(x), -1, 1)
            print("g={0:>5}, integral: {1}".format(ig, result))


        import matplotlib.pyplot as plt
        mu  = np.linspace(-1,1,10000)
        fig = plt.figure(figsize=(12, 8))
        plt.subplots_adjust(hspace=0.4)
        fig.suptitle(self.name+' angular distribution', fontsize=14)
        for i in range(4):
            ax = plt.subplot(pos[i])
            self.g = g[i]
            plt.plot(mu,self.pdf(mu),label='pdf')
            plt.plot(mu,self.cdf(mu),label='cdf'.format(g[i]))
            mu_random = self.random_mu(sample=100000)
            plt.hist(mu_random, bins=2000, density=True)
            axes = plt.gca()
            #axes.set_xlim([0.85,1])
            plt.legend(loc='best')
            plt.grid(True)
            plt.gca().set_xlabel(r'$\cos\;\theta$')
            #plt.gca().set_ylabel(r'PDF')
            plt.yscale('log')
            ax.title.set_text('g={0:>5}'.format(g[i]))
        plt.savefig('plots/'+'pdf_HenyeyGreenstein.pdf')

    def pdf(self,mu):
        g = self.g
        return 0.5*(1-g**2)*np.power(1+g**2-2*g*mu,-1.5)

    def cdf(self,mu):
        g = self.g
        g2 = np.power(g,2)
        gmu = g*mu
        f1 = 1/np.sqrt(1+g2-2*gmu)
        f2 = 1/(1+g)
        cdf = 0.5*(1-g2)*(f1-f2)
        return cdf

    def random_mu(self,sample=1):
        g = self.g
        s = np.random.uniform(-1,1,sample) # -1,1 is crucial! (DN)

        if (g != 0.0):
            x = np.power((1-g**2)/(1+g*s),2)
            return 0.5/g*(1+g**2-x)
        else:
            return s



class Rayleigh(ScatteringModel):
    def plot_pdf(self):
        import scipy.integrate as integrate
        result = integrate.quad(lambda x: self.pdf(x), -1, 1)
        print("\t integral:{}".format(result))

        import matplotlib.pyplot as plt
        mu  = np.linspace(-1,1,1000)
        fig = plt.figure(figsize=(12, 8))
        plt.plot(mu,self.pdf(mu),label='pdf')
        plt.plot(mu,self.cdf(mu),label='cdf')

        tic = time()
        mu_random = self.random_mu(sample=100000)
        toc = time()
        print(f"\t random analytic: {toc-tic} seconds")
        tic = time()
        mu_random_numeric = self.random_mu_numeric(sample=100000)
        toc = time()
        print(f"\t random numeric: {toc-tic} seconds")
        plt.hist(mu_random, bins=2000, density=True)
        plt.hist(mu_random_numeric, bins=2000, density=True)

        axes = plt.gca()
        axes.set_xlim([-1.,1])
        plt.grid(True)
        plt.xlabel(r'$\cos\;\theta$')
        plt.ylabel(r'PDF')
        plt.yscale('log')
        plt.savefig('plots/'+'pdf_Rayleigh.pdf')

    def pdf(self, mu):
        return 3./8.*(1 + mu**2)

    def cdf(self,mu):
        return 0.5+1/8*mu*(3+mu*mu)

    def random_mu(self,sample):
        r = np.random.uniform(0,1,sample)
        z = 2*(2*r-1)
        dz = np.sqrt(np.power(z,2)+1)
        z1 = z+dz
        z2 = z-dz
        B_sign = np.sign(z2)
        A = (z+dz)**(float(1)/3)
        B = np.abs(z-dz)**(float(1)/3)
        mu = A+B*B_sign
        return mu

    def random_mu_numeric(self, sample=1):
        # F(mu) = (mu^3 + 3*mu + 4) / 8
        CDF = 1./8.*np.poly1d([1.,0.,3.,4.])
        costh = np.linspace(-1,1,1000)
        import matplotlib.pyplot as plt
        if sample != 1:
            res = []
            for s in np.random.uniform(0,1,sample):
                poly_roots = (CDF-s).roots
                real_root = poly_roots[poly_roots.imag==0].real[0]
                res.append(real_root)
            return np.array(res)
        else:
            s = np.random.uniform(0,1)
            poly_roots = (CDF-s).roots
            real_root = poly_roots[poly_roots.imag==0].real[0]
            return real_root



class HGplusRayleigh(ScatteringModel):

    def __init__(self, rl_fraction=0.01, *args, **kwargs):
        super(HGplusRayleigh, self).__init__(*args, **kwargs)
        self.hg_fraction = 1. - rl_fraction
        self.rl_fraction = rl_fraction
        self.hg_model = HenyeyGreenstein(*args, **kwargs)
        self.rl_model = Rayleigh(*args, **kwargs)

    def plot_pdf(self):
        import scipy.integrate as integrate
        result = integrate.quad(lambda x: self.pdf(x), -1, 1)
        print("\t integral:{}".format(result))

        import matplotlib.pyplot as plt
        mu  = np.linspace(-1,1,1000)
        fig = plt.figure(figsize=(12, 8))
        plt.plot(mu,self.pdf(mu),label='pdf')
        plt.plot(mu,self.cdf(mu),label='cdf')

        mu_random = self.random_mu(sample=100000)
        plt.hist(mu_random, bins=2000, density=True)

        axes = plt.gca()
        axes.set_xlim([-1.,1])
        plt.grid(True)
        plt.title(f"Rayleigh: {self.rl_fraction*100:.0f}%, Henyey-Greenstein: {self.hg_fraction*100:.0f}%")
        plt.xlabel(r'$\cos\;\theta$')
        plt.ylabel(r'PDF')
        plt.yscale('log')
        plt.savefig('plots/'+'pdf_HGplusRayleigh.pdf')

    def pdf(self, mu):
        g = self.g
        return self.hg_fraction*self.hg_model.pdf(mu) + self.rl_fraction*self.rl_model.pdf(mu)

    def cdf(self, mu):
        g = self.g
        return self.hg_fraction*self.hg_model.cdf(mu) + self.rl_fraction*self.rl_model.cdf(mu)

    def random_mu(self, sample=1):
        if sample != 1:
            rnd_nb = np.random.uniform(0,1,sample)
            s_hg = self.hg_model.random_mu(len(rnd_nb[rnd_nb <  self.hg_fraction]))
            s_rl = self.rl_model.random_mu(len(rnd_nb[rnd_nb >= self.hg_fraction]))
            s_tot = np.concatenate((s_hg,s_rl))
            np.random.shuffle(s_tot)
            return s_tot
        else:
            if np.random.uniform(0,1) < self.hg_fraction:
                return self.hg_model.random_mu()
            else:
                return self.rl_model.random_mu()

class FlatScatteringModel(ScatteringModel):
    def plot_pdf(self):
        import scipy.integrate as integrate
        result = integrate.quad(lambda x: self.pdf(x), -1, 1)
        print("\t integral:{}".format(result))

        import matplotlib.pyplot as plt
        mu  = np.linspace(-1,1,1000)
        fig = plt.figure(figsize=(12, 8))
        plt.plot(mu,self.pdf(mu),label='pdf')
        plt.plot(mu,self.cdf(mu),label='cdf')

        mu_random = self.random_mu(sample=100000)
        plt.hist(mu_random, bins=2000, density=True)

        axes = plt.gca()
        axes.set_xlim([-1.,1])
        plt.grid(True)
        plt.title(f"Flat distribution of scattering angles")
        plt.xlabel(r'$\cos\;\theta$')
        plt.ylabel(r'PDF')
        #plt.yscale('log')
        plt.savefig('plots/'+'pdf_FlatScattering.pdf')

    def pdf(self, mu):
        if type(mu) == float:
            return 0.5
        else:
            return np.ones(mu.shape)/2.

    def cdf(self, mu):
        return 0.5*(1.+mu)

    def random_mu(self, sample=1):
        return np.random.uniform(-1,1,sample)


def main():
    print("  Flat Scattering Model")
    fl = FlatScatteringModel(name='FlatModel"', mua=1./(20*units.m), mus=1./(40*units.m), refractive_index=1.35)
    fl.plot_pdf()

    print("  Henyey-Greenstein:")
    hg = HenyeyGreenstein(name='Henyey-Greenstein',mua=1./(20*units.m),mus=1./(40*units.m),refractive_index=1.35,g=0.9)
    hg.plot_pdf()
    #hg.plot_random_direction()

    print("  Rayleigh:")
    rg = Rayleigh(name='Rayleigh',mua=1./(20*units.m),mus=1./(40*units.m),refractive_index=1.35,g=0.9)
    rg.plot_pdf()

    print("  Henyey-Greenstein plus Rayleigh")
    hg_rl = HGplusRayleigh(name="HG+Rayleigh", rl_fraction=0.05, mua=1./(20*units.m), mus=1./(40*units.m), refractive_index=1.35, g=0.9)
    hg_rl.plot_pdf()



if __name__ == "__main__":
    main()
