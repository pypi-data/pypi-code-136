from numpy_array_buffer.ring_buffer import RingBuffer
import pytest
import numpy as np


@pytest.fixture
def example_buffer_1d():
    """create ring buffer of scalar value that overwrites entries twice"""
    column_names = ["latency_queue"]
    ring_buffer = RingBuffer(3, 1, column_names=column_names)
    for i in range(5):
        ring_buffer.append(i)

    return ring_buffer


@pytest.fixture
def example_buffer_2d():
    """create ring buffer with array of [x,y,z] that overwrites entries twice"""
    column_names = ["x", "y", "z"]
    ring_buffer = RingBuffer(3, 3, column_names=column_names)
    for i in range(5):
        ring_buffer.append([i, i + 100, i + 200])

    return ring_buffer


class TestDunderMethods:
    def test_dunder_len_1d(
        self,
    ):

        example_buffer_1d = RingBuffer(3, 1)
        expected_len = 0
        assert len(example_buffer_1d) == expected_len

        example_buffer_1d.append(0)
        expected_len = 1
        assert len(example_buffer_1d) == expected_len

        example_buffer_1d.append(1)
        expected_len = 2
        assert len(example_buffer_1d) == expected_len

        example_buffer_1d.append(2)
        expected_len = 3
        assert len(example_buffer_1d) == expected_len

        example_buffer_1d.append(3)
        expected_len = 3
        assert len(example_buffer_1d) == expected_len

    def test_dunder_len_2d(
        self,
    ):

        example_buffer_2d = RingBuffer(3, 2)
        expected_len = 0
        assert len(example_buffer_2d) == expected_len

        example_buffer_2d.append([0, 10])
        expected_len = 1
        assert len(example_buffer_2d) == expected_len

        example_buffer_2d.append([1, 11])
        expected_len = 2
        assert len(example_buffer_2d) == expected_len

        example_buffer_2d.append([2, 12])
        expected_len = 3
        assert len(example_buffer_2d) == expected_len

        example_buffer_2d.append([3, 13])
        expected_len = 3
        assert len(example_buffer_2d) == expected_len

    def test_dunder_array_1d(self, example_buffer_1d):
        expected_array = np.array([2, 3, 4])
        assert np.array_equal(example_buffer_1d[:], expected_array)

    def test_dunder_index(self, example_buffer_1d):
        expected_value = 2
        assert example_buffer_1d[0] == expected_value

    def test_dunder_index_last(self, example_buffer_1d):
        expected_value = 4
        assert example_buffer_1d[-1] == expected_value

    def test_dunder_index_missing(
        self,
    ):
        example_buffer_1d = RingBuffer(4, 1)
        with pytest.raises(Exception) as exception_info:
            last_val = example_buffer_1d[-1]
        expected_error = "index -1 is out of bounds for axis 0 with size 0"
        assert str(exception_info.value) == expected_error

    def test_dunder_array_2d(self, example_buffer_2d):

        expected_array = np.array(
            [[2.0, 102.0, 202.0], [3.0, 103.0, 203.0], [4.0, 104.0, 204.0]]
        )
        assert np.array_equal(example_buffer_2d[:], expected_array)

    def test_dunder_repr(self, example_buffer_2d):
        assert repr(example_buffer_2d) == (
            f"RingBuffer(buffer_length={example_buffer_2d.buffer_length}, width={example_buffer_2d.width}, "
            f"dtype={example_buffer_2d.dtype}, column_names={example_buffer_2d.column_names}, "
            f"initial_data=np.array({example_buffer_2d.get_array()})"
        )

    def test_dunder_str(self, example_buffer_2d):
        assert str(example_buffer_2d) == f"RingBuffer of dim: 3x3, curr_idx: 2"

    def test_dunder_array(self, example_buffer_2d):

        expected_data = np.array(
            [
                [3.0, 103.0, 203.0],
                [4.0, 104.0, 204.0],
            ]
        )

        assert np.array_equal(example_buffer_2d[1:3], expected_data)

    def test_dunder_getitem_1d(self, example_buffer_1d):
        expected_list = [2, 3, 4]

        for val, expected in zip(example_buffer_1d, expected_list):
            assert val == expected

    def test_dunder_getitem_2d(self, example_buffer_2d):
        expected_list = [[2.0, 102.0, 202.0], [3.0, 103.0, 203.0], [4.0, 104.0, 204.0]]
        for val, expected in zip(example_buffer_2d, expected_list):
            assert np.array_equal(val, expected)


class TestMethods:
    def test_initial_data(
        self,
    ):
        length = 5
        example_buffer_1d = RingBuffer(
            buffer_length=length, width=1, initial_data=np.arange(10)
        )
        assert np.allclose(example_buffer_1d.get_array(), np.arange(10)[-length:])

    def test_1d_mean_method(self, example_buffer_1d):

        assert example_buffer_1d.mean() == 3.0
        buf = list(example_buffer_1d)

    def test_2d_mean_method(self, example_buffer_2d):
        expected_array = np.array([3.0, 103.0, 203.0])
        assert np.array_equal(example_buffer_2d.mean(), expected_array)

        assert len(example_buffer_2d) == 3

    def test_add_dict(self, example_buffer_2d):
        data_dict = {"x": 10.0, "y": 11.0, "z": 12.0}
        example_buffer_2d.add_dict(data_dict)
        expected_data = np.array(
            [[3.0, 103.0, 203.0], [4.0, 104.0, 204.0], [10.0, 11.0, 12.0]]
        )
        assert np.array_equal(expected_data, example_buffer_2d.get_array())

    def test_add_unordered_dict(self, example_buffer_2d):
        data_dict = {"y": 11.0, "z": 12.0, "x": 10.0}
        example_buffer_2d.add_dict(data_dict)
        expected_data = np.array(
            [[3.0, 103.0, 203.0], [4.0, 104.0, 204.0], [10.0, 11.0, 12.0]]
        )
        assert np.array_equal(expected_data, example_buffer_2d.get_array())

    def test_get_array_2d(self, example_buffer_2d):
        expected_array = np.array(
            [[2.0, 102.0, 202.0], [3.0, 103.0, 203.0], [4.0, 104.0, 204.0]]
        )
        assert np.array_equal(example_buffer_2d.get_array(), expected_array)

    def test_get_array_not_full(
        self,
    ):
        column_names = ["x", "y", "z"]
        ring_buffer = RingBuffer(5, 3, column_names=column_names)
        for i in range(3):
            ring_buffer.append([i, i + 100, i + 200])
        expected_data = np.array(
            [
                [0.0, 100.0, 200.0],
                [1.0, 101.0, 201.0],
                [2.0, 102.0, 202.0],
            ]
        )
        assert np.array_equal(expected_data, ring_buffer.get_array())

    def test_get_array_full(self, example_buffer_2d):
        expected_data = np.array(
            [
                [2.0, 102.0, 202.0],
                [3.0, 103.0, 203.0],
                [4.0, 104.0, 204.0],
            ]
        )
        assert np.array_equal(expected_data, example_buffer_2d.get_array())

    def test_get_col(self, example_buffer_2d):
        expected_col = np.array([2.0, 3.0, 4.0])
        assert np.array_equal(expected_col, example_buffer_2d.get_col("x"))

    def test_clear_buffer(self, example_buffer_2d):

        example_buffer_2d.clear()
        expected_array = np.empty(shape=(0, 3), dtype=np.float64)
        assert np.array_equal(example_buffer_2d[:], expected_array)


class TestNumpyMethods:
    def test_np_mean_2d(self, example_buffer_2d):
        expected_data = np.array(
            [
                [2.0, 102.0, 202.0],
                [3.0, 103.0, 203.0],
                [4.0, 104.0, 204.0],
            ]
        )
        mean_val = np.mean(example_buffer_2d, axis=0)
        assert np.array_equal(mean_val, np.mean(expected_data, axis=0))

        sum_val = np.sum(example_buffer_2d, axis=0)
        assert np.array_equal(sum_val, np.sum(expected_data, axis=0))

    def test_np_mean_1d(self, example_buffer_1d):
        expected_data = np.array([2.0, 3.0, 4.0])
        mean_val = np.mean(example_buffer_1d)
        assert mean_val == np.mean(expected_data)

    def test_np_mean_1d_empty(
        self,
    ):
        empty_buffer = RingBuffer(3, 1)

        with pytest.warns(Warning):
            assert np.isnan(np.mean(empty_buffer))

    def test_np_mean_1d_single_val(
        self,
    ):
        empty_buffer = RingBuffer(3, 1)

        empty_buffer.append(0)
        assert np.mean(empty_buffer) == 0.0


class TestExceptions:
    def test_col_get_invalid_exception(self, example_buffer_2d):
        with pytest.raises(Exception) as exception_info:
            example_buffer_2d.get_col("invalid_col")
        assert str(exception_info.value) == "Invalid column name"

    def test_add_unordered_dict_exception(self, example_buffer_2d):
        data_dict = {"y": 11.0, "z": 12.0, "f": 10.0}
        with pytest.raises(Exception) as exception_info:
            example_buffer_2d.add_dict(data_dict)
        assert str(exception_info.value) == "Could not parse data dict"

    def test_mismatch_exception(
        self,
    ):
        """inconsistent column names and width"""
        column_names = ["x", "y", "z"]
        with pytest.raises(Exception) as exception_info:
            ring_buffer = RingBuffer(10, 2, column_names=column_names)
        assert (
            str(exception_info.value) == "Length of column names does not match width"
        )

    def test_add_data_exception(self, example_buffer_2d):
        # inconsistent data to column
        with pytest.raises(Exception) as exception_info:
            example_buffer_2d.append([0, 1])
        assert str(exception_info.value) == "wrong data format"
