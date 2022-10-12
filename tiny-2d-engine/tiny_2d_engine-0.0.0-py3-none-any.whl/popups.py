from abc import ABCMeta
from abc import abstractmethod

import tkinter as tk

#from tiny_2d_engine.forms import OBJ2FORM
from tiny_2d_engine.forms import (
    PointForm,
    LineForm,
    SliderForm,
    CalibrationRectangleForm,
    CanvasImageForm
)

class _BasePopupMenu(tk.Menu, metaclass=ABCMeta):
    """All popup menus ahave the following behavior
    
    the first argument master (self.master) is the canvas itself
    """
    def __init__(self, 
            master:tk.Canvas,  # Make SHURE that it is not necessary an acquisition canvas
        #    bind_trigger=True, 
            config_on_trigger=False):
        """Create a popup up menu
        
        master:  Canvas 
        config_on_trigger:  is true, the options are retested
        """
        super().__init__(master)

        self._preferred_order = self._define_preferred_order()
        self._config_bindings()
        self._config_on_trigger = config_on_trigger

        #if bind_trigger:
        self.bind_menu_trigger()

    def _define_preferred_order(self)-> list:
        """Return an ordered list of the dialog names
        
        Allows to control the order of dialogs to show"""
        return []

    def unbind_menu_trigger(self):
        """Make canvasbtn not binded anymore"""
        
        self.master.unbind("<Button-2>")

    def bind_menu_trigger(self, delay=None):
        """Set btn 2 binding to"""

        if delay is not None:
            raise NotImplementedError
        
        self.master.bind("<Button-2>", self.on_popup_menu_trigger)
        
    def on_popup_menu_trigger(self, event):
        """Callback when Btn2 is hit"""
        
        if self._config_on_trigger: #TODO : ADN: do we really need this ?
            self.delete(0, "end") # remove initial bindings/menuitems
            self._config_bindings() # add bindings/menuitems
        
        self.tk_popup(event.x_root, event.y_root) # Pops up th menu
        self.grab_release()

    def _get_placement_index(self, label):
        index = self._preferred_order.index(label)
        for label in self._preferred_order[:index]:
            if not self.has_item(label):
                index -= 1

        return index

    def _bind_item(self, label, command):
        if not self.has_item(label):
            if label in self._preferred_order:
                index = self._get_placement_index(label)
                self.insert_command(index=index, label=label, command=command)
            else:
                self.add_command(label=label, command=command)

    def _unbind_item(self, label):
        if self.has_item(label):
            self.delete(label)

    @abstractmethod
    def _config_bindings(self):
        """Add the different dialogs in the popup"""
        pass

    def has_item(self, item_label):
        try:
            self.index(item_label)
            return True
        except tk.TclError:
            return False


class ObjectPopupMenu(_BasePopupMenu):
    def __init__(self, obj):
        self.object = obj
        self.triggers = []

        super().__init__(self.object.canvas)#, tearoff=0)
           
    def _define_preferred_order(self):
        return ["Hide", "Edit", "View properties", "Delete"]

    
    def unbind_menu_trigger(self):
        for obj in [self.object] + self.triggers:
            self._unbind_obj_menu_trigger(obj)

    def bind_menu_trigger(self, delay=None):

        if delay is not None:
            raise NotImplementedError

        for obj in [self.object] + self.triggers:
            self._bind_obj_menu_trigger(obj)

    def _unbind_obj_menu_trigger(self, obj):
        self.master.tag_unbind(obj.id, "<Button-2>")

    def _bind_obj_menu_trigger(self, obj):
        self.master.tag_bind(
            obj.id, "<Button-2>", self.on_popup_menu_trigger, add="+"
        )

    def _config_bindings(self):
        self.add_command(label="Hide", command=self.on_show_hide)

        if self.object.allow_edit:
            self.bind_edit()
        else:
            self.bind_view()

        if self.object.allow_delete:
            self.bind_delete()

        self.bind_add_objects()

    def bind_delete(self):
        self._bind_item("Delete", self.on_delete)

    def unbind_delete(self):
        self._unbind_item("Delete")

    def bind_edit(self):
        self._bind_item("Edit", self.on_edit)
        self._bind_edit_behavior()

    def unbind_edit(self):
        self._unbind_item("Edit")
        self._unbind_edit_behavior()
        self.bind_view()

    def _bind_edit_behavior(self):
        pass

    def _unbind_edit_behavior(self):
        pass

    def bind_view(self):
        self._bind_item("View properties", self.on_view)

    def bind_add_objects(self):
        pass

    def _bind_trigger(self, obj):
        pass

    def _unbind_trigger(self):
        pass

    def add_trigger(self, obj):
        self.triggers.append(obj)
        self._bind_obj_menu_trigger(obj)
        self._bind_trigger(obj)

    def remove_trigger(self, obj):
        self.triggers.remove(obj)
        self._unbind_obj_menu_trigger(obj)
        self._unbind_trigger(obj)

    def on_show_hide(self, *args):
        hidden = self.master.is_hidden(self.object.id)

        if hidden:
            self.object.show()
        else:
            self.object.hide()

    def on_delete(self, *args):
        self.master.delete_object(self.object.id)
        self.master.popup_menu.bind_menu_trigger(delay=True)

    def on_edit(self, readonly=False):
        # todo : make these calls explicit so we can trace this
        # OBJ2FORM.get(self.object.type, lambda *args, **kwargs: None)(
        #     self.master, obj=self.object
        # )

        if self.object.type == "Point":
            PointForm(self.master, obj=self.object, readonly=readonly)
        if self.object.type == "Line":
            LineForm(self.master, obj=self.object, readonly=readonly)
        if self.object.type == "Slider":
            SliderForm(self.master, obj=self.object, readonly=readonly)
        if self.object.type == "CalibrationRectangle":
            CalibrationRectangleForm(self.master, obj=self.object, readonly=readonly)
        if self.object.type == "CanvasImage":
            CanvasImageForm(self.master, obj=self.object, readonly=readonly)
        else:
            raise NotImplementedError    


    def on_view(self):
        self.on_edit(readonly=True)
        # OBJ2FORM.get(self.object.type, lambda *args, **kwargs: None)(
        #     self.master, obj=self.object, readonly=True
        # )


class LinePopupMenu(ObjectPopupMenu):
    def _define_preferred_order(self):
        order = super()._define_preferred_order()
        order.extend(["Refine", "Add point", "Remove point", "Add slider"])
        return order

    def _bind_store_click_position(self):
        self.object.canvas.tag_bind(
            self.object.id, "<Button-2>", self.on_store_click_position, add="+"
        )

    def _bind_trigger(self, obj):
        # avoid addition of overlapped point
        self.object.canvas.tag_bind(obj.id, "<Enter>", self._unbind_add_point, add="+")
        self.object.canvas.tag_bind(obj.id, "<Leave>", self._bind_add_point, add="+")

        # hide remove point if not point
        self.object.canvas.tag_bind(
            obj.id,
            "<Enter>",
            lambda e, point=obj: self.bind_remove_point(point, e),
            add="+",
        )
        self.object.canvas.tag_bind(
            obj.id, "<Leave>", self.unbind_remove_point, add="+"
        )

    def _bind_edit_behavior(self):
        self._bind_item("Refine", self.on_refine)
        self._bind_store_click_position()

    def _unbind_edit_behavior(self):
        # store click is not being unbind since there's no side effects
        self._unbind_item("Refine")
        self._unbind_add_point()

    def _bind_add_point(self, *args):
        if self.object.allow_edit:
            self._bind_item("Add point", self.on_add_point)

    def _unbind_add_point(self, *args):
        self._unbind_item("Add point")

    def bind_add_objects(self):
        self._bind_add_slider()

    def _bind_add_slider(self):
        self._bind_item("Add slider", self.on_add_slider)

    def bind_remove_point(self, point, *args):
        if self.object.allow_edit:
            self._bind_item(
                "Remove point", lambda point=point: self.on_remove_point(point)
            )

    def unbind_remove_point(self, *args):
        self._unbind_item("Remove point")

    def on_add_slider(self):
        SliderForm(self.object.canvas, line_names=[self.object.name])

    def on_add_point(self):
        coords = (self._x_click, self._y_click)
        new_coords = self.object.find_closest_point(coords)
        self.object.add_point(new_coords)

    def on_refine(self):
        coords = self.object.canvas_coords
        for coords1, coords2 in zip(coords, coords[1::]):
            new_coords = (coords2 + coords1) / 2
            self.object.add_point(new_coords)

    def on_remove_point(self, point):
        self.object.remove_point(point)
        self.unbind_remove_point()
        self._bind_add_point()

    def on_store_click_position(self, event):
        self._x_click = event.x
        self._y_click = event.y


class SliderPopupMenu(ObjectPopupMenu):
    def _define_preferred_order(self):
        order = super()._define_preferred_order()
        #order.extend(["Refine", "Coarse"])
        return order

    # def _bind_edit_behavior(self):
    #     self._bind_item("Refine", self.on_refine)
    #     self._bind_item("Coarse", self.on_coarse)

    # def _unbind_edit_behavior(self):
    #     self._unbind_item("Refine")
    #     self._unbind_item("Coarse")

    # def on_refine(self):
    #     self.object.n_points = self.object.n_points + 1

    # def on_coarse(self):
    #     self.object.n_points = self.object.n_points - 1


class ImagePopupMenu(ObjectPopupMenu):
    def on_popup_menu_trigger(self, event):
        self.object.canvas.popup_menu.delay_menu_trigger()
        super().on_popup_menu_trigger(event)

    def _unbind_obj_menu_trigger(self, obj):
        self.object.canvas.tag_unbind(obj.id, "<Control-2>")

    def _bind_obj_menu_trigger(self, obj):
        self.object.canvas.tag_bind(obj.id, "<Control-2>", self.on_popup_menu_trigger)

    def on_delete(self, *args):
        self.object.canvas.delete_image()
        self.object.canvas.popup_menu.bind_menu_trigger(delay=True)


class ObjectAddPopupMenu(_BasePopupMenu):
    """Pop up dialog to add objects"""
    def __init__(self, canvas):
        super().__init__(canvas, config_on_trigger=True)#, bind_trigger=False)

    def _define_preferred_order(self):
        return ["Point", "Line", "Slider"]

    def _config_bindings(self):
        self._bind_item("Point", self.on_add_point)
        self._bind_item("Line", self.on_add_line)
        if len(self.master.get_by_type("Line")) > 0:
            self._bind_item("Slider", self.on_add_slider)

    def on_add_point(self):
        PointForm(self.master)

    def on_add_line(self):
        LineForm(self.master)

    def on_add_slider(self):
        SliderForm(self.master)
