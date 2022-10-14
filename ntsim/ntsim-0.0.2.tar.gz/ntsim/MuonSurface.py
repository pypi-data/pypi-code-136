import numpy as np
import logging
log = logging.getLogger('MuonSurface')



class MuonSurface():

    def __init__(self, geometry):

        self._min = 0
        self.R_max = 70
        self.H = 1360 # make configurable
        self.h = 750 # make configurable
#        self.L_max = 1e6 # should be a function of muon energy
        self.theta_firstMu = 0.
        self.x_firstMu = 0.
        self.y_firstMu = 0.
        self.r_firstMu = 0.
        self.phi_firstMu = 0.
        self.maxDfromDet = 50. # make configurable
        self.geometry = geometry


    def L_max(self, muonEnergy):
        #to be implemented
        return 1e6

#    def shiftToFirstMu(self,x,y):
        
        



    def calculateSurface(self, theta, muonEnergy):
        log.debug("Calculating muon surface")
        theta = np.radians(theta)
        cos_theta = np.cos(theta)
        pr1 = self.H/np.tan(theta)
        pr2 = self.L_max(muonEnergy)*cos_theta
        self.R_max = self.geometry.gvd_radius + min(pr1,pr2)

        log.debug("GVD Radius: %f",self.geometry.gvd_radius)
        
        diff1 = (self.h - self.maxDfromDet) if (self.h - self.maxDfromDet) > 0 else 0
        self.R_min = diff1/np.tan(theta)
        
        if self.R_min > pr2: 
            log.warning("R_min exceeds maximum propagation distance, skipping...")
            return

        log.debug("R_min, R_max: %f, %f",self.R_min, self.R_max)

        

 
    def generatePoint(self):
        r = (np.random.uniform(self.R_max, self.R_min))
        #print("r =", (r))

        #Calculating random phi
        phi_1 = np.radians(0)
        phi_2 = np.radians(360)
        #print("phi from the range is : ", end="")
        phi = np.random.uniform(phi_1, phi_2)
        #print("phi =", (phi))

        circle_x = self.geometry.gvd_centre[0]
        circle_y = self.geometry.gvd_centre[1]
        #print(circle_x, circle_y)
        # calculating coordinates
        self.x_firstMu = r * np.cos(phi) + circle_x
        self.y_firstMu = r * np.sin(phi) + circle_y

        log.debug("Generated muon entry point: %f, %f",self.x_firstMu,self.y_firstMu)



    




