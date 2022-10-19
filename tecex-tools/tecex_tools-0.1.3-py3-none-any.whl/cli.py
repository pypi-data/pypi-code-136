import typer
import pandas as pd
import datetime
import os

from tecex_tools.models import BTAImport

app = typer.Typer()


@app.command()
def test():
    typer.echo('test worked!')


@app.command()
def bta_import(file_path: str, year: int, month: int):
    """A function to generate the BTA Import File"""

    if os.path.isfile(file_path):
        typer.echo(f"File exists!")
        df = pd.read_excel(file_path, sheet_name='BTA Raw data')

        cna_business_sector = 'Business Sector'
        cna_gl_account = 'GL Account: GL Account Name'
        cna_amount = 'Amount'
        cna_date = 'Date'

        columns = [
            cna_amount,
            cna_gl_account,
            cna_business_sector,
            cna_date
        ]

        def create_column_site(gl_code: str, bus_sec: str) -> str:
            if str(gl_code) == '624256':
                return 'US00E'

            elif bus_sec == 'ECOMMERCE':
                return 'MU00L'

            else:
                return 'MU00E'

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

        df_step_001 = df[columns].groupby(
            by=[cna_business_sector, 'Date', cna_gl_account]).agg(
            {cna_amount: 'sum'}
        ).reset_index()

        typer.echo(f"Step 1 complete!")

        date_ = datetime.datetime(year, month, 1)
        journal_description = f"{date_.strftime('%b')} {year} BTA's"

        df_step_001['Company'] = df_step_001['GL Account: GL Account Name'].map({
            '624256': 'USVAT'
        }).fillna('MUGRP')

        df_step_001['Site'] = df_step_001.apply(
            lambda x: create_column_site(
                gl_code=str(x[cna_gl_account]),
                bus_sec=str(x[cna_business_sector])
            ), axis=1
        )

        df_step_001['Amount'] = df_step_001[cna_amount].round(2)

        df_step_001['Journal Description'] = journal_description
        df_step_001['Line description'] = df_step_001['Journal Description'] + '/' + df_step_001[cna_business_sector]
        df_step_001['BPR'] = df_step_001.apply(
            lambda x: create_column_bpr(
                gl_code=x[cna_gl_account],
                bus_sec=x[cna_business_sector],
                site=x['Site']
            ), axis=1
        )

        df_step_001['Accounting Date'] = df_step_001[cna_date].dt.strftime('%Y%m%d')

        records = []
        date_ = datetime.datetime(year, month, 1)
        record_description = f"{date_.strftime('%b')} {year} BTA's"

        for index, row in df_step_001.iterrows():
            records.append(
                BTAImport(
                    _1=1,
                    _2=1,
                    _3=1,
                    _4=1,
                    company=row['Company'],
                    account=row[cna_gl_account],
                    line_description=record_description,
                    division='SHARED' if row[cna_gl_account] in [314500, 611500] else '',
                    branch='SHARED' if row[cna_gl_account] in [314500, 611500] else '',
                    product='',
                    other='SHARED' if row[cna_gl_account] in [314500, 611500] else '',
                    function='',
                    employee='',
                    n___a_1='',
                    n___a_2='',
                    amount=row[cna_amount],
                    accounting_date=row[cna_date],
                    ratedate=row[cna_date],
                    site=row['Site'],
                    journal_description=row['Line description'],
                    bpr=row['BPR'],
                    control_account='',
                    currency='USD',
                    tax='VATT40' if row[cna_gl_account] in [611500, 314500] else ''
                )
            )

        export_path = os.path.dirname(file_path)

        pd.DataFrame(records).to_excel(
            os.path.join(
                export_path,
                f'{year}_{str(month).zfill(2)}bta_import_file.xlsx'
            ), index=False
        )

    else:
        typer.echo(f"File path provided does not exist\n File path provided: '{file_path}'")


