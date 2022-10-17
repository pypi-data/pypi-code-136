from dash.dependencies import Output, State
from dash_extensions.enrich import Trigger
from rats.modules.jitter_analysis import jitter_plots
from rats.core.rats_parser import RatsParser
import plotly
import datetime


def register_callbacks(app=None, number_of_banks: int = 1, callback_designation:str = 'interscan_app_') -> None:
    for bank in range(number_of_banks):
        @app.callback([Output(f'{callback_designation}plot{bank}', 'figure'),
                       Output(f'{callback_designation}histo_plot{bank}', 'figure'),
                       Output(f'{callback_designation}interscan_plot{bank}', 'figure'),
                       Output(f'{callback_designation}fileselect-accordion{bank}','title')],
                      [Trigger(f'{callback_designation}replot{bank}', 'n_clicks')],
                      [State(f'{callback_designation}fileselect{bank}', 'value')],
                      prevent_initial_call=True)
        def handle_jitter_replots(file):
            parser = RatsParser(file)
            parser.load_dataframe()
            df = parser.dataframe.copy()
            del parser

            scatter_plot = jitter_plots.llc_cycle_times_scatter(df)
            histo_plot = jitter_plots.llc_cycle_times_histo(df)
            interscan_plot = jitter_plots.interscan_times(df)

            return scatter_plot, histo_plot, interscan_plot, file

        @app.callback(Output(f'{callback_designation}download{bank}', 'data'),
                      [Trigger(f'{callback_designation}download-btn{bank}', 'n_clicks')],
                      [State(f'{callback_designation}plot{bank}', 'figure'),
                       State(f'{callback_designation}fileselect{bank}', 'value')],
                      prevent_initial_call=True)
        def handle_scatter_download(fig, filename):
            date = datetime.datetime.now().strftime("%d%b%Y-%T")
            html = plotly.io.to_html(fig)
            return dict(content=html, filename=f"{date}-{filename}-{callback_designation}-scatter.html")

        @app.callback(Output(f'{callback_designation}download_histo{bank}', 'data'),
                      [Trigger(f'{callback_designation}download-histo-btn{bank}', 'n_clicks')],
                      [State(f'{callback_designation}histo_plot{bank}', 'figure'),
                       State(f'{callback_designation}fileselect{bank}', 'value')],
                      prevent_initial_call=True)
        def handle_histo_download(fig, filename):
            date = datetime.datetime.now().strftime("%d%b%Y-%T")
            html = plotly.io.to_html(fig)
            return dict(content=html, filename=f"{date}-{filename}-{callback_designation}-histogram.html")

        @app.callback(Output(f'{callback_designation}download_interscan{bank}', 'data'),
                      [Trigger(f'{callback_designation}download-interscan-btn{bank}', 'n_clicks')],
                      [State(f'{callback_designation}interscan_plot{bank}', 'figure'),
                       State(f'{callback_designation}fileselect{bank}', 'value')],
                      prevent_initial_call=True)
        def handle_interscan_download(fig, filename):
            date = datetime.datetime.now().strftime("%d%b%Y-%T")
            html = plotly.io.to_html(fig)
            return dict(content=html, filename=f"{date}-{filename}-{callback_designation}-interscan.html")
