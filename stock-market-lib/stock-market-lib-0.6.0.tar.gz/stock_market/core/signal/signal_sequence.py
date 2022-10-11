import json
from heapq import merge

from simputils.algos import is_sorted

from .signal import Signal


class SignalSequence:
    def __init__(self, signals=None):
        if signals is None:
            self.__signals = []
        else:
            self.__signals = signals
            assert is_sorted(signals, lambda s: s.date)

    @property
    def signals(self):
        return self.__signals

    def signals_since(self, date):
        """
        Returns all signals since the given date.
        The given date is not included.
        """
        return SignalSequence([s for s in self.signals if s.date > date])

    def __str__(self):
        signals_string = ", ".join(map(str, self.signals))
        return f"SignalSequence({signals_string})"

    def __repr__(self):
        signals_string = ", ".join(map(repr, self.signals))
        return f"SignalSequence({signals_string})"

    def __eq__(self, other):
        if not isinstance(other, SignalSequence):
            return False
        return self.signals == other.signals

    def to_json(self):
        return json.dumps([s.to_json() for s in self.signals])

    @staticmethod
    def from_json(json_str):
        return SignalSequence([Signal.from_json(s) for s in json.loads(json_str)])


def add_signal(sequence, signal):
    assert not sequence.signals or signal.date >= sequence.signals[-1].date, str(
        (sequence.signals, signal)
    )
    signals = sequence.signals.copy()
    signals.append(signal)
    return SignalSequence(signals)


def merge_signals(*signal_sequences):
    for signals in signal_sequences:
        assert is_sorted(signals.signals, lambda s: s.date)
    return SignalSequence(
        list(merge(*map(lambda s: s.signals, signal_sequences), key=lambda s: s.date))
    )
