import logging
import numpy as np
from tabulate import tabulate
import pandas as pd


def test():
    nnn = 2
    assert generateListRows(nnn) == [[0, 1, 0, 1], [
        0, 0, 1, 1]], "Should be [[0, 1, 0, 1], [0, 0, 1, 1]]"
    assert generateListColumns(nnn) == [[0, 0], [1, 0], [0, 1], [
        1, 1]], "Should be [[0, 0], [1, 0], [0, 1], [1, 1]]"
    assert generateString(nnn) == "+-----+-----+----------+\n|  A  |  B  |  result  |\n+=====+=====+==========+\n|  0  |  0  |          |\n+-----+-----+----------+\n|  1  |  0  |          |\n+-----+-----+----------+\n|  0  |  1  |          |\n+-----+-----+----------+\n|  1  |  1  |          |\n+-----+-----+----------+", "should be +-----+-----+----------+\n|  A  |  B  |  result  |\n+=====+=====+==========+\n|  0  |  0  |          |\n+-----+-----+----------+\n|  1  |  0  |          |\n+-----+-----+----------+\n|  0  |  1  |          |\n+-----+-----+----------+\n|  1  |  1  |          |\n+-----+-----+----------+"
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("all went well")


def generateListRows(opt):
    """make a list of rows with all the options you can have with n amount of variables

    Args:
        opt (int/str than can be turned to int): number of variables to consider

    Returns:
        list: truth table in list format
    """
    opt = int(opt)
    tt, index, len, zo = [], 1, 1, [1, 0]
    for i in range(opt):
        len = len*2
    for i in range(opt):
        tt.append([])
        toggle = 0
        for j in range(len//index):
            for z in range(index):
                tt[i].append(toggle)
            toggle = zo[toggle]
        index = index*2
    return tt


def generateListColumns(opt):
    """make a list of columns with all the options you can have with n amount of variables

    Args:
        opt (int/str than can be turned to int): number of variables to consider

    Returns:
        list: truth table in list format
    """
    return np.array(generateListRows(opt)).transpose().tolist()


def generateString(opt):
    """make a string with all the options you can have with n amount of variables

    Args:
        opt (int/str that can be turned to int): number of variables to consider

    Returns:
        str: truth table in string format
    """
    alph = [chr(i) for i in range(ord('A'), ord('A')+opt)]
    l = generateListColumns(opt)
    for i in range(len(l)):
        l[i].append(' ')
    alph.append('result')
    return tabulate(l, headers=alph, tablefmt="grid", numalign="center", stralign="center")


def generateExcelFile(opt, dir, fileName="output", header=False, indexing=False):
    """convert n number of variables to a truth table in excel

    Args:
        opt (int/str that can be turned to int): number of variables to consider
        dir (str): the folder where it will save
        fileName (str, optional): name of the file without extension. Defaults to "output".
        header (bool, optional): If there are headers or not. Defaults to False.
        indexing (bool, optional): If there are indexes or not. Defaults to False.
    """
    alph, l, d = [chr(i) for i in range(
        ord('A'), ord('A')+opt)], generateListRows(opt), {}
    for i in range(len(l)):
        d[alph[i]] = l[i]
    pd.DataFrame(d).to_excel(f'{dir}\{fileName}.xlsx',
                             sheet_name=fileName, index=indexing, header=header)


def generateToTextFile(opt, dir, fileName="output"):
    """convert n number of variables to a truth table in text file

    Args:
        opt (int/str that can be turned to int): number of variables to consider
        dir (str): the folder where it will save
        fileName (str, optional): name of the file without extension. Defaults to "output".
    """
    with open(f'{dir}/{fileName}.txt', 'w') as f:
        f.write(generateString(opt))
