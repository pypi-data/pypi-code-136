import napari
from arkitekt.apps.rekuest import ArkitektRekuest
from rekuest.structures.registry import StructureRegistry
from rekuest.widgets import SearchWidget
from fakts.fakts import Fakts
from fakts.grants.meta.failsafe import FailsafeGrant
from fakts.grants.remote.public_redirect_grant import PublicRedirectGrant
from koil.qt import QtRunner
from mikro.api.schema import (
    RepresentationVariety,
    Search_representationQuery,
    afrom_xarray,
    RepresentationFragment,
    aget_roi,
    from_xarray,
)
import mikro
from qtpy import QtWidgets
from qtpy import QtCore
from arkitekt.apps.connected import ConnectedApp
from koil.composition.qt import QtPedanticKoil
from herre.fakts import FaktsHerre
from arkitekt.qt.magic_bar import AppState, MagicBar
from rekuest.qt.builders import (
    QtInLoopActorBuilder,
    QtInLoopBuilder,
    QtPassFutureActorBuilder,
    QtPassFutureBuilder,
)
from mikro_napari.models.representation import RepresentationQtModel
from mikro_napari.widgets.dialogs.open_image import OpenImageDialog
from fakts.grants.remote.base import StaticDiscovery
import xarray as xr


SMLM_REPRESENTATIONS = SearchWidget(
    query="""
    query Search($search: String){
        options: representations(name: $search, tags: ["smlm"]){
            value: id
            label: name
        }
    }
    """,
    ward="mikro",
)  #


MULTISCALE_REPRESENTATIONS = SearchWidget(
    query="""
        query Search($search: String){
            options: representations(name: $search, derivedTags: ["multiscale"]){
                value: id
                label: name
            }
        }
        """,
    ward="mikro",
)


class MikroNapariWidget(QtWidgets.QWidget):
    emit_image: QtCore.Signal = QtCore.Signal(object)

    def __init__(self, viewer: napari.Viewer, app: ConnectedApp, *args, **kwargs):
        super(MikroNapariWidget, self).__init__(*args, **kwargs)

        self.viewer = viewer

        self.mylayout = QtWidgets.QVBoxLayout()

        self.app = app
        self.viewer.window.app = self.app

        self.representation_controller = RepresentationQtModel(self)

        self.magic_bar = MagicBar(self.app, dark_mode=True)
        self.magic_bar.app_up.connect(self.on_app_up)
        self.magic_bar.app_down.connect(self.on_app_down)

        self.upload_task = QtRunner(afrom_xarray)
        self.upload_task.errored.connect(self.on_error)
        self.upload_task.returned.connect(
            self.representation_controller.on_image_loaded
        )

        self.task = None
        self.stask = None

        self.open_image_button = QtWidgets.QPushButton("Open Image")
        self.open_image_button.clicked.connect(self.cause_image_load)
        self.open_image_button.setEnabled(False)

        self.upload_image_button = QtWidgets.QPushButton("Upload Image")
        self.upload_image_button.clicked.connect(self.cause_upload)
        self.upload_image_button.setEnabled(False)

        self.active_non_mikro_layers = []
        self.active_mikro_layers = []
        self.mylayout.addWidget(self.open_image_button)
        self.mylayout.addWidget(self.upload_image_button)
        self.mylayout.addWidget(self.magic_bar)

        self.setWindowTitle("My Own Title")
        self.setLayout(self.mylayout)

        self.viewer.layers.selection.events.active.connect(self.on_selection_changed)

        self.app.rekuest.register(builder=QtInLoopActorBuilder(), interfaces=["show"])(
            self.representation_controller.on_image_loaded
        )
        self.app.rekuest.register(builder=QtInLoopActorBuilder(), interfaces=["show"])(
            self.representation_controller.open_feature
        )
        self.app.rekuest.register(builder=QtInLoopActorBuilder(), interfaces=["show"])(
            self.representation_controller.open_metric
        )
        self.app.rekuest.register(builder=QtInLoopActorBuilder(), interfaces=["show"])(
            self.representation_controller.open_label
        )

        self.app.rekuest.register(builder=QtInLoopActorBuilder(), interfaces=["show"])(
            self.representation_controller.tile_images
        )
        self.app.rekuest.register(interfaces=["producer"])(self.upload_layer)
        self.app.rekuest.register(interfaces=["producer"])(
            self.representation_controller.stream_rois
        )

    def on_app_up(self):
        self.open_image_button.setEnabled(True)
        self.on_selection_changed()  # TRIGGER ALSO HERE

    def on_app_down(self):
        self.open_image_button.setEnabled(False)

    def on_selection_changed(self):
        self.active_non_mikro_layers = [
            layer
            for layer in self.viewer.layers.selection
            if not layer.metadata.get("mikro")
        ]
        self.active_mikro_layers = [
            layer
            for layer in self.viewer.layers.selection
            if layer.metadata.get("mikro")
        ]

        if self.active_non_mikro_layers and not self.active_mikro_layers:
            self.upload_image_button.setText(f"Upload Layer")
            self.upload_image_button.setEnabled(self.magic_bar.state == AppState.UP)
        else:
            self.upload_image_button.setText(f"Upload Layer")
            self.upload_image_button.setEnabled(False)

    async def upload_layer(self, name: str = "") -> RepresentationFragment:
        """Upload Napari Layer

        Upload the current image to the server.

        Args:
            name (str, optional): Overwrite the layer name. Defaults to None.

        Returns:
            RepresentationFragment: The uploaded image
        """
        if not self.active_non_mikro_layers:
            raise Exception("No active layer")

        image_layer = self.active_non_mikro_layers[0]

        variety = RepresentationVariety.VOXEL

        if image_layer.ndim == 2:
            if image_layer.rgb:
                xarray = xr.DataArray(image_layer.data, dims=list("xyc"))
                variety = RepresentationVariety.RGB
            else:
                xarray = xr.DataArray(image_layer.data, dims=list("xy"))

        if image_layer.ndim == 3:
            xarray = xr.DataArray(image_layer.data, dims=list("zxy"))

        if image_layer.ndim == 4:
            xarray = xr.DataArray(image_layer.data, dims=list("tzxy"))

        if image_layer.ndim == 5:
            xarray = xr.DataArray(image_layer.data, dims=list("tzxyc"))

        return await afrom_xarray(
            xarray, name=name or image_layer.name, variety=variety
        )

    def cause_upload(self):
        for image_layer in self.active_non_mikro_layers:
            variety = RepresentationVariety.VOXEL

            if image_layer.ndim == 2:
                if image_layer.rgb:
                    xarray = xr.DataArray(image_layer.data, dims=list("xyc"))
                    variety = RepresentationVariety.RGB
                else:
                    xarray = xr.DataArray(image_layer.data, dims=list("xy"))

            if image_layer.ndim == 3:
                xarray = xr.DataArray(image_layer.data, dims=list("zxy"))

            if image_layer.ndim == 4:
                xarray = xr.DataArray(image_layer.data, dims=list("tzxy"))

            if image_layer.ndim == 5:
                xarray = xr.DataArray(image_layer.data, dims=list("tzxyc"))

            self.upload_task.run(xarray, name=image_layer.name, variety=variety)
            self.upload_image_button.setText(f"Uploading {image_layer.name}...")
            self.upload_image_button.setEnabled(False)

    def on_upload_finished(self, image):
        self.on_selection_changed()

    def cause_image_load(self):

        rep_dialog = OpenImageDialog(self)
        x = rep_dialog.exec()
        if x:
            self.representation_controller.active_representation = (
                rep_dialog.selected_representation
            )

    def on_error(self, error):
        print(error)
