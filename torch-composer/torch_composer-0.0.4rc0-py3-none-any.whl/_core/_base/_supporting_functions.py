
__module_name__ = "_supporting_functions.py"
__doc__ = """Supporting functions module."""
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu"])


# -- Supporting functions: ---------------------------------------------------------------
def as_list(item, n=1):
    if not isinstance(item, list):
        return [item] * n
    return item


def io_dim(hidden):

    keys = list(hidden.keys())

    input_connect = hidden[keys[0]][0]
    output_connect = hidden[keys[-1]][-1]
    n_hidden = len(keys)

    return input_connect, output_connect, n_hidden


def parse_kwargs(args, ignore=["self"]):
    kwargs = {}
    for arg, val in args.items():
        if not arg in ignore:
            kwargs[arg] = val
    return kwargs