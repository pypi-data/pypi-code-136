from typing import Union

from loozr_sdk.utils.account import LZR_MIXER_ACCOUNT_ID, \
    LZR_FACTORY_MIXER_ACCOUNT_ID
from loozr_sdk.utils.constants import BASE_TEN, DEFAULT_TOKEN_DECIMAL


def get_expanded_notation(flt):
    str_vals = str(flt).split('e')
    if len(str_vals) > 1:
        coef = float(str_vals[0])
        exp = int(str_vals[1])
        return_val = ''
        if int(exp) > 0:
            return_val += str(coef).replace('.', '')
            return_val += ''.join(
                ['0' for _ in range(
                    0, abs(exp - len(
                        str(coef).split('.')[1])))])
        elif int(exp) < 0:
            return_val += '0.'
            return_val += ''.join(
                ['0' for _ in range(0, abs(exp) - 1)])
            return_val += str(coef).replace('.', '')
        return return_val
    else:
        return flt


def balance_format(
        amount: Union[str, int],
        decimal=DEFAULT_TOKEN_DECIMAL) -> Union[float, int]:
    """
    Converts account balance from an internal
    indivisible unit to NEAR or any value depending
    on the value passed to as an argument to `decimal`

    Parameters
    ----------
    amount: str|int
        balance amount to be converted
    decimal: int
        token decimal places
    Returns
    -------
    int
        The amount of balance
    """
    return int(amount) / pow(BASE_TEN, decimal)


def yocto_format(amount: Union[float, int]) -> int:
    return amount * pow(BASE_TEN, DEFAULT_TOKEN_DECIMAL)


def get_account_id_from_name(account_name):
    return "%s.%s" % (account_name, LZR_MIXER_ACCOUNT_ID)


def get_creator_account_id_from_name(account_name):
    return "%s.%s" % (account_name, LZR_FACTORY_MIXER_ACCOUNT_ID)
