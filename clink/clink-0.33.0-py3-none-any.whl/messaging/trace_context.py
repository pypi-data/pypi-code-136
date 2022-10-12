import collections
import dataclasses
import logging
import re
import unicodedata
import uuid
from typing import ClassVar, Dict, Pattern


__all__ = ["TraceParent", "TraceState"]


logger = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class TraceParent:
    """Partial implementation of TraceParent header value from Trace Context
    Level 2.

    https://w3c.github.io/trace-context/#traceparent-header

    This software or document includes material copied from or derived from
    `Trace Context Level 2 <https://w3c.github.io/trace-context/>`_.
    Copyright © 2021 W3C® (MIT, ERCIM, Keio, Beihang).
    """

    version: str = "00"

    trace_id: str = dataclasses.field(default_factory=lambda: uuid.uuid4().hex)

    parent_id: str = dataclasses.field(
        default_factory=lambda: uuid.uuid4().hex[16:]
    )

    trace_flags: str = "00000000"

    _header_format: ClassVar[Pattern] = re.compile(
        r"^(?P<version>00)-"
        r"(?P<trace_id>[0-9a-f]{32})-"
        r"(?P<parent_id>[0-9a-f]{16})-"
        r"(?P<trace_flags>(?:[0-1]{2}){,4})$"
    )

    def __str__(self) -> str:
        return "-".join(
            [self.version, self.trace_id, self.parent_id, self.trace_flags]
        )

    @classmethod
    def from_string(class_, value: str) -> "TraceParent":
        match = class_._header_format.match(value)
        if match:
            return class_(**match.groupdict())
        else:
            raise ValueError("Not a valid traceparent string format.")

    def to_string(self) -> str:
        return str(self)


class TraceState(collections.OrderedDict):
    """Partial implementation of TraceState header value from Trace Context
    Level 2.

    https://w3c.github.io/trace-context/#tracestate-header

    This software or document includes material copied from or derived from
    `Trace Context Level 2 <https://w3c.github.io/trace-context/>`_.
    Copyright © 2021 W3C® (MIT, ERCIM, Keio, Beihang).
    """

    # TODO: Key/value validation.
    # TODO: There can be a maximum of 32 list-members.

    _header_format: ClassVar[Pattern] = re.compile(
        r"^\s*(?P<key>[0-9a-z]{1}[0-9a-z_\-\*/\@]{,255})="
        r"(?P<value>(?:(?![,=])[\x20-\x7e])*(?:(?![,=\s])[\x20-\x7e]){1})\s*$"
    )

    def __setitem__(self, key: str, value: str) -> None:
        # When setting or updating an item, first remove it so that it is added
        # to the end of the dict.
        if key in self:
            del self[key]
        super().__setitem__(key, value)

    def __str__(self) -> str:
        items = [f"{key}={value}" for key, value in self.items()]
        items.reverse()
        return ",".join(items)

    @classmethod
    def from_string(class_, value: str) -> "TraceState":
        data: Dict[str, str] = {}
        items = list(filter(None, value.split(",")))
        items.reverse()

        for item in items:
            match = class_._header_format.match(item)
            if match:
                key, value = match.groups()
                data.update({key: value.rstrip()})
            else:
                logger.warning(
                    f'"{item}" is not a valid tracestate string format.'
                )
        return class_(**data)

    @staticmethod
    def slugify(value: str) -> str:
        """
        Convert to ASCII. Convert spaces or repeated
        dashes to single dashes. Remove characters that aren't 0-9, a-z, @,
        asterisks, underscores, or hyphens. Convert to lowercase. Also strip
        leading and trailing whitespace, dashes, and underscores.

        Adapted from
        https://github.com/django/django/blob/3.2.2/django/utils/text.py

        Copyright (c) Django Software Foundation and individual contributors.
        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are
        met:

            1. Redistributions of source code must retain the above copyright
            notice, this list of conditions and the following disclaimer.

            2. Redistributions in binary form must reproduce the above
            copyright notice, this list of conditions and the following
            disclaimer in the documentation and/or other materials provided
            with the distribution.

            3. Neither the name of Django nor the names of its contributors may
            be used to endorse or promote products derived from this software
            without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
        IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
        TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
        PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
        OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
        SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
        LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
        DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
        THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
        OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
        """
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
        value = re.sub(r"[^0-9a-z_\-\*/\@\.\s]", "", value.lower())
        value = re.sub(r"[\.\-\s]+", "-", value).strip("-_")
        return value

    def to_string(self) -> str:
        return str(self)
