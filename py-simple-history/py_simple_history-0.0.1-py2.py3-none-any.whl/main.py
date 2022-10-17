#!/usr/bin/env python
"""A super simple history tracking class / mixin"""

from collections import deque


class _history_object:
    """Object to hold history data. Not meant to be instantiated directly."""

    __slots__ = ["id", "data"]

    def __init__(self, id: str, data):
        self.id, self.data = str(id), data

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id


class history_mixin:
    """Abstract mixin to add simple history-tracking to an object."""

    __slots__ = ["history", "_index", "_uid"]

    def __init__(self, start_data):
        self._uid, self._index, self.history = 0, 0, deque()
        self.history.append(_history_object(self._get_uid(), start_data))

    def _get_uid(self):
        """Internal function to get unique id per history."""
        self._uid += 1
        return self._uid - 1

    def add_history(self, data):
        """Add a history point. Clears any undone data history points."""
        while self._index < len(self.history) - 1:
            self.history.pop()  # Clear old timeline
        self.history.append(_history_object(uid := self._get_uid(), data))
        self._index = len(self.history) - 1
        return uid

    def undo(self):
        """Undoes history one step if possible."""
        if self._index > 0:
            self._index -= 1
        return self.history[self._index].data

    def redo(self):
        """Redoes history one step if possible."""
        if self.history_index == len(self.history) - 1:
            return
        self.history_index += 1
        return self.history[self._index].data

    def clear_history(self, data=None):
        """Clears history. Sets a new history point, if no data specified uses the current data point."""
        if not data:
            data = self.history[self._index]
        self.history = deque()
        self._index = 0
        self.history.append(_history_object(0, data))
