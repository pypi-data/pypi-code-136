import yaml


def yml2dict(file):
    """
    Open yaml file and return as dict

    input:
    file --  the yaml input file

    output:
    dic -- the content of the yaml file as a python dictionary
    """

    with open(file, 'r') as f:
        # The FullLoader parameter handles the conversion from YAML scalar values to Python the dictionary format
        dic = yaml.load(f, Loader=yaml.FullLoader)

    return dic