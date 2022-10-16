import factory_component
from dash import Dash, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
        html.Pre(
            id='div-position'
        ),
        factory_component.TextEditor(id='text-editor'),
        # factory_component.Rnd(
        #     default={
        #         'x':0,
        #         'y':0,
        #         'width':200,
        #         'height':200,
        #     },
        #     resizeGrid=[50,50],
        #     dragGrid=[50,50],
        #     style={
        #         'background':'red',
        #     },
        #     id='teste'
        # )
    ],
    style={
        'height':'300px',
    }
    )

@app.callback(
    Output('div-position','children'),
    Input('text-editor','value'),
)
def update_position(value):
    return value

# @app.callback(
#     Output('div-size','children'),
#     Input('teste','size'),
# )
# def update_position(size):
#     print(size)
#     return str(size)

if __name__ == '__main__':
    app.run_server(debug=True)
