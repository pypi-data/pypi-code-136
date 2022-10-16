from dash import Dash, dcc, html, Input, Output, State, ALL
import dash_daq as daq
from .components import *
import time

class Aggregate:

    chart_bg = '#1f2c56'
    valid_colour = 'DeepSkyBlue'
    df_equity_curves = pd.DataFrame()
    df_ready = False

    def __new__(self):

        chart_bg = self.chart_bg
        components = Components()
        valid_colour = self.valid_colour

        empty_line_chart = components.empty_line_chart()

        self.df_equity_curves, checklist_div = components.aggregate_df()

        app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO,dbc.icons.BOOTSTRAP], suppress_callback_exceptions=True)

        app.layout = html.Div([

            dbc.Row([
                # Left Column
                dbc.Col(html.Div([

                    html.Div(style={'height': '10px', }),

                    html.Div(children=html.Div([
                        html.Div(style={'height': '10px', }),

                        html.Div('Equity Curves', style={'color': 'DeepSkyBlue', 'font-size': '17px'}),

                        html.Div(style={'height': '10px', }),

                        html.Div(id='checklist-container', children=checklist_div,
                                 style={
                                        'maxHeight': '628px',
                                        'minHeight': '628px',
                                        'overflow-y': 'scroll',
                                        'overflow-x': 'hidden',
                                        }),

                    ],), style={'padding': '5px 5px','padding-left':'15px', 'border-radius': '5px',
                                'font-size': '13px','background-color': chart_bg},
                    ),

                ],), style={'padding': '0', 'padding-left': '5px',}, width=4),

                # Right Column
                dbc.Col(html.Div([

                    html.Div(style={'height': '10px', }),

                    html.Div(children=html.Div([

                        html.Div(style={'height': '10px', }),

                        html.Div([
                            html.Div(html.Div('Aggregate', id='aggregate_string',style={'color': valid_colour}),
                                     style={'vertical-align': 'top',
                                            'position': 'relative','top': '0.12em',
                                            'display': 'inline-block'}),

                            html.Div(daq.BooleanSwitch(on=True, color=valid_colour,id='aggregate_boolean',
                                                       style={'height':'5px',}),
                                     style={'margin-left':'5px','display':'inline-block'}),

                            html.Div(html.Div('Normalized',id='normalized_string',style={'color': 'Grey'}),
                                     style={'margin-left':'15px', 'vertical-align': 'top',
                                            'position': 'relative', 'top': '0.12em',
                                            'display': 'inline-block'}),

                            html.Div(daq.BooleanSwitch(on=False, color=valid_colour,id='normalized_boolean',
                                                       style={'height': '5px', }),
                                     style={'margin-left':'5px','display': 'inline-block'}),

                        ]),



                        html.Div(style={'height': '15px', }),

                        html.Div(id='performance_div',
                                 style={'padding-left':'10px', 'font-size': '14px'}),

                        html.Div(style={'height': '15px', }),

                        html.Div(id='chart_area',
                                 children=dcc.Graph(id='line_chart',
                                                    figure=empty_line_chart)),

                        html.Div(style={'height': '20px', }),

                    ]), style={'padding': '5px 25px', 'border-radius': '5px',
                               'background-color': chart_bg}),

                ]), style={'padding': '0', 'padding-left': '5px'}, width=8),

            ]),

        ], style={'width': '1400px', 'margin': 'auto', 'padding': '0px', 'color': 'white'})


        # For initial curve list
        @app.callback(
            Output('checklist-container', 'children'),
            Input('checklist-container', 'children'),
        )
        def init_checklist(checklist_container):
            self.df_ready = False
            self.df_equity_curves, checklist_div = components.aggregate_df()
            self.df_ready = True

            return checklist_div


        @app.callback(
            Output('line_chart', 'figure'),
            Output('normalized_string', 'style'),
            Output('aggregate_string', 'style'),
            Output('performance_div', 'children'),
            Input('curve_checklist', 'value'),
            Input('normalized_boolean','on'),
            Input('aggregate_boolean', 'on')
        )
        def aggregate_chart(curve_checklist,normalized_boolean, aggregate_boolean):

            while not self.df_ready:
                time.sleep(0.2)

            curve_checklist.sort()
            valid_colour = self.valid_colour

            title_text = ''

            if aggregate_boolean:
                aggregate_style = {'color': valid_colour}
                title_text += 'Aggregate '
            else:
                aggregate_style = {'color': 'Grey'}

            if normalized_boolean:
                normalized_style = {'color': valid_colour}
                title_text += 'Normalized '
            else:
                normalized_style = {'color': 'Grey'}

            title_text += 'Equity Curves'


            df = self.df_equity_curves.loc[curve_checklist]
            folders = list(df['folder'])
            pys = list(df['py'])
            paths = list(df['path'])

            dfs = []
            for i, path in enumerate(paths):
                df = pd.read_csv(path, index_col='date')
                df_current = pd.DataFrame()
                if normalized_boolean:
                    df_current[f'{folders[i]}_{pys[i]}_{i}'] = df['equity_value'] / (df['equity_value'].iloc[0] / 100000)
                else:
                    df_current[f'{folders[i]}_{pys[i]}_{i}'] = df['equity_value']
                df_current.index = df.index
                dfs.append(df_current.copy())

            df_all_curves = pd.concat(dfs, axis=1).sort_index()
            df_all_curves = df_all_curves.fillna(method='pad')
            df_all_curves = df_all_curves.fillna(method='backfill')
            df_all_curves["Aggregate_Equity"] = df_all_curves.sum(axis=1)
            if normalized_boolean:
                df_all_curves["Aggregate_Equity"] = df_all_curves["Aggregate_Equity"] / (len(df_all_curves.columns) - 1)
            # print(df_all_curves)

            # Performance
            df_agg = df_all_curves['Aggregate_Equity']
            dd_pct = []
            for i in range(len(df_agg)):
                max_list = list(df_agg[:i + 1]).copy()
                dd = max(max_list) - df_agg.iloc[i]
                dd_pct.append( dd / max(max_list))
                # print(dd, max(max_list), dd / max(max_list))
            mdd_pct = max(dd_pct)

            df_all_curves['date'] = pd.to_datetime(df_all_curves.index, format='%Y-%m-%d')
            holding_period_day = (df_all_curves.loc[df_all_curves.index[-1], 'date'] - df_all_curves.loc[
                df_all_curves.index[0], 'date']).days

            equity_value_pct_series = df_all_curves["Aggregate_Equity"].pct_change()
            equity_value_pct_series = equity_value_pct_series.dropna()

            initial_capital = df_agg.iloc[0]
            net_profit = df_agg.iloc[-1] - initial_capital

            return_on_capital = net_profit / initial_capital
            annualized_return = (1 + return_on_capital) ** (365 / holding_period_day) - 1
            annualized_std = equity_value_pct_series.std() * math.sqrt(365)
            if annualized_std > 0:
                annualized_sr = annualized_return / annualized_std
            else:
                annualized_sr = 0

            performance_list = [return_on_capital, annualized_return, annualized_sr, mdd_pct]
            aggregate_performance = components.aggregate_performance(performance_list)

            # Generate Chart
            if aggregate_boolean:
                fig_line = px.line()
                fig_line.update_layout(title={'text': title_text })
                fig_line.update_xaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
                fig_line.update_yaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
                fig_line.update_layout(plot_bgcolor=self.chart_bg, paper_bgcolor=self.chart_bg, height=500,
                                       margin=dict(l=0, r=25, t=60, b=0),
                                       showlegend=True,
                                       font={"color": "white", 'size': 10.5}, yaxis={'title': ''},
                                       xaxis={'title': ''}
                                       )
                fig_line.add_trace(go.Scatter(mode='lines', # hovertemplate=hovertemplate,
                                              x=df_all_curves.index, y=df_all_curves['Aggregate_Equity'],
                                              line=dict(color=valid_colour, width=1.5), name='Aggregate'), )
            else:
                fig_line = px.line()
                fig_line.update_layout(title={'text': title_text})
                fig_line.update_xaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
                fig_line.update_yaxes(showline=True, zeroline=False, linecolor='white', gridcolor='rgba(0, 0, 0, 0)')
                fig_line.update_layout(plot_bgcolor=self.chart_bg, paper_bgcolor=self.chart_bg, height=500,
                                       margin=dict(l=0, r=25, t=60, b=0),
                                       showlegend=True,
                                       font={"color": "white", 'size': 10.5}, yaxis={'title': ''},
                                       xaxis={'title': ''},
                                       )
                # print(list(df_all_curves.columns))

                columns = list(df_all_curves.columns)[:-1]
                for curve_number, column in zip(curve_checklist,columns):
                    fig_line.add_trace(go.Scatter(mode='lines',  # hovertemplate=hovertemplate,
                                                  x=df_all_curves.index, y=df_all_curves[column],
                                                  line=dict(color=self.df_equity_curves.loc[curve_number].line_colour, width=1.5), name=f'Curve {str(curve_number).zfill(3)}'), )



            return fig_line, normalized_style, aggregate_style, aggregate_performance





        return app