import pytest

from micropsi_challenge import get_first_local_minima


@pytest.fixture
def empty_lst() -> list[int]:
    return []


@pytest.fixture
def lst_with_single_element() -> list[int]:
    return [1]


@pytest.fixture
def lst_with_proper_data() -> list[int]:
    return [2, 1, 2, 3]


@pytest.fixture
def lst_with_monotonically_ascending_data() -> list[int]:
    return [1, 2, 3]


@pytest.fixture
def lst_with_monotonically_descending_data() -> list[int]:
    return [3, 2, 1]


def test_empty_list(empty_lst):
    with pytest.raises(IndexError):
        get_first_local_minima(empty_lst)


def test_single_element(lst_with_single_element):
    assert get_first_local_minima(lst_with_single_element) == 1


def test_proper_data(lst_with_proper_data):
    assert get_first_local_minima(lst_with_proper_data) == 1


def test_monotonically_ascending_data(lst_with_monotonically_ascending_data):
    assert get_first_local_minima(lst_with_monotonically_ascending_data) == 1


def test_monotonically_descending_data(lst_with_monotonically_descending_data):
    assert get_first_local_minima(lst_with_monotonically_descending_data) == 1
