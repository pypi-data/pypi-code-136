import numpy as np
import pandas as pd
from scipy import stats
from .utility import (gammaGetShapeRate, negbinomGetSizeProb, 
                                genQuantU)
import math


def checkBoundsBin(p1, p2, d):
    """Internal functions called by genCorGen and addCorGen
    Checks for boundaries of correlation matrix to be within
    upper bounds and lower bounds


    Args:
        p1 (int): parameter to calculate lower bounds
        p2 (int): parameter to calculate upper bounds
        d (int): dimensions of correlation matrix to check

    returns: None if successful, error if bounds are exceeded
    """
    l = (p1*p2) / ((1 - p1) * (1 - p2))
    L = max(-np.sqrt(l), -np.sqrt(1 / l))
    u = (p1 * (1 - p2)) / (p2 * (1 - p1))
    U = min(np.sqrt(u), np.sqrt(1 / u))
    if (d < L and d != L) or (d > U and d != U):
        LU = f"{round(L, 2)} ... {round(U, 2)}"
        raise Exception(f"Specified\
                        correlation {d} out of range {LU}")
    return


def findRhoBin(p1, p2, d):
    """_summary_

    Args:
        p1 (_type_): _description_
        p2 (_type_): _description_
        d (_type_): _description_
    """
    checkBoundsBin(p1, p2, d)
    target = d * np.sqrt(p1 * p2 * (1 - p1) * (1 - p2)) + p1 * p2
    Max = 1
    Min = 1
    test = 0
    found = False
    while not found:
        corr = np.identity(2)
        corr[0, 1] = corr[1, 0] = test
        est = multivariate_normal.cdf([stats.norm.ppf(p1),
                                      stats.norm.ppf(p2)],
                                      mean=[0, 0], cov=corr)
        if (round(est, 5) == round(target, 5)):
            found = True
            rho = test
        elif (est < target):
            Min = test
            test = (Min + Max) / 2
        else:
            Max = test
            test = (Min + Max) / 2
    return rho


def genCorData(n: int, mu: list, sigma, rho=None, corMatrix=None, corstr="ind",
               cnames=None, idname="id"):
    """

    Args:
        n (int): _description_
        mu (list): _description_
        sigma (int or list): _description_
        rho (float): _description_
        corMatrix (_type_, optional): _description_. Defaults to None.
        corstr (str, optional): _description_. Defaults to "ind".
        cnames (_type_, optional): _description_. Defaults to None.
        idname (str, optional): _description_. Defaults to "id".
    """

    nvars = len(mu)

    if cnames is not None and len(cnames) != nvars:
        raise Exception("Invalid number of variable names")

    corMatrix = buildCorMat(nvars, corMatrix, corstr, rho)

    if not isinstance(sigma, list):
        varMatrix = (sigma**2) * corMatrix
    elif isinstance(sigma, list) and len(sigma) > 0:
        D = np.diag(sigma)
        if len(np.diag(corMatrix)) != len(sigma):
            raise Exception("Improper number of standard deviations")
        else:
            varMatrix = (D @ corMatrix) @ D

    dt = pd.DataFrame(np.random.multivariate_normal(mean=mu, 
                      cov=varMatrix, size=n))

    if cnames is None:
        cnames = ['Var_'+str(i) for i in range(nvars)]

    dt.columns = cnames
    dt[idname] = [i+1 for i in range(len(dt))]

    return dt


def genCorGen(n: int, nvars: int,  dist: str, corstr: str, params1, rho,
              params2=None, corMatrix=None, wide=False, cnames=None,
              method: str = "copula", idname="id"):
    """_summary_

    Args:
        n (int): _description_
        nvars (int): _description_
        dist (str): _description_
        corstr (str): _description_
        params1 (_type_): _description_
        rho (_type_): _description_
        params2 (_type_, optional): _description_. Defaults to None.
        corMatrix (_type_, optional): _description_. Defaults to None.
        wide (bool, optional): _description_. Defaults to False.
        cnames (_type_, optional): _description_. Defaults to None.
        method (str, optional): _description_. Defaults to "copula".
        idname (str, optional): _description_. Defaults to "id".
    """
    import numbers

    if dist not in ["poisson", "binary", "gamma", "uniform",
                    "negBinomial", "normal"]:
        raise Exception("Distribution not properly specified.")

    if not isinstance(params1, numbers.Number):
        raise Exception("Parameters must be numeric")

    if params2 is not None:
        if not isinstance(params2, numbers.Number):
            raise Exception("Parameters must be numeric")
        nparams = 2
    else:
        nparams = 1
    if nparams > 1 and dist in ["poisson", "binary"]:
        raise Exception(f"Too many parameter vectors({nparams}) for \
            distribution {dist}")
    if nparams < 2 and dist in ["gamma", "uniform", "normal",
                                "negBinomial"]:
        raise Exception(f"Too few parameter vectors({nparams}) for\
             distribution({dist})")

    if len(params1) == 1:
        params1 = np.repeat(params1, nvars)

    if params2 is not None:
        if len(params2) == 1:
            params2 = np.repeat(params2, nvars)

    if len(params1) != nvars:
        raise Exception(f"Length of vector 1 = {len(params1)},\
                          not equal to number of correlated \
                              variables({nvars})")

    # TODO This gets written like 3 times.
    # if params2 is not None
    if params2 is not None:
        if len(params2) != nvars:
            raise Exception(f"Length of vector 2{len(params2)}\
                 not equal to # of corr variables{nvars}")

    if method in ["copula", "ep"]:
        raise Exception(f"{method} is not a valid method")

    if dist != 'binary' and method == 'ep':
        raise Exception(f"Method {method} applies only to binary\
                         data generation")

    if method == 'copula':
        mu = np.repeat(0, nvars)

    dtM = genQuantU(nvars, n, rho, corstr, corMatrix)

    if dist == "binary":
        dtM['param1'] = np.repeat(params1, len(dtM) / len(params1))[:len(dtM)]
        dtM['X'] = dtM.apply(lambda x: stats.binom.ppf(x['Unew'],
                             x['param1']), axis=1)
    elif dist == "poisson":
        dtM['param1'] = np.repeat(params1, len(dtM) / len(params1))
        dtM['X'] = dtM.apply(lambda x: stats.poisson.ppf(x['Unew'],
                            x['param1']),
                            axis=1)
    elif dist == "negBinomial":
        sp = negbinomGetSizeProb(params1, params2)
        dtM['param1'] = np.repeat(sp[0], len(dtM))
        dtM['param2'] = np.repeat(sp[1], len(dtM))
        dtM['X'] = dtM.apply(lambda x: stats.nbinom.ppf(x['Unew'], x['param1'],
                                                        x['param2']), axis=1)
    elif dist == "uniform":
        dtM['param1'] = np.repeat(params1, len(dtM) / len(params1))[:len(dtM)]
        dtM['param2'] = np.repeat(params2, len(dtM) / len(params2))[:len(dtM)]
        dtM['X'] = dtM.apply(lambda x: stats.uniform.ppf(x['Unew'], x['param1'],
                            x['param2']),
                            axis=1)
    elif dist == "gamma":
        sr = gammaGetShapeRate(params1, params2)
        dtM['param1'] = np.repeat(sr[0], len(dtM))
        dtM['param2'] = np.repeat(sr[1], len(dtM))
        dtM['X'] = dtM.apply(lambda x: stats.gamma.ppf(x['Unew'], x['param1'],
                            x['param2']),
                            axis=1)
    elif dist == "normal":
        dtM['param1'] = np.repeat(params1, len(dtM) / len(params1))[:len(dtM)]
        dtM['param2'] = np.repeat(params2, len(dtM) / len(params2))[:len(dtM)]
        dtM['X'] = dtM.apply(lambda x: stats.norm.ppf(x['Unew'], x['param1'],
                                                      np.sqrt(x['param2'])),
                             axis=1)
    elif method == "ep":
        corMatrix = buildCorMat(nvars, corMatrix, corstr, rho)
        dtM = genBinEP(n, params1, corMatrix)

    # TODO check if we need this later on
    # in R, they set the id explicitly
    # setkey(dtM, "id")

    if not wide:
        dFinal = dtM[['id', 'period', 'X']]

        if cnames is not None:
            dFinal = dFinal.rename({"X":cnames}, axis=1)
        else:
            dFinal = pd.melt(dtM, id_vars="seq", value_vars="X")
        # duplicate line 169 + 174
        if cnames is not None:
            # declared but not used yet , it is used in rename
            nnames = cnames.split(",")
            # TODO double check necessity of this
            # R code line 410 seems to just rename here

    return dFinal


def genBinEP(n, p, tcorr):
    """generate

    Args:
        n (_type_): _description_
        p (_type_): _description_
        tcorr (_type_): _description_
    """

    n_p = len(p)
    phicorr = np.diag(len(p))

    for i in range(1, n_p):
        for j in range(i+1, n_p+1):
            p1 = p[i]
            p2 = p[j]
            phicorr[i, j] = phicorr[j, i] = findRhoBin(p1, p2, tcorr[i, j])

    w, v = np.linalg.eig(phicorr)
    
    if not x.all() > 0:
        phicorr = nearestPD(phicorr)

    normvars = np.random.multivariate_normal(mean=np.repeat(0, len(p)),
                                             cov=phicorr, size=n)

#       z <- matrix(rep(stats::qnorm(p), nrow(normvars)), nrow = nrow(normvars), byrow = TRUE)
#   binvars <- matrix(as.integer(normvars < z), nrow = nrow(z))

#   dtX <- data.table(binvars)
#   dtX[, id := .I]

#   dtM <- melt(dtX, id.vars = "id", variable.factor = TRUE, value.name = "X", variable.name = "seq")

#   dtM[, period := as.integer(seq) - 1]
#   setkey(dtM, "id")
#   dtM[, seqid := .I]

#   return(dtM[])

    return #something


def genCorFlex(n: int, defs: pd.DataFrame, rho=0, tau=None, corstr: str = "cs",
               corMatrix=None):
    """_summary_

    Args:
        n (int): _description_
        defs (pd.DataFrame): _description_
        rho (int, optional): _description_. Defaults to 0.
        tau (_type_, optional): _description_. Defaults to None.
        corstr (str, optional): _description_. Defaults to "cs".
        corMatrix (_type_, optional): _description_. Defaults to None.
    """
    acceptedDists = ["normal", "gamma", "uniform", "binary",
                     "poisson", "negBinomial"]
    passedDists = defs['dist'].values

    if len([d for d in passedDists if d in acceptedDists]) != len(passedDists):
        raise Exception("Only implemented for the following distributions: \
                        binary, uniform, normal, poisson, gamma, \
                        and negative binomial")

    corDefs = defs.copy()
    nvars = corDefs.shape[0]

    # Uniform parameters entered as string
    nUniform = corDefs[corDefs['dist'] == "uniform"].shape[0]

    if nUniform > 0:
        defUnif = corDefs[corDefs['dist'] == 'uniform']

        newFormVar = defUnif['formula'].apply(lambda x:
                                              x.split(','))

        corDefs.loc[corDefs['dist'] == 'uniform', 'formula'] = \
            newFormVar.apply(lambda x: x[0])

        corDefs.loc[corDefs['dist'] == 'uniform', 'variance'] = \
            newFormVar.apply(lambda x: x[1])

    # get shape rates
    if 'gamma' in corDefs['dist'].values:
        shapeDict = corDefs[corDefs['dist'] == 'gamma'].\
            apply(lambda x: gammaGetShapeRate(x.formula, x.variance), axis=1)

        # print(corDefs[corDefs['dist'] == 'gamma', 'formula'])

        corDefs.loc[corDefs['dist'] == 'gamma', 'formula'] = \
            shapeDict.apply(lambda x: x[0])
        corDefs.loc[corDefs['dist'] == 'gamma', 'variance'] = \
            shapeDict.apply(lambda x: x[1])

    if 'negBinomial' in corDefs['dist'].values:
        sizeDict = corDefs[corDefs['dist'] == 'negBinomial'].\
            apply(lambda x: negbinomGetSizeProb(x.formula, x.variance), axis=1)

        corDefs.loc[corDefs['dist'] == 'negBinomial', 'formula'] = \
            sizeDict.apply(lambda x: x[0])
        corDefs.loc[corDefs['dist'] == 'negBinomial', 'variance'] = \
            sizeDict.apply(lambda x: x[1])

    if corDefs['formula'].isnull().any() > 0:
        raise Exception("Non-scalar values in definitions")

    if tau is not None:
        rho = math.sin(tau * math.pi / 2)

    # Start generating data (first, using copula)
    dx = genQuantU(nvars=nvars, n=n, rho=rho, corstr=corstr,
                   corMatrix=corMatrix)

    dx['dist'] = np.repeat(corDefs['dist'].values,
                           int(len(dx)/len(corDefs['dist'].values)))

    dx['param1'] = np.repeat(corDefs['formula'].values,
                             int(len(dx)/len(corDefs['formula'].values)))\
        .astype(np.float)

    dx['param2'] = np.repeat(corDefs['variance'].values,
                             int(len(dx)/len(corDefs['variance'].values))).\
        astype(np.float)

    dFinal = pd.DataFrame(index=dx.loc[dx['period'] == 0].index)

    for i in range(nvars):
        dTemp = dx[dx['period'] == (i)]
        type = corDefs['dist'].iloc[i]

        if type == "binary":
            V = dTemp.apply(lambda x: stats.binom.ppf(x['Unew'], 1,
                            x['param1']), 
                            axis=1)
        elif type == 'poisson':
            V = dTemp.apply(lambda x: stats.poisson.ppf(x['Unew'],
                            x['param1']),
                            axis=1)
        elif type == "uniform":
            V = dTemp.apply(lambda x: stats.uniform.ppf(x['Unew'], x['param1'],
                            x['param2']),
                            axis=1)
        elif type == "gamma":
            V = dTemp.apply(lambda x: stats.gamma.ppf(x['Unew'], x['param1'],
                            x['param2']),
                            axis=1)
        elif type == "normal":
            V = dTemp.apply(lambda x: stats.norm.ppf(x['Unew'], x['param1'],
                            np.sqrt(x['param2'])), axis=1)
        elif type == "negBinomial":
            V = dTemp.apply(lambda x: stats.nbinom.ppf(x['Unew'], x['param1'], 
                            x['param2']),
                            axis=1)

        print(corDefs['varname'].iloc[i])
        # V.rename({"V": corDefs['varname'].iloc[i]}, axis=1, inplace=True)
        dFinal = pd.concat([dFinal, V], ignore_index=True, axis=1)

    dFinal.columns = corDefs['varname'].values
    return dFinal


def buildCorMat(nvars: int, corMatrix, corstr, rho):
    """ Check or create correlation matrix

    Args:
        nvars (_type_): _description_
        corMatrix (_type_): _description_
        corstr (_type_): _description_
        rho (_type_): _description_
    """
    if corMatrix is None:
        corMatrix = np.diag(np.full(nvars, 1))
        if corstr == "cs":
            # replace non-diag elements with rho
            corMatrix = np.where(corMatrix != 1, rho, corMatrix)
        elif corstr == 'ar1':
            # hacky... I don't know any way to call R's
            # col() / row() functions... but this works
            row_ix = np.repeat([i+1 for i in range(nvars)], nvars).\
                     reshape(nvars, nvars)
            col_ix = row_ix.T
            corMatrix = rho**abs(col_ix - row_ix)
    elif corMatrix is not None:
        if nvars != len(corMatrix.diagonal()):
            raise Exception("Length of mean vector mismatched with correlation\
                  matrix")
        # this checks if a matrix is symmetric
        if (corMatrix != corMatrix.T).all():
            raise Exception("Correlation matrix not symmetric")
        if not np.all(np.linalg.eigvals(corMatrix) > 0):
            raise Exception("Correlation matrix not positive definite")

    return corMatrix


def genCorMat(nvars: int, cors=None):
    """_summary_

    Args:
        nvars (_type_): _description_
        cors (_type_, optional): _description_. Defaults to None.
    """
    from math import comb

    if cors is None:
        ev = np.random.uniform(0, 10, size=nvars)
        Z = np.random.normal(size=nvars**2)
        decomp = np.linalg.qr(Z.reshape(nvars, nvars))
        Q = decomp[0]
        R = decomp[1]
        d = np.diag(R)
        ph = d / abs(d)
        O = Q @ np.diag(ph)
        Z = O.T @ np.diag(ev) @ O
        Z = np.array(Z)
        # this step is cov2cor in R
        # generates correlation matrix from correlation matrix
        diag = np.sqrt(np.diag(np.diag(Z)))
        inv = np.linalg.inv(diag)
        corr = inv @ Z @ inv
        return corr
    else:
        if comb(nvars, 2) != len(cors):
            raise Exception("Correlations improperly specified")
        else:
            cm = np.zeros(shape=(nvars, nvars))
            inds_u = np.triu_indices(len(cm), 1)
            cm[inds_u] = cors
            cm.T[inds_u] = cors
            np.fill_diagonal(cm, 1)
            return cm


def nearestPD(A):
    """Find the nearest positive-definite matrix to input
    A Python/Numpy port of John D'Errico's `nearestSPD` MATLAB code [1], which
    credits [2].
    [1] https://www.mathworks.com/matlabcentral/fileexchange/42885-nearestspd
    [2] N.J. Higham, "Computing a nearest symmetric positive semidefinite
    matrix" (1988): https://doi.org/10.1016/0024-3795(88)90223-6
    """

    B = (A + A.T) / 2
    _, s, V = la.svd(B)

    H = np.dot(V.T, np.dot(np.diag(s), V))

    A2 = (B + H) / 2

    A3 = (A2 + A2.T) / 2

    if isPD(A3):
        return A3

    spacing = np.spacing(la.norm(A))
    # The above is different from [1]. It appears that MATLAB's `chol` Cholesky
    # decomposition will accept matrixes with exactly 0-eigenvalue, whereas
    # Numpy's will not. So where [1] uses `eps(mineig)` (where `eps` is Matlab
    # for `np.spacing`), we use the above definition. CAVEAT: our `spacing`
    # will be much larger than [1]'s `eps(mineig)`, since `mineig` is usually on
    # the order of 1e-16, and `eps(1e-16)` is on the order of 1e-34, whereas
    # `spacing` will, for Gaussian random matrixes of small dimension, be on
    # othe order of 1e-16. In practice, both ways converge, as the unit test
    # below suggests.
    I = np.eye(A.shape[0])
    k = 1
    while not isPD(A3):
        mineig = np.min(np.real(la.eigvals(A3)))
        A3 += I * (-mineig * k**2 + spacing)
        k += 1

    return A3


def isPD(B):
    """Returns true when input is positive-definite, via Cholesky"""
    try:
        _ = la.cholesky(B)
        return True
    except la.LinAlgError:
        return False
