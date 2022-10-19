# encoding: utf-8

import os
from simpil import SimpilImage
from simpil import (RED,
                    GREEN,
                    BLUE,
                    WHITE,
                    YELLOW,
                    DEFAULT_FONT,
                    CENTRE,
                    LEFT,
                    RIGHT,
                    TOP,
                    BOTTOM)

from PIL import ImageFont

try:
   CONSOLAS_36 = ImageFont.truetype(u"C:\Windows\Fonts\consola.ttf", 36)
   font = CONSOLAS_36
except:
   font = DEFAULT_FONT

for justify in (LEFT, CENTRE, RIGHT):
    for y, x in ((TOP, LEFT),
                 (TOP, CENTRE),
                 (TOP, RIGHT),
                 (CENTRE, LEFT),
                 (CENTRE, CENTRE),
                 (CENTRE, RIGHT),
                 (BOTTOM, LEFT),
                 (BOTTOM, CENTRE),
                 (BOTTOM, RIGHT),
                 ):

        destination = f'images/multiline_{justify}_{x}_{y}.jpg'

        simpil_image = SimpilImage(width=800,
                                   height=400,
                                   background_colour=RED,
                                   destination=destination)

        simpil_image.text(text=f"Multiline\nText\nJustify:{justify}\nX:{x} Y:{y}",
                          justify=justify,
                          x=x,
                          y=y,
                          colour=BLUE,
                          font=font)

        destination = f'images/multiline_shadow_{justify}_{x}_{y}.jpg'

        simpil_image = SimpilImage(width=800,
                                   height=400,
                                   background_colour=RED,
                                   destination=destination)

        simpil_image.shadowed_text(
            text=f"Multiline\nShadowed Text\nJustify:{justify}\nX:{x} Y:{y}",
            justify=justify,
            x=x,
            y=y,
            colour=BLUE,
            shadow_colour=YELLOW,
            shadow_size=2,
            font=font)

        destination = f'images/multiline_outline_{justify}_{x}_{y}.jpg'

        simpil_image = SimpilImage(width=800,
                                   height=400,
                                   background_colour=RED,
                                   destination=destination)

        simpil_image.outlined_text(
            text=f"Multiline\nOutlined Text\nJustify:{justify}\nX:{x} Y:{y}",
            justify=justify,
            x=x,
            y=y,
            colour=BLUE,
            outline_colour=WHITE,
            font=font,
            outline_size=2)
