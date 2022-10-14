from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

def createcontent(numberofbanks: int, designation:str = 'interscan_app_'):
    cards = []
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
                    ],
                    className='fileselect-accordion',
                    start_collapsed=True),

                # html.P(['Select the file you want to interrogate in this bank of plots:']),
                # dcc.Dropdown(id=f'{designation}fileselect{i}',
                #              options=[], persistence=True),

                html.Button(id=f'{designation}replot{i}', n_clicks=0, children='Update Plot',
                            className='btn rats-btn',
                            type='button'),
            ], className='card-header rats-card-header'),

            html.Div([
                dcc.Graph(id=f'{designation}plot{i}', figure={'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',modebar=dict(bgcolor='rgba(0,0,0,0)', color='grey', activecolor='lightgrey'))}),
                html.Button(id=f'{designation}download-btn{i}', children=[html.Img(src='/assets/download.svg', alt='Download Plot')],
                            className='btn rats-btn-outline', type='button', n_clicks=0),
                dcc.Download(id=f'{designation}download{i}'),
                dcc.Graph(id=f'{designation}histo_plot{i}', figure={'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                                                                  plot_bgcolor='rgba(0,0,0,0)',
                                                                                  modebar=dict(bgcolor='rgba(0,0,0,0)',
                                                                                               color='grey',
                                                                                               activecolor='lightgrey'))}),
                html.Button(id=f'{designation}download-histo-btn{i}',
                            children=[html.Img(src='/assets/download.svg', alt='Download Plot')],
                            className='btn rats-btn-outline', type='button', n_clicks=0),
                dcc.Download(id=f'{designation}download_histo{i}'),

                dcc.Graph(id=f'{designation}interscan_plot{i}', figure={'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                                                                        plot_bgcolor='rgba(0,0,0,0)',
                                                                                        modebar=dict(
                                                                                            bgcolor='rgba(0,0,0,0)',
                                                                                            color='grey',
                                                                                            activecolor='lightgrey'))}),
                html.Button(id=f'{designation}download-interscan-btn{i}',
                            children=[html.Img(src='/assets/download.svg', alt='Download Plot')],
                            className='btn rats-btn-outline', type='button', n_clicks=0),
                dcc.Download(id=f'{designation}download_interscan{i}'),

            ],
                className='card-body rats-card-body', id=f'{designation}plotcontainer{i}'),

        ], className='card rats-card', draggable=True)

        cards.append(card)

    group = html.Div(children=cards, className='card-group rats-card-group')

    layout = html.Div([
        html.Div(id=f'{designation}-plots', children=group,
                 className='container-fluid text-center'),
        ########################################
    ], className='container-fluid')

    return layout
