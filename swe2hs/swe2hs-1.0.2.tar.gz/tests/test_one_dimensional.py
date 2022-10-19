import pytest
import numpy as np
import pandas as pd

from swe2hs.one_dimensional import convert_1d


def test_zeros_at_correct_positions(valid_swe_sample_data):
    swe2hs_result = convert_1d(valid_swe_sample_data, return_layers=True)

    np.testing.assert_array_equal(
        valid_swe_sample_data.to_numpy().nonzero(),
        swe2hs_result['hs'].to_numpy().nonzero()
    )

    np.testing.assert_array_equal(
        valid_swe_sample_data.to_numpy().nonzero(),
        swe2hs_result['layer_heights'].sum(dim='layers').to_numpy().nonzero() 
    )


def test_cumulative_layer_height_against_hs(valid_swe_sample_data):
    swe2hs_result = convert_1d(valid_swe_sample_data, return_layers=True)
    pd.testing.assert_series_equal(
        swe2hs_result['hs'].to_pandas(),
        swe2hs_result['layer_heights'].sum(dim='layers').to_pandas()
    )

@pytest.mark.parametrize(
    "swe_unit",
    [("m"), ("cm"), ("mm")]
)
@pytest.mark.parametrize(
    "hs_unit",
    [("m"), ("cm"), ("mm")]
)
def test_with_and_without_layers_return_types(
    valid_swe_sample_data,
    swe_unit,
    hs_unit,
):
    without_layers = convert_1d(
        valid_swe_sample_data,
        return_layers=False,
        swe_input_unit=swe_unit,
        hs_output_unit=hs_unit,
    )
    
    with_layers = convert_1d(
        valid_swe_sample_data,
        return_layers=True,
        swe_input_unit=swe_unit,
        hs_output_unit=hs_unit,
    )

    pd.testing.assert_series_equal(
        without_layers,
        with_layers['hs'].to_pandas(),
        check_names=False,  # index name can be different to "time"
        check_freq=False,  # roundtrip through xarray looses frequency
    )