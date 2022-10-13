import pandas as pd
import numpy as np
import datetime
import math
import os

from dash import dcc, html    ## pip install dash
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots


class Components:
    chart_bg = '#1f2c56'

    sort_method_dropdown = html.Div(
        dbc.Select(id='sort_method',
                   placeholder="Select Sorting Method",
                   value='Top 20 Net Profit',
                   options=[{'label': 'Top 20 Net Profit', 'value': 'Top 20 Net Profit'},
                            {'label': 'Top 20 Return/BaH % Difference', 'value': 'Top 20 Return to BaH Ratio'},
                            {'label': 'Top 20 Net Profit/MDD Ratio', 'value': 'Top 20 Net Profit to MDD'}, ],
                   style={'border-radius': '5px',   'font-size': '12px', }),
        style={'padding-left': '15px', 'width': '235px'})


    filter_dropdown = html.Div(id='filter_dropdown',
                               children=dbc.Select(id='filter_name',
                                                   placeholder="Select Filter",
                                                   options=[
                                                       {'label': 'Exclude Stock', 'value': 'exclude'},
                                                       {'label': 'Return/BaH % Diff. >', 'value': 'return_to_bah>'},
                                                       {'label': 'Return/BaH % Diff. <', 'value': 'return_to_bah<'},
                                                       {'label': 'Sharp Ratio >', 'value': 'annualized_sr>'},
                                                       {'label': 'Sharp Ratio <', 'value': 'annualized_sr<'},
                                                       {'label': 'MDD Percentage >', 'value': 'mdd_pct>'},
                                                       {'label': 'MDD Percentage <', 'value': 'mdd_pct<'},
                                                       {'label': 'Trade Count >', 'value': 'num_of_trade>'},
                                                       {'label': 'Trade Count <', 'value': 'num_of_trade<'},
                                                       {'label': 'COV >', 'value': 'cov>'},
                                                       {'label': 'COV <', 'value': 'cov<'},
                                                       {'label': 'Win Rate >', 'value': 'win_rate>'},
                                                       {'label': 'Win Rate <', 'value': 'win_rate<'},
                                                   ],
                                                   style={'border-radius': '5px', 'font-size': '12px'}),
                               style={'padding-left': '15px', 'width': '175px'})

    filter_dropdown_disabled = html.Div(id='filter_dropdown',
                                        children=dbc.Select(id='filter_name', disabled=True,
                                                            placeholder="Select Filter",
                                                            style={'border-radius': '5px', 'font-size': '12px',
                                                                   'backgroundColor': 'Gray'}),
                                        style={'padding-left': '15px', 'width': '180px'})

    filter_input = dbc.Input(id='filter_input', value=None, size="md", type='text',
                             style={'width': '50px', 'margin-right': '5px', 'border-radius': '3px',
                                      'padding': '6px 5px', 'font-size': '12px', })

    filter_input_disabled = dbc.Input(id='filter_input', value=None, size="md", disabled=True,
                                      style={'width': '50px', 'margin-right': '5px', 'border-radius': '3px',
                                               'padding': '6px 5px', 'font-size': '12px', 'backgroundColor': 'Gray'})

    add_button_style = {'margin-left': '50px', 'width': '150px', 'backgroundColor': 'blue',
                        'border-radius': '5px', 'text-align': 'center', 'cursor': 'pointer',
                        'font-size': '13px', 'height':'30px'}

    add_button_style_disabled = {'margin-left': '50px', 'width': '150px', 'color': 'Silver', 'backgroundColor': 'Gray',
                                 'border-radius': '5px', 'text-align': 'center',
                                 'font-size': '13px', 'height':'30px'}


    def empty_line_chart(self):
        chart_bg = self.chart_bg
        fig_line = px.line()
        fig_line.update_layout(plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, margin=dict(l=85, r=60, t=30, b=40),
                               height=500, font={"color": chart_bg})
        fig_line.update_xaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor=chart_bg)
        fig_line.update_yaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor=chart_bg)

        return fig_line


    def update_checkbox_div(self, para_dict, result_df):
        # find the unique values from result_df according to the key from para_dict
        checkbox_values = {}
        for key in para_dict:
            # if not key == 'code':
            unique_values = list(dict.fromkeys(result_df[key].tolist()))
            try:
                unique_values.sort()
            except:
                pass
            checkbox_values[key] = unique_values

        checkbox_div = []
        for i, para_name in enumerate (para_dict):
            # if not para_name == 'code':
            _options = checkbox_values[para_name]
            if _options == [False, True]:
                _checklist = dcc.Checklist([str(tf) for tf in _options], [str(tf) for tf in _options], inline=True,
                                           id={'type': 'para-checklist', 'index': i},
                                           labelStyle={},
                                           inputStyle={'margin-left': '10px', 'margin-right': '3px'})
            else:
                _checklist = dcc.Checklist(_options, _options, inline=True,
                                           id={'type': 'para-checklist', 'index': i},
                                           labelStyle={'font-size': '12px'},
                                           #label_checked_style={"color": "red"},
                                           inputStyle={'margin-left': '10px', 'margin-right': '3px','background-color':'red',
                                                       'vertical-align':'middle','position':'relative',
                                                       'bottom':'.15em'})
            row = html.Div(
                dbc.Row([
                    html.Div(para_name),
                    html.Div(style={'height': '5px'}),
                    html.Div(_checklist),
                    html.Div(style={'height': '5px'}),
                ]), style={'padding': '0px 20px', 'font-size': '12px'})

            checkbox_div.append(row)

        return checkbox_div

    def update_stat_div(self, period, pct_mean, rise_mean, fall_mean):
        div = html.Div([

            dbc.Row([
                 dbc.Col(width=2),
                 dbc.Col(str(period[0]) + ' Days', width=2),
                 dbc.Col(str(period[1]) + ' Days', width=2),
                 dbc.Col(str(period[2]) + ' Days', width=2),
                 dbc.Col(str(period[3]) + ' Days', width=2),
                 dbc.Col(str(period[4]) + ' Days', width=2),
             ]),

            # html.Div(style={'height': '5px', }),

            dbc.Row([
                 dbc.Col('pct_change', width=2),
                 dbc.Col(f'{pct_mean[0]}%', width=2),
                 dbc.Col(f'{pct_mean[1]}%', width=2),
                 dbc.Col(f'{pct_mean[2]}%', width=2),
                 dbc.Col(f'{pct_mean[3]}%', width=2),
                 dbc.Col(f'{pct_mean[4]}%', width=2),
             ]),

            # html.Div(style={'height': '5px', }),

            dbc.Row([
                 dbc.Col('max_rise', width=2),
                 dbc.Col(f'{rise_mean[0]}%', width=2),
                 dbc.Col(f'{rise_mean[1]}%', width=2),
                 dbc.Col(f'{rise_mean[2]}%', width=2),
                 dbc.Col(f'{rise_mean[3]}%', width=2),
                 dbc.Col(f'{rise_mean[4]}%', width=2),
             ]),

            # html.Div(style={'height': '5px', }),

            dbc.Row([
                 dbc.Col('max_fall', width=2),
                 dbc.Col(f'{fall_mean[0]}%', width=2),
                 dbc.Col(f'{fall_mean[1]}%', width=2),
                 dbc.Col(f'{fall_mean[2]}%', width=2),
                 dbc.Col(f'{fall_mean[3]}%', width=2),
                 dbc.Col(f'{fall_mean[4]}%', width=2),
             ]),

            # html.Div(style={'height': '15px', }),
        ])

        return div


    def generate_radioitems(self, para_dict):
        radioitems_div = []

        for i, key in enumerate(para_dict):
            options = para_dict[key]

            radioitems_div.append(html.Div(key,style={'color': 'Yellow','font-size': '14px'}))

            radioitems_div.append(dcc.RadioItems(
                id={'type': 'para_radioitems', 'index': i},
                options=[{'label': k,
                          'value': k} for k in options],
                labelStyle={'font-size': '13px'},
                inputStyle={'margin-left': '10px', 'margin-right': '5px'}

            ), )

            radioitems_div.append(html.Div(html.Img(),style={'height':'10px'}))

        return radioitems_div


    def update_performance_matrix(self, start_date,end_date,df,para_dict):
        per_col1 =[]
        per_col2 = []
        per_col_1_1 = []
        per_col_1_2 = []
        per_col_2_1 = [html.Div(html.Img())]
        per_col_2_2 = [html.Div('Selected',style={'text-align': 'center', 'font-weight': 'bold', 'color':'yellow'})]
        per_col_2_3 = [html.Div('BaH',style={'text-align': 'center', 'font-weight': 'bold', 'color':'yellow'})]

        keys = ['num_of_trade',
                'net_profit',
                'net_profit_to_mdd',
                'return_to_bah',
                'win_rate',
                'cov',
                'total_commission',
                'return_on_capital',
                'annualized_return',
                'annualized_std',
                'annualized_sr',
                'mdd_dollar',
                'mdd_pct',
                'bah_return',
                'bah_annualized_return',
                'bah_annualized_std',
                'bah_annualized_sr',
                'bah_mdd_dollar',
                'bah_mdd_pct',
                ]

        try:
            df['net_profit'] = "{:,}".format(int(round(df['net_profit'], 0)))
            if df['net_profit_to_mdd'] == np.inf: df['net_profit_to_mdd'] = 'inf'
            else: df['net_profit_to_mdd'] = round(df['net_profit_to_mdd'], 2)
            df['total_commission'] = "{:,}".format(int(round(df['total_commission'] , 0)))

            df['mdd_dollar'] = "{:,}".format(int(round(df['mdd_dollar'], 0)))
            df['mdd_pct'] = "{:.0%}".format(df['mdd_pct'] / 100)
            df['return_on_capital'] = "{:.0%}".format(df['return_on_capital'] / 100)
            df['annualized_return'] = "{:.0%}".format(df['annualized_return'] / 100)
            df['annualized_std'] = "{:.0%}".format(df['annualized_std'] / 100)

            df['cov'] = round(df['cov'], 2)
            df['win_rate'] = "{:.0%}".format(df['win_rate'] / 100)
            df['return_to_bah'] = "{:.0%}".format(df['return_to_bah'] / 100)

            df['bah_mdd_dollar'] = "{:,}".format(int(round(df['bah_mdd_dollar'], 0)))
            df['bah_mdd_pct'] = "{:.0%}".format(df['bah_mdd_pct'] / 100)
            df['bah_return'] = "{:.0%}".format(df['bah_return'] / 100)
            df['bah_annualized_return'] = "{:.0%}".format(df['bah_annualized_return'] / 100)
            df['bah_annualized_std'] = "{:.0%}".format(df['bah_annualized_std'] / 100)
            # df['bah_annualized_sr'] = round(df['bah_annualized_sr'], 1)
        except Exception as e:
            # print(e)
            pass

        per_col_1_1.append(html.Div('Number of Trade'))
        per_col_1_1.append(html.Div('Net Profit'))
        per_col_1_1.append(html.Div('Net Profit/MDD Ratio'))
        per_col_1_1.append(html.Div('Return/BaH % Diff.'))
        per_col_1_1.append(html.Div('Win Rate'))
        per_col_1_1.append(html.Div('COV'))
        per_col_1_1.append(html.Div('Total Commission'))

        per_col_2_1.append(html.Div('Return on Capital'))
        per_col_2_1.append(html.Div('Ann. Return'))
        per_col_2_1.append(html.Div('Ann. Std'))
        per_col_2_1.append(html.Div('Ann. Sharp Ratio'))
        per_col_2_1.append(html.Div('MDD Dollar'))
        per_col_2_1.append(html.Div('MDD Percentage'))

        for i in range(7):
            per_col_1_2.append(html.Div(df[keys[i]], style={'text-align': 'center'}))
        for i in range(7, 13):
            per_col_2_2.append(html.Div(str(df[keys[i]]), style={'text-align': 'center'}))
        for i in range(13, 19):
            per_col_2_3.append(html.Div(str(df[keys[i]]), style={'text-align': 'center'}))

        per_col1.append(dbc.Row([dbc.Col(html.Div(per_col_1_1), width=6),
                                 dbc.Col(per_col_1_2, style={'padding': '0'}, width=6)]))
        per_col2.append(dbc.Row([dbc.Col(html.Div(per_col_2_1), width=6),
                                 dbc.Col(per_col_2_2, style={'padding': '0'}, width=3),
                                 dbc.Col(per_col_2_3, style={'padding': '0'}, width=3)
                                 ]))

        start_date_year = datetime.datetime.strptime(start_date, '%Y-%m-%d').year
        end_date_year = datetime.datetime.strptime(end_date, '%Y-%m-%d').year
        year_list = list(range(start_date_year, end_date_year + 1))

        year_col1 = [dbc.Row([dbc.Col(style={'margin-left':'15px'}, width=3),
                              dbc.Col('Year Count', style={'text-align': 'center', 'font-weight': 'bold', 'color':'yellow'},width=4),
                              dbc.Col('Win Rate', style={'text-align': 'center', 'font-weight': 'bold', 'color':'yellow'},width=4)
                              ], style={'font-size': '11px'})]


        for i in range(len(year_list)):
            try:
                # print(df[f'{year_list[i]}_win_rate'])
                # # win_rate = df[f'{year_list[i]}_win_rate']
                # print(df[f'{year_list[i]}_win_rate'].value())
                # print(df[f'{year_list[i]}_win_rate'])
                win_rate = "{:.0%}".format( int(df[f'{year_list[i]}_win_rate'])/100 )
            except:
                win_rate = '-----'

            year_col1.append(dbc.Row([dbc.Col(year_list[i],style={'margin-left':'15px'} ,width=3),
                                      dbc.Col(df[str(year_list[i])], style={'text-align': 'center'} , width=4),
                                      dbc.Col(win_rate, style={'text-align': 'center'} , width=4)]))
        # Selected Equity Curve
        title = []
        for key in para_dict:
            title.append(dbc.Row(
                [dbc.Col(key,width=6),
                dbc.Col(f'{df[key]}',style={ 'text-align': 'center'},width=6)]))



        matrix_div = html.Div([
            html.Div(style={'height': '8px', }),

            html.Div([
                html.Div('Selected Curve', style={'color': 'Cyan',
                                                  'display': 'inline',
                                                  'font-size': '15px'}),
                html.Div('', id='save_status',
                         style={'color': 'Cyan',
                                'display': 'inline',
                                'padding-left': '5px',
                                'font-size': '15px'}),
            ]),

            #
            # dbc.Row([
            #     dbc.Col(html.Div('Selected Curve', style={'color': 'Cyan', 'font-size': '15px'}), width=7),
            #     dbc.Col(html.Div('--', id='save_status',
            #                      style={'color': 'Grey',
            #                             'padding-left': '5px',
            #                             'font-size': '15px'}),
            #             width=4),
            #     # dbc.Col(html.Div('--', id='save',
            #     #                  style={'font-size': '15px',
            #     #                         'text-align': 'center', 'border-radius': '5px',
            #     #                         'background-color': 'Grey', 'color':'black',
            #     #                         }), width=5),
            #     # dbc.Col(html.Div('List All', id="open",
            #     #                  style={'font-size': '15px','cursor': 'pointer',
            #     #                         'text-align': 'center', 'border-radius': '5px',
            #     #                         'background-color': 'Yellow', 'color':'black',
            #     #                         }), width=4),
            # ], style={'padding-right': '20px'}),

            # dbc.Modal(
            #     [
            #         # dbc.ModalHeader("HEADER"),
            #         dbc.ModalBody("List of Saved Strategies here"),
            #         dbc.ModalBody(html.Div('Close', id="close", style={'font-size': '15px', 'cursor': 'pointer'})),
            #
            #         # dbc.ModalFooter(
            #         #     dbc.Button("CLOSE BUTTON", id="close", className="ml-auto")
            #         # ),
            #     ],
            #     id="modal",
            # ),

            # html.Div(style={'height': '5px', }),

            dbc.Row(html.Div(title), style={'font-size': '11px'}),

            html.Div(style={'height': '15px', }),

            html.Div('Performance', style={'color': 'Cyan', 'font-size': '15px'}),
            html.Div(children=per_col1, style={'font-size': '11px'}),
            html.Div(style={'height': '15px', }),

            html.Div('Comparison', style={'color': 'Cyan', 'font-size': '15px'}),
            html.Div(children=per_col2, style={'font-size': '11px','padding-right': '10px'}),
            html.Div(style={'height': '15px', }),

            html.Div('Performance by Year', style={'color': 'Cyan', 'font-size': '15px'}),
            html.Div(style={'height': '5px', }),
            html.Div(children=year_col1, style={'font-size': '11px'}),
            html.Div(style={'height': '20px'}),

            html.Div([
                html.Div(style={'height': '5px'}),
                html.Div('', id='save_string'),
                html.Div(style={'height': '5px'}),
            ], id='save_button'),

        ],style={'padding': '0px',})

        return matrix_div


    def selection_title(self, para_dict, values):
        title = []
        for i, key in enumerate(para_dict):
            title.append(dbc.Row(
                [dbc.Col(key, width=6),
                 dbc.Col(f'{values[i]}', style={'text-align': 'center'}, width=6)]))

        return title



    filter_options = {
            'num_of_trade':'Trade Count',
            'annualized_sr': 'Sharp Ratio',
            'mdd_pct':'MDD Percentage',
            'cov':'COV',
            'win_rate':'Win Rate',
            'return_to_bah': 'Return/BnH % Diff.',
            'exclude': 'Exclude',
        }
    def update_filter_div(self, filter_list):
        filter_button = []
        for i, element in enumerate(filter_list):
            # element = filter_list[i]
            filter_full = []
            filter_full.append(html.Div(self. filter_options[element[0]], style={'margin-right': '15px', 'display': 'inline'}))
            filter_full.append(html.Div(element[1], style={'margin-right': '15px', 'display': 'inline'}))
            filter_full.append(html.Div(element[2], style={'margin-right': '15px', 'display': 'inline'}))
            filter_button.append(dbc.Row([
                dbc.Col(html.Div(filter_full,
                                 style={'font-size': '12px', 'padding': '0px', 'margin': '0px'}), width=10),
                dbc.Col(html.Div(children=html.Div('✗', style={'padding': '0px', 'margin': '0px'}),
                                 id='button_' + str(i), n_clicks=i,
                                 style={'font-size': '12px', 'backgroundColor': 'rgba(0, 0, 0, 0)',
                                        'border': '0px black solid', 'padding': '0px', 'padding-bottom': '10px',
                                        'margin': '0px', 'width': '5px', 'cursor': 'pointer'}), width=2)
            ]))

        for i in range(len(filter_list), 10):
            filter_button.append(html.Div(id='button_' + str(i), n_clicks=i))

        return filter_button


    def sort_method_df(self, sort_method, result_df):
        if sort_method == 'Top 20 Net Profit':
            df_sorted = result_df.sort_values(by='net_profit', ascending=False).head(20).copy()
        elif sort_method == 'Top 20 Net Profit to MDD':
            df_sorted = result_df.sort_values(by='net_profit_to_mdd', ascending=False).head(20).copy()
        elif sort_method == 'Top 20 Return to BaH Ratio':
            df_sorted = result_df.sort_values(by='return_to_bah', ascending=False).head(20).copy()
        else:
            df_sorted = result_df.copy()

        df_sorted = df_sorted.reset_index(drop=True)

        line_colour = []
        for c in range(len(df_sorted)):
            profile = c % 6
            degree = (c // 6) / math.ceil(len(df_sorted) / 6)
            line_colour.append(self.assign_colour(profile, degree))
        df_sorted['line_colour'] = line_colour

        return df_sorted


    def assign_colour(self, profile, degree):
        if profile == 0:    rgb = (0, int(252 - 252 * degree), 252)
        elif profile == 1:  rgb = (int(252 - 252 * degree), 252, 0)
        elif profile == 2:  rgb = (252, 0, int(252 - 252 * degree))
        elif profile == 3:  rgb = (0, 252, int(252 * degree))
        elif profile == 4:  rgb = (252, int(252 * degree), 0)
        elif profile == 5:  rgb = (int(252 * degree), 0, 252)
        return 'rgb' + str(rgb)


    def generate_chart_1(self, graph_df, para_key_list, generate_filepath, filename, output_folder, start_date, end_date,
                   para_dict):
        fig_line = px.line()
        fig_line.update_layout(title = {'text': filename})
        fig_line.update_xaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
        fig_line.update_yaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
        fig_line.update_layout(plot_bgcolor=self.chart_bg, paper_bgcolor=self.chart_bg, height=500,
                               margin=dict(l=85, r=25, t=60, b=0),
                               showlegend=False,
                               font={"color": "white", 'size': 10.5}, yaxis={'title': 'Equity'},
                               xaxis={'title': ''}
                               )

        for i in graph_df.index:
            para_values = []
            hovertemplate = "%{x}<br>"
            for key in para_key_list:
                para_values.append(graph_df.iloc[i][key])
                hovertemplate = hovertemplate + \
                                key + " : " + str(graph_df.iloc[i][key]) + "<br>"
            hovertemplate = hovertemplate + "<br>"
            hovertemplate = hovertemplate + "Return/BaH % Diff. : " + str(
                round(graph_df.iloc[i]['return_to_bah'], 2)) + "<br>"
            hovertemplate = hovertemplate + "Net Profit to MDD: " + str(
                round(graph_df.iloc[i]['net_profit_to_mdd'], 2)) + "<br>"
            hovertemplate = hovertemplate + "Sharp Ratio : " + str(graph_df.iloc[i]['annualized_sr']) + "<br>"
            hovertemplate = hovertemplate + "MDD Percentage : " + "{:.0%}".format(
                graph_df.iloc[i]['mdd_pct'] / 100) + "<br>"
            hovertemplate = hovertemplate + "Trade Count : " + str(graph_df.iloc[i]['num_of_trade']) + "<br>"
            hovertemplate = hovertemplate + "COV : " + str(round(graph_df.iloc[i]['cov'], 2)) + "<br>"
            hovertemplate = hovertemplate + "Win Rate : " + "{:.0%}".format(
                graph_df.iloc[i]['win_rate'] / 100) + "<br>"
            hovertemplate = hovertemplate + "<br>"

            save_path = generate_filepath(filename, output_folder, start_date, end_date, para_dict, para_values)
            line_colour = graph_df.loc[i].line_colour

            df = pd.read_csv(save_path)
            df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

            hovertemplate = hovertemplate + "Equity : %{y:,.0f}"

            fig_line.add_trace(go.Scatter(mode='lines', hovertemplate=hovertemplate,
                                          x=df['date'], y=df['equity_value'],
                                          line=dict(color=line_colour, width=1.5), name=''), )
        return fig_line


    def prepare_df_chart(self, df):     # Chart Data for Chart 2
        initial_value = df.iloc[0].equity_value

        df_chart = df.copy()
        df_chart['date'] = pd.to_datetime(df_chart['date'], format='%Y-%m-%d')
        df_chart['bah'] = df['close'] * (initial_value / df_chart.iloc[0].close)

        _open = []
        _stop_loss = []
        _close_logic = []
        _profit_target = []

        for i in range(len(list(df['action']))):
            element = list(df['action'])[i]
            if element == 'open':
                _open.append(df_chart.iloc[i].bah)
                _stop_loss.append(None)
                _close_logic.append(None)
                _profit_target.append(None)
            elif element == 'stop_loss':
                _open.append(None)
                _stop_loss.append(df_chart.iloc[i].bah)
                _close_logic.append(None)
                _profit_target.append(None)
            elif element == 'close_logic':
                _open.append(None)
                _stop_loss.append(None)
                _close_logic.append(df_chart.iloc[i].bah)
                _profit_target.append(None)
            elif element == 'profit_target':
                _open.append(None)
                _stop_loss.append(None)
                _close_logic.append(None)
                _profit_target.append(df_chart.iloc[i].bah)
            else:
                _open.append(None)
                _stop_loss.append(None)
                _close_logic.append(None)
                _profit_target.append(None)

        df_chart['open'] = _open
        df_chart['stop_loss'] = _stop_loss
        df_chart['close_logic'] = _close_logic
        df_chart['profit_target'] = _profit_target

        return df_chart


    def generate_chart_2(self,df_chart,line_colour, para_dict,para_values, settings):
        df_signal = df_chart.copy()
        df_signal = df_signal.dropna(subset=['action'])
        df_signal = df_signal.reset_index()
        signal_open_date = []
        signal_open_close = []
        signal_close_date = []
        signal_close_close = []
        signal_close_reason = []


        for i, row in df_signal.iterrows():
            if row['action'] == 'open':
                signal_open_date.append(df_signal.iloc[i]['date'])
                signal_open_close.append(df_signal.iloc[i]['close'])
                signal_close_date.append(df_signal.iloc[i + 1]['date'])
                signal_close_close.append(df_signal.iloc[i + 1]['close'])
                signal_close_reason.append(df_signal.iloc[i + 1]['action'])
            else:
                signal_open_date.append(df_signal.iloc[i - 1]['date'])
                signal_open_close.append(df_signal.iloc[i - 1]['close'])
                signal_close_date.append(df_signal.iloc[i]['date'])
                signal_close_close.append(df_signal.iloc[i]['close'])
                signal_close_reason.append(df_signal.iloc[i]['action'])

        df_signal['signal_open_date'] = signal_open_date
        df_signal['signal_open_close'] = signal_open_close
        df_signal['signal_close_date'] = signal_close_date
        df_signal['signal_close_close'] = signal_close_close
        df_signal['close_reason'] = signal_close_reason
        df_signal = df_signal.set_index('date')

        open_date = []
        open_close = []
        close_date = []
        close_close = []
        close_reason = []
        for i, row in df_chart.iterrows():
            try:
                open_date.append(df_signal.loc[row['date']].signal_open_date.strftime("%Y-%m-%d"))
            except:
                open_date.append(None)
            try:
                open_close.append(df_signal.loc[row['date']].signal_open_close)
            except:
                open_close.append(None)
            try:
                close_date.append(df_signal.loc[row['date']].signal_close_date.strftime("%Y-%m-%d"))
            except:
                close_date.append(None)
            try:
                close_close.append(df_signal.loc[row['date']].signal_close_close)
            except:
                close_close.append(None)
            try:
                close_reason.append(df_signal.loc[row['date']].close_reason)
            except:
                close_reason.append(None)

        df_signal_final = pd.DataFrame()
        df_signal_final['open_date'] = open_date
        df_signal_final['open_close'] = open_close
        df_signal_final['close_date'] = close_date
        df_signal_final['close_close'] = close_close
        df_signal_final['close_reason'] = close_reason
        df_signal_final['pctchange'] = ((df_signal_final['close_close'] - df_signal_final['open_close']) /
                                        df_signal_final['open_close']) * 100
        df_signal_final.open_close = df_signal_final.open_close.round(2)
        df_signal_final.close_close = df_signal_final.close_close.round(2)
        df_signal_final.pctchange = df_signal_final.pctchange.round(2)

        hover_template = "<br>".join([
            "Close Reason: %{customdata[4]}",
            "Open Date: %{customdata[0]}",
            "Close Date: %{customdata[2]}",
            "Open Close: %{customdata[1]}",
            "Close Close: %{customdata[3]}",
            "Pct Change: %{customdata[5]}%",
        ])

        self.selection_title(para_dict, para_values)

        title = ''
        for i, key in enumerate(para_dict):
            title = title + f'{key}:{para_values[i]} '

        # Count number of subchart
        subchart_count = 0
        try:
            fig = settings['subchart_1']
            subchart_count += 1
        except Exception as e: pass
        try:
            fig = settings['subchart_2']
            subchart_count += 1
        except Exception as e: pass

        if subchart_count == 0: row_height = [1]
        if subchart_count == 1: row_height = [0.85,0.15]
        if subchart_count == 2: row_height = [0.7,0.15,0.15]

        fig_line = make_subplots(rows=subchart_count+1, cols=1,
                                 row_heights=row_height,shared_xaxes=True)

        fig_line.update_layout(title = {'text': title , 'font': {'size': 10 }  })
        fig_line.update_xaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
        fig_line.update_yaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
        fig_line.add_trace(go.Scatter(mode='lines', hoverinfo='skip',
                                      x=df_chart['date'], y=df_chart['equity_value'],
                                      line=dict(color=line_colour, width=1), name='Strategy Equity'), row=1, col=1)
        fig_line.add_trace(go.Scatter(mode='lines', hoverinfo='skip',
                                      x=df_chart['date'], y=df_chart['bah'],
                                      line=dict(color='Grey', width=1), name='BnH Equity'),row=1, col=1 )
        fig_line.update_layout(plot_bgcolor=self.chart_bg, paper_bgcolor=self.chart_bg, height=500,
                               margin=dict(l=85, r=25, t=35, b=20),
                               font={"color": "white", 'size': 9}, yaxis={'title': 'Equity'},
                               xaxis={'title': ''}
                               )
        fig_line.add_trace(go.Scatter(mode='markers', customdata=df_signal_final, hovertemplate=hover_template,
                                      x=df_chart['date'], y=df_chart['open'], visible='legendonly',
                                      marker=dict(color='rgba(0, 0, 0, 0)', size=9,
                                                  line=dict(color='yellow', width=2.5)), name='open'), row=1, col=1)
        fig_line.add_trace(go.Scatter(mode='markers', customdata=df_signal_final, hovertemplate=hover_template,
                                      x=df_chart['date'], y=df_chart['close_logic'], visible='legendonly',
                                      marker=dict(color='rgba(0, 0, 0, 0)', size=9,
                                                  line=dict(color='green', width=2.5)), name='close_logic'), row=1, col=1)
        fig_line.add_trace(go.Scatter(mode='markers', customdata=df_signal_final, hovertemplate=hover_template,
                                      x=df_chart['date'], y=df_chart['profit_target'], visible='legendonly',
                                      marker=dict(color='rgba(0, 0, 0, 0)', size=9,
                                                  line=dict(color='red', width=2.5)), name='profit_target'), row=1, col=1)
        fig_line.add_trace(go.Scatter(mode='markers', customdata=df_signal_final, hovertemplate=hover_template,
                                      x=df_chart['date'], y=df_chart['stop_loss'], visible='legendonly',
                                      marker=dict(color='rgba(0, 0, 0, 0)', size=9,
                                                  line=dict(color='Cyan', width=2.5)), name='stop_loss'), row=1, col=1)


        subchart_count = 2
        try:
            fig = self.generate_subchart(df_chart, settings['subchart_1'][0], settings['subchart_1'][1], 'yellow')
            fig_line.add_trace(fig, row=subchart_count, col=1)
            subchart_count += 1
        except Exception as e:
            # print(e)
            pass
        try:
            fig = self.generate_subchart(df_chart, settings['subchart_2'][0], settings['subchart_2'][1], '#FF01FE')
            fig_line.add_trace(fig, row=subchart_count, col=1)
        except Exception as e:
            # print(e)
            pass



        return fig_line


    def generate_subchart(self,df_chart, element, line_type, line_color):
        if line_type == 'bar':
            fig = go.Bar(hoverinfo='skip', x=df_chart['date'], y=df_chart[element], showlegend=True,
                           marker_color=line_color, marker_line_color=line_color, name=element)
        else:
            fig = go.Scatter(mode='lines', hoverinfo='skip', x=df_chart['date'], y=df_chart[element], showlegend=True,
                           line=dict(color=line_color, width=1.5), name=element)
        return fig


    def generate_histogram(self, df, period, mode):
        chart_bg = self.chart_bg
        col_pct = 'pct_change_' + str(period)
        col_rise = 'max_rise_' + str(period)
        col_fall = 'max_fall_' + str(period)
        df_his = df.copy()
        df_his[col_pct] = df_his['close'].pct_change(period)
        df_his[col_pct] = df_his[col_pct].shift(-1 * period)
        df_his[col_pct] = df_his[col_pct] * 100
        df_his[col_pct] = df_his[col_pct].map(lambda x: round(x, 2))
        df_his[col_rise] = (df_his['high'].rolling(period).max().shift(-1 * (period)) / df_his['close']) - 1
        df_his[col_fall] = (df_his['low'].rolling(period).min().shift(-1 * (period)) / df_his['close']) - 1
        if mode == 'backtest':
            df_his = df_his[df_his['action'] == 'open']
        else:
            df_his = df_his[df_his['logic'] == 'trade_logic']

        df_his[col_rise] = df_his[col_rise] * 100
        df_his[col_fall] = df_his[col_fall] * 100

        df_his[col_rise] = df_his[col_rise].map(lambda x: round(x, 2))
        df_his[col_fall] = df_his[col_fall].map(lambda x: round(x, 2))

        df_his = df_his[['date'] + [col_pct, col_rise, col_fall]]

        margin = dict(l=5, r=5, t=5, b=15)
        h = 70
        w = 120
        f = {"color": "white", 'size': 8}

        fig_pct = go.Figure()
        fig_pct.update_layout(plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, height=h, width=w, margin=margin,
                              font=f, bargap=0.1)
        fig_pct.update_xaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor='#1f2c56', )
        fig_pct.update_yaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor='#626567', )
        fig_pct.add_trace(go.Histogram(x=df_his[col_pct], marker_color='Cyan'))

        fig_rise = go.Figure()
        fig_rise.update_layout(plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, height=h, width=w, margin=margin,
                               font=f, bargap=0.1)
        fig_rise.update_xaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor='#1f2c56', )
        fig_rise.update_yaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor='#626567', )
        fig_rise.add_trace(go.Histogram(x=df_his[col_rise], marker_color='Yellow'))

        fig_fall = go.Figure()
        fig_fall.update_layout(plot_bgcolor=chart_bg, paper_bgcolor=chart_bg, height=h, width=w, margin=margin,
                               font=f, bargap=0.1)
        fig_fall.update_xaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor='#1f2c56', )
        fig_fall.update_yaxes(showline=True, zeroline=False, linecolor='#979A9A', gridcolor='#626567', )
        fig_fall.add_trace(go.Histogram(x=df_his[col_fall], marker_color='Fuchsia'))

        return fig_pct, fig_rise, fig_fall


    def path_to_dict(self,path):
        filename = path.split('/')[-1].split('.csv')[0]
        parameters = {}
        for element in filename.split('&'):
            key, content = element.split('=')
            if key == 'date':
                # parameters['date'] = f'{content[:8]} - {content[8:]}'
                parameters['startdate'], parameters['enddate'] = content[:8], content[8:]
            else:
                parameters[key] = content

        return parameters


    def generate_df_stat(self, df, period):
        col_pct = 'pct_change_' + str(period)
        col_rise = 'max_rise_' + str(period)
        col_fall = 'max_fall_' + str(period)
        df_his = df.copy()
        df_his[col_pct] = df_his['close'].pct_change(period)
        df_his[col_pct] = df_his[col_pct].shift(-1 * period)
        df_his[col_pct] = df_his[col_pct] * 100
        df_his[col_pct] = df_his[col_pct].map(lambda x: round(x, 2))
        df_his[col_rise] = (df_his['high'].rolling(period).max().shift(-1 * (period)) / df_his['close']) - 1
        df_his[col_fall] = (df_his['low'].rolling(period).min().shift(-1 * (period)) / df_his['close']) - 1

        df_his = df_his[df_his['logic'] == 'trade_logic']

        df_his[col_rise] = df_his[col_rise] * 100
        df_his[col_fall] = df_his[col_fall] * 100

        df_his[col_rise] = df_his[col_rise].map(lambda x: round(x, 2))
        df_his[col_fall] = df_his[col_fall].map(lambda x: round(x, 2))

        return round(df_his[col_pct].mean(), 2), round(df_his[col_rise].mean(), 2), round(df_his[col_fall].mean(), 2)


    def aggregate_df(self):
        folders = []
        for filename in os.listdir():
            if os.path.isfile(f'{filename}/saved_strategies.csv'):
                folders.append(filename)
        folders.sort()

        equity_curves = []
        for folder in folders:
            df_saved = pd.read_csv(f'{folder}/saved_strategies.csv')
            for i, row in df_saved.iterrows():
                equity_path = f'{folder}/{row["path"]}'
                parameters = self.path_to_dict(equity_path)
                dict = {}
                dict['folder'] = folder
                dict['py'] = parameters['file']
                dict['path'] = equity_path
                dict['parameters'] = parameters
                equity_curves.append(dict)

        line_colour = []
        for c in range(len(equity_curves)):
            profile = c % 6
            degree = (c // 6) / math.ceil(len(equity_curves) / 6)
            line_colour.append(self.assign_colour(profile, degree))

        df = pd.DataFrame.from_dict(equity_curves, orient='columns', dtype=None, columns=None)
        df['line_colour'] = line_colour
        df.index += 1

        choices = []
        for i in list(df.index):
            line_height = '120%'
            text = []
            for key, value in df.iloc[i - 1].parameters.items():
                if not key == 'file':
                    text.append(html.Div(f'{key} : {value}',style={'line-height': line_height}))
            choices.append({
                "label": html.Div([

                    html.Div('----------------------------------------------------------------------------------'),

                    dbc.Row([
                        dbc.Col([html.Div('Curve', style={'line-height': line_height})],
                                width=3),
                        dbc.Col([html.Div(str(i).zfill(3), style={'line-height': line_height})],
                                width=6),
                    ]),

                    html.Div(style={'height': '5px'}),

                    dbc.Row([
                        dbc.Col([html.Div('folder',style={'line-height':line_height})],
                                width=3),
                        dbc.Col([html.Div(df.iloc[i - 1].folder,style={'line-height':line_height})],
                                width=6),
                    ]),

                    html.Div(style={'height': '5px'}),

                    dbc.Row([
                        dbc.Col([html.Div('.py',style={'line-height':line_height})],
                                width=3),
                        dbc.Col([html.Div(df.iloc[i - 1].py,style={'line-height':line_height})],
                                width=6),
                    ]),

                    html.Div(style={'height': '5px'}),

                    dbc.Row([
                        dbc.Col([html.Div('parameters',style={'line-height':line_height})],
                                width=3),
                        dbc.Col([html.Div(text,style={'line-height':line_height})],
                                width=6),
                    ]),

                ],style={"display": "inline-block", 'width':'400px'}

                ),

                "value": i,
            })

        _checklist = html.Div([
            dcc.Checklist(
                options=choices,
                id='curve_checklist',
                value=list(df.index),
                inputStyle={'margin-left': '3px', 'margin-right': '10px',
                               'background-color': 'red',
                               'vertical-align': 'top', 'position': 'relative',
                               'top': '1.6em'}
            )],

        ),

        row = html.Div(
            dbc.Row([
                html.Div(_checklist),
                html.Div(style={'height': '5px'}),
            ]), style={'padding': '0px', 'font-size': '12px'})

        return df, row