from dash import Dash, dcc, html, Input, Output, State, ALL
from .components import *

import os

class Plot:
    # Settings
    chart_bg = '#1f2c56'

    # State
    graph_df = pd.DataFrame()
    sort_method_current = ''
    filter_list = []
    add_button_count = 0
    chart1_button_clicks = 0
    chart2_button_clicks = 0
    save_clicks = 0
    line_selected = -1
    button_list = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    chart_type = 1
    relayoutData = []
    init = True
    save_path = ''
    initial_capital = 0
    return_in_capital = 0
    mdd = 0
    sharp = 0


    def __new__(self, filename, output_folder, start_date, end_date, para_dict, result_df, generate_filepath, settings):

        chart_bg = self.chart_bg

        components = Components()

        empty_line_chart = components.empty_line_chart()
        checkbox_div = components.update_checkbox_div(para_dict, result_df)
        col_df = result_df.columns.values.tolist()
        df_col = pd.DataFrame([['-----' for column in col_df]], columns=col_df)
        performance_matrix = components.update_performance_matrix(start_date, end_date, df_col.iloc[0].copy(), para_dict)
        filter_div = components.update_filter_div([])


        sort_method_dropdown  = components.sort_method_dropdown
        filter_dropdown = components.filter_dropdown
        filter_dropdown_disabled = components.filter_dropdown_disabled
        filter_input = components.filter_input
        filter_input_disabled = components.filter_input_disabled
        add_button_style = components.add_button_style
        add_button_style_disabled = components.add_button_style_disabled



        app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO], suppress_callback_exceptions=True)

        app.layout = html.Div([
            html.Div(style={'height': '10px', }),
            html.Div(
                dbc.Row([
                    # Left Column
                    dbc.Col(html.Div([
                        html.Div(style={'height': '15px', }),
                        html.Div('Sorting Method', style={'color': 'Cyan', 'margin-left': '15px', 'font-size': '15px'}),
                        html.Div(style={'height': '10px', }),
                        sort_method_dropdown,
                        html.Div(style={'height': '15px', }),
                        html.Div('Parameters', style={'color': 'Cyan', 'margin-left': '15px', 'font-size': '15px'}),
                        html.Div(id='checklist-container',children=checkbox_div),
                        html.Div(style={'height': '10px', }),
                        html.Div('Filters for', style={'color': 'Cyan', 'margin-left': '15px', 'font-size': '15px'}),
                        html.Div(style={'height': '10px', }),
                        html.Div(id='filter', children=filter_div,style={'padding': '0px 20px',
                                                                         'padding-right': '10px',
                                                                         'font-size': '12px'}),
                        dbc.Row([
                            dbc.Col(id='filter_dropdown_div',children=filter_dropdown,width=8),
                            dbc.Col(id='filter_input_div',children=filter_input,width=3),
                        ]),
                        html.Div(style={'height': '10px', }),
                        html.Div(id='add_button',children=html.Div([html.Div(style={'height': '5px'}),'Add Filter']),
                                 style=add_button_style),

                    ],style={'padding':'0px','border-radius':'5px','height': '704px',
                             'background-color':'rgba(0, 0, 0, 0)'})
                        ,style={'padding':'0','padding-left':'5px'}, width=2),

                    # Middle Column
                    dbc.Col(html.Div([

                        html.Div(id='performance_matrix', children=performance_matrix ),

                    ], style={'padding': '5px',})
                        , style={'padding': '0', }, width=2),


                    # Right Column
                    dbc.Col(html.Div([
                        html.Div(style={'height': '5px', }),
                        html.Div([html.Div(html.Img(),style={'height':'10px'}),

                                  dbc.Row([
                                      dbc.Col(html.Div(id='chart1_button', children='',
                                                       style={'text-align': 'left', 'cursor': 'pointer',
                                                              'font-size': '14px'}), width=4),
                                      dbc.Col(html.Div(html.Img()), width=4),
                                      dbc.Col(html.Div(id='chart2_button', children=''), width=4),
                                  ], style={'margin': '0px 5px'}),
                                  html.Div(id='chart_area',
                                           children=dcc.Graph(id='line_chart', figure=empty_line_chart)),
                                  html.Div(style={'height': '10px', }),

                                 ],style={'padding':'5px','border-radius':'5px','background-color':chart_bg}),
                        html.Div(style={'height': '5px', }),
                        html.Div(id='hist_area', children=html.Div(),
                                 style={'display': 'none'}),
                    ]), style={'padding':'0'}, width=8),
                ])
            ),

        ], style={'width':'1500px','margin':'auto','padding':'0px 10px','color':'white'})


        @app.callback(
            Output('line_chart', 'figure'),
            Output('filter', 'children'),
            Output('filter_dropdown_div', 'children'),
            Output('filter_input_div', 'children'),
            Output('add_button', 'style'),
            Output('filter_input', 'value'),
            Output('chart1_button', 'children'),
            Output('chart2_button', 'children'),
            Output('hist_area', 'children'),
            Output('hist_area', 'style'),
            Input('sort_method', 'value'),
            Input({'type': 'para-checklist', 'index': ALL}, 'value'),
            State('filter_dropdown_div', 'children'),
            State('filter_input_div', 'children'),
            State('line_chart', 'figure'),
            State('filter', 'children'),
            Input('add_button', 'n_clicks'),
            Input('chart1_button', 'n_clicks'),
            Input('chart2_button', 'n_clicks'),
            State('add_button', 'style'),
            State('filter_name', 'value'),
            State('filter_input', 'value'),
            State('hist_area', 'children'),
            State('hist_area', 'style'),
            [Input('button_' + str(i), 'n_clicks') for i in range(10)],
        )
        def display_output(sort_method,para_checklist,filter_dropdown_div,filter_input_div,fig_line,\
                           filter_div,add_button_clicks, \
                           chart1_button_clicks,chart2_button_clicks,\
                           _add_button_style,filter_name,filter_input_value,\
                           hist_area,hist_style, *vals):

            chart1_button_text = ''
            chart2_button_text = ''

            chart1_button_click = False


            if chart1_button_clicks:
                if chart1_button_clicks > self.chart1_button_clicks:
                    chart1_button_click = True
                    self.chart1_button_clicks = chart1_button_clicks
                    self. chart_type = 1
                    hist_style = {'display': 'none'}

            if chart2_button_clicks:
                if chart2_button_clicks > self.chart2_button_clicks:
                    self.chart2_button_clicks = chart2_button_clicks
                    if self.chart_type == 2:
                        chart1_button_text = '< Back'
                        return fig_line, filter_div, filter_dropdown_div, filter_input_div, _add_button_style, \
                               None, chart1_button_text, chart2_button_text, hist_area, hist_style
                    else:
                        if self.line_selected > -1:
                            para_key_list = list(para_dict)
                            para_values = []
                            for key in para_key_list:
                                para_values.append(self.graph_df.iloc[self.line_selected][key])
                            # save_path = generate_filepath(filename, output_folder, start_date, end_date, para_dict,
                            #                               para_values)
                            line_colour = self.graph_df.iloc[self.line_selected].line_colour
                            save_path = self.save_path
                            df = pd.read_csv(save_path)
                            df_chart = components.prepare_df_chart(df)

                            self.chart_type = 2
                            chart1_button_text = '< Back'

                            fig_line = components.generate_chart_2(df_chart, line_colour,
                                                                   para_dict,para_values, settings)


                            # Histograms
                            period = settings['histogram_period']
                            # First column of the 5 charts
                            title_list = [dbc.Col(width=1)]
                            pct_list = [dbc.Col(html.Div('pct_change', style={'font-size': '12px', 'margin-top': '55px',
                                                                              'margin-left': '45px',
                                                                              'transform': 'rotate(-90deg)'}), width=1)]
                            rise_list = [dbc.Col(html.Div('max_rise', style={'font-size': '12px', 'margin-top': '55px',
                                                                              'margin-left': '45px',
                                                                              'transform': 'rotate(-90deg)'}), width=1)]
                            fall_list = [dbc.Col(html.Div('max_fall', style={'font-size': '12px', 'margin-top': '55px',
                                                                              'margin-left': '45px',
                                                                              'transform': 'rotate(-90deg)'}), width=1)]


                            for p in period:
                                title_list.append(dbc.Col(f'{p} Days',style={'font-size': '12px', 'text-align': 'center'},width=2))
                                fig_pct, fig_rise, fig_fall = components.generate_histogram(df, p, 'backtest')
                                pct_list.append( dbc.Col(dcc.Graph(figure=fig_pct,config={'displayModeBar': False})
                                                         ,style={'padding':'0'},width=2))
                                rise_list.append(dbc.Col(dcc.Graph(figure=fig_rise,config={'displayModeBar': False})
                                                         ,style={'padding': '0'}, width=2))
                                fall_list.append(dbc.Col(dcc.Graph(figure=fig_fall,config={'displayModeBar': False})
                                                         ,style={'padding': '0'}, width=2))


                            title_list = html.Div(dbc.Row(title_list))
                            pct_list = html.Div(dbc.Row(pct_list))
                            rise_list = html.Div(dbc.Row(rise_list))
                            fall_list = html.Div(dbc.Row(fall_list))

                            hist_area = [html.Div(style={'height': '5px', }),
                                         title_list, pct_list, rise_list, fall_list,
                                         html.Div(style={'height': '5px', })]

                            hist_style = {'padding': '5px', 'border-radius': '5px', 'background-color': chart_bg}

                            return fig_line, filter_div, filter_dropdown_div, filter_input_div, _add_button_style,\
                                   None, chart1_button_text, chart2_button_text, hist_area, hist_style


                        else:
                            pass    # No Line Selected


            ## Initialize After Refresh
            if not self.init:
                if not add_button_clicks:
                    if not chart1_button_click:
                        self.sort_method_current = sort_method
                        self.filter_list = []
                        self.add_button_count = 0
                        self.chart2_button_clicks = 0
                        self.save_clicks = 0
                        self.chart_type = 1
                        hist_area = []
                        hist_style = {'display': 'none'}
                        self.init = True
                        filter_dropdown_div = filter_dropdown
                        filter_input_div = filter_input

                   # if not chart1_button_click:
                   #     print('No!!!')
                   #     self.line_selected = -1
                   # self.chart_type = 1
                   # hist_area = []
                   # hist_style = {'display': 'none'}
                   # self.init = True
                   # filter_dropdown_div = filter_dropdown
                   # filter_input_div = filter_input


            ## Add Button Pressed
            if add_button_clicks:
                if add_button_clicks > self.add_button_count: ## Add Button Pressed
                    self.add_button_count = add_button_clicks
                    if filter_name:
                        if filter_input_value: ## Paremeter
                            if filter_name == 'exclude':
                                self.filter_list.append(['exclude', ' ', filter_input_value])
                            else:
                                self.filter_list.append([filter_name[0:-1], filter_name[-1], filter_input_value])
                            filter_div = components.update_filter_div(self.filter_list)
                            if len(self.filter_list) > 11:
                                filter_dropdown_div = filter_dropdown_disabled
                                filter_input_div = filter_input_disabled
                                _add_button_style = add_button_style_disabled
                            else:
                                filter_dropdown_div = filter_dropdown
                                filter_input_div = filter_input
                            self.init = False

            else:
                self.add_button_count = 0  # Necessary for initialization


            # Filter delete button pressed, remove one filter
            for i in range(len(vals)):
                if not vals[i] == self.button_list[i]:
                    self.filter_list.pop(i)
                    filter_div = components.update_filter_div(self.filter_list)
                    filter_dropdown_div = filter_dropdown
                    filter_input_div = filter_input
                    self.add_button_count =- 1  # Necessary for add button count
                    if len(self.filter_list) < 12:
                        filter_dropdown_div = filter_dropdown
                        filter_input_div = filter_input
                        _add_button_style = add_button_style
                    break


            # Sort Method Selected, generate Chart 1
            if sort_method:
                current_df = result_df.copy()

                # Filter according to the filer list
                if len(self.filter_list) > 0:
                    for element in self.filter_list:
                        # print(element)
                        if element[0] == 'exclude':
                            try: code = int(element[2])
                            except: code = element[2]
                            current_df = current_df.loc[current_df['code'] != code]
                        elif element[1] == '<':
                            current_df = current_df.loc[current_df[element[0]] < float(element[2])]
                        else:
                            current_df = current_df.loc[current_df[element[0]] > float(element[2])]

                current_df = current_df.reset_index(drop=True)


                para_key_list = list(para_dict)

                if len(para_checklist) > 0:
                    and_list = []
                    for i in range(len(para_key_list)):
                        key = para_key_list[i]
                        or_list = []
                        for element in para_checklist[i]: # -1 because code / para_dict index
                            if element == 'True':element = True
                            elif element == 'False':element = False
                            _list = current_df[key] == element
                            or_list.append(_list)
                        or_list = np.logical_or.reduce(or_list)
                        and_list.append(or_list)
                    and_list = np.logical_and.reduce(and_list)
                    df_checked = current_df.loc[pd.DataFrame(and_list, columns=['check'])['check']].reset_index(
                        drop=True).copy()
                else:
                    df_checked = current_df.copy()

                # Sort
                graph_df = components.sort_method_df(sort_method, df_checked)
                self.graph_df = graph_df

                fig_line = components.generate_chart_1(graph_df, para_key_list, generate_filepath, filename,
                                                      output_folder, start_date, end_date, para_dict)

                # Disable Chart 2
                chart2_button_text = 'Strategy Analysis >'
                self.chart_type = 1
                hist_style = {'display': 'none'}


            return fig_line, filter_div, filter_dropdown_div,filter_input_div,_add_button_style, \
                   None, chart1_button_text, chart2_button_text, hist_area, hist_style



        # Click on Chart 1 line
        @app.callback(
            Output(component_id='performance_matrix', component_property='children'),
            Output('chart2_button', 'style'),
            Input('line_chart', 'clickData'),
            State(component_id='performance_matrix', component_property='children'),
        )
        def update_matrix(clickData,performance_matrix):
            button_style = {'text-align': 'right','color':'grey','font-size':'14px'}
            self.init = False
            if clickData:
                if self.chart_type == 1:
                    i = clickData['points'][0]['curveNumber'] - 1
                    performance_matrix = components.update_performance_matrix(start_date, end_date,
                                                                              self.graph_df.iloc[i].copy(), para_dict)
                    self.line_selected = i
                    button_style = {'text-align': 'right','cursor': 'pointer','font-size':'14px'}

                    para_key_list = list(para_dict)
                    para_values = []
                    for key in para_key_list:
                        para_values.append(self.graph_df.iloc[self.line_selected][key])
                    save_path = generate_filepath(filename, output_folder, start_date, end_date, para_dict,
                                                  para_values)

                    self.save_clicks = 0 # Needed for save button click tracking

                    df = self.graph_df.iloc[i].copy()
                    self.save_path = save_path
                    self.initial_capital = pd.read_csv(save_path).iloc[0].equity_value
                    self.return_in_capital = df['return_on_capital']
                    self.mdd = df['mdd_pct']
                    self.sharp = df['annualized_sr']


            return performance_matrix, button_style


        # # Model
        # @app.callback(
        #     Output("modal", "is_open"),
        #     [Input("open", "n_clicks"), Input("close", "n_clicks")],
        #     [State("modal", "is_open")],
        # )
        # def toggle_modal(n1, n2, is_open):
        #     # print('Modal!')
        #     if n1 or n2:
        #         return not is_open
        #     else:
        #         pass
        #         # print('No Modal Click')
        #     return is_open


        # Save Button
        @app.callback(
            Output('save_status', "children"),
            Output('save_string', "children"),
            Output('save_button', "style"),
            Input('save_status', "children"),
            Input('save_button', "n_clicks"),
            State('save_string', "children"),
        )
        def save_button(save_status, save_clicks, button_string):
            if not os.path.isfile('saved_strategies.csv'):
                pd.DataFrame(columns=['path','initial','return','mdd','sharp']).to_csv('saved_strategies.csv', index=False)
            else:
                pass

            button_available = None
            save_status = ''
            button_string = ''
            button_style = {}

            # Process until first line selected
            # save_path = self.save_path
            # if self.init:
            #     save_status = ''
            #     button_string = ''
            #     button_style = {}
            # print('Trigger!',self.line_selected)

            save_path = self.save_path
            if not self.init:
                if not save_clicks: #

                    save_status = ''
                    button_string = '--'
                    button_style = {'font-size': '15px', 'margin-left': '20px', 'margin-right': '30px',
                                    'text-align': 'center', 'border-radius': '5px',
                                    'background-color': 'Grey', 'color': 'black',
                                    }

                    if self.line_selected > -1:
                        saved_df = pd.read_csv('saved_strategies.csv')
                        if not save_path in list(saved_df['path']):
                            button_available = True
                        else:
                            button_available = False


                else:
                    if save_clicks > self.save_clicks:
                        self.save_clicks = save_clicks

                        if self.line_selected > -1:
                            saved_df = pd.read_csv('saved_strategies.csv')

                            if not save_path in list(saved_df['path']):
                                saved_df = pd.concat([saved_df, pd.DataFrame({'path': save_path,
                                                                              'initial': self.initial_capital,
                                                                              'return': self.return_in_capital,
                                                                              'mdd': self.mdd,
                                                                              'sharp': self.sharp,
                                                                              },index={10})],
                                                     ignore_index=True)
                                button_available = False
                            else:
                                index = saved_df.index[saved_df['path'] == save_path].tolist()
                                saved_df = saved_df.drop(index=index)
                                button_available = True

                            saved_df.to_csv('saved_strategies.csv', index=False)

            if button_available is not None:
                if button_available:
                    save_status = ''
                    button_string = 'Save Curve'
                    button_style = {'font-size': '15px', 'margin-left': '20px', 'margin-right': '30px',
                                    'text-align': 'center', 'border-radius': '5px', 'cursor': 'pointer',
                                    'background-color': 'Yellow', 'color': 'black',
                                    }
                else:
                    save_status = '( Saved )'
                    button_string = 'Unsave Curve'
                    button_style = {'font-size': '15px', 'margin-left': '20px', 'margin-right': '30px',
                                    'text-align': 'center', 'border-radius': '5px', 'cursor': 'pointer',
                                    'background-color': 'Magenta', 'color': 'white',
                                    }



            return save_status, button_string, button_style



        return app