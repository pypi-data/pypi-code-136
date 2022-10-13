

def addCorGen(dtOld, nvars, rho, corstr, dist, param1,
              corMatrix=None, param2=None, cnames=None, idvar="id",
              method="copula", formSpec=None, periodvar="period"):
    """
    Create multivariate correlated data for general distributions.

    Takes a dataframe, and generates correlated data based on
    provided parameters.

    Args:
        dtOld (pd.Dataframe): if an existing dataframe is specified,
        then `wide` will be set to True and n will be set to the
        number of rows in the dataframe without any warning or error.

        nvars (int): Number of new variables to create for each id
        
        rho (float): Correlation coeffient, -1 <= rho <= 1. Use if 
        corMatrix is not provided.

        corstr (str): Correlation structure of the variance-covariance
        matrix. Defined by sigma and rho. Options include "cs" for a
        compound symmetry structure and "ar1" for an autoregressive
        structure.

        dist (str): A string for distribution indicating "normal", 
        "binary", "poisson", or "gamma"
        
        param1 (str): A string that represents the column in dtOld
        that contains the parameter for the mean of the distribution.
        In the case of the uniform distribution, the column specifies
        the minimum.

        idvar (str, optional): Defaults to "id". String variable 
        name of columns represents individual level id for correlated data.

        corMatrix (np.ndarray, optional): Defaults to None. 
        Correlation matrix can be entered directly. It must be 
        symmetrical and positive semi-definite. It is not a required
        field; if a matrix is not provided, then a structure and
        correlation coefficient rho must be specified.

        param2 (str, optional):Defaults to None. A string that 
        represents the column in dtOld that contains a possible
        second parameter for the distribution. For the normal 
        distribution, this will be the variance; for the gamma
        distribution, this will be dispersion, for uniform,
        this will be the maximum.

        cnames (str, optional): Defaults to None. Explicit column
        names. A single string with names separated by commas. If no
        string is provided, the default names will be V#,
        where # represents the column.

        method (str, optional): Defaults to "copula". Two methods are
        available to generate correlated data. (1) "copula" uses
        themultivariate gaussian copula method that is applied to all
        other distributions; this applies to all available
        distributions. (2) "ep" uses an algorithm developed by Emrich
        and Piedmonte(1991).

        formSpec (str, optional):Defaults to None. The formula that
        was used to generate the binary outcome in the defDataAdd
        statement. This is only necessary when the method "ep"
        is requested.

        periodvar (str, optional):Defaults to "period". A string 
        value that indicates the name of the field that indexes the
        repeated measurement for an individual unit. The value
        defaults to "period"


        returns:
        The original dataframe with added columns of correlated data
    """


    dtTemp = dtOld.copy()

    # check args
    assert dist in ["poisson", "binary", "gamma", "uniform",
                    "negBinomial", "normal"],\
        "Distribution not properly specified."
    assert idvar in dtTemp.columns,\
        f"{idvar} not a valid field/column"
    assert param1 in dtTemp.columns,\
        f"{param1} not a valid field/column"
    assert param2 in dtTemp.columns,\
        f"{param2} not a valid field/column"   

    if param2 is not None:
        nParams = 2
    else:
        nParams = 1

    if nParams > 1 and dist in ["poisson", "binary"]:
        raise Exception(f"Too may parameters ({nParams}) for distribution {dist}")
    if nParams < 2 and dist in ["gamma", "uniform", "normal", "negBinomial"]:
        raise Exception(f"Too few parameters ({nParams}) for distribution {dist}")

    assert method in ['copula', 'ep'], \
        f"{method} not a valid method"

    if dist != "binary" and method == "ep": 
        raise Exception("Method `ep` applies only to binary data generation")
