"""
Contains functions to copy styles and content from equivalent elements:
- TextFrame
- Paragraph
- Run
- Font
- Fill
- Color
"""

import logging
import sys

from pptx.oxml.text import CT_RegularTextRun, CT_TextCharacterProperties
from pptx.oxml.text import CT_TextLineBreak, CT_TextParagraphProperties

from pptx.enum.dml import MSO_COLOR_TYPE, MSO_FILL


def color_copy(cfrom, cto):
    if cfrom.type is not None:
        if cfrom.type == MSO_COLOR_TYPE.RGB:
            cto.rgb = cfrom.rgb
        elif cfrom.type == MSO_COLOR_TYPE.SCHEME:
            cto.theme_color = cfrom.theme_color
        else:
            logging.getLogger(__name__).warning(
                "font_copy: unknown color type '%s'", cfrom.type)
        cto.brightness = cfrom.brightness


def fill_copy(ffrom, fto):
    if ffrom.type is None:
        return

    if ffrom.type == MSO_FILL.BACKGROUND:
        fto.background()
    elif ffrom.type == MSO_FILL.GRADIENT:
        fto.gradient()
        fto.gradient_angle = ffrom.gradient_angle
        fto.gradient_stops = ffrom.gradient_stops
    elif ffrom.type == MSO_FILL.PATTERNED:
        fto.patterned()
        fto.pattern = ffrom.pattern
        color_copy(ffrom.back_color, fto.back_color)
    elif ffrom.type == MSO_FILL.PICTURE:
        fto.picture()
    elif ffrom.type == MSO_FILL.SOLID:
        fto.solid()
    elif ffrom.type == MSO_FILL.TEXTURED:
        fto.textured()
    else:
        logging.getLogger(__name__).warning(
            "font_copy: unknown fill type '%s'", ffrom.type)
    color_copy(ffrom.fore_color, fto.fore_color)


def font_copy(ffrom, fto):
    fto.bold = ffrom.bold
    fto.italic = ffrom.italic
    fto.language_id = ffrom.language_id
    fto.name = ffrom.name
    fto.size = ffrom.size
    fto.underline = ffrom.underline
    fill_copy(ffrom.fill, fto.fill)

    # beware that accessing the color field updates the fill type to SOLID
    # so only do it if ffrom.type is already SOLID
    if ffrom.fill.type == MSO_FILL.SOLID:
        color_copy(ffrom.color, fto.color)


def run_copy(rfrom, rto):
    font_copy(rfrom.font, rto.font)
    rto.text = rfrom.text


def paragraph_copy(pfrom, pto):
    pto.clear()

    run_idx = 0
    # iterate directly on the xml elements since it's the
    # only way to get line breaks
    for e in pfrom._element:
        if isinstance(e, CT_RegularTextRun):
            # some text (a run)
            run = pto.add_run()
            run_copy(pfrom.runs[run_idx], run)
            run_idx += 1
        elif isinstance(e, CT_TextLineBreak):
            # a line break
            pto.add_line_break()
        elif not isinstance(
                e, (CT_TextParagraphProperties, CT_TextCharacterProperties)):
            # CT_TextParagraphProperties is at the beginning of each paragraph and
            # contains paragraph style information, copied by paragraph_copy
            # CT_TextCharacterProperties is at the beginning of runs which have a different style from the paragraph,
            # and contains information about this style, copied by run_copy
            logging.getLogger(__name__).warning(
                "paragraph_copy: element non prévu de type '%s'", type(e))

    # we have to copy after creating the runs or the style is not completely kept
    # (add line_break breaks the level ?)
    font_copy(pfrom.font, pto.font)
    pto.alignment = pfrom.alignment
    pto.line_spacing = pfrom.line_spacing
    pto.space_after = pfrom.space_after
    pto.space_before = pfrom.space_before
    pto.level = pfrom.level


def textframe_copy(tffrom, tfto):
    tfto.clear()

    while len(tfto.paragraphs) != len(tffrom.paragraphs):
        pt = tfto.add_paragraph()

    for pf, pt in zip(tffrom.paragraphs, tfto.paragraphs):
        paragraph_copy(pf, pt)

    tfto.margin_bottom = tffrom.margin_bottom
    tfto.margin_left = tffrom.margin_left
    tfto.margin_right = tffrom.margin_right
    tfto.margin_top = tffrom.margin_top
    tfto.vertical_anchor = tffrom.vertical_anchor
    tfto.word_wrap = tffrom.word_wrap
