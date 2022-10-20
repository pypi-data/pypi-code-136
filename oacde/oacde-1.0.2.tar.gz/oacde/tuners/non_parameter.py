#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Non-Parametric family
'''
import numpy as np
from sklearn.neighbors import KernelDensity
# internal imports
from oacde.tuners._base import __base



#!------------------------------------------------------------------------------
#!                                     CLASSES
#!------------------------------------------------------------------------------
## ------------------------- Kernel Density Estimation -------------------------
class KDE(__base):
    '''Kernel Density Estimation (KDE) tuner'''
    TUNER_NAME = "Kernel Density Estimation"

    def __init__(self, RS, feature_continued, kernel, bandwidth, feature_name,
                 max_training_size):
        self.kde_model = KernelDensity()
        self.kernel = kernel
        self.bandwidth = bandwidth
        self.feature_continued = feature_continued
        self.feature_name = feature_name
        self.max_training_size = max_training_size
        self.RS = RS
        self.data = []
        # indicate the KDE model for current data is fitted or not
        self.model_is_fitted = False

    @property
    def kernel(self):
        return self._kernel

    @kernel.setter
    def kernel(self, name):
        if name is None:
            name = "gaussian"
        self._kernel = name
        self.kde_model.set_params(kernel=self._kernel)

    @property
    def bandwidth(self):
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value):
        if value is None:
            value = 1.0  # default value from scikit-learn
        self._bandwidth = value
        self.kde_model.set_params(bandwidth=self._bandwidth)

    @property
    def feature_continued(self):
        return self._value_range

    @feature_continued.setter
    def feature_continued(self, boundary):
        if boundary is None:
            self._value_range = None
        else:
            if isinstance(boundary[0], (list, tuple)):
                self._value_range = boundary
            else:
                self._value_range = ((boundary[0],), (boundary[1],))

    @property
    def feature_name(self):
        return self._features_name

    @feature_name.setter
    def feature_name(self, name):
        if name is None:
            self._features_name = None
        elif isinstance(name, str):
            self._features_name = [name, ]
        elif isinstance(name, (tuple, list)):
            self._features_name = name
        else:
            raise TypeError("`feature_name` must be None, str, or a list of "
                "str, not '{}'".format(type(name)))

    @property
    def data_size(self):
        return len(self.data)

    def reset(self):
        self.data = []
        self.model_is_fitted = False

    def set_params(self, **kwargs):
        self.kde_model.set_params(**kwargs)

    def get_params(self, deep=True):
        return self.kde_model.get_params(deep)

    def get_log_density(self, X):
        return self.kde_model.score_samples(X)

    def add_data(self, new_sample):
        '''update the training data set by a batch'''
        self.data.append(new_sample)
        self.model_is_fitted = False

    def add_batch_data(self, new_batch_samples):
        '''update the training data set by a batch'''
        self.data.extend(new_batch_samples)
        self.model_is_fitted = False

    def sample(self, n_samples=1):
        if self.data_size >= 1:
            if self.model_is_fitted is False:
                self.fit()
            samples = []
            for i in range(int(n_samples)):
                x = self.kde_model.sample(
                    n_samples=1, random_state=self.RS)[0]
                # TODO 把regenerate/truncate检查单独挪出去
                while (x < self.feature_continued[0]).any() or (x > self.feature_continued[-1]).any():
                    x = self.kde_model.sample(
                        n_samples=1, random_state=self.RS)[0]
                samples.append(x)

                # x = self.kde_model.sample(n_samples=1, random_state=self.RS)[0]
                # if "F" in self.feature_name:
                #     F_index = self.feature_name.index("F")
                #     while x[F_index] <= self.feature_continued[0][F_index]:
                #         x = self.kde_model.sample(n_samples=1, random_state=self.RS)[0]
                # x = np.clip(x, self.feature_continued[0], self.feature_continued[1])
                # samples.append(x.tolist())

        else:
            X = self.RS.uniform(low=self.feature_continued[0],
                                 high=self.feature_continued[-1],
                                 size=(n_samples, len(self.feature_continued[0])))
            samples = X.tolist()
        return samples

    def score_samples(self, X):
        return self.kde_model.score_samples(X)

    def fit(self):
        if self.data_size >= 1:
            if self.max_training_size is not None:
                if self.data_size > self.max_training_size:
                    training_data = self.data[-self.max_training_size:]
                else:
                    training_data = self.data
            else:
                training_data = self.data
            self.kde_model.fit(X=np.array(training_data))
            self.training_data = training_data
            self.model_is_fitted = True
        else:
            raise ValueError("The training data set must have at least one data"
                             " point")



#!------------------------------------------------------------------------------
#!                                    FUNCTIONS
#!------------------------------------------------------------------------------



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    pass

if __name__ == "__main__":
    main()
