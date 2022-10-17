from rats.core.rats_parser import RatsParser
import datetime
import plotly
from dash.dependencies import Output, State
from dash_extensions.enrich import Trigger

from rats.modules.scope import scope_plots

def register_callbacks(app, number_of_banks: int, callback_designation: str = 'scope_app_') -> None:
    for bank in range(number_of_banks):
        @app.callback([Output(f'{callback_designation}plot{bank}', 'figure'),
                       Output(f'{callback_designation}edbselect{bank}', 'options'),
                       Output(f'{callback_designation}edbselect{bank}','value'),
                       Output(f'{callback_designation}fileselect-accordion{bank}','title')],
                      [Trigger(f'{callback_designation}replot{bank}', 'n_clicks'),
                       Trigger(f'{callback_designation}centre_data', 'n_clicks')],
                      [State(f'{callback_designation}llc', 'value'),
                       State(f'{callback_designation}buffer', 'value'),
                       State(f'{callback_designation}fileselect{bank}', 'value'),
                       State(f'{callback_designation}edbselect{bank}', 'value')],
                      prevent_initial_call=True)
        def plotbank(llc, buffer, file, edbs=[]):
            parser = RatsParser(file)
            parser.load_dataframe()
            df = parser.dataframe.copy()
            del parser

            options_creator_df = df[['ACTIVE_EDBS', 'ACTIVE_EDBS_id']].drop_duplicates()
            optionsdict = options_creator_df.to_dict(orient='list')
            options = [{"label": f"EDB {x}: {y}", "value": x} for x,y in list(zip(optionsdict['ACTIVE_EDBS'], optionsdict['ACTIVE_EDBS_id']))]
            s = scope_plots.scopeplot(df, llc=llc, buffer=buffer, facet=True, timescale=1000, edbs=edbs)

            del df
            return s, options, edbs, file

        @app.callback(Output(f'{callback_designation}download{bank}', 'data'),
                      [Trigger(f'{callback_designation}download-btn{bank}', 'n_clicks')],
                      [State(f'{callback_designation}plot{bank}', 'figure'),
                       State(f'{callback_designation}fileselect{bank}', 'value')], prevent_initial_call=True)
        def handle_scope_download(fig, filename):
            date = datetime.datetime.now().strftime("%d%b%Y-%T")
            html = plotly.io.to_html(fig)
            return dict(content=html, filename=f"{date}-{filename}-{callback_designation}.html")
