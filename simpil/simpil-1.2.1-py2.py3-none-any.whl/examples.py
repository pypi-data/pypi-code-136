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
                    TOP)

from PIL import ImageFont


import requests

try:
   CONSOLAS_36 = ImageFont.truetype(u"C:\Windows\Fonts\consola.ttf", 36)
   font = CONSOLAS_36
except:
   font = DEFAULT_FONT


PYTHON_IMAGE_URL = u"https://s-media-cache-ak0.pinimg.com/736x/13/e5/c3/13e5c3587e3010552923f30310fe1563.jpg"
PYTHON_IMAGE_FROM_URL_FILENAME = u'images/python.jpg'
PYTHON_IMAGE_FROM_DATA_FILENAME = u'images/python_from_data.jpg'
RED_RECT = u'images/red_rect.jpg'
ORANGE_AND_UKE = u'images/orange_and_uke.jpg'
ORANGE_AND_UKE_MANIPULATED = u'images/orange_and_uke_manipulated.jpg'


# Reads and image from a file and does not save a new file
modified_date = os.path.getmtime(ORANGE_AND_UKE)
orange_and_uke = SimpilImage(source=ORANGE_AND_UKE)
assert modified_date == os.path.getmtime(ORANGE_AND_UKE)

# Reads and image from a file and saves a copy to a new file
orange_and_uke = SimpilImage(source=ORANGE_AND_UKE,
                             destination=ORANGE_AND_UKE_MANIPULATED)

# Pulls image from a requests url
python_from_url = SimpilImage(source=PYTHON_IMAGE_URL,
                              destination=PYTHON_IMAGE_FROM_URL_FILENAME)

# Pulls image from a requests url, passes data
python_from_data = SimpilImage(source=requests.get(PYTHON_IMAGE_URL).content,
                               destination=PYTHON_IMAGE_FROM_DATA_FILENAME)



# Creates a new image (No source supplied)
red_rect = SimpilImage(width=100,
                       height=25,
                       background_colour=RED,
                       destination=RED_RECT)

# Above image is created and saved.
# This wipes any previous RED_RECT file
#
red_rect = SimpilImage(source=RED_RECT)

red_rect.scale(2)
assert red_rect.width == 200
assert red_rect.height == 50

red_rect.scale(2, 4)
assert red_rect.width == 400
assert red_rect.height == 200

# Adds text to the images. Autosave will be enabled. The files are saved
# Each time one of the functions is called.

for image in (python_from_data,
              python_from_url,
              orange_and_uke,
              red_rect):

    image.shadowed_text(text=u'Shadow',
                        x=LEFT,
                        y=CENTRE,
                        colour=GREEN,
                        shadow_size=3)

    image.outlined_text(text=u"Outline",
                        x=CENTRE,
                        y=TOP,
                        colour=RED,
                        outline_colour=WHITE,
                        outline_size=3,
                        font=font)

    image.text(text=u"Text",
               x=RIGHT,
               y=CENTRE,
               colour=BLUE)
