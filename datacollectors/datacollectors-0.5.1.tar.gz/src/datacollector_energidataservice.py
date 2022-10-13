from datetime import datetime, timedelta

import requests


def main():
    start_date = datetime(2022, 10, 1)
    end_date = datetime(2022, 10, 31)

    price_areas = ['DE', 'DK1', 'DK2', 'SE4', 'NO2', 'NO3', 'SE3']
    in_data = energidataservice.dayahead_prices_df(price_areas, start_date, end_date)
    print(in_data.head())


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

    @classmethod
    def _get_dayahead_prices(cls, countries, start_date, end_date):
        filters = f'{{"PriceArea":"{",".join(countries)}"}}'
        start_date_str = start_date.strftime("%Y-%m-%dT00:00")
        end_date_str = (end_date + timedelta(days=1)).strftime("%Y-%m-%dT00:00")
        print(start_date_str, end_date_str)
        url = f"https://api.energidataservice.dk/dataset/Elspotprices?offset=0&start={start_date_str}&end={end_date_str}&filter={filters}&sort=HourUTC ASC"
        indata_json = requests.get(url).json()['records']
        for d in indata_json:
            d.update((k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S')) for k, v in d.items() if k in ['HourUTC', 'HourDK'])
        return indata_json


if __name__ == '__main__':
    main()
