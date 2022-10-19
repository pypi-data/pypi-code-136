# encoding: utf-8

import logging
from past.builtins import basestring
import os
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

from PIL import Image
from PIL import ImageDraw
import requests

from .constants import *


def text_dimensions(font,
                    text):
    return font.getsize(text)


class SimpilImage(object):

    def __init__(self,
                 source=None,
                 destination=None,
                 width=None,
                 height=None,
                 background_colour=None,
                 autosave=True,
                 font=None):
        """
        There are four ways to initialise the image.

        1. From a URL - fetches the image at given URL
        2. From image data - data representing the image, such as data already
                             read from a file. The data should be supplied as
                             a StringIO object or a string
        3. From a filename - reads from the file if it exists
        4. From dimensions - creates an image with width and height,
                            of background colour

        :param source: 1) File to read
                       2) URL of an image to fetch
                       3) Image data as StringIO
                       4) Image data as string

        :param destination: File to save/autosave to
        :param width: Width in pixels of an image to create
        :param height: Height in pixels of an image we want to create
        :param background_colour: Fill colour of a created image
        :param autosave: Flag to indicate whether to autosave changes.
                         Default is True.
                         Note that for files, if the destination is not
                         supplied, changes will overwrite the original file
        :param font: A default font to use when adding text. If not supplied,
                     The DEFAULT_FONT from simpil_constants is used.
        """
        self.source = source
        self.destination = destination

        self.__autosave = autosave

        autosave_on_init = True

        if source is None:
            self.__new_image(width=width,
                             height=height,
                             background_colour=background_colour)

        elif self.source_is_file(source):
            self.image = Image.open(source)
            if destination is None:
                self.destination = source

            if self.destination == source:
                # Don't save over the top if there's no change
                autosave_on_init = False

        elif isinstance(source, BytesIO):
            # stream
            self.image = Image.open(source)

        else:
            try:
                data = requests.get(source).content
            except Exception as e:
                # raw data
                self.image = Image.open(BytesIO(source))
            else:
                # Image is from link
                self.image = Image.open(BytesIO(data))

        self.image_info = self.image.info
        # logging.info(self.image_info)
        self.draw = ImageDraw.Draw(self.image)
        self.default_font = (font
                             if font
                             else DEFAULT_FONT)

        if autosave_on_init:
            self.autosave()

    @staticmethod
    def source_is_file(source):
        try:
            return os.path.isfile(source)
        except TypeError:
            pass
        return False

    @property
    def width(self):
        return self.image.width

    @property
    def height(self):
        return self.image.height

    def __new_image(self,
                    width,
                    height,
                    background_colour
                    ):
        """
        Creates an image with the given dimensions and filled with the
        background colour
        """
        if not(width and height):
            raise ValueError(u'You must provide a height and a width '
                             u'when creating a new image')

        background_colour = (background_colour
                             if background_colour
                             else BLACK)

        self.image = Image.new(mode=RGB,
                               size=(width, height),
                               color=background_colour)

    def __justify(self,
                  font,
                  text,
                  x,
                  y,
                  left_border=0,
                  right_border=0,
                  top_border=0,
                  bottom_border=0,
                  justify=CENTRE):
        """

        :param font:
        :param text:
        :param x:
        :param y:
        :param left_border:
        :param right_border:
        :param top_border:
        :param bottom_border:
        :param justify:
        :return:
        """

        lines = text.splitlines() if isinstance(text, str) else text

        # To get a consistent distribution, use the height of
        # a string that includes a descender for all lines.
        line_height = font.getsize('My')[1]
        widths = [(font.getsize(line))[0] for line in lines]
        max_width = max(widths)
        if justify in CENTRE:
            width_adjustments = [(max_width - width) // 2 for width in widths]
        elif justify is RIGHT:
            width_adjustments = [(max_width - width) for width in widths]
        else:
            width_adjustments = [0 for _ in widths]

        w = max_width
        h = len(lines) * line_height

        w += left_border + right_border
        h += top_border + bottom_border

        if isinstance(x, basestring) or isinstance(y, basestring):

            if x in (CENTRE, CENTER):
                x = self.image.width // 2 - w // 2
            elif x == RIGHT:
                x = self.image.width - w
            elif x == LEFT:
                x = 0

            if y in (CENTRE, CENTER):
                y = self.image.height // 2 - h // 2
            elif y == TOP:
                y = 0
            elif y == BOTTOM:
                y = self.image.height - h

        xys = [(line, (x + width_adjustment,
                       y + line_height * i))
               for i, (line, width_adjustment) in enumerate(zip(lines, width_adjustments))]

        return xys

    def text(self,
             text,
             x,
             y,
             justify=CENTRE,
             font=None,
             colour=WHITE):

        """
        Draws text on the image

        :param text: Text string to draw.
                     This can be a list of strings (without newlines)
                     of a string with newlines
        :param x: horizontal position or LEFT, CENTRE, RIGHT
        :param y: vertical position or TOP, CENTRE, BOTTOM
        :param justify: How multi-line text is justified LEFT, CENTRE, RIGHT
        :param font: The find object to use
        :param colour: foreground text colour
        :return:
        """

        font = font if font else self.default_font

        justified_text_and_positions = self.__justify(font=font,
                                                      text=text,
                                                      x=x,
                                                      y=y,
                                                      justify=justify)
        for line, xy in justified_text_and_positions:
            self.draw.text(xy=xy,
                           text=line,
                           fill=colour,
                           font=font)
        self.autosave()

    def shadowed_text(self,
                      text,
                      x,
                      y,
                      justify=CENTRE,
                      font=None,
                      colour=WHITE,
                      shadow_colour=BLACK,
                      shadow_size=1):
        """
        Draws text with a bottom-right shadow. Useful for making text stand out
        again a background that is similar to the text colour

        :param text: Text string to draw
        :param x: horizontal position
        :param y: vertical position
        :param justify: How multi-line text is justified LEFT, CENTRE, RIGHT
        :param font: The find object to use
        :param colour: foreground text colour
        :param shadow_colour: Outline colour
        :param shadow_size: Size of the outline in pixels
        :return:
        """

        font = font if font else self.default_font

        justified_text_and_positions = self.__justify(font=font,
                                                      text=text,
                                                      x=x,
                                                      y=y,
                                                      justify=justify,
                                                      right_border=shadow_size,
                                                      bottom_border=shadow_size)

        for line, (x, y) in justified_text_and_positions:
            shadow_positions = [(xx, yy)
                                for xx in range(x, x + shadow_size + 1)
                                for yy in range(y, y + shadow_size + 1)
                                if not(xx == x and yy == y)]

            for shadow_position in shadow_positions:
                self.draw.text(xy=shadow_position,
                               text=line,
                               fill=shadow_colour,
                               font=font)

        for line, xy in justified_text_and_positions:
            self.draw.text(xy=xy,
                           text=line,
                           fill=colour,
                           font=font)
        self.autosave()

    def outlined_text(self,
                      text,
                      x,
                      y,
                      justify=CENTRE,
                      font=None,
                      colour=WHITE,
                      outline_colour=BLACK,
                      outline_size=1):
        """
        Draws text with an outline. Useful for making text stand out against
        a background that is similar to the text colour

        :param text: Text string to draw
        :param x: horizontal position
        :param y: vertical position
        :param justify: How multi-line text is justified LEFT, CENTRE, RIGHT
        :param font: The find object to use
        :param colour: foreground text colour
        :param outline_colour: Outline colour
        :param outline_size: Size of the outline in pixels
        :return:
        """
        font = font if font else self.default_font

        justified_text_and_positions = self.__justify(font=font,
                                                      text=text,
                                                      x=x,
                                                      y=y,
                                                      justify=justify,
                                                      left_border=outline_size,
                                                      right_border=outline_size,
                                                      top_border=outline_size,
                                                      bottom_border=outline_size)

        for line, (x, y) in justified_text_and_positions:

            outline_positions = [(xx, yy)
                                 for xx in range(x - outline_size,
                                                 x + outline_size + 1)
                                 for yy in range(y - outline_size,
                                                 y + outline_size + 1)
                                 if not(xx == x and yy == y)]

            for outline_position in outline_positions:
                self.draw.text(xy=outline_position,
                               text=line,
                               fill=outline_colour,
                               font=font)

        for line, xy in justified_text_and_positions:
            self.draw.text(xy=xy,
                           text=line,
                           fill=colour,
                           font=font)
        self.autosave()

    def scale(self,
              x,
              y=None):
        y = x if y is None else y
        self.image = self.image.resize((self.width * x,
                                        self.height * y),
                                       Image.ANTIALIAS)

    def save(self,
             filename=None):
        """
        Save the image to a file. Will use the filename provided.
        If the filename is not provided, will use a previously
        configured destination.  Supply of filename will not
        alter where autosave is done.

        :param filename:
        :return:
        """
        filename = filename if filename else self.destination
        if filename:
            self.image.save(filename, **self.image_info)
        else:
            logging.warning(u"Can't save: (No filename provided)")

    def autosave(self,
                 filename=None):
        """
        Called by self after operations that alter the image.
        Can also be called outside the object to enable autosave
        and to supply an auto save filename

        :param filename: Filename for autosave
        :return: None
        """
        if filename:
            self.destination = filename
            self.__autosave = True

        if self.__autosave and self.destination:
            self.save()

    def image_data(self,
                   fmt=None):
        """
        Returns the raw image data in the desired format.
        This can be used when there's no need to save the
        file to disk, such as for images dynamically created
        from webserver requests.

        :param fmt: Format of the image file
        :return: raw image data
        """
        fmt = fmt if fmt else self.image.format
        output = BytesIO()
        self.image.save(output,
                        format=fmt)
        image_data = output.getvalue()
        output.close()
        return image_data
