"""
Feature Extractor Class
"""
from pandas import DataFrame

from .extract_functions import is_dichotomous, is_quantitative, get_missing_entries_ratio
from .features_set import DataFeaturesSet, VariableFeaturesSet


class FeaturesExtractor:
    """
    Feature Extractor class
    """

    def run(self, data: DataFrame, response_name: str):
        """Extracts features from providaded data
        Args:
            data (DataFrame): Pandas dataframe
        Returns:
            DataFeaturesSet: Features set
        """
        features_set = DataFeaturesSet()
        features_set.rows_count, features_set.variables_count = data.shape

        response_ndarray = data[response_name].to_numpy(copy=False)
        features_set.is_response_dichotomous = is_dichotomous(response_ndarray)

        if features_set.is_response_dichotomous:
            features_set.is_response_quantitative = False
        else:
            features_set.is_response_quantitative = is_quantitative(
                response_ndarray)

        _vars_features_set = dict.fromkeys(data.columns, VariableFeaturesSet())
        _quantitatives_count = 0
        for variable_name in data.columns:
            var_features = _vars_features_set.get(variable_name)
            var_features.is_quantitative = is_quantitative(
                data[variable_name].to_numpy(copy=False))
            var_features.missing_entries_ratio = get_missing_entries_ratio(
                data[variable_name].to_numpy(copy=False))

            if var_features.is_quantitative:
                _quantitatives_count += 1

        features_set.variables_features_set = _vars_features_set
        features_set.ratio_of_continous_variables = _quantitatives_count / \
            features_set.variables_count

        return features_set
