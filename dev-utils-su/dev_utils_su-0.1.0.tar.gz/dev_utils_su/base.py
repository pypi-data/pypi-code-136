import sys,typing


def exc_message(where: str = None):
    e_type, e_data, e_tb = sys.exc_info()
    return f"{where+' ' if where else ''}exception: {e_type}@{e_tb.tb_lineno if e_tb else ''} => {e_data}"


def list_attrs(obj, magic: bool = False):
    attrs = dir(obj)
    return (attrs if magic else [x for x in attrs if not x.startswith('_')])

