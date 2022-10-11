from mikro_napari.widgets.main_widget import MikroNapariWidget
from arkitekt.apps.connected import ConnectedApp
from arkitekt.apps.rekuest import ArkitektRekuest
from fakts.fakts import Fakts
from fakts.grants.meta.failsafe import FailsafeGrant
from fakts.grants.remote.public_redirect_grant import PublicRedirectGrant
from herre.fakts.herre import FaktsHerre
from koil.composition.qt import QtPedanticKoil

class ArkitektPluginWidget(MikroNapariWidget):

    def __init__(self, viewer: 'napari.viewer.Viewer'):

        app = ConnectedApp(
            koil=QtPedanticKoil(parent=self),
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


        super(ArkitektPluginWidget, self).__init__(viewer, app)


        app.enter()



