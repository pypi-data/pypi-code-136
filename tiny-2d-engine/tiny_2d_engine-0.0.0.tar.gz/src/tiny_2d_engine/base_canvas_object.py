"""Module defining the base canvas object used for T2DE"""
from __future__ import annotations
import numpy as np
import tkinter as tk
from abc import ABCMeta

import numpy as np
from PIL import ImageTk
from PIL import Image

from tiny_2d_engine.popups import (
    ObjectPopupMenu,
    LinePopupMenu,
    SliderPopupMenu,
    ImagePopupMenu,
)

from tiny_2d_engine.utils import (
    clean_data_dict,
    flatten_list,
    MAP_POS_TO_CURSOR_SYMBOL,
    clean_data_dict, 
    which_segment,
    which_segment_exact,
    abcissa_segment
)


from tiny_2d_engine.color_utils import tk_color
from tiny_2d_engine.utils import clean_data_dict
from tiny_2d_engine.constants import DEFAULT_PROPERTIES



class _BaseCanvasObject(metaclass=ABCMeta):
    """Base class for all canvas objects.
    
    Avoid redefinitions of these methods pleeeeease!"""
    def __init__(self, 
            name: str, 
            text: str, 
            color: str, # one of declared colors in color_utils 
            allow_translate: bool, 
            allow_delete: bool, 
            allow_edit: bool
        ):
        self.name = name
        self.text = text
        self._allow_translate = allow_translate and allow_edit
        self._allow_delete = allow_delete
        self._allow_edit = allow_edit
        self._color = color

        self._id = None

    def create_widget(self, canvas: tk.Canvas):
        """What happen at the widget creation
                
        Essentially  this should also create  self.id !!!
        """
        self._set_canvas(canvas)


    @property
    def id(self)-> int:
        """Object Id in the canvas"""
        return self._id

    @id.setter
    def id(self, value: int):
        """When an object is added to the canvas, the id is stored in self _id
        AND """
        if self._id is not None:
            raise Exception("A widget can be set only once")

        self._id = value
        self._on_widget_creation()


    def _on_widget_creation(self):
        """Canvas preparation when a widget is created"""
        self._config_bindings()
        self._create_popup_menu()

    def _set_canvas(self, canvas: tk.Canvas):
        """ADN why to we set this attribute via a method"""
        self.canvas = canvas

    ###################
    # ADN : too bad this method is never the same
    @property
    def canvas_coords(self)->np.array:
        """Return the cordinates of the object in canvas coords (pix)"""
        return np.array(self.canvas.coords(self.id))

    @canvas_coords.setter
    def canvas_coords(self, pix_coords: list):
        """Chanf the cordinates of the object in canvas coords (pix)"""
        self.canvas.coords(self.id, *pix_coords)
    ###################
    

    @property
    def color(self)->str:
        """Return the color of the widget """
        return self._color

    @color.setter
    def color(self, value: str):
        """Change the color of the widget as soon a .color is used"""
        self._color = value
        self.canvas.itemconfigure(self.id, fill=tk_color(value))
        self.canvas.itemconfigure(self.id, activefill=tk_color(value))
        try:
            self.canvas.itemconfigure(self.id, outline=tk_color(value))
        except tk.TclError:
            pass
        

    @property
    def allow_translate(self)-> bool:
        """Evaluates if translation is allowed"""
        return self._allow_translate and self._allow_edit

    @allow_translate.setter
    def allow_translate(self, value):
        """Depending on value change, tranlation binding is on or off"""
        self._allow_translate = value
        if value:
            self.bind_translate()
        else:
            self.unbind_translate()

    @property
    def allow_delete(self):
        """Evaluates if deletion is allowed"""
        return self._allow_delete

    @allow_delete.setter
    def allow_delete(self, value):
        """Depending on value change, deletion binding is on or off"""
        self._allow_delete = value
        if value:
            self.bind_delete()
        else:
            self.unbind_delete()

    @property
    def allow_edit(self):
        """Evaluates if edition is allowed"""
        return self._allow_edit

    @allow_edit.setter
    def allow_edit(self, value):
        """Depending on value change, edition binding is on or off"""
        self._allow_edit = value
        if value:
            self.bind_edit()
        else:
            self.unbind_edit()


    def bind_translate(self):
        """ Activate Binding for translation"""
        self.canvas.tag_bind(self.id, "<Button-1>", self.on_config_delta_mov)
        self.canvas.tag_bind(self.id, "<B1-Motion>", self.on_translate)

    def unbind_translate(self):
        """Stop Binding for translation"""
        self.canvas.tag_unbind(self.id, "<Button-1>")
        self.canvas.tag_unbind(self.id, "<B1-Motion>")

    def bind_delete(self):
        """ Activate Binding for deletion"""
        self.popup_menu.bind_delete()

    def unbind_delete(self):
        """ DeActivate Binding for deletion"""
        
        self.popup_menu.unbind_delete()

    def bind_edit(self):
        """ Activate Binding for edition"""
        self.popup_menu.bind_edit()

    def unbind_edit(self):
        """ DeActivate Binding for edition"""
        self.unbind_translate()
        self.popup_menu.unbind_edit()

    def _config_bindings(self):
        """Add the bindings """
        if self.allow_translate:
            self.bind_translate()
        self.canvas.tag_bind(self.id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.id, "<Leave>", self.on_leave)
        
    def hide(self):
        """Hiding method"""
        self.canvas.itemconfigure(self.id, state="hidden")

    def show(self):
        """Showding method"""
        self.canvas.itemconfigure(self.id, state="normal")

    def destroy(self):
        """What to destroy when we remove an object"""
        self._destroy_popup_menu()
        self.canvas.delete(self.id)



    def as_dict(self)-> dict:
        """Return the meomry of the object as dict"""
        data = {
            "type": self.type,
            "name": self.name,
            "text": self.text,
            "color": self.color,
            "allow_translate": self.allow_translate,
            "allow_delete": self.allow_delete,
            "allow_edit": self.allow_edit,
        }

        return clean_data_dict(data)

    def update(
        self,
        name:str=None,
        text:str=None,
        color:str=None,
        allow_translate:bool=None,
        allow_delete:bool= None,
        allow_edit:bool=None,
    ):
        """Update the memory of the object
        
        note that all these '=' actually changes the aspect of the object
        due to the properties/setter
        """
        if name is not None:
            self.name = name

        if color is not None:
            self.color = color

        if text is not None:
            self.text = text

        if allow_translate is not None:
            self.allow_translate = allow_translate

        if allow_delete is not None:
            self.allow_delete = allow_delete

        if allow_edit is not None:
            self.allow_edit = allow_edit

    # Callbacks
    def on_translate(self, event):
        """Callback for translation of any object
        
        Action is done -via- the setter method of canvas_coords """
        
        self.canvas_coords = self._click_coords + self._get_delta_mov(event)

    def on_config_delta_mov(self, event):
        """Callback for start of motion in translation"""
        self._click_mouse_coords = event.x, event.y
        self._click_coords = self.canvas_coords

    def _get_delta_mov(self, event):
        """Callback for motion in translation"""
        return np.array(
            (
                event.x - self._click_mouse_coords[0],
                event.y - self._click_mouse_coords[1],
            )
        )

    def on_enter(self, event):
        """Callback when mouse enter over the widget .id"""
        self.canvas.popup_menu.unbind_menu_trigger()
        self.canvas.popup_menu.bind_menu_trigger()
        
        info = self.name
        if self.text is not None:
            info += "\n"+self.text
        
        for i in [-1, 1]:
            for j in [-1, 1]:
                self.canvas.create_text(
                    event.x+10+ i,
                    event.y-10 +j,
                    text=info,
                    anchor="sw",
                    fill=tk_color(DEFAULT_PROPERTIES["background"]),
                    tags="balloon_help"
                )
        self.canvas.create_text(
            event.x+10,
            event.y-10,
            text=info,
            anchor="sw",
            fill=tk_color(DEFAULT_PROPERTIES["foreground"]),
            tags="balloon_help",
        )
        self.balloon = "balloon_help"

    
    def on_leave(self, event):
        """Callback when mouse quit over the widget .id"""
        self.canvas.popup_menu.unbind_menu_trigger()
        self.canvas.delete(self.balloon)

    # ADN Do we really need all this stuff????
    def _create_popup_menu(self):
        """What kind of popup menu we should use"""
        self.popup_menu = ObjectPopupMenu(self) # Why is it already set

    def _destroy_popup_menu(self):
        """As name states. But do we really need this"""
        self.popup_menu.destroy()
        
    def on_config_cursor_translate(self, *args):
        """Updates of cursor"""
        self.canvas.config(cursor="fleur")

    def on_reset_cursor(self, *args):
        """Updates of cursor"""
        self.canvas.config(cursor="")


class _CompositeBaseObject(_BaseCanvasObject, metaclass=ABCMeta):
    """Not a clue for now on why we have this composite one here"""
    def __init__(
        self, name, text, color, allow_translate, allow_delete, allow_edit,
    ):
        super().__init__(name, text, color, allow_translate, allow_delete, allow_edit)
        
    @property
    def real_coords(self):
        return np.array([point.real_coords for point in self.points])

    @real_coords.setter
    def real_coords(self, values):
        for point, new_coords in zip(self.points, values):
            point.real_coords = new_coords


    @property
    def canvas_coords(self):
        return np.array([point.canvas_coords for point in self.points])

    @canvas_coords.setter
    def canvas_coords(self, values):
        for point, new_coords in zip(self.points, values):
            point.canvas_coords = new_coords

    @_BaseCanvasObject.color.setter
    def color(self, value):
        super(_CompositeBaseObject, type(self)).color.fset(self, value)

        for point in self.points:
            point.color = self.color

    def show(self):
        super().show()
        for point in self.points:
            point.show()

    def hide(self):
        super().hide()
        for point in self.points:
            point.hide()

    @_BaseCanvasObject.allow_edit.setter
    def allow_edit(self, value):
        super(_CompositeBaseObject, type(self)).allow_edit.fset(self, value)

        for point in self.points:
            point.allow_edit = value

    def destroy(self):
        super().destroy()
        for point in self.points:
            point.destroy()

    def _create_points(self, canvas):
        for point in self.points:
            point.create_widget(canvas)

    def update(
        self,
        name=None,
        coords=None,
        color=None,
        text=None,
        allow_translate=None,
        allow_delete=None,
        allow_edit=None,
    ):
        super().update(
            name=name,
            text=text,
            color=color,
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )

        if coords is not None:
            self.real_coords = coords
        

    def as_dict(self):
        data = super().as_dict()
        data.update(
            {
                "coords": [coords.tolist() for coords in self.real_coords],
            }
        )
        return clean_data_dict(data)
    
    
class _CalibrationRectangle(_CompositeBaseObject):
    """This widget is the calibration dialog to get world coordinates mapping"""
    type = "CalibrationRectangle"

    def __init__(
        self,
        canvas_coords,
        coords,
        color="black",
        keep_real=False,
        allow_translate=True,
        allow_edit=True,
    ):
        super().__init__(
            None,
            None,
            color,
            allow_translate=allow_translate,
            allow_delete=False,
            allow_edit=allow_edit,
        )
        self._pt1 = _MasterCalibrationPoint(
            self,
            canvas_coords[0],
            coords[0],
            name="Calib. point 1",
            color=DEFAULT_PROPERTIES["color_calib_pt1"],
            allow_translate=allow_edit,
        )
        self._pt2 = _MasterCalibrationPoint(
            self,
            canvas_coords[1],
            coords[1],
            name="Calib. point 2",
            color=DEFAULT_PROPERTIES["color_calib_pt2"],
            allow_translate=allow_edit,
        )
        self.keep_real = keep_real
        self._min_dist = 2

    @property
    def points(self):
        return [self._pt1, self._pt2]

    def create_widget(self, canvas:AcquisitionCanvas):
        self.canvas = canvas
        # create rectangle
        pt_top_left, pt_bottom_right = self._get_corners()
       
        #.id is critical, the whole object is anchored to this canvas item
        self.id = self.canvas.create_rectangle(
            *pt_top_left.canvas_coords,
            *pt_bottom_right.canvas_coords,
            outline=tk_color(DEFAULT_PROPERTIES["color_calib_rect"]),
            width=1,
            dash=(10,10),
            activewidth=2,
        )
       
        # create points
        self._create_points(canvas)

    def _get_corners(self):
        # alternative is to modify mapping functions
        pt1_position = self._pt1.position
        pt2_position = self._pt2.position

        if pt1_position == "top_left" and pt2_position == "bottom_right":
            return self._pt1, self._pt2
        elif pt1_position == "bottom_right" and pt2_position == "top_left":
            return self._pt2, self._pt1
        elif (
            (pt1_position == "bottom_left" and pt2_position == "top_right")
            or pt1_position == "top_right"
            and pt2_position == "bottom_left"
        ):
            if pt1_position == "bottom_left" and pt2_position == "top_right":
                pt_bottom_left, pt_top_right = self._pt1, self._pt2
            else:
                pt_bottom_left, pt_top_right = self._pt2, self._pt1

            # pt top left
            canvas_coords = (
                pt_bottom_left.canvas_coords[0],
                pt_top_right.canvas_coords[1],
            )
            coords = (pt_bottom_left.coords[0], pt_top_right.coords[1])
            pt_top_left = _CalibrationPoint(canvas_coords, coords)

            # pt bottom right
            canvas_coords = (
                pt_top_right.canvas_coords[0],
                pt_bottom_left.canvas_coords[1],
            )
            coords = (pt_top_right.coords[0], pt_bottom_left.coords[1])
            pt_bottom_right = _CalibrationPoint(canvas_coords, coords)

            return pt_top_left, pt_bottom_right

    def map2real(self, coords):
        pt_top_left, pt_bottom_right = self._get_corners()

        canvas_diff, real_diff = pt_bottom_right - pt_top_left
        u = (coords - pt_top_left.canvas_coords) / canvas_diff

        return real_diff * u * np.array([1, 1]) + pt_top_left.coords

    def map2canvas(self, coords):
        pt_top_left, pt_bottom_right = self._get_corners()

        canvas_diff, real_diff = pt_bottom_right - pt_top_left
        u = (coords - pt_top_left.coords) / real_diff

        return canvas_diff * u + pt_top_left.canvas_coords

    def update_coords(self):
        # when master points are updated
        pt_top_left, pt_bottom_right = self._get_corners()

        self.canvas.coords(
            self.id, *pt_top_left.canvas_coords, *pt_bottom_right.canvas_coords
        )

    
    # def bind_translate(self):
    #     super().bind_translate()
    #     self.canvas.tag_bind(
    #         self.id, "<Button-1>", self.on_config_cursor_translate, add="+"
    #     )
    #     print("Bin translate")
    #     self.canvas.tag_bind(self.id, "<ButtonRelease-1>", self.on_reset_cursor)

    # def unbind_translate(self):
    #     super().unbind_translate()
    #     self.canvas.tag_unbind(self.id, "<ButtonRelease-1>")

    def update(
        self,
        name=None,
        coords=None,
        canvas_coords=None,
        color=None,
        keep_real=None,
        allow_translate=None,
        allow_delete=None,
        allow_edit=None,
    ):

        if keep_real is not None:
            self.keep_real = keep_real

        super().update(
            name=name,
            coords=coords,
            color=color,
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )

        if canvas_coords is not None:
            self.canvas_coords = np.array(canvas_coords)

    def as_dict(self):
        data = super().as_dict()
        del data["allow_delete"]
        del data["type"]

        data.update(
            {
                "canvas_coords": [
                    point.canvas_coords.tolist() for point in self.points
                ],
                "keep_real": self.keep_real,
            }
        )

        return clean_data_dict(data)


class _CanvasImage(_BaseCanvasObject):
    """Widget to add an image under the drawing zone"""
    type = "CanvasImage"

    def __init__(
        self,
        path: str,
        allow_translate=True,
        allow_delete=True,
        allow_edit=True,
    ):
        super().__init__(
            None,
            None,
            None,
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )
        self._init_path = path 
        self._image = None
        
    @property
    def path(self)-> str:
        """The actual path of the source"""
        return self._image.filename

    @path.setter
    def path(self, filename: str):
        """Change the image source"""
        if self.path == filename:
            return
        self._image = Image.open(filename)
        self.canvas.itemconfig(self.id, image=self._image)

    def create_widget(self, canvas):
        """On creation of the widget
        
        Essentially create self.id !!!"""
        super().create_widget(canvas)

        self._image = Image.open(self._init_path)
        self._photo_image = ImageTk.PhotoImage(self._image)
        self.id = self.canvas.create_image(
            (0,0), image=self._photo_image, anchor="nw"
        )

    def _create_popup_menu(self):
        """The specific popup menu of the image"""
        self.popup_menu = ImagePopupMenu(self)

    def update(
        self,
        allow_translate:bool=None, # we do not want it to be tranlated a any cost
        allow_delete:bool=None,
        allow_edit: bool=None,
        path: str=None,  # This is actually the only specific thing to update
    ):
        """Updtate object from memory"""
        super().update(
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )

        if path is not None:
            self.path = path
     
    def as_dict(self)->dict:
        """Memory repr of image
        
        add path,
        remove type,"""
        data = super().as_dict()
        del data["type"]  # Why do we remove type btw?
        data.update({"path": self.path})

        return clean_data_dict(data)
    
    # Do WE REALLY NEED THIS? 
    def _config_cursor_bound(self, position):
        """Not realy sure why we change the cursor here"""
        symbol = MAP_POS_TO_CURSOR_SYMBOL.get(position)
        self.canvas.config(cursor=symbol)


class Point(_BaseCanvasObject):
    """Defines a single point"""
    type = "Point"

    def __init__(
        self,
        name: str,
        coords: list,
        color: str="red",
        text: list="",
        allow_translate: bool=True,
        allow_delete: bool=True,
        allow_edit: bool=True,
        size: float=1,
        shape: str="circle", # enum would be nice
        shade: float=None #TOKILL
    ):
        super().__init__(name, text, color, allow_translate, allow_delete, allow_edit)
        self._init_coords = coords
        self._init_shape = shape
        self.symsize = size*DEFAULT_PROPERTIES["symbol_size"]

    def __sub__(self, other:Point):
        """Substraction of two Points"""
        return self.canvas_coords - other.canvas_coords

    # Geometrical properties of Point
    # note that it is not actually stored in the item
    # but always found or set into self.canvas( self.id )
    @property
    def real_coords(self)->np.array:
        """Return the coords of Point in Meters"""
        return np.array(self.canvas.map2real(self.canvas_coords))
    
    @real_coords.setter
    def real_coords(self, r_coords:list):
        """Set the coords of Point in Meters
        
        This properties setter makes the Point 'jump' to the new location
        self.real_coords =   becomes a canvas action!"""
        self.canvas_coords = self.canvas.map2canvas(np.array(r_coords))
      
    @property 
    def canvas_coords(self)->np.array:
        """Return the coords of Point id in Pixels, as stored by the canvas"""
        x1, y1, x2, y2, *_ = self.canvas.coords(self.id)
        return np.array([int(0.5*(x1+x2)), int(0.5*(y1+y2))]) 

    @canvas_coords.setter
    def canvas_coords(self, pix_coords: list):
        """Set the coords of Point in Pixels
        
        This properties setter makes the Point 'jump' to the new location
        self.canvas_coords =   becomes a canvas action!"""
        
        # readjsut coordinates of canvas
        self.canvas.coords(
            self.id, 
            get_symbol_bbox(pix_coords, size=self.symsize)
        )

    def _get_init_coords(self):
        """Magic metho to get the initial coordinates
        
        Still not sure how it is working because it cannot be unrolled"""
        return self.canvas.map2canvas(self._init_coords)
    
    def create_widget(self, canvas:AcquisitionCanvas):
        """Initial creation of widget.
        
        Only for creation, its not redrawn afterwards,
        only coordinates are moved around 
        through :
            canvas_coords=
            real_coords=
            """
        super().create_widget(canvas)
       
        color = tk_color(self.color)
        symb_bbox = get_symbol_bbox(
            self._get_init_coords(), 
            size=self.symsize),
               
        if self._init_shape == "square":
            self.id = self.canvas.create_rectangle(
                *symb_bbox,
                activewidth=DEFAULT_PROPERTIES["activewidth"],
                fill=color,
                outline=color,
            )
        elif self._init_shape == "circle":
            self.id = self.canvas.create_oval(
                *symb_bbox,
                activewidth=DEFAULT_PROPERTIES["activewidth"],
                fill=color,
                outline=color,
            )
        else: # None -> Invisible item on canvas
            self.id = self.canvas.create_oval(
                *symb_bbox,
                fill="",
                outline=""
            )

        return self.id

    def update(
        self,
        name: str=None,
        coords: list=None,
        color: str=None,
        text: str=None,
        allow_translate: bool=None,
        allow_delete: bool=None,
        allow_edit: bool=None,
    ):
        """.update like a dict the info of a point
        
        Can change point position is coords provided"""
        
        super().update(
            name,
            text,
            color,
            allow_translate,
            allow_delete,
            allow_edit
        )

        # this is where the position of the point is updated in the canvas
        # the = iqs triggering the canvas update.
        if coords is not None:
            self.real_coords = coords

    def as_dict(self):
        """Return all properties as a dict"""
        data = super().as_dict()
        data.update({"coords": list(self.real_coords)})

        return clean_data_dict(data)


class _DependentPoint(Point, metaclass=ABCMeta):
    def __init__(
        self,
        master,
        name: str,
        coords,
        color="red",
        allow_translate=True,
        shape="circle",
        shade=0,
    ):
        super().__init__(
            name,
            coords,
            color=color,
            text=None,
            allow_translate=allow_translate,
            shape=shape,
            shade=shade,
        )
        self.master = master

    @property
    def popup_menu(self):
        return self.master.popup_menu

    def _create_popup_menu(self):
        # uses line menu
        self.popup_menu.add_trigger(self)

    def _destroy_popup_menu(self):
        pass


class _CalibrationPoint:
    def __init__(self, canvas_coords, coords):
        self._canvas_coords = np.array(canvas_coords)
        self._coords = np.array(coords)

    def __sub__(self, other):
        canvas_diff = self.canvas_coords - other.canvas_coords
        real_diff = self.coords - other.coords

        return canvas_diff, real_diff

    @property
    def canvas_coords(self):
        return self._canvas_coords

    @property
    def coords(self):
        return self._coords


class _MasterCalibrationPoint(_DependentPoint, _CalibrationPoint):
    # TODO: use 2 lines instead of a point?

    def __init__(
        self,
        calibration_rectangle: _CalibrationRectangle,
        canvas_coords,
        coords,
        name,
        color="green",
        allow_translate=True,
    ):
        _DependentPoint.__init__(
            self,
            calibration_rectangle,
            name,
            None,
            color=color,
            allow_translate=allow_translate,
        )
        _CalibrationPoint.__init__(self, canvas_coords, coords)

    def __sub__(self, other):
        return _CalibrationPoint.__sub__(self, other)

    @property
    def real_coords(self):
        """REDEFINITION of real_coords 'get'
        
        Because real coords are not accessed
        the same in callibration points
        """
        return self._coords

    @real_coords.setter
    def real_coords(self, center_coords):
        """REDEFINITION of real_coords 'set'
        
        Because real coords are notupdated
        the same in callibration points
        """
        # collect previous coords
        if self.master.keep_real:
            previous_coords = self._collect_previous_obj_coords()

        # update calibration
        self._coords = np.array(center_coords)

        # update coords
        if self.master.keep_real:
            self._update_obj_coords(previous_coords)

    @property
    def canvas_coords(self):
        """REDEFINITION of real_coords 'get'
        
        Because canvas coords are not accessed  
        the same in calibration points
        """
        return self._canvas_coords

    @canvas_coords.setter
    def canvas_coords(self, center_coords):
        """REDEFINITION of real_coords 'set'
        
        Because canvas coords are not accessed
        the same in calibration points
        """
        pt1, pt2 = self.master.points
        other = pt2 if self is pt1 else pt1
        diff = np.abs(center_coords - other.canvas_coords)
        if np.any(diff < self.master._min_dist):
            return

        # collect previous coords
        if self.master.keep_real:
            previous_coords = self._collect_previous_obj_coords()

        # update calibration
        self._canvas_coords = np.array(center_coords)
        Point.canvas_coords.__set__(self, center_coords)
        self.master.update_coords()

        # update coords
        if self.master.keep_real:
            self._update_obj_coords(previous_coords)

    def _get_init_coords(self):
        return self._canvas_coords

    def _collect_previous_obj_coords(self):
        coords = []
        for obj in self.canvas.objects.values():  # assumes dict is ordered
            coords.append(obj.real_coords)
        return coords

    def _update_obj_coords(self, coords):
        for obj, coords in zip(self.canvas.objects.values(), coords):
            obj.update(coords=coords)

    @property
    def position(self):
        pt1, pt2 = self.master.points
        other = pt2 if self is pt1 else pt1

        if self.canvas_coords[0] < other.canvas_coords[0]:
            if self.canvas_coords[1] < other.canvas_coords[1]:
                return "top_left"
            else:
                return "bottom_left"

        else:
            if self.canvas_coords[1] < other.canvas_coords[1]:
                return "top_right"
            else:
                return "bottom_right"


class _LinePoint(_DependentPoint):
    ###A point depending from a Line
    def __init__(
        self,
        line,
        coords: list,
        color: str="red",
        allow_translate: bool=True,
        shape: str="circle",
        shade: float=0,
    ):
        super().__init__(
            line,
            None,
            coords,
            color=color,
            allow_translate=allow_translate,
            shape=shape,
            shade=shade,
        )

    # OMG redefine something trivial initially
    @property
    def canvas(self):
        return self.master.canvas

    def _set_canvas(self, *args):
        pass

    @Point.canvas_coords.setter
    def canvas_coords(self, center_coords):
        #super(_LinePoint, type(self)).canvas_coords.fset(self, center_coords)
        Point.canvas_coords.fset(self, center_coords)
        self.master.update_coords()


class _MasterSliderPoint(_LinePoint):
    def __init__(
        self,
        slider,
        v,
        color="blue",
        allow_translate=True,
        shape="circle",
    ):
        super().__init__(
            slider,
            None,
            color=color,
            allow_translate=allow_translate,
            shape=shape,
        )
        self.v = v

    def _get_init_coords(self):
        return self.master.anchor.get_coords_by_v(self.v)

    @_LinePoint.canvas_coords.setter
    def canvas_coords(self, center_coords):
        center_coords_ = self.master.anchor.find_closest_point(center_coords)
        self.v = self.master.anchor.get_v(center_coords_)
        
        _LinePoint.canvas_coords.fset(self, center_coords_)

        #super(_MasterSliderPoint, type(self)).canvas_coords.fset(self, center_coords_)

    def update_coords(self):
        # when line changes, to keep v
        self.canvas_coords = self.master.anchor.get_coords_by_v(self.v)


class _SlaveSliderPoint(_LinePoint):
    def __init__(self, slider, t, color="blue", ):
        super().__init__(slider, None, color=color, shape=None, allow_translate=False)
        self._t = t

    def _get_init_coords(self):
        return self.master.anchor.get_coords_by_v(self.v)

    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value
        self.canvas_coords = self.canvas_coords  # beautiful
        self.master.update_coords()

    @property
    def v(self):
        return self.master.master_pts[0].v + self.t * (
            self.master.master_pts[1].v - self.master.master_pts[0].v
        )

    @property
    def canvas_coords(self):
        return self.master.anchor.get_coords_by_v(self.v)

    @canvas_coords.setter
    def canvas_coords(self, center_coords):
        if not np.allclose(center_coords, self.canvas_coords):
            raise Exception("Invalid center coords.")

        super(_LinePoint, type(self)).canvas_coords.fset(self, center_coords)


class _AbstractLine(_CompositeBaseObject, metaclass=ABCMeta):
    def __init__(
        self,
        name,
        points,
        color="red",
        text="",
        allow_translate=True,
        allow_delete=True,
        allow_edit=True,
    ):
        super().__init__(
            name,
            text,
            color,
            allow_translate,
            allow_delete,
            allow_edit=allow_edit,
        )
        self.points = points
        self.sliders = []

    @_CompositeBaseObject.allow_translate.setter
    def allow_translate(self, value):
        super(_AbstractLine, type(self)).allow_translate.fset(self, value)

        for slider in self.sliders:
            slider.allow_translate = value

    @_CompositeBaseObject.allow_edit.setter
    def allow_edit(self, value):
        super(_AbstractLine, type(self)).allow_edit.fset(self, value)
        for slider in self.sliders:
            if slider.allow_translate:
                slider.allow_translate = value

    def create_widget(self, canvas):
        self.canvas = canvas

        # create line
        coords = [point._get_init_coords() for point in self.points]
        self.id = self.canvas.create_line(
            flatten_list(coords),
            fill=tk_color(self.color),
            width=DEFAULT_PROPERTIES["linewidth"],
            activewidth=DEFAULT_PROPERTIES["activewidth"],
        )

        # create points (order matters for bindings)
        self._create_points(canvas)

        return self.id

    def show(self):
        super().show()
        for slider in self.sliders:
            slider.show(from_anchor=True)

    def hide(self):
        super().hide()
        for slider in self.sliders:
            slider.hide(from_anchor=True)

    def destroy(self):
        super().destroy()
        for slider in self.sliders.copy():
            slider.destroy()

    def find_closest_point(self, coords):
        # check first if already in line
        if which_segment_exact(self.canvas_coords, coords) is not None:
            return coords

        line_coords = self.canvas_coords

        pt = np.array(coords)
        dist = np.linalg.norm(line_coords - pt, axis=1)

        closest_idx = np.argmin(dist)
        n_pts = line_coords.shape[0]

        closest_pt = line_coords[closest_idx, :]

        pt_left = line_coords[closest_idx - 1, :] if closest_idx > 0 else np.nan
        pt_right = (
            line_coords[closest_idx + 1, :] if closest_idx < n_pts - 1 else np.nan
        )

        direcs = [pt_left - closest_pt, pt_right - closest_pt]
        direcs = [direc / np.linalg.norm(direc) for direc in direcs]
        vec = pt - closest_pt

        par_projs = []
        for direc in direcs:
            scalar = np.dot(vec, direc)
            if scalar > 0:
                par_projs.append(scalar * direc)
            else:
                par_projs.append(np.inf)
        perp_projs = [vec - par_proj for par_proj in par_projs]

        par_projs.append(np.zeros(2))
        perp_projs.append(vec)

        closest_idx = np.argmin(np.linalg.norm(perp_projs, axis=1))

        return closest_pt + par_projs[closest_idx]

    def update_coords(self):
        new_coords = [point.canvas_coords for point in self.points]
        self.canvas.coords(self.id, flatten_list(new_coords))

        for slider in self.sliders:
            slider.update_master_pts()

        return new_coords

    def get_coords_by_v(self, v):
        vlims = self._get_vlims()
        for seg_index, (vlim1, vlim2) in enumerate(vlims):
            if v >= vlim1 and v <= vlim2:
                break
        s = (v - vlim1) / (vlim2 - vlim1)
        pt1 = self.points[seg_index].canvas_coords
        pt2 = self.points[seg_index + 1].canvas_coords

        return pt1 + s * (pt2 - pt1)

    def get_v(self, coords: np.array) -> float:
        """Return the curvilinear abscissa"""
        # stepwise-linear curve independent variable
        seg_index = which_segment_exact(self.canvas_coords, coords)
        s = self.get_s(seg_index, coords)
        vlims = self._get_vlims()[seg_index]
        return vlims[0] + s * (vlims[1] - vlims[0])

    def _get_vlims(self):
        """Return the curvilinear abscissa limits of each segment"""
        points = self.canvas_coords
        t_vecs = []
        for pt1, pt2 in zip(points, points[1::]):
            t_vecs.append(pt2 - pt1)

        ts = np.linalg.norm(np.array(t_vecs), axis=1)
        ts = np.cumsum(ts / np.sum(ts))
        ts = [0.0] + list(ts)

        return [(t0, t1) for t0, t1 in zip(ts, ts[1::])]

    def get_s(self, seg_index: int, coords:np.array)-> float:
        """Return the local curvilinear absissa on a segment"""
        # segment independent variable
        pt1 = self.points[seg_index].canvas_coords
        pt2 = self.points[seg_index + 1].canvas_coords

        return abcissa_segment(pt1, pt2, coords)

    def add_slider(self, slider):
        self.sliders.append(slider)

    def remove_slider(self, slider):
        self.sliders.remove(slider)

    def update(
        self,
        name=None,
        coords=None,
        color=None,
        text=None,
        allow_translate=None,
        allow_delete=None,
        allow_edit=None,
    ):
        super().update(
            name=name,
            coords=coords,
            text=text,
            color=color,
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )



    def as_dict(self):
        data = super().as_dict()
       
        return clean_data_dict(data)


class Line(_AbstractLine):
    type = "Line"

    def __init__(
        self,
        name,
        coords,
        color="red",
        text="",
        allow_translate=True,
        allow_delete=True,
        allow_edit=True,
    ):
        points = []
        for i, coords_ in enumerate(coords):
            brighten = 0.8 * (i + 1) / len(coords)
            points.append(
                _LinePoint(
                    self,
                    coords_,
                    color=color,
                    allow_translate=allow_edit,
                    shade=brighten,
                )
            )
        points[0]._init_shape = "square"

        super().__init__(
            name,
            points,
            color=color,
            text=text,
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )

    def _create_popup_menu(self):
        self.popup_menu = LinePopupMenu(self)

    def add_point(self, coords: np.array, pos: str=None):
        """Add a new point to the line
        
        pos either `begin`, `end` or None
        If none it should create on the segment under scrutiny
        """
        point = _LinePoint(
            self,
            self.canvas.map2real(coords),
            color=self.color,
            allow_translate=self.allow_translate,
        )
        point.create_widget(self.canvas)

        if pos == "begin":
            self.points.insert(0, point)

        elif pos == "end":
            self.points.append(point)
        
        else:
            seg_index, _ = which_segment(self.canvas_coords,point.canvas_coords)
            self.points.insert(seg_index + 1, point)

        self.update_coords()

    def remove_point(self, point):
        if len(self.points) < 3:
            return

        index = self.points.index(point)

        self.points[index].destroy()
        del self.points[index]

       
        self.update_coords()


class Slider(_AbstractLine):
    type = "Slider"

    def __init__(
        self,
        name,
        anchor,
        v_init,
        v_end,
        n_points,
        color="green",
        text="",
        allow_delete=True,
        allow_translate=True,
        allow_edit=True,
    ):
        self.anchor = anchor
        self.anchor.add_slider(self)

        self.master_pts = [
            _MasterSliderPoint(
                self,
                v_init,
                color=color,
                allow_translate=allow_edit,
                shape="square",
            ),
            _MasterSliderPoint(
                self, v_end, color=color,  allow_translate=allow_edit
            ),
        ]

        n_points_static = 30
        
        points = [self.master_pts[0]]
        for t in self._get_ts(n_points_static):
            points.append(_SlaveSliderPoint(self, t, color=color))
        points.append(self.master_pts[1])

        allow_translate = allow_translate and anchor.allow_edit
        super().__init__(
            name,
            points,
            color=color,
            text=text,
            allow_delete=allow_delete,
            allow_translate=allow_translate,
            allow_edit=allow_edit,
        )

    def _get_ts(self, n_points):
        return [(i + 1) / (n_points - 1) for i in range(n_points - 2)]

    @property
    def n_points(self):
        return len(self.points)

    @n_points.setter
    def n_points(self, n_points):
        if self.n_points == n_points or n_points < 2:
            return

        previous_n = self.n_points

        if previous_n > n_points:  # delete points
            diff_n = previous_n - n_points
            for i in range(diff_n):
                self.points[i + 1].destroy()

            del self.points[1 : (1 + diff_n)]

        # add missing points
        ts = self._get_ts(n_points)
        if len(ts) > previous_n - 2:
            for t in ts[previous_n - 2 :]:
                new_point = _SlaveSliderPoint(
                    self, t, color=self.color
                )
                new_point.create_widget(self.canvas)
                self.points.insert(-1, new_point)

        # update points t
        if len(ts) > 0:
            for point, t in zip(self.points[1:-1], ts):
                point.t = t
        else:
            self.update_coords()  # guarantees update of line coords

    @property
    def v_init(self):
        return self.master_pts[0].v

    @v_init.setter
    def v_init(self, value):
        self.master_pts[0].canvas_coords = self.anchor.get_coords_by_v(value)

    @property
    def v_end(self):
        return self.master_pts[1].v

    @v_end.setter
    def v_end(self, value):
        self.master_pts[1].canvas_coords = self.anchor.get_coords_by_v(value)

    @_AbstractLine.allow_translate.setter
    def allow_translate(self, value):
        if value is True and not self.anchor.allow_edit:
            return

        super(Slider, type(self)).allow_translate.fset(self, value)

    def _create_popup_menu(self):
        self.popup_menu = SliderPopupMenu(self)

    def _get_direc(self):
        return self.master_pts[1] - self.master_pts[0]

    def update_coords(self):
        new_coords = super().update_coords()

        # also update slaves
        for point, new_coords_ in zip(self.points[1:-1], new_coords[1:-1]):
            point.canvas_coords = new_coords_

    def update_master_pts(self):
        for pt in self.master_pts:
            pt.update_coords()

    def destroy(self):
        super().destroy()
        self.anchor.remove_slider(self)

    def on_config_delta_mov(self, event):
        self.anchor._click_mouse_coords = event.x, event.y
        self.anchor._click_coords = self.anchor.canvas_coords

    def on_translate(self, event):
        self.anchor.canvas_coords = (
            self.anchor._click_coords + self.anchor._get_delta_mov(event)
        )

    def show(self, from_anchor=False):
        if from_anchor:
            super().show()
        else:
            self.anchor.show()

    def hide(self, from_anchor=False):
        if from_anchor:
            super().hide()
        else:
            self.anchor.hide()

    def update(
        self,
        name=None,
        v_init=None,
        v_end=None,
        n_points=None,
        color=None,
        text=None,
        allow_translate=None,
        allow_delete=None,
        allow_edit=None,
        **kwargs
    ):
        super().update(
            name=name,
            coords=None,
            color=color,
            text=text,
            allow_translate=allow_translate,
            allow_delete=allow_delete,
            allow_edit=allow_edit,
        )

        if v_init is not None:
            self.v_init = v_init

        if v_end is not None:
            self.v_end = v_end

        if n_points is not None:
            self.n_points = n_points

    def as_dict(self):
        data = super().as_dict()

        data.update(
            {
                "v_init": self.v_init,
                "v_end": self.v_end,
                "n_points": self.n_points,
                "anchor": self.anchor.name,
            }
        )
        return clean_data_dict(data)


#TYPE2OBJ = {"Point": Point, "Line": Line, "Slider": Slider}

def get_symbol_bbox(coords: list, size: int):
    """Returns a symbol bounding box
    
    coords are in Pixels
    size is in Pixels
    """
    x, y = coords
    r = int(0.5*size)
    x0, y0 = x - r, y - r
    x1, y1 = x + r, y + r

    return (x0, y0, x1, y1)