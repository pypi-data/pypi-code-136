import random as _random
from math import floor as _floor
from PIL import Image as _Image

# Technique to use golden ratio is mentioned in
# https://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/
_GOLDEN_RATIO = 0.618033988749895
_HUE = _random.random()

def _hsv_to_rgb(hue, sat, val):
    """
    Algorithm: https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB
    Range of Hue is [0, 360]
    """
    chroma = sat*val
    _hue = hue/60
    X = chroma*(1 - abs(_hue % 2 - 1))
    mapping = {
        (0, 1): (chroma, X, 0),
        (1, 2): (X, chroma, 0),
        (2, 3): (0, chroma, X),
        (3, 4): (0, X, chroma),
        (4, 5): (X, 0, chroma),
        (5, 6): (chroma, 0, X)
    }
    key = (_floor(_hue), _floor(_hue)+1)
    m = val - chroma
    return (int((color+m)*255) for color in mapping[key])

def color(sat=0.5, val=0.95):
    """
    Returns an RGB color

    Keyword arguments:
    Saturation -- range [0, 1]
    Value -- range [0, 1]
    """    
    global _HUE
    _HUE = (_HUE+_GOLDEN_RATIO)%1
    if 0 <= sat <= 1 and 0 <= val <= 1:
        return _hsv_to_rgb(HUE*360, sat, val)
    else:
        raise ValueError("sat/val should be in range [0, 1]")

def visualize(num_colors=10):
    """
    Runs color() 'num_colors' times and plots the RGB colors
    Logic: https://holypython.com/python-visualization-tutorial/colors-with-python/
    """
    width_px=1000
    new = _Image.new(mode="RGB", size=(width_px, 120))
    for i in range(num_colors):
        palette=tuple(color())
        newt = _Image.new(mode="RGB", size=(width_px//num_colors, 100), color=palette)
        new.paste(newt, (i*width_px//num_colors, 10))
    new.show()
