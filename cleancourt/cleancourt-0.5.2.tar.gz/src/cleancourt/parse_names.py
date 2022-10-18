from loguru import logger
import probablepeople as pp
from tqdm import tqdm
import pandas as pd
import json
import re
from cleancourt.filter_types import filter_people


def format_people_names(df):

    '''Take in a list or df of one column and return a dictionary with each name in First Last format'''

    # Group data by exact matches and count the number of values
    logger.info("GROUPING DATA")
    grouped_df = df.value_counts().rename_axis('first_plaintiff').reset_index(name='counts')

    # Grab the names of each plaintiff and place into a list
    # Note: Order of this list does matter. 
    # Names are prioritized based on the number of exact matches in the document

    names = grouped_df.first_plaintiff
    
    names_dict = {}

    # Iterate over names

    for name in tqdm(names):
        
        # Check if name is a person
        is_person = filter_people(name)
        
        # If is a person, grab name components from parsed names and place in a common format
        if(is_person):
            val = pp.tag(name)
            try:
                firstI = val[0]['FirstInitial']
            except KeyError:
                firstI = ""

            try:
                first = val[0]['GivenName']
            except KeyError:
                first = ""
            
            try:
                middle = val[0]['MiddleName']
            except KeyError:
                middle = ""
            
            try:
                middleI = val[0]['MiddleInitial']
            except KeyError:
                middleI = ""

            try: 
                last = val[0]['Surname']
            except KeyError:
                last = ""

            try: 
                suffix = val[0]['SuffixGenerational']
            except KeyError:
                suffix = ""

            full_name = firstI + " " + first + " " + middle + " " + middleI +" " + last + " " + suffix

            names_dict[name] = re.sub(" +", " ", full_name.strip())

    return names_dict

