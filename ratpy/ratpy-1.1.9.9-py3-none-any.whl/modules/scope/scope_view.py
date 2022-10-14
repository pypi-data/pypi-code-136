from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def createcontent(numberofbanks: int, designation:str = 'scope_app_'):
    cards = []
    for i in range(numberofbanks):
        card = html.Div([

            html.Div([
                html.Div(
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
                                    dbc.Checklist(id=f'{designation}edbselect{i}',
                                                  options=[],
                                                  value=[], switch=True
                                                  ),
                                    html.P('All are shown if none are specified')
                                ],
                                title="Select EDBs",
                            )
                        ],
                    className='fileselect-accordion',
                    start_collapsed=True)
                ),

                html.Button(id=f'{designation}replot{i}', n_clicks=0, children='Update Plot', className='btn rats-btn',
                            type='button'),
            ], className='card-header rats-card-header'),

            html.Div([
                dcc.Loading([
                    dcc.Graph(id=f'{designation}plot{i}', className=f'{designation}plot',figure={'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))}),
                ]),
                html.Button(id=f'{designation}download-btn{i}', children=[html.Img(src='/assets/download.svg', alt='Download Plot')],
                            className='btn rats-btn-outline', type='button', n_clicks=0),
                dcc.Download(id=f'{designation}download{i}')
                ],
                className='card-body rats-card-body', id=f'{designation}plotcontainer{i}'),

        ], className='card rats-card', draggable='true')

        cards.append(card)

    group = html.Div(children=cards, className='card-group rats-card-group')

    layout = html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        dbc.Label(['LLC count on which to centre plots:']),
                        dbc.Input(id=f"{designation}llc", type="number", value=1, persistence=True),
                    ], className='col-6 text-center'),

                    html.Div([
                        dbc.Label(['Number of LLC intervals to buffer \u00B1 the trace:']),
                        dbc.Input(id=f"{designation}buffer", type="number", value=1, persistence=True),
                    ], className='col-6 text-center'),

                ], className='row rats-llc-row'),

                html.Div(
                    html.Button("Centre plots on designated LLC \u00B1 buffer", id=f'{designation}centre_data',
                                className='btn rats-btn'),
                    className='row p-4'
                ),
            ], className='container-fluid rats-llc-container')
        ],className='container-fluid'),

        html.Div(id=f'{designation}plots', children=group,
                 className='container-fluid text-center'),
        ########################################
    ], className='container-fluid')

    return layout



