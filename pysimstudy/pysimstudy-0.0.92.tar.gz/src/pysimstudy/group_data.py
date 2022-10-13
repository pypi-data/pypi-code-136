import pandas as pd
import numpy as np
import math
from .define_data import defData
from .generate_dist import generate
# silence SettingWithCopyWarning
pd.options.mode.chained_assignment = None

def addColumns(dtdefs, dtOld):
    """
    Add columns to existing dataset


    Args:
        dtdefs (dataframe): name of data definition table for cols
        dtOld (dataframe): name of data table to be updated

    returns:
        A dataframe with added columns
    """

    assert isinstance(dtdefs, pd.DataFrame), \
        "definitions should be a dataframe"
    assert isinstance(dtOld, pd.DataFrame), \
        "data table should be a dataframe"

    if any([name for name in dtdefs['varname'] if name in dtOld.columns]):
        raise Exception("Column name to generate already exists \n" +
                        "Please choose another one")

    # TODO evalDef code goes in here
    # for i in range(0, dtdefs.shape[0]):
    # add evalDef code

    if len(dtOld.attrs) > 0:
        oldkey = dtOld.attrs['id']
    else:
        oldkey = 'id'
    iterations = dtdefs.shape[0]
    n = dtOld.shape[0]

    for i in range(0, iterations):
        dtOld = generate(args=dtdefs.iloc[i], n=n,
                         dfSim=dtOld, idname=oldkey)
    # TODO Check id assignments. we are overwriting 'id'

    dtOld = pd.DataFrame(dtOld)

    return dtOld

def addPeriods(df, nPeriods=None, idvars="id",
               timevars=None, timevarName="timevar",
               timeid="timeID", perName="period"):
    """
    Add periods and melts dataframe to show periods with time id

    Takes a generated dataframe, and generates a melted version
    where observations are split based on a passed number of periods.

    Args:
    df - dataframe to use
    nPeriods - Number of periods to create
    idvars - the id variable of dataframe
    timevars - the variables to melt into periods
    timevarName - the name of the resulting time variable
    timeid - the name of the id column to account for passing time
    pername - the name of the period column in the output

    Returns:
    dataframe of observations grouped by period
    """
    df_copy = df.copy()

    # reindex dataframe
    # the new index is n * nPeriods
    newindex = df.shape[0] * nPeriods
    period = np.tile([i for i in range(nPeriods)], df.shape[0])

    timeid = [i for i in range(1, newindex+1)]

    # check for timevars if no timevars

    if nPeriods is not None and timevars is not None:
        if nPeriods != len(timevars):
            raise Exception("Number of periods and number of timevars \
                should match.")

    if timevars is None:
        df_copy2 = df_copy.copy()
        for i in range(1, nPeriods):
            # df_copy2 = df_copy2.append(df_copy)
            df_copy2 = pd.concat([df_copy2, df_copy], axis=0)

        df_copy2 = df_copy2.sort_values(by=[idvars])
        df_copy2['timeID'] = [i+1 for i in range(len(df_copy2))]
        df_copy2[perName] = np.tile([i+1 for i in range(nPeriods)],
                                    reps=len(df_copy[idvars].unique()))
        # df_copy2.rename({'id': timevarName}, axis=1, inplace=True)
        # df_copy2[timevarName] += 1
        
        return df_copy2.reset_index(drop=True)

    df_melted = pd.melt(df_copy, id_vars=idvars, value_vars=timevars,
                        var_name='period',
                        value_name="Y").sort_values(by='id')

    df_melted['period'] = period
    df_melted['timeID'] = timeid
    df_melted = df_melted.reset_index(drop=True)
    return df_melted


def genNthEvent(dtName, defEvent, nEvents=1, perName="period", id="id"):
    """_summary_

    Args:
        dtName (DataFrame): Datatable to be updated
        defEvent (DataFrame): Data definition table with
        event generation formula. Should only have 1 row!
        nEvents (int, optional): Maximum number of events
        per id until truncation. Defaults to 1.
        perName (str, optional): variable name for period field.
                                Defaults to "period".
        id (str, optional): string representing name of the id.
                                Defaults to "id".
    """

    assert len(defEvent) == 1, 'defEvent should only have one row!'

    dtCopy = dtName.copy()

    generatedColumnName = defEvent['varname'][0]

    binom = np.random.binom(size=defEvent['variance'][0],
                            p=defEvent['formula'][0],
                            n=dtCopy.shape[0])

    dtCopy[generatedColumnName] = binom
    # this filters out when an event occurs more than nEvent times
    # for a single id
    # dtCopy.groupby(id)[generatedColumnName].cumsum() <= nEvents
    return dtCopy[dtCopy.groupby(id)[generatedColumnName].cumsum() <= nEvents]


def genCluster(dtClust, cLevelVar, numIndsVar, level1ID,
               allLevel2=True):
    """_summary_

    Args:
        dtClust (_type_): _description_
        cLevelVar (_type_): _description_
        numIndsVar (_type_): _description_
        level1ID (_type_): _description_
        allLevel2 (bool, optional): _description_. Defaults to True.

    Raises:
        Exception: _description_

    Returns:
        _type_: _description_
    """
    if dtClust is None:
        raise Exception("dtClust Missing")
    else:
        dtCopy = dtClust.copy()
    if isinstance(numIndsVar, int):
        dtCopy = dtCopy.append([dtCopy]*(numIndsVar-1),
                               ignore_index=True)
    elif isinstance(numIndsVar, str):
        for ind, row in dtCopy.iterrows():
            numb = row[numIndsVar] - 1
            dtCopy = dtCopy.append([row]*int(numb),
                                   ignore_index=True)
    dtCopy = dtCopy.sort_values(by=cLevelVar)
    dtCopy = dtCopy.reset_index(drop=True)
    dtCopy[level1ID] = dtCopy.index
    if allLevel2:
        return dtCopy
    else:
        dtCopy = dtCopy[[cLevelVar, level1ID]]
        return dtCopy


def trtObserve(dt, formulas, logit_link=True, grpName="trtGrp"):
    """

    Args:
        dt (dataframe): dataframe to receive exposure
        formulas (list): list of strings for the number of formulas
        logit_link (bool, optional): _description_. Defaults to False.
        grpName (str, optional): _description_. Defaults to "trtGrp".
    """

    assert dt is not None, "DtName is missing!"
    assert grpName not in dt.columns, "Group name has previously"
    +"been defined in data table"

    if not isinstance(formulas, list):
        formulas = [formulas]

    dtcopy = dt.copy()
    # TODO check this, it's declared but not used
    ncols = dtcopy.shape[1]

    ncat = len(formulas)
    ddef = pd.DataFrame()

    for i in range(0, ncat):
        ddef = defData(ddef, varname="e"+str(i), dist="nonrandom",
                       formula=formulas[i])

    dtnew = addColumns(ddef, dtcopy)
    # create new dataframe to calculate probs with
    dtTemp = dtnew.iloc[:, -ncat:]

    if logit_link:
        dtTemp = dtTemp.apply(lambda x: np.exp(x))
        dtTemp = dtTemp.apply(lambda x: x / (1+sum(x)), axis=1)
        # dtTemp['last_category'] = dtTemp.ap
        dtTemp['last_category'] = dtTemp.apply(
            lambda x: 1 - x.sum(), axis=1)

    dtTemp[grpName] = dtTemp.apply(
        lambda x: np.random.choice(a=len(x), size=1, p=x), axis=1)

    dt[grpName] = dtTemp[grpName].apply(lambda x: x[0])

    return dt


def stratSamp(nrow: int, ncat: int, ratio=None):
    """Randomly assign treatment groups to elements of a stratum

    Helper function called by trtobserve which randomly assigns a
    treatment group to the elements of a given stratum.

    Args:
        nrow (int): Number of rows in the stratum

        ncat (int): number of treatment categories to apply

        ratio (int or list): vector of values indicating
        relative proportion of group assignment. If nothing passed,
        defaults to None and the returning vector is an evenly
        distributed treatment to the strata.

    Returns:
    A vector of length(nrow) containing the group assignments for
    each element of the stratum.
    """
    if ratio is None:
        ratio = np.repeat(1, ncat)
    n_each = math.floor(nrow / np.sum(ratio))
    n_each_arr = np.dot(n_each, ratio)
    distrx = []
    for i, times in zip(range(1, ncat+1), n_each_arr):
        for x in range(times):
            distrx.append(i)
    extra = nrow - len(distrx)
    strata = distrx
    if extra > 0:
        strata.append(np.random.choice(distrx, extra))
    np.random.shuffle(strata)

    # if there are 2 categories only, values are 0,1
    if ncat == 2:
        strata = [val - 1 for val in strata]

    return strata


def addStrataCode(dt, strata):
    """add strata code to data table. Each integer represents a
    unique combination of the stratifying variables.

    Example:
    if strata = 'male' , there will only be 2 strata
    if strata = ['male' 'unemployed'] there will be 4 strata

    Args:
        dt (dataframe): original dataframe to manipulate
        strata (string or list of strings): list of columns to
        create strata by

    returns:
    modified dataframe with strata column added
    """
    dtcopy = dt.copy()
    # if isinstance(strata, str):
    #     N = 1
    # elif isinstance(strata, list):
    #     N = len(strata)
    dtstrata = dtcopy.groupby(strata).size().reset_index()
    dtstrata['strata_num'] = dtstrata.index+1
    dtcopy = dtcopy.merge(dtstrata, on=strata)
    dtcopy = dtcopy.drop(0, axis=1)
    return dtcopy


def trtStepWedge(dtName, clustID, nWaves, lenWaves,
                 startPer, perName="period", grpName="rx",
                 lag=0, xrName="xr"):
    """_summary_

    Args:
        dtName (_type_): _description_
        clustID (_type_): _description_
        nWaves (_type_): _description_
        lenWaves (_type_): _description_
        startPer (_type_): _description_
        perName (str, optional): _description_. Defaults to "period".
        grpName (str, optional): _description_. Defaults to "rx".
        lag (int, optional): _description_. Defaults to 0.
        xrName (str, optional): _description_. Defaults to "xr".
    """
    if lag == 0:
        # TODO this is assigned but not used
        xrName = 'xr'

    assert dtName is not None, "DtName is missing!"
    assert grpName not in dtName.columns, "Group name has previously"
    +"been defined in data table"
    assert perName in dtName.columns, "Period name has not been"
    +"defined in data table"

    dd = dtName.copy()

    nClust = len(dd[clustID].unique())
    nPer = len(dd[perName].unique())
    cPerWave = nClust / nWaves

    assert nClust % nWaves == 0, \
        "Cannot create equal size waves with"+str(nClust)+"\
            clusters and"+str(nWaves)+"waves."

    if (nPer < (startPer+(nWaves - 1) * lenWaves+1)):
        raise Exception("Design requires"
              + str((startPer + (nWaves - 1) * lenWaves + 1))
              + "periods but only"+str(nPer)+"generated")

    startTrt = np.repeat([(x*lenWaves)+startPer for x in range(nWaves)],
                         cPerWave)

    dstart = pd.DataFrame(data={clustID: range(1, nClust+1),
                                'startTrt': startTrt})

    dd = dd.merge(dstart)

    # dd['xr'] = [((dd[perName] >= dd[startTrt]) & (dd[perName] < (dd[
    # startTrt] + lag))) * 1]
    # dd['rx'] = [((dd[startTrt] + lag) <= dd[perName]) * 1]
    dd['xr'] = np.where((dd[perName] >= dd['startTrt']) &
                        (dd[perName] < (dd['startTrt'] + lag)), 1, 0)

    dd['rx'] = np.where(((dd['startTrt'] + lag) <= dd[perName]), 1, 0)

    if lag == 0:
        dd.drop('xr', axis=1, inplace=True)

    return dd
