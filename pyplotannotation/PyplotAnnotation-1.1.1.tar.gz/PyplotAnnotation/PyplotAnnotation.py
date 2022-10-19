import os
import glob
import json
from PIL import Image, ImageDraw
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
import datetime

import fire

INPUT_FOLDER = "inputs"
MASK_FOLDER = "masks"

COLORS = ('tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
          'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'white')

def save_json(entry):
    json_filename = 'results.json'
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as json_file:
            json_data = json.load(json_file)
    else:
        json_data = {}
    json_data.update(entry)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, sort_keys=True)

class Annotater:

    def button_press_event(self, event):
        def central_click_event():
            """
            Can be done after selecting a class, add a point to a polygon.
            """
            if event.xdata is None or event.ydata is None:
                print('Error: "central click" should add a point, but you clicked outside the figure')
                return
                
            (x1, y1) = (int(event.xdata), int(event.ydata))
            if self.rectangle_mode and len(self.polygons_details[-1][1]) == 1:
                x0, y0 = self.polygons_details[-1][1][0]
                for point in [(x0, y1), (x1, y1), (x1, y0)]:
                    self.polygons_details[-1][1].append(point)
                    self.add_point(self.polygons_details[-1][0], point)
            else:
                self.polygons_details[-1][1].append((x1, y1))
                self.add_point(self.polygons_details[-1][0], (x1, y1))

        def right_click_event():
            """
            Can be done before validating a polygon, remove the last point.
            """
            if len(self.plotted_points) == 0:
                print('Error: "right click" should remove the last point, but there is none.')
                return
            self.remove_point()
            self.polygons_details[-1][1].pop(-1)

        if self.polygons_details[-1][0] is None:
            print('Error: right and central clicks require a class to be selected.')
            return

        _ = (central_click_event, right_click_event)[event.button.value - 2]()

    def key_press_event(self, event):
        def class_key_event(class_id):
            """
            Can be done when no polygon is in the current stack, select a class.
            """
            if self.polygons_details[-1][1]:
                print(f'Error: {class_id} should select a class, but the current polygon has not been confirmed.')
                return
            self.polygons_details[-1][0] = class_id

            handles = [mpatches.Patch(color=color, label=f"Class {i + 1}") for i, color in enumerate(COLORS)]
            handles.append(mpatches.Patch(color=COLORS[class_id], label=f"Current class"))
            plt.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))
            plt.draw()

        def enter_press_event():
            """
            Can be done when no class is selected, validate an image, create the input/output files.
            """
            if self.polygons_details[-1][0] is not None:
                print('Error: "Enter" validate a picture, but this is not possible if a class is selected')
                return
            self.draw_masks()
            self.remove_polygons()
            self.polygons_details = [[None, []]]
            self.plotted_image.remove()
            
            print('Validate, working for', datetime.datetime.now() - self.begin)
            self.count += 1
            print('Mean annotation time:', (datetime.datetime.now()-self.begin)/self.count)

            plt.draw()
            if self.filenames:
                self.new_image(self.filenames.pop(0))
            else:
                plt.close()

        def zero_press_event():
            """
            Can be done after adding at least three points to a polygon, validate the current polygon.
            """
            if len(self.polygons_details[-1][1]) < 0:
                self.polygons_details[-1][0] = None
            if len(self.polygons_details[-1][1]) < 3:
                print('Error: Not enough point to create a polygon')
                return
            self.add_polygon()
            self.polygons_details.append([None, []])
            
        def r_press_event():
            """
            Can be done when no class is selected, toogle the rectangle mode
            """
            if len(self.polygons_details[-1][1]) > 1:p
            if len(self.polygons_details[-1][1]) > 1:
                print("Can't switch to rectangle mode while drawing polygons")
            else:
                self.rectangle_mode = False if self.rectangle_mode else True
                print(f'Rectangle Mode is now at {self.rectangle_mode}')

        class_keys = '123456789ab'
        if event.key in class_keys:
            class_key_event(class_keys.index(event.key))
        elif event.key == "enter":
            enter_press_event()
        elif event.key == "0":
            zero_press_event()
        elif event.key == 'r':
            r_press_event()

    def new_image(self, filename, border=0.1):
        self.current_filename = filename
        self.current_image = Image.open(filename)
        self.plotted_image = plt.imshow(self.current_image, interpolation="bilinear", cmap='gray')

        x_border = int(border * self.current_image.size[0])
        y_border = int(border * self.current_image.size[1])
        plt.xlim((-x_border, self.current_image.size[0] + x_border))
        plt.ylim((self.current_image.size[1] + y_border, -y_border))

        plt.legend(handles=[mpatches.Patch(color=color, label=f"Class {i + 1}") for i, color in enumerate(COLORS)],
                   loc='center left', bbox_to_anchor=(1, 0.5))
        plt.draw()

    def add_polygon(self, alpha=0.5):
        self.plotted_polygons.append(self.ax.add_patch(mpatches.Polygon(self.polygons_details[-1][1],
                                                                        color=COLORS[self.polygons_details[-1][0]],
                                                                        alpha=alpha)))
        plt.draw()

        while self.plotted_points:
            self.remove_point()

    def add_point(self, class_id, point, point_marker='+', linestyle='--'):
        self.plotted_points.append(plt.scatter(point[0], point[1], c=COLORS[class_id], marker=point_marker))
        if len(self.polygons_details[-1][1]) > 1:
            (x1, y1), (x2, y2) = self.polygons_details[-1][1][-2:]
            self.plotted_lines.extend(plt.plot((x1, x2), (y1, y2), c=COLORS[class_id], linestyle=linestyle))
        plt.draw()

    def remove_point(self):
        self.plotted_points.pop(-1).remove()
        if self.plotted_lines:
            self.plotted_lines.pop(-1).remove()
        plt.draw()

    def remove_polygons(self):
        while self.plotted_polygons:
            polygon = self.plotted_polygons.pop()
            polygon.remove()

    def draw_masks(self, void_mask_class = 8):
        input_filename = os.path.join(self.input_folder, os.path.split(self.current_filename)[-1])
        output_filename = os.path.join(self.mask_folder, os.path.split(self.current_filename)[-1])

        os.makedirs(os.path.split(input_filename)[0], exist_ok=True)
        os.makedirs(os.path.split(output_filename)[0], exist_ok=True)

        self.current_image.save(f"{os.path.splitext(input_filename)[0]}.png")

        masks = {}
        void_mask_polygons = []
        complete_mask = Image.new('L', self.current_image.size)
        complete_mask_draw = ImageDraw.Draw(complete_mask)
        for class_id, points in self.polygons_details:
            if len(points) < 3:
                continue
            if class_id == void_mask_class:
                void_mask_polygons.append(points)
            if class_id not in masks:
                new_im = Image.new('L', self.current_image.size)
                masks[class_id] = new_im, ImageDraw.Draw(new_im)
            masks[class_id][1].polygon(points, fill=255)
            complete_mask_draw.polygon(points, fill=255)
        for points in void_mask_polygons:
            for class_id, (mask, mask_draw) in masks.items():
                if class_id != void_mask_class:
                    mask_draw.polygon(points, fill=0)
            complete_mask_draw.polygon(points, fill=0)

        for class_id, (mask, _) in masks.items():
            mask.save(f"{os.path.splitext(output_filename)[0]}_{class_id+1}.png")
        complete_mask.save(f"{os.path.splitext(output_filename)[0]}.png")
        
        save_json({self.current_filename:self.polygons_details})
        

    def __init__(self, filenames, input_folder, mask_folder):
        print(filenames)
        self.filenames = glob.glob(filenames)
        self.input_folder = input_folder
        self.mask_folder = mask_folder
        self.rectangle_mode = False
        self.begin = datetime.datetime.now()
        self.count = 0

        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.fig.subplots_adjust(left=-0.052)
        self.connexions = {
            "button_press_event": self.fig.canvas.mpl_connect("button_press_event", self.button_press_event),
            "key_press_event": self.fig.canvas.mpl_connect("key_press_event", self.key_press_event)
        }

        self.plotted_points = []
        self.plotted_lines = []
        self.plotted_polygons = []
        self.plotted_image = None

        self.current_filename = None
        self.current_image = None
        self.polygons_details = [[None, []]]
        
        self.new_image(self.filenames.pop(0))
        plt.tight_layout()
        plt.show()


def main(filenames="*.png", input_folder=INPUT_FOLDER, mask_folder=MASK_FOLDER):
    """
    Launch the annotater

    :param filenames: a path, as recognized by glob, corresponding to the filenames to segment.
    :type filenames: str. Optional. Default is "*.png".
    :param input_folder: name of the folder for the input files.
    :type input_folder: str. Optional.
    :param mask_folder: name of the folder for the output files.
    :type mask_folder: str. Optional.
    :return: Nothing, the files are created.
    """
    Annotater(filenames, input_folder, mask_folder)


if __name__ == '__main__':
    fire.Fire(main)
