from dataclasses import dataclass, field

import networkx as nx

from classiq.interface.generator.function_call import FunctionCall
from classiq.interface.generator.function_params import IO

from classiq.exceptions import ClassiqWiringError
from classiq.model_designer import logic_flow_change_handler
from classiq.quantum_register import QReg, Qubit


# We need the _FuncCallNode dataclass to be hashable for inserting it into the graph,
# hence the dataclass is frozen.
@dataclass(frozen=True)
class _FuncCallNode:
    # compare=False here because the FunctionCall object is mutable,
    # and comparing it will make the class unhashable.
    # So instead we compare only by name (which corresponds to the unique FunctionCall.name)
    func_call: FunctionCall = field(compare=False)
    name: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, "name", self.func_call.name)

    def __str__(self):
        return self.func_call.name


# See note about frozen=True in line 12
@dataclass(frozen=True)
class _Pin:
    pin_name: str
    index: int
    call_name: str  # We need to store call_name because different function calls may have the same base_name and index
    io: IO  # We need to store IO because a function may have an input and an output pin with the same name

    def __str__(self) -> str:
        return f"{self.pin_name}[{self.index}]"


class _StrictDiGraph(nx.DiGraph):
    def add_edge(self, u_of_edge, v_of_edge, **attr) -> None:
        if u_of_edge in self and v_of_edge in self[u_of_edge]:
            raise ClassiqWiringError(
                f"Cannot reconnect an already connected edge: {u_of_edge}, {v_of_edge}"
            )
        super().add_edge(u_of_edge, v_of_edge, **attr)


class LogicFlowBuilder:
    def __init__(self) -> None:
        self._logic_flow_graph = _StrictDiGraph()
        self._connect_qubit_func = {
            IO.Input: self._connect_qubit_to_func_call,
            IO.Output: self._connect_func_call_to_qubit,
        }

    def _is_qubit_available(self, qubit: Qubit) -> bool:
        return qubit in self._logic_flow_graph.nodes

    def _validate_qreg(self, qreg: QReg) -> None:
        invalid_qubit_indices = [
            i
            for i, qubit in enumerate(qreg.qubits)
            if not self._is_qubit_available(qubit)
        ]
        if invalid_qubit_indices:
            raise ClassiqWiringError(
                f"Cannot use a QReg with consumed or uninitialized qubits: {invalid_qubit_indices}"
            )

    def _verify_no_loops(self, dest_node: _FuncCallNode):
        if not nx.is_directed_acyclic_graph(self._logic_flow_graph):
            raise ClassiqWiringError(f"Cannot wire function {dest_node} to itself")

    def _connect_qubit_to_func_call(
        self, qubit: Qubit, dest_pin: _Pin, dest_node: _FuncCallNode
    ) -> None:
        self._logic_flow_graph.add_edge(dest_pin, dest_node)
        nx.relabel_nodes(self._logic_flow_graph, {qubit: dest_pin}, copy=False)
        self._handle_change(dest_pin, dest_node)

    def _connect_func_call_to_qubit(
        self, qubit: Qubit, source_pin: _Pin, source_node: _FuncCallNode
    ) -> None:
        self._logic_flow_graph.add_edge(source_node, source_pin)
        self._logic_flow_graph.add_edge(source_pin, qubit)

    def _connect_io(self, io: IO, func_call: FunctionCall, pin_name: str, qreg: QReg):
        func_node = _FuncCallNode(func_call)
        pins = [_Pin(pin_name, i, func_node.name, io) for i in range(len(qreg))]
        for pin, qubit in zip(pins, qreg.qubits):
            self._connect_qubit_func[io](qubit, pin, func_node)

    def connect_qreg_to_func_call(
        self, source: QReg, dest_pin_name: str, dest_func_call: FunctionCall
    ):
        self._validate_qreg(source)
        self._connect_io(IO.Input, dest_func_call, dest_pin_name, source)
        self._verify_no_loops(_FuncCallNode(dest_func_call))

    def connect_func_call_to_qreg(
        self, source_func_call: FunctionCall, source_pin_name: str, dest: QReg
    ):
        self._connect_io(IO.Output, source_func_call, source_pin_name, dest)

    def _handle_change(self, dest_pin: _Pin, dest_node: _FuncCallNode) -> None:
        source_pin, _ = next(iter(self._logic_flow_graph.in_edges(dest_pin)))
        source_node, _ = next(iter(self._logic_flow_graph.in_edges(source_pin)))
        logic_flow_change_handler.handle(
            source_node.func_call,
            str(source_pin),
            str(dest_pin),
            dest_node.func_call,
        )
