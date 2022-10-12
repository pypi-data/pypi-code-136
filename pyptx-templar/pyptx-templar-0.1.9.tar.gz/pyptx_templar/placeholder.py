"""
Everything related to placeholders and text or image replacement.
"""

import logging
import re
import traceback

from PIL import Image

from .presmanager import delete_run

# Define the characters marking the opening of a placeholder.
CMD_P1_ = CMD_P2_ = '{'

# Define the characters marking the closing of a placeholder.
CMD_S1_ = CMD_S2_ = '}'

# Characters which are replaced before executing the code.
# By default, the only replaced characters are ‘ and ’ which are replaced by a straight single quote.
REPLACE_CHARS_ = {'‘': '\'', '’': '\''}


def cmd_p():
    """
    Returns the opening string of a placeholder.
    """
    return f"{CMD_P1_}{CMD_P2_}"


def cmd_s():
    """
    Returns the closing string of a placeholder.
    """
    return f"{CMD_S1_}{CMD_S2_}"


def cmd_pattern():
    """
    Returns the (compiled) pattern corresponding to a text placeholder.
    """
    return re.compile(f"{cmd_p()}(.*?){cmd_s()}")


def img_pattern():
    """
    Returns the (compiled) pattern corresponding to an image placeholder.
    """
    return f"{cmd_p()}img:(.*?):(.*?){cmd_s()}"


def interp(cmd, **kwargs):
    """
    Given python code extracted from a placeholder, interpret it with kwargs
    as environment, and return the value fetched from the code as a string.

    Characters in cmd are replaced if they appear in REPLACE_CHARS_, then
    the command is executed with
    ```py
    exec(f"_ret={cmd}", None, kwargs)
    ```
    and lastly the value of `_ret` is fetched and returned as a string.

    In case of error, an empty string is returned.

    Using exec is of course very unsafe, but we assume the users knows what
    he is executing, or else that he at least knows the risks.
    """

    if '_r' in kwargs and '_c' in kwargs:
        context = f"[Slide {kwargs['_idx']}, cell at row {kwargs['_r']} and col {kwargs['_c']}]"
    else:
        context = f"[Slide {kwargs['_idx']}]"

    logging.getLogger(__name__).debug("%s Interpreting command '%s'", context,
                                      cmd)
    for cfrom, cto in REPLACE_CHARS_.items():
        cmd = cmd.replace(cfrom, cto)
    try:
        exec(f"_ret={cmd}", None, kwargs)
    except:
        logging.getLogger(__name__).warning("%s Error executing:\n%s\n%s",
                                            context, cmd,
                                            traceback.format_exc())
        # raise again or just keep going ?
        # for now just keep going
        return ''
    return kwargs['_ret']


def run_replace(run, **kwargs):
    """
    Find and replace placeholders inside a run, with the given local environment.

    Placeholders are replaced in order.

    Placeholders are removed before executing the code.
    """

    cmd_pat = cmd_pattern()
    # do not use 'subn' since we want to remove the code before executing
    m = cmd_pat.search(run.text)
    while m is not None:
        # delete code, then interpret and insert where the code used to be
        # prevents issues when the piece of code duplicates the current slide
        run.text = run.text[:m.start()] + run.text[m.end():]
        val = str(interp(m.group(1), **kwargs))
        run.text = run.text[:m.start()] + val + run.text[m.start():]

        m = cmd_pat.search(run.text)


def cell_replace(cell, _cell=None, **kwargs):
    """
    Find and replace placeholders inside a cell,
    with the given local environment.

    Adds the cell to the environment, as `_cell`.
    """
    textframe_replace(cell.text_frame, **kwargs, _cell=cell)


def paragraph_replace(par, _p=None, **kwargs):
    """
    Find and replace placeholders inside a paragraph,
    with the given local environment.

    Adds the paragraph to the environment, as `_p`.

    The order in which placeholders are interpreted is first by considering
    runs independently, in text order, and then checking whether the paragraph
    has placeholders over run boundaries.

    Placeholders are fully removed before being interpreted, and the result of
    the execution is inserted in the first run.
    """

    for run in par.runs:
        run_replace(run, **kwargs, _p=par)

    idx = 0
    runs = list(par.runs)
    matches = list(cmd_pattern().finditer(par.text))
    for match in matches:
        idcs = -1  # char start
        while idcs == -1:
            rt = runs[idx].text
            if not rt:
                continue
            idcs = rt.find(cmd_p())

            if idcs == -1 and rt[-1] == CMD_P1_ and \
               runs[idx + 1].text[0] == CMD_P2_:
                idcs = len(rt) - 1

            idx += 1

        idrs = idx - 1  # run start

        idce = 1  # char end
        while idce == 1:
            rt = runs[idx].text
            if not rt:
                continue
            idce = rt.find(cmd_s()) + 2

            if idce == 1 and rt[-1] == CMD_S1_ and \
               runs[idx + 1].text[0] == CMD_S2_:
                idx += 2
                idce = 1
                break

            idx += 1

        idre = idx - 1  # run end

        runs[idrs].text = runs[idrs].text[:idcs]
        runs[idre].text = runs[idre].text[idce:]

        idx = idrs + 1

        for i in range(idrs + 1, idre):
            delete_run(runs[i])
        if not runs[idre].text:
            delete_run(runs[idre])

        # delete code, then interpret and insert where the code used to be
        # prevents issues when the piece of code duplicates the current slide
        val = interp(match.group(1), **kwargs, _p=par)
        runs[idrs].text += str(val)

        if not runs[idrs].text:
            delete_run(runs[idrs])
        runs = list(par.runs)


def textframe_replace(tf, _tf=None, **kwargs):
    """
    Find and replace placeholders inside a TextFrame,
    with the given local environment.

    Adds the TextFrame to the environment, as `_tf`.

    If the TextFrame contains an image placeholder, the container is removed
    and the image added at its position. Otherwise, paragraphs are interpreted
    in text order separately (textual placeholders are not searched across
    paragraph boundaries).
    """

    # match image
    m = re.search(img_pattern(), tf.text)

    if m is None:
        for par in tf.paragraphs:
            paragraph_replace(par, **kwargs, _tf=tf)
        return
        # don't replace across paragraphs

    # insert the image
    slide = tf.part.slide
    sh = tf._element.getparent()
    l, t, w, h = sh.x, sh.y, sh.cx, sh.cy

    modifs = set(m.group(1))
    file = interp(m.group(2), **kwargs, _tf=tf)
    slide.shapes.element.remove(sh)

    if not file:
        # ignore placeholders with undefined image
        return

    context = f"[Slide {kwargs['_idx']}] textframe_replace (image '{file}', modifiers={modifs})"

    try:
        with Image.open(file, mode='r') as im:
            width = im.width
            height = im.height
    except (FileNotFoundError, PermissionError, OSError):
        logging.getLogger(__name__).exception("%s: ", context)
        return

    hm = {'r', 'l', 'c'}
    vm = {'t', 'b', 'm'}
    allm = hm | vm

    if not modifs.issubset(allm):
        logging.getLogger(__name__).info("%s: unknown modifiers %s ignored",
                                         context, modifs - allm)

    if len(modifs.intersection(hm)) > 1:
        logging.getLogger(__name__).warning(
            "%s: several horizontal modifiers %s", context,
            modifs.intersection(hm))
        return
    if len(modifs.intersection(vm)) > 1:
        logging.getLogger(__name__).warning(
            "%s: several vertical modifiers %s", context,
            modifs.intersection(vm))
        return

    factor = min(w / width, h / height)
    if modifs.isdisjoint(hm):
        width = w
    else:
        # scaling horizontal
        width *= factor
    if modifs.isdisjoint(vm):
        height = h
    else:
        # scaling vertical
        height *= factor

    if 'r' in modifs:
        # aligned right
        l += w - width
    if 'c' in modifs:
        # centered (horizontal)
        l += (w - width) // 2
    if 'b' in modifs:
        # aligned bottom
        t += h - height
    if 'm' in modifs:
        # centered (vertically)
        t += (h - height) // 2

    slide.shapes.add_picture(file, l, t, width=width, height=height)


def row_replace(row, _c=None, **kwargs):
    """
    Find and replace placeholders inside a table row,
    with the given local environment.

    Adds the table column index to the environment, as `_c`.

    Cells are interpreted from left to right.
    """

    # I did not use enumerate to avoid issues if interpreting changes the number of rows
    # but not sure it's much better using range(len(...))
    for _c in range(len(row.cells)):
        cell_replace(row.cells[_c], **kwargs, _c=_c)


def table_replace(table, _r=None, _table=None, **kwargs):
    """
    Find and replace placeholders inside a table,
    with the given local environment.

    Adds the table and row index to the environment, as `_table` and `r`.

    Rows are interpreted from top to bottom.
    """

    # I did not use enumerate to avoid issues if interpreting changes the number of rows
    # but not sure it's much better using range(len(...))
    for _r in range(len(table.rows)):
        row_replace(table.rows[_r], **kwargs, _table=table, _r=_r)


def slide_replace(slide, _sl=None, **kwargs):
    """
    Find and replace placeholders inside a slide,
    with the given local environment.

    Adds the slide in the environment, as `_sl`.

    Shapes are interpreted from in the order defined in the slide, which
    can be seen and edited by clicking on the `Select` button in the `Home`
    tab and then `Selection Pane` (bottom-up).

    Only shape TextFrames and Tables are interpreted.
    """

    for sh in slide.shapes:
        if sh.has_text_frame:
            textframe_replace(sh.text_frame, **kwargs, _sl=slide)
        if sh.has_table:
            table_replace(sh.table, **kwargs, _sl=slide)


def pres_replace(pres, _idx=None, _pres=None, **kwargs):
    """
    Find and replace placeholders inside the presentation,
    with the given local environment.

    Adds the Presentation and slide index in the environment,
    as `_pres` and `_idx`.

    Slides are interpreted in ascending order.
    """

    idx = 0
    # len(pres.slides) can change during execution
    while idx < len(pres.slides):
        slide = pres.slides[idx]
        slide_replace(slide, **kwargs, _pres=pres, _idx=idx)
        idx += 1
