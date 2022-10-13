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

"""Parse source text file into a book model."""

import argparse
import logging
from collections import OrderedDict
from dataclasses import dataclass, field
from importlib import import_module
from typing import Any, List, Tuple, Union

import cjkwrap
import regex as re

from txt2ebook.models import Book, Chapter, Volume

logger = logging.getLogger(__name__)


@dataclass
class Parser:
    """Parser class to massage and parse a text content."""

    raw_content: str = field()
    config: argparse.Namespace = field()

    def __init__(self, raw_content: str, config: argparse.Namespace) -> None:
        """Set the constructor for the Parser."""
        self.raw_content = raw_content
        self.config = config

        config_lang = config.language.replace("-", "_")
        self.langconf = import_module(f"txt2ebook.languages.{config_lang}")

    def __getattr__(self, key: str) -> Any:
        """Get a value of the config based on key name.

        Args:
            key(str): The key name of the config.

        Returns:
            Any: The value of a key, if found. Otherwise raise AttributeError
            exception.
        """
        if hasattr(self.config, key):
            return getattr(self.config, key)

        if hasattr(self.langconf, key):
            return getattr(self.langconf, key)

        raise AttributeError(key)

    def parse(self) -> Book:
        """Parse the content into volumes (optional) and chapters.

        Returns:
          txt2ebook.models.Book: The Book model
        """
        massaged_content = self.massage()
        (parsed_content, volumes, chapters) = self.parse_content(
            massaged_content
        )

        return Book(
            title=self.detect_book_title(),
            language=self.language,
            authors=self.detect_authors(),
            cover=self.cover,
            raw_content=self.raw_content,
            massaged_content=massaged_content,
            parsed_content=parsed_content,
            volumes=volumes,
            chapters=chapters,
            structure_names=self.STRUCTURE_NAMES,
        )

    def massage(self) -> str:
        """Massage the txt content.

        Returns:
          str: The book in parsed string
        """
        content = self.raw_content

        content = Parser.to_unix_newline(content)

        if self.re_delete:
            content = self.do_delete_regex(content)

        if self.re_replace:
            content = self.do_replace_regex(content)

        if self.re_delete_line:
            content = self.do_delete_line_regex(content)

        if self.width:
            content = self.do_wrapping(content)

        return content

    def get_regex(self, metadata: str) -> Union[List, str]:
        """Get the regex by the book metadata we want to parse and extract.

        Args:
          metadata(str): The type of the regex for each parser by language.

        Returns:
          str | list: The regex or list of regexs of the type.
        """
        regexs = getattr(self, f"re_{metadata}")
        if regexs:
            return regexs if metadata == "replace" else "|".join(regexs)

        return getattr(self, f"DEFAULT_RE_{metadata.upper()}")

    def detect_book_title(self) -> str:
        """Extract book title from the content of the txt file.

        Returns:
          str: The extracted book title
        """
        if isinstance(self.title, str):
            return self.title

        match = re.search(self.get_regex("title"), self.raw_content)
        if match:
            book_title = next(
                (title.strip() for title in match.groups() if title)
            )
            logger.info("Found book title: %s", book_title)
            return book_title

        logger.info("No book title found from file!")
        return ""

    def detect_authors(self) -> List[str]:
        """Extract author from the content of the txt file.

        Returns:
          list: A list of author names
        """
        if isinstance(self.author, list) and self.author:
            logger.info("Author set: %s", self.author)
            return self.author

        match = re.search(self.get_regex("author"), self.raw_content)
        if match:
            author = match.group(1).strip()
            logger.info("Found author: %s", author)
            return [author]

        logger.info("No author found from file!")
        return []

    @staticmethod
    def to_unix_newline(content: str) -> str:
        """Convert all other line ends to Unix line end.

        Args:
          content(str): The book content

        Returns:
          str: The formatted book content
        """
        return content.replace("\r\n", "\n").replace("\r", "\n")

    def do_delete_regex(self, content: str) -> str:
        """Remove words/phrases based on regex.

        Args:
          content(str): The book content

        Returns:
          str: The formatted book content
        """
        for delete_regex in self.get_regex("delete"):
            content = re.sub(
                re.compile(rf"{delete_regex}", re.MULTILINE), "", content
            )
        return content

    def do_replace_regex(self, content: str) -> str:
        """Replace words/phrases based on regex.

        Args:
          content(str): The book content

        Returns:
          str: The formatted book content
        """
        regex = self.get_regex("replace")
        if isinstance(regex, list):
            for search, replace in regex:
                content = re.sub(
                    re.compile(rf"{search}", re.MULTILINE),
                    rf"{replace}",
                    content,
                )

        return content

    def do_delete_line_regex(self, content: str) -> str:
        """Delete whole line based on regex.

        Args:
          content(str): The book content

        Returns:
          str: The formatted book content
        """
        for delete_line_regex in self.get_regex("delete_line"):
            content = re.sub(
                re.compile(rf"^.*{delete_line_regex}.*$", re.MULTILINE),
                "",
                content,
            )
        return content

    def do_wrapping(self, content: str) -> str:
        """Wrap or fill CJK text.

        Args:
            content (str): Massage book content

        Returns:
            str: Massage book content
        """
        logger.info("Wrapping paragraph to width: %s", self.width)

        paragraphs = []
        # We don't remove empty line and keep all formatting as it.
        for paragraph in content.split("\n"):
            paragraph = paragraph.strip()

            lines = cjkwrap.wrap(paragraph, width=self.width)
            paragraph = "\n".join(lines)
            paragraphs.append(paragraph)

        wrapped_content = "\n".join(paragraphs)
        return wrapped_content

    def parse_content(
        self, content: str
    ) -> Tuple[List, List[Volume], List[Chapter]]:
        """Parse the content into volumes (if exists) and chapters.

        Args:
          content(str): The book content

        Returns:
          tuple: The formatted book content, volumes (if exists), and chapters
        """
        (parsed_content, volumes) = self.parse_volumes_chapters(content)
        if parsed_content:
            return (parsed_content, volumes, [])

        (parsed_content, volumes) = self.parse_volumes(content)
        if parsed_content:
            return (parsed_content, volumes, [])

        (parsed_content, chapters) = self.parse_chapters(content)
        if parsed_content:
            return (parsed_content, [], chapters)

        return ([], [], [])

    def parse_volumes_chapters(
        self, content
    ):  # pylint: disable=too-many-locals
        """Split the content of txt file into volumes and chapters.

        The section header contains volume and chapter as shown:

            volume_title chapter_title

        Args:
          content(str): The book content

        Returns:
          tuple: A list of parsed volumes and volumes
        """
        regex = self.get_regex("volume_chapter")
        logger.info(regex)
        pattern = re.compile(regex, re.MULTILINE)

        headers = re.findall(pattern, content)
        logger.info("Found chapters: %s", len(headers))

        if not headers:
            return ([], [])

        volume_chapter_bodies = re.split(pattern, content)[1:]
        vcb = list(zip(*[volume_chapter_bodies[i::3] for i in range(3)]))

        parsed_content = OrderedDict()
        for key, *value in vcb:
            parsed_content.setdefault(key, []).append(tuple(value))

        volumes = []
        for vol, chps in parsed_content.items():
            chapters = []
            for title, body in chps:
                title = title.rstrip()
                paragraphs = self.parse_paragraphs(body, title)
                chapters.append(
                    Chapter(
                        title=title, raw_content=body, paragraphs=paragraphs
                    )
                )

            volumes.append(
                Volume(
                    title=vol,
                    raw_content="",
                    chapters=chapters,
                )
            )

        return (parsed_content, volumes)

    def parse_volumes(self, content):
        """Split the content of txt file into volumes and later by chapter.

        Args:
          content(str): The book content

        Returns:
          tuple: A list of parsed volumes and volumes
        """
        volume_pattern = re.compile(self.get_regex("volume"), re.MULTILINE)
        volume_headers = re.findall(volume_pattern, content)
        logger.info("Found volumes: %s", len(volume_headers))

        if not volume_headers:
            return ([], [])

        volume_bodies = re.split(volume_pattern, content)
        parsed_volumes = list(zip(volume_headers, volume_bodies[1:]))

        parsed_content = []
        volumes = []

        for volume_header, body in parsed_volumes:
            (parsed_body, chapters) = self.parse_chapters(body)
            if parsed_body:
                parsed_content.append((volume_header, parsed_body))
                volumes.append(
                    Volume(
                        title=volume_header,
                        raw_content=body,
                        chapters=chapters,
                    )
                )
            else:
                logger.error("Found 0 chapters for volume: %s", volume_header)

        return (parsed_content, volumes)

    def parse_chapters(
        self, content: str
    ) -> Tuple[List[Tuple[str, str]], List[Chapter]]:
        """Split the content of txt file into chapters by chapter regex.

        Args:
          content(str): The book content

        Returns:
          tuple: A list of parsed chapters and chapters
        """
        regex = re.compile(self.get_regex("chapter"), re.MULTILINE)
        headers = re.findall(regex, content)
        logger.info("Found chapters: %s", len(headers))

        if not headers:
            return ([], [])

        bodies = re.split(regex, content)
        parsed_chapters = list(zip(headers, bodies[1:]))

        chapters = []
        for title, body in parsed_chapters:
            title = title.rstrip()
            paragraphs = self.parse_paragraphs(body, title)
            chapters.append(
                Chapter(title=title, raw_content=body, paragraphs=paragraphs)
            )

        return (parsed_chapters, chapters)

    def parse_paragraphs(self, body: str, title: str) -> List[str]:
        """Split the body of text into list of individual paragraph.

        With assumptions of:
        - newline in UNIX format
        - each paragraph is separated by an empty line (two newlines)
        - resort to single newline if not paragraphs found

        Args:
          body(str): The body of a chapter
          title(str): The title of a chapter

        Returns:
          list: A list of paragraph of a chapter
        """
        # remove whitespaces (e.g.: newline) at the head/tail of string
        body = body.strip("\n")
        paragraphs = body.split(self.paragraph_separator)
        if len(paragraphs) == 1:
            logger.debug("one paragraph found for chapter: %s", title)
            paragraphs = body.split("\n")

        # remove empty string from parsed paragraphs
        return list(filter(None, paragraphs))
