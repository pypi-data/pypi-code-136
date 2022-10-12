"""Main declaration of viewer2d widget


Way too complex,
 need to add doctstrings and remove many mathods"""

from __future__ import annotations 

import json
import tkinter as tk

from tiny_2d_engine.popups import (
    ObjectAddPopupMenu,
)
from tiny_2d_engine.color_utils import tk_color

from tiny_2d_engine.base_canvas_object import (
    Line,
    Point,
    Slider,
    _CalibrationRectangle,
    _CanvasImage
)

ATOL = 1e-6


class AcquisitionCanvas(tk.Canvas):
    type = "GeometricCanvas"

    def __init__(self, holder, width=800, height=800, **canvas_kwargs):
        super().__init__(holder, width=width, height=height, background=tk_color("dark"), **canvas_kwargs)
        self.objects = {}

        self.popup_menu = ObjectAddPopupMenu(self)

        self.calibration_rectangle = None
        self.image = None
        self._width = width
        self._height = height
        self.whereami = tk.StringVar(self, value="None") # Variable to store current coordinates
        self.bind("<Configure>", self._update_size)
        self.bind("<Motion>", self._motion_callback)
        
    def _motion_callback(self, event=None):
        """Callback to print current position via self.whereami Tk.Variable"""
        x, y = event.x, event.y
        def _fmt(value):
            return "{:.2f}".format(value)
        try:
            x_r, y_r = self.calibration_rectangle.map2real((x,y))
        except AttributeError:
            x_r, y_r = 0,0
        self.whereami.set(f"pix : {x},{y}\n m  :{_fmt(x_r)},{_fmt(y_r)}")
        

    @property
    def calibrated(self):
        return self.calibration_rectangle is not None

    @property
    def _border_width(self):
        return 2 * (int(self["bd"]) + int(self["highlightthickness"]))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.config(width=value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.config(height=value)

    def _update_size(self, event):
        self._width = int(event.width) - self._border_width
        self._height = int(event.height) - self._border_width

    def has_image(self):
        return self.image is not None

    def map2real(self, coords):
        return self.calibration_rectangle.map2real(coords)

    def map2canvas(self, coords):
        return self.calibration_rectangle.map2canvas(coords)

    def get_by_type(self, obj_type):
        return [obj for obj in self.objects.values() if obj.type == obj_type]

    def get_by_name(self, name):
        for obj in self.objects.values():
            if obj.name == name:
                return obj

        return None

    def get_names(self, obj_type=None):
        if obj_type:
            objects = self.get_by_type(obj_type)
        else:
            objects = self.objects.values()

        return [obj.name for obj in objects]

    def add_object_by_type(self, objects_info:dict, obj_type:str):
        """Necessity for Loader"""
        for object_info in objects_info:
            if object_info.get("type") != obj_type:
                continue
            #TYPE2OBJ = {"Point": Point, "Line": Line, "Slider": Slider}

            object_info = self.transform_obj_dict(object_info)
            
            if obj_type == "Point":
                obj = Point(**object_info)
            elif obj_type == "Line":
                obj = Line(**object_info)
            elif obj_type == "Slider":
                obj = Slider(**object_info)
            else:
                raise NotImplementedError
            
            #obj = TYPE2OBJ[obj_type](**object_info)
            self.add_object(obj)

    def transform_obj_dict(self, obj_info:dict):
        """Clean object definitions
        
        Type and show are not necessary
        For sliders, corrections are needed"""
        obj_type = obj_info.get("type")
        del obj_info["type"]

        show = obj_info.get("show", None)
        if show is not None:
            show = True
            del obj_info["show"]

        if obj_type == "Slider":
            obj_info=self.transform_slider_dict(obj_info)

        return obj_info
    
    def transform_slider_dict(self, obj_info:dict):
        """For a slider the information must be changed a bit, 
        because it is dependent from its anchor
        
        Coords are not needed
        anchor name is replaced by its object"""
        del obj_info["coords"]

        anchor_name = obj_info.get("anchor")
        obj_info["anchor"] = self.get_by_name(anchor_name)
        return obj_info


    

    def delete_object(self, id):
        obj = self.objects[id]
        obj.destroy()
        del self.objects[id]

    def show_all(self):
        for obj in self.objects.values():
            obj.show()

    def hide_all(self):
        for obj in self.objects.values():
            obj.hide()

    def calibrate(
        self,
        canvas_coords,
        coords,
        keep_real=False,
        color="black",
        allow_translate=True,
        allow_edit=True,
        show=True,
    ):
        self.calibration_rectangle = _CalibrationRectangle(
            canvas_coords,
            coords,
            keep_real=keep_real,
            color=color,
            allow_translate=allow_translate,
            allow_edit=allow_edit,
        )

        self.calibration_rectangle.create_widget(self)

        if not show:
            self.calibration_rectangle.hide()

    def add_image(
        self,
        path,
        show=True,
        allow_translate=True,
        allow_edit=True,
        allow_delete=True,
    ):
        self.image = _CanvasImage(
            path=path,
            allow_translate=allow_translate,
            allow_edit=allow_edit,
            allow_delete=allow_delete,
        )

        self.image.create_widget(self)
        self.tag_lower(self.image.id)  # move image back

        if not show:
            self.image.hide()

    def delete_image(self):
        if self.image is not None:
            self.image.destroy()
            self.image = None

    def is_hidden(self, obj_id):
        return self.itemcget(obj_id, "state") == "hidden"

    def as_dict(self):
        output_dict = {}

        output_dict["metadata"] = {"width": self.width, "height": self.height}

        if not self.calibrated:
            return output_dict

        output_dict["calibration"] = self.calibration_rectangle.as_dict()

        if self.image:
            output_dict["image"] = self.image.as_dict()

        output_dict["objects"] = [obj.as_dict() for obj in self.objects.values()]

        return output_dict


    def load_dict(self, data: dict):
        """Load a memory into the widget"""
        metadata = data.get("metadata", {})
        width = metadata.get("width", 800)
        height = metadata.get("height", 600)

        self.width = width
        self.height = height

        # calibrate
        calibration_info = data.get("calibration", None)
        if calibration_info is not None:
            self.calibrate(**calibration_info)
        else:
            return self

        # add image
        image_info = data.get("image", None)
        if image_info is not None:
            self.add_image(**image_info)

        # add objects
        objects_info = data.get("objects", None)
        if objects_info is not None:
            for obj_type in ["Line", "Slider", "Point"]:  # because order matters
                #_add_objects_by_type(canvas, objects_info, obj_type)
                self.add_object_by_type(objects_info, obj_type)


    def dump(self, filename):
        with open(filename, "w") as file:
            json.dump(self.as_dict(), file, indent=2)

    def clear(self):
        for obj_id in reversed(list(self.objects.keys())):
            self.delete_object(obj_id)

        self.delete_image()

        if self.calibration_rectangle is not None:
            self.calibration_rectangle.destroy()
            self.calibration_rectangle = None
    
    
    def add_object(self, obj, show=True):
        if not self.calibrated:
            raise Exception("Cannot add objects before calibration")

        if obj.name == "" or obj.name in self.get_names():
            raise Exception("Name already exists")

        item_id = obj.create_widget(self)

        self.objects[item_id] = obj

        if not show:
            obj.hide()
    
    def add_line(self, data):

        if "coords" not in data:
            (x1, x2), (y1, y2) = _get_canvas_coords_lims(self)
            x = x1 + abs(x2 - x1) * 0.5
            y = y1 + (y2 - y1) * 0.1
            data["coords"] =[x, y]
        self.add_object(Line(**data))

    def add_point(self, data):
        if "coords" not in data:
            (x1, x2), (y1, y2) = _get_canvas_coords_lims(self)
            data["coords"] = [[x1, y1], [x2, y2]]
        self.add_object(Point(**data))

    def add_slider(self, data):
        if "v_init" not in data:
            data["v_init"]=0.2
        if "v_end" not in data:
            data["v_end"]=0.4
        if "n_points" not in data:
            data["n_points"]=6
        self.add_object(Slider(**data))


def _get_canvas_coords_lims(canvas):
    pt_top_left, pt_bottom_right = canvas.calibration_rectangle._get_corners()
    x1, y1 = pt_top_left.coords
    x2, y2 = pt_bottom_right.coords

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    return (x1, x2), (y1, y2)
