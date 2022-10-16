import plotly.express as px
import pandas as pd


def create_radar(x_labels, y_values):
    '''
    https://plotly.com/python/radar-chart/
    '''
    df = pd.DataFrame(dict(
        r = y_values,
        theta = x_labels))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.show()

if __name__=="__main__":
    create_radar(["a","b"], [1,2])
