import json

__all__ = ["dumps", "to_hex"]

def dumps(obj, pretty=False):
    d = json.dumps(obj, indent=4) if pretty else json.dumps(obj)
    if "\\" in d: return d.replace("\\\\", "\\")
    return d

def to_hex(obj, glue=r"\x"):
    if isinstance(obj, dict): return {to_hex(k, glue): to_hex(v, glue) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)): return [to_hex(v, glue) for v in obj]
    return "".join([r'{}{:02}'.format(glue, ord(c)) for c in str(obj)])