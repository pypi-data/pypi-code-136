import re
from tqdm import tqdm


def remove_company_connector(string):
    string = re.sub("(.+) as a? ?management agent for (.+)", "\\2 /-/ \\1", string) # Remove any appareance of as management agent for
    string = re.sub("(.+) successor in interest to (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) [as ]?assignee of (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) [as ]?managing agent for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) [as ]?m/a for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) by (.+) as managing agent$", "\\1 /-/ \\2", string)
    string = re.sub("(.+) a[^A-z]?s[^A-z]?o[^A-z]? (.+)", "\\2 /-/ \\1", string) # Remove any appearance of a.s.o. and what follows
    string = re.sub("(.+) d[^A-z]?b[^A-z]?a[^A-z]? (.+)", "\\2 /-/ \\1", string) # Remove any appearance of d.b.a and what follows
    string = re.sub("(.+) as agent for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) agent for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) as mg agent for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) mg agt (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) as managing for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) asset\.? management for (.+)", "\\2 /-/ \\1", string)
    string = re.sub("(.+) doing business as (.+)", "\\2 /-/ \\1", string)

    return string


def separate_company_names(names):
    plaintiffs = []
    plaintiff_parents = []
    
    for name in tqdm(names):
        split_names = re.split(" /-/ ", remove_company_connector(name))

        plaintiff_parents.append(split_names[1])  if(len(split_names) == 2)  else  plaintiff_parents.append('') 
        plaintiffs.append(split_names[0])

    return(plaintiffs, plaintiff_parents)



