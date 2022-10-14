"""
File contains the boilerplate for the single page rats visualiser app.

This page brings together the views and callback functions within the frame of the general page
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
from rats.core.RATS_CONFIG import PlotBanks
import dash_uploader as du


def create_rats_application(modules):
    layout = html.Div([
        dcc.Location(id='url', refresh=False),

        #############################################################################################
        # HEADER
        #############################################################################################
        html.Div([
            html.Div(className='logo', children=[html.Img(src='assets/graph-up.svg', className='logo-svg'),
                                                 html.Span('RATS'), ' DATA VISUALISER']),
            html.Div([], id='runstatus', className='text-center text-danger'),
        ],
            className='header-bar'),

        dbc.Accordion(id='accordion-upload',
                      children=[
                          dbc.AccordionItem(id='accordion-topo-item',
                                            children=[
                                                dcc.Upload(
                                                    id='upload-topo',
                                                    children=html.Div([
                                                        'Drag and Drop or Click to Select Relevant Topo Files'
                                                    ]),
                                                    multiple=True),

                                                html.P('Topo files and EDS files loaded:'),
                                                html.Div([html.Div([], id='toporeport', className='col')],
                                                         id='topodatacontainer',
                                                         className='container'),

                                                html.Button(['Clear Topo Data'],
                                                            id='cleartopo',
                                                            n_clicks=None,
                                                            className='btn btn-danger',
                                                            type='button'),

                                                html.Div([], id='clearedtopo')
                                            ],
                                            title="Upload Topology File and Data Sheets",
                                            ),

                          dbc.AccordionItem(id='accordion-upload-item',
                                            children=[
                                                du.Upload(max_files=10,
                                                          filetypes=['txt'],
                                                          text='Drag and drop files here or click to browse',
                                                          text_completed='Uploaded File(s) include: ',
                                                          max_file_size=2048
                                                          ),
                                                # ==================================================
                                                # the du.Upload max_files attribute is still experimental. This is a potential weak point in the app
                                                # but seems to work fine for now. It won't reliably work properly to call the processing function
                                                # if multiple files are uploaded, so a button is required to kick that process off.
                                                # ==================================================
                                                html.Button(id='rats_upload_button', className='btn rats-btn',
                                                            children='Process Available Data')
                                            ],
                                            title="Upload RATS Data",
                                            ),

                      ],
                      start_collapsed=True),

        #############################################################################################
        # BODY
        #############################################################################################
        html.Div(className='body-content', children=[

            dbc.Spinner([
            html.Div(children=[html.Div([],
                                        id='datalist',
                                        className='container')])]),

            html.Div([html.Div([],
                               id='errorlog',
                               className='col')],
                     id='errorlogcontainer',
                     className='container'),

            html.Div([
                dcc.Textarea(
                    id='notes',
                    style={'width': '100%'},
                    persistence=True,
                    persistence_type='local'
                ),
            ], className='container'),

            html.Br(),

            #############################################################################################
            # MODULES
            #############################################################################################
            dbc.Tabs(id='rattab', className='justify-content-center', persistence=True, persistence_type='local',
                     children=[

                         # ==========================================================================================
                         #    Apps go here
                         # ==========================================================================================
                         dcc.Tab(label=module_name.replace('_', ' '), value=module_name, children=[
                             html.Div(className='tab-padding', children=[
                                 # this code creates the application tabs using list comprehension
                                 module.createcontent(numberofbanks=PlotBanks[module_name].number_of_plot_banks,
                                                      designation=PlotBanks[module_name].designation)
                             ]),
                         ])

                         for module, module_name in modules]),
        ]),



        # ============================================================================
        #    OVERLAY DIV - display:flex fires from data management app to prompt a refresh of the page
        # ============================================================================
        html.Div(id='refresh-overlay',
                 className='refresh-overlay',
                 children=[html.A(children=['CLICK to Refresh the Page'],
                                  href='/', id='refresh-page-btn',
                                  className='btn rats-refresh-btn refresh-page',
                                  n_clicks=0)
                           ],
                 style={'display': 'None'}),
        html.Div(className='footer',children=[html.Div(className='logo',
                                                       children=[html.Span('WATERS')])
                                              ]),
        # html.Div(className='footer-overlay',
        #          children=[
        #              html.Div(className='logo', children=[html.Span('WATERS')])
        #          ]),
    ])
    return layout
