import ftfy
import re

def clean_data(string):
    '''Takes in a string and cleans it using regex and other standard functions'''

    if not isinstance(string, str): 
        string = ""

    string = ftfy.fix_text(string) # Fix text to ensure any non-ascii characters appear properly
    string = string.encode("ascii", errors="ignore").decode() # Remove these non-ascii characters
    string = string.lower() # Convert all characters to lowercase

    chars_to_remove = [")", "(", "[", "]", "{", "}", "'", "#", ";"] # remove these characters    
    rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
    string = re.sub(rx, '', string)

    # Replace special characters and symbols
    string = string.replace('&', 'and') 
    string = string.replace('@', 'at')
    string = string.replace('h/w', '') # Sometimes appears next to party names that are husband (h) and wife (w)
    
    
    string = re.sub(' +', ' ', string).strip() # Remove multiple spaces and spaces at the end of a word

    string = re.sub("^the ", "", string) # Remove 'the' at the beginning of party names
    string = re.sub(' i+ ', ' ', string) # Remove one or more 'i' characters that appear in isolation (denotes numbers)

    
    

    string = re.sub(' c/o.*', '', string) # Remove care of


    string = re.sub(" corporation(\s|$)", " corp\\1", string) # shorten corporation to corp
    string = re.sub(" company(\s|$)", " co\\1", string) # shorten company to co
    string = re.sub(" maa?nage?ment(\s|$)", " mgmt\\1", string)  # etc
    string = re.sub(" incorporated(\s|$)", " inc\\1", string)
    string = re.sub(" apartments(\s|$)", " apts\\1", string)
    string = re.sub( " square(\s|$)", " sq\\1", string)
   
    

    string = re.sub(" et\.?\s?al\.?$", "", string)
    string = re.sub( "p\.?c\.?$", "", string) # Remove P.C. (Personal Corporation) abbreviation on the end of a name
    

    string = re.sub( "\.", "", string) # Remove any periods

    return(string)
