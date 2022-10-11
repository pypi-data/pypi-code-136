import json
import numpy as np
import pandas as pd
import os
import math
import logging

from typing import List, Dict, Set
from teradataml.analytics.valib import *
from teradataml import DataFrame
from decimal import Decimal
from aoa.stats import store
from aoa.stats.metrics import publish_data_stats
from aoa.context.model_context import ModelContext

logger = logging.getLogger(__name__)


class _NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating) or isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(_NpEncoder, self).default(obj)


def _get_legacy_reference_edges(variables: List[str], statistics, dtypes):
    edges = []

    if os.path.isfile("artifacts/input/data_stats.json"):
        with open("artifacts/input/data_stats.json") as f:
            data_stats = json.load(f)
            training_stats = dict(data_stats["features"])
            training_stats.update(data_stats["predictors"])
            for v in variables:
                edges.append(training_stats[v]["statistics"]["histogram"]["edges"])
    else:
        edges = _compute_continuous_edges(variables, statistics, dtypes)

    return edges


def _compute_continuous_edges(variables, statistics, dtypes, bins=10, **kwargs):
    edges = []

    # should return what is in the feature catalog.. for now calculate linspace boundaries based on min/max
    ranges = statistics.drop(statistics.columns.difference(["xcol", "xmin", "xmax"]), axis=1)
    ranges = ranges.set_index("xcol")
    ranges.index = ranges.index.map(str.lower)
    ranges = ranges.to_dict(orient='index')

    for var in variables:
        x_min, x_max = ranges[var]["xmin"], ranges[var]["xmax"]

        # if integer type and range is less than the number of bins, only use 'range' bins
        if x_max - x_min < bins and dtypes[var].startswith("int"):
            edges.append(np.linspace(x_min, x_max, int(x_max) - int(x_min) + 1).tolist())
        # if decimal fix to two decimal places for now.. we really need to know the decimal precision to do this
        # correctly.
        elif dtypes[var].startswith("decimal") or dtypes[var].startswith("float"):
            # for bins other than 1st and last, round to two decimal places
            # (min / max must be rounded up / down accordingly so easier to just use the vals from stats)
            vals = np.linspace(x_min, x_max, bins + 1).tolist()

            for i in range(1, bins):
                vals[i] = float(Decimal("{:.2f}".format(vals[i])))

            # VAL Histogram function fails for some reason when FLOAT min boundary is set to min value, so rounding min down
            # max is rounded up just for symmetry (max boundary set to max value does work with VAL)
            p = 2
            vals[0] = np.true_divide(np.floor(vals[0] * 10 ** p), 10 ** p)
            vals[bins] = np.true_divide(np.ceil(vals[bins] * 10 ** p), 10 ** p)

            edges.append(vals)
        else:
            edges.append(np.linspace(x_min, x_max, bins + 1).tolist())

    return edges


def _decode_continuous_edges_from_stats(variables, statistics):
    new_edges = []
    for v in variables:
        if statistics[v.lower()]['edges']:
            new_edges.append(statistics[v.lower()]['edges'])
        else:
            raise Exception(f"Failed to find variable {v} edges in Dataset Stats Metadata. " +
                            f"Have you run `aoa feature compute-stats` for this columns?")

    return new_edges


def _convert_all_edges_to_val_str(all_edges):
    # boundaries for multiple columns follows the following format..
    # ["{10, 0, 200000}", "{5, 0, 100}"]
    boundaries = []
    for edges in all_edges:
        edges_str = ",".join(str(edge) for edge in edges)
        boundaries.append("{{ {} }}".format(edges_str))

    return boundaries


def _get_key_of(a, b):
    "Return the first key of b in a."
    for i, j in a.items():
        if j == b:
            return i
    return


def _stringify_keys(obj):
    return {str(k): v for (k, v) in obj.items()}


def _dict_mapper(obj, mapper):
    return {mapper[k] if k in sorted(mapper) else k: v for (k, v) in obj.items()}


def _dict_unmapper(obj, mapper):
    return {_get_key_of(mapper, k) if _get_key_of(mapper, k) is not None else k: v for (k, v) in obj.items()}


def _list_unmapper(obj, mapper):
    return [_get_key_of(mapper, item) if _get_key_of(mapper, item) is not None else item for item in
            obj] if mapper else obj


def _fill_missing_bins(bin_edges, bin_values, var_ref_edges):
    epsilon = 1e-08
    for i, edge in enumerate(var_ref_edges):
        is_present = False
        for curr_edge in bin_edges:
            if abs(float(curr_edge) - float(edge)) < epsilon:
                is_present = True

        if not is_present:
            bin_values.insert(i, 0.0)


def _strip_key_x(d: Dict):
    return {k[1:]: v for k, v in d.items()}


def _process_category_labels(labels, overrides):
    return {k: _stringify_keys(overrides)[v] if v in _stringify_keys(overrides).keys() else v for (k, v) in
            _stringify_keys(labels).items()}


def _process_category_dictionary(labels, current=[]):
    result = {}

    new_categories = sorted(list(set(labels) - set(current)))

    for i, label in enumerate(sorted(current)):
        result[i] = label

    for i, label in enumerate(new_categories):
        result[i + len(current)] = label

    return result


def _process_frequencies_dictionary(frequencies_dict):
    result = {}
    sorted_labels = sorted(frequencies_dict)

    for i, label in enumerate(sorted_labels):
        if label in frequencies_dict:
            result[i] = frequencies_dict[label]

    return result


def _process_categorical_var(frequencies, group_label, var, importance, category_labels_override, is_ordinal,
                             category_dictionary):
    data_struct = {
        "type": "categorical",
        "group": group_label,
        "category_dictionary": {},
        "category_labels": {},
        "ordinal": is_ordinal,
        "statistics": {}
    }

    var_freq = frequencies[frequencies.xcol == var]
    current_categories = list(category_dictionary.values())

    # if first row is nan then it is the null values in the dataset. remove from histogram
    if var_freq["xval"].isnull().values.any():
        n = var_freq[var_freq["xval"].isnull()]
        data_struct["statistics"]["nulls"] = n.xcnt.tolist()[0]
        var_freq = var_freq[var_freq["xval"].notnull()]

    frequencies_dict = var_freq[["xval", "xcnt"]].set_index("xval").T.to_dict(orient='records')[0]
    category_dictionary = _process_category_dictionary(frequencies_dict, current_categories)
    category_labels = _process_category_labels(category_dictionary, category_labels_override)
    processed_frequencies_dict = _process_frequencies_dictionary(frequencies_dict)

    data_struct["category_dictionary"] = category_dictionary
    data_struct["category_labels"] = category_labels
    data_struct["statistics"]["frequency"] = processed_frequencies_dict

    if importance:
        data_struct["importance"] = importance

    return data_struct


def _process_continuous_var(hist, stats, var_ref_edges, group_label, var, importance):
    data_struct = {
        "type": "continuous",
        "group": group_label,
        "statistics": {},
    }

    var_hist = hist[hist.xcol == var].sort_values(by=['xbin'])

    # if first row is nan then it is the null values in the dataset. remove from histogram
    if var_hist["xbin"].isnull().values.any():
        n = var_hist[var_hist["xbin"].isnull()]
        data_struct["statistics"]["nulls"] = n.xcnt.tolist()[0]

        var_hist = var_hist[var_hist["xbin"].notnull()]

    bin_edges = [var_hist.xbeg.tolist()[0]] + var_hist.xend.tolist()
    bin_values = var_hist.xcnt.tolist()

    # (issue #123) VAL docs originally stated that:
    # VAL histograms will values lower than the first bin to the first bin, but values greater than the
    # largest bin are added to a new bin.. Therefore we did the same on both sides. However, it turns out this doc is
    # incorrect.

    is_right_outlier_bin = math.isnan(bin_edges[-1])
    is_left_outlier_bin = math.isnan(bin_edges[0])
    if is_right_outlier_bin:
        bin_edges = bin_edges[:-1]
    if is_left_outlier_bin:
        bin_edges = bin_edges[1:]

    # Add missing bin_values based on the bin_edges vs reference_edges.
    # VAL doesn't return empty bins
    if len(bin_edges) < len(var_ref_edges):
        _fill_missing_bins(bin_edges, bin_values, var_ref_edges)

    if is_right_outlier_bin:
        bin_values[-2] += bin_values[-1]
        bin_values = bin_values[:-1]
    if is_left_outlier_bin:
        bin_values[1] += bin_values[0]
        bin_values = bin_values[1:]

    stats_values = stats[stats.xcol == var].drop(["xdb", "xtbl", "xcol"], axis=1).to_dict(orient='records')[0]
    data_struct["statistics"].update(_strip_key_x(stats_values))

    data_struct["statistics"]["histogram"] = {
        "edges": var_ref_edges,
        "values": bin_values
    }

    if importance:
        data_struct["importance"] = importance

    return data_struct


def _parse_scoring_stats(features_df: DataFrame,
                         predicted_df: DataFrame,
                         data_stats: Dict,
                         feature_importance: Dict[str, float] = {},
                         feature_metadata_fqtn: str = None,
                         feature_metadata_group: str = None) -> Dict:

    if not isinstance(features_df, DataFrame):
        raise TypeError("We only support teradataml DataFrame for features")

    if not isinstance(predicted_df, DataFrame):
        raise TypeError("We only support teradataml DataFrame for predictions")

    features = []
    targets = []
    categorical = []
    category_labels = {}
    category_ordinals = set()
    category_dictionary = {}

    for var_type in ["features", "predictors"]:
        for name, value in data_stats[var_type].items():
            # for backward compatibility with data stats created before we lower-cased
            name = name.lower()

            if var_type == "features":
                features.append(name)
            elif var_type == "predictors":
                targets.append(name)
            if "type" in value and value["type"] == "categorical":
                categorical.append(name)
                if "category_dictionary" in value:
                    category_dictionary[name] = value["category_dictionary"]
                if "category_labels" in value:
                    category_labels[name] = value["category_labels"]
                if "ordinal" in value and value["ordinal"]:
                    category_ordinals.add(name)

    total_rows_features = features_df.shape[0]
    total_rows_predictors = predicted_df.shape[0]

    if total_rows_predictors != total_rows_features:
        raise ValueError("The number of prediction rows do not match the number of features rows!")

    data_stats = _capture_stats(df=features_df,
                                features=features,
                                targets=[],
                                categorical=categorical,
                                category_labels=category_labels,
                                category_ordinals=category_ordinals,
                                category_dictionary=category_dictionary,
                                feature_importance=feature_importance,
                                feature_metadata_fqtn=feature_metadata_fqtn,
                                feature_metadata_group=feature_metadata_group)

    predictors_struct = _capture_stats(df=predicted_df,
                                       features=[],
                                       targets=targets,
                                       categorical=categorical,
                                       category_labels=category_labels,
                                       category_ordinals=category_ordinals,
                                       category_dictionary=category_dictionary,
                                       feature_importance=feature_importance,
                                       feature_metadata_fqtn=feature_metadata_fqtn,
                                       feature_metadata_group=feature_metadata_group)

    data_stats["predictors"] = predictors_struct["predictors"]

    return data_stats


def _capture_stats(df: DataFrame,
                   features: List,
                   targets: List,
                   categorical: List,
                   category_labels: Dict[str, str] = {},
                   category_ordinals: Set = set({}),
                   category_dictionary: Dict[str, str] = {},
                   feature_importance: Dict[str, float] = {},
                   feature_metadata_fqtn: str = {},
                   feature_metadata_group: str = "default") -> Dict:

    if not isinstance(df, DataFrame):
        raise TypeError("We only support teradataml DataFrame")

    # lowercase all keys/names to avoid mismatches between sql/dataframes case sensitivity
    features = [f.lower() for f in features]
    targets = [t.lower() for t in targets]
    categorical = [c.lower() for c in categorical]
    category_labels = {k.lower(): v for k, v in category_labels.items()}
    category_ordinals = {k.lower() for k in category_ordinals}
    category_dictionary = {k.lower(): v for k, v in category_dictionary.items()}
    feature_importance = {k.lower(): v for k, v in feature_importance.items()}
    df_columns = [c.lower() for c in df.columns]

    # validate that the dataframe contains the features/targets provided
    if features and not set(features).issubset(df_columns):
        raise ValueError(f"features dataframe with columns ({df.columns}) does not contain features: {features}")

    if targets and not set(targets).issubset(df_columns):
        raise ValueError(f"targets dataframe with columns ({df.columns}) does not contain targets: {targets}")

    total_rows = df.shape[0]
    continuous_vars = list((set(features) | set(targets)) - set(categorical))
    categorical_vars = list((set(features) | set(targets)) - set(continuous_vars))
    reference_edges = []

    if len(continuous_vars) > 0:
        stats = valib.Statistics(data=df, columns=continuous_vars, stats_options="all")
        stats = stats.result.to_pandas().reset_index()
        stats["xcol"] = stats["xcol"].str.lower()

        if feature_metadata_fqtn:
            feature_metadata = store.get_feature_stats(feature_metadata_fqtn)

            if not all(x in feature_metadata.keys() for x in continuous_vars):
                raise Exception(f"Ensure feature statistics in {feature_metadata_fqtn} are up to date. "
                                f"Attempted to compute stats for {continuous_vars} but only found {reference_edges}.")

            reference_edges = _decode_continuous_edges_from_stats(continuous_vars, feature_metadata)
        else:
            logging.warning(
                "This dataset doesn't have feature metadata information, this is deprecated behaviour and will not be "
                "supported in next release; at the moment histogram edges are computed dynamically during training")
            dtypes = {r[0].lower(): r[1] for r in df.dtypes._column_names_and_types}
            reference_edges = _get_legacy_reference_edges(continuous_vars, stats, dtypes)

        hist = valib.Histogram(data=df, columns=continuous_vars,
                               boundaries=_convert_all_edges_to_val_str(reference_edges))
        hist = hist.result.to_pandas().reset_index()
        hist["xcol"] = hist["xcol"].str.lower()

    if len(categorical_vars) > 0:
        frequencies = valib.Frequency(data=df, columns=categorical_vars)
        frequencies = frequencies.result.to_pandas().reset_index()
        frequencies["xcol"] = frequencies["xcol"].str.lower()

    data_struct = {
        "num_rows": total_rows,
        "features": {},
        "predictors": {}
    }

    def add_var_metadata(variable, var_type, group_label):
        if variable in continuous_vars:
            var_ref_edges = reference_edges[continuous_vars.index(variable)]
            data_struct[var_type][variable] = _process_continuous_var(
                hist,
                stats,
                var_ref_edges,
                group_label,
                variable,
                feature_importance.get(variable, None))

        else:
            data_struct[var_type][variable] = _process_categorical_var(
                frequencies,
                group_label,
                variable,
                feature_importance.get(variable, None),
                category_labels.get(variable, {}),
                variable in category_ordinals,
                category_dictionary.get(variable, {})
            )

    for var in features:
        add_var_metadata(var, "features", feature_metadata_group)

    for var in targets:
        add_var_metadata(var, "predictors", feature_metadata_group)

    return data_struct


def record_training_stats(df: DataFrame,
                          features: List[str],
                          targets: List[str],
                          categorical: List[str] = [],
                          context: ModelContext = {},
                          feature_importance: Dict[str, float] = {},
                          category_labels: Dict[str, str] = {},
                          category_ordinals: Set[str] = {},
                          **kwargs) -> Dict:
    """
    Compute and record the dataset statistics used for training. This information provides ModelOps with a snapshot
    of the dataset at this point in time (i.e. at the point of training). ModelOps uses this information for data and
    prediction drift monitoring. It can also be used for data quality monitoring as all of the information which is
    captured here is available to configure an alert on (e.g. max > some_threshold).

    Depending on the type of variable (categorical or continuous), different statistics and distributions are computed.
    All of this is computed in Vantage via the Vantage Analytics Library (VAL).

    Continuous Variable:
        Distribution: Histogram
        Statistics: Min, Max, Average, Skew, etc, nulls

    Categorical Variable:
        Distribution: Frequency
        Statistics: nulls

    The following example shows how you would use this function for a binary classification problem where the there
    are 3 features and 1 target. As it is classification, the target must be categorical and in this case, the features
    are all continuous.
    example usage:
        training_df = DataFrame.from_query("SELECT * from my_table")

        record_training_stats(training_df,
                              features=["feat1", "feat2", "feat3"],
                              targets=["targ1"],
                              categorical=["targ1"],
                              context=context)

    :param df: teradataml dataframe used for training with the feature and target variables
    :type df: teradataml.DataFrame
    :param features: feature variable(s) used in this training
    :type features: List[str]
    :param targets: target variable(s) used in this training
    :type targets: List[str]
    :param categorical: variable(s) (feature or target) that is categorical
    :type categorical: List[str]
    :param context: ModelContext which is associated with that training invocation
    :type context: ModelContext
    :param feature_importance: (Optional) feature importance
    :type feature_importance: Dict[str, float]
    :param category_labels: (Optional) category->name mapping for the categorical variables. Uses category label by default
    :type category_labels: Dict[str, str]
    :param category_ordinals: (Optional) categorical variable(s) which are of ordinal type
    :type category_labels: Set[str]
    :return: the computed data statistics
    :rtype: Dict
    :raise ValueError: if features or targets are not provided
    :raise TypeError: if df is not of type teradataml.DataFrame
    """

    logger.info("Computing training dataset statistics")

    if not features:
        raise ValueError("One or more features must be provided")

    # backward compatibility due to rename of predictors to targets in api
    if not targets:
        if "predictors" in kwargs:
            targets = kwargs["predictors"]
        else:
            raise ValueError("One or more targets must be provided")

    # backward compatibility due to rename of importance to feature_importance in api
    if not feature_importance and "importance" in kwargs:
        feature_importance = kwargs["importance"]

    feature_metadata_fqtn = None
    feature_metadata_group = None
    data_stats_filename = "artifacts/output/data_stats.json"

    if context:
        feature_metadata_fqtn = context.dataset_info.get_feature_metadata_fqtn()
        feature_metadata_group = context.dataset_info.feature_metadata_monitoring_group
        data_stats_filename = os.path.join(context.artifact_output_path, "data_stats.json")

    data_stats = _capture_stats(df=df,
                                features=features,
                                targets=targets,
                                categorical=categorical,
                                category_labels=category_labels,
                                category_ordinals=category_ordinals,
                                feature_importance=feature_importance,
                                feature_metadata_fqtn=feature_metadata_fqtn,
                                feature_metadata_group=feature_metadata_group)

    with open(data_stats_filename, 'w+') as f:
        json.dump(data_stats, f, indent=2, cls=_NpEncoder)

    return data_stats


def record_evaluation_stats(features_df: DataFrame,
                            predicted_df: DataFrame,
                            feature_importance: Dict[str, float] = {},
                            context: ModelContext = None,
                            **kwargs) -> Dict:
    """
    Compute and record the dataset statistics used for evaluation. This information provides ModelOps with a snapshot
    of the dataset at this point in time (i.e. at the point of evaluation). ModelOps uses this information for data
    and prediction drift monitoring. It can also be used for data quality monitoring as all of the information which
    is captured here is available to configure an alert on (e.g. max > some_threshold).

    Depending on the type of variable (categorical or continuous), different statistics and distributions are computed.
    All of this is computed in Vantage via the Vantage Analytics Library (VAL).

    Continuous Variable:
        Distribution: Histogram
        Statistics: Min, Max, Average, Skew, etc, nulls

    Categorical Variable:
        Distribution: Frequency
        Statistics: nulls

    example usage:
        features_df = DataFrame.from_query("SELECT * from my_features_table")

        predicted_df = model.predict(features_df)

        record_evaluation_stats(features_df=features_df,
                                predicted_df=predicted_df,
                                context=context)

    :param features_df: dataframe containing feature variable(s) from evaluation
    :type features_df: teradataml.DataFrame
    :param predicted_df: dataframe containing predicted target variable(s) from evaluation
    :type predicted_df: teradataml.DataFrame
    :param context: ModelContext which is associated with that training invocation
    :type context: ModelContext
    :param feature_importance: (Optional) feature importance
    :type feature_importance: Dict[str, float]
    :return: the computed data statistics
    :rtype: Dict
    :raise ValueError: if the number of predictions (rows) do not match the number of features (rows)
    :raise TypeError: if features_df or predicted_df is not of type teradataml.DataFrame
    """

    logger.info("Computing evaluation dataset statistics")

    # backward compatibility due to rename of importance to feature_importance in api
    if not feature_importance and "importance" in kwargs:
        feature_importance = kwargs["importance"]

    feature_metadata_fqtn = None
    feature_metadata_group = None
    output_data_stats_filename = "artifacts/output/data_stats.json"
    input_data_stats_filename = "artifacts/input/data_stats.json"

    if context:
        feature_metadata_fqtn = context.dataset_info.get_feature_metadata_fqtn()
        feature_metadata_group = context.dataset_info.feature_metadata_monitoring_group
        output_data_stats_filename = os.path.join(context.artifact_output_path, "data_stats.json")
        input_data_stats_filename = os.path.join(context.artifact_input_path, "data_stats.json")

    with open(input_data_stats_filename, 'r') as f:
        training_data_stats = json.load(f)

    data_stats = _parse_scoring_stats(features_df=features_df,
                                      predicted_df=predicted_df,
                                      data_stats=training_data_stats,
                                      feature_importance=feature_importance,
                                      feature_metadata_fqtn=feature_metadata_fqtn,
                                      feature_metadata_group=feature_metadata_group)

    # for evaluation, the core will do it (we may change this later to unify)..
    with open(output_data_stats_filename, 'w+') as f:
        json.dump(data_stats, f, indent=2, cls=_NpEncoder)

    return data_stats


def record_scoring_stats(features_df: DataFrame,
                         predicted_df: DataFrame,
                         context: ModelContext = None) -> Dict:
    """
    Compute and record the dataset statistics used for scoring. This information provides ModelOps with a snapshot
    of the dataset at this point in time (i.e. at the point of scoring). ModelOps uses this information for data
    and prediction drift monitoring. It can also be used for data quality monitoring as all of the information which
    is captured here is available to configure an alert on (e.g. max > some_threshold).

    Depending on the type of variable (categorical or continuous), different statistics and distributions are computed.
    All of this is computed in Vantage via the Vantage Analytics Library (VAL).

    Continuous Variable:
        Distribution: Histogram
        Statistics: Min, Max, Average, Skew, etc, nulls

    Categorical Variable:
        Distribution: Frequency
        Statistics: nulls

    example usage:
        features_df = DataFrame.from_query("SELECT * from my_features_table")

        predicted_df = model.predict(features_df)

        record_scoring_stats(features_df=features_df,
                            predicted_df=predicted_df,
                            context=context)

    :param features_df: dataframe containing feature variable(s) from evaluation
    :type features_df: teradataml.DataFrame
    :param predicted_df: dataframe containing predicted target variable(s) from evaluation
    :type predicted_df: teradataml.DataFrame
    :param context: ModelContext which is associated with that training invocation
    :type context: ModelContext
    :return: the computed data statistics
    :rtype: Dict
    :raise ValueError: if the number of predictions (rows) do not match the number of features (rows)
    :raise TypeError: if features_df or predicted_df is not of type teradataml.DataFrame
    """

    logger.info("Computing scoring dataset statistics")

    feature_metadata_fqtn = None
    feature_metadata_group = None
    input_data_stats_filename = "artifacts/input/data_stats.json"

    if context:
        feature_metadata_fqtn = context.dataset_info.get_feature_metadata_fqtn()
        feature_metadata_group = context.dataset_info.feature_metadata_monitoring_group
        input_data_stats_filename = os.path.join(context.artifact_input_path, "data_stats.json")

    with open(input_data_stats_filename, 'r') as f:
        training_data_stats = json.load(f)

    data_stats = _parse_scoring_stats(features_df=features_df,
                                      predicted_df=predicted_df,
                                      data_stats=training_data_stats,
                                      feature_metadata_fqtn=feature_metadata_fqtn,
                                      feature_metadata_group=feature_metadata_group)

    # Another possibility could be to make an api call to the core to publish
    # it (but for now let's implement it on the scorer side)
    publish_data_stats(data_stats)

    return data_stats


def compute_continuous_stats(features_df: DataFrame, continuous_features: List, **kwargs):
    dtypes = {r[0].lower(): r[1] for r in features_df.dtypes._column_names_and_types}

    stats = valib.Statistics(data=features_df, columns=continuous_features, stats_options="all")
    stats = stats.result.to_pandas().reset_index()
    reference_edges = _compute_continuous_edges(continuous_features, stats, dtypes)
    edges_dict = dict(zip(continuous_features, reference_edges))
    column_stats = {f.lower(): {'edges': edges_dict[f]} for f in edges_dict.keys()}
    return column_stats


def compute_categorical_stats(features_df: DataFrame, categorical_features: List, **kwargs):
    statistics = valib.Frequency(data=features_df, columns=categorical_features)
    statistics = statistics.result.to_pandas().reset_index()
    statistics = statistics.drop(statistics.columns.difference(["xcol", "xval", "xpct"]), axis=1)
    statistics = statistics.groupby('xcol').apply(lambda x: dict(zip(x['xval'], x['xpct']))).to_dict()
    column_stats = {}
    for var in categorical_features:
        column_stats[var.lower()] = {
            'frequencies': {k: float(Decimal("{:.2f}".format(float(v)))) for k, v in statistics[var].items()}}

    return column_stats
