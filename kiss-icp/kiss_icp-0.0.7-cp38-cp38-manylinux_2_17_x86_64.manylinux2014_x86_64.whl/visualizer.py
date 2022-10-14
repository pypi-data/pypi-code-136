from abc import ABC
import copy
from functools import partial
import importlib
import os
from typing import Callable, List

import numpy as np

YELLOW = np.array([1, 0.706, 0])
RED = np.array([128, 0, 0]) / 255.0
BLACK = np.array([0, 0, 0]) / 255.0


class StubVisualizer(ABC):
    def __init__(self):
        pass

    def update(self, source, keypoints, target_map, pose):
        pass


class RegistrationVisualizer(StubVisualizer):
    # Public Interaface ----------------------------------------------------------------------------
    def __init__(self):
        try:
            self.o3d = importlib.import_module("open3d")
        except ModuleNotFoundError as err:
            print(f'open3d is not installed on your system, run "pip install open3d"')
            exit(1)

        # Initialize GUI controls
        self.block_vis = True
        self.play_crun = False
        self.reset_bounding_box = True

        # Create data
        self.source = self.o3d.geometry.PointCloud()
        self.keypoints = self.o3d.geometry.PointCloud()
        self.target = self.o3d.geometry.PointCloud()

        # Initialize visualizer
        self.vis = self.o3d.visualization.VisualizerWithKeyCallback()
        self._register_key_callbacks()
        self._initialize_visualizer()

        # Visualization options
        self.render_map = True
        self.render_source = True
        self.render_keypoints = False
        self.global_view = False

    def update(self, source, keypoints, target_map, pose):
        target = target_map.point_cloud()
        self._update_geometries(source, keypoints, target, pose)
        while self.block_vis:
            self.vis.poll_events()
            self.vis.update_renderer()
            if self.play_crun:
                break
        self.block_vis = not self.block_vis

    # Private Interaface ---------------------------------------------------------------------------
    def _initialize_visualizer(self):
        w_name = self.__class__.__name__
        self.vis.create_window(window_name=w_name, width=1920, height=1080)
        self.vis.add_geometry(self.source)
        self.vis.add_geometry(self.keypoints)
        self.vis.add_geometry(self.target)
        self._set_black_background(self.vis)
        self.vis.get_render_option().point_size = 1
        print(
            f"{w_name} initialized. Press:\n"
            "\t[SPACE] to pause/start\n"
            "\t  [ESC] to exit\n"
            "\t    [N] to step\n"
            "\t    [F] to toggle on/off the frame\n"
            "\t    [K] to toggle on/off the subsbampled frame\n"
            "\t    [M] to toggle on/off the local map\n"
            "\t    [V] to toggle ego/global viewpoint\n"
            "\t    [C] to center the viewpoint"
        )

    def _register_key_callback(self, keys: List, callback: Callable):
        for key in keys:
            self.vis.register_key_callback(ord(str(key)), partial(callback))

    def _register_key_callbacks(self):
        self._register_key_callback(["Ā", "Q", "\x1b"], self._quit)
        self._register_key_callback([" "], self._start_stop)
        self._register_key_callback(["N"], self._next_frame)
        self._register_key_callback(["V"], self._toggle_view)
        self._register_key_callback(["C"], self._center_viewpoint)
        self._register_key_callback(["S"], self._toggle_source)
        self._register_key_callback(["F"], self._toggle_source)
        self._register_key_callback(["K"], self._toggle_keypoints)
        self._register_key_callback(["M"], self._toggle_map)
        self._register_key_callback(["B"], self._set_black_background)
        self._register_key_callback(["W"], self._set_white_background)

    def _set_black_background(self, vis):
        vis.get_render_option().background_color = [0.0, 0.0, 0.0]

    def _set_white_background(self, vis):
        vis.get_render_option().background_color = [1.0, 1.0, 1.0]

    def _quit(self, vis):
        print("Destroying Visualizer")
        vis.destroy_window()
        os._exit(0)

    def _next_frame(self, vis):
        self.block_vis = not self.block_vis

    def _start_stop(self, vis):
        self.play_crun = not self.play_crun

    def _toggle_source(self, vis):
        if self.render_keypoints:
            self.render_keypoints = False
            self.render_source = True
        else:
            self.render_source = not self.render_source
        return False

    def _toggle_keypoints(self, vis):
        if self.render_source:
            self.render_keypoints = True
            self.render_source = False
        else:
            self.render_keypoints = not self.render_keypoints

        return False

    def _toggle_map(self, vis):
        self.render_map = not self.render_map
        return False

    def _update_geometries(self, source, keypoints, target, pose):
        # Source hot frame
        if self.render_source:
            self.source.points = self.o3d.utility.Vector3dVector(source)
            self.source.paint_uniform_color(YELLOW)
            if self.global_view:
                self.source.transform(pose)
        else:
            self.source.points = self.o3d.utility.Vector3dVector()

        # Keypoints
        if self.render_keypoints:
            self.keypoints.points = self.o3d.utility.Vector3dVector(keypoints)
            self.keypoints.paint_uniform_color(YELLOW)
            if self.global_view:
                self.keypoints.transform(pose)
        else:
            self.keypoints.points = self.o3d.utility.Vector3dVector()

        # Target Map
        if self.render_map:
            target = copy.deepcopy(target)
            self.target.points = self.o3d.utility.Vector3dVector(target)
            if not self.global_view:
                self.target.transform(np.linalg.inv(pose))
        else:
            self.target.points = self.o3d.utility.Vector3dVector()

        self.vis.update_geometry(self.source)
        self.vis.update_geometry(self.keypoints)
        self.vis.update_geometry(self.target)
        if self.reset_bounding_box:
            self.vis.reset_view_point(True)
            self.reset_bounding_box = False

    def _toggle_view(self, vis):
        self.global_view = not self.global_view

    def _center_viewpoint(self, vis):
        vis.reset_view_point(True)
