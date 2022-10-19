import numpy as np
import scipy 

class Perlin:
    def __init__(self, seed=-1): # Initialize a PRNG (Linear Congruential Generator)
        self.M = 4294967296
        self.A = 1664525         
        self.C = 1
        if(seed == -1):
            self.Z = np.floor(np.random.random() * self.M)
        else:
            self.Z = seed
    
    def __rand(self):
        self.Z = (self.A*self.Z+self.C) % self.M
        return self.Z/self.M
    
    def __interpolate(self,pa,pb,px): # cosine interpolation
        ft =  px * np.pi
        f = (1-np.cos(ft))*0.5
        return pa * (1-f) + pb*f
    
    def __generate(self, numValues=1000, min=0, max=30, wavelength=100,firstValue=-1):
        if firstValue ==-1:
            a = self.__rand() * (max-min) + min
            b = self.__rand() * (max-min) + min
        else:
            a = firstValue
            b = firstValue

        currentValue = 0
        values=[]
        for i in range(numValues):
            if i % wavelength == 0:
                a = b
                b = self.__rand() * (max-min) + min
                currentValue = a
            else:
                currentValue = self.__interpolate(a, b, (i % wavelength) / wavelength)
            values.append(currentValue)
        return values

    @staticmethod
    def Generate(numValues=1000, min=0, max=30, wavelength=100, firstValue=-1, seed=-1):
        p = Perlin(seed)
        return p.__generate(numValues, min, max, wavelength, firstValue)

class DanMaPerlin:
    def generate(self, numValues=1000, MinV=0, MaxV=30, numOctaves=4, persistance=2):
        ns=numOctaves
        p=persistance
        total = np.zeros((ns, numValues))
        for s in range(ns):
            frequency = pow(2, ns-s)
            amplitude = pow(p,s)
            X = np.arange(1, (numValues+200), frequency)
            spline = scipy.interpolate.splrep(X, np.random.rand(len(X)))
            nv = scipy.interpolate.splev(range(numValues+200), spline) * amplitude
            nv[nv<0] = 0
            total[s,:] = nv[100:-100]
        stotal = np.sum(total,0)
        stotal = stotal-np.min(stotal)
        vector = np.divide(stotal,max(stotal)) * (MaxV-MinV) + MinV
        return vector
