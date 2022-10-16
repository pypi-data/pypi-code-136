"""File containing all model classes necessary to run the classifier"""
import logging
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

from xgboost import XGBClassifier


# initiate logger
MODELS_LOGGER = logging.getLogger(__name__)


class BaseMixin:
    """A mixin class for all models. This allows for each algorithm to use the
    optimise and plotting functions"""

    def plot_time_vs_accuracy(self, out_dir: Path) -> None:
        """Plotting the training time vs the accuracy.

        Args:
            time (array): The time values to plot
            accuracy(array) The accuracy values to plot
            out_dir (Path): Output directory

        Returns:
            None
        """
        time = self.cv_df['mean_fit_time']
        accuracy = self.cv_df['mean_test_score']
        fig = plt.figure()
        axis = fig.add_subplot(111)
        axis.scatter(time, accuracy)
        axis.set_xlabel("Time (s)")
        axis.set_ylabel("Accuracy (-) ")
        plt.tight_layout()
        plt.savefig(out_dir / 'Optimisation_time.png', dpi=300)

    def random_optimise(
            self, optimization_parameters: dict,
            trainx: np.ndarray, trainy: np.ndarray, out_dir: Path,
            optimise_iters: int = 10) -> Any:
        """Optimization of a parameter space using random samples from the
        parameter space

        Args:
            trainx (np.ndarray):   Training dataset features (X-values)
            trainy (np.ndarray):   Training dataset outputs
                (class names, y values)
            out_dir (Path):  The output directory path
            optimise_iters (int): The number of iterations for the optimisation.

        Returns:
            The best performing parameter combination  (dict)

        """
        MODELS_LOGGER.info("\n####-----Optimization----#####\n")
        MODELS_LOGGER.info(
            "Starting Optimization. This might take a while....")
        clf = RandomizedSearchCV(
            self,
            optimization_parameters, scoring='accuracy', verbose=100,
            refit=False, cv=3, return_train_score=True, n_jobs=-1,
            n_iter=optimise_iters)

        clf.fit(trainx, trainy)
        self.cv_df = pd.DataFrame(clf.cv_results_)
        MODELS_LOGGER.debug("--Optimization Results--\n %s",
                            self.cv_df[['mean_train_score', 'mean_test_score',
                                        'mean_fit_time']])
        parameter_set = self.cv_df['params'][self.cv_df['rank_test_score'] ==
                                             1].values[0]
        MODELS_LOGGER.debug("\nThe best parameter combination is:\n %s",
                            parameter_set)
        self.plot_time_vs_accuracy(out_dir)
        return parameter_set

# pylint: disable=too-many-ancestors


class RandomForest(RandomForestClassifier, BaseMixin):
    """RandomForest class; child of RandomForestClassifier from sk-learn"""

    def __init__(self,
                 n_estimators=100,
                 criterion="gini",
                 max_depth=None,
                 min_samples_split=2,
                 min_samples_leaf=1,
                 min_weight_fraction_leaf=0.,
                 max_features="auto",
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 bootstrap=True,
                 oob_score=False,
                 n_jobs=1,
                 random_state=None,
                 verbose=0,
                 class_weight=None,
                 ccp_alpha=0.0,
                 max_samples=None):
        super().__init__()

        self.n_estimators = n_estimators
        self.criterion = criterion
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.min_weight_fraction_leaf = min_weight_fraction_leaf
        self.max_features = max_features
        self.max_leaf_nodes = max_leaf_nodes
        self.min_impurity_decrease = min_impurity_decrease
        self.bootstrap = bootstrap
        self.oob_score = oob_score
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.verbose = verbose
        self.class_weight = class_weight
        self.ccp_alpha = ccp_alpha
        self.max_samples = max_samples


class XGBoost(XGBClassifier, BaseMixin):
    """XGBoost class, child of XGBoostclassifier model from sk-learn"""

    def __init__(self, objective="binary:logistic", **kwargs) -> None:
        super().__init__(objective=objective, **kwargs)
        self.optimization_parameters = {
            "learning_rate": [0.1, 0.2, 0.3],
            "n_estimators": [10, 20, 50, 100, 200],
            "max_depth": [1, 3, 5, 10]
        }


class SingleClass(IsolationForest, BaseMixin):

    """Singleclass class, child of IsolationForest model from sk-learn"""

    def __init__(self,
                 n_estimators=100,
                 max_samples="auto",
                 max_features=1) -> None:
        super().__init__(
            n_estimators=n_estimators,
            max_samples=max_samples,
            max_features=max_features)

        self.optimization_parameters = {
            "n_estimators": [10, 20, 50, 100, 200],
            "max_samples": ['auto', 10, 50, 100, 200],
            "max_features": [0.1, 0.3, 0.5, 1.0]
        }


class Knn(KNeighborsClassifier, BaseMixin):
    """K-Nearest-Neighbor class; child of KNeighborsClassifier from sk-learn"""

    def __init__(self,
                 n_neighbors,
                 weights,
                 algorithm,
                 leaf_size,
                 p,
                 metric,
                 metric_params,
                 n_jobs):
        super().__init__(n_neighbors=n_neighbors,
                         weights=weights,
                         algorithm=algorithm,
                         leaf_size=leaf_size,
                         p=p,
                         metric=metric,
                         metric_params=metric_params,
                         n_jobs=n_jobs)
        self.algorithm = algorithm

    def fit(self, X, y):
        if isinstance(X, tuple):
            # Tuple when patterns where created in this run from
            # DtwPatternCreator
            sample_x, sample_y = X
            super().fit(sample_x, sample_y)
        else:
            super().fit(X, y)


class KnnDtw(Pipeline, BaseMixin):
    """SKlearn Pipeline, child of Pipeline model from sk-learn
       Contains K-Nearest-Neighbors classification
       Creates time series patterns from data on the first run.
       Then normalizes the data
       And then runs classification with Knn and dtw as distance
       metrics"""

    def __init__(self,
                 n_neighbors=1,
                 weights="uniform",
                 algorithm="brute",
                 leaf_size=30,
                 p=2,
                 metric="minkowski",
                 metric_params=None,
                 n_jobs=None,
                 fit_params=None,
                 number_of_patterns_per_class=1,
                 use_gam=True,
                 out_dir=None,
                 patterns_path=None,
                 patterns_save=False
                 ):

        from classifier.timeseries import dtw_metric  # pylint: disable=import-outside-toplevel

        self.fit_params = fit_params
        self.n_neighbors = n_neighbors
        self.weights = weights
        self.algorithm = algorithm
        self.leaf_size = leaf_size
        self.p = p  # pylint: disable=invalid-name
        self.metric = metric
        self.metric_params = metric_params
        self.n_jobs = n_jobs
        self.number_of_patterns_per_class = \
            number_of_patterns_per_class
        self.use_gam = use_gam
        self.out_dir = out_dir
        self.patterns_path = patterns_path
        self.patterns_save = patterns_save

        super().__init__(steps=[
            ('pattern_creator', DtwPatternCreator(
                number_of_patterns_per_class=number_of_patterns_per_class,
                use_gam=use_gam,
                out_dir=out_dir,
                patterns_path=patterns_path,
                patterns_save=patterns_save)),
            ('transformer', NormalizeTsTransformer(
                fit_params=fit_params)),
            ('classifier', Knn(
                n_neighbors=n_neighbors,
                weights=weights,
                algorithm=algorithm,
                leaf_size=leaf_size,
                p=p,
                metric=dtw_metric,
                metric_params=metric_params,
                n_jobs=n_jobs,
            ))
        ])

    def set_params(self, **kwargs):
        """Set the parameters of this estimator.

        Valid parameter keys can be listed with ``get_params()``.

        Returns
        -------
        self
        """
        # Add "classifier__" to Classifier arguments
        classifier_args = ["n_neighbors", "weights", "algorithm", "leaf_size",
                           "p", "metric", "metric_params", "n_jobs"]
        pattern_creator_args = ["number_of_patterns_per_class",
                                "use_gam", "out_dir", "patterns_path",
                                "patterns_save"]
        transformer_args = ["fit_params"]

        classifier_kwargs = {'classifier__'+key: value for key,
                             value in kwargs.items() if key in classifier_args}
        pattern_creator_kwargs = {
            'pattern_creator__' + key: value for key, value in kwargs.items()
            if key in pattern_creator_args}
        transformer_kwargs = {
            'transformer__' + key: value for key, value in kwargs.items()
            if key in transformer_args}

        kwargs_adjusted = {
            **classifier_kwargs, **pattern_creator_kwargs, **transformer_kwargs}
        self._set_params('steps', **kwargs_adjusted)
        return self


class NormalizeTsTransformer(BaseEstimator, TransformerMixin):
    """ Normalizes timeseries data
    """
    # pylint: disable=unused-argument, invalid-name

    def __init__(self, fit_params=None):
        self.fit_params = fit_params
        self.scaler = MinMaxScaler()

    def fit(self, sample, y=None):
        """ Fit method """
        if isinstance(sample, tuple):
            # Tuple when patterns where created in this run from
            # DtwPatternCreator
            X = sample[0]
            self.scaler.fit(
                X.reshape(-1, self.fit_params['band_count']))
        else:
            self.scaler.fit(
                sample.reshape(-1, self.fit_params['band_count']))
        return self

    def transform(self, sample):  # pylint: disable=unused-argument
        """ Normalize the samples based on the limits learned on fit

        Args:
            dataset (np.ndarray):
                index: pixels; columns: bands per date (flattened)

        Returns:
            dataset_extracted_features (np.ndarray): standardized per band
        """
        if isinstance(sample, tuple):
            # Tuple when patterns where created in this run from
            # DtwPatternCreator
            sampleX, sample_y = sample
            sampleX_transformed = self.scaler.transform(
                sampleX.reshape(-1, self.fit_params['band_count'])).reshape(
                    -1, sampleX.shape[-1])
            return sampleX_transformed, sample_y

        sample_transformed = self.scaler.transform(
            sample.reshape(-1, self.fit_params['band_count'])).reshape(
                -1, sample.shape[-1])
        return sample_transformed


class DtwPatternCreator(BaseEstimator, TransformerMixin):
    """ Creates the pattern for the dynamic time warping algorithm
    """
    # pylint: disable=unused-argument, invalid-name

    def __init__(self, number_of_patterns_per_class=1, use_gam=True,
                 out_dir=None, patterns_path=None, patterns_save=False):
        self.number_of_patterns_per_class = number_of_patterns_per_class
        self.use_gam = use_gam
        self.created_patterns = False
        self.out_dir = out_dir
        self.patterns_path = patterns_path
        self.patterns_save = patterns_save

    def fit(self, sample, y=None):
        """ Fit method """
        return self

    def transform(self, sample):
        """ Transforms the data to patterns for each class. Does only transform
        once during fit.

        Args:
            dataset (np.ndarray):
                index: pixels; columns: bands per date (flattened)

        Returns:
            dataset_extracted_features (np.ndarray): standardized per band
        """
        from classifier.timeseries import get_characteristic_timeseries  # pylint: disable=import-outside-toplevel

        if not self.created_patterns:
            # Get patterns
            if self.patterns_path:
                MODELS_LOGGER.info("Use provided pattern file.")
                # From provided file
                sample = pd.read_pickle(self.patterns_path)
            else:
                MODELS_LOGGER.info("Create new patterns from data.")
                # Create new patterns
                sample = get_characteristic_timeseries(
                    sample, self.number_of_patterns_per_class,
                    self.use_gam, self.out_dir)
            # Save patterns only if not provided
            if self.patterns_save and not self.patterns_path and \
               self.out_dir:
                sample.to_pickle(self.out_dir / "training_patterns.pkl")

            # set y to class values of the patterns
            y = sample['class'].values
            # only extract data columns
            sample = sample.loc[:, ~sample.columns.get_level_values(0).isin(
                ['class', 'roi_fid'])].values
            self.created_patterns = True
            return sample, y
        if isinstance(sample, pd.DataFrame):
            # if it has already extracted patterns but gets dataframe with
            # class and roi_fid columns
            sample = sample.loc[:, ~sample.columns.get_level_values(0).isin(
                ['class', 'roi_fid'])].values
        # If numpy array or converted to numpy array
        return sample
