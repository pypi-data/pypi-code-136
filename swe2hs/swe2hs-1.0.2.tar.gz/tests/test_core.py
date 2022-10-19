import pytest
import numpy as np

from swe2hs._core import (
    _adjust_rho_max_based_on_overburden,
    _adjust_rho_max_wet_snowpack,
    _calculate_overburden,
    _pad_end_of_array_with_zero,
    _pad_layer_arrays_with_zero,
    _remove_swe_from_top,
)


@pytest.mark.parametrize(
    "rho_max_layers_in, overburden_layers_in, swe_layers_in, rho_max_init_in, rho_max_end_in, sigma_max_in, rho_max_layers_expected",
    [(np.array([400, 420, 400, 420, 460, 400, 420, 400, 420, 500, 500, 500, 420], dtype='float64'),
      np.array([0,  0,  0.5, 0.5, 0.5, 1,  1,  1.5,
               1.5,  0,  1,  1, 1.5], dtype='float64'),
      np.array([1,  1,    1,  1,  1, 1,  1,    1,  1,  1,  1,  1,  0], dtype='float64'),
      400.,
      500.,
      1.,
      np.array([400, 420, 450, 450, 460, 500, 500, 500,
               500, 500, 500, 500,  0], dtype='float64')
      ),
     ]
)
def test_adjust_rho_max_based_on_overburden(
    rho_max_layers_in,
    overburden_layers_in,
    swe_layers_in,
    rho_max_init_in,
    rho_max_end_in,
    sigma_max_in,
    rho_max_layers_expected
):
    rho_max_layers_out = _adjust_rho_max_based_on_overburden(
        rho_max_layers_in,
        overburden_layers_in,
        swe_layers_in,
        rho_max_init_in,
        rho_max_end_in,
        sigma_max_in
    )
    np.testing.assert_almost_equal(rho_max_layers_out, rho_max_layers_expected)


@pytest.mark.parametrize(
    "rho_max_layers_in, swe_layers_in, rho_max_end_in, v_melt_in, rho_max_layers_expected",
    [(np.array([400, 400, 400], dtype='float64'),
      np.array([1, 0.1, 0], dtype='float64'),
      np.array([500, 500, 500], dtype='float64'),
      0.5,
      np.array([439.34693402873665, 439.34693402873665, 400], dtype='float64')
      ),
     ]
)
def test_adjust_rho_max_wet_snowpack(
    rho_max_layers_in,
    swe_layers_in,
    rho_max_end_in,
    v_melt_in,
    rho_max_layers_expected
):
    rho_max_layers_out = _adjust_rho_max_wet_snowpack(
        rho_max_layers_in,
        swe_layers_in,
        rho_max_end_in,
        v_melt_in
    )
    np.testing.assert_almost_equal(rho_max_layers_out, rho_max_layers_expected)


@pytest.mark.parametrize(
    "swe_layers_in, overburden_layers_expected",
    [
        (np.array([1, 1, 1, 1, 1, 1, 0, 0], dtype='float64'), np.array(
            [5.5, 4.5, 3.5, 2.5, 1.5, 0.5, 0, 0], dtype='float64')),
        (np.array([1, 1, 0, 0, 1, 1, 0, 0], dtype='float64'), np.array(
            [3.5, 2.5, 2, 2, 1.5, 0.5, 0, 0], dtype='float64')),
        (np.array([0, 0, 0, 0, 0], dtype='float64'),
         np.array([0, 0, 0, 0, 0], dtype='float64')),
        (np.array([0, 0, 0, 0, 2], dtype='float64'),
         np.array([2, 2, 2, 2, 1], dtype='float64')),
        (np.array([2, 0, 0, 0, 0], dtype='float64'),
         np.array([1, 0, 0, 0, 0], dtype='float64')),
    ],
)
def test_calculate_overburden(swe_layers_in, overburden_layers_expected):
    np.testing.assert_almost_equal(
        _calculate_overburden(swe_layers_in),
        overburden_layers_expected
    )


@pytest.mark.parametrize(
    "swe_layers_in, delta_swe, swe_layers_expected",
    [
        (np.array([1, 1, 1, 1, 1, 1, 0, 0], dtype='float64'), -1.5,
         np.array([1, 1, 1, 1, 0.5, 0, 0, 0], dtype='float64')),
        (np.array([1, 1, 1, 1, 1, 1, 1, 1], dtype='float64'), -1.5,
         np.array([1, 1, 1, 1, 1, 1, 0.5, 0], dtype='float64')),
        (np.array([1, 1, 1, 1, 1, 0, 0, 1], dtype='float64'), -2.5,
         np.array([1, 1, 1, 0.5, 0, 0, 0, 0], dtype='float64')),
        (np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype='float64'), -2.8,
         np.array([0.2, 0, 0, 0, 0, 0, 0, 0], dtype='float64')),
        (np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype='float64'), -
         3.5, np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='float64')),
        (np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype='float64'), 3.0,
         np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype='float64')),
        (np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype='float64'), 0.0,
         np.array([1, 1, 1, 0, 0, 0, 0, 0], dtype='float64')),
    ],
)
def test_remove_swe_from_top(swe_layers_in, delta_swe, swe_layers_expected):
    swe_layers_out = _remove_swe_from_top(swe_layers_in, delta_swe)
    np.testing.assert_almost_equal(swe_layers_out, swe_layers_expected)


@pytest.mark.parametrize(
    "input, expected",
    [
        (np.array([1], dtype='float64'), np.array([1, 0], dtype='float64')),
        (np.array([], dtype='float64'), np.array([0], dtype='float64')),
        (np.array([1., 2., 3., 4.], dtype='float64'),
         np.array([1., 2., 3., 4., 0.], dtype='float64')),
    ]
)
def test_pad_end_of_array_with_zero(
    input,
    expected
):
    out = _pad_end_of_array_with_zero(input)
    np.testing.assert_equal(out, expected)


def test_pad_layer_arrays_with_zero(model_state_arrays):
    swe_layers, rho_layers, rho_max_layers = model_state_arrays
    swe_layers_nb, rho_layers_nb, rho_max_layers_nb = _pad_layer_arrays_with_zero(
        swe_layers,
        rho_layers,
        rho_max_layers
    )

    swe_layers_np = np.pad(swe_layers, (0, 1))
    rho_layers_np = np.pad(rho_layers, (0, 1))
    rho_max_layers_np = np.pad(rho_max_layers, (0, 1))

    np.testing.assert_almost_equal(swe_layers_nb, swe_layers_np)
    np.testing.assert_almost_equal(rho_layers_nb, rho_layers_np)
    np.testing.assert_almost_equal(rho_max_layers_nb, rho_max_layers_np)
