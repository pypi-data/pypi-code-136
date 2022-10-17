from dash.dependencies import Input, State
from dash_extensions.enrich import Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import html, ClientsideFunction
from dash_extensions.enrich import Trigger

from rats.core.RATS_CONFIG import packagepath, PlotBanks, topopath, dfpath
from rats.app import session_data

from bs4 import BeautifulSoup as bs
import pandas as pd
import shutil
import base64
import os

'''
Contents: 
1 - Dropdown population 
    - Generic placeholder generation, fired on server startup
2 - File upload 
    - No real purpose right now as upload handled by dash_uploader module 
3 - Data pre-processing 
    - preprocessdata()
        - Creates dataframes, list of files in session and performs comparison between dataframes
        - compares dataframes and checks for intra and inter file errors
4 - Figure management
    - clearprogramdata()
        - clears out files from rats/feathereddataframes
5 - Server shutdown 
    - shutdown()
        - clears the RATS files and sessionfilenames dataframe from the rats/cache directory

'''


# ============================================================
#           FILE UPLOAD
# ============================================================

def register_callbacks(app):
    outputs = [[Output(f'{j.designation}fileselect{i}', 'options') for i in range(j.number_of_plot_banks)] for j in
               PlotBanks]

    def flatten_outputs(complex_outputs):
        return [output for output_list in complex_outputs for output in output_list]

    outputs = flatten_outputs(outputs)

    @app.callback([Output('datalist', 'children')] + outputs,
                  [Trigger('rats_upload_button', 'n_clicks')])
    def preprocessdata():
        # function to add to the session file dataframe the status of each file and yield the gui output

        session_data.scan_for_files()
        session_data.parse_data_files()
        session_data.compare_data_files()
        session_data.save_session_data()

        children = dbc.Table.from_dataframe(session_data.data_files, striped=True, id='table')

        filenames = session_data.data_files['File'].tolist()
        options = []
        for i in range(len(filenames)):
            if filenames[i] != 0:  # only append filename of inteterest, with index, no empty data!
                item = {'label': f'{filenames[i]}', 'value': f'{filenames[i]}'}
                options.append(item)
        return [children] + [options for _ in range(len(outputs))]

    # ============================================================
    #           /FILE UPLOAD
    # ============================================================

    # ============================================================
    #           CLEAR PROGRAM DATA
    # ============================================================
    @app.callback(Output('clearstatus', 'children'),
                  [Input('cleardata', 'n_clicks')], prevent_initial_call=True)
    def clearprogramdata(n_clicks):
        if n_clicks is None:
            pass
        else:
            print('Ratdash has cleared all the program data!')

            # clear session data before shutdown
            for filename in os.listdir(str(packagepath / dfpath)):
                if filename != '__init__.py':
                    file_path = str(packagepath / dfpath / filename)
                else:
                    file_path = False
                if file_path:
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))

            return 'All previously processed data has been cleared'

    # ============================================================
    #           /CLEAR PROOGRAM DATA
    # ============================================================

    # ============================================================
    #           TOPO MANAGEMENT
    # ============================================================

    def populatetoporeport():
        """
        Finds loaded topo files and constructs a DF for display with dash_table of the files and the device to which they
        map.
        :return: dash_table
        """
        topodict = []
        for filename in os.listdir(str(packagepath / topopath)):
            # print(filename)
            if '.xml' in filename:
                topology = {}
                if filename == '__init__.py':
                    pass
                elif 'topology' in filename.lower():
                    topology['Filename'] = filename
                    topology['Device'] = 'Instrument Topo File'
                    topodict.append(topology)
                else:
                    with open(str(packagepath / topopath / filename), 'r') as f:
                        content = f.readlines()
                    content = "".join(content)
                    soup = bs(content, 'lxml')
                    device = soup.find('de:device')
                    topology['Filename'] = filename
                    topology['Device'] = f'EDS for {device["instancename"]}'
                    topodict.append(topology)
            topodf = pd.DataFrame(topodict)

            children = dbc.Table.from_dataframe(topodf, striped=True, id='topotable')
            # might be worth implementing similar thing to datamanagement app here.. couple of buttons and return to options of list

        return children

    def parse_topo(contents, filename):
        """
        Handle uploads from dcc.upload component - topo files are small enough for this to be effective.
        """
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string).decode('utf-8')
        try:
            if '.xml' in filename:
                with open(str(packagepath / topopath / filename), 'w') as f:
                    f.write(str(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

    @app.callback(Output('topodatacontainer', 'children'),
                  Input('upload-topo', 'contents'),
                  State('upload-topo', 'filename'))
    def update_toporeport(list_of_contents, list_of_names):
        """
        Upload EDS files and update the displayed output
        """
        if list_of_contents is None:
            pass
        elif list_of_contents is not None:
            [parse_topo(contents, name) for contents, name in zip(list_of_contents, list_of_names)]
        children = populatetoporeport()
        return children

    @app.callback([Output('clearedtopo', 'children'),
                   Output('topodatacontainer', 'children')],
                  [Input('cleartopo', 'n_clicks')])
    def cleartopodata(n_clicks):
        """
        clear all topo data
        """
        if n_clicks is None:
            raise PreventUpdate
        else:
            # clear session data before shutdown
            for filename in os.listdir(str(packagepath / topopath)):
                if filename != '__init__.py':
                    file_path = os.path.join(str(packagepath / topopath / filename))
                else:
                    file_path = False
                if file_path:
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                        print('topo data deleted')
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))

            return 'All topo data has been cleared', html.Div([], id='toporeport', className='col')

    app.clientside_callback(ClientsideFunction(namespace="clientside", function_name="make_draggable"),
                            [Output("refresh-page-btn", "data-drag")],
                            [Input("refresh-page-btn", "id")])
