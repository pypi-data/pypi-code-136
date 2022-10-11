from typing import Dict, List, Optional
from qtpy import QtCore, QtWidgets
from arkitekt.apps.connected import ConnectedApp
from koil.qt import QtFuture, QtRunner, QtGeneratorRunner
from mikro.api.schema import (
    InputVector,
    MetricFragment,
    LabelFragment,
    FeatureFragment,
    ROIFragment,
    ListROIFragment,
    RepresentationFragment,
    RepresentationVariety,
    RoiTypeInput,
    Watch_roisSubscriptionRois,
    acreate_roi,
    get_representation,
    aget_rois,
    awatch_rois,
    create_roi,
)
from mikro_napari.api.schema import (
    DetailLabelFragment,
    aget_label_for,
    delete_roi,
)
import pandas as pd

import dask.array as da
import xarray as xr
import napari
from napari.layers.shapes._shapes_constants import Mode
import numpy as np

from mikro_napari.utils import NapariROI, convert_roi_to_napari_roi


DESIGN_MODE_MAP = {
    Mode.ADD_RECTANGLE: RoiTypeInput.RECTANGLE,
    Mode.ADD_ELLIPSE: RoiTypeInput.ELLIPSIS,
    Mode.ADD_LINE: RoiTypeInput.LINE,
}

SELECT_MODE_MAP = {
    Mode.DIRECT: "direct",
}


DOUBLE_CLICK_MODE_MAP = {
    Mode.ADD_POLYGON: RoiTypeInput.POLYGON,
    Mode.ADD_PATH: RoiTypeInput.PATH,
}


class AskForRoi(QtWidgets.QWidget):
    def __init__(
        self,
        controller,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.button = QtWidgets.QPushButton("All Rois Marked")
        self.button.clicked.connect(self.on_done)
        self.mylayout = controller.widget.mylayout

    def ask(self, qt_generator):
        self.qt_generator = qt_generator
        self.mylayout.addWidget(self.button)
        self.mylayout.update()

    def on_done(self) -> None:
        self.qt_generator.stop()
        self.mylayout.removeWidget(self.button)
        self.button.setParent(None)
        self.mylayout.update()


class RepresentationQtModel(QtCore.QObject):
    rep_changed = QtCore.Signal(RepresentationFragment)

    def __init__(self, widget, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.widget = widget
        self.app: ConnectedApp = self.widget.app
        self.viewer: napari.Viewer = self.widget.viewer

        self.get_rois_query = QtRunner(aget_rois)
        self.get_rois_query.returned.connect(self.on_rois_loaded)
        self.get_rois_query.errored.connect(print)

        self.create_rois_runner = QtRunner(acreate_roi)
        self.create_rois_runner.returned.connect(print)
        self.create_rois_runner.errored.connect(print)

        self.watch_rois_subscription = QtGeneratorRunner(awatch_rois)
        self.watch_rois_subscription.yielded.connect(self.on_rois_updated)
        self.watch_rois_subscription.errored.connect(print)

        self.get_label_query = QtRunner(aget_label_for)
        self.get_label_query.returned.connect(self.on_label_loaded)
        self.get_label_query.errored.connect(print)
        self.rep_changed.connect(self.set_active_representation)

        self._active_representation = None
        self.stream_roi_generator = None
        self._watchroistask = None
        self._getroistask = None
        self._getlabeltask = None

        self.ask_roi_dialog = AskForRoi(self)

        self._image_layer = None
        self._roi_layer = None
        self.roi_state: Dict[str, ListROIFragment] = {}

    @property
    def active_representation(self) -> Optional[RepresentationFragment]:
        return self._active_representation

    @active_representation.setter
    def active_representation(self, value: RepresentationFragment):
        self.rep_changed.emit(value)

    def set_active_representation(self, value: RepresentationFragment):
        if self._getroistask and not self._getroistask.done():
            self._getroistask.cancel()
            self._getroistask.result(swallow_cancel=True)

        if self._watchroistask and not self._watchroistask.done():
            self._watchroistask.cancel()
            self._watchroistask.result(swallow_cancel=True)

        self._getroistask = self.get_rois_query.run(representation=value.id)
        self._watchroistask = self.watch_rois_subscription.run(representation=value.id)
        self._active_representation = value

        if self._image_layer:
            del self._image_layer
            self._image_layer = None

        if self._roi_layer:
            del self._roi_layer
            self._roi_layer = None

        scale = None

        print(value.omero)

        if value.omero:
            if value.omero.scale:
                scale = value.omero.scale
            else:
                phys = value.omero.physical_size
                if phys:
                    scale = [
                        phys.c or 1,
                        phys.t or 1,
                        phys.z or 1,
                        phys.x or 1,
                        phys.y or 1,
                    ]

        if value.variety == RepresentationVariety.RGB:
            self._image_layer = self.viewer.add_image(
                value.data.transpose(*list("tzxyc")),
                metadata={"mikro": True, "representation": value, "type": "IMAGE"},
                scale=scale,
            )
        else:
            self._image_layer = self.viewer.add_image(
                value.data.transpose(*list("ctzxy")),
                metadata={"mikro": True, "representation": value, "type": "IMAGE"},
                scale=scale,
            )

        print(scale)

        self._image_layer.mouse_drag_callbacks.append(self.on_drag_image_layer)
        self._image_layer.name = f"{value.name} (ID: {value.id})"

    def on_image_loaded(self, rep: RepresentationFragment):
        """Show on Napari

        Loads the image into the viewer

        Args:
            rep (RepresentationFragment): The Image
        """
        self.active_representation = rep

    def open_metric(self, metric: MetricFragment):
        """Open a metric

        Loads the metric into the viewer

        Args:
            rep (RepresentationFragment): The Image
        """
        self.active_representation = get_representation(metric.rep.id)

    def open_label(self, label: LabelFragment):
        """Show on Napari

        Loads the label into the viewer

        Args:
            rep (RepresentationFragment): The Image
        """
        self.active_representation = get_representation(label.representation.id)

    def open_feature(self, rep: FeatureFragment):
        """Open Feature

        Loads the feature into the viewer

        Args:
            rep (RepresentationFragment): The Image
        """
        self.active_representation = get_representation(rep.label.representation.id)

    def tile_images(self, reps: List[RepresentationFragment]):
        """Tile Images on Napari

        Loads the images and tiles them into the viewer

        Args:
            reps (List[RepresentationFragment]): The Image
        """

        shape_array = np.array([np.array(rep.data.shape[:4]) for rep in reps])
        max_shape = np.max(shape_array, axis=0)

        cdata = []
        for rep in reps:
            data = da.zeros(list(max_shape) + [rep.data.shape[4]])
            data[
                : rep.data.shape[0],
                : rep.data.shape[1],
                : rep.data.shape[2],
                : rep.data.shape[3],
                :,
            ] = rep.data
            cdata.append(data)

        x = da.concatenate(cdata, axis=-1).squeeze()
        name = " ".join([rep.name for rep in reps])

        self.viewer.add_image(
            x,
            name=name,
            metadata={"mikro": True, "type": "IMAGE"},
            scale=reps[0].omero.scale if reps[0].omero else None,
        )

    async def stream_rois(self, rep: RepresentationFragment) -> ROIFragment:
        """Stream ROIs

        Asks the user to mark rois on the image, once user deams done, the rois are returned

        Args:
            rep (RepresentationFragment): The Image

        Returns:
            rois (List[RoiFragment]): The Image
        """
        self.active_representation = rep
        self.stream_roi_generator = QtGenerator()
        self.ask_roi_dialog.ask(self.stream_roi_generator)

        async for roi in self.stream_roi_generator:
            yield roi

        self.stream_roi_generator = None

    def on_label_loaded(self, label: DetailLabelFragment):
        """Shows beauitful Images

        Loads the image into the viewer

        Args:
            rep (RepresentationFragment): The Image
        """
        print("This is the label", label)

    def on_rois_loaded(self, rois: List[ListROIFragment]):
        self.roi_state = {roi.id: roi for roi in rois}
        self.update_roi_layer()

    def on_rois_updated(self, ev: Watch_roisSubscriptionRois):
        if ev.create:
            self.roi_state[ev.create.id] = ev.create
            if self.stream_roi_generator:
                self.stream_roi_generator.next(ev.create)

        if ev.delete:
            del self.roi_state[ev.delete]

        self.update_roi_layer()

    def on_drag_image_layer(self, layer, event):
        while event.type != "mouse_release":
            yield

        print("Fired")
        print(self.active_representation.variety)
        if self.active_representation.variety == RepresentationVariety.MASK:
            if self._getlabeltask and not self._getlabeltask.done():
                self._getlabeltask.cancel(wait=True)

            value = layer.get_value(event.position)
            print(value)
            if value:
                self._getlabeltask = self.get_label_query.run(
                    representation=self.active_representation.id, instance=int(value)
                )

    def on_drag_roi_layer(self, layer, event):
        while event.type != "mouse_release":
            yield

        if layer.mode in SELECT_MODE_MAP:
            print(self._roi_layer.selected_data)
            for i in self._roi_layer.selected_data:
                napari_roi = self._napari_rois[i]
                self.viewer.window.sidebar.select_roi(napari_roi)

        if layer.mode in DESIGN_MODE_MAP:
            if len(self._roi_layer.data) > len(self._napari_rois):
                t, z, c = layer.position[:3]

                self.create_rois_runner.run(
                    representation=self._active_representation.id,
                    vectors=InputVector.list_from_numpyarray(
                        self._roi_layer.data[-1], t=t, z=z, c=c
                    ),
                    type=DESIGN_MODE_MAP[layer.mode],
                )

        if len(self._roi_layer.data) < len(self._napari_rois):
            there_rois = set([f for f in self._roi_layer.features["roi"]])
            state_rois = set([f.id for f in self._napari_rois])
            difference_rois = state_rois - there_rois
            for roi_id in difference_rois:
                delete_roi(roi_id)

    def on_double_click_roi_layer(self, layer, event):
        print("Fired")
        print(self._roi_layer.features)
        if layer.mode in DOUBLE_CLICK_MODE_MAP:
            if len(self._roi_layer.data) > len(self._napari_rois):
                t, z, c = layer.position[:3]

                self.create_rois_runner.run(
                    representation=self._active_representation.id,
                    vectors=InputVector.list_from_numpyarray(
                        self._roi_layer.data[-1], t=t, z=z, c=c
                    ),
                    type=DOUBLE_CLICK_MODE_MAP[layer.mode],
                )

    def print(self, *args, **kwargs):
        print(*args, **kwargs)

    def update_roi_layer(self):

        if not self._roi_layer:

            self._roi_layer = self.viewer.add_shapes(
                metadata={
                    "mikro": True,
                    "type": "ROIS",
                    "representation": self._active_representation,
                }
            )
            self._roi_layer.mouse_drag_callbacks.append(self.on_drag_roi_layer)
            self._roi_layer.mouse_double_click_callbacks.append(
                self.on_double_click_roi_layer
            )

        self._napari_rois: List[NapariROI] = list(
            filter(
                lambda x: x is not None,
                [convert_roi_to_napari_roi(roi) for roi in self.roi_state.values()],
            )
        )

        self._roi_layer.data = []
        self._roi_layer.name = f"ROIs for {self._active_representation.name}"

        for i in self._napari_rois:
            self._roi_layer.add(
                i.data,
                shape_type=i.type,
                edge_width=1,
                edge_color="white",
                face_color=i.color,
            )

        self._roi_layer.features = {"roi": [r.id for r in self._napari_rois]}
