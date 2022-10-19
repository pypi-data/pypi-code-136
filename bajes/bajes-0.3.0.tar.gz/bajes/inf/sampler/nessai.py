from __future__ import division, unicode_literals, absolute_import
import numpy as np
import os

import logging
logger = logging.getLogger(__name__)

from nessai.flowsampler import FlowSampler
from nessai.model import Model

from . import SamplerBody

class NessaiModel(Model):
    """
        Wrapper model object for nessai
    """

    def __init__(self, posterior):

        self.like   = posterior.like
        self.prior  = posterior.prior
        self.names  = self.prior.names
        self.bounds = {ni: bi for ni,bi in zip(self.prior.names, self.prior.bounds)}

    def log_likelihood(self,x):
        p = self.prior.this_sample({n : x[n] for n in self.prior.names})
        return self.like.log_like(p)

    def log_prior(self,x):
        if self.prior.in_bounds(x):
            return self.prior.log_prior(x)
        else:
            return -np.inf

class SamplerNessai(SamplerBody):

    def __initialize__(self, posterior,
                       nlive,
                       tolerance=0.1,
                       max_epochs=50, patience=10,
                       n_blocks=2, n_neurons=4, n_layers=1,
                       batch_norm_between_layers=True, device_tag='cpu',
                       pool=None, **kwargs):

        if nlive < len(posterior.prior.names)*(len(posterior.prior.names)-1)//2:
            logger.warning("Given number of live points < Ndim*(Ndim-1)/2. This may generate problems in the exploration of the parameters space.")

        # set flow arguments
        flow_config = { 'max_epochs':   max_epochs,
                        'patience':     patience,
                        'max_epochs':   max_epochs,
                        'model_config': {   'n_blocks':     n_blocks,
                                            'n_neurons':    n_neurons,
                                            'n_layers':     n_layers,
                                            'device_tag':   device_tag,
                                            'kwargs':       {'batch_norm_between_layers':batch_norm_between_layers}
                                        }
                      }

        # check resume
        if self.store_flag:
            resume = True
        else:
            resume = False

        # initialize model
        _model = NessaiModel(posterior)

        # set sampler arguments
        sampler_kwargs  = { 'output':           self.outdir+'/nessai',
                            'flow_config':      flow_config,
                            'nlive':            nlive,
                            'stopping':         tolerance,
                            'seed':             self.seed,
                            'prior_sampling':   True,
                            'resume':           resume}

        logger.info("Initializing nested sampler ...")
        self.sampler =  FlowSampler(_model, **sampler_kwargs)
