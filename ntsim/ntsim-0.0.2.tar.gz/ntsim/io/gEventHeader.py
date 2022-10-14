import logging
logger = logging.getLogger('gEventHeader')

class gEventHeader:
    def __init__(self):
        self.photons_sampling_weight = 1      # statistical weight of photons
        self.om_area_weight          = 1      # weight accounts for a larger area of optical module = np.power(true_radius/radius,2)
        self.vertices                = 0

    def clean(self):
        del self.vertices
        self.vertices = 0

    def add_vertices(self,v):
        self.vertices = v

    def get_vertices(self):
        return self.vertices

    def set_photons_sampling_weight(self,w):
        self.photons_sampling_weight = w

    def get_photons_sampling_weight(self):
        return self.photons_sampling_weight

    def set_om_area_weight(self,w):
        self.om_area_weight = w

    def get_om_area_weight(self):
        return self.om_area_weight

    def print(self):
        logger.info(f'om_area_weight={self.om_area_weight:6.3E}')
        logger.info(f'photons_sampling_weight={self.photons_sampling_weight:6.3E}')
        self.print_vertices()

    def print_vertices(self):
        if self.vertices:
            logger.info('particle vertices:')
            print(self.vertices)
            for iv, v in enumerate(self.vertices):
                pos = v[0]
                logger.info(f'vertex_id={iv}')
                logger.info(f'   o   (x,y,z,t)/m=({pos[0]:6.3E},{pos[1]:6.3E},{pos[2]:6.3E},{pos[3]:6.3E})')
                in_particles = v[1]
                for ip, p in enumerate(in_particles):
                    print(ip, p)
                    logger.info(f'-->o   particle_id={ip}, PDG = {p[0]}, (px,py,pz,E)/GeV = ({p[1]:6.3E},{p[2]:6.3E},{p[3]:6.3E},{p[4]:6.3E})')
                out_particles = v[2]
                for ip, p in enumerate(out_particles):
                    logger.info(f'   o-->particle_id={ip}, PDG = {p[0]}, (px,py,pz,E)/GeV = ({p[1]:6.3E},{p[2]:6.3E},{p[3]:6.3E},{p[4]:6.3E})')
