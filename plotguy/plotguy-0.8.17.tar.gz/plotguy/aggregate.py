from dash import Dash, dcc, html, Input, Output, State, ALL
import dash_daq as daq
from .components import *

class Aggregate:

    chart_bg = '#1f2c56'
    valid_colour = 'DeepSkyBlue'
    df_equity_curves = pd.DataFrame()

    def __new__(self):

        chart_bg = self.chart_bg
        components = Components()
        valid_colour = self.valid_colour

        empty_line_chart = components.empty_line_chart()

        self.df_equity_curves, checklist_div = components.aggregate_df()

        # print(self.df_equity_curves)
        #
        # print(checklist_div)

        app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO], suppress_callback_exceptions=True)

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
                                 style={'maxHeight': '700px', #471
                                        'overflow-y': 'scroll',
                                        'overflow-x': 'hidden',
                                        }),

                        html.Div(style={'height': '5px', }),

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


                        html.Div(style={'height': '10px', }),

                        html.Div(id='chart_area',
                                 children=dcc.Graph(id='line_chart',
                                                    figure=empty_line_chart)),

                    ]), style={'padding': '5px 25px', 'border-radius': '5px',
                               'background-color': chart_bg}),

                ]), style={'padding': '0', 'padding-left': '5px'}, width=8),

            ]),
        ], style={'width': '1400px', 'margin': 'auto', 'padding': '0px', 'color': 'white'})

        @app.callback(
            Output('line_chart', 'figure'),
            Output('normalized_string', 'style'),
            Output('aggregate_string', 'style'),
            Input('curve_checklist', 'value'),
            Input('normalized_boolean','on'),
            Input('aggregate_boolean', 'on')
        )
        def aggregate_chart(curve_checklist,normalized_boolean, aggregate_boolean):

            curve_checklist.sort()

            valid_colour = self.valid_colour

            # print(curve_checklist)
            #
            # print(normalized_boolean)

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



            return fig_line, normalized_style, aggregate_style





        return app