from ntsim.photonTransporters.mcPhotonTransport.ptMC_scattering_models import HenyeyGreenstein, Rayleigh, HGplusRayleigh

import logging
logger = logging.getLogger('Medium')

import configargparse
p = configargparse.get_argument_parser()
p.add_argument("--medium_scattering_model",default='HG',help="scattering model name: HG, Rayleigh, HG+Rayleigh")
p.add_argument("--medium_anisotropy",type=float,default=0.99,help="light scattering anisotropy")

class Medium():
    def __init__(self):
        self.model = None

    def configure(self,opts):
        self.scattering_model_name = opts.medium_scattering_model
        self.anisotropy            = opts.medium_anisotropy
        from bgvd_model.BaikalWater import BaikalWater # FIXME must go outside
        self.BaikalWaterProps = BaikalWater()
        self.models = {'HG':HenyeyGreenstein,'Rayleigh':Rayleigh,'HG+Rayleigh':HGplusRayleigh}
        logger.info('configured')
        return

    def get_model(self,photons):
        import numpy as np
        mu_sca = np.interp(photons.wavelength, self.BaikalWaterProps.wavelength, self.BaikalWaterProps.scattering_inv_length)
        mu_abs = np.interp(photons.wavelength, self.BaikalWaterProps.wavelength, self.BaikalWaterProps.absorption_inv_length)
        n_gr   = np.interp(photons.wavelength, self.BaikalWaterProps.wavelength, self.BaikalWaterProps.group_refraction_index)
        name = self.scattering_model_name
        if name in self.models:
            self.model = self.models[name](name=name,mua=mu_abs,mus=mu_sca,refractive_index=n_gr,g=self.anisotropy)
        else:
            log.error(f'unknown model name {name}')
        return self.model
