import pprint
import yaml


def op(label_or_var, var=None, format=False, yml=False):
    """
    short-hand override print() formatter

    @params
    label_or_var
    var=None
    format=False
    yml=False
    """
    try:
        if var and format:
            if yml:
                return print(f'\n{label_or_var}\n', yaml.dump(var))
            return print(f'\n{label_or_var}\n', pprint.pformat(var))
        if not var and format:
            if yml:
                return print('\n', yaml.dump(label_or_var))
            return print('\n', pprint.pformat(label_or_var))
        if var:
            return print(f'\n{label_or_var}\n', var, '\n')
        return print('\n', label_or_var, '\n')
    except Exception as error:
        print('\nopPrint internal error...')
        print(error, '\n')
