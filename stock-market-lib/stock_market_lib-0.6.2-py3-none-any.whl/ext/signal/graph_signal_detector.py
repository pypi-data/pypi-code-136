import copy
import datetime as dt
import json
from enum import Enum

from simputils.functional import Mutable
from transitions import State
from transitions.extensions.markup import MarkupMachine

from stock_market.common.json_mixins import SingleAttributeJsonMixin
from stock_market.core import (
    Sentiment,
    Signal,
    SignalDetector,
    SignalSequence,
    add_signal,
    merge_signals,
)


class EnterOrExit(SingleAttributeJsonMixin, Enum):
    @classmethod
    @property
    def JSON_ATTRIBUTE_NAME(cls):
        return "value"

    @classmethod
    @property
    def JSON_ATTRIBUTE_TYPE(cls):
        return "string"

    ENTER = "ENTER"
    EXIT = "EXIT"


class GraphSignalDetectorBuilder:
    def __init__(
        self,
        identifier,
        name=None,
        detectors=None,
        state_descriptions=None,
        initial_state=None,
        signal_descriptions=None,
        transitions=None,
    ):
        self.id = identifier
        self.name = name
        self.detectors = [] if detectors is None else detectors
        self.state_descriptions = (
            [] if state_descriptions is None else state_descriptions
        )
        self.initial_state = initial_state
        self.signal_descriptions = (
            [] if signal_descriptions is None else signal_descriptions
        )
        self.transitions = [] if transitions is None else transitions

    def set_name(self, name):
        builder = copy.deepcopy(self)
        builder.name = name
        return builder

    def add_detector(self, detector):
        assert detector not in self.detectors
        builder = copy.deepcopy(self)
        builder.detectors.append(detector)
        return builder

    def add_state(self, state_description):
        assert state_description not in self.state_descriptions
        builder = copy.deepcopy(self)
        builder.state_descriptions.append(state_description)
        return builder

    def set_initial_state(self, initial_state):
        assert initial_state in self.state_descriptions
        builder = copy.deepcopy(self)
        builder.initial_state = initial_state
        return builder

    def add_signal_description(self, signal_state, sentiment, enter_or_exit):
        assert signal_state in self.state_descriptions
        signal_description = (signal_state, sentiment, enter_or_exit)
        assert signal_description not in self.signal_descriptions
        builder = copy.deepcopy(self)
        builder.signal_descriptions.append(signal_description)
        return builder

    def add_transition(self, source, dest, trigger):
        assert source in self.state_descriptions
        assert dest in self.state_descriptions
        assert trigger in [d.id for d in self.detectors]

        builder = copy.deepcopy(self)
        builder.transitions.append({"source": source, "dest": dest, "trigger": trigger})
        return builder

    @staticmethod
    def __create_state(state_description, signal_descriptions):
        def __get_signal_factory(sentiment):
            if sentiment == Sentiment.BULLISH:
                return Model.add_bullish_signal
            elif sentiment == Sentiment.BEARISH:
                return Model.add_bearish_signal
            assert sentiment == Sentiment.NEUTRAL
            return Model.add_neutral_signal

        enters = []
        exits = []
        assert signal_descriptions is not None and len(signal_descriptions) > 0
        for state, sentiment, enter_or_exit in signal_descriptions:
            if state == state_description:
                if enter_or_exit == EnterOrExit.ENTER:
                    enters.append(__get_signal_factory(sentiment))
                else:
                    assert enter_or_exit == EnterOrExit.EXIT
                    exits.append(__get_signal_factory(sentiment))
        return State(
            state_description,
            on_enter=enters,
            on_exit=exits,
            ignore_invalid_triggers=True,
        )

    @staticmethod
    def __create_states(state_descriptions, signal_descriptions):
        assert state_descriptions is not None and len(state_descriptions) > 0
        return [
            GraphSignalDetectorBuilder.__create_state(s, signal_descriptions)
            for s in state_descriptions
        ]

    @staticmethod
    def __create_machine(
        state_descriptions, initial_state, signal_descriptions, transitions
    ):
        assert initial_state is not None
        transitions = [t | {"trigger": str(t["trigger"])} for t in transitions]
        return MarkupMachine(
            model=[],
            states=GraphSignalDetectorBuilder.__create_states(
                state_descriptions, signal_descriptions
            ),
            initial=initial_state,
            transitions=transitions,
        )

    def build(self):
        assert self.name is not None
        assert self.detectors is not None
        return GraphSignalDetector(
            self.id,
            self.name,
            self.detectors,
            GraphSignalDetectorBuilder.__create_machine(
                self.state_descriptions,
                self.initial_state,
                self.signal_descriptions,
                self.transitions,
            ),
        )

    def to_json(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "signal_detectors": [
                    {"name": sd.NAME(), "config": sd.to_json()} for sd in self.detectors
                ],
                "state_descriptions": self.state_descriptions,
                "initial_state": self.initial_state,
                "signal_descriptions": [
                    (state, sentiment.to_json(), enter_or_exit.to_json())
                    for state, sentiment, enter_or_exit in self.signal_descriptions
                ],
                "transitions": self.transitions,
            }
        )

    @staticmethod
    def from_json(json_str, signal_detector_factory):
        json_obj = json.loads(json_str)
        return GraphSignalDetectorBuilder(
            json_obj["id"],
            json_obj["name"],
            [
                signal_detector_factory.create(config["name"], config["config"])
                for config in json_obj["signal_detectors"]
            ],
            json_obj["state_descriptions"],
            json_obj["initial_state"],
            [
                (
                    state,
                    Sentiment.from_json(sentiment),
                    EnterOrExit.from_json(enter_or_exit),
                )
                for state, sentiment, enter_or_exit in json_obj["signal_descriptions"]
            ],
            json_obj["transitions"],
        )


class Model:
    name: str = "Model"

    @staticmethod
    def add_bullish_signal(*args):
        GraphSignalDetector.add_state_signal(*args, Sentiment.BULLISH)

    @staticmethod
    def add_bearish_signal(*args):
        GraphSignalDetector.add_state_signal(*args, Sentiment.BEARISH)

    @staticmethod
    def add_neutral_signal(*args):
        GraphSignalDetector.add_state_signal(*args, Sentiment.NEUTRAL)


class GraphSignalDetector(SignalDetector):
    def __init__(
        self,
        identifier,
        name,
        detectors,
        machine,
    ):
        super().__init__(identifier, name)
        self.detectors = detectors
        self.machine = machine
        assert len(self.machine.models) == 0

    @staticmethod
    def add_state_signal(
        identifier, name, date, mutable_signal_sequence, tickers, sentiment
    ):
        ss = mutable_signal_sequence.get()
        new_ss = add_signal(ss, Signal(identifier, name, sentiment, date, tickers))
        mutable_signal_sequence.set(new_ss)

    @property
    def __tickers(self):
        tickers = set()
        for d in self.detectors:
            if hasattr(d, "ticker"):
                tickers.add(d.ticker)
            if hasattr(d, "tickers"):
                tickers |= d.tickers
        return list(tickers)

    def detect(self, from_date, to_date, stock_market, sequence):
        model = Model()
        self.machine.add_model(model)

        signals = merge_signals(
            *[
                detector.detect(
                    stock_market.start_date, to_date, stock_market, SignalSequence()
                )
                for detector in self.detectors
            ]
        )

        mutable_sequence = Mutable(SignalSequence())
        for signal in signals.signals:
            model.trigger(
                str(signal.id),
                self.id,
                self.name,
                signal.date,
                mutable_sequence,
                self.__tickers,
            )

        self.machine.remove_model(model)
        return merge_signals(
            sequence,
            mutable_sequence.get().signals_since(from_date - dt.timedelta(days=1)),
        )

    def is_valid(self, stock_market):
        return all((t in stock_market.tickers for t in self.__tickers))

    @staticmethod
    def __eq_machines(first, second):
        first_markup = first.markup
        second_markup = second.markup
        return (first_markup["states"], first_markup["transitions"],) == (
            second_markup["states"],
            second_markup["transitions"],
        )

    def __eq__(self, other):
        if not isinstance(other, GraphSignalDetector):
            return False

        def get_id(detector):
            return detector.id

        if not GraphSignalDetector.__eq_machines(self.machine, other.machine):
            return False
        return sorted(self.detectors, key=get_id) == sorted(other.detectors, key=get_id)

    @staticmethod
    def NAME():
        return "Graph"

    def to_json(self):
        return json.dumps(
            {
                "id": self.id,
                "name": self.name,
                "signal_detectors": [
                    {"name": sd.NAME(), "config": sd.to_json()} for sd in self.detectors
                ],
                "machine": self.machine.markup,
            }
        )

    @staticmethod
    def from_json(json_str, signal_detector_factory):
        json_obj = json.loads(json_str)
        return GraphSignalDetector(
            json_obj["id"],
            json_obj["name"],
            [
                signal_detector_factory.create(config["name"], config["config"])
                for config in json_obj["signal_detectors"]
            ],
            MarkupMachine(markup=json_obj["machine"]),
        )

    @staticmethod
    def json_schema():
        return {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "signal_detectors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                    },
                },
                "machine": {"type": "object"},
            },
        }
