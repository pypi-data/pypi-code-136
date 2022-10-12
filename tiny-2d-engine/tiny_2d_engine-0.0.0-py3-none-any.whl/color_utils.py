custom_colors = {
    "grey": (187,187,187),
    
    "green_olive": (153,153,51),
    "green": (17,119,51),
    "green_teal": (68,170,153),
    "green_pear": (187,204,51),
    
    "yellow_light": (238,221,136),
    "yellow_sand": (221,204,119),
    
    "blue_indigo": (51,34,136),
    "blue": (0,119,187),
    "blue_cyan_light": (153,221,155),
    
    "orange": (238,119,51),
    "red": (204,51,17),
    "magenta": (238,51,119),
    
    "dark":(46, 47, 48),
    "light":(221, 221, 221),
    
}


def tk_color(color_name: str, brighter=None):
    """ """
    if color_name in custom_colors:
        out = custom_colors[color_name]
    else:
        out = custom_colors["grey"]

    if brighter is not None:
        out = brighten_color(out, brighter=brighter)
    return rgb_to_hex(out)


def rgb_to_hex(tuple_: tuple):
    """translates an rgb tuple of int to a tkinter friendly color code"""
    rgb = (int(channel) for channel in tuple_)
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def brighten_color(tuple_rgb, brighter=0.7):
    """

    To brighten the color, use a float valuecloser to 1

    """

    if brighter < 0:
        return tuple_rgb

    out = (
        (tuple_rgb[0] * (1 - brighter) + 255 * brighter),
        (tuple_rgb[1] * (1 - brighter) + 255 * brighter),
        (tuple_rgb[2] * (1 - brighter) + 255 * brighter),
    )

    return out
