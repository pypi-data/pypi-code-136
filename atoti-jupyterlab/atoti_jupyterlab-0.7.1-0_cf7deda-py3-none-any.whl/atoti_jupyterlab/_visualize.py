from __future__ import annotations

from typing import Optional

from atoti_core import BaseSessionBound


def visualize(self: BaseSessionBound, name: Optional[str] = None) -> None:  # noqa: D417
    """Display an atoti widget to explore the session interactively.

    Note:
        This method requires the :mod:`atoti-jupyterlab <atoti_jupyterlab>` plugin.

    The widget state will be stored in the cell metadata.
    This state should not have to be edited but, if desired, it can be found in JupyterLab by opening the "Notebook tools" sidebar and expanding the "Advanced Tools" section.

    Args:
        name: The name to give to the widget.
    """
    self._widget_manager.display_widget(self, name)  # type: ignore
