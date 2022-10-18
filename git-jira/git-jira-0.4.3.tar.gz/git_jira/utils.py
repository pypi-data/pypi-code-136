from prettytable import PrettyTable

INDICATOR = '>'

def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

def print_table(columns, rows):
    table = PrettyTable(field_names=columns)
    table.add_rows(rows)
    table.align = "l"
    return table
