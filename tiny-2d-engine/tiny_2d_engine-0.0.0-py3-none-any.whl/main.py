"""Principal access to 2D Acquisition """

import json

from tkinter import (ttk)
import tkinter as tk

from tiny_2d_engine.forms import (
    CalibrationRectangleForm,
    CanvasImageForm
)

from tiny_2d_engine.acquisition_canvas import (
    AcquisitionCanvas
)

class Acquisition2D(ttk.Frame):
    """Main widget for acquisition"""
    def __init__(self,holder, filename=None, standalone=False, **kwargs):

        super().__init__(holder,  **kwargs)
        self.acq_canvas = AcquisitionCanvas(self)
        self.holder=holder
        self.filename = filename
        self.standalone = standalone
        
        if filename is not None:
            with open(filename, "r") as file:
                data = json.load(file)
                self.acq_canvas.load_dict(data)
        

        self.acq_canvas.pack(side="right", fill="both", expand=True)
        control = self.control()
        control.pack()

    def control(self, width=20):
        """Its good to have some self control no?"""
        dialog = ttk.LabelFrame(self, text="2D-Acquisition")
        dialog.pack()


        if not self.standalone :
        
            memry = ttk.LabelFrame(dialog,text="Memory")
            memry.pack(side="top")

            memry_reload= ttk.Button(
                memry, 
                text="Reload",
                command=self.on_load,
                )
            memry_reload.pack(side="top")
        
            memry_save = ttk.Button(
                memry, 
                text="Save",
                command=self.on_save,
                )
            memry_save.pack(side="top")

        
            memry_saveas = ttk.Button(
                memry, 
                text="Save as",
                command=self.on_save_as,
            )
            memry_saveas.pack(side="top")
            memry_quit= ttk.Button(
                memry, 
                text="Quit",
                command=self.on_quit,
                )
            memry_quit.pack(side="top")

        whereami = ttk.LabelFrame(dialog,text="Pointer location")
        whereami.pack(side="top")

        whereami_lbl = ttk.Label(
            whereami, 
            textvariable=self.acq_canvas.whereami,
            width=width,
            justify="center" )
        whereami_lbl.pack(side="top")

        mainct = ttk.LabelFrame(dialog,text="Main controls")
        mainct.pack(side="top")
        
        self.calib_show=tk.BooleanVar(self,value=1)
        calib_switch = ttk.Checkbutton(
            mainct, 
            text="Show/hide calibration",
            command=self.on_show_hide_cal,
            variable=self.calib_show
            )
        calib_switch.pack(side="top")

        self.img_show=tk.BooleanVar(self,value=1)
        img_switch = ttk.Checkbutton(
            mainct, 
            text="Show/hide image",
            command=self.on_show_hide_img,
            variable=self.img_show
            )
        img_switch.pack(side="top")
        

        img_edit = ttk.Button(
            mainct, 
            text="Image edit",
            command=self.on_edit_image,
            )
        img_edit.pack(side="top")

        calib_edit = ttk.Button(
            mainct, 
            text="Calibration edit",
            command=self.on_edit_calibration,
            )
        calib_edit.pack(side="top")

        show_all = ttk.Button(
            mainct, 
            text="Show all objects",
            command=self.on_show_all,
            )
        show_all.pack(side="top")



        info_lbl = ttk.Label(
            dialog, 
            text="Right-click in the canvas for contextual menus",
            width=width,
            wraplength=width*10 )
        info_lbl.pack(side="top")
        
        return dialog


    def on_show_hide_cal(self):
        """Callback for calibration show or not"""
        can = self.acq_canvas
        hidden = can.is_hidden(can.calibration_rectangle.id)
        if hidden:
            can.calibration_rectangle.show()
        else:
            can.calibration_rectangle.hide()
    
    def on_show_hide_img(self):
        """Callback for image show or not"""
        can = self.acq_canvas
        hidden = can.is_hidden(can.image.id)
        if hidden:
            can.image.show()
        else:
            can.image.hide()
    
    def on_edit_calibration(self):
        """Ask for edition of the calibration menu"""
        # if obj is None, a new calibration is created
        #     else the object in question is edited
        # before creation, self.acq_canvas.calibration_rectangle is None
        CalibrationRectangleForm(self.acq_canvas, obj=self.acq_canvas.calibration_rectangle)

    def on_edit_image(self):
        CanvasImageForm(self.acq_canvas, obj=self.acq_canvas.image )

    def on_show_all(self):
        self.acq_canvas.show_all()

    def on_save(self):
        if self.standalone:
            print("no save in standalone mode")
            return
        
        if self.filename is None:
                self.on_save_as()
        else:
            self.acq_canvas.dump(self.filename)


    def on_load(self):
        if self.standalone:
            print("no load in standalone mode")
            return
    
        filename = tk.filedialog.askopenfilename(
            tixtle="Load file", filetypes=(("json files", ".json"),)
        )
        if filename == "":
            return

        self.acq_canvas.clear()
        with open(filename, "r") as file:
            data = json.load(file)
        self.filename = filename
        update_canvas_from_dict(self.acq_canvas, data)
        
    ##############
    # Only for file based situations
    #
    def on_save_as(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".json")

        if filename == "":
            return
        self.filename = filename
        self.acq_canvas.dump(self.filename)

        return filename

    def on_quit(self):
        save = tk.messagebox.askyesno("Save before exiting", "Save changes before exit?")
        if save:
            self.on_save()
        self.holder.quit()
