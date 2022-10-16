#===============================================================================
# betabinom_pmf.py
#===============================================================================

# Imports ======================================================================

from scipy.special import comb
from scipy.special import beta as beta_function




# Functions ====================================================================

def betabinom_pmf(k, n, a, b):
    """Probability mass function for a beta binomial distribution

    Parameters
    ----------
    k : int
        number of successes
    n : int
        number of trials
    a : float
        first (positive) shape parameter
    b : float
        second (positive) shape parameter

    Returns
    -------
    float
        the probability mass
    """

    return comb(n, k) * beta_function(k + a, n - k + b) / beta_function(a, b)
