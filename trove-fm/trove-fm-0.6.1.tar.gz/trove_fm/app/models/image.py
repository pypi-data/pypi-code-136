
"""
TroveFM is an online store and headless CMS.

Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from datetime import datetime
from enum import Enum, IntEnum
from typing import Optional

from pydantic import HttpUrl


from trove_fm.app.models.core import CoreModel, DateTimeModelMixin, IDModelMixin
from trove_fm.app.models.profile import PersonProfileCreate, PersonProfilePublic


class ImageBase(CoreModel):
    url: HttpUrl
    length: int
    width: int
    resolution: int
    alt_text: Optional[str]
    date_added: datetime


class AvatarImage(ImageBase):
    pass


class ProductImage(ImageBase):
    pass


class BarcodeImage(ImageBase):
    pass
