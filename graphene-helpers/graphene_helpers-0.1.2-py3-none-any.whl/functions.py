import re

def get_fields(info):
    out_list = []
    for n in info.field_nodes[0].selection_set.selections:
        out_list.append(n.name.value)
    return out_list

def replace_empty(fields):
    for key in fields:

        if fields[key] == {}:
            fields[key] = True

        else:
            replace_empty(fields[key])

def process_to_lower_with_underscore(fields):
    new_fields = {}
    for key in fields:
        new_key = re.sub('([A-Z]{1})', r'_\1', key).lower()

        if fields[key] == {}:
            new_fields[new_key] = True

        else:
            new_fields[new_key] = process_to_lower_with_underscore(fields[key])
    
    return new_fields

def get_projection(info, to_lower_with_underscore=False):
    fields = get_fields(info)
    
    if to_lower_with_underscore:
        fields = process_to_lower_with_underscore(fields)
    else:
        replace_empty(fields)
    return fields