#!/usr/bin/python

"""A set of functions to make working with Python Pandas a little easier,
and to collect idioms and patterns that are useful."""

import pandas
import dateutil

###### Functions ######

# Collect the elements of a series by type - may be used for counting, but
# also has utility for testing for maximum and minimum values in 
# mixed-composition series

def byType( series , printout=False ):
    integers = []
    strings = []
    floats = []
    booleans = []
    nones = []
    others = []

    for element in series:
        if type(element) == int:
            integers.append(element)
        elif type(element) == str:
            strings.append(element)
        elif type(element) == float:
            floats.append(element)
        elif type(element) == bool:
            booleans.append(element)
        elif type(element) == None:
            nones.append(element)
        else:
            others.append(element)
    
    output = {
                "integers":integers,\
                "strings":strings,\
                "floats":floats,\
                "booleans":booleans,\
                "nones":nones,\
                "others":others\
            }

    if printout == True:
        po = f"Integers: {len(output['integers'])}\n"
        po = po + f"Strings: {len(output['strings'])}\n"
        po = po + f"Floats: {len(output['floats'])}\n"
        po = po + f"Booleans: {len(output['booleans'])}\n"
        po = po + f"Nones: {len(output['nones'])}\n"
        po = po + f"Others: {len(output['others'])}\n"

        print(po)
    
    return output


# Take a column, run byType on it, and return the proportions of each type. 
# Mostly an intermediate step to looking for outliers, 
# minimum and maximum values, dates, etc.

def proportionOfTypes( columnname , printout=False ):
    mytypes = byType(columnname)
    total_length = len(columnname)
    int_prop = len(mytypes["integers"]) / total_length * 100
    str_prop = len(mytypes["strings"]) / total_length * 100
    float_prop = len(mytypes["floats"]) / total_length * 100
    boolean_prop = len(mytypes["booleans"]) / total_length * 100
    none_prop = len(mytypes["nones"]) / total_length * 100
    other_prop = len(mytypes["others"]) / total_length * 100

    output = {
                "integers"  :   int_prop,\
                "strings"   :   str_prop,\
                "floats"    :   float_prop,\
                "booleans"  :   boolean_prop,\
                "nones"     :   none_prop,\
                "others"    :   other_prop,\
                "mytypes"   :   mytypes\
            }

    if printout == True:
        po = f"Integers: {int_prop}%\n"
        po = po + f"Strings: {str_prop}%\n"
        po = po + f"Floats: {float_prop}%\n"
        po = po + f"Booleans: {boolean_prop}%\n"
        po = po + f"Nones: {none_prop}%\n"
        po = po + f"Others: {other_prop}%\n"

        print(po)

    return output


# Convert all elements of a list to some Type - useful for harmonizing list of 
# numbers for getting maximum and minimum values.

def typeCoerce( mylist , dtype=float ):
    return list(map(dtype, mylist))


# Return a dictionary with the maximum and minimum values of one or more lists.
# If not all of the values are the same type (intgers, floats) then we convert 
# all of the elements to floats and then return the maximum and minimum values.

def minMaxNumbers( *lists ):
    if len(lists) > 1:
        #print("Several lists.")
        list_element_types = []
        all_list_elements = []
        for lst in lists:
            for item in lst:
                list_element_types.append(type(item))
                all_list_elements.append(item)
        if len(set(list_element_types)) == 1:
            minimum = pandas.Series(all_list_elements).min()
            maximum = pandas.Series(all_list_elements).max()
        else:
            #print(all_list_elements)
            coerced_list = typeCoerce(all_list_elements)
            minimum = pandas.Series(coerced_list).min()
            maximum = pandas.Series(coerced_list).max()
        #print(lists)
    else:
        #print("Just one list.")
        minimum = pandas.Series(lists[0]).min()
        maximum = pandas.Series(lists[0]).max()
        
    return {"minimum":minimum, "maximum":maximum}


# Return a dictionary with the maximum and minimum values of one or more 
# lists of dates.

def minMaxDates( *lists ):
    def discardNonDates( listofdates ):
        justdates = []
        for item in listofdates:
            if pandas.notna(item):
                try:
                    justdates.append(dateutil.parser.parse(item, fuzzy=True))
                except:
                    pass

        return justdates

    if len(lists) > 1:
        all_list_elements = []
        for lst in lists:
            for item in lst:
                all_list_elements.append(item)       
    else:
        all_list_elements = lists[0]
    
    return {"minimum":pandas.Series(discardNonDates(all_list_elements)).min(),\
            "maximum":pandas.Series(discardNonDates(all_list_elements)).max()}


# Index on datetime column

def makeDateTimeIndex( dataframe , columnname ):
    """
    Usage example:
    hr = makeDateTimeIndex( pandas.read_csv("myCSVfile.csv"), "nameOfDateTimeColumnToIndexOn" )
    """
    dataframe[columnname] = pandas.to_datetime( dataframe[columnname] )
    dataframe = dataframe.set_index( dataframe[columnname] )

    return dataframe


# Plot rows over time, based on a rows-per-interval approach

def plotRowsOverTime( dataframe , frequency ):
    """
    The dataframe has to be using a datetime column as the index.
    You then specify the frequency that you are looking for results on, i.e.
    day, month, year, etc.
    Day = D
    Month = M
    Read "pandas Grouper" documentation for details.
    """
    dataframe.groupby(pandas.Grouper(freq=frequency)).size().plot()


# Look at a column and try to learn something about it.

def inspectColumn( columnname , printout=True ):
    """
    Look at the column, extract some information about it, and produce a set 
    of information that can be inferred without reading the whole column for 
    outliers, weirdness, values used to infer "not available", and whatever 
    else we can figure out automatically. 
    """
    info = {}
    column_types = proportionOfTypes(columnname)
    # Note that column_types is a dictionary with the following elements:
    # "integers, strings, floats, booleans, nones, others, mytypes."
    # The first six elements contain the percentage proportion of those types 
    # to the rest of the column, and mytypes is a nested dictionary with the 
    # same element names, but including lists of the elements of those types.
    
    info = {\
        "rowcount":len(columnname),\
        "factorcount":0,\
        "maxvalue":0,\
        "minvalue":0,\
        "minvalue":0,\
        "datecount":0,\
        "notdatecount":0,\
        "nullcount":0\
    }

    notdate = 0
    nulls = 0
    isdate = 0
    possible_dates = []

    for item in columnname:
        """Loop through the column, """
        #print(item)
        if pandas.notna(item):
            try:
                maybe_date = dateutil.parser.parse(item, fuzzy=True)
                if len(maybe_date) > 0:
                    isdate = isdate + 1
                    possible_dates.append(maybe_date)
            except:
                notdate = notdate + 1
        else:
            nulls = nulls + 1
    notdate = notdate + nulls
    info["notdatecount"] = notdate

    if len(possible_dates) > 0:
        min_max_dates = minMaxDates(columnname)
        column_max = min_max_dates["maximum"]
        column_min = min_max_dates["minimum"]
    elif column_types["strings"] == 0:
        min_max_numbers = minMaxNumbers(columnname)
        column_max = min_max_numbers["maximum"]
        column_min = min_max_numbers["minimum"]
    else:
        column_max = "No maximum"
        column_min = "No minimum"

    info["maxvalue"] = column_max
    info["minvalue"] = column_min

    codes, uniques = pandas.factorize(columnname)
    # We want to know how much of the column is nulls, so we keep them in the 
    # "uniques" list by changing the default behaviour of factorize.
    info["factorcount"] = len(uniques)
    if len(uniques) < 11:
        info["uniquevalues"] = uniques.values
        pairs = {}
        for uniq in uniques:
            pairs[uniq] = columnname.loc[columnname == uniq].count()
            proportionOfFactors = "Proportion of factors:\n"
            factorProps = {}
            for key in pairs:
                proportionOfFactors = proportionOfFactors + f"{key}:\t\t\t{pairs[key] / len(columnname) * 100}%\n"
                factorProps[key] = pairs[key] / len(columnname) * 100
            info["factorprops"] = factorProps
    else:
        #print("Ten factors or more.")
        proportionOfFactors = f"Too many factors to analyse automatically: {len(uniques)}\n"

    po = "Column Details:\n"
    po = po + f"Number of Rows: {len(columnname)}\n"
    po = po + f"Number Factors: {len(uniques)}\n"
    try:
        proportionOfFactors
        po = po + proportionOfFactors
    except:
        pass
    po = po + f"Maximun value: {column_max}\n"
    po = po + f"Minimum value: {column_min}\n"
    po = po + f"Number of possible dates: {isdate}\n"
    po = po + f"Number of non-dates: {notdate}\n"
    po = po + f"Number of nulls: {nulls}\n"

    if printout == True:
        print(po)
    
    return info


###### Patterns ######

## Connect two or more dataframes together that probably overlap, dropping 
## whatever is duplicated
#firstDataFrame = pandas.DataFrame()
#secondDataFrame = pandas.DataFrame()
#newDataFrame = pandas.concat( [firstDataFrame , firstDataFrame] ).drop_duplicates()
#
#
## Change the encoding of NotANumber on import - useful when your data has 
## inadvertent entries that are not null, like sodium (NA)
#from pandas._libs.parsers import STR_NA_VALUES
#
#disable_na_values = { "NA" }
#my_default_na_values = STR_NA_VALUES - disable_na_values
#df = pandas.read_csv( "myCSVfile.csv" , na_values = my_default_na_values )
#
#
## Pad out values with 4 leading zeros on pandas.read_csv()
#df = pandas.read_csv("myCSVfile.csv", converters={'UnpaddedColumn1': '{:0>4}'.format, 'UnpaddedColumn2': '{:0>4}'.format}) 
#
#
## Filter a dataframe into a subset that all meets a criteria.
## In the example case, we use pandas.factorize() to get all of the values, 
## because it _should_ be a small set, but there are mispellings, other 
## weirdness that we have to find, so this pattern lets us group all rows 
## that have the set of values in the list
#
#pos = ['DÉTECTÉ', 'DÉTEDÉTECTÉ', 'detecté', 'detecte', '03DÉTECTÉ']
#
#posCases = firstDataFrame[firstDataFrame["RESULTAT"].isin(pos)]

