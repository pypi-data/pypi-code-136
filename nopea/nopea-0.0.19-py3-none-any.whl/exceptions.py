#!/usr/bin/env python
# coding: utf-8


class TooManyResultsError(Exception):
    error_code = 1
    pass


class MaxLengthError(Exception):
    error_code = 1
    pass


class UnknownFieldError(Exception):
    error_code = 1
    pass
