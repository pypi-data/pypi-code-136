import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import poisson
from .utility import (gammaGetShapeRate, negbinomGetSizeProb,
                                betaGetShapes, evalWith, parseCatFormula,
                                parseUnifFormula)
from patsy.splines import bs

def trtAssign(dtName: pd.DataFrame, nTrt=2, balanced=True, strata=None,
              grpName="trtGrp", ratio=None):
    """assign treatment groups

    Args:
        dtName (_type_): _description_
        nTrt (int, optional): _description_. Defaults to 2.
        balanced (bool, optional): _description_. Defaults to True.
        strata (_type_, optional): _description_. Defaults to None.
        grpName (str, optional): _description_. Defaults to "trtGrp".
        ratio (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    # TODO implement these asserts
    # assertNotMissing(dtName = missing(dtName))
    # assertNotInDataTable(grpName, dtName)
    dt = dtName.copy()

    if ratio is not None:
        if isinstance(ratio, list):
            assert len(ratio) == nTrt, "Lengths of ratios and"
            +"number of treaments should be equal"
        elif isinstance(ratio, int):
            assert ratio == nTrt, "Lengths of ratios and"
            +"number of treaments should be equal"
            # dt = dtName.copy()
    if balanced:
        if strata is None:
            dt['strata_num'] = [1] * dt.shape[0]
        else:
            dt = addStrataCode(dt, strata)

        dt = dt.merge(dt['strata_num'].value_counts().reset_index().
                      rename({'index': 'strata_num', 'strata_num': '_n'},
                      axis=1))

        dt[grpName] = stratSamp(dt.shape[0], ncat=nTrt, ratio=None)
        dt = dt.drop(['_n', 'strata_num'], axis=1)
    else:
        if ratio is None:
            if nTrt == 2:
                formula = 0.5
            else:
                formula = list(np.repeat(1/nTrt, nTrt))

        dt = trtObserve(dt, formulas=formula, logit_link=False,
                        grpName=grpName)

    return dt


def generate(args, n, dfSim, idname):
    """_summary_
    args is a pd row representing a row from a data definition
    Args:
        args (_type_): _description_
        n (_type_): _description_
        dfSim (_type_): _description_
        idname (_type_): _description_
    """
    if args['dist'] == 'beta':
        newColumn = genbeta(
                    n=n,
                    formula=args['formula'],
                    precision=args['variance'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),
    elif args['dist'] == 'binary':
        newColumn = genbinom(
                    n=n,
                    formula=args['formula'],
                    size=1,
                    link=args['link'],
                    dtSim=dfSim.copy(),
                )
    elif args['dist'] == 'binomial':
        newColumn = genbinom(
                    n=n,
                    formula=args['formula'],
                    size=args['variance'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                )

    elif args['dist'] == 'categorical':
        newColumn = gencat(
                    n=n,
                    formula=args['formula'],
                    variance=args['variance'],
                    # link=args['link'], ## we are not implenting the link for this for now!!
                    dtSim=dfSim.copy(),
                    ),
    elif args['dist'] == 'exponential':
        newColumn = genexp(
                    n=n,
                    formula=args['formula'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),
    elif args['dist'] == 'gamma':
        newColumn = gengamma(
                    n=n,
                    formula=args['formula'],
                    dispersion=args['variance'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),
    elif args['dist'] == 'mixture':
        newColumn = genmixture(
            n=n,
            formula=args['formula'],
            dtSim=dfSim.copy(),
            ),

    elif args['dist'] == 'negBinomial':
        newColumn = gennegbinom(
                    n=n,
                    formula=args['formula'],
                    variance=args['variance'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),

    elif args['dist'] == 'nonrandom':
        newColumn = gendeterm(
                    n=n,
                    formula=args['formula'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),

    elif args['dist'] == 'normal':
        newColumn = gennorm(
                    n=n,
                    formula=args['formula'],
                    variance=args['variance'],
                    # link=args['link'],
                    dtSim=dfSim.copy(),
                    ),
    
    elif args['dist'] == 'lognormal':
        newColumn = genlognorm(
                    n=n,
                    formula=args['formula'],
                    variance=args['variance'],
                    # link=args['link'],
                    dtSim=dfSim.copy(),
                    ),

    elif args['dist'] == 'noZeroPoisson':
        newColumn = genpoisTrunc(
                    n=n,
                    formula=args['formula'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),

    elif args['dist'] == 'poisson':
        newColumn = genpois(
                    n=n,
                    formula=args['formula'],
                    link=args['link'],
                    dtSim=dfSim.copy(),
                    ),

    elif args['dist'] == 'trtAssign':
        newColumn = genAssign(
                    dtName=dfSim.copy(),
                    grpName=args['varname'],
                    strata=args['variance'],
                    ratio=args['formula'],
                    balanced=args['link']
                    ),

    elif args['dist'] == 'uniform':
        newColumn = genunif(
                    n=n,
                    formula=args['formula'],
                    dtSim=dfSim.copy(),
                    ),

    elif args['dist'] == 'uniformInt':
        newColumn = genUnifInt(
                    n=n,
                    formula=args['formula'],
                    dtSim=dfSim.copy(),
                    ),
    else:
        raise Exception("not a valid distribution. Please check spelling.")

    # newcolumn is sometimes returned as a tuple, with the array at index 0
    # this grabs the array from within the tuple to avoid errors
    if len(newColumn) == 1:
        newColumn = pd.Series(data=np.squeeze(newColumn[0]),
                              name=args['varname'])
    else:
        newColumn = pd.Series(data=newColumn, name=args['varname'])

    # Create data frame
    if dfSim is None:
        # TODO: check if this works
        dfNew = pd.DataFrame(newColumn)
    else:
        dfNew = pd.concat([dfSim.reset_index(drop=True), newColumn], axis=1)

    return dfNew


def genbasisdt(x, knots, degree, theta):
    """
    # Internal function called by viewSplines, viewBasis,
    # and genSplines - function returns a list object
    # @param x The support of the function
    # @param knots The cutpoints of the spline function
    # @param degree The polynomial degree of curvature
    # @param theta A vector of coefficents/weights
    # @return A list that includes a data.table with x and y values,
    # a matrix of basis values (basis functions), the knots, and degree

    Args:
        x (_type_): _description_
        knots (_type_): _description_
        degree (_type_): _description_
        theta (_type_): _description_
    """
    reqparam = len(knots) + degree + 1
    if len(theta) != reqparam:
        raise Exception("Number of specified paramaters (theta) not correct. \
                        Needs to be " + str(reqparam))

    # if (!all(theta <= 1)) {
    if not all(i <= 1 for i in theta):
        if sum([i > 1 for i in theta] == 1):
            valueS = " value of theta exceeds 1.00"
        else:
            valueS = " values of theta exceed 1.00"

        raise Exception(str(sum([i > 1 for i in theta]))+valueS)

    # if (!is.null(knots) & !all(knots < 1) & !all(knots > 0))
    if knots is not None and not all([i < 1 for i in knots]) \
       and not all([i > 0 for i in knots]):
        raise Exception("All knots must be between 0 and 1")

    basis = bs(x=x, knots=knots, degree=degree, lower_bound=0,
               upper_bound=1, include_intercept=True,)

    y_spline = basis @ theta

    dt = pd.DataFrame({'x': x, 'y_spline': y_spline})

    return(dt, basis, knots, degree)


def genbeta(n, formula, precision, dtSim, link="identity",):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        precision (_type_): _description_
        dtSim (_type_): _description_
        link (str, optional): _description_. Defaults to "identity".
    """

    mean, precision = evalWith(formula=formula, variance=precision,
                               dtSim=dtSim.copy(), link=link)

    sr = betaGetShapes(mean=mean, precision=precision)

    new = np.random.beta(a=sr['shape1'], b=sr['shape2'], size=n)

    return new


def genbinom(n: int, formula: str, size: int, link: str, dtSim: pd.DataFrame):
    """generate binomial distribution of data

    Careful not to be confused!
    When calling np.random.binomial, n is the number of trials
    not the number of datapoints to generate!
    But the argument n to genbinom represents the number
    of datapoints to generate.

    Args:
        n (int): Number of data points to generate
        formula (str): 
        size (int): Number of trials to conduct. Defaults to 1
        NB: This gets passed into the 'variance' column of the
        data definitions table.
        link (str): _description_
        dtSim (DataFrame): _description_
    """
    p, _ = evalWith(formula=formula, dtSim=dtSim, link=link)

    # TODO: Double check this
    p = np.where(p > 1, 1, np.where(p < 0, 0, p))

    return np.random.binomial(n=size, p=p, size=n)


def gendeterm(n: int, formula, link, dtSim):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        link (_type_): _description_
        dtSim (_type_): _description_
    """

    num, _ = evalWith(formula=formula, dtSim=dtSim.copy(), link=link)

    generatedColumn = np.random.normal(loc=num, scale=0,
                                       size=n)

    return generatedColumn


def genexp(n, formula, dtSim, link="identity"):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        dtSim (_type_): _description_
        link (str, optional): _description_. Defaults to "identity".
    """
    mean, _ = evalWith(formula=formula, link=link,
                       dtSim=dtSim.copy())

    new = np.random.exponential(scale=mean, size=n)
    return new


def gengamma(n, formula, dispersion, dtSim, link="identity"):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        dispersion (_type_): _description_
        dtSim (_type_): _description_
        link (str, optional): _description_. Defaults to "identity".
    """

    mean, dispersion = evalWith(formula, dtSim=dtSim.copy(),
                                variance=dispersion)

    sr = gammaGetShapeRate(mean=mean, dispersion=dispersion)

    generatedColumn = np.random.gamma(shape=sr['shape'],
                                      scale=sr['rate'],
                                      size=n)

    return generatedColumn


def genunif(n, formula, dtSim):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        dtSim (_type_): _description_

    Returns:
        _type_: _description_
    """

    uMin, uMax = parseUnifFormula(formula, dtSim, n)

    generatedColumn = [round(i, 2) for i in np.random.uniform(low=uMin,
                       high=uMax, size=n)]

    return generatedColumn

def genmixture(n, formula, dtSim):
    """ Internal function called by generate function

    Internal function called by the generate function
    when ('dist' == mixture) in a data definition. Creates
    a distribution of values based on specified formula input.

    Args:
        n (int): number of observations to produce

        formula (string): string holding distribution
        for output. example format is:
        "x1 | .3 + x2 | .4 + x3 | .3"
        In this format, variables are followed by their desired
        output quantity. The above example shows x1 having an
        output quantity of .3, meaning that .3 of the resulting
        distribution will be sourced from the x1 variable. All
        variables output quantities should equal to 1.

        dtSim (dataframe): data frame holding data definitions

    Returns:
        Variable with a distribution of values derived from
        formula.
    """

    probs = [np.float(pair.split("|")[1]) for pair in formula.split("+")]
    vars = [pair.split("|")[0] for pair in formula.split("+")]

    if len(probs) != len(vars):
        raise Exception("Mixture Definition must have the same amount"
                        + "of variables and probabilites")

    if sum(probs) != 1:
        raise Exception('Given probabilities do not sum to 1!')

    generatedColumn = dtSim.apply(lambda x: np.random.choice(x, p=probs),
                                  axis=1)

    return generatedColumn


def gencat(n: int, formula: str, variance: list, dtSim: pd.DataFrame):
    """
    Generates Categorical data.

    Note that if the past probabities do not sum to 1 (i.e. ".33, .33")
    a new category will be appended with prob = 1-sum(probs)

    Args:
        n (int): number of rows to generate
        formula (str): contains the distribution of desired categories
        variance (list): for categorical data, we set the category names
                         in the variance field.
        dtSim (pandas DataFrame): _description_

    Returns:
        a numpy array containing generated categories according to specified 
        distributions
    """
    probs = parseCatFormula(formula, dtSim=dtSim.copy())
    if np.round(sum(probs), 5) < 0.99:
        print("Probabilities do not add to 1! Adding category to all rows!")
        probs.append(1-sum(probs))
    else:
        probs[-1] += 1-sum(probs)
    # i.e. cat_1, cat_2, to cat_N
    if variance == 0:
        cats = [i+1 for i in range(len(probs))]
    elif variance != 0 and isinstance(variance, str):
        cats = variance.split(",")
        cats = [i.strip(" ") for i in cats]
    elif variance != 0 and isinstance(variance, list):
        pass
    else:
        pass

    if len(cats) != len(probs):
        raise Exception("Number of probabilities and number of categories"
                        + "do not match!")

    generatedColumn = np.random.choice(a=cats, size=n, p=probs)

    return generatedColumn


def gennegbinom(n: int, formula, variance, link, dtSim):
    """_summary_

    Args:
        n (int): _description_
        formula (_type_): _description_
        variance (_type_): _description_
        link (_type_): _description_
        dtSim (_type_): _description_
    """
    mean, _ = evalWith(formula, link)
    size, prob = negbinomGetSizeProb(mean, variance)

    generatedColumn = np.random.negative_binomial(n=size, p=prob, size=n)

    return generatedColumn


def gennorm(n: int, formula, variance, dtSim):
    """
    All the args are provided by a row in a data definition Data Frame
    Generate column with data drawn from a normal distribution
    When formula is an int , this amounts to the mean of the distribution
    When formula is an equation (or includes a previous variable) then we draw
    from a row-wise mean

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        variance (_type_): _description_
        dtSim (_type_): _description_
    """

    mean, variance = evalWith(formula=formula, variance=variance,
                              dtSim=dtSim.copy())

    generatedColumn = np.random.normal(loc=mean, scale=np.sqrt(variance),
                                       size=n)

    return generatedColumn


def genlognorm(n: int, formula, variance, dtSim):
    """
    All the args are provided by a row in a data definition Data Frame
    Generate column with data drawn from a log normal distribution
    When formula is an int , this amounts to the mean of the distribution
    When formula is an equation (or includes a previous variable) then we draw
    from a row-wise mean

    NB: NOT INCLUDED IN ORIGINAL R PACKAGE
    Created by Gab for demo purposes

    Args:
        n (int): Number of distribution draws
        formula (_type_): Mean of the distribution
        variance (_type_): Variance of the distribution
        dtSim (_type_): _description_
    """

    mean, variance = evalWith(formula=formula, variance=variance,
                              dtSim=dtSim.copy())

    generatedColumn = np.random.lognormal(mean=mean, sigma=np.sqrt(variance),
                                          size=n)

    return generatedColumn


def genpois(n, formula, link, dtSim):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        link (_type_): _description_
        dtSim (_type_): _description_

    Returns:
        _type_: _description_
    """
    mean, _ = evalWith(formula=formula, variance=0, dtSim=dtSim.copy())

    if link == "log":
        mean = np.exp(mean)

    return np.random.poisson(lam=mean, size=n)


def genpoisTrunc(n, formula, link, dtSim):
    mean, _ = evalWith(formula=formula, variance=0, dtSim=dtSim.copy())
    u = stats.uniform().rvs(size=n)
    x = poisson.ppf(poisson.cdf(0, mean) + u * (
        poisson.cdf(float('inf'), mean) - poisson.cdf(0, mean)), mean)

    return x


def genAssign(dtName, balanced, strata, grpName, ratio):
    # The number of treatments is length of ratio
    # reuse random.choice
    # convert ratio to probability done by parse formula
    # probs = parsetrtFormula(dtName,)
    if isinstance(ratio, list):
        ntrt = len(ratio)
    elif isinstance(ratio, int):
        ntrt = ratio
    elif isinstance(ratio, str):
        ntrt = len(ratio.split(','))
    if balanced == 'identity':
        balanced = True
    if strata == 0:
        strata = None
    elif isinstance(strata, str):
        pass
    elif isinstance(strata, list):
        # TODO refactor this
        for i in strata:
            if i in dtName.columns:
                continue
            else:
                raise Exception("strata not found in data columns")

    probs = trtAssign(dtName, ntrt, balanced, strata, grpName, ratio)

    return probs


# def parsetrtFormula(ratio):
#     """
#     Converts ratios to probabilities.

#     Args:
#         ratio (list): ratios from data table
#     """

#     "1;1"
#     "1;1;1"

#     if len(varNames) == 0:
#         ratios = [int(i) for i in formula.split(",")]
#         tempSum = sum(ratios)
#         probs = [y/tempSum for y in ratios]

#         return probs

#     else:
#         ratios = [int(simple_eval(u, names=names)) for u in formula.split(",")]
#         tempSum = sum(ratios)
#         probs = [y/tempSum for y in ratios]
#         return probs


def genUnifInt(n, formula, dtSim):
    """_summary_

    Args:
        n (_type_): _description_
        formula (_type_): _description_
        dtSim (_type_): _description_
    """
    # import math
    uMin, uMax = parseUnifFormula(formula, dtSim, n)
    # uMin, uMax = math.floor(uMin), math.floor(uMax)

    generatedColumn = np.random.randint(low=uMin, high=uMax, size=n)

    return generatedColumn
