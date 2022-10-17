# -*- encoding:utf-8 -*-
import datetime, pdb
import pandas as pd
import numpy as np
import six
from jdw import DBAPI
from jdw.kdutils.singleton import Singleton
from jdw.mfc.lombard.indicator.atr import atr14, atr21
from jdw.mfc.lombard.indicator.symbol_pd import _benchmark


@six.add_metaclass(Singleton)
class Atomic(object):

    def __init__(self, market_trade_year=252):
        self._kd_engine = DBAPI.FetchEngine.create_engine('kd')
        self._market_trade_year = market_trade_year

    def transform(self, market_data):
        market_data['date'] = pd.to_datetime(
            market_data['trade_date']).dt.strftime('%Y%m%d').astype(int)
        market_data['date_week'] = market_data['date'].apply(
            lambda x: datetime.datetime.strptime(str(x), '%Y%m%d').weekday())
        market_data['trade_date'] = pd.to_datetime(market_data['trade_date'])
        market_data['p_change'] = market_data['p_change'] * 100
        market_data = market_data.dropna(subset=['pre_close'])
        return market_data

    def prev_returs_impl(self, price_data, key, name):
        price_tb = price_data[key].unstack()
        price_tb.fillna(method='pad', inplace=True)
        return_tb = np.log(price_tb / price_tb.shift(-1))
        return_tb = return_tb.replace([np.inf, -np.inf], np.nan)
        return_tb = return_tb.stack().reindex(price_data.index)
        return_tb.name = name
        return return_tb

    def pre_impl(self, price_data, key, name):
        price_tb = price_data[key].unstack()
        price_tb.fillna(method='pad', inplace=True)
        return_tb = price_tb.shift(-1)
        return_tb = return_tb.stack().reindex(price_data.index)
        return_tb.name = name
        return return_tb

    def calc_atr(self, kline_df):
        kline_df['atr21'] = 0
        if kline_df.shape[0] > 21:
            # 大于21d计算atr21
            kline_df['atr21'] = atr21(kline_df['high'].values,
                                      kline_df['low'].values,
                                      kline_df['pre_close'].values)
            # 将前面的bfill
            kline_df['atr21'].fillna(method='bfill', inplace=True)
        kline_df['atr14'] = 0
        if kline_df.shape[0] > 14:
            # 大于14d计算atr14
            kline_df['atr14'] = atr14(kline_df['high'].values,
                                      kline_df['low'].values,
                                      kline_df['pre_close'].values)
            # 将前面的bfill
            kline_df['atr14'].fillna(method='bfill', inplace=True)

    def fut_index_market(self, codes, benchmark, begin_date, end_date,
                         columns):
        market_data = DBAPI.FutruesIndexMarketFactory(self._kd_engine).result(
            codes=codes + [benchmark],
            key='code',
            begin_date=begin_date,
            end_date=end_date,
            columns=columns)

        market_data = market_data.sort_values(
            by=['trade_date', 'code'], ascending=True).rename(columns={
                'CHGPct': 'chgPct',
                'CHG': 'chg'
            })
        if 'turnoverValue' in market_data.columns and 'turnoverVol' in market_data.columns:
            market_data['vwap'] = market_data['turnoverValue'] / market_data[
                'turnoverVol']

        pre_close = self.pre_impl(
            market_data.set_index(['trade_date', 'code']), 'closePrice',
            'pre_close').reset_index()
        pre_close['trade_date'] = pd.to_datetime(pre_close['trade_date'])

        prev_rets = self.prev_returs_impl(
            market_data.set_index(['trade_date', 'code']), 'closePrice',
            'pre1_ret').reset_index()
        prev_rets['trade_date'] = pd.to_datetime(prev_rets['trade_date'])

        market_data = market_data.merge(prev_rets,
                                        on=['trade_date', 'code'
                                            ]).merge(pre_close,
                                                     on=['trade_date', 'code'])

        market_data = market_data.rename(
            columns={
                'preSettlePrice': 'pre_settle',
                'openPrice': 'open',
                'highestPrice': 'high',
                'lowestPrice': 'low',
                'closePrice': 'close',
                'settlePrice': 'settle',
                'turnoverVol': 'volume',
                'turnoverValue': 'value',
                'vwap': 'vwap',
                'pre1_ret': 'p_change'
            })
        market_data = self.transform(market_data=market_data)

        return market_data

    def transform_benchmark(self, market_data, benchmark, n_fold):
        benchmark_kl_pd = market_data.reset_index().set_index(
            'code').loc[benchmark].reset_index().set_index('trade_date')
        benchmark_kl_pd['key'] = list(range(0, len(benchmark_kl_pd)))
        self.calc_atr(benchmark_kl_pd)
        ind = benchmark_kl_pd.key.values[
            -1] - self._market_trade_year * n_fold + 1
        start_date = benchmark_kl_pd.index[ind]
        benchmark_kl_pd = benchmark_kl_pd.loc[start_date:]
        benchmark_kl_pd.name = str('benchmark')
        return benchmark_kl_pd

    def transform_code(self, market_data, benchmark, benchmark_kl_pd):
        pick_kl_pd_dict = {}
        choice_symbols = [
            code for code in market_data.code.unique().tolist()
            if code != benchmark
        ]
        for code in choice_symbols:
            kl_pd = market_data.reset_index().set_index(
                'code').loc[code].reset_index().set_index('trade_date')
            kl_pd.index = pd.to_datetime(kl_pd.index)
            kl_pd.name = str(code) + '0'
            if benchmark_kl_pd is not None:
                kl_pd = _benchmark(kl_pd, benchmark_kl_pd)
            self.calc_atr(kl_pd)
            kl_pd['key'] = list(range(0, len(kl_pd)))
            pick_kl_pd_dict[str(code) + '0'] = kl_pd
        return pick_kl_pd_dict

    def run(self, codes, benchmark, begin_date, end_date, columns, n_fold):
        market_data = self.fut_index_market(codes=codes,
                                            benchmark=benchmark,
                                            begin_date=begin_date,
                                            end_date=end_date,
                                            columns=columns)
        benchmark_kl_pd = self.transform_benchmark(market_data=market_data,
                                                   benchmark=benchmark,
                                                   n_fold=n_fold)
        pick_kl_pd_dict = self.transform_code(market_data=market_data,
                                              benchmark=benchmark,
                                              benchmark_kl_pd=benchmark_kl_pd)
        pick_kl_pd_dict['benchmark'] = benchmark_kl_pd
        return pick_kl_pd_dict