import numpy as np
import pandas as pd
from scipy import special
from scipy import stats
from scipy.stats import logistic
from .utility import adjustProbs, evalWith
from .generate_dist import generate
from .asserts import *
from typing import List, Union


def genData(n: int, dtDefs: pd.DataFrame = None, id: str = "id"):
    """_summary_

    Args:
        n (_type_): _description_
        dtDefs (_type_, optional): _description_. Defaults to None.
        id (str, optional): _description_. Defaults to "id".

    Returns:
        _type_: _description_
    """
    #   assertNotMissing(n = missing(n))
    #   assertValue(n = n, id = id)
    #   assertType(id = id, type = "character")
    #   assertNumeric(n = n)

    if dtDefs is None:
        dt = pd.DataFrame({'id': range(1, n)})
        dt.set_index('id', inplace=True)
    else:
        assert isinstance(dtDefs, pd.DataFrame)
    
    # oldId = attr(dtDefs, "id")
    # try:
    #     oldId = dtDefs.attrs['id']
    #     if oldId != id and id is not None:
    #         if oldId != "id":
    #             print("Previously defined 'id'-column found:" + oldId)
    #             print("The current specification: " + id + " will override it.")
    # except: 
    #     ifxnulltheny(oldId, id)

    # init empty DataFrame with n rows
    dfSimulate = pd.DataFrame(data={'id': range(n)}).set_index('id')
    
    if dtDefs is None:
        return dfSimulate
    else:
        # generate a column of data for each row of dtDefs
        iter = dtDefs.shape[0]

    for i in range(iter):
        # print(dtDefs.iloc[i])
        
        dfSimulate = generate(
                        args=dtDefs.iloc[i],
                        n=n,
                        dfSim=dfSimulate,
                        idname=id,
                    )
        # print(dfSimulate.head())

    # print(dfSimulate.head())
    # dt = pd.DataFrame(dfSimulate)
    dfSimulate = dfSimulate.reset_index().rename({'index':'id'},
                                                 axis=1)

    return dfSimulate


def genDummy(dtName, varname, sep=".", replace=False):
    """#' Create dummy variables from a factor or integer variable
        #'
        #' @param dtName Data table with column
        #' @param varname Name of factor
        #' @param sep Character to be used in creating new name for dummy fields.
        #' Valid characters include all letters and "_". Will default to ".". If
        #' an invalid character is provided, it will be replaced by default.
        #' @param replace If replace is set to TRUE (defaults to FALSE) the field
        #' referenced varname will be removed.

    Args:
        dtName (_type_): _description_
        varname (_type_): _description_
        sep (str, optional): _description_. Defaults to ".".
        replace (bool, optional): _description_. Defaults to False.
    """
    # Initial data checks
    if dtName is None:
        raise Exception('argument "dtName" is missing')
    if varname is None:
        raise Exception("argument 'varname' is missing")

    # Check if varname exists

    if not np.isin(varname, dtName.columns):
        raise Exception("variable "+varname+" not found in data table")

    # Check if field is integer or factor

    x = dtName[varname]

    if x.dtype != 'int' or x.dtype != 'category':
        raise Exception("variable "+varname+" must be a factor or integer" )

    if x.dtype == 'int':
        x = x.astype('category')

    # if sep is invalid, defaults to "."
    nlevels = len(x.unique)
    dummy_names = [varname + '_' + i for i in range(nlevels)]
    
    # Check to see if new field names exist
    for i in range(nlevels):
        if np.isin(dummy_names[i], dtName.columns):
            raise Exception("variable " + dummy_names[i]+ " already exists in data table") 

    # Create dummies for each level of factor

    dummies = pd.DataFrame(np.diag(np.full(nlevels,1)), columns = dummy_names)

    if replace:
        dtName.drop(varname, axis=1, inplace=True)

    return pd.concat([dtName, dummies], axis=1)
  
  
def genFactor(dtName,
              varname,
              labels=None,
              prefix="f",
              replace=False):
    """
    Create factor string variable from an existing variable

    Args:
    dtName - dataframe with columns
    varname - name of the field to be converted
    labels - Factor level labels. if not provided, the generated factor
    levels will be used as labels. Can be a vector if only one new factor
    or all factors have the same labels. Or can be a list of charactor vectors
    with the same length as varname
    prefix - prefix to concatenate to the field name. defaults to "f"
    replace - if True, field referenced varname will be removed. Defaults to false.

    returns:
    dataframe with observations and factor column generated

    """


    assert dtName is not None
    assert varname is not None

    fname = prefix+varname
    # assertNotInDataTable({'vars' : fname, 'dt' : dtName})

    # Create new column as factor
    if labels is not None:
        dtName[fname] = pd.Categorical(dtName[varname], categories=labels)
    else:
        dtName[fname] = pd.Categorical(dtName[varname])

    if replace:
        dtName.drop(varname, axis=1, inplace=True)

    return dtName


def genFormula(coefs, vars):
    """Generate a linear formula
    Formulas for additive linear models can be generated
    with specified coefficient values and variable names.

    Args:
        coefs (str or list of numbers): A vector that contains the values of the
        coefficients. Coefficients can also be defined as character for use with 
        double dot notation. If length(coefs) == length(vars), then no intercept
        is assumed. Otherwise, an intercept is assumed.
        vars (str or list of strings): A vector of strings that specify the names of the
        explanatory variables in the equation.

    Returns a string that represents the desired formula
    """
    import numbers

    if not isinstance(vars, list):
        vars = [vars]

    if not isinstance(coefs, list):
        coefs = [coefs]

    lcoef = len(coefs)
    lvars = len(vars)

    if not (lcoef == lvars or lcoef == (lvars + 1)):
        raise Exception("Coefficients or variables not properly specified")

    if not all(isinstance(coef, numbers.Number) for coef in coefs):
        raise Exception("Coefficients must be specified as numeric values or \
                        numeric variables")

    if not all(isinstance(var, str) for var in vars):
        raise Exception("Variable names must be specified as string")

    if lcoef != lvars:  # Intercept
        form = str(coefs[0])
        coefs = coefs[1:]
    else:  # no intercept
        form = str(coefs[0]) + " * " + vars[0]
        coefs = coefs[1:]
        vars = vars[1:]

    form += "+"
    form += ''.join([str(coefs[i]) + '*' + vars[i] + '+' for i in range(lcoef-1)])
    # gets rid of that trailing `+`
    form = form.strip('+')

    return form


def genMarkov(n: int, transMat, chainLen: int, 
              wide=False, id="id", pername="period",
              varname="state", widePrefix="S", trimvalue=None):
    """_summary_

    Args:
        n (int): _description_
        transMat (np.matrix): _description_
        chainLen (int): _description_
        wide (bool, optional): _description_. Defaults to False.
        id (str, optional): _description_. Defaults to "id".
        pername (str, optional): _description_. Defaults to "period".
        varname (str, optional): _description_. Defaults to "state".
        widePrefix (str, optional): _description_. Defaults to "S".
        trimvalue (_type_, optional): _description_. Defaults to None.
    """
    # check transMat is square matrix and row sums = 1
    # if not isinstance(transMat, np.matrix) or len(transMat.shape) != 2 or \
    #     transMat.shape[0] != transMat.shape[1]:
    #         raise Exception ("Transition matrix needs to be a square matrix")

    # # check row sums = 1
    # if not all(np.ravel(np.round(transMat.sum(axis=0), 5) == 1)):
    #     raise Exception("Rows in transition matrix must sum to 1")

    # # check chainLen is > 1
    # if (chainLen <= 1):
    #     raise Exception("Chain length must be greater than 1")

    # ####
    # dd = genData(n = n, id = id)
    # dd = addMarkov(dd, transMat, chainLen, wide, id, pername, varname,
    #                widePrefix, start0lab = None, trimvalue = trimvalue)

    # return dd


def genMultiFac(nFactors: int, each: int, levels=2, coding="dummy",
                colNames=None, idName="id"):
    """_summary_

    Args:
        nFactors (int): _description_
        each (int): _description_
        levels (int, or scalar optional): _description_. Defaults to 2.
        coding (str, optional): _description_. Defaults to "dummy".
        colNames (_type_, optional): _description_. Defaults to None.
        idName (str, optional): _description_. Defaults to "id".

    Raises:
        Exception: _description_
    """
    if nFactors < 2:
        raise Exception("Must specify at least 2 factors")
    
    if (len(levels) > 1 & (len(levels) != nFactors)): 
        # TODO: GAB- Should we be calling len(levels) or just levels?
        raise Exception("Number of levels does not match factors")

    x = []

    if all([level == 2 for level in levels]):
        if coding == "effect":
            opts = [-1, 1]
        elif coding == "dummy":
            opts = [0, 1]
        else:
            raise Exception("Need to specify 'effect' or 'dummy' coding")
        for i in range(nFactors):
        
            x.append(opts)
    else:
        if len(levels) == 1:
            levels = np.repeat(a=levels, repeats=nFactors)
        for i in range(nFactors):
            x.append(np.range(i))  # TODO: check this
    
    t = np.repeat(x, each)
    dt = pd.DataFrame(t)

    if colNames is not None:
        dt.columns = colNames
    
    dt[idName] = range(len(dt))
    dt.set_index(idName, inplace=True)

    return dt


def genOrdCat(dtName, baseprobs, adjVar=None, catVar="cat",
              asFactor=True, idname="id", prefix="grp", rho=0,
              corstr="ind", corMatrix=None, npVar=None, npAdj=None):
    """_summary_

    Args:
        dtName (_type_): _description_
        baseprobs (_type_): _description_
        adjVar (_type_, optional): _description_. Defaults to None.
        catVar (str, optional): _description_. Defaults to "cat".
        asFactor (bool, optional): _description_. Defaults to True.
        idname (str, optional): _description_. Defaults to "id".
        prefix (str, optional): _description_. Defaults to "grp".
        rho (int, optional): _description_. Defaults to 0.
        corstr (str, optional): _description_. Defaults to "ind".
        corMatrix (_type_, optional): _description_. Defaults to None.
        npVar (_type_, optional): _description_. Defaults to None.
        npAdj (_type_, optional): _description_. Defaults to None.
    """

    baseprobs = adjustProbs(baseprobs)
    nCats = len(baseprobs)

    if corstr not in ["ind", "cs", "ar1"]:
        raise Exception("corstr value must be 'ind', 'cs' or 'ar1'")

    if adjVar is not None:
        adjVar = ensureLength(dict(adjVar = adjVar), n = nCats)

    if npAdj is not None and npVar is None:
        raise Exception("npAdj was specified but npVar was not")
    elif npAdj is None and npVar is not None:
        raise Exception("npVar was specified but npAdj was not")
    elif npAdj is None and npVar is None:
        # npAdj = np.matrix(np.repeat(0, len(baseprobs))) ##TODO: double check this
        npAdj = np.repeat(0, np.array(baseprobs).shape[1])
    elif npAdj is not None and npVar is not None:
        b_len = len(baseprobs)
        if isinstance(npVar, str):
            v_len = 1
        else:
            v_len = len(npVar)

        # npAdj = ensureMatrix(npAdj)
        npAdj = np.matrix(npAdj)

        if npAdj.shape[0] != v_len:
            raise Exception("Number of rows for npAdj"+ str(npAdj.shape[0])
            + " does not match with the number of"
            + " adjustment variables specified in npVar "+ str(v_len)+" !")
    
        if npAdj.shape[1] != b_len:
            raise Exception("Number of categories implied by baseprobs and npAdj"
            +" do not match npAdj should have " + str(b_len) + 
            " columns but has "+str(npAdj)+ " !")
        
    if nCats > 1 and len(catVar) != nCats:
        catVar = [prefix+str(i) for i in range(1, nCats+1)]
    
    dt = dtName.copy()
    n = dt.shape[0]
    zs = genQuantU(nCats, n, rho = rho, corstr = corstr, corMatrix = corMatrix)
    zs['logisZ'] = logistic.ppf(zs['Unew'])

    cprob = np.matrix(baseprobs).cumsum(axis=1).T
    nrow = cprob.shape[0]
    ncol = cprob.shape[1]
    quant = np.apply_along_axis(lambda x: logistic.ppf(x), 1, cprob).\
            reshape(nrow,ncol).T

    mycat = []

    for i in range(1, nCats+1):
        iLogisZ = zs.loc[zs['period'] == i - 1, 'logisZ']
        n_obs_i = len(iLogisZ)
        matlp = np.tile(quant[i-1], n).reshape(n, len(quant[i-1]))

        if adjVar is not None:
            z = dt[adjVar[i]].values
        else:
            z = np.repeat(0, n_obs_i)

        if npVar is not None:
            npVar_mat = np.array(dt[npVar])
        else:
            npVar_mat = np.array(np.repeat(0, n_obs_i))
        

        if len(npAdj.shape) == 1:
            npAdj = npAdj.reshape(1, len(npAdj))
   
        npmat = np.matmul(npVar_mat.reshape(npVar_mat.shape[0], 1), 
                          npAdj)

 
        matlp = np.subtract(np.subtract(matlp, npmat), z.reshape(n, 1))

        # if chkNonIncreasing(matlp): ## TODO: c++ CODE
            # raise Exception("Overlapping thresholds. Check adjustment values!")

        # append a column of infs to matrix
        newMat = np.append(matlp, np.repeat(np.inf, matlp.shape[0]).reshape(-1,1),
                           axis=1) 
        locateGrp = np.array(iLogisZ).reshape(-1,1) > newMat
        assignGrp = locateGrp.sum(axis = 1)

        print(dt)
        return dt, catVar[i-1], assignGrp
        if 'id' in dt.columns: ## quick fix to this id problem...
            mycat.append(pd.DataFrame(data=dict(
                            id = dt[idname],
                            var = catVar[i-1],
                            cat = assignGrp
            )))
        else: # assume id is the index...
            mycat.append(pd.DataFrame(data=dict(
                            id = dt.index,
                            var = catVar[i-1],
                            cat = assignGrp
            )))
    
    dcat = pd.concat(mycat)
    cats = pd.pivot(dcat, index = 'id', columns = 'var', values= 'cat')

    # add a 1 so categories aren't 0 indexed
    cats += 1

    cats = cats.rename({'id': idname}, axis =1)

    dt = pd.concat([dt, cats], axis = 1)

    if asFactor:
        dt = genFactor(dt, catVar, replace = True)
        dt.columns = ['f'+catVar for catVar in dt.columns]

    return dt


def genSpline(dt: pd.DataFrame, newvar: str, predictor: str, theta,
              knots = [0.25, 0.50, 0.75], degree: int=3,
              newrange = None, noisevar = 0):
    """ Generate spline curves

    Args:
        dt (pd.DataFrame): Dataframe that will be modified
        newvar (str): Name of new variable to be created
        predictor (str): Name of field in old dataframe that is predicting new value
        theta (array): A vector or matrix of values between 0 and 1. Each column of the matrix
        represents the weights/coefficients that will be applied to the basis functions
        determined by the knots and degree. Each column of theta represents a separate
        spline curve.
        knots (list, optional): A vector of values between 0 and 1, specifying quantile
        cut-points for splines. Defaults to [0.25, 0.50, 0.75].
        degree (int, optional): Integer specifying polynomial degree of curvature. 
        Defaults to 3.
        newrange (_type_, optional): Range of the spline function , specified as a string
        with two values separated by a semi-colon. The first value represents the
        minimum, and the second value represents the maximum. Defaults to None.
        noisevar (int, optional):  Add to normally distributed noise to observation - where mean
        is value of spline curve. Defaults to 0.

        Returns a modified pandas DataFrame with an added column named `newvar`.
    """

    # TODO: add checks

    if newrange is not None:
        rangenum = [np.float(i) for i in newrange.split(',')]
        if len(rangenum) != 2:
            raise Exception("Range not specified as two values")
        if not all(i.isdigit() for i in newrange.split(',')):
            raise Exception("Non-numbers entered in range")
        newmin = rangenum.min()
        newmax = rangenum.max()
        
    x = dt[predictor]

    if not (x.min() >= 0 and x.max() <= 1):
        x_normalize = (x - x.min()) / (x.max() - x.min())
    else:
        x_normalize = x.copy()
    
    qknots = np.quantile(a=x, q=knots)

    sdata = genbasisdt(x_normalize, qknots, degree, theta)

    if newrange is None:
        newy = sdata[0]['y_spline']
    else: # finish
        newy = sdata[0]['y_spline'] * ((newmax-newmin) + newmin)
    
    dt[newvar] = np.random.normal(loc=newy, scale=noisevar, size=len(newy))

    return dt


def genSurv(dtName: pd.DataFrame, survDefs: pd.DataFrame, digits: int=3, 
            timeName: str=None,  censorName: str=None, eventName: str="event",  
            typeName: str="type", keepEvents: bool=False, idName: str="id"):
    """Generate survival data
    Survival data is added to an existing data set.

    Args:
        dtName (pd.DataFrame): DataFrame to be updated
        survDefs (pd.DataFrame): Definitions to be generated
        digits (int, optional): Number of digits to round. 
        Defaults to 3.
        timeName (str, optional): A string to indicate the name of a combined competing risk
        time-to-event outcome that reflects the minimum observed value of all 
        time-to-event outcomes. 
        Defaults to None.
        censorName (str, optional): The name of a time to event variable that is the censoring. 
        Defaults to None.
        eventName (str, optional): The name of the new numeric/integer column representing the
        competing event outcomes. If censorName is specified, the integer value for
        that event will be 0. Defaults to "event", but will be ignored 
        if timeName is None.
        typeName (str, optional): The name of the new character column that will indicate the
        event type. The type will be the unique variable names in survDefs. Defaults
        to "type", but will be ignored if timeName is None.
        keepEvents (bool, optional): Indicator to retain original "events" columns. 
        Defaults to False.
        idName (str, optional): Name of id field in existing data set. 
        Defaults to "id".
    
    Returns dtName with added survival times
    """

    events = survDefs['varname'].unique()

    dtSurv = dtName.copy()
    
    for i in range(len(events)):
        nlogu = -np.log(np.random.uniform(low=0, high=1, size=dtSurv.shape[0]))
        subDef = survDefs[survDefs['varname'] == events[i]]
        scale, _ = evalWith(formula=subDef['scale'].iloc[0], dtSim=dtSurv)
        shape, _ = evalWith(formula=subDef['shape'].iloc[0], dtSim=dtSurv)
        form1, _ = evalWith(formula=subDef['formula'].iloc[0], dtSim=dtSurv)

        if subDef.shape[0] > 1:
            transition = subDef['transition'].iloc[1]
            t_adj = transition**(1/shape)
            form2, _ = evalWith(formula=subDef['formula'].iloc[1], dtSim=dtSurv)
            threshold = np.exp(form1) * t_adj
            period =  1*(nlogu < threshold) + 2*(nlogu >= threshold)
            tempdt = pd.DataFrame([nlogu, form1, form2, period])
            tempdt['survx'] = np.where(tempdt.period==1, (nlogu/((1/scale)*np.exp(form1)))**shape,
                            ((nlogu - (1/scale)*np.exp(form1)*t_adj + (1/scale)*np.exp(form2)*t_adj)\
                            /((1/scale)*np.exp(form2)))**shape)
            
            newCol = np.round(tempdt['survx'], digits)
        else:
            tempdt = pd.DataFrame([nlogu])
            tempdt['form1'] = form1
            newCol = np.round((nlogu/((1/scale)*np.exp(form1)))**shape, digits)

        dtSurv = pd.concat([dtSurv, pd.Series(newCol, name = events[i])], axis = 1)

    if timeName is not None:
        dtSurv = addCompRisk(dtSurv, events, timeName, censorName, 
                            eventName, typeName, keepEvents)
    
    return dtSurv










