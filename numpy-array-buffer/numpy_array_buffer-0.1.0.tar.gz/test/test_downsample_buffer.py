#!/usr/bin/env python3
import pytest
import numpy as np
from numpy_array_buffer.downsampling_buffer import DownsamplingBuffer


@pytest.fixture
def example_buffer_1d():
    """create ring buffer that overwrites entries twice"""
    column_names = "x"
    downsampling_buffer = DownsamplingBuffer(4, 1, column_names=column_names)
    for i in range(9):
        downsampling_buffer.append(i)
    return downsampling_buffer


@pytest.fixture
def example_buffer_1d_pre_downsampling():
    """create ring buffer that overwrites entries twice"""
    column_names = ["x"]
    downsampling_buffer = DownsamplingBuffer(4, 1, column_names=column_names)
    for i in range(8):
        downsampling_buffer.append(i)
    return downsampling_buffer


@pytest.fixture
def example_buffer_2d():
    """create ring buffer that overwrites entries twice"""
    column_names = ["x", "y", "z"]
    downsampling_buffer = DownsamplingBuffer(4, 3, column_names=column_names)
    for i in range(9):
        downsampling_buffer.append([i, i + 100, i + 200])
    return downsampling_buffer


@pytest.fixture
def example_buffer_2d_pre_downsampling():
    """create ring buffer that overwrites entries twice"""
    column_names = ["x", "y", "z"]
    downsampling_buffer = DownsamplingBuffer(4, 3, column_names=column_names)
    for i in range(8):
        downsampling_buffer.append([i, i + 100, i + 200])
    return downsampling_buffer


class TestDunderMethods:
    def test_dunder_methods_1d(self, example_buffer_1d):
        expected_len = 3
        assert len(example_buffer_1d) == expected_len

        expected_array = np.array([0, 4, 8])
        assert np.array_equal(example_buffer_1d[:], expected_array)

    def test_dunder_len_1d(self, example_buffer_1d):
        expected_len = 3
        assert len(example_buffer_1d) == expected_len

    def test_dunder_len_2d(self, example_buffer_2d):
        expected_len = 3
        assert len(example_buffer_2d) == expected_len

    def test_dunder_iter_1d(self, example_buffer_1d):
        expected_list = [0, 4, 8]

        for val, expected in zip(example_buffer_1d, expected_list):
            assert val == expected

    def test_dunder_iter_2d(self, example_buffer_2d):
        expected_list = [
            [0.0, 100.0, 200.0],
            [4.0, 104.0, 204.0],
            [8.0, 108.0, 208.0],
        ]

        for val, expected in zip(example_buffer_2d, expected_list):
            # assert val == expected
            assert np.array_equal(val, expected)

    def test_dunder_get_array_1d(self, example_buffer_1d):
        expected_array = np.array([0.0, 4.0, 8.0])
        assert np.array_equal(example_buffer_1d[:], expected_array)

    def test_dunder_get_array_2d(self, example_buffer_2d):
        expected_array = np.array(
            [
                [0.0, 100.0, 200.0],
                [4.0, 104.0, 204.0],
                [8.0, 108.0, 208.0],
            ]
        )
        assert np.array_equal(example_buffer_2d[:], expected_array)

    def test_dunder_2d(self, example_buffer_2d):
        expected_array = np.array(
            [
                [0.0, 100.0, 200.0],
                [4.0, 104.0, 204.0],
                [8.0, 108.0, 208.0],
            ]
        )
        assert repr(example_buffer_2d) == f"{expected_array}"

    def test_dunder_str_2d(self, example_buffer_2d):
        assert (
            str(example_buffer_2d)
            == f"Downsampling buffer of buffer length: 4, rowlength: 3"
        )


class TestDownsampling:
    def test_first_downsampling(
        self,
    ):

        example_buffer = DownsamplingBuffer(4, 1)
        for i in range(4):
            example_buffer.append(i)

        assert np.array_equal(example_buffer[:], np.array([0.0, 1.0, 2.0, 3.0]))

        example_buffer.append(4)
        assert np.array_equal(example_buffer[:], np.array([0, 2, 4]))

    def test_second_downsampling(
        self,
    ):

        example_buffer = DownsamplingBuffer(4, 1)

        for i in range(8):
            example_buffer.append(i)
        assert np.array_equal(example_buffer[:], np.array([0.0, 2.0, 4.0, 6.0]))

        example_buffer.append(8)
        assert np.array_equal(example_buffer[:], np.array([0, 4, 8]))

    def test_third_downsampling(
        self,
    ):

        example_buffer = DownsamplingBuffer(4, 1)

        for i in range(16):
            example_buffer.append(i)

        assert np.array_equal(example_buffer[:], np.array([0.0, 4.0, 8.0, 12.0]))

        example_buffer.append(16)
        assert np.array_equal(example_buffer[:], np.array([0, 8, 16]))


class TestMethods:
    def test_get_array_1d(self, example_buffer_1d):
        expected_array = np.array([0.0, 4.0, 8.0])

        assert np.array_equal(example_buffer_1d.get_array(), expected_array)

    def test_get_array_2d(self, example_buffer_2d):
        expected_array = np.array(
            [
                [0.0, 100.0, 200.0],
                [4.0, 104.0, 204.0],
                [8.0, 108.0, 208.0],
            ]
        )

        assert np.array_equal(example_buffer_2d.get_array(), expected_array)

    def test_downsample_array_get_array_not_full(
        self,
    ):
        column_names = ["x", "y", "z"]
        downsampling_buffer = DownsamplingBuffer(6, 3, column_names=column_names)
        for i in range(3):
            downsampling_buffer.append([i, i + 100, i + 200])
        expected_data = np.array(
            [
                [0.0, 100.0, 200.0],
                [1.0, 101.0, 201.0],
                [2.0, 102.0, 202.0],
            ]
        )
        assert np.array_equal(expected_data, downsampling_buffer.get_array())

    def test_downsample_array_get_col_2d(self, example_buffer_2d):
        expected_col = np.array([0.0, 4.0, 8.0])
        assert np.array_equal(expected_col, example_buffer_2d.get_col("x"))

    def test_downsample_array_get_col_1d(self, example_buffer_1d):
        expected_col = np.array([0.0, 4.0, 8.0])
        assert np.array_equal(expected_col, example_buffer_1d.get_col("x"))

    def test_downsample_array_get_array_full(self, example_buffer_2d):
        expected_data = np.array(
            [
                [0.0, 100.0, 200.0],
                [4.0, 104.0, 204.0],
                [8.0, 108.0, 208.0],
            ]
        )
        assert np.array_equal(expected_data, example_buffer_2d.get_array())

    def test_add_dict(self, example_buffer_2d_pre_downsampling):
        data_dict = {"x": 10.0, "y": 11.0, "z": 12.0}
        example_buffer_2d_pre_downsampling.add_dict(data_dict)
        expected_data = np.array(
            [
                [0.0, 100.0, 200.0],
                [4.0, 104.0, 204.0],
                [10.0, 11.0, 12.0],
            ]
        )
        assert np.array_equal(
            expected_data, example_buffer_2d_pre_downsampling.get_array()
        )

    def test_add_unordered_dict(self, example_buffer_2d_pre_downsampling):
        data_dict = {"y": 11.0, "z": 12.0, "x": 10.0}
        example_buffer_2d_pre_downsampling.add_dict(data_dict)
        expected_data = np.array(
            [
                [0.0, 100.0, 200.0],
                [4.0, 104.0, 204.0],
                [10.0, 11.0, 12.0],
            ]
        )
        assert np.array_equal(
            expected_data, example_buffer_2d_pre_downsampling.get_array()
        )

    def test_add_unordered_dict_exception(self, example_buffer_2d):
        data_dict = {"y": 11.0, "z": 12.0, "f": 10.0}
        with pytest.raises(Exception) as exception_info:
            example_buffer_2d.add_dict(data_dict)
        assert str(exception_info.value) == "Could not parse data dict"


class TestExceptions:
    def test_constructor_exception(
        self,
    ):
        """Test uneven array, cannot downsample"""
        with pytest.raises(Exception) as exception_info:
            downsampling_buffer = DownsamplingBuffer(
                5, 2, column_names=["first", "second"]
            )
        assert str(exception_info.value) == "array_len needs to be even"

    def test_downsample_array_mismatch_exception(
        self,
    ):
        """inconsistent column names and width"""
        column_names = ["x", "y", "z"]
        with pytest.raises(Exception) as exception_info:
            downsampling_buffer = DownsamplingBuffer(10, 2, column_names=column_names)
        assert (
            str(exception_info.value) == "Length of column names does not match width"
        )

    def test_downsample_array_add_data_exception(self, example_buffer_2d):
        """inconsistent data to column"""
        with pytest.raises(Exception) as exception_info:
            example_buffer_2d.append([0, 1])
        assert str(exception_info.value) == "wrong data format"

    def test_downsample_array_get_invalid_col(self, example_buffer_2d):
        with pytest.raises(Exception) as exception_info:
            example_buffer_2d.get_col("invalid_col")
        assert str(exception_info.value) == "Invalid column name"

    def test_clear_buffer(self, example_buffer_2d):

        example_buffer_2d.clear()
        expected_array = np.empty(shape=(0, 3), dtype=np.float64)
        # print(f"{expected_array = }")
        assert np.array_equal(example_buffer_2d[:], expected_array)
