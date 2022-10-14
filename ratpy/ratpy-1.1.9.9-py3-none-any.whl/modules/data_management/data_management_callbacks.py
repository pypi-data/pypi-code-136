from dash.dependencies import State, Input
from dash import html
from dash_extensions.enrich import Output, Trigger
from rats.app import session_data, rats_data
from rats.core.RATS_CONFIG import PlotBanks
from rats.core.rats_parser import RatsParser


def register_callbacks(app=None, callback_designation: str = 'data_management_app_') -> None:
    outputs = [[Output(f'{j.designation}fileselect{i}', 'options') for i in range(j.number_of_plot_banks)] for j in
               PlotBanks if j.designation != callback_designation]

    def flatten_outputs(complex_outputs):
        return [output for output_list in complex_outputs for output in output_list]

    outputs = flatten_outputs(outputs)

    @app.callback([Output(f'{callback_designation}data', 'options'),
                   Output(f'{callback_designation}report', 'children'),
                   Output(f'{callback_designation}log-fileselect','options')],
                  [Trigger(f'{callback_designation}pulldata', 'n_clicks')])
    def pull_data():
        options = []
        log_options = []
        rats_data.scan_for_files()
        file_list = rats_data.data_files['file'].tolist()
        sizes = rats_data.data_files['file_size'].tolist()
        total_size = rats_data.data_files['file_size'].sum()
        for file, size in zip(file_list, sizes):
            options.append(dict(label=f'{file.split(".")[0]}: {size:.2f}Mb', value=file))

        for i in range(len(file_list)):
            if file_list[i] != 0:  # only append filename of inteterest, with index, no empty data!
                item = {'label': f'{file_list[i]}', 'value': f'{file_list[i]}'}
                log_options.append(item)

        return [options] + [f'Total data use: {total_size:.2f}Mb'] + [log_options]

    @app.callback([Output(f'{callback_designation}parser_log','children'),
                   Output(f'{callback_designation}fileselect-accordion', 'title')],
                  [Input(f'{callback_designation}log-fileselect','value')], prevent_initial_call=True)
    def display_log(file):
        parser = RatsParser(file)
        parser.load_dataframe()
        print()
        output = []
        for line in parser.metadata['log'].split('\n'):
            output.append(html.P(line))
            output.append(html.Br())

        return output, file

    @app.callback([Output('refresh-overlay', 'style')] + outputs,
                  [Trigger(f'{callback_designation}delete', 'n_clicks')],
                  [State(f'{callback_designation}data', 'value')],
                  prevent_initial_call=True)
    def delete_selected_data(values):
        session_file_filter_values = [file.replace('.feather', '') for file in values]

        session_data.data_files = session_data.data_files[~session_data.data_files['File'].
            isin(session_file_filter_values)]

        filenames = session_data.data_files['File'].tolist()

        options = []

        for i in range(len(filenames)):
            item = {'label': f'{filenames[i]}', 'value': f'{filenames[i]}'}
            options.append(item)

        rats_data.delete_data(values)

        return [{'display': 'flex'}] + \
               [options for _ in outputs]

    @app.callback([Output('refresh-overlay', 'style')] + outputs,
                  [Trigger(f'{callback_designation}cleardata', 'n_clicks')],
                  prevent_initial_call=True)
    def clear_program_data():
        print('Ratdash has cleared all the program data!')

        rats_data.scan_for_files()
        stored_files = rats_data.data_files['file'].tolist()
        stored_files_filter = [file[:-8] for file in stored_files]
        try:
            session_data.data_files = session_data.data_files[
                ~session_data.data_files['file'].isin(stored_files_filter)]
        except:
            pass
        rats_data.delete_data(all_files=True)
        options = []

        return [{'display': 'flex'}] + \
               [options for _ in outputs]

    @app.callback([Output('refresh-overlay', 'style')] + outputs,
                  [Trigger(f'{callback_designation}loaddata', 'n_clicks')],
                  [State(f'{callback_designation}data', 'value')],
                  prevent_initial_call=True)
    def load_stored_data(values):

        files_to_load = [file.replace('.feather', '') for file in values]

        session_data.scan_for_files(file_list=files_to_load)
        session_data.parse_data_files()
        session_data.compare_data_files()
        session_data.save_session_data()

        filenames = session_data.data_files['File'].tolist()

        options = []

        for i in range(len(filenames)):
            item = {'label': f'{filenames[i]}', 'value': f'{filenames[i]}'}
            options.append(item)

        return [{'display': 'flex'}] + \
               [options for _ in outputs]
