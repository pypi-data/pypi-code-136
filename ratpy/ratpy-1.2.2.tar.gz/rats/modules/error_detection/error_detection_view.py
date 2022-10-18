from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def createcontent(numberofbanks: int, designation: str = 'dashboard_app_'):
    children = []

    for i in range(numberofbanks):
        card = html.Div([
                html.Div([
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.RadioItems(id=f'{designation}fileselect{i}',
                                                   options=[],
                                                   value=[]
                                                   ),
                                ],
                                id=f'{designation}fileselect-accordion{i}',
                                title="Select Data",
                            ),
                            dbc.AccordionItem(
                                [
                                    dbc.Input(id=f"{designation}numberofscans{i}", type="number", value=1, max=50,
                                              persistence=True,
                                              persistence_type='session')
                                ],
                                title="LLC Buffer",
                            ),
                            dbc.AccordionItem(
                                [
                                    dbc.RadioItems(id=f"{designation}resolution{i}",
                                                   options=[{'label': 'Low', 'value': 'low'},
                                                            {'label': 'High', 'value': 'high'}],
                                                   value=['low']),
                                    html.P('Note that performance might be impacted in high resolution mode if you plot more than 1 million LLCs'),
                                    dbc.Label('Lower LLC bound for error plot'),
                                    dbc.Input(id=f"{designation}low_llc_bound{i}", type="number", value=1,
                                              persistence=True,
                                              persistence_type='session'),
                                    dbc.Label('Higher LLC bound for error plot'),
                                    dbc.Input(id=f"{designation}high_llc_bound{i}", type="number", value=1000000,
                                              persistence=True,
                                              persistence_type='session')
                                ],
                                title="Advanced Options",
                            )
                        ],
                        className='fileselect-accordion',
                        start_collapsed=True),

                    html.Br(),
                    html.Button(id=f'{designation}replot{i}', n_clicks=0, children='Update Plots', className='btn rats-btn',
                                type='button'),
                    html.Br(),
                    html.P([], id=f'{designation}interscanprompt{i}', className='text-danger')
                ], className='card-header rats-card-header'),

                html.Div([
                    html.Div([
                        html.Div(id=f'{designation}error_detection{i}', children=[
                            dcc.Loading([
                                dcc.Graph(id=f'{designation}error_detection_plot{i}', figure={
                                    'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                                                        modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))
                                })
                            ]),
                            html.Button(id=f'{designation}download-error_detection-btn{i}', children=[html.Img(src='/assets/download.svg', alt='Download Plot')],
                                        className='btn rats-btn-outline', type='button', n_clicks=0),
                            dcc.Download(id=f'{designation}download_error_detection_plot{i}')
                        ], className='col-6 text-center'),

                        html.Div(id=f'{designation}scope{i}', children=[
                            dcc.Loading([
                                dcc.Graph(id=f'{designation}scopeplot{i}', figure={
                                    'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                                                        modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))
                                })
                            ]),
                            html.Button(id=f'{designation}download-scope-btn{i}', children=[html.Img(src='/assets/download.svg', alt='Download Plot')],
                                        className='btn rats-btn-outline', type='button', n_clicks=0),
                            dcc.Download(id=f'{designation}download_scope{i}')
                        ], className='col-6 text-center'),

                    ], className='row')
                ], className='card-body')

            ], className='card rats-card rats-single-card', style={'height': 'auto'})

        children.append(card)

    layout = html.Div([
        ########################################
        # dynamic plot content ('children') goes below
        ########################################
        html.Div(id='plots', children=children,
                 className='container-fluid text-center'),
        ########################################
    ], className='container-fluid')

    return layout








