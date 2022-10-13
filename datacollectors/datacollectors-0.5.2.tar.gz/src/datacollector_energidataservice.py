from datetime import datetime, timedelta

import requests
import incentivedkutils as utils


def main():
    start_date = datetime(2022, 10, 1)
    end_date = datetime(2022, 10, 31)

    areas=['DK1','DK2']
    in_data=Energidataservice.production_consumption(areas, start_date,end_date)
    utils.prt(in_data[-10:])

    df = Energidataservice.production_consumption_df(areas, start_date, end_date)
    utils.prt(df.head())

    df = Energidataservice.production_consumption_df(['DK1'], start_date, end_date)
    utils.prt(df.head())


class Energidataservice():
    @staticmethod
    def dayahead_prices_df(countries, start_date, end_date=datetime(2030, 12, 31)):
        import pandas as pd
        indata_list = Energidataservice.dayahead_prices(countries, start_date, end_date)
        df = pd.DataFrame(indata_list)
        df = df.pivot_table(index='HourUTC', columns='PriceArea', values='SpotPriceEUR')
        df = df.ffill()
        df.columns = [f'Spotprice {c}' for c in df.columns]
        return df

    @staticmethod
    def dayahead_prices(countries, start_date, end_date=datetime(2030, 12, 31)):
        in_list = Energidataservice._get_dayahead_prices(countries, start_date, end_date)
        return in_list

    @staticmethod
    def production_consumption(areas, start_date, end_date=datetime(2030, 12, 31)):
        in_list = Energidataservice._get_production_consumption(areas, start_date, end_date)
        return in_list

    @staticmethod
    def production_consumption_df(areas, start_date, end_date=datetime(2030, 12, 31)):
        import pandas as pd
        indata_list = Energidataservice.production_consumption(areas, start_date, end_date)
        df = pd.DataFrame(indata_list)
        if len(areas)>1:
            df = df.pivot_table(index='HourUTC',columns='PriceArea')
        else:
            df = df.pivot_table(index='HourUTC')
        df = df.ffill()
        return df

    @classmethod
    def _get_dayahead_prices(cls, countries, start_date, end_date):
        filters = f'{{"PriceArea":"{",".join(countries)}"}}'
        start_date_str = start_date.strftime("%Y-%m-%dT00:00")
        end_date_str = (end_date + timedelta(days=1)).strftime("%Y-%m-%dT00:00")
        base_url = f"https://api.energidataservice.dk/dataset/Elspotprices?offset=0"
        url = f"{base_url}&start={start_date_str}&end={end_date_str}&filter={filters}&sort=HourUTC ASC"
        indata_json = requests.get(url).json()['records']
        for d in indata_json:
            d.update((k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')) for k, v in d.items() if k in ['HourUTC', 'HourDK'])
        return indata_json

    @classmethod
    def _get_production_consumption(cls, countries, start_date, end_date):
        filters = f'{{"PriceArea":"{",".join(countries)}"}}'
        start_date_str = start_date.strftime("%Y-%m-%dT00:00")
        end_date_str = (end_date + timedelta(days=1)).strftime("%Y-%m-%dT00:00")
        base_url = f"https://api.energidataservice.dk/dataset/ProductionConsumptionSettlement?offset=0"
        url = f"{base_url}&start={start_date_str}&end={end_date_str}&filter={filters}&sort=HourUTC ASC"
        indata_json = requests.get(url).json()['records']
        for d in indata_json:
            d.update((k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')) for k, v in d.items() if k in ['HourUTC', 'HourDK'])
        return indata_json



if __name__ == '__main__':
    main()
