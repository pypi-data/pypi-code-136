from arkitekt.apps.connected import ConnectedApp
from arkitekt.apps.rekuest import ArkitektRekuest
from fakts.fakts import Fakts
from fakts.grants.meta.failsafe import FailsafeGrant
from fakts.grants.remote.public_redirect_grant import PublicRedirectGrant
from herre.fakts.herre import FaktsHerre
from koil.composition.qt import QtPedanticKoil
from mikro_napari.widgets.main_widget import MikroNapariWidget

import napari
import argparse
from skimage.data import astronaut

from mikro_napari.widgets.sidebar.sidebar import SidebarWidget


def main(**kwargs):
    viewer = napari.Viewer()

    app = ConnectedApp(
        rekuest=ArkitektRekuest(),
        fakts=Fakts(
            subapp="napari",
            grant=FailsafeGrant(
                grants=[
                    PublicRedirectGrant(name="Napari", scopes=["openid"]),
                ]
            ),
            assert_groups={"mikro", "arkitekt"},
        ),
        herre=FaktsHerre(),
    )

    widget = MikroNapariWidget(viewer, app, **kwargs)
    sidebar = SidebarWidget(viewer, app, **kwargs)
    viewer.window.add_dock_widget(widget, area="left", name="Mikro")
    viewer.window.add_dock_widget(sidebar, area="right", name="Mikro")
    # viewer.add_image(astronaut(), name="astronaut")

    with app:
        napari.run()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config", help="Which config file to use", default="bergen.yaml", type=str
    )
    args = parser.parse_args()

    main(config_path=args.config)
