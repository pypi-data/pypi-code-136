from dash.dependencies import Input, State
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import Trigger, Output
from rats.modules.error_detection import error_detection_plot
from rats.modules.scope import scope_plots
from rats.core.rats_parser import RatsParser
import plotly
import datetime

def register_callbacks(app=None, number_of_banks: int = 1, callback_designation:str = 'dashboard_app_') -> None:
    for bank in range(number_of_banks):
        @app.callback([Output(f'{callback_designation}error_detection_plot{bank}', 'figure'),
                       Output(f'{callback_designation}scopeplot{bank}', 'figure'),
                       Output(f'{callback_designation}replot{bank}', 'n_clicks'),
                       Output(f'{callback_designation}fileselect-accordion{bank}','title'),
                       Output(f'{callback_designation}error_detection_plot{bank}', 'clickData')],
                      [Input(f'{callback_designation}error_detection_plot{bank}', 'clickData'),
                       Input(f'{callback_designation}numberofscans{bank}', 'value')],
                      [Trigger(f'{callback_designation}replot{bank}', 'n_clicks')],
                      [State(f'{callback_designation}fileselect{bank}', 'value'),
                       State(f'{callback_designation}resolution{bank}', 'value'),
                       State(f'{callback_designation}low_llc_bound{bank}', 'value'),
                       State(f'{callback_designation}high_llc_bound{bank}', 'value'),
                       State(f'{callback_designation}error_detection_plot{bank}', 'figure')],
                      prevent_initial_call=True)
        def handle_dashboard_plots(error_detection_click_data, scans, file, resolution, low_llc, high_llc,bpplot):
            # will add another few controls to the app... advanced plot options?
            parser = RatsParser(file)
            parser.load_dataframe()
            df = parser.dataframe.copy()
            del parser # do not need to hold this object in memory anymore

            # surely we can do something here to stop the plot reloading every time??

            # ========================================================
            # PLOT LINKAGES
            # ========================================================
            if error_detection_click_data is not None:
                start = int(error_detection_click_data['points'][0]['x'])
                s = scope_plots.scopeplot(df, llc=start, buffer=scans, facet=False, resample=False)
                bp = bpplot
                error_detection_click_data = None
            else:
                s = scope_plots.scopeplot(df, buffer=scans, facet=False, resample=False)

                decimate = False if resolution == 'high' else True

                if resolution == 'high':
                    bpdf = df[(df['LLC_COUNT'] > low_llc) & (df['LLC_COUNT'] < high_llc)]
                else:
                    bpdf = df

                bp = error_detection_plot.error_detection_plot(bpdf, decimate=decimate)

                del bpdf

            del df # clean up memory

            return bp, s, None, file, error_detection_click_data

        @app.callback(Output(f'{callback_designation}download_error_detection_plot{bank}', 'data'),
                      [Trigger(f'{callback_designation}download-error_detection-btn{bank}', 'n_clicks')],
                      [State(f'{callback_designation}error_detection_plot{bank}', 'figure'),
                       State(f'{callback_designation}fileselect{bank}', 'value')],
                      prevent_initial_call=True)
        def handle_error_detection_download(fig, filename):
            date = datetime.datetime.now().strftime("%d%b%Y-%T")
            html = plotly.io.to_html(fig)
            return dict(content=html, filename=f"{date}-{filename}-{callback_designation}bp.html")

        @app.callback(Output(f'{callback_designation}download_scope{bank}', 'data'),
                      [Trigger(f'{callback_designation}download-scope-btn{bank}', 'n_clicks')],
                      [State(f'{callback_designation}scopeplot{bank}', 'figure'),
                       State(f'{callback_designation}fileselect{bank}', 'value')],
                      prevent_initial_call=True)
        def handle_dashboard_download(fig, filename):
            date = datetime.datetime.now().strftime("%d%b%Y-%T")
            html = plotly.io.to_html(fig)
            return dict(content=html, filename=f"{date}-{filename}-{callback_designation}scope.html")
