import pandas as pd
import requests
from datetime import datetime


def get_month(month_str):
    if month_str == 'JAN':
        return 1
    if month_str == 'FEB':
        return 2
    if month_str == 'MAR':
        return 3
    if month_str == 'APR':
        return 4
    if month_str == 'MAY':
        return 5
    if month_str == 'JUN':
        return 6
    if month_str == 'JUL':
        return 7
    if month_str == 'AUG':
        return 8
    if month_str == 'SEP':
        return 9
    if month_str == 'OCT':
        return 10
    if month_str == 'NOV':
        return 11
    if month_str == 'DEC':
        return 12

def retrieve_instruments(currency, expired=False):
    assert currency in ["ETH", "SOL", "BTC"]
    expired = "true" if expired else "false"
    instruments = requests.get(
        f"https://deribit.com/api/v2/public/get_book_summary_by_currency?currency={currency}&kind=option"
    ).json()["result"]
    return instruments



def create_derivatives_for_instrument_dic(instrument_data, initial_asset_price):
    name = instrument_data["instrument_name"]
    if (
        not (name.endswith("C") or name.endswith("P"))
        or (instrument_data["bid_price"] is None)
        or (instrument_data["ask_price"] is None)
    ):
        return None
    strike = int(name.split("-")[-2])
    maturity = name.split("-")[-3]
    best_bid = instrument_data["bid_price"] * initial_asset_price
    best_ask = instrument_data["ask_price"] * initial_asset_price
    info = {"instrument_data": instrument_data}

    volume = instrument_data["volume"]
    long_payoff_fun = None
    short_payoff_fun = None
    # call
    type = None
    if name.endswith("C"):
        type = 'CALL'
        # long
        long_payoff_fun = lambda x: max(0, x - strike) - best_ask
        # short
        short_payoff_fun = lambda x: best_bid - max(0, x - strike)
    else:  # put
        type = 'PUT'
        # long
        long_payoff_fun = lambda x: max(0, strike - x) - best_ask
        # short
        short_payoff_fun = lambda x: best_bid - max(0, strike - x)

    deriv_dic ={
        'name': name + "_LONG",
        'type' : type,
        'volume': volume,
        'strike':strike,
        'best_bid': best_bid,
        'best_ask': best_ask,
        'maturity': maturity,
        'long_payoff_fun':long_payoff_fun,
        'short_payoff_fun':short_payoff_fun

    }

    return deriv_dic


def create_derivatives_from_instrument_data(data, initial_asset_price, long_only):
    assert type(data) == list
    derivatives = []
    for instrument in data:
        long_deriv, short_deriv = create_derivatives_for_instrument(
            instrument, initial_asset_price
        )
        if long_deriv is None or short_deriv is None:
            continue
        derivatives.append(long_deriv)
        if not long_only:
            derivatives.append(short_deriv)
    return derivatives


def create_derivatives_from_instrument_data_df(data, initial_asset_price, long_only):
    assert type(data) == list
    derivatives = []
    for instrument in data:
        deriv_dic = create_derivatives_for_instrument_dic(
            instrument, initial_asset_price
        )
        if deriv_dic is None :
            continue
        derivatives.append(deriv_dic)
    derivatives_df = pd.DataFrame().from_dict(derivatives)

    def compute_proper_maturity(row):
        maturity = row['maturity']
        monht_str = maturity[-5:-2]

        me_date = datetime(year= int(maturity[-2:]) + 2000, month=get_month(monht_str),day=int(maturity[:-5]))
        return me_date

    derivatives_df['maturity_date'] = derivatives_df.apply(compute_proper_maturity, axis = 1)
    derivatives_df = derivatives_df.sort_values(by ='maturity_date')
    return derivatives_df

def retrieve_and_create_derivatives(currency, initial_asset_price, long_only):
    instruments = retrieve_instruments(currency)
    derivs = create_derivatives_from_instrument_data(
        instruments, initial_asset_price, long_only
    )
    return derivs

def retrieve_and_create_derivatives_df(currency, initial_asset_price, long_only):
    instruments = retrieve_instruments(currency)
    derivs = create_derivatives_from_instrument_data_df(
        instruments, initial_asset_price, long_only
    )
    return derivs
