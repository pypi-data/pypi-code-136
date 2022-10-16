#===============================================================================
# bbprop.py
#===============================================================================

# Imports ======================================================================

from itertools import chain
from math import ceil, floor
from scipy.stats import fisher_exact
from bbpmf import betabinom_pmf




# Functions ====================================================================

def region(x: float, n0: int, n1: int, func='cdf', exhaustive=False):
    """Region of integration for bbprop_cdf or bbprop_test

    Parameters
    ----------
    x : float
        difference of proportions
    n0, n1 : int
        number of trials for the two samples
    func : str
        function to determine region for. should be "cdf" or "test".
    exhaustive : bool
        if set to true, check value in exhaustive mode

    Yields
    -------
    r0, r1
        tuple of coordinates
    """

    if func not in {'cdf', 'test'}:
        raise RuntimeError('invalid "func" option')

    if not exhaustive:
        if func == 'cdf':
            yield from (
                (r0, r1)
                for r0 in range(n0 + 1)
                for r1 in (
                    range(floor(n1/n0 * (r0 + x * n0)) + 1) if r0 < x * n0
                    else range(ceil(n1/n0 * (r0 - x * n0)), n1 + 1) if r0 > (1 - x) * n0
                    else range(
                        ceil(n1/n0 * (r0 - x * n0)),
                        floor(n1/n0 * (r0 + x * n0)) + 1
                    )
                )
            )
        elif func == 'test':
            yield from (
                (r0, r1)
                for r0 in range(n0 + 1)
                for r1 in (
                    range(ceil(n1/n0 * (r0 + x * n0)), n1 + 1) if r0 < x * n0
                    else range(floor(n1/n0 * (r0 - x * n0)) + 1) if r0 > (1 - x) * n0
                    else chain(
                        range(floor(n1/n0 * (r0 - x * n0)) + 1),
                        range(ceil(n1/n0 * (r0 + x * n0)), n1 + 1)
                    )
                )
            )
    else:
        if func == 'cdf':
            yield from (
                (r0, r1)
                for r0 in range(n0 + 1)
                for r1 in range(n1 + 1)
                if abs(r0*n1 - r1*n0) <= n1 * n0 * x
            )
        elif func == 'test':
            yield from (
                (r0, r1)
                for r0 in range(n0 + 1)
                for r1 in range(n1 + 1)
                if abs(r0*n1 - r1*n0) >= n1 * n0 * x
            )


def bbprop_cdf(x: float, n, a, b, exhaustive=False):
    """Cumulative distribution function for a difference of beta-binomial
    proportions

    Parameters
    ----------
    x
        difference of proportions
    n
        integer (or iterable of len 2) giving the number of trials
    a
        float (or iterable of len 2) giving the first shape parameter
    b
        float (or iterable of len 2) giving the second shape parameter

    Returns
    -------
    float
        the value of the CDF
    """

    if isinstance(n, int):
        n = n, n
    if isinstance(a, float) or isinstance(a, int):
        a = a, a
    if isinstance(b, float) or isinstance(b, int):
        b = b, b
    
    return sum(
        betabinom_pmf(r[0], n[0], a[0], b[0])
        * betabinom_pmf(r[1], n[1], a[1], b[1])
        for r in region(x, n[0], n[1], func='cdf', exhaustive=exhaustive)
    )


def bbprop_test(x: float, n, a, b, exhaustive=False):
    """Hypothesis test for a difference of beta-binomial proportions

    Parameters
    ----------
    x
        difference of proportions
    n
        integer (or iterable of len 2) giving the number of trials
    a
        float (or iterable of len 2) giving the first shape parameter
    b
        float (or iterable of len 2) giving the second shape parameter

    Returns
    -------
    float
        the p-value of the test
    """

    if isinstance(n, int):
        n = n, n
    if isinstance(a, float) or isinstance(a, int):
        a = a, a
    if isinstance(b, float) or isinstance(b, int):
        b = b, b
    
    return sum(
        betabinom_pmf(r[0], n[0], a[0], b[0])
        * betabinom_pmf(r[1], n[1], a[1], b[1])
        for r in region(x, n[0], n[1], func='test', exhaustive=exhaustive)
    )
