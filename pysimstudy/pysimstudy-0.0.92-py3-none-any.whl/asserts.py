# LINK TO R FILE: https://github.com/kgoldfeld/simstudy/blob/main/R/asserts.R
import pandas as pd
import numpy as np


def dots2argNames(vars: dict = {}):
    """
    Only used within Asserts file

    vars - Any number of variables as named elements
    e.g. {var1name : var1arg}

    returns a list containing the arguments and names. # @ainesh1993
    """
    assert len(vars) != 0, 'Empty dictionary passed'
    args = list(vars.values())
    names = list(vars.keys())
    assert '' not in names, 'Empty key passed'
    return {'args': args, 'names': names}


def assertLength(vars: dict = {}, length: int = 0):
    """

    Checks if all passed values in vars are of length 'length'. Caveat:
    length(matrix) = number of elements but length(data.frame) = number
    of columns.

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()
        length (int): an interger measurement the var length
        should match (default = 0)

    Return: nothing if assert passes or error if assert fails
    """
    dots = dots2argNames(vars)
    print(f"vars: {dots}")
    print(dots['args'])
    for arg in list(dots['args']):
        print(arg)
        print(len(arg))
        assert len(arg) == length, 'All lists must be of length {}\
            '.format(length)


def assertClass(vars: dict = {}, class_to_check=None):
    """
    Check for Class equality

    Checks if all passed vars inherit from class.

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()
        class_to_check (class) : Class to check against. (default = None)

    Return: nothing if assert passes or error if assert fails

    """
    dots = dots2argNames(vars)

    for arg in list(dots['args']):
        assert type(arg) == class_to_check, 'All elements must be of class {}\
            '.format(str(class_to_check))


def assertType(vars: dict = {},
               type_to_check: object = str, deep: bool = True):
    """
    Checks if values in vars are of type type_to_check

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()
        type_to_check(object): a variable type e.g str, int, float
        (default = str)
        deep (bool): boolean e.g True, False (default = True)

    Return: nothing if assert passes or error if assert fails
    """
    dots = dots2argNames(vars)
    # TODO deep seems to be useless, execution order seems
    # irrelevant. check if we can do this without deep arg
    if deep:
        for arg in list(dots['args']):
            if type(arg) == list:
                assert all(type(i) == type_to_check for i in arg), '\
                    All elements must be of type {}'.format(str(type_to_check))
            else:
                assert type(arg) == type_to_check, 'All elements \
                    must be of type {}'.format(str(type_to_check))
    else:
        for arg in list(dots['args']):
            assert type(arg) == type_to_check, 'All elements must \
                be of type {}'.format(str(type_to_check))


def assertNumeric(vars: dict = {}):
    """
    Checks if values in vars are numeric

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()

    Return: nothing if assert passes or error if assert fails

    """
    dots = dots2argNames(vars)
    for arg in list(dots['args']):
        if type(arg) == list:
            assert all(type(i) in [int,
                       float, complex] for i in arg), 'All elements \
                           must be numeric'
        else:
            assert type(arg) in [int, float, complex], 'All \
                elements must be numeric'


def assertInteger(vars: dict = {}):
    """
    Checks if values in vars are integers

    Args:
    vars (dict): a dictionary arguement passed through dots2argNames()

    Return: nothing if assert passes or error if assert fails.

    """
    assertNumeric(vars)
    dots = dots2argNames(vars)
    for arg in list(dots['args']):
        if type(arg) == list:
            assert all(type(i) == int for i in arg), 'All elements \
                must be of type int'
        else:
            assert type(arg) == int, 'All elements must be of type int'


def assertValue(vars: dict = {}):
    """
    Checks if values in vars are not Null, NA, None, or 0

    Args;
        vars (dict): a dictionary arguement passed through dots2argNames()

    Return: nothing if assert passes or error if assert fails
    """
    dots = dots2argNames(vars)
    for arg in list(dots['args']):
        if type(arg) == list:
            assert all(arg), 'Cannot have null elements'
        else:
            assert all([arg]), 'Cannot have null elements'


def assertUnique(vars: dict = {}):
    """
    Checks if values in each key are unique.
        e.g {'a': [2, 2], 'b': [2, 4]} is not unique because of key 'a'
        e,g {'a': [3, 4], 'b': [3, 4]} is unique

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()

    Return: nothing if assert passes or error if assert fails
    """
    dots = dots2argNames(vars)
    for arg in list(dots['args']):
        if type(arg) == list:
            assert len(arg) == len(set(arg)), 'Must have unique elements'


def assertInDataTable(vars, df):
    """
    Checks if vars is a column name in a dataframe

    Args:
        vars (int, str, float, or list): variable or list of variables used
        to check if in columns of dataframe
        df (DataFrame): a dataframe used to check if vars are in column names.

    Return: nothing if assert passes or error if assert fails.
    """
    df_names = None
    if type(df) == pd.DataFrame:
        df_names = list(df.columns)
    else:
        df_names = df

    if type(vars) == list:
        assert all(i in df_names for i in vars), 'Variables not \
            found in dataframe column names'
    else:
        assert vars in df_names, 'Variable {} not found in dataframe\
             column names'.format(vars)


def assertNotInDataTable(vars, df):
    """
     Checks if vars is not a column name in a dataframe

    Args:
        vars (int, str, float, or list): variable or list of variables
        used to check if in columns of dataframe
        df (DataFrame): a dataframe used to check if vars are in column names.

    Return: nothing if assert passes or error if assert fails
    """
    df_names = None
    if type(df) == pd.DataFrame:
        df_names = list(df.columns)
    else:
        df_names = df

    if type(vars) == list:
        assert all(i not in df_names for i in vars), 'Variables \
            already defined in dataframe column names'
    else:
        assert vars not in df_names, 'Variable {} already defined \
            in dataframe column names'.format(vars)


def assertAscending(vec):
    """
    Checks if vector is in ascending order

    Args:
    vec (list of ints, floats, or str): List of variables of types
    that can be compared.

    Return: nothing if assert passes. Returns TypeError if list
    contains variables of types that are uncomparable
    """
    assert all(vec[i] <= vec[i+1] for i in range(len(vec) - 1)), 'Ve\
        ctor is not in ascending order'


def assertDescending(vec):
    """
   Checks if vector is in descending order

    Args:
    vec (list of ints, floats, or str): List of variables of types
    that can be compared.

    Return: nothing if assert passes. Returns TypeError if list
    contains variables of types that are uncomparable
    """
    assert all(vec[i] >= vec[i+1] for i in range(len(vec) - 1)), 'Ve\
        ctor is not in descending order'


def assertPositive(vec):
    """
    Checks if values in vector are all positive

    Args:
    vec (list of numeric values): a list of numeric values passed for
     positive check

    Return: nothing if assert passes or error if assert fails
    """
    assert all(vec[i] >= 0 for i in range(len(vec))), 'All values \
        in vector must be positive'


def assertProbability(vec):
    """
    Checks if all values in vector are between 0 and 1

    Args:
        vec (list of numeric values): a list of numeric values
        to check if between 0 and 1

    Return: nothing if assert passes or error if assert fails
    """
    assert all(vec[i] >= 0
               and vec[i] <= 1
               for i in range(len(vec))), 'All values in vector \
                   must be probabilities (>=0 and <=1)'


def ensureLength(vars: dict = {}, n: int = 1):
    """
    Ensures the length of one variable

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()
        n (int): the measurement the variable length should match.
        (default = 1)

    Return: nothing if function passes or error if fuction fails.

    """
    dots = dots2argNames(vars)
    if len(dots['args']) != 1:
        raise ValueError('Must pass only one variable')

    var = dots['args'][0]
    if type(var) == list:
        assert len(var) == n, 'List must be of leng\
            th {}'.format(str(n))
        return(var)
    else:
        return([var for i in range(n)])


def ensureMatrix(var: list):
    """
    Ensures a variable is assigned to a matrix.
    Takes any list or dataframe and returns it as
    a numpy array.

    var - Variable to check

    returns - np array
    """
    if type(var) not in [pd.DataFrame, list]:
        raise ValueError('Must pass a dataframe or list')

    return np.array(var)


def assertPositiveDefinite(matrix):
    """
    Checks if Matrix is positive definite

    A matrix is positive definite if it is symmetric
    and all of its eigenvalues are positive. This means
    that the matrix vectors will always expand in the same
    direction regardless of what scalar is used to transform
    it.

    Args
    matrix -  The matrix to check for positive definite

    Returns
    Nothing if matrix is positive definite, error if it is not
    """

    if len(matrix) != 1:
        raise ValueError('Must pass only one variable')
    matrixT = np.transpose(matrix)
    if matrix.shape() != matrixT.shape():
        raise Exception("Matrix is not symmetric")
    if not np.all(matrix == matrixT):
        raise Exception("Matrix is not symmetric")
    w = np.linalg.eigvals(matrix)
    if not np.all(w > 0):
        raise ValueError('Matrix is not positive definite')


def assertInRange(vars: dict = {}, vrange: tuple = (0, 1)):
    """
    Checks if values in vars are in a certain range

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()
        vrange (tuple): a tuple of two ints setting the range parameter
        for the vars to fall in (default= (0,1))

    Return: nothing if assert passes or an error if assert fails.

    """
    assertNumeric(vars)
    assertLength({'vrange': vrange}, 2)

    dots = dots2argNames(vars)
    min_val = vrange[0]
    max_val = vrange[1]

    for arg in dots['args']:
        if type(arg) == list:
            assert all(i >= min_val and i <= max_val for i in arg), '\
                All values need to be between {} \
                    and {}'.format(str(min_val), str(max_val))
        else:
            assert arg >= min_val and arg <= max_val, 'All values \
                need to be between {} and\
                     {}'.format(str(min_val), str(max_val))


def ensureOption(vars: dict = {}, options: list = [], default_val: object = 1):
    """
    Ensures values in vars are also in options

    Args:
        vars (dict): a dictionary arguement passed through dots2argNames()
        options (list): a list of values used to test if vars matches
        (default = [])
        default_val (object): value that will be returned

    Return: Value if in options or default_val
    """
    dots = dots2argNames(vars)
    if len(dots['args']) != 1:
        raise ValueError('Must pass only one variable')

    value = dots['args'][0]
    if type(value) == list:
        for x in range(len(value)):
            if value[x] not in options:
                value[x] = default_val
    else:
        if value not in options:
            value = default_val

    return value
