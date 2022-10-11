import logging
from typing import Any, Dict, List, Optional, Union

from aporia.core.http_client import HttpClient
from aporia.core.logging_utils import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class FieldTrainingData:
    """Field training data."""

    def __init__(
        self,
        field_name: str,
        key: Optional[str] = None,
        bins: Optional[List[Union[float, int, str, bool]]] = None,
        counts: Optional[List[int]] = None,
        min: Optional[float] = None,
        max: Optional[float] = None,
        sum: Optional[float] = None,
        median: Optional[float] = None,
        average: Optional[float] = None,
        std: Optional[float] = None,
        variance: Optional[float] = None,
        num_samples: Optional[int] = None,
        num_missing_values: Optional[int] = None,
        num_posinf_values: Optional[int] = None,
        num_neginf_values: Optional[int] = None,
        num_unique_values: Optional[int] = None,
        num_zero_values: Optional[int] = None,
        mse: Optional[float] = None,
        rmse: Optional[float] = None,
        mae: Optional[float] = None,
        tn: Optional[int] = None,
        fp: Optional[int] = None,
        fn: Optional[int] = None,
        tp: Optional[int] = None,
        recall_score: Optional[float] = None,
        precision_score: Optional[float] = None,
        accuracy: Optional[float] = None,
        f1_score: Optional[float] = None,
        top: Optional[Union[float, int, str, bool]] = None,
        top_frequency: Optional[int] = None,
    ):
        """Initializes a FieldTrainingData object.

        Args:
            field_name: Field name
            key: Key for dict fields.
            bins: Histogram bin edges.
            counts: Hitsogram.
            min: Minimum value.
            max: Maximum Value.
            sum: Sum of all values.
            median: Median values.
            average: Average value.
            std: Standard deviation value.
            variance: Variance value.
            num_samples: Number of data samples.
            num_missing_values: Number of missing values.
            num_posinf_values: Number of positive infinite values.
            num_neginf_values: Number of negative infinite values.
            num_unique_values: Number of unique values.
            num_zero_values: Number of zero values.
            mse: MSE for numeric predictions (if labels were reported).
            rmse: RMSE for numeric predictions (if labels were reported).
            mae: MAE for numeric predictions (if labels were reported).
            tn: TN for boolean predictions (if labels were reported).
            fp: FP for boolean predictions (if labels were reported).
            fn: FN for boolean predictions (if labels were reported).
            tp: TP for boolean predictions (if labels were reported).
            recall_score: Recall score for boolean predictions (if labels were reported).
            precision_score: Precision score for boolean predictions (if labels were reported).
            accuracy: Accuracy for boolean predictions (if labels were reported).
            f1_score: F1 score for boolean predictions (if labels were reported).
            top: The value that appears the top number of times in non-numeric dataset.
            top_frequency: The number of times the top value appear in the non-numeric dataset.
        """
        self.field_name = field_name
        self.key = key
        self.bins = bins
        self.counts = counts
        self.min = min
        self.max = max
        self.sum = sum
        self.median = median
        self.average = average
        self.std = std
        self.variance = variance
        self.num_samples = num_samples
        self.num_missing_values = num_missing_values
        self.num_posinf_values = num_posinf_values
        self.num_neginf_values = num_neginf_values
        self.num_unique_values = num_unique_values
        self.num_zero_values = num_zero_values
        self.mse = mse
        self.rmse = rmse
        self.mae = mae
        self.tn = tn
        self.fp = fp
        self.fn = fn
        self.tp = tp
        self.recall_score = recall_score
        self.precision_score = precision_score
        self.accuracy = accuracy
        self.f1_score = f1_score
        self.top = top
        self.top_frequency = top_frequency

    def serialize(self) -> dict:
        """Serializes the field training data to a dict.

        Returns:
            Serialized training data.
        """
        return {
            "fieldName": self.field_name,
            "key": self.key,
            "bins": self.bins,
            "counts": self.counts,
            "min": self.min,
            "max": self.max,
            "sum": self.sum,
            "median": self.median,
            "average": self.average,
            "std": self.std,
            "variance": self.variance,
            "numSamples": self.num_samples,
            "numMissingValues": self.num_missing_values,
            "numPosinfValues": self.num_posinf_values,
            "numNeginfValues": self.num_neginf_values,
            "numUniqueValues": self.num_unique_values,
            "numZeroValues": self.num_zero_values,
            "mse": self.mse,
            "rmse": self.rmse,
            "mae": self.mae,
            "tn": self.tn,
            "fp": self.fp,
            "fn": self.fn,
            "tp": self.tp,
            "recallScore": self.recall_score,
            "precisionScore": self.precision_score,
            "accuracy": self.accuracy,
            "f1Score": self.f1_score,
            "top": self.top,
            "topFrequency": self.top_frequency,
        }

    def serialize_backward_compatibility_no_performance(self) -> dict:
        """Serializes the field training data to a dict without the new performance metric.

        Returns:
            Serialized training data without the new performance metric for backward compatibility.
        """
        return {
            "fieldName": self.field_name,
            "key": self.key,
            "bins": self.bins,
            "counts": self.counts,
            "min": self.min,
            "max": self.max,
            "sum": self.sum,
            "median": self.median,
            "average": self.average,
            "std": self.std,
            "variance": self.variance,
            "numSamples": self.num_samples,
            "numMissingValues": self.num_missing_values,
            "numPosinfValues": self.num_posinf_values,
            "numNeginfValues": self.num_neginf_values,
            "numUniqueValues": self.num_unique_values,
            "numZeroValues": self.num_zero_values,
        }

    def serialize_backward_compatibility_no_top_metric(self) -> dict:
        """Serializes the field training data to a dict without the top and top_frequency metrics.

        Returns:
            Serialized training data without the new top and top_frequency metrics for backward compatibility.
        """
        return {
            "fieldName": self.field_name,
            "key": self.key,
            "bins": self.bins,
            "counts": self.counts,
            "min": self.min,
            "max": self.max,
            "sum": self.sum,
            "median": self.median,
            "average": self.average,
            "std": self.std,
            "variance": self.variance,
            "numSamples": self.num_samples,
            "numMissingValues": self.num_missing_values,
            "numPosinfValues": self.num_posinf_values,
            "numNeginfValues": self.num_neginf_values,
            "numUniqueValues": self.num_unique_values,
            "numZeroValues": self.num_zero_values,
            "mse": self.mse,
            "rmse": self.rmse,
            "mae": self.mae,
            "tn": self.tn,
            "fp": self.fp,
            "fn": self.fn,
            "tp": self.tp,
            "recallScore": self.recall_score,
            "precisionScore": self.precision_score,
            "accuracy": self.accuracy,
            "f1Score": self.f1_score,
        }


async def log_training_data(
    http_client: HttpClient,
    model_id: str,
    model_version: str,
    features: List[FieldTrainingData],
    predictions: Optional[List[FieldTrainingData]] = None,
    labels: Optional[List[FieldTrainingData]] = None,
    raw_inputs: Optional[List[FieldTrainingData]] = None,
):
    """Reports training data.

    Args:
        http_client: Http client
        model_id: Model ID
        model_version: Mode version
        features: Training set features.
        predictions: Training set predictions.
        labels: Training set labels.
        raw_inputs: Training set raw inputs.
    """
    newest_query = """
        mutation LogTrainingSet(
            $modelId: String!,
            $modelVersion: String!,
            $features: [FieldTrainingData]!
            $predictions: [FieldTrainingData]
            $labels: [FieldTrainingData]!
            $rawInputs: [FieldTrainingData]
        ) {
            logTrainingSet(
                modelId: $modelId,
                modelVersion: $modelVersion,
                predictions: $predictions
                features: $features
                labels: $labels
                rawInputs: $rawInputs
            ) {
                warnings
            }
        }
    """

    newest_variables = {
        "modelId": model_id,
        "modelVersion": model_version,
        "predictions": [field_data.serialize() for field_data in predictions]
        if predictions is not None
        else None,
        "features": [field_data.serialize() for field_data in features],
        "labels": [field_data.serialize() for field_data in labels] if labels is not None else None,
        "rawInputs": [field_data.serialize() for field_data in raw_inputs]
        if raw_inputs is not None
        else None,
    }

    # For on_prem deployment with old controller version that don't support predictions
    backward_compatibility_query = """
        mutation LogTrainingSet(
            $modelId: String!,
            $modelVersion: String!,
            $features: [FieldTrainingData]!
            $labels: [FieldTrainingData]!
            $rawInputs: [FieldTrainingData]
        ) {
            logTrainingSet(
                modelId: $modelId,
                modelVersion: $modelVersion,
                features: $features
                labels: $labels
                rawInputs: $rawInputs
            ) {
                warnings
            }
        }
    """
    backward_compatibility_variables_no_performance = {
        "modelId": model_id,
        "modelVersion": model_version,
        "features": [
            field_data.serialize_backward_compatibility_no_performance() for field_data in features
        ],
        "labels": [
            field_data.serialize_backward_compatibility_no_performance() for field_data in labels
        ]
        if labels is not None
        else None,
        "rawInputs": [
            field_data.serialize_backward_compatibility_no_performance()
            for field_data in raw_inputs
        ]
        if raw_inputs is not None
        else None,
    }

    backward_compatibility_variables_no_top_metric = {
        "modelId": model_id,
        "modelVersion": model_version,
        "features": [
            field_data.serialize_backward_compatibility_no_top_metric() for field_data in features
        ],
        "predictions": [
            field_data.serialize_backward_compatibility_no_top_metric()
            for field_data in predictions
        ]
        if predictions is not None
        else None,
        "labels": [
            field_data.serialize_backward_compatibility_no_top_metric() for field_data in labels
        ]
        if labels is not None
        else None,
        "rawInputs": [
            field_data.serialize_backward_compatibility_no_top_metric() for field_data in raw_inputs
        ]
        if raw_inputs is not None
        else None,
    }

    async def _log_training_data_with_backward_compatibility(query: str, query_variables: dict):
        try:
            result = await http_client.graphql(query, query_variables)
            for warning in result["logTrainingSet"]["warnings"]:
                logger.warning(warning)

        # Handling new sdk with old controllers that don't receive predictions in training
        except Exception as exp:
            # The compatibility is for versions before inserting ticket APR-1080
            if "Unknown argument 'predictions' on field 'Mutation.logTrainingSet'" in str(exp):
                logger.warning(
                    "Training set's predictions reporting is unsupported.\
                    Please update your controller version."
                )

                await _log_training_data_with_backward_compatibility(
                    backward_compatibility_query, backward_compatibility_variables_no_performance
                )
            # The compatibility is for versions before inserting ticket APR-1080
            elif "Field 'mse' is not defined by type 'FieldTrainingData'" in str(exp):
                # We don't log a warning cause the user didn't try to report predictions
                await _log_training_data_with_backward_compatibility(
                    backward_compatibility_query, backward_compatibility_variables_no_performance
                )
            # The compatibility is for versions before inserting ticket APR-1135
            elif "Field 'top' is not defined by type 'FieldTrainingData'" in str(exp):
                # we use the newest query because if this is the received error then
                # the predictions field is defined
                await _log_training_data_with_backward_compatibility(
                    newest_query, backward_compatibility_variables_no_top_metric
                )
            else:
                raise exp

    await _log_training_data_with_backward_compatibility(newest_query, newest_variables)


async def log_test_data(
    http_client: HttpClient,
    model_id: str,
    model_version: str,
    features: List[FieldTrainingData],
    predictions: List[FieldTrainingData],
    labels: List[FieldTrainingData],
    raw_inputs: Optional[List[FieldTrainingData]] = None,
):
    """Reports test data.

    Args:
        http_client: Http client
        model_id: Model ID
        model_version: Mode version
        features: Test set features.
        predictions: Test set features.
        labels: Test set labels.
        raw_inputs: Test set raw inputs.
    """
    newest_query = """
        mutation LogTestSet(
            $modelId: String!,
            $modelVersion: String!,
            $features: [FieldTrainingData]!
            $predictions: [FieldTrainingData]!
            $labels: [FieldTrainingData]!
            $rawInputs: [FieldTrainingData]
        ) {
            logTestSet(
                modelId: $modelId,
                modelVersion: $modelVersion,
                features: $features
                predictions: $predictions
                labels: $labels
                rawInputs: $rawInputs
            ) {
                warnings
            }
        }
    """

    newest_variables = {
        "modelId": model_id,
        "modelVersion": model_version,
        "features": [field_data.serialize() for field_data in features],
        "predictions": [field_data.serialize() for field_data in predictions],
        "labels": [field_data.serialize() for field_data in labels],
        "rawInputs": [field_data.serialize() for field_data in raw_inputs]
        if raw_inputs is not None
        else None,
    }

    backward_compatibility_variables_no_performance = {
        "modelId": model_id,
        "modelVersion": model_version,
        "features": [
            field_data.serialize_backward_compatibility_no_performance() for field_data in features
        ],
        "predictions": [
            field_data.serialize_backward_compatibility_no_performance()
            for field_data in predictions
        ],
        "labels": [
            field_data.serialize_backward_compatibility_no_performance() for field_data in labels
        ],
        "rawInputs": [
            field_data.serialize_backward_compatibility_no_performance()
            for field_data in raw_inputs
        ]
        if raw_inputs is not None
        else None,
    }

    backward_compatibility_variables_no_top_metric = {
        "modelId": model_id,
        "modelVersion": model_version,
        "features": [
            field_data.serialize_backward_compatibility_no_top_metric() for field_data in features
        ],
        "predictions": [
            field_data.serialize_backward_compatibility_no_top_metric()
            for field_data in predictions
        ],
        "labels": [
            field_data.serialize_backward_compatibility_no_top_metric() for field_data in labels
        ],
        "rawInputs": [
            field_data.serialize_backward_compatibility_no_top_metric() for field_data in raw_inputs
        ]
        if raw_inputs is not None
        else None,
    }

    async def _log_test_data_with_backward_compatibility(query: str, query_variables: dict):
        try:
            result = await http_client.graphql(query, query_variables)
            for warning in result["logTestSet"]["warnings"]:
                logger.warning(warning)

        # Handling new sdk with old controllers that don't receive predictions in training
        except Exception as exp:
            # The compatibility is for versions before inserting ticket APR-1080
            if "Field 'mse' is not defined by type 'FieldTrainingData'" in str(exp):
                # We don't log a warning cause the user didn't try to report predictions
                await _log_test_data_with_backward_compatibility(
                    newest_query, backward_compatibility_variables_no_performance
                )
            # The compatibility is for versions before inserting ticket APR-1135
            elif "Field 'top' is not defined by type 'FieldTrainingData'" in str(exp):
                await _log_test_data_with_backward_compatibility(
                    newest_query, backward_compatibility_variables_no_top_metric
                )
            else:
                raise exp

    await _log_test_data_with_backward_compatibility(newest_query, newest_variables)


async def log_training_sample_data(
    http_client: HttpClient,
    model_id: str,
    model_version: str,
    features: List[Dict[str, Any]],
    labels: Optional[List[Any]] = None,
    raw_inputs: Optional[List[Any]] = None,
):
    """Reports training sample.

    Args:
        http_client: Http client
        model_id: Model ID.
        model_version: Mode version.
        features: List of features.
        labels: List of labels.
        raw_inputs: List of raw inputs.
    """
    await http_client.post(
        url=f"/models/{model_id}/versions/{model_version}/training_sample",
        data={"features": features, "labels": labels, "raw_inputs": raw_inputs},
    )
