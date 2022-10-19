from .nadlan import load_page_from_nadlan
from .yad2 import load_estate, load_additional_info


def fetch(args):
    command = args['command']
    if command == 'load_estate':
        return load_estate(args)
    elif command == 'additional_info':
        return load_additional_info(False, args)
    elif command == 'nadlan.gov.il':
        return load_page_from_nadlan(args)
    else:
        return None
