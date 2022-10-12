from abc import ABC
from pathlib import Path
from typing import Mapping, Optional, Union

from .base_session import BaseSessionBound
from .empty_mapping import EMPTY_MAPPING


class Plugin(ABC):
    def activate(self) -> None:  # pylint: disable=no-self-use
        """Activate the plugin.

        It can be used to monkey patch the public API to plug the real functions.
        """
        ...

    def init_session(  # pylint: disable=no-self-use,unused-argument
        self, session: BaseSessionBound, /
    ) -> None:
        """Handle newly initialized session."""
        ...

    @property
    def app_extensions(self) -> Mapping[str, Union[str, Path]]:
        """The app extensions contributed by the plugin to be added to the session configuration."""
        return EMPTY_MAPPING

    @property
    def jar_path(self) -> Optional[Path]:
        """The path to the plugin's JAR.

        When not ``None``, the JAR will be added to the classpath of the Java process.
        """
        return None
