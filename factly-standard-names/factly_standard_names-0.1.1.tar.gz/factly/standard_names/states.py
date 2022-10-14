import json
from pathlib import Path

import pandas as pd
from fuzzywuzzy import fuzz, process


def getIndexes(dfObj, value):
    """Get index positions of value in dataframe i.e. dfObj."""
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col]].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos


def state_std_names(
    dfObj, column_name, thresh=70, manual_changes={}, identifier="None"
):
    """
    find all improper state names from a given dataframe
    and replaces it with standard names proved.
    dfObj : DataFrame object on which states name should be standardize
    column_name : name of column which has entries as state name
    manual_changes = Dict , default : null dict , changes in names done manually.
    """

    # name of excel file from where standard reference is adopted
    lib_path = str(Path(__file__).resolve().parents[0])
    file_name = lib_path + "/state.csv"

    # importing excel file
    # address will change when project move to library
    # names_file_path = str(project_dir) + "/data/raw/" + file_name
    proper_name = pd.read_csv(file_name)["state"].tolist()
    proper_name = [name.strip() for name in proper_name]

    improper_name = dfObj[column_name].tolist()
    improper_name = list(set(improper_name))

    # Dictionaries will have key value pair as improper and proper name
    logs = {}
    changes = {}
    corrupt = {}
    # will probably create filters for ratio
    for query in improper_name:
        match = process.extractOne(
            query.strip(), proper_name, scorer=fuzz.token_set_ratio
        )
        if match[1] >= thresh:
            changes[query] = match[0]
        else:
            if query not in manual_changes.keys():
                corrupt[query] = ""

    changes.update(manual_changes)

    # Provide the corrupt_names.json at the same folder where script is
    if bool(corrupt):
        print(
            "There are improper names that function can't fix.\nPlease refer to logs.json."
        )

    logs.update({identifier: {"changes": changes, "corrupt": corrupt}})

    with open("standard_names.log", "a+") as log_file:
        log_file.write(json.dumps(logs) + "\n")

    # replacing values that needs to be changes only to specific column
    dfObj = dfObj.replace({column_name: changes})

    return dfObj


def state_abbr_std_names(dfObj, column_name, manual_changes={}, identifier="None"):

    """
    find all state names from respective state abbreviation from a given dataframe
    and replaces it with standard names proved.
    dfObj : DataFrame object on which states abbreviation should be standardize
    column_name : name of column which has entries as state abbreviation
    manual_changes = Dict , default : null dict , changes in names done manually.
    """

    # name of csv file from where standard reference is adopted
    lib_path = Path(__file__).resolve().parents[0]
    file_path = lib_path / "states-and-abbreviations.csv"

    df_map = pd.read_csv(file_path)
    proper_names = df_map[df_map.columns[1]].to_list()

    improper_names = dfObj[column_name].unique()

    # Dictionaries will have key value pair as improper and proper name
    logs = {}
    changes = {}
    corrupt = {}

    for query in list(improper_names):
        if query in list(proper_names):
            changes[query] = df_map.loc[
                (df_map[df_map.columns[1]] == query), "state"
            ].values[0]
        else:
            if query not in manual_changes.keys():
                corrupt[query] = ""

    changes.update(manual_changes)

    # Provide the corrupt_names.json at the same folder where script is
    if bool(corrupt):
        print(
            "There are improper names that function can't fix.\nPlease refer to logs.json."
        )

    logs.update({identifier: {"changes": changes, "corrupt": corrupt}})

    with open("standard_names.log", "a+") as log_file:
        log_file.write(json.dumps(logs) + "\n")

    # replacing values that needs to be changes only to specific column
    dfObj = dfObj.replace({column_name: changes})

    return dfObj
