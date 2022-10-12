import os
from abc import ABCMeta
from abc import abstractmethod
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import numpy as np
from PIL import Image
from PIL import ImageTk


#import tiny_2d_engine.acquisition_canvas as canvas_objects  # avoid circular import
#from tiny_2d_engine.generic_widgets import ScrollableFrame
from tiny_2d_engine.utils import get_image_path
from tiny_2d_engine.utils import disable_children

from tiny_2d_engine.constants import ICON_NAMES
from tiny_2d_engine.color_utils import custom_colors

# TODO: check translate in sliders -> should not change if line cannot

IMG_FORMATS = [".gif", ".jpg", ".jpeg", ".png"]


class _BaseForm(tk.Toplevel, metaclass=ABCMeta):
    def __init__(
        self,
        canvas,
        frame_names,
        *args,
        obj=None,
        title=None,
        vert_space=10,
        readonly=False,
        **kwargs,
    ):
        self.canvas = canvas
        self.vert_space = vert_space
        self.object = obj

        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.holder = ttk.Frame(self)
        self.holder.grid(column=0, row=0, sticky="n")

        self.info_container = dict()
        for i, frame_name in enumerate(frame_names):
            vert_space_ = self.vert_space if i else 0.0
            # ugly redirection to all ._config_######()
            frame, dict_info = getattr(self, f"_config_{frame_name}")()
            frame.pack(fill="both", expand=True, pady=vert_space_)
            self.info_container.update(dict_info)
        
        if self.edit:
            self._set_edit_values()
            self._set_edit_bindings()
        else:
            self._set_add_default_values()
            self._set_add_bindings()

        self._set_bindings()

        if title:
            self.title(title)

        if readonly:
            disable_children(self)

        self._config_button(self.edit)

    def _set_edit_values(self):
        self.set(self.object.as_dict())

    def _set_add_default_values(self):
        pass

    def _set_bindings(self):
        self._bind_allow_edit()
        self._bind_allow_translate()

    def _set_add_bindings(self):
        pass

    def _set_edit_bindings(self):
        pass

    @property
    def edit(self):
        return False if self.object is None else True

    def _config_name(self):
        forbidden_values = self.canvas.get_names()
        if self.edit:
            forbidden_values.remove(self.object.name)

        frame = StringEntryFrame(
            self.holder, "name", allow_empty=False, forbidden_values=forbidden_values
        )
        return frame, {"name": frame}

    def _config_coords(self, name="coords", label="coords"):
        frame = CoordsFrame(self.holder, label=label)
        return frame, {name: frame}

    def _config_color(self):
        frame = ComboFrame(
            self.holder, "color", default="red", values=list(custom_colors.keys())
        )
        return frame, {"color": frame}

   
    def _config_allow(self, allow_edit=True, allow_translate=True, allow_delete=True):
        container_frame = ttk.Frame(self.holder)
        frame_dict = {}

        if allow_translate:
            translate_frame = BoolFrame(
                container_frame, "allow_translate", default=True
            )
            translate_frame.pack(side="left", fill="both", expand=True)
            frame_dict["allow_translate"] = translate_frame

        if allow_edit:
            edit_frame = BoolFrame(container_frame, "allow edit")
            edit_frame.pack(side="left", fill="both", expand=True)
            frame_dict["allow_edit"] = edit_frame

        if allow_delete:
            delete_frame = BoolFrame(container_frame, "allow delete")
            delete_frame.pack(side="left", fill="both", expand=True)
            frame_dict["allow_delete"] = delete_frame

        return container_frame, frame_dict

    def _config_text(self):
        frame = StringEntryFrame(self.holder, "text")
        return frame, {"text": frame}

    def _config_button(self, edit):
        if edit:
            if self.object.allow_edit:
                btn = ttk.Button(self.holder, command=self.on_edit, text="Update")
            else:
                btn = ttk.Button(self.holder, command=self.on_quit, text="Close")
        else:
            btn = ttk.Button(self.holder, command=self.on_add, text="Add")
        btn.pack(pady=self.vert_space)

    def _bind_allow_edit(self):
        if not (
            "allow_edit" in self.info_container
            and "allow_translate" in self.info_container
        ):
            return

        edit_var = self.info_container["allow_edit"].tk_var
        edit_var.trace("w", self._on_allow_edit_change)

    def _bind_allow_translate(self):
        if "allow_translate" not in self.info_container:
            return

        translate_var = self.info_container["allow_translate"].tk_var
        translate_var.trace("w", self._on_allow_translate_change)

    def _post_process_get_data(self, data):
        return data

    def _preprocess_set_data(self, values):
        return values

    def _add_object(self, data):


        if self.obj_type == "Point":
            self.canvas.add_point(data)
        
        elif self.obj_type == "Line":
            self.canvas.add_line(data)
    
        elif self.obj_type == "Slider":
            self.canvas.add_slider(data)
        
    def _get_invalid_frames(self):
        """Returns invalid frames."""
        return [
            label_frame
            for label_frame in self.info_container.values()
            if not label_frame.validate()
        ]

    def _validate(self):
        invalid_frames = self._get_invalid_frames()
        if len(invalid_frames) == 0:
            return True

        # create message box
        invalid_names = [frame.name for frame in invalid_frames]
        message = f'The following fields are invalid:\n{", ".join(invalid_names)}'
        messagebox.showwarning(message=message)

        return False

    def get(self):
        data = {key: frame.get() for key, frame in self.info_container.items()}
        return self._post_process_get_data(data)

    def set(self, values):
        values = self._preprocess_set_data(values)
        for key, value in values.items():
            if key in self.info_container:
                self.info_container[key].set(value)

    def on_add(self, *args):
        if not self._validate():
            return

        data = self.get()
        self._add_object(data)
        self.on_quit(*args)

    def on_edit(self, *args):
        if not self._validate():
            return

        data = self.get()
        self.object.update(**data)
        self.on_quit(*args)

    def on_quit(self, *args):
        self.destroy()

    def _on_allow_edit_change(self, *args):
        value = self.info_container["allow_edit"].tk_var.get()
        if not value:
            self.info_container["allow_translate"].tk_var.set(False)

    def _on_allow_translate_change(self, *args):
        translate_var = self.info_container["allow_translate"].tk_var
        if translate_var.get() and not self.info_container["allow_edit"].tk_var.get():
            translate_var.set(False)


class PointForm(_BaseForm):
    def __init__(self, canvas, *args, obj=None, vert_space=10, **kwargs):
        self.obj_type = "Point"
        frame_names = ["name", "color", "allow", "text"]

        title = "Add new point" if obj is None else "Edit point"
        super().__init__(
            canvas,
            frame_names,
            *args,
            obj=obj,
            title=title,
            vert_space=vert_space,
            **kwargs,
        )


class LineForm(_BaseForm):
    def __init__(self, canvas, *args, obj=None, vert_space=10, **kwargs):
        self.obj_type = "Line"
        frame_names = ["name", "color", "allow", "text"]

        title = "Add new line" if obj is None else "Edit line"
        super().__init__(
            canvas,
            frame_names,
            *args,
            obj=obj,
            title=title,
            vert_space=vert_space,
            **kwargs,
        )


class SliderForm(_BaseForm):
    def __init__(
        self, canvas, *args, obj=None, vert_space=10, line_names=None, **kwargs
    ):
        self.obj_type = "Slider"
        frame_names = [
            "name",
            "lines",
            "color",
            "allow",
            "text",
        ]
        self.line_names = line_names

        title = "Add new slider" if obj is None else "Edit slider"
        super().__init__(
            canvas,
            frame_names,
            *args,
            obj=obj,
            title=title,
            vert_space=vert_space,
            **kwargs,
        )

    def _config_lines(self):
        if self.edit:
            line_names = [self.object.anchor.name]
        else:
            line_names = self._get_available_line_names()

        frame = ComboFrame(
            self.holder, "anchor name", default=line_names[0], values=line_names
        )
        return frame, {"anchor": frame}

    def _get_lines(self):
        return self.canvas.get_by_type("Line")

    def _get_line_names(self):
        return self.canvas.get_names("Line")

    def _get_available_line_names(self):
        if self.line_names is not None:
            return self.line_names
        else:
            return self._get_line_names()

    def _get_line_from_name(self, line_name):
        line_names = self._get_line_names()
        return self._get_lines()[line_names.index(line_name)]

    def _post_process_get_data(self, data):
        line = self._get_line_from_name(data["anchor"])
        if self.edit:
            del data["anchor"]
        else:
            data["anchor"] = line

        return data

    def _preprocess_set_data(self, values):
        values = super()._preprocess_set_data(values)
        values["v"] = [[v] for v in [values["v_init"], values["v_end"]]]

        return values

    def _on_allow_translate_change(self, *args):
        line_name = self.info_container["anchor"].get()
        line = self._get_line_from_name(line_name)
        if not line.allow_edit:
            self.info_container["allow_translate"].tk_var.set(False)


class CalibrationRectangleForm(_BaseForm):
    def __init__(self, canvas, *args, obj=None, vert_space=10, **kwargs):
        frame_names = [
            "canvas_coords",
            "coords",
            "keep_real",
            "allow",
        ]

        title = "Add calibration" if obj is None else "Edit calibration"
        super().__init__(
            canvas,
            frame_names,
            *args,
            obj=obj,
            title=title,
            vert_space=vert_space,
            **kwargs,
        )

    def _set_add_default_values(self):
        self._set_default_coords()

    def _get_coords_frame(self):
        return self.info_container["coords"]

    def _get_canvas_coords_frame(self):
        return self.info_container["canvas_coords"]

    def _config_coords(self):
        """Dialog on coordinates in meters"""
        frame = MultipleCoordsFrame(
            self.holder,
            label="World coords (m)",
            state="normal"
        )
        return frame, {"coords": frame}

    def _config_canvas_coords(self):
        """Dialog on coordinates in pixels"""
        frame = MultipleCoordsFrame(
            self.holder,
            label="Canvas coords (pix)",
        )
        return frame, {"canvas_coords": frame}

    def _config_keep_real(self):
        """For calibration
        
        If true, all objects are resacled to match changes
        """
        frame = BoolFrame(self.holder, label="Rescale everything")
        return frame, {"keep_real": frame}

    def _config_allow(self):
        return super()._config_allow(
            allow_edit=True, allow_translate=True, allow_delete=False
        )

    def _set_default_coords(self):
        """What happen when the calibration has never bieen done"""
        coords_frame = self._get_coords_frame()
        coords_frame.set([[-10.0, 10.0], [10.0, -10.0]])
        canvas_coords_frame = self._get_canvas_coords_frame()
        width, height = float(self.canvas.width), float(self.canvas.height)
        canvas_coords_frame.set([[20.0, 20.0], [width - 20, height - 20]])

    def _add_object(self, data):
        self.canvas.calibrate(**data)


class CanvasImageForm(_BaseForm):
    def __init__(self, canvas, *args, obj=None, vert_space=10, **kwargs):
        frame_names = ["path", "allow"]

        title = "Add image" if obj is None else "Edit image"
        super().__init__(
            canvas,
            frame_names,
            *args,
            obj=obj,
            title=title,
            vert_space=vert_space,
            **kwargs,
        )

    def _config_path(self):
        frame = PathEntryFrame(self.holder, "path", self.on_browse)
        return frame, {"path": frame}

    def _add_object(self, data):
        self.canvas.add_image(**data)

    def _config_allow(self):
        return super()._config_allow(
            allow_edit=True, allow_translate=False, allow_delete=False
        )

    def on_browse(self, *args):
        previous_path = self.info_container["path"].get()

        title = "Choose image"
        filetypes = [("image files", fmt) for fmt in IMG_FORMATS]
        path = filedialog.askopenfilename(title=title, filetypes=filetypes)

        if path == "":
            return

        path = os.path.relpath(path)

        if path == previous_path:
            return

        self.info_container["path"].set(path)


class _LabeledFrame(ttk.Frame):
    def __init__(self, holder, label):
        super().__init__(holder)
        self.label = None

        if label is not None:
            self.label = ttk.Label(self, text=label)
            self.label.pack()

    @property
    def name(self):
        return self.label.cget("text") if self.label is not None else None

    def get(self):
        return self.tk_var.get()

    def set(self, value):
        return self.tk_var.set(value)

    def validate(self):
        return True


class _EntryFrame(_LabeledFrame, metaclass=ABCMeta):
    def __init__(self, holder, label, default):
        super().__init__(holder, label)

        self.tk_var = self._create_tk_var()
        self.tk_var.set(default)

        self.entry = ttk.Entry(self, textvariable=self.tk_var)
        self.entry.pack()

    @abstractmethod
    def _create_tk_var(self):
        pass


class StringEntryFrame(_EntryFrame):
    def __init__(
        self, holder, label, default="", allow_empty=True, forbidden_values=None
    ):
        self.allow_empty = allow_empty
        self.forbidden_values = forbidden_values if forbidden_values is not None else ()

        super().__init__(holder, label, default)

    def _create_tk_var(self):
        return tk.StringVar()

    def validate(self):
        value = self.get()
        if not self.allow_empty:
            if value == "":
                return False

        if value in self.forbidden_values:
            return False

        return True


class IntEntryFrame(_EntryFrame):
    def __init__(self, holder, label, default=0, min_value=None, max_value=None):
        super().__init__(holder, label, default)
        self.min_value = min_value
        self.max_value = max_value

    def _create_tk_var(self):
        return tk.IntVar()

    def validate(self):
        value = self.get()

        if self.min_value is not None:
            if value < self.min_value:
                return False

        if self.max_value is not None:
            if value > self.max_value:
                return False

        return True


class BoolFrame(_LabeledFrame):
    def __init__(self, holder, label, default=True):
        super().__init__(holder, label)

        self.tk_var = tk.BooleanVar()
        self.tk_var.set(default)
        btn = ttk.Checkbutton(self, variable=self.tk_var)
        btn.pack()


class ComboFrame(_LabeledFrame):
    def __init__(self, holder, label, default, values):
        super().__init__(holder, label)

        self.tk_var = tk.StringVar()
        self.tk_var.set(default)

        combo = ttk.Combobox(
            self, textvariable=self.tk_var, values=values, state="readonly"
        )
        combo.pack()



class CoordsFrame(_LabeledFrame):
    """Sub dialog for geting coordinates"""
    def __init__(self, holder, label="Coords (pix)", state="disabled" ):
        super().__init__(holder, label)
        self.tk_vars = [tk.DoubleVar(), tk.DoubleVar()]
        line_x = ttk.Frame(self)
        line_x.pack(side="top")
        label_x = ttk.Label(line_x, text="x")
        entry_x = ttk.Entry(line_x, textvariable=self.tk_vars[0], state=state)
        entry_x.pack(side="right")
        label_x.pack(side="right")
        
        line_y = ttk.Frame(self)
        line_y.pack(side="top")
        
        label_y = ttk.Label(line_y, text="y")
        entry_y = ttk.Entry(line_y, textvariable=self.tk_vars[1], state=state)
        entry_y.pack(side="right")
        label_y.pack(side="right")
        
    def get(self):
        return [tk_var.get() for tk_var in self.tk_vars]

    def set(self, values):
        for tk_var, value in zip(self.tk_vars, values):
            tk_var.set(value)

    def validate(self):
        try:
            self.get()
        except tk.TclError:
            return False

        return True


class MultipleCoordsFrame(_LabeledFrame):
    """Dialog to gt multiple coordinates"""

    def __init__(self, holder, label="Coords", state="disabled", allow_rep=False):
        super().__init__(holder, label)
        self.allow_rep = allow_rep
        self.frames = []
        self.state = state

    def add_entry(self, coords, id_):
        frame = CoordsFrame(self,label=f"Point #{id_}", state=self.state)
        frame.set(coords)
        frame.pack()

        self.frames.append(frame)

    def remove_last_entry(self):
        self.frames[-1].destroy()
        del self.frames[-1]

    def set(self, values):
        n_frames = len(self.frames)
        n_values = len(values)

        # update existing entries
        for frame, coords in zip(self.frames, values):
            frame.set(coords)

        # delete frames in excess
        if n_frames > n_values:
            for i in range(n_frames - n_values):
                self.remove_last_entry()

        # add missing entries
        elif n_values > n_frames:
            for id_,coords in enumerate(values[n_frames:]):
                self.add_entry(coords, id_+1)

    def get(self):
        return [frame.get() for frame in self.frames]

    def validate(self):
        # verify each frame
        for frame in self.frames:
            if not frame.validate():
                return False

        # verify repetitions
        if not self.allow_rep:
            for i, frame in enumerate(self.frames):
                coords = frame.get()
                for other_frame in self.frames[i + 1 :]:
                    other_coords = other_frame.get()
                    if np.allclose(coords, other_coords):
                        return False
        return True


class PathEntryFrame(_LabeledFrame):
    def __init__(self, holder, label, command, default="", allow_empty=False):
        super().__init__(holder, label)

        self.path_frame = StringEntryFrame(
            self, None, default=default, allow_empty=allow_empty
        )
        self.path_frame.pack(side="left", fill="both")
        self.path_frame.entry.configure(state="readonly")

        self.button = self._create_button(command)
        self.button.pack(side="left", fill="y")

    def _create_button(self, command):
        filename = get_image_path(ICON_NAMES["load"])

        img = Image.open(filename).convert("RGBA")
        self._button_image = ImageTk.PhotoImage(img)

        button = ttk.Button(self, command=command, image=self._button_image)
        return button

    def get(self):
        return self.path_frame.get()

    def set(self, value):
        self.path_frame.set(value)

    def validate(self):
        return self.path_frame.validate()


