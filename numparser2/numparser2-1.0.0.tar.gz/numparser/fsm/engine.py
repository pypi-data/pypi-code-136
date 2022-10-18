from __future__ import annotations

import copy
import re
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from operator import itemgetter
from typing import (
    Callable,
    Dict,
    Generic,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    TypeVar,
    Union,
)
from uuid import uuid4

import networkx as nx
from numparser.fsm.tokenizer import Token, TokenType
from numparser.output import ParsedNumber

# ID = Union[int, str]
ID = str
FSMResult = Dict[str, List[List[Tuple[str, List[Token]]]]]
FSMResultParser = Callable[[FSMResult, str], List[ParsedNumber]]


@dataclass
class Bound:
    id: str = field(default_factory=lambda: str(uuid4()))
    # inclusive, zero mean optional, default 1 to prevent infinite loop
    min: int = 1
    # inclusive
    max: int = float("inf")  # type: ignore


K = TypeVar("K")


class ConsumingHist(Generic[K]):
    def __init__(self, dict: Dict[K, Bound]):
        self.counters = {}
        bound2counter = {}
        for k, v in dict.items():
            if v.id not in bound2counter:
                bound2counter[v.id] = {"count": 0, "min": v.min}
            self.counters[k] = bound2counter[v.id]

    def does_satisfy_minimum_consumption(self):
        """Whether any the minimum consumption is satisfied."""
        return any(
            counter["count"] >= counter["min"] for counter in self.counters.values()
        )

    def __getitem__(self, id: K) -> int:
        return self.counters[id]["count"]

    def __setitem__(self, id: K, value: int) -> None:
        self.counters[id]["count"] = value


@dataclass
class BaseState(ABC):
    """Represent a state configuration."""

    # id of the state
    id: ID
    name: str = ""

    # states that belong to the group must share the token value in order to consume the token.
    # for example, token delimiters may have multiple possible values, but once the first delimiter token is consumed, the rest of the state should
    # use the same delimiters
    group_id: Optional[ID] = None
    # denote that value of states in this group must be different from values of states in other groups
    diff_group_id: Optional[ID] = None

    # the name of the registry that will store the consumed tokens of this state. none if we do not want to store the consumed tokens
    registry_id: Optional[ID] = None

    # no consume: telling this state won't consume any value, so it can be used as look-ahead state
    no_consume: bool = False

    @abstractmethod
    def _create_consuming_hist(self) -> ConsumingHist:
        pass

    @abstractmethod
    def _consume_one_token(self, token: Token, consuming_hist: ConsumingHist) -> bool:
        """Consume the token & update history.

        Args:
            token: the token to consume
            consuming_hist: the history of consuming tokens

        Returns:
            True if the token is consumed, False otherwise
        """
        pass

    @abstractmethod
    def is_optional(self) -> bool:
        """Return whether this state can be passed even when there is no matched token"""
        pass

    @abstractmethod
    def does_accept_token(self, token: Token) -> bool:
        """Return whether this state accept the given token regardless of the minimum consumption requirement"""
        pass

    def consume(self, seq: List[Token], index: int) -> Tuple[int, List[Token], bool]:
        """Consume the tokens in the sequence from the index

        Returns:
            The index of the remaining unconsumed token, the consumed tokens, and whether the state
            consumed at least minimum number of tokens as specified in the requirements
        """
        tokens = []
        consuming_hist = self._create_consuming_hist()

        origin_index = index

        while index < len(seq):
            token = seq[index]
            if not self._consume_one_token(token, consuming_hist):
                if self.no_consume:
                    return (
                        origin_index,
                        tokens,
                        consuming_hist.does_satisfy_minimum_consumption(),
                    )
                return index, tokens, consuming_hist.does_satisfy_minimum_consumption()

            tokens.append(token)
            index += 1
        if self.no_consume:
            return (
                origin_index,
                tokens,
                consuming_hist.does_satisfy_minimum_consumption(),
            )
        return len(seq), tokens, consuming_hist.does_satisfy_minimum_consumption()


@dataclass
class StateAcceptingTokenType(BaseState):
    # token types that allows to be in this state, and the bound (maximum & minimum) of each type this state can consume
    # at the same time, they can consume multiple types of tokens as long as the bound of each type is not exceeded threshold
    # assuming that the token types are disjoint (enforced by enum)
    token_types: Dict[TokenType, Bound] = field(default_factory=dict)

    def _create_consuming_hist(self) -> ConsumingHist:
        return ConsumingHist(self.token_types)

    def _consume_one_token(
        self, token: Token, consuming_hist: ConsumingHist[TokenType]
    ) -> bool:
        # TODO: if this state is no consuming, stop consuming if we hit the minimum requirements
        if token.type not in self.token_types:
            return False
        if consuming_hist[token.type] >= self.token_types[token.type].max:
            # already hit the limit
            return False
        consuming_hist[token.type] += 1
        return True

    def is_optional(self) -> bool:
        return all(bound.min == 0 for bound in self.token_types.values())

    def does_accept_token(self, token: Token) -> bool:
        return token.type in self.token_types


@dataclass
class StateAcceptingTokenCharacters(BaseState):
    # tokens that are allowed / not allowed to be in this state, and the bound (maximum & minimum) of each token this state can consume
    # at the same time, they can consume multiple tokens as long as the bound of each set of characters is not exceeded threshold
    # each item is: list of characters that matched, whether to accept if it is in the list or not, and finally the bound
    # assuming the list of characters are disjoint
    tokens: List[Tuple[Set[str], bool, Bound]] = field(default_factory=list)
    # set of types that we don't want to accept
    not_accept_types: Set[TokenType] = field(default_factory=set)

    def _create_consuming_hist(self) -> ConsumingHist[int]:
        return ConsumingHist({i: b for i, (_, _, b) in enumerate(self.tokens)})

    def _consume_one_token(
        self, token: Token, consuming_hist: ConsumingHist[int]
    ) -> bool:
        if token.type in self.not_accept_types:
            return False

        # TODO: if this state is no consuming, stop consuming if we hit the minimum requirements
        for i, (chars, flag, bound) in enumerate(self.tokens):
            if token.value in chars:
                if not flag:
                    # not suppose to match
                    continue
            else:
                if flag:
                    # suppose to match
                    continue

            if consuming_hist[i] >= bound.max:
                # already hit the limit
                return False
            consuming_hist[i] += 1
            return True
        return False

    def is_optional(self) -> bool:
        return all(bound.min == 0 for _, _, bound in self.tokens)

    def does_accept_token(self, token: Token) -> bool:
        if token.type in self.not_accept_types:
            return False

        for chars, flag, bound in self.tokens:
            if token.value in chars:
                if not flag:
                    # not suppose to match
                    continue
            elif flag:
                # suppose to match
                continue
            return True
        return False


@dataclass
class WildcardState(BaseState):
    # this state won't consume any token
    no_consume: bool = True

    def _create_consuming_hist(self) -> ConsumingHist:
        raise Exception("This function should never be called")

    def _consume_one_token(
        self, token: Token, consuming_hist: ConsumingHist[int]
    ) -> bool:
        raise Exception("This function should never be called")

    def is_optional(self) -> bool:
        return True

    def does_accept_token(self, token: Token) -> bool:
        return True

    def consume(self, seq: List[Token], index: int) -> Tuple[int, List[Token], bool]:
        return index, [], True


def is_group_equal(group1: List[Token], group2: List[Token]) -> bool:
    """This group comparison function ignore spaces and only compared non empty tokens"""
    return "".join([t.value.strip() for t in group1]) == "".join(
        [t.value.strip() for t in group2]
    )


State = Union[StateAcceptingTokenType, StateAcceptingTokenCharacters, WildcardState]


@dataclass
class FSM:
    states: Dict[ID, State]
    transitions: Dict[ID, List[ID]]
    # the initial states of the FSA
    start_states: List[ID]
    # list of states that the FSA can terminate at
    terminate_states: Set[ID]
    fasttrack_to_terminate: Set[ID] = field(init=False)
    is_verified: bool = field(init=False)

    def __post_init__(self):
        """Verify the pattern to ensure it can terminate and will comply with the engine"""
        g = nx.DiGraph()
        for pid, cids in self.transitions.items():
            parent = self.states[pid]
            if parent.is_optional() or parent.no_consume:
                for cid in cids:
                    child = self.states[cid]
                    if child.is_optional() or child.no_consume:
                        g.add_edge(pid, cid)
            if pid in cids:
                raise Exception(
                    "Can't not transite back to the same state. Self-loop is implemented via bounding"
                )
        try:
            nx.find_cycle(g)
            raise Exception("This FSA may not terminate. Please fix it")
        except nx.NetworkXNoCycle:
            pass

        inverted_transitions = {sid: [] for sid in self.states}
        for sid, cids in self.transitions.items():
            for cid in cids:
                inverted_transitions[cid].append(sid)
        self.is_verified = True
        self.fasttrack_to_terminate = set(self.terminate_states)
        dfs = list(self.terminate_states)
        visited = set()
        while len(dfs) > 0:
            state_id = dfs.pop()
            if self.states[state_id].is_optional():
                visited.add(state_id)
                self.fasttrack_to_terminate.add(state_id)
                for pid in inverted_transitions[state_id]:
                    if pid in visited:
                        continue
                    dfs.append(pid)
                    self.fasttrack_to_terminate.add(pid)
        return

    def rename(self, newns: str, newregs: Optional[Dict[ID, ID]] = None) -> FSM:
        states = {}
        rename = {}
        for name, state in self.states.items():
            if name == "start" or name == "end":
                newname = name
            else:
                if name.find(":") != -1:
                    newname = newns + ":" + name.replace(":", "_")
                else:
                    newname = newns + ":" + name

            rename[name] = newname
            state = copy.deepcopy(state)
            state.id = newname
            if newregs is not None and state.registry_id in newregs:
                state.registry_id = newregs[state.registry_id]  # type: ignore
            states[newname] = state

        transitions = {}
        for source_id, target_ids in self.transitions.items():
            transitions[rename[source_id]] = [rename[x] for x in target_ids]

        return FSM(
            states,
            transitions,
            [rename[x] for x in self.start_states],
            {rename[x] for x in self.terminate_states},
        )

    def execute(
        self,
        seq: List[Token],
        is_group_equal: Callable[[List[Token], List[Token]], bool] = is_group_equal,
    ) -> Optional[FSMResult]:
        """Execute the FSA and returns groups of tokens that are asked to be kept in the registries

        Args:
            seq: the sequence of tokens to be tested against the FSA
            is_group_equal: a function that compares two groups of tokens and returns True if they are the similar

        Returns:
            None if the FSA can't reach the terminate states (including if the sequence is empty)
        """
        if len(seq) == 0:
            return None
        assert self.is_verified, "This FSA must be verified before execution"

        index = 0
        groups = {}
        histories = []
        registries = {}
        first_registered_states = {}

        if len(self.start_states) > 0:
            # more than one start state, we have a branching point!
            ranked_next_states = self.rank_next_states(seq, index, self.start_states)
            if len(ranked_next_states) == 0:
                # no start state matched...
                return None
            elif len(ranked_next_states) == 1:
                # only one start state matched
                state = ranked_next_states[0]
            else:
                # more than one state can consume the token,
                # record this branching point, and select the best state to move next
                histories.append(
                    {
                        "index": index,
                        "remaining_possible_states": ranked_next_states[1:],
                        "groups": copy.deepcopy(groups),
                        "registries": copy.deepcopy(registries),
                    }
                )
                state = ranked_next_states[0]
        else:
            assert len(self.start_states) == 1, "Must have no empty start states"
            state = self.states[self.start_states[0]]
            if not state.does_accept_token(seq[index]) and not state.is_optional():
                # no start state matched...
                return None

        while index < len(seq):
            index, tokens, valid_state = state.consume(seq, index)

            if index >= len(seq) and state.id not in self.fasttrack_to_terminate:
                # reach the end of the sequence, but not terminate state
                valid_state = False

            if valid_state and state.group_id is not None:
                if state.group_id not in groups:
                    groups[state.group_id] = tokens
                elif not is_group_equal(groups[state.group_id], tokens):
                    # value supposed to be the same, but it's not, invalid state
                    valid_state = False

            if valid_state and state.diff_group_id is not None:
                if state.diff_group_id in groups and is_group_equal(
                    groups[state.diff_group_id], tokens
                ):
                    # value supposed to be different, but it's the same, invalid state
                    valid_state = False

            if valid_state:
                if state.registry_id is not None:
                    if state.registry_id not in registries:
                        first_registered_states[state.registry_id] = state.id
                        registries[state.registry_id] = []

                    if first_registered_states[state.registry_id] == state.id:
                        registries[state.registry_id].append([])
                    registries[state.registry_id][-1].append((state.name, tokens))

                if index >= len(seq):
                    # reach the end of the sequence, we done
                    break

                # gather information of the next states
                ranked_next_states = self.rank_next_states(
                    seq, index, self.transitions[state.id]
                )

                if len(ranked_next_states) == 0:
                    if len(histories) == 0:
                        # no way to backtrack to, so we can't reach the terminate states
                        return None

                    # backtrack to the previous branching point if possible
                    index = histories[-1]["index"]
                    groups = histories[-1]["groups"]
                    registries = copy.deepcopy(histories[-1]["registries"])
                    possible_states = histories[-1]["remaining_possible_states"]
                    if len(possible_states) == 1:
                        # we already explored all possible ways at this branching point
                        # need to remove this branching point
                        histories.pop()
                    else:
                        # remove the one we are going to explore next
                        histories[-1]["remaining_possible_states"] = possible_states[1:]
                    state = possible_states[0]
                elif len(ranked_next_states) == 1:
                    state = ranked_next_states[0]
                else:
                    # more than one state can consume the token,
                    # record this branching point, and select the best state to move next
                    histories.append(
                        {
                            "index": index,
                            "remaining_possible_states": ranked_next_states[1:],
                            "groups": copy.deepcopy(groups),
                            "registries": copy.deepcopy(registries),
                        }
                    )
                    state = ranked_next_states[0]
            else:
                if len(histories) == 0:
                    # no way to backtrack to, so we can't reach the terminate states
                    return None

                # backtrack to the previous branching point if possible
                index = histories[-1]["index"]
                groups = histories[-1]["groups"]
                registries = copy.deepcopy(histories[-1]["registries"])
                possible_states = histories[-1]["remaining_possible_states"]
                if len(possible_states) == 1:
                    # we already explored all possible ways at this branching point
                    # need to remove this branching point
                    histories.pop()
                else:
                    # remove the one we are going to explore next
                    histories[-1]["remaining_possible_states"] = possible_states[1:]
                state = possible_states[0]

        return registries

    def rank_next_states(
        self, seq: List[Token], index: int, next_state_ids: Iterable[str]
    ) -> List[State]:
        """Rank the next states"""
        token = seq[index]
        ranked_next_states = []
        for sid in next_state_ids:
            state = self.states[sid]
            if not state.does_accept_token(token):
                if state.is_optional():
                    ranked_next_states.append((state, 0))
            else:
                ranked_next_states.append((state, 1 if state.no_consume else 2))

        ranked_next_states = sorted(ranked_next_states, key=itemgetter(1), reverse=True)
        return [x[0] for x in ranked_next_states]

    @staticmethod
    def from_string(graph: str, **fsms: FSM) -> FSM:
        """Deserialize a graph"""

        def string2state(s: str) -> State:
            """Create a state from a string.
            Args:
                s: input string, must in the following format
                    <id>: (group=<group_id> )?(diff_group=<diff_group_id> )?(registry=<registry_id> )?tokens=<token_type>[<min>(,<max>)?](,<token_type>[<min>(,<max>)?])*

                    Note that if it contains a newline character, you need to escape it with a backslash (e.g., \\n), other character such as \t do not need to be escaped.
            """
            m = re.match(
                r"(?P<id>\w+): *(name=(?P<name>\w+))? *(group=(?P<group>\w+))? *(diff_group=(?P<diff_group>\w+))? *(registry=(?P<registry>\w+))? *args=(?P<args>.+)",
                s,
            )
            assert m is not None
            tokens = []
            type = None
            args = m.group("args")
            if args.startswith("^"):
                caret = args[1:].find("^")
                assert caret != -1
                exclude_types = {TokenType(x) for x in args[1 : caret + 1].split(",")}
                args = args[caret + 2 :]
            else:
                exclude_types = set()

            for token_s in args.split(" | "):
                mi = re.match(
                    r"^(?P<token>(?:([^\[][^\{]+)|\[((?![^\\]\]).)*.\])){(?:(?P<bid>[a-zA-Z]+):)?(?P<min>\d+)(?:(?P<comma>,)(?P<max>\d+)?)?}$",
                    token_s.strip(),
                )
                assert mi is not None
                if mi.group("comma") is None:
                    max = int(mi.group("min"))
                elif mi.group("max") is None:
                    max = float("inf")
                else:
                    max = int(mi.group("max"))

                if mi.group("bid") is not None:
                    bound = Bound(id=mi.group("bid"), min=int(mi.group("min")), max=max)  # type: ignore
                else:
                    bound = Bound(min=int(mi.group("min")), max=max)  # type: ignore

                if mi.group("token") in set(TokenType):
                    tokens.append((TokenType(mi.group("token")), bound))
                    assert type is None or type == "token_type", type
                    type = "token_type"
                else:
                    assert type is None or type == "token_value", type
                    token = mi.group("token")
                    if len(token) > 1:
                        token = token[1:-1]
                    if token.startswith("^"):
                        token = token[1:]
                        flag = False
                    else:
                        flag = True

                    chars = set()
                    i = 0
                    while i < len(token):
                        if token[i] == "\\":
                            c = token[i + 1 : i + 2]
                            if c == "n":
                                c = "\n"
                            i += 1
                        else:
                            c = token[i]

                        if i < len(token) - 1 and token[i + 1] == "-":
                            assert i < len(token) - 2
                            i = i + 2
                            if token[i] == "\\":
                                nc = token[i + 1 : i + 2]
                                if nc == "n":
                                    nc = "\n"
                                i += 1
                            else:
                                nc = token[i]

                            for ci in range(ord(c), ord(nc) + 1):
                                chars.add(chr(ci))
                        else:
                            chars.add(c)
                        i += 1
                    tokens.append((chars, flag, bound))

            if type == "token_type":
                state = StateAcceptingTokenType(
                    id=m.group("id"), token_types=dict(tokens)
                )
            else:
                state = StateAcceptingTokenCharacters(
                    id=m.group("id"), tokens=tokens, not_accept_types=exclude_types
                )
            if m.group("name") is not None:
                state.name = m.group("name")
            if m.group("group") is not None:
                state.group_id = m.group("group")
            if m.group("diff_group") is not None:
                state.diff_group_id = m.group("diff_group")
            if m.group("registry") is not None:
                state.registry_id = m.group("registry")
            return state

        def parse_transition_node(line: str) -> Tuple[List[str], str]:
            if line.startswith("("):
                m = re.match(r"\([^)]+\)", line)
                assert m is not None
                content = line[1 : m.span()[1] - 1]
                return [x.strip() for x in content.split(";")], line[
                    m.span()[1] :
                ].strip()

            m = re.match(r"(\w|:)+", line)
            assert m is not None
            node = line[: m.span()[1]]
            return [node], line[m.span()[1] :].strip()

        state_s, tran_s = graph.split("---")
        lst = [string2state(s.strip()) for s in state_s.split("\n") if s.strip() != ""]
        states = {state.id: state for state in lst}

        transitions = defaultdict(list)
        for line in tran_s.split("\n"):
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue

            current_node_ids, line = parse_transition_node(line)

            while len(line) > 0:
                m = re.match(" *(?P<direction><?->?) *", line)
                assert m is not None, line
                direction = m.group("direction")
                line = line[m.span()[1] :].strip()

                next_node_ids, line = parse_transition_node(line)

                for curr_node_id in current_node_ids:
                    for next_node_id in next_node_ids:
                        if direction == "<->":
                            transitions[curr_node_id].append(next_node_id)
                            transitions[next_node_id].append(curr_node_id)
                        elif direction == "<-":
                            transitions[next_node_id].append(curr_node_id)
                        else:
                            assert direction == "->"
                            transitions[curr_node_id].append(next_node_id)
                current_node_ids = next_node_ids

        all_states = set()
        for source_id, target_ids in transitions.items():
            all_states.add(source_id)
            all_states.update(target_ids)

        assert "start" in all_states and "end" in all_states
        if "start" not in states:
            states["start"] = WildcardState(id="start")
        if "end" not in states:
            states["end"] = WildcardState(id="end")
        assert {x for x in all_states if x.find(":") == -1} == states.keys()

        transitions = dict(transitions)
        for state_id in states.keys():
            if state_id not in transitions:
                transitions[state_id] = []

        for name, fsm in fsms.items():
            assert "start" in fsm.states and "end" in fsm.states
            rename = {}
            for sname, state in fsm.states.items():
                if sname.find(":") == -1:
                    rename[sname] = name + ":" + sname
                    assert rename[sname] not in states
                else:
                    # already in different namespace, nested fsm
                    rename[sname] = sname

            for sname in fsm.states:
                state = copy.deepcopy(fsm.states[sname])
                state.id = rename[sname]
                states[rename[sname]] = state
            for source_id, target_ids in fsm.transitions.items():
                if rename[source_id] in transitions:
                    assert len(target_ids) == 0 and source_id in {
                        "start",
                        "end",
                    }, "Should use only start and end states of nested fsm"
                    continue
                transitions[rename[source_id]] = [rename[x] for x in target_ids]

        return FSM(states, transitions, ["start"], {"end"})
