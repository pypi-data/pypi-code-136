from bokeh.plotting import figure
from bokeh.io import export_png
import os


def plot_model(data, x, y, analysis=False):
    p = figure(x_axis_label='Time (MJD)', y_axis_label='Elevation (Degrees)', plot_width=1200)
    p.line(x=x, y=data['np_model'].tolist(), color='red', line_width=5)
    p.scatter(x=x, y=y, color='blue', size=2)

    p.axis.major_label_text_font_size = "15pt"
    p.axis.axis_label_text_font_size = "20pt"
    p.axis.axis_label_text_font_style = "bold"

    filename = 'satellite' + data['sat'] + '_file' + data['filename']

    if analysis:
        filename = 'analysis_' + filename

    export_png(p, filename=os.path.join(data['save'], filename) + '.png')

    return data
