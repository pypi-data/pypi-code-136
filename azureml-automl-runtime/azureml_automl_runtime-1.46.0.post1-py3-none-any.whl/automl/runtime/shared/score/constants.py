# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Metrics constants."""
from azureml.training.tabular.score.constants import (
    CLASSIFICATION,
    REGRESSION,
    FORECASTING,
    IMAGE_CLASSIFICATION,
    IMAGE_CLASSIFICATION_MULTILABEL,
    IMAGE_MULTI_LABEL_CLASSIFICATION,
    IMAGE_OBJECT_DETECTION,
    IMAGE_INSTANCE_SEGMENTATION,
    TEXT_CLASSIFICATION,
    TEXT_CLASSIFICATION_MULTILABEL,
    TEXT_NER,
    TASKS,
    ACCURACY,
    WEIGHTED_ACCURACY,
    BALANCED_ACCURACY,
    NORM_MACRO_RECALL,
    LOG_LOSS,
    AUC_BINARY,
    AUC_MACRO,
    AUC_MICRO,
    AUC_WEIGHTED,
    F1_BINARY,
    F1_MACRO,
    F1_MICRO,
    F1_WEIGHTED,
    PRECISION_BINARY,
    PRECISION_MACRO,
    PRECISION_MICRO,
    PRECISION_WEIGHTED,
    RECALL_BINARY,
    RECALL_MACRO,
    RECALL_MICRO,
    RECALL_WEIGHTED,
    AVERAGE_PRECISION_BINARY,
    AVERAGE_PRECISION_MACRO,
    AVERAGE_PRECISION_MICRO,
    AVERAGE_PRECISION_WEIGHTED,
    MATTHEWS_CORRELATION,
    ACCURACY_TABLE,
    CONFUSION_MATRIX,
    CLASSIFICATION_REPORT,
    IOU,
    IOU_MICRO,
    IOU_MACRO,
    IOU_WEIGHTED,
    IOU_CLASSWISE,
    PRECISION_CLASSWISE,
    RECALL_CLASSWISE,
    F1_CLASSWISE,
    AUC_CLASSWISE,
    AVERAGE_PRECISION_CLASSWISE,
    CLASSIFICATION_SCALAR_SET,
    CLASSIFICATION_BINARY_SET,
    CLASSIFICATION_MULTILABEL_SET,
    CLASSIFICATION_NLP_MULTILABEL_SET,
    CLASSIFICATION_CLASSWISE_SET,
    CLASSIFICATION_NONSCALAR_SET,
    CLASSIFICATION_SET,
    UNSUPPORTED_CLASSIFICATION_TABULAR_SET,
    CLASSIFICATION_PRIMARY_SET,
    CLASSIFICATION_BALANCED_SET,
    EXPLAINED_VARIANCE,
    R2_SCORE,
    SPEARMAN,
    MAPE,
    MEAN_ABS_ERROR,
    NORM_MEAN_ABS_ERROR,
    MEDIAN_ABS_ERROR,
    NORM_MEDIAN_ABS_ERROR,
    RMSE,
    NORM_RMSE,
    RMSLE,
    NORM_RMSLE,
    RESIDUALS,
    PREDICTED_TRUE,
    REGRESSION_SCALAR_SET,
    REGRESSION_NORMALIZED_SET,
    REGRESSION_NONSCALAR_SET,
    REGRESSION_SET,
    REGRESSION_PRIMARY_SET,
    FORECASTING_MAPE,
    FORECASTING_RESIDUALS,
    FORECASTING_TABLE,
    FORECASTING_SCALAR_SET,
    FORECASTING_NONSCALAR_SET,
    FORECASTING_SET,
    IMAGE_CLASSIFICATION_SET,
    IMAGE_CLASSIFICATION_MULTILABEL_CLASSIFICATION_SET,
    MEAN_AVERAGE_PRECISION,
    IMAGE_OBJECT_DETECTION_SCALAR_SET,
    IMAGE_OBJECT_DETECTION_SET,
    TEXT_CLASSIFICATION_SET,
    TEXT_CLASSIFICATION_MULTILABEL_SET,
    TEXT_NER_SET,
    FULL_SET,
    FULL_NONSCALAR_SET,
    FULL_SCALAR_SET,
    METRICS_TASK_MAP,
    SAMPLE_WEIGHTS_UNSUPPORTED_SET,
    TRAIN_TIME,
    FIT_TIME,
    PREDICT_TIME,
    ALL_TIME,
    FULL_SCALAR_SET_TIME,
    SCHEMA_TYPE_ACCURACY_TABLE,
    SCHEMA_TYPE_FORECAST_HORIZON_TABLE,
    SCHEMA_TYPE_CONFUSION_MATRIX,
    SCHEMA_TYPE_CLASSIFICATION_REPORT,
    SCHEMA_TYPE_RESIDUALS,
    SCHEMA_TYPE_PREDICTIONS,
    SCHEMA_TYPE_MAPE,
    SCORE_UPPER_BOUND,
    MULTILABEL_PREDICTION_THRESHOLD,
    CLASSIFICATION_RANGES,
    REGRESSION_RANGES,
    FORECASTING_RANGES,
    RANGES_TASK_MAP,
    MAXIMIZE,
    MINIMIZE,
    NA,
    OBJECTIVES,
    CLASSIFICATION_OBJECTIVES,
    REGRESSION_OBJECTIVES,
    FORECASTING_OBJECTIVES,
    IMAGE_CLASSIFICATION_OBJECTIVES,
    IMAGE_CLASSIFICATION_MULTILABEL_OBJECTIVES,
    IMAGE_OBJECT_DETECTION_OBJECTIVES,
    TEXT_CLASSIFICATION_OBJECTIVES,
    TEXT_CLASSIFICATION_MULTILABEL_OBJECTIVES,
    TEXT_NER_OBJECTIVES,
    FULL_OBJECTIVES,
    OBJECTIVES_TASK_MAP,
    DEFAULT_PIPELINE_SCORE,
    MINIMUM_METRIC_NAME_LENGTH,
    MAXIMUM_METRIC_NAME_LENGTH
)
