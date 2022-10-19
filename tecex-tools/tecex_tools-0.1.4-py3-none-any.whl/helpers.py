import pandas as pd
import datetime
from tecex_tools.models import BTAImport


class RawBTAImport:
    """Class assisting process of RAW BTA data"""

    cna_business_sector = 'Business Sector'
    cna_gl_account = 'GL Account: GL Account Name'
    cna_amount = 'Amount'
    cna_date = 'Date'

    raw_columns = [
        cna_amount,
        cna_gl_account,
        cna_business_sector,
        cna_date
    ]

    def __init__(self, data: pd.DataFrame, report_date: datetime.datetime):
        self.data = data
        self.record_description = f"{report_date.strftime('%b')} {report_date.year} BTA's"

    def aggregate(self):
        return self.data[self.raw_columns].groupby(
            by=[
                self.cna_business_sector,
                self.cna_date,
                self.cna_gl_account
            ]
        ).agg(
            {self.cna_amount: 'sum'}
        ).reset_index()

    @staticmethod
    def create_column_site(gl_code: str, bus_sec: str) -> str:
        if str(gl_code) == '624256':
            return 'US00E'

        elif bus_sec == 'ECOMMERCE':
            return 'MU00L'

        else:
            return 'MU00E'

    @staticmethod
    def create_column_bpr(gl_code: int, bus_sec: str, site: str) -> str:

        # Determine last 4
        last_4 = ''

        if gl_code == 610000:
            last_4 = 'CUST'

        if gl_code == 920000:
            last_4 = 'SUPP'

        if last_4 != '':

            # Determine pre-3
            pre_4__3 = None
            if bus_sec == 'MEDICAL':
                pre_4__3 = 'MDX'

            elif bus_sec == 'TECH':
                pre_4__3 = 'TCX'

            elif bus_sec == 'ECOMMERCE':
                pre_4__3 = 'ZEE'

            return f"{site}-{pre_4__3}{last_4}"

        else:
            return ''

    def create_report_records(self):
        df = self.aggregate()

        df['Company'] = df['GL Account: GL Account Name'].map({
            '624256': 'USVAT'
        }).fillna('MUGRP')

        df['Site'] = df.apply(
            lambda x: self.create_column_site(
                gl_code=str(x[self.cna_gl_account]),
                bus_sec=str(x[self.cna_business_sector])
            ), axis=1
        )

        df['Amount'] = df[self.cna_amount].round(2)

        df['Journal Description'] = self.record_description
        df['Line description'] = df['Journal Description'] + '/' + df[self.cna_business_sector]
        df['BPR'] = df.apply(
            lambda x: self.create_column_bpr(
                gl_code=x[self.cna_gl_account],
                bus_sec=x[self.cna_business_sector],
                site=x['Site']
            ), axis=1
        )

        df['Accounting Date'] = df[self.cna_date].dt.strftime('%Y%m%d')

        records = []
        for index, row in df.iterrows():
            records.append(
                BTAImport(
                    _1=1,
                    _2=1,
                    _3=1,
                    _4=1,
                    company=row['Company'],
                    account=row[self.cna_gl_account],
                    line_description=self.record_description,
                    division='SHARED' if row[self.cna_gl_account] in [314500, 611500] else '',
                    branch='SHARED' if row[self.cna_gl_account] in [314500, 611500] else '',
                    product='',
                    other='SHARED' if row[self.cna_gl_account] in [314500, 611500] else '',
                    function='',
                    employee='',
                    n___a_1='',
                    n___a_2='',
                    amount=row[self.cna_amount],
                    accounting_date=row[self.cna_date],
                    ratedate=row[self.cna_date],
                    site=row['Site'],
                    journal_description=row['Line description'],
                    bpr=row['BPR'],
                    control_account='',
                    currency='USD',
                    tax='VATT40' if row[self.cna_gl_account] in [611500, 314500] else ''
                )
            )

        return records


class RawBTImport:
    """Class assisting process of RAW BT data"""
    # cna_business_sector = 'Business Sector'
    cna_gl_account = 'GL Account'
    cna_amount = 'Amount'
    cna_date = 'Date'

    raw_columns = [
        cna_amount,
        cna_gl_account,
        cna_date
    ]

    def __init__(self, data: pd.DataFrame, report_date: datetime.datetime):
        self.data = data
        self.record_description = f"{report_date.strftime('%B')} {report_date.year} BT's"

    def aggregate(self):
        return self.data[self.raw_columns].groupby(
            by=[
                self.cna_date,
                self.cna_gl_account
            ]
        ).agg(
            {self.cna_amount: 'sum'}
        ).reset_index()

    @staticmethod
    def create_column_bpr(gl_code: int, bus_sec: str, site: str) -> str:

        # Determine last 4
        last_4 = ''

        if gl_code == 610000:
            last_4 = 'CUST'

        if gl_code == 920000:
            last_4 = 'SUPP'

        if last_4 != '':

            # Determine pre-3
            pre_4__3 = None
            if bus_sec == 'MEDICAL':
                pre_4__3 = 'MDX'

            elif bus_sec == 'TECH':
                pre_4__3 = 'TCX'

            elif bus_sec == 'ECOMMERCE':
                pre_4__3 = 'ZEE'

            return f"{site}-{pre_4__3}{last_4}"

        else:
            return ''

    def create_report_records(self):
        df = self.aggregate()
        df['Company'] = df[self.cna_gl_account].map({'624256': 'USVAT'}).fillna('MUGRP')
        df['Site'] = df[self.cna_gl_account].map({'624256': 'US00E'}).fillna('MU00E')
        df['Journal Description'] = self.record_description
        df['Accounting Date'] = df[self.cna_date].dt.strftime('%Y%m%d')
        df['Amount'] = df[self.cna_amount].round(2)

        records = []
        for index, row in df.iterrows():
            records.append(
                BTAImport(
                    _1=1,
                    _2=1,
                    _3=1,
                    _4=1,
                    company=row['Company'],
                    account=row[self.cna_gl_account],
                    line_description=self.record_description,
                    division='SHARED' if row[self.cna_gl_account] in [314500, 611500] else '',
                    branch='SHARED' if row[self.cna_gl_account] in [314500, 611500] else '',
                    product='',
                    other='SHARED' if row[self.cna_gl_account] in [314500, 611500] else '',
                    function='',
                    employee='',
                    n___a_1='',
                    n___a_2='',
                    amount=row[self.cna_amount],
                    accounting_date=row[self.cna_date],
                    ratedate=row[self.cna_date],
                    site=row['Site'],
                    journal_description=self.record_description,
                    bpr='',
                    control_account='',
                    currency='USD',
                    tax='VATT40' if row[self.cna_gl_account] in [611500, 314500] else ''
                )
            )

        return records
