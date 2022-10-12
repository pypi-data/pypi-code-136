from aidev.utilities.types import Sampling, FeatureDefinition
from numpy import ndarray
from numpy.random import uniform
from scipy.stats import qmc


class Random(Sampling):
    """
    Class for random design space sampling.
    """

    def __init__(self, features: FeatureDefinition) -> None:
        """

        :param features: Collective targets and parameters information in the form of FeatureDefinition class
        :type features: FeatureDefinition
        """
        super().__init__(features)

    def _method(self, n_samples: int = 50) -> ndarray:
        """

        Method defining the sampling strategy.

        :param n_samples: Number of samples to generate in the DoE.
        :type n_samples: int
        :return: The samples.
        :rtype: ndarray
        """
        samples = uniform(self.lbs, self.ubs, (n_samples, self.nvar))
        return samples


class Latin(Sampling):
    """
    Class for Latin design space sampling.
    """

    def __init__(self, features: FeatureDefinition) -> None:
        """

        :param features: Collective targets and parameters information in the form of FeatureDefinition class
        :type features: FeatureDefinition
        """
        super().__init__(features)

    def _method(self, n_samples: int = 50) -> ndarray:
        """

        Method defining the sampling strategy.

        :param n_samples: Number of samples to generate in the DoE.
        :type n_samples: int
        :return: The samples.
        :rtype: ndarray
        """
        sampler = qmc.LatinHypercube(d=self.nvar)
        samp = sampler.random(n=n_samples)
        samples = qmc.scale(samp, self.lbs, self.ubs)
        return samples
