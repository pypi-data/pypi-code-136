import pandas as pd
import numpy as np
from scipy import special, stats
from scipy.optimize import minimize
import parser
from simpleeval import simple_eval
from typing import List, Union


def negbinomGetSizeProb(mean: int, dispersion: int):
    """
    NegBinom mean and dispersion params to size and prob params.

    In simstudy, users specify the negative binomial distribution as
    a function of two parameters - a mean and dispersion. In this case,
    the variance of the specified distribution is mean + (mean**2)*dispersion.
    The base R function rnbinom uses the size and probability parameters
    to specify the negative binomial distribution. This function converts
    the mean and dispersion into size and probability parameters.

    Args:
    mean: The mean of a gamma distribution
    dispersion: The dispersion parameter of a gamma distribution


    Returns:
    A Dictionary which includes the size and probability
    parameters of a negative binomial distribution.
    """
    variance = mean + dispersion * (mean**2)
    size = (mean**2) / (variance - mean)

    prob = mean / variance

    return size, prob
    # return size, prob


def gammaGetShapeRate(mean: float, dispersion: float):
    """
    This function converts the mean and dispersion into the shape and rate.

    In simstudy, users specify the gamma distribution as a function of two
    parameters - a mean and dispersion. In this case, the variance of the
    specified distribution is (mean^2)*dispersion. The base R function rgamma
    uses the shape and rate parameters to specify the gamma distribution.

    Args:
    mean: The mean of a gamma distribution
    dispersion: The dispersion parameter of a gamma distribution

    Returns:
    List of shape and rate parameters of the gamma distribution
    """
    variance = dispersion * (mean**2)

    shape = (mean**2) / variance
    rate = mean / variance

    return shape, rate


def delColumns(dtOld, vars):
    """
    Delete columns from existing data set

    Args:
    dtOld: Name of data table that is to be updated.
    vars: Vector of column names (as strings). vars can be LIST or STRING

    Returns:
    An updated data.table without `vars`

    Example:
    assertNotMissing(dtOld = missing(dtOld), vars = missing(vars))
    assertValue(dtOld = dtOld, vars = vars)
    assertType(vars = vars, type = "character")
    assertInDataTable(vars, dtOld)
    """
    df = dtOld.copy()

    if type(vars) == str:
        vars = list(vars)

    if not all(np.isin(vars, df.columns)):
        raise Exception('Variables to be dropped not in DataFrame')
    else:
        return df.drop(vars, axis=1)


def mergeData(dt1, dt2, idvars):
    """
    Merge two data tables

    Args:
    dt1: Name of first data.table
    dt2: Name of second data.table
    idvars: Vector of string names to merge on

    Returns:
    A new data table that merges dt2 with dt1
    """

    df1 = dt1.copy()
    df2 = dt2.copy()

    df1.set_index(idvars, inplace=True)
    df2.set_index(idvars, inplace=True)

    return pd.merge(dt1, dt2)


def iccRE(ICC, dist, varTotal=None,
          varWithin=None, lambda_param=None, disp=None):
    """
    Generate variance for random effects producing desired ICCs.

    Generate variance for random effects producing desired intra-class
    coefficients (ICCs) for clustered data.

    Args:
    ICC: Vector of values between 0 and 1 that represent the
    target ICC levels
    dist: The distribution that describes the outcome data at the
    individual level. Possible distributions include "normal", "binary",
    "poisson", or "gamma"
    varTotal: Numeric value that represents the total variation for a
    normally distributed model. If "normal" distribution is specified, either
    varTotal or varWithin must be specified, but not both.
    varWithin: Numeric value that represents the variation within a
    cluster for a normally distributed model. If "normal" distribution is
    specified, either varTotal or varWithin must be specified, but not both.
    lambda_param: Numeric value that represents grand mean. Must be specified
    when distribution is "poisson" or "negative binomial".
    disp: Numeric value that represents the dispersion parameter that is used
    to define a gamma or negative binomial distribution with log link. Must be
    specified when distribution is "gamma".

    Returns
    A vector of values that represents the variances of random effects
    at the cluster level that correspond to the ICC vector.
    @examples
    targetICC <- seq(0.05, 0.20, by = .01)
    """

    if dist == "poisson":
        if lambda_param is None:
            raise Exception("Specify a value for lambda")
        else:
            vars = [findPoisVar(1/lambda_param * x / (1-x)) for x in ICC]
            # unlist(lapply(ICC,
            #  function(x) .findPoisVar(1 / lambda * x / (1 - x))))

    elif dist == "binary":
        vars = [(x / (1-x) * (np.pi**2) / 3) for x in ICC]

    elif dist == "normal":
        if varTotal is not None and varWithin is not None:
            raise Exception("Do not specify total and within\
               variance simultaneously")

        if varTotal is None and varWithin is None:
            raise Exception("Specify either total or within variance")

        if varTotal is not None:
            vars = [x*varTotal for x in ICC]

        if varWithin is not None:
            vars = [(x / (1-x)) * varWithin for x in ICC]
            #  unlist(lapply(ICC, function(x) (x / (1 - x)) * varWithin))

    elif dist == "gamma":
        if disp is None:
            raise Exception("Specify dispersion")
        else:
            # special.polygamma(1) is equivalent to R's trigamma function
            vars = [(x / (1-x)) * special.polygamma(1, 1/disp) for x in ICC]

    elif dist == "negBinomial":
        if disp is None:
            raise Exception("Specify dispersion")
        if lambda_param is None:
            raise Exception("Specify lambda")
        if disp is not None and lambda_param is not None:
            vars = [(x / (1-x))
                    * special.polygamma(1, (1/lambda_param + disp)**(-1))
                    for x in ICC]
            # vars = unlist(lapply(ICC, function(x) (
            # x / (1 - x)) * trigamma((1 / lambda + disp)^(-1))))
        else:
            raise Exception("Specify appropriate distribution")

    return vars


def trimData(df_old, seqvar, eventvar, idvar="id"):
    """
    Trim Longitudinal data file once an event occurs

    Trims a dataframe to get rid of observations defined using
    eventvar. Events are defined using the defDataAdd function.
    This returns an updated pandas dataframe which removes
    all rows following the first event for each sequence.

    Args:
    df_old: name of dataframe to be trimmed
    seqvar: string referencing column that indexes the sequence or period
    eventvar: string referencing event data column
    idvar: string referencing id column

    Returns:
    Trimmed Data Frame
    """
    import pandas as pd
    from temp_cpp_py import python_cpp

    df = df_old.copy()

    ids = [i for i in df[idvar]]
    seq = [i for i in df[seqvar]]
    event = [i for i in df[eventvar]]
    idorder = [i for i in set(ids)]

    last = python_cpp.clipVec(ids, seq, event)
    d = {"id": idorder, "last": last}
    dfd = pd.DataFrame(d)

    dftd = pd.DataFrame(columns=df.columns)

    for ind, row in df.iterrows():
        trimmedcount = int(dftd[dftd['id'] == row['id']].shape[0])
        stopat = int(dfd[dfd['id'] == row['id']]['last'].values[0])
        if trimmedcount < stopat:
            dftd.loc[len(dftd.index)] = row
    dftd['id'] = dftd['id'].astype(int)
    dftd['period'] = dftd['period'].astype(int)
    dftd['u'] = dftd['u'].astype(int)
    dftd['e'] = dftd['e'].astype(bool)
    return last, dftd


def survGetParams(points):
  """
  Get survival curve parameters
  
  Args:
  points: A dict of tuples specifying the desired time and 
  probability pairs that define the desired survival curve.
  This arg type should be refactored at some point.
    
  Returns:
  A vector of parameters that define the survival curve optimized for
  the target points. The first element of the vector represents the "f"
  parameter and the second element represents the "shape" parameter.
    
  Example:
  Could refactor input type...right now is dict of tuples
  points = {1:(60, 0.90),2:(100, .75),3:(200, .25),4:(250, .10)}
  survGetParams(points)
  """
  
  #assertNotMissing(missing(points))
  #assertClass(points,type = "dict")
  
  #these seem not ideal; can change with refactored input type
  #time 
  pts1 = np.array(list((k[0] for key, k in points.items())))
  #probabilities
  pts2 = np.array(list((k[1] for key, k in points.items())))
  
  #assertPositive(pts1)
  #assertAscending(pts1)
  
  #assertProbability(pts2)
  #assertDescending(pts2)
  
  def loss_surv(params,pt1,pt2):
    
    def loss(pt1, pt2, params):
      return(( params[1]*(np.log(-np.log(pt2)) - params[0]) - np.log(pt1) ) ** 2)
      
    return (sum([loss(x,y,params) for (x,y) in zip(pt1, pt2)]))
	
  params = [1,1]

  optim_results = minimize(
    fun = loss_surv,
    x0 = params,
    args = (pts1,pts2),
    method = 'L-BFGS-B',
    bounds  = ((-np.inf, np.inf), (0, np.inf))
  )
  
  if optim_results.success == 'False': 
    print("Optimization did not converge")
    
  return(optim_results.x)
  

def updateDef(dtDefs, changevar, newformula=None, newvariance=None,
              newdist=None, newlink=None, remove=False):
    """
    Update definition table

    Updates row definition table which are
    created by defData or defRead. (for tables created with
    defDataAdd or defReadAdd, use updateDefAdd.) Does not modify
    in place.

    Args
    dtDefs - Definition table that will be modified
    changevar - Name of field definition that will be changed
    newformula - New formula definition
    newvariance - New variance specification
    newdist - new distribution definition
    newlink - new link specifcation
    remove - if TRUE, remove 'changevar' from definition table

    Returns
    the updated definition table
    """

    xdef = dtDefs.copy()

    var_ind = xdef[xdef['varname'] == changevar].index[0]

    if newformula:
        xdef.iloc[var_ind, 1] = newformula

    if newvariance:
        xdef.iloc[var_ind, 2] = newvariance

    if newdist:
        xdef.iloc[var_ind, 3] = newdist

    if newlink:
        xdef.iloc[var_ind, 4] = newlink

    if remove:
        xdef.drop(var_ind, inplace=True)
    return xdef


def updateDefAdd(dtDefs, changevar, newformula=None,
                 newvariance=None, newdist=None, newlink=None, remove=None):
    """
    Update definition table

    Updates row of definition table created
    by functions defDataAdd and defReadAdd. (For tables
    created using defData or defRead use updateDef.) This
    operation does not occur in place; a copy is returned.
    All fields beyond the required dtDefs and changevar
    begin with None, (meaning the fields won't update)

    Args:
    dtDefs - Definition table to be modified
    changevar - name of field definition to change
    newformula - new formula definition
    newvariance - new variance specification
    newdist - new distribution definition
    newlink - new link specification
    remove - if True, removes the definition

    Returns:
    a copy of the data table with updates
    """

    xdef = dtDefs.copy()

    var_ind = xdef[xdef['varname'] == changevar].index[0]

    if newformula:
        xdef.iloc[var_ind, 1] = newformula

    if newvariance:
        xdef.iloc[var_ind, 2] = newvariance

    if newdist:
        xdef.iloc[var_ind, 3] = newdist

    if newlink:
        xdef.iloc[var_ind, 4] = newlink

    if remove:
        xdef.drop(var_ind, inplace=True)

    return xdef


def betaGetShapes(mean, precision):
    assert mean > 0 and mean < 1, "Mean out of range [0,1]."
    assert precision > 0, "Precision out of range [0,Inf]."

    a = mean * precision
    b = (1 - mean) * precision

    return({'shape1': a, 'shape2': b})


def addCompRisk(dtName: pd.DataFrame, events: Union[List[str], str],
                timeName: str, censorName=None, eventName="event",
                typeName="type", keepEvents=False, idName="id"):
    """_summary_

    Args:
        dtName (pd.DataFrame): _description_
        events (Union[List[str], str]): _description_
        timeName (str): _description_
        censorName (_type_, optional): _description_. Defaults to None.
        eventName (str, optional): _description_. Defaults to "event".
        typeName (str, optional): _description_. Defaults to "type".
        keepEvents (bool, optional): _description_. Defaults to False.
        idName (str, optional): _description_. Defaults to "id".

    Raises:
        Exception: _description_
    """

    if isinstance(events, list) and len(events) < 2:
        raise Exception("Number of events should be of at least length 2")
    
    # TODO: add more asserts/checks

    dtSurv = dtName.copy()
    
    dtSurv['timeName'] = dtSurv[events].apply(lambda x: x.min(), axis=1)
    dtSurv['eventName'] = dtSurv[events].apply(lambda x: np.argmin(x), axis=1)
    dtSurv['typeName'] = dtSurv[events].apply(lambda x: dtSurv[events]
                                              [np.argmin(x)], axis=1)

    if not keepEvents:
        dtSurv.drop(events, axis=1)
    
    if censorName is not None:
        dtSurv['eventName'] == np.where(dtSurv['typeName'] == censorName, 0,
                                        dtSurv['eventName'])

    return dtSurv


def evalWith(formula, dtSim: pd.DataFrame,
             variance=0, link: str = 'identity'):
    """_summary_

    Args:
        formula (str): _description_
        dtSim (pd.DataFrame): _description_
    """

    # TODO: maybe this is better done in a separate function?
    # May have to add special characters here
    special_chars_mapping = {'^': '**'}

    for k, v in special_chars_mapping.items():
        formula = str(formula).replace(k, v)
        variance = str(variance).replace(k, v)
    ##########################################################

    formulaParsed = parser.expr(str(formula)).compile()
    varNames = formulaParsed.co_names

    # skips special words like abs which should not be evaluated
    # directly, instead we pass this to a dictionary called by
    # simple_eval
    # TODO check for more special words... 'ln' 'log'
    skip = ['abs']
    varNames = [el for el in varNames if el not in skip]

    special_fct_dict = {'abs': lambda x: abs(x)}

    for varName in varNames:
        if varName not in dtSim.columns:
            raise Exception("variable " + str(varName) +
                            " not previously created in definitions table")

    names = {}

    for varName in varNames:
        if np.isin(varName, dtSim.columns):
            names[varName] = dtSim[varName]

    # if there are no variables but just constants i.e. 10
    if len(varNames) == 0:
        mean = np.float(simple_eval((formula))
        variance = np.float(simple_eval(variance))
    else:
        mean = dtSim.apply(lambda x: simple_eval(formula,
                           names=dict([(i, x[list(dtSim.columns).index(i)])
                                      for i in varNames]),
                           functions=special_fct_dict), axis=1)
        # mean = simple_eval(formula, names=names, functions=special_fct_dict)
        # mean = dtSim.apply(lambda z: simple_eval(formula, names=names,
        #                    functions=special_fct_dict)).squeeze()


    if link == "log":
        mean = np.exp(mean)

    elif link == "logit":
        mean = 1 / (1 + np.exp(-mean))

    return mean, variance


def adjustProbs(probs):
    """
    #' Adjust probabilities so they sum to 1
    #'
    #' @description The probabilities will be normalized for sum(probs) > 1 or an
    #' additional probability will be added if sum(probs) < 1. For matrices the
    #' probabilities will be assumed to be row wise!
    #' @param probs numeric vector or matrix of probabilities
    #' @return  The adjusted probabilities.
    """

    # TODO: the R code assumes probs is a list. 
    # Original R script adjusts for matrices with row-wise probs too

    adjustedProbs = []

    # if array is `flat` make it `thick`
    if len(np.array(probs).shape) == 1:
        probs = [probs]

    for p in probs:
        if any(num < 0 for num in p):
            raise Exception("Probabilities cannot be negative!")

        if np.round(sum(p), 5) == 1:
            adjustedProbs.append(p)
        elif sum(p) < 1:
            remainder = 1 - sum(p)
            p.append(remainder)
            adjustedProbs.append(p)
            print("Probabilities do not sum to 1. Adding category with" +
                  f" p = {remainder}")
        elif sum(p) > 1:
            print("Probabilities are higher than ! Normalizing probabilities" +
                  " they sum to 1")
            adjustedProbs.append([prob / sum(p) for prob in p])

    if len(adjustedProbs) == 1:
        adjustedProbs = adjustedProbs[0]

    return adjustedProbs


def findPoisVar(j):
    """
    #' Find variance associated with ICC
    #' @param j Value of function
    #' @return inverse of Poisson ICC function
    """

    a = np.linspace(0, 20, num=int(((20-0)/(0.01))+1))
    dx = pd.DataFrame()
    dx['a'] = a
    dx['y'] = np.exp(3 * a / 2) - np.exp(a / 2)

    dx = dx[dx['y'] <= j]
    amin = dx['a'][dx.shape[0]-1]

    a = np.linspace(amin, amin + 1e-02, num=101)

    dx = pd.DataFrame()
    dx['a'] = a
    dx['y'] = np.exp(3 * a / 2) - np.exp(a / 2)

    dx = dx[dx['y'] <= j]
    amin = dx['a'][dx.shape[0]-1]

    a = np.linspace(amin, amin + 1e-04, num=1001)
    dx = pd.DataFrame()
    dx['a'] = a
    dx['y'] = np.exp(3 * a / 2) - np.exp(a / 2)

    dx = dx[dx['y'] <= j]
    amin = dx['a'][dx.shape[0]-1]

    return amin


def genPosSkew(n: int, mean: np.float, dispersion=0):
    """
    #' Gamma distribution - variation to generate positive skew
    #'
    #' @param n The number of observations required in the data set
    #' @param mean The mean
    #' @param dispersion The variance
    #' @return A data.frame column with the updated simulated data
    #' @details Internal function called by .generate - returns gamma data
    """
    if dispersion == 0:
        new = np.repeat(a=mean, repeats=n)
    else:
        variance = mean**2 * dispersion
        shape = (mean**2) / variance
        rate = mean / variance

        new = np.random.gamma(shape=shape, scale=rate, size=n)

    return new


def genQuantU(nvars, n: int, rho, corstr=None, corMatrix=None, idname="id"):
    """
    #' Quantile for copula data generation
    #'
    #' @param nvars Number of new variables to generate
    #' @param n Number records to generate
    #' @param rho Correlation coefficient
    #' @param corstr Correlation structure
    #' @param corMatrix Correlation matrix
    #' @param idname Name of id variable
    #' @return A data.frame column with correlated uniforms
    #' @details Internal function called by genCorGen and addCorGen
    #' @noRd
    """
    from py_scripts.generate_correlated_data import genCorData

    mu = np.repeat(0, nvars)

    if corMatrix is None:
        dt = genCorData(n, mu, sigma=1, rho=rho, corstr=corstr, idname=idname)
    else:
        dt = genCorData(n, mu, sigma=1, corMatrix=corMatrix, idname=idname)

    dtM = pd.melt(dt, id_vars=idname, value_name="Y", var_name="seq")

    dtM['period'] = dtM['seq'].astype('category').cat.codes
    dtM['seqid'] = dtM.index.astype(int)
    # dtM['period'] = df['seq'].astype(int) - 1
    dtM.set_index(idname, inplace=True)

    dtM['Unew'] = dtM['Y'].apply(lambda x: stats.norm.cdf(x))

    return dtM.drop('Y', axis=1)


def log2Prob(logOdds):
    """
    #' Convert log odds to probability
    #' @param logodds Log odds
    #' @return Probability
    """
    return np.exp(logOdds) / (1 + np.exp(logOdds))


def parseCatFormula(formula, dtSim):
    """

    Args:
        formula (_type_): _description_
        dtSim (_type_): _description_
    """
    formulaParsed = parser.expr(str(formula)).compile()
    varNames = formulaParsed.co_names
    for varName in varNames:
        if varName not in dtSim.columns:
            raise Exception("variable " + str(varName) +
                            " not previously created in definitions table")

    names = {}

    for varName in varNames:
        if np.isin(varName, dtSim.columns):
            names[varName] = dtSim[varName]

    if len(varNames) == 0:
        newForm = formula.split(",")
        newForm = [x.lstrip(' ') for x in newForm]
        newForm = [form for form in newForm if
                   form.replace('.', '', 1).isdigit()]
        probs = [np.float(i) for i in newForm]
        return probs

    else:
        probs = [np.float(simple_eval(u, names=names))
                 for u in formula.split(",")]
        return probs


def parseUnifFormula(formula, dtSim, n):
    """

    Args:
        formula (_type_): _description_
        dtSim (_type_): _description_
        n (_type_): _description_
    """
    formulaParsed = parser.expr(str(formula)).compile()
    varNames = formulaParsed.co_names

    for varName in varNames:
        if varName not in dtSim.columns:
            raise Exception("variable " + str(varName) +
                            " not previously created in definitions table") 

    names = {}

    for varName in varNames:
        if np.isin(varName, dtSim.columns):
            names[varName] = dtSim[varName]

    if len(varNames) == 0:
        uMin, uMax = formula.split(",")
        return np.float(uMin), np.float(uMax)

    else:
        uMin, uMax = [simple_eval(u, names=names) for u in formula.split(",")]
        return uMin.apply(np.float), uMax.apply(np.float)