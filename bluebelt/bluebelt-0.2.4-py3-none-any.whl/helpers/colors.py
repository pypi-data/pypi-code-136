import pandas as pd
import math
from matplotlib.colors import to_rgb, to_hex, is_color_like

def _get_colors_from_style(style_dict):
    result = []
    for value in style_dict.values():
        if isinstance(value, dict):
            result += _get_colors_from_style(value)
        elif is_color_like(value):
            return [value]
    return list(set(result))

def _closest_colors(match_colors, to_colors):
    
    if len(to_colors) < len(match_colors):
        raise ValueError(f"not enough to_colors to match all input {len(to_colors)} < ")
        
    if not isinstance(match_colors, list):
        match_colors = [match_colors]
    
    frame = pd.DataFrame([to_rgb(c) for c in to_colors])
    result = {}
        
    def close(row, color):
        r, g, b = to_rgb(color)
        return math.sqrt((r - row.iloc[0])**2 + (g - row.iloc[1])**2 + (b - row.iloc[2])**2)
    
    to_colors = pd.DataFrame(to_colors)
    
    for c in match_colors:
                
        # get closest color and drop from frame
        idx = frame.apply(lambda x: close(x, c), axis=1).idxmin()
        closest = to_hex(tuple(frame.iloc[idx].values))
        frame = frame.drop(index = idx).reset_index(drop=True)

        # add to result if the color is not the same
        if c != closest:
            result[c] = closest
        
    return result

def _replace_colors(style, colors_dict):
    replaced = {}
    for key, value in style.items():
        if isinstance(value, dict):
            replaced[key] = _replace_colors(value, colors_dict)
        elif isinstance(value, list):
            replaced[key] = [colors_dict.get(val, val) if is_color_like(val) else val for val in value]
        elif is_color_like(value):
            # replace the color if it is in the colors_dict
            replaced[key] = colors_dict.get(value, value)
        else:
            replaced[key] = value
    return replaced

def replace_colors(style, to_colors):
    match_colors = style.get('colors', _get_colors_from_style(style))
    colors_dict = _closest_colors(match_colors, to_colors)
    return _replace_colors(style, colors_dict)
