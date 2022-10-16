"""Test runner.

Two ways to run tests:

1. To run all tests::

    python tests

2. To run a specific test::

    python -m tornado.testing tests.test_module_name

"""
import os
import unittest


TEST_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(TEST_DIR)
    runner = unittest.TextTestRunner()
    runner.run(suite)
