from pathlib import Path
from typing import Dict, Optional

from unfolded.map_sdk.map.base import (
    DEFAULT_MAP_STYLE,
    BasemapParams,
    BaseNonInteractiveMap,
)
from unfolded.map_sdk.transport.html import HTMLTransport

TEMPLATE_DIR = (Path(__file__).parent / ".." / "templates").resolve()


class HTMLMap(BaseNonInteractiveMap):
    transport: HTMLTransport

    def __init__(
        self,
        style: Optional[Dict] = None,
        basemaps: Optional[Dict] = None,
    ):

        if style:
            self.style = {**DEFAULT_MAP_STYLE, **style}
        else:
            self.style = DEFAULT_MAP_STYLE

        if basemaps:
            validated_basemaps = BasemapParams(**basemaps)
            self.basemaps = validated_basemaps.dict(by_alias=True, exclude_none=True)
        else:
            self.basemaps = {}

        self.transport = HTMLTransport()
        self.rendered = False

    def _repr_html_(self) -> str:
        return self.render()

    def render(self) -> str:
        return self.transport.render_template(style=self.style, basemaps=self.basemaps)
