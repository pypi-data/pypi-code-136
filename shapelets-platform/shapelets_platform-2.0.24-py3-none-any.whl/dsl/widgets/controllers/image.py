# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
import base64

from dataclasses import dataclass
from io import BytesIO
from matplotlib.figure import Figure
from pathlib import Path
from typing import Union, Tuple, Optional

from os.path import isfile as file_exists
from shapelets.dsl.widgets import Widget, AttributeNames, StateControl


@dataclass
class Image(StateControl):
    img: Optional[Union[str, bytes, Path, Figure]] = None
    caption: Optional[str] = None
    placeholder: Optional[Union[str, bytes, Path]] = None


class ImageWidget(Image, Widget):
    def __init__(self,
                 img: Optional[Union[str, bytes, Path, Figure]] = None,
                 caption: Optional[str] = None,
                 placeholder: Optional[Union[str, bytes, Path]] = None,
                 **additional):

        Widget.__init__(self, Image.__name__, **additional)
        Image.__init__(self, img, caption, placeholder)
        self._parent_class = Image.__name__
        self._compatibility: Tuple = (str.__name__, bytes.__name__, Path.__name__, Figure.__name__, Image.__name__)

    def to_dict_widget(self):
        image_dict = Widget.to_dict_widget(self)
        # Widget providers are used when the value of a different widget must be set inside an attribute.
        _widget_providers = []
        if self.img is not None:
            if isinstance(self.img, str):
                # Reading image from local PATH
                if file_exists(self.img):
                    file = open(self.img, 'rb')
                    buffer = file.read()
                    image_data = base64.b64encode(buffer).decode('utf-8')

                    image_dict[AttributeNames.PROPERTIES.value].update(
                        {AttributeNames.DATA.value: f"{image_data}"}
                    )
                else:
                    raise FileNotFoundError(f"The file {self.img} does not exist")
            elif isinstance(self.img, Path):
                if self.img.exists():
                    file = open(self.img, 'rb')
                    buffer = file.read()
                    image_data = base64.b64encode(buffer).decode('utf-8')

                    image_dict[AttributeNames.PROPERTIES.value].update(
                        {AttributeNames.DATA.value: f"{image_data}"}
                    )
                else:
                    raise FileNotFoundError(f"The file {self.img} does not exist")
            elif isinstance(self.img, bytes):
                image_data = base64.b64encode(self.img).decode("utf-8")

                image_dict[AttributeNames.PROPERTIES.value].update(
                    {AttributeNames.DATA.value: f"{image_data}"}
                )
            elif isinstance(self.img, Figure):
                bio = BytesIO()
                # TODO: pass information from self._additional to savefig function
                self.img.savefig(bio, format="png", bbox_inches='tight')
                image_data = base64.b64encode(bio.getvalue()).decode("utf-8")

                image_dict[AttributeNames.PROPERTIES.value].update(
                    {AttributeNames.DATA.value: f"{image_data}"}
                )
            elif isinstance(self.img, Widget):
                target = {"id": self.img.widget_id, "target": "img"}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Image value not allow")

        if self.placeholder is None:
            currentDirectory = Path(__file__).parent.resolve()
            dataDirectory = currentDirectory.joinpath("resources")
            placeholder_img = dataDirectory / "placeholder.jpg"
            self.placeholder = placeholder_img

        if isinstance(self.placeholder, str):
            # Reading image from local PATH
            if file_exists(self.placeholder):
                file = open(self.placeholder, 'rb')
                buffer = file.read()
                image_data = base64.b64encode(buffer).decode('utf-8')

                image_dict[AttributeNames.PROPERTIES.value].update(
                    {AttributeNames.PLACEHOLDER.value: f"{image_data}"}
                )
            else:
                raise FileNotFoundError(f"The file {self.placeholder} does not exist")
        elif isinstance(self.placeholder, Path):
            if self.placeholder.exists():
                file = open(self.placeholder, 'rb')
                buffer = file.read()
                image_data = base64.b64encode(buffer).decode('utf-8')

                image_dict[AttributeNames.PROPERTIES.value].update(
                    {AttributeNames.PLACEHOLDER.value: f"{image_data}"}
                )
            else:
                raise FileNotFoundError(f"The file {self.placeholder} does not exist")
        elif isinstance(self.placeholder, bytes):
            image_data = base64.b64encode(self.placeholder).decode("utf-8")

            image_dict[AttributeNames.PROPERTIES.value].update(
                {AttributeNames.PLACEHOLDER.value: f"{image_data}"}
            )

        if self.caption is not None:
            if isinstance(self.caption, str):
                image_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.CAPTION.value: self.caption
                })
            elif isinstance(self.caption, Widget):
                target = {"id": self.caption.widget_id, "target": "caption"}
                _widget_providers.append(target)
            else:
                raise ValueError(f"Error Widget {self.widget_type}: Caption value should be a string or another widget")

        if _widget_providers:
            self.add_widget_providers(image_dict, _widget_providers)

        return image_dict
