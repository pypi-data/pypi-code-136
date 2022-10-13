import pandas as pd
import numpy as np
import random
from .generate_dist import generate
import parser
# silence SettingWithCopyWarning
pd.options.mode.chained_assignment = None

def addCondition(condDefs: pd.DataFrame, dtOld: pd.DataFrame,
                 newvar: str, keepOld=False):
    """
    Add a single column to existing data set based on a condition.

    Args:
        condDefs (str): Name of definitions for added column

        dtOld (pd.DataFrame): Name of data table that is to be
        updated.

        newvar (str): Name of new column to add

        keepOld(bool): set to True to keep the columns in dtOld
        that are not modified by the definitions in condDefs
        so newvar will have conditional values based on condition
        and the original values that DO NOT meet the conditions as well
        Will only work if condition is based ONE column

    returns:
    data frame with added column based on condition

    """

    cDefs = condDefs.copy()
    if newvar in dtOld.columns:
        newvar = newvar+"_condition"

    cDefs['varname'] = newvar

    if len(dtOld.attrs) > 0:
        oldkey = dtOld.attrs['id']
    else:
        oldkey = 'id'

    # TODO: add evaldef checks

    iter = cDefs.shape[0]

    dtNew = pd.DataFrame()

    for i in range(iter):
        cond = cDefs['condition'].iloc[i]
        dtTemp = dtOld.query(expr=cond)

        n = dtTemp.shape[0]

        if n > 0:
            dtGen = generate(
                args=cDefs.iloc[i],
                n=n,
                dfSim=dtTemp.copy(),
                idname=oldkey
            )

        # TODO: this looks inefficient... might need fixing
        dtTemp[newvar] = dtGen[dtGen[newvar].notnull()][newvar].values
        dtNew = pd.concat([dtNew, dtTemp], axis=0)

    if keepOld and iter == 1:
        formulaParsed = parser.expr(str(cDefs['formula'].iloc[0])).compile()
        varName = formulaParsed.co_names[0]
        dtNew = dtOld.merge(dtNew, how='left')
        dtNew[newvar] = np.where(dtNew[newvar].isnull(),
                                 dtNew[varName], dtNew[newvar])

    else:
        dtNew = dtNew.merge(dtOld)

    return dtNew


def addMultiFac(dtOld: pd.DataFrame, nFactors: int,
                levels: int or list = None,
                coding="dummy", colNames=None):
    """
    add multi-factorial data.

    Args:
        dtOld (pd.DataFrame): datatable to be updated

        nFactors (int): number of factors to add

        levels (int, optional): Number of levels that the factors
        will be added to. Defaults to None. Can be a list as well

        coding (str, optional): Acceptable values
        are "dummy" or "effect"

        colNames (array, optional): list of column names to use
        for levels. Defaults to None.

    Returns:
        dtNew (pd.DataFrame): data table with multifactor effects
    """

    dtNew = dtOld.copy()

    if dtNew.shape[0] % 2 == 0:
        extra = 0
    else:
        extra = 1

    assert nFactors >= 2, 'Must specify at least 2 factors'

    if isinstance(levels, list) and len(levels) != nFactors:
        raise Exception('Number of levels does not match factors')

    if colNames is None:
        colNames = ['Var'+str(i) for i in range(1, nFactors+1)]
        assert not bool(set(colNames) & set(dtNew.columns)), \
            'Default column name(s) already in use'
    else:
        assert not bool(set(colNames) & set(dtNew.columns)), \
            'Default column name(s) already in use'
    if isinstance(levels, int):
        levelsdict = {'effect': [i for i in range(1, levels+1)],
                      'dummy': [i for i in range(levels)]}
        levels = levelsdict[coding]
    elif levels is None and coding == 'dummy':
        levels = [0, 1]
    elif levels is None and coding == 'effect':
        levels = [-1, 1]
    repeats = dtNew.shape[0] / len(levels)
    if extra == 0:
        for i in range(len(colNames)):
            name = colNames[i]
            # facts = [x for x in range(1, levels[i])]
            dtNew[name] = np.repeat(levels,
                                    repeats=repeats)
            random.shuffle(dtNew[name])
    else:
        for i in range(len(colNames)):
            name = colNames[i]
            reps = np.repeat(levels, repeats=repeats)
            extra = dtNew.shape[0] % len(reps)
            extras = np.random.choice(reps, size=extra)
            reps = np.concatenate((reps, extras))
            dtNew[name] = reps
            random.shuffle(dtNew[name])

    return dtNew
