import pytest


def pytest_on_path(path: str, test_func: str = None):
    """Given a filepath, run pytest"""
    if test_func:
        path = f"{path}::{test_func}"
    print("pytest_on_path", "path", path)
    return pytest.main([path])
