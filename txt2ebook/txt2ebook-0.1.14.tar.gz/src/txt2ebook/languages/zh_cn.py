# Copyright (C) 2021,2022 Kian-Meng Ang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Config for Simplified Chinese (zh-cn) language."""

IDEOGRAPHIC_SPACE = "\u3000"
SPACE = "\u0020"
NUMS_WORDS = "零一二三四五六七八九十百千两"
FULLWIDTH_NUMS = "０１２３４５６７８９"

RE_NUMS = f"[.0-9{FULLWIDTH_NUMS}{NUMS_WORDS}]"
RE_VOLUMES = [
    f"^第{RE_NUMS}*[集卷册][^。~\n]*$",
    f"^卷{RE_NUMS}.*$",
]
RE_CHAPTERS = [
    f"^第{RE_NUMS}*[章篇回折].*$",
    "^[楔引]子[^，].*$",
    "^序[章幕曲]?$",
    "^前言.*$",
    "^[内容]*简介.*$",
    "^[号番]外[篇]?.*$",
    "^尾声$",
    "^终章.*$",
    "^后记.*$",
    "^文案.*$",
]

DEFAULT_RE_TITLE = r"书名：(.*)|【(.*)】|《(.*)》"
DEFAULT_RE_AUTHOR = r"作者：(.*)"
DEFAULT_RE_VOLUME_CHAPTER = "|".join(
    [
        "^(第.*[卷篇].*)[ ]*(第.*章.*$)",
    ]
)

DEFAULT_RE_VOLUME = "|".join(RE_VOLUMES)
DEFAULT_RE_CHAPTER = "|".join(RE_CHAPTERS)

STRUCTURE_NAMES = {
    "cover": "封面",
}
