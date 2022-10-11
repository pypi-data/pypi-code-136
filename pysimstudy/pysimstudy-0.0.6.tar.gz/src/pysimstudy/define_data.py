import numpy as np
import os
import pandas as pd
from scipy import special
from simpleeval import simple_eval
from .asserts import (assertValue, assertLength,
                                assertType, assertNotInDataTable)


def defCondition(dtDefs=None, condition="", formula="",
                 variance=0, dist="normal",
                 link="identity"):
    """ Add a single condition to a conditions table

    Adds a condition to a conditions table to be used to create
    data based on meeting or not meeting said conditions.


    Args:
        condition (str): Formula specifying the condition to be
         checked
        formula (str): a string expression for the mean
        dtDefs (pd.DataFrame, optional): Name of conditions table to
         be modified. Defaults to None.
        variance (int, optional): Variance of condition.
         Defaults to 0.
        dist (str, optional): Distribution for the condition.
         Defaults to "normal".
        link (str, optional): Link function for the mean.
         Defaults to "identity".

    returns:
    dataframe with the passed condition added to the table.
    """
    if dtDefs is None:
        dtDefs = pd.DataFrame()

    dtNew = pd.DataFrame([{
        'condition': condition,
        'formula': formula,
        'variance': variance,
        'dist': dist,
        'link': link
        }])

    return pd.concat([dtDefs, dtNew], axis=0)


def defData(dtDefs=None, varname: str = "", formula: str = "", variance=0,
            dist="normal", link="identity", idx="id"):
    """ Add a row of a data definition to a definition table.

    Adds a data defintion to a definition dataframe.
    This resulting dataframe will be used to generate a new dataframe
    which does not yet exist.

    Args:
        dtDefs (pd.DataFrame, optional): Dataframe which the data
         definition will be added to. If not specified, one will
         be created. Defaults to None.
        varname (str, optional): Name of data definition.
         Defaults to "".
        formula (str, optional): A string expression for the
         formula of the data definition.. Defaults to "".
        variance (int, optional): Variance of the data to be
         generated. Defaults to 0.
        dist (str, optional): Distribution type for the data
         to be generated. Defaults to "normal".
        link (str, optional): Linking function for the mean
         of the data definition. Defaults to "identity".
        idx (str, optional): A string indicating the field name
         for the unique record identifier. Defaults to "id".

    Returns:
    Dataframe holding the passed data definition as an observation.
    """

    if varname == "":
        raise Exception("argument 'varname' is missing")

    if formula == "":
        raise Exception("argument 'formula' is missing")

    if dtDefs is None:
        dtDefs = pd.DataFrame()
        # GAB: I have not worked with attributes before,
        # this might need to be refactored later
        # Also, .attrs is an experimental feature in pandas so we
        # will need to keep track of that
        dtDefs.attrs = {'id': idx}
        defVars = ""
    else:
        if 'varname' in dtDefs.columns and varname in dtDefs.varname.values:
            raise Exception("Variable name already exists")
        # TODO: Variable not used in the function?
        defVars = dtDefs.copy()

    if isinstance(formula, str):
        formula = formula.replace(' ', '')

    dtNew = pd.DataFrame([{
        'varname': varname,
        'formula': formula,
        'variance': variance,
        'dist': dist,
        'link': link
        }])

    defNew = pd.concat([dtDefs, dtNew], axis=0, ignore_index=True)

    if len(dtDefs.attrs) > 0:
        defNew.attrs = {"id": dtDefs.attrs['id']}

    return defNew


def defDataAdd(dtDefs=None, varname: str = "", formula: str = "",
               variance=0, dist="normal", link="identity"):
    """Add single row to definition dataframe.

    Adds a row to a definition dataframe which will be used
    to generate a dataset.

    Args:
        dtDefs (Dataframe, optional): dataframe to add observation.
        If none is passed, creates a new dataframe. Defaults to
        None.
        varname (str, optional): Name of new variable.
        Defaults to "".
        formula (str): String expression for mean. Defaults to "".
        variance (int, optional): Variance of data definition.
        Defaults to 0.
        dist (str, optional): Distribution. Defaults to "normal".
        link (str, optional): link function for mean.
        Defaults to "identity".

    returns:
    dataframe with data definition added

    """
    if dtDefs is None:
        dtDefs = pd.DataFrame()

    dtNew = pd.DataFrame([{
        'varname': varname,
        'formula': formula,
        'variance': variance,
        'dist': dist,
        'link': link
        }])
    defNew = pd.concat([dtDefs, dtNew], axis=0)
    # attr(defNew, "id") <- attr(dtDefs, "id")

    return(defNew)


def defRepeat(dtDefs=None, nVars: int = None, prefix: str = "",
              formula: str = "", variance=0, dist="normal",
              link="identity", idx="id"):
    # nVars = missing(nVars),
    # prefix = missing(prefix),
    # formula = missing(formula)
    if nVars is None:
        raise Exception('Please specify the number of variables \
            to include')
    else:
        varnames = ['prefix'+str(i) for i in range(1, nVars+1)]

    if dtDefs is None:
        defNew = defData(varname=varnames[0], formula=formula,
                         variance=variance, dist=dist,
                         link=link, idx=id)

        if nVars > 1:
            for i in range(1, nVars + 1):
                defNew = defData(defNew, varname=varnames[i],
                                 formula=formula, variance=variance,
                                 dist=dist, link=link, idx=id)
    else:
        defNew = dtDefs.copy()

        for i in range(1, nVars + 1):
            defNew = defData(defNew, varname=varnames[i],
                             formula=formula, variance=variance,
                             dist=dist, link=link, idx=id)

    return defNew


def defRead(filen: str = "", idx="id"):
    """
    Read external csv data set definitions

    External CSV needs to have following column names and appropriate
    column types:
        ["varname", "formula", "variance", "dist", "link"]

    Args:
        filen (str): file name to read in
        id (str, optional): optional id column identifier.
        Defaults to "id".

    returns:
    pandas dataframe of definitions.

    """
    import numbers

    if not os.path.isfile(filen):
        raise Exception('No such file')
    else:
        dt = pd.read_csv(filen)

    if not all(dt.columns == ['condition', 'formula', 'variance',
                              'dist', 'link']):
        raise Exception("Field names do not match")

    # check validity of data set

    if not isinstance(dt['formula'].iloc[0], numbers.Number):
        raise Exception("First defined formula must be scalar")

    # if (nrow(read.dt) > 1) {
    if dt.shape[0] > 1:
        for i in range(1, dt.shape[0]):
            evalDef(newvar=dt['varname'].iloc[i],
                    newform=dt['formula'].iloc[i],
                    newdist=dt['dist'].iloc[i],
                    defVars=dt['varname'].iloc[1:i-1])
    dt.attrs = {"id": idx}
    return dt


def defReadAdd(filen: str = ""):
    """
    Adds definitions to definition dataframe from external source

    Read external csv data set definitions for adding columns
    Add additional data based on external definitions.

    Args:
        filen (str, optional): _description_. Defaults to "".

    returns:
    definiton table from file
    """
    # TODO - Check this
    # This should include an original dataframe
    # to which the data should be appended to?

    if not os.path.isfile(filen):
        raise Exception('No such file')
    else:
        dt = pd.read_csv(filen)

    if not all(dt.columns == ['varname', 'formula',
                              'variance', 'dist', 'link']):
        raise Exception("Field names do not match")

    return dt


def defReadCond(filen: str = ""):
    """
    Reads condition to add to a conditions dataframe

    TODO: very similar to defReadAdd, maybe merge both functions later?

    Args:
        filen (str, optional): _description_. Defaults to "".

    Raises:
        Exception: _description_
    """
    if not os.path.isfile(filen):
        raise Exception('No such file')
    else:
        dt = pd.read_csv(filen)

    if not all(dt.columns == ['condition', 'formula',
                              'variance', 'dist', 'link']):
        raise Exception("Field names do not match")

    return dt


def defSurv(dtDefs=None, varname: str = "", formula=0, scale=1,
            shape=1, transition=0):
    """Add definition to survival definitions dataframe

    Args:
        dtDefs pd.DataFrame, optional): Original dataframe
        to append new data definition to. Defaults to None.
        varname (str): data definition name. Defaults to ""
        formula (int): covariates predicting survival.
        Defaults to 0.
        scale (int): Scale parameter for Weibull dist.
        Defaults to 0.
        shape (int): Shape of weibull distribution.
         Defaults to 1.
        transition (int): An integer value indicating the starting
        point for a new specification of the hazard function.
        Defaults to 0 for the first instance of varname.

    returns:
    a dataframe with updated data definitions
    """
    # newvarname = varname

    if dtDefs is None:
        dtDefs = pd.DataFrame()
    if transition != 0:
        raise Exception("first transition time must be set to 0")

    # TODO:
    # https://github.com/kgoldfeld/simstudy/blob/main/R/define_data.R
    #  -> defSurv
    # not sure what is going on in R, but this can't be translated
    # literally in Python we should check and fix this in the future
    # else:
    #     if dtDefs.loc[dtDefs[varname] == newvarname].shape[0] == 0 \
    #        and transition != 0:
    #         raise Exception("first transition time must be set to 0")

    dtNew = pd.DataFrame([{
        'varname': varname,
        'formula': formula,
        'scale': scale,
        'shape': shape,
        'transition': transition
        }])

    defNew = pd.concat([dtDefs, dtNew], axis=0)

    import collections
    varnames = dtNew['varname'].values
    dups = [item for item, count in collections.Counter(varnames).items()
            if count > 1]

    if len(dups) >= 1:
        for i in range(len(dups)):
            transition = defNew.loc[varname == dups[i], 'transition']
            # assertAscending(transition)

    return defNew


def evalDef(newvar, newform, newdist, defVars,
            variance=0, link="identity"):
    """Check new data definition

    Check validity of data definition. Can only check properties
    independent of previously generated data.

    Args:
        newvar (obj): name of new var
        newform (obj): new formula variable
        newdist (obj): new distribution variable
        defVars (obj): existing column names
        variance (int, optional): variance of new data definition.
         Defaults to 0.
        link (str): identity function for formula.
        Defaults to "identity".

    returns:
        blank if definition evaluated successfully

    """
    dists = ["normal", "binary", "binomial", "poisson",
             "noZeroPoisson", "uniform", "categorical", "gamma",
             "beta", "nonrandom", "uniformInt", "negBinomial",
             "exponential", "mixture", "trtAssign"]
    assertValue(dict(varname=newvar))
    # TODO this is a problem of the whole dots2args nonsense
    # assertLength(dict(varname=newvar), length=1)
    if isinstance(newvar, str):
        pass
    elif isinstance(newvar, list):
        assert len(newvar) == 1, "Pass 1 new variable at a time"
    assertType(vars=dict(varname=newvar))
    # TODO assert type is still not working
    # assertType(vars=dict(varname=defVars))
    assert newdist in dists, f'{newdist} not a valid distribution'
    assertNotInDataTable(vars=newvar, df=defVars)

    if newdist == 'binary':
        isValidArithmeticFormula(newform, defVars)
        isIdLogit(link)
    elif newdist == 'binomial':
        isValidArithmeticFormula(newform, defVars)
        isValidArithmeticFormula(variance, defVars)
        isIdLogit(link)
    elif newdist == 'noZeroPoisson':
        pass
    elif newdist == 'exponential':
        isValidArithmeticFormula(newform, defVars)
        isIdLog(link)
    elif newdist == 'negBinomial':
        isValidArithmeticFormula(newform, defVars)
        isValidArithmeticFormula(variance, defVars)
        isIdLog(link)
    elif np.isin(newdist, ['gamma', 'beta', 'poisson', 'uniform']):
        pass
    elif newdist == 'nonrandom':
        isValidArithmeticFormula(newform, defVars)
    elif newdist == 'normal':
        isValidArithmeticFormula(newform, defVars)
        isValidArithmeticFormula(variance, defVars)
    elif newdist == 'categorical':
        # categorical = checkCategorical(newform)
        pass
    elif newdist == 'mixture':
        isValidArithmeticFormula(newform, defVars)
        # checkMixture(newform)
    elif newdist == 'uniformInt':
        # checkUniform(newform)
        pass
    elif newdist == 'trtAssign':
        # checkCategorical(newform),
        pass
    else:
        raise Exception('Unknown distribution')


def isValidArithmeticFormula(formula, defVars):
    """
    Args:
        formula (_type_): _description_
        defVars (_type_): _description_
    """
    import parser

    formula = str(formula)

    if ';' in formula:
        raise Exception("';' not allowed in definitions")

    assertValue(dict(formula=formula))

    if formula == "" or formula is None:
        raise Exception("Formula can't be empty!")

    try:
        formulaParsed = parser.expr(formula).compile()
    # TODO fix blank except
    except:
        raise Exception(f"Equation not properly specified: {formula}")

    operators = set("*+/~")# TODO: more needed
    # TODO what are these vars assigned for?
    formFuncs = [char for char in formula if char in operators]
    formVars = formulaParsed.co_names

    # assertInDataTable(dict(formVars), defVars)


def isIdLogit(link: str):
    """check identity func for logit
    Args:
        link (str): link to check

    returns: None if successful, error if not
    """
    isLink(link, ["identity", "logit"])


def isIdLog(link: str):
    """check identity to see if it is log

    Args:
        link (str): link to check

    returns: blank if successful, error if not
    """
    isLink(link, options=["identity", "log"])


def isLink(link: str, options):
    """check link function validity

    Args:
        link (str): link to check
        options (array): acceptable types for link function

    returns:
    none if successful, error if not
    """
    if link not in options:
        print(f"Invalid link function: {link},\
             must be {options}.")


def rmWS(string):
    """ removes whitespace from string

    args:
        string: string to remove whitespace from

    returns:
        Same string input, without whitespace
    """
    copy = string
    copy = copy.replace(" ", "")
    return copy
