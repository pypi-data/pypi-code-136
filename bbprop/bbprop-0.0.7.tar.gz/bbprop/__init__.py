"""This package provides a statistical test for the difference of beta-binomial
proportions.


Functions
---------
bbprop_cdf
    cumulative distribution function for difference of beta-binomial proportions
bbprop_test
    hypothesis test for difference of beta-binomial proportions


Examples
--------

```python
from bbprop import bbprop_cdf, bbprop_test
help(bbprop_cdf)
help(bbprop_test)
bbprop_cdf(0.1, [30, 12], [4, 5], [6, 5])
bbprop_test(0.1, [30, 12], [4, 5], [6, 5])
```


Notes
-----

The aim of the test is to determine whether two values drawn from beta-binomial
distributions are significantly different from one another.

The null hypothesis of the test is that two random variables `B0` and `B1` have
beta-binomial distribtions with parameters `theta0 = (n0, alpha0, beta0)` and
`theta1 = (n1, alpha1, beta1)`, respectively.

The test statistic is the value `x = abs(b0/n0 - b1/n1)` where `b0` and `b1`
are the number of successes drawn from `B0` and `B1`.

The p-value is then the probability that `x` is greater than or equal to its
observed value, given the predefined null distribution.
"""

from bbprop.bbprop import bbprop_cdf
from bbprop.bbprop import bbprop_test
