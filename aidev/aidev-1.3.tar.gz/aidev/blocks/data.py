from typing import List, Union, Callable

from aidev.utilities.types import FeatureDefinition
from numpy import array, concatenate, ndarray
from pandas import DataFrame


class Data:
    """
    Class handling the database for surrogate model training.
    """

    def __init__(
        self,
        features: FeatureDefinition,
        simulator: Callable[..., List[float]],
        db_name: str = "db.csv",
    ) -> None:
        """

        Initialize class.

        :param features: Collective targets and parameters information in the form of Definition class
        :type features: FeatureDefinition
        :param simulator: Function to be optimized.
        :type simulator: callable
        :param db_name: training database name (including path if necessary)
        :type db_name: str
        """
        self.simulator = simulator
        self.db_name = db_name
        self.pnames = features.pnames
        self.tnames = features.tnames

    def generate(
        self,
        samples: Union[List[list], ndarray],
        fval: Union[List[list], ndarray, None] = None,
    ) -> DataFrame:
        """
        Method to generate Design of Experiment (DoE) data.

        :param samples: DoE (as returned by Sampling class).
        :type samples: Union[List[list], ndarray, None]
        :param save: if to save database to disk.
        :type save: bool
        :param behaviour: Whether to write or append to existing database. Options are 'w' or 'a'.
        :type behaviour: str
        :return: pandas dataframe for training surrogate model.
        :rtype: DataFrame
        """

        if fval is None:
            fval = self._evaluate(samples)

        data = DataFrame(
            concatenate((samples, fval), axis=1),  # type: ignore
            columns=self.pnames + self.tnames,
            dtype=float,
        )

        return data

    def add(
        self,
        data: DataFrame,
        samples: Union[List[list], ndarray],
        fval: Union[List[list], ndarray, None] = None,
    ) -> DataFrame:
        """
        Method to add samples to database.

        :param data:
        :type data:
        :param samples: Samples to be evaluated and added.
        :type samples: Union[List[list], ndarray]
        :param save: if to save database to disk.
        :type save: bool
        :return: pandas dataframe for training surrogate model.
        :rtype: DataFrame
        """
        if fval is None:
            fval = self._evaluate(samples)
        new_data = concatenate((samples, fval), axis=1)  # type: ignore
        data = concatenate((data.values, new_data), axis=0)  # type: ignore
        data = DataFrame(
            data,
            columns=self.pnames + self.tnames,
            dtype=float,
        )

        return data

    def _evaluate(self, samples: Union[List[list], ndarray]) -> ndarray:
        """

        :param samples: DoE (as returned by Sampling class).
        :type samples: Union[List[list], ndarray]
        :return: array containing simulator evaluations based on DoE
        :rtype: ndarray
        """
        fval = []
        for p in samples:
            try:
                fval.append(self.simulator(p))
            except:
                print(f"simulator evaluation failed with parameters: {p}")
                continue
        fval = array(fval)

        return fval
