"Test for samples module"
import numpy as np
from classifier.samples import Samples, TimeSeries


def test_impute_timeseries_AsExpected(
        setup_samples_df_with_nans_ref, setup_samples_df_with_nans):
    ref_samples = setup_samples_df_with_nans_ref
    timeseries = TimeSeries(None, None, None)

    timeseries_imputed = timeseries.impute_ts(setup_samples_df_with_nans)
    assert np.array_equal(
        ref_samples.to_numpy(),
        timeseries_imputed.to_numpy())


def test_outlier_removal_RemovedAsExpected(
        setup_samples_df, setup_samples_df_with_outliers):
    ref_samples = setup_samples_df
    samples_outlier_removed = Samples.outlier_removal(
        setup_samples_df_with_outliers)
    np.array_equal(ref_samples.values, samples_outlier_removed.values)
