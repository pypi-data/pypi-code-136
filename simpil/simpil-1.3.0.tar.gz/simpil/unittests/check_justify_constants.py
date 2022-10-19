# encoding: utf-8

import os
from simpil import SimpilImage
from simpil import (RED,
                    GREEN,
                    BLUE,
                    WHITE,
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

    destination = f'images/{x}_{y}.jpg'

    simpil_image = SimpilImage(width=800,
                               height=400,
                               background_colour=RED,
                               destination=destination)

    simpil_image.text(text=f"justify x:{x}, y:{y}",
                      x=x,
                      y=y,
                      colour=BLUE,
                      font=font)
