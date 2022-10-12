import os
import numpy as np
import tkinter as tk

ATOL = 1e-6

MAP_POS_TO_CURSOR_SYMBOL = {
    "bottom-right": "bottom_right_corner",
    "top-right": "top_right_corner",
    "top-left": "top_left_corner",
    "bottom-left": "bottom_left_corner",
    "left": "left_side",
    "right": "right_side",
    "top": "top_side",
    "bottom": "bottom_side",
}


def flatten_list(ls):
    new_list = []
    for ls_ in ls:
        new_list.extend(ls_)

    return new_list


def get_root(widget):
    parent = widget
    while True:
        if parent.master is None:
            return parent
        parent = parent.master


def disable_children(parent):
    for child in parent.winfo_children():
        try:
            child.configure("state")
        except tk.TclError:
            disable_children(child)
            continue

        wtype = child.winfo_class()

        if "Label" in wtype:
            continue

        elif "Entry" in wtype:
            state = "readonly"
        else:
            state = "disabled"

        child.configure(state=state)
        disable_children(child)


def get_bound_position(canvas, widget_id, x, y, tol=2):
    coords = canvas.bbox(widget_id)
    if coords is None:
        return None

    x1, y1, x2, y2 = coords

    left = _is_left(x1, x, tol)
    right = _is_right(x2, x, tol)
    top = _is_top(y1, y, tol)
    bottom = _is_bottom(y2, y, tol)

    if not left and not right and not top and not bottom:
        return None

    str_out = ""
    for pos, pos_str in zip(
        [bottom, top, right, left], ["bottom", "top", "right", "left"]
    ):
        if pos:
            str_out += f"-{pos_str}"

    return str_out[1:]


def _is_left(x1, x, tol):
    return x1 - tol <= x <= x1 + tol


def _is_right(x2, x, tol):
    return x2 - tol <= x <= x + tol


def _is_top(y1, y, tol):
    return y1 - tol <= y <= y1 + tol


def _is_bottom(y2, y, tol):
    return y2 - tol <= y <= y2 + tol


def get_image_path(filename):

    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", filename)

def clean_data_dict(data: dict) -> dict:
    """Return a dict, filtering None values"""
    return {key: value for key, value in data.items() if value is not None}


def which_segment_exact(line: list, coords: np.array):
    """Same as which segment but returns none if 
    point not exactly on line"""

    seg_idx, dist =  which_segment(line, coords)

    if seg_idx is None:
        return None
    if dist<ATOL:
        return seg_idx
    else: 
        return None


def which_segment(line: list, coords: np.array):
    """
    Says if loaction at COords in on line, and if so, which segment
    Points (list of np.array): the line points

    Returns NONE if coords not on segment
    Returns segment index if already on the line
        
    None situation is essential to moce sliders along the line
    """
    last_dist=1e10
    seg_out = None
         
    for seg_index, (pt1, pt2) in enumerate(zip(line, line[1::])): 
        dotp = abcissa_segment(pt1, pt2, coords)
        if dotp < 0. or dotp > 1.:
            #print("skipping" ,seg_index)
            continue
            
        proj = pt1+dotp*(pt2 - pt1)
        dist= np.linalg.norm(proj-coords)
        if dist<last_dist:
            seg_out=seg_index
            last_dist=dist
    
    return seg_out, last_dist
        
    #print("Out of any segment", coords, line)
    
def abcissa_segment(pt1:np.array, pt2:np.array, coords:np.array)-> float:
    """Return the curvilinear abcissa on a segment"""
    segment = (pt2 - pt1)
    tgt= segment/np.linalg.norm(segment)
    dotp = np.dot(coords-pt1, tgt)/np.linalg.norm(segment)
    return dotp