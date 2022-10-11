import json
from datetime import datetime, timedelta
import requests
import incentivedkutils as utils
from concurrent.futures import ThreadPoolExecutor
import xmltodict
from dateutil import parser


@utils.timer()
def main():
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2022, 1, 31)
    countries = ['DE', 'DK1']
    entsoe_token = '95019cf4-6474-4df8-86b3-225459b315ca'
    ents = Entsoe(entsoe_token,chunksize=30,max_workers=12)
    indata = ents._get_dayahead_prices(countries, start_date, end_date)
    utils.prt(indata[-10:])


class Entsoe():
    def __init__(self, token, chunksize=30,max_workers=12):
        self._token = token
        self._chunksize = chunksize
        self._max_workers = max_workers

    def dayahead_prices_df(self, countries, start_date, end_date):
        import pandas as pd
        indata_list = Entsoe.dayahead_prices(self, countries, start_date, end_date)
        df = pd.DataFrame(indata_list)
        df = df.pivot_table(index='ts', columns='country', values='price')
        df = df.ffill()
        df.columns = [f'Spotprice {c}' for c in df.columns]
        return df

    def dayahead_prices(self, countries, start_date, end_date=datetime(2030, 12, 31)):
        in_list = self._get_dayahead_prices(countries, start_date, end_date)
        return in_list

    def _get_dayahead_prices(self, countries, start_date, end_date):
        parms_list = Entsoe._read_parms()
        document_type = 'A44'
        base_url = f'https://transparency.entsoe.eu/api?securityToken={self._token}&'
        chunk_size = self._chunksize
        start_date = start_date - timedelta(days=1)
        if end_date > datetime.today() + timedelta(days=2):
            end_date = datetime.today() + timedelta(days=2)
        tasks = []
        for country in countries:
            zones = [obs['Code'] for obs in parms_list if obs['Country'] == country]
            for zone in zones:
                for datestep in range((end_date - start_date).days // chunk_size + 1):
                    date_start = start_date + timedelta(days=chunk_size * datestep)
                    date_end = min(date_start + timedelta(days=chunk_size), end_date)
                    doc_url = f'documentType={document_type}&in_Domain={zone}&out_Domain={zone}' \
                              f'&periodStart={date_start.strftime("%Y%m%d2300")}&periodEnd={date_end.strftime("%Y%m%d2300")}'
                    url = f'{base_url}{doc_url}'
                    tasks.append((url, country))
        with ThreadPoolExecutor(max_workers=self._max_workers) as executor:
            indata_list = list(executor.map(Entsoe._get_xml, tasks))
        indata_dict = [Entsoe._read_xml(indata[0], indata[1]) for indata in indata_list]
        indata_dict = utils.flatten_list(indata_dict)
        return indata_dict

    @classmethod
    def _get_xml(cls, task):
        indata_xml = requests.get(task[0]).text
        return indata_xml, task[1]

    @classmethod
    def _read_xml(cls, indata_xml, country):
        indata_json = json.dumps(xmltodict.parse(indata_xml))
        indata_dict = json.loads(indata_json)
        out_list = []
        if 'Publication_MarketDocument' in indata_dict.keys():
            timeseries = indata_dict['Publication_MarketDocument']['TimeSeries']
            if type(timeseries) != list:
                timeseries = [timeseries]
            for obs in timeseries:
                ts_start = parser.parse(obs['Period']['timeInterval']['start'])
                time_resolution = int(obs['Period']['resolution'][-3:-1])
                data_points = obs['Period']['Point']
                if type(data_points) != list:
                    data_points = [data_points]
                for data_point in data_points:
                    obs_dict = {}
                    obs_dict['country'] = country
                    obs_dict['ts'] = ts_start + timedelta(minutes=(int(data_point['position']) - 1) * time_resolution)
                    obs_dict['price'] = float(data_point['price.amount'])
                    out_list.append(obs_dict)
        return out_list

    @classmethod
    def _read_parms(cls):
        parms_list = [
            {"Code": "10YAT-APG------L", "Meaning": "Austria, APG CA / MBA", "Country": "AT",
             "Country_long": "Austria"},
            {"Code": "10YBE----------2", "Meaning": "Belgium, Elia BZ / CA / MBA", "Country": "BE",
             "Country_long": "Belgium"},
            {"Code": "10YCH-SWISSGRIDZ", "Meaning": "Switzerland, Swissgrid BZ / CA / MBA", "Country": "CH",
             "Country_long": "Switzerland"},
            {"Code": "10Y1001A1001A82H", "Meaning": "DE-LU MBA", "Country": "DE", "Country_long": "Germany"},
            {"Code": "10Y1001A1001A63L", "Meaning": "DE-AT-LU BZ", "Country": "DE", "Country_long": "Germany"},
            {"Code": "10YDK-1--------W", "Meaning": "DK1 BZ / MBA", "Country": "DK1", "Country_long": "Denmark West"},
            {"Code": "10YDK-2--------M", "Meaning": "DK2 BZ / MBA", "Country": "DK2", "Country_long": "Denmark East"},
            {"Code": "10YES-REE------0", "Meaning": "Spain, REE BZ / CA / MBA", "Country": "ES",
             "Country_long": "Spain"},
            {"Code": "10YFI-1--------U", "Meaning": "Finland, Fingrid BZ / CA / MBA", "Country": "FI",
             "Country_long": "Finland"},
            {"Code": "10YFR-RTE------C", "Meaning": "France, RTE BZ / CA / MBA", "Country": "FR",
             "Country_long": "France"},
            {"Code": "10YGR-HTSO-----Y", "Meaning": "Greece, IPTO BZ / CA/ MBA", "Country": "GR",
             "Country_long": "Greece"},
            {"Code": "10YHU-MAVIR----U", "Meaning": "Hungary, MAVIR CA / BZ / MBA", "Country": "HU",
             "Country_long": "Hungary"},
            {"Code": "10Y1001A1001A59C", "Meaning": "Ireland, EirGrid CA", "Country": "IE", "Country_long": "Ireland"},
            {"Code": "10Y1001A1001A70O", "Meaning": "Italy, IT CA / MBA", "Country": "IT_N",
             "Country_long": "Italy North"},
            {"Code": "10Y1001A1001A71M", "Meaning": "Italy, IT CA / MBA", "Country": "IT_S",
             "Country_long": "Italy South"},
            {"Code": "10YLT-1001A0008Q", "Meaning": "Lithuania, Litgrid BZ / CA / MBA", "Country": "LT",
             "Country_long": "Lithuania"},
            {"Code": "10YLV-1001A00074", "Meaning": "Latvia, AST BZ / CA / MBA", "Country": "LV",
             "Country_long": "Latvia"},
            {"Code": "10YNL----------L", "Meaning": "Netherlands, TenneT NL BZ / CA/ MBA", "Country": "NL",
             "Country_long": "Netherlands"},
            {"Code": "10YNO-1--------2", "Meaning": "NO1 BZ / MBA", "Country": "NO1", "Country_long": "Norway 1"},
            {"Code": "10YNO-2--------T", "Meaning": "NO2 BZ / MBA", "Country": "NO2", "Country_long": "Norway 2"},
            {"Code": "10YNO-3--------J", "Meaning": "NO3 BZ / MBA", "Country": "NO3", "Country_long": "Norway 3"},
            {"Code": "10YNO-4--------9", "Meaning": "NO4 BZ / MBA", "Country": "NO4", "Country_long": "Norway 4"},
            {"Code": "10Y1001A1001A48H", "Meaning": "NO5 BZ / MBA", "Country": "NO5", "Country_long": "Norway 5"},
            {"Code": "10YPL-AREA-----S", "Meaning": "Poland, PSE SA BZ / BZA / CA / MBA", "Country": "PL",
             "Country_long": "Poland"},
            {"Code": "10YPT-REN------W", "Meaning": "Portugal, REN BZ / CA / MBA", "Country": "PT",
             "Country_long": "Portugal"},
            {"Code": "10Y1001A1001A44P", "Meaning": "SE1 BZ / MBA", "Country": "SE1", "Country_long": "Sweden 1"},
            {"Code": "10Y1001A1001A45N", "Meaning": "SE2 BZ / MBA", "Country": "SE2", "Country_long": "Sweden 2"},
            {"Code": "10Y1001A1001A46L", "Meaning": "SE3 BZ / MBA", "Country": "SE3", "Country_long": "Sweden 3"},
            {"Code": "10Y1001A1001A47J", "Meaning": "SE4 BZ / MBA", "Country": "SE4", "Country_long": "Sweden 4"},
            {"Code": "10YGB----------A", "Meaning": "National Grid BZ / CA/ MBA", "Country": "UK", "Country_long": "UK"}
        ]
        # with open(Path(__file__).parent / 'entsoe_A44_codes.py', 'r') as file:
        #     parms_list = json.load(file)
        return parms_list

    @classmethod
    def _dfg(cls):
        pass


if __name__ == '__main__':
    main()
