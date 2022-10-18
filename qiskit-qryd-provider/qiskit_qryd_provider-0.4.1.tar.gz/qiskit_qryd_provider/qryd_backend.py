import warnings
from contextlib import suppress
from itertools import product
from math import pi
from typing import Any
from typing import Dict
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union

import requests
from qiskit.circuit import Measure
from qiskit.circuit import Parameter
from qiskit.circuit.library import CPhaseGate
from qiskit.circuit.library import CXGate
from qiskit.circuit.library import CYGate
from qiskit.circuit.library import CZGate
from qiskit.circuit.library import HGate
from qiskit.circuit.library import iSwapGate
from qiskit.circuit.library import PhaseGate
from qiskit.circuit.library import RGate
from qiskit.circuit.library import RXGate
from qiskit.circuit.library import RYGate
from qiskit.circuit.library import RZGate
from qiskit.circuit.library import SwapGate
from qiskit.circuit.library import SXdgGate
from qiskit.circuit.library import SXGate
from qiskit.circuit.library import UGate
from qiskit.circuit.library import XGate
from qiskit.circuit.library import YGate
from qiskit.circuit.library import ZGate
from qiskit.providers import BackendV2 as Backend
from qiskit.providers import Options
from qiskit.transpiler import InstructionProperties
from qiskit.transpiler import Target

from .qryd_gates import PCZGate
from .qryd_job import QRydJob

if TYPE_CHECKING:
    import qiskit
    import qiskit_qryd_provider


class QRydBackend(Backend):
    """Super class for accessing the emulator of the `QRydDemo`_ consortium.

    .. _QRydDemo: https://thequantumlaend.de/qryddemo/

    All backends are derived from this class, which provides functionality for running a
    quantum circuit on the emulator. For usages examples, see the derived backends.

    """

    url_base = "https://api.qryddemo.itp3.uni-stuttgart.de/v3_0/jobs"
    """URL to the `web API
    <https://api.qryddemo.itp3.uni-stuttgart.de/docs>`_ endpoint for submitting
    simulation jobs to QRydDemo's cloud emulator."""

    def __init__(self, **kwargs) -> None:
        """Initialize the class.

        Args:
            **kwargs: Arguments to pass to Qiskit's
                :external+qiskit:py:class:`Backend <qiskit.providers.BackendV2>` class.

        """
        super().__init__(**kwargs)

        # Set option validators
        self.options.set_validator("shots", (1, 2**18))
        self.options.set_validator("memory", [False])
        self.options.set_validator("seed_simulator", int)
        self.options.set_validator("seed_compiler", int)
        self.options.set_validator("dev", bool)
        self.options.set_validator("fusion_max_qubits", (2, 6))
        self.options.set_validator("use_extended_set", bool)
        self.options.set_validator("use_reverse_traversal", bool)
        self.options.set_validator("extended_set_size", (1, 100))
        self.options.set_validator("extended_set_weight", float)
        self.options.set_validator("reverse_traversal_iterations", (1, 30))

    @property
    def target(self) -> Target:
        """A target object which defines a model of the backend for Qiskit's transpiler.

        Returns:
            A target object of the backend.

        """
        return self._target

    @property
    def max_circuits(self) -> int:
        """The maximum number of circuits that can be run in a single job.

        Currently, it is only supported to run a single circuit in a single job.

        Returns:
            1

        """
        return 1

    @classmethod
    def _default_options(cls) -> Options:
        """Get default options.

        Returns:
            An Options object.

        """
        return Options(
            shots=1024,
            memory=False,
            seed_simulator=None,
            seed_compiler=None,
            dev=False,
            fusion_max_qubits=4,
            use_extended_set=True,
            use_reverse_traversal=True,
            extended_set_size=5,
            extended_set_weight=0.5,
            reverse_traversal_iterations=2,
        )

    def set_option(
        self,
        key: str,
        value: Union[Optional[int], Optional[bool], Optional[str], Optional[float]],
    ) -> None:
        r"""Set an option.

        Args:
            key: The key of the option. Currently, the following options are supported:

                * :code:`shots` (:external:py:class:`int`, default: 1024):
                  Number of measurements, must be :math:`\geq 1` and
                  :math:`\leq 2^{18}`.
                * :code:`seed_simulator` (:external:py:class:`int`, default: None):
                  A seed for the random number generator of the emulator.
                * :code:`fusion_max_qubits` (:external:py:class:`int`, default: 4):
                  The maximum number of qubits that can be fused in a single unitary.
                * :code:`dev` (:external:py:class:`bool`, default: False):
                  Whether to use the development version of the emulator.

                If the backend supports compilation in the cloud, the following
                additional options are supported:

                * :code:`seed_compiler` (:external:py:class:`int`, default: None):
                  A seed for the random number generator of the compiler.
                * :code:`use_extended_set` (:external:py:class:`bool`, default: True):
                  Whether the `SABRE algorithm`_ uses the extended set of gates.
                * :code:`use_reverse_traversal` (:external:py:class:`bool`, default:
                  True): Whether SABRE uses the reverse traversal
                  technique to update the initial mapping.
                * :code:`extended_set_size` (:external:py:class:`int`, default: 5):
                  Size of the extended set of gates used by SABRE.
                * :code:`extended_set_weight` (:external:py:class:`float`, default:
                  0.5):
                  Weight of the extended set of gates used by SABRE.
                * :code:`reverse_traversal_iterations` (:external:py:class:`int`,
                  default: 2): The number of times SABRE is run back and forth.

            value: The value of the option.

        Raises:
            NotImplementedError: If `key` does not describe a valid option.

        .. _SABRE algorithm: https://arxiv.org/abs/1809.02573

        .. # noqa: DAR101 value

        """
        if hasattr(self.options, key):
            if value is not None:
                setattr(self.options, key, value)
            else:
                setattr(self.options, key, getattr(self._default_options(), key))
        else:
            raise NotImplementedError(f'"{key}" is not a valid option.')

    def run(self, circuit: "qiskit.QuantumCircuit", **kwargs) -> QRydJob:
        """Serialize a circuit, submit it to the backend, and create a job.

        This method will submit a simulation job and return a Job object that runs the
        circuit on QRydDemo's emulator. This is an async call so that running does not
        block the program.

        Args:
            circuit: A QuantumCircuit to run on the backend.
            **kwargs: Any kwarg options to pass to the backend.

        Returns:
            A job object.

        """
        for kwarg in kwargs:
            if not hasattr(self.options, kwarg):
                warnings.warn(
                    "Option %s is not used by this backend." % kwarg,
                    UserWarning,
                    stacklevel=2,
                )

        options = self.options
        if "dev" in kwargs:
            options.update_options(dev=kwargs["dev"])
        if "seed_simulator" in kwargs:
            options.update_options(seed_simulator=kwargs["seed_simulator"])
        if "seed_compiler" in kwargs:
            options.update_options(seed_compiler=kwargs["seed_compiler"])
        if "memory" in kwargs:
            options.update_options(memory=kwargs["memory"])
        if "shots" in kwargs:
            options.update_options(shots=kwargs["shots"])
        if "fusion_max_qubits" in kwargs:
            options.update_options(fusion_max_qubits=kwargs["fusion_max_qubits"])
        if "use_extended_set" in kwargs:
            options.update_options(use_extended_set=kwargs["use_extended_set"])
        if "use_reverse_traversal" in kwargs:
            options.update_options(
                use_reverse_traversal=kwargs["use_reverse_traversal"]
            )
        if "extended_set_size" in kwargs:
            options.update_options(extended_set_size=kwargs["extended_set_size"])
        if "extended_set_weight" in kwargs:
            options.update_options(extended_set_weight=kwargs["extended_set_weight"])
        if "reverse_traversal_iterations" in kwargs:
            options.update_options(
                reverse_traversal_iterations=kwargs["reverse_traversal_iterations"]
            )

        job_dict = self._convert_to_wire_format(circuit, options)
        job_handle = self._submit_to_backend(job_dict, self._provider.session)
        job_url = job_handle.headers["Location"]

        return QRydJob(self, job_url, self._provider.session, options, circuit)

    def _convert_to_wire_format(
        self, circuit: "qiskit.QuantumCircuit", options: Options
    ) -> dict:
        """Convert a circuit to a dictionary.

        The method converts a circuit to a Json-serializable dictionary for submitting
        it to the API of QRydDemo's emulator.

        Args:
            circuit: The QuantumCircuit to be converted.
            options: The Options object of the backend.

        Raises:
            RuntimeError: If the `circuit` contains a quantum gate or operation that
                is not supported.
            AssertionError: If the `circuit` contains definitions that are inconsistent
                with definitions used by the web API.

        Returns:
            Json-serializable dictionary describing the simulation job.

        """
        circuit_dict = {
            "ClassicalRegister": {
                "measurement": {
                    "circuits": [
                        {
                            "definitions": [
                                {
                                    "DefinitionBit": {
                                        "name": "ro",
                                        "length": len(circuit.clbits),
                                        "is_output": True,
                                    }
                                }
                            ],
                            "operations": [],
                            "_roqoqo_version": {
                                "major_version": 1,
                                "minor_version": 0,
                            },
                        }
                    ],
                },
            },
        }  # type: Dict[str, Any]
        qubits_map = {bit: n for n, bit in enumerate(circuit.qubits)}
        clbits_map = {bit: n for n, bit in enumerate(circuit.clbits)}
        for instruction in circuit.data:
            inst = instruction[0]
            params = inst.params
            qubits = [qubits_map[bit] for bit in instruction[1]]
            clbits = [clbits_map[bit] for bit in instruction[2]]

            if inst.name == "barrier":
                continue
            elif inst.name == "measure":
                if len(qubits) != len(clbits):
                    raise AssertionError(
                        "Number of qubits and classical bits must be same."
                    )
                for qubit, clbit in zip(qubits, clbits):
                    circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                        "operations"
                    ] += [
                        {
                            "MeasureQubit": {
                                "readout": "ro",
                                "qubit": qubit,
                                "readout_index": clbit,
                            }
                        }
                    ]
            elif inst.name == "p":
                if len(qubits) != 1 or len(params) != 1:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "PhaseShiftState1": {
                            "qubit": qubits[0],
                            "theta": float(params[0]),
                        }
                    }
                ]
            elif inst.name == "r":
                if len(qubits) != 1 or len(params) != 2:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "RotateXY": {
                            "qubit": qubits[0],
                            "theta": float(params[0]),
                            "phi": float(params[1]),
                        }
                    }
                ]
            elif inst.name == "rx":
                if len(qubits) != 1 or len(params) != 1:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "RotateX": {
                            "qubit": qubits[0],
                            "theta": float(params[0]),
                        }
                    }
                ]
            elif inst.name == "ry":
                if len(qubits) != 1 or len(params) != 1:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "RotateY": {
                            "qubit": qubits[0],
                            "theta": float(params[0]),
                        }
                    }
                ]
            elif inst.name == "pcz":
                if len(qubits) != 2 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "PhaseShiftedControlledZ": {
                            "control": qubits[0],
                            "target": qubits[1],
                            "phi": float(PCZGate().get_theta()),
                        }
                    }
                ]
            elif inst.name == "h":
                if len(qubits) != 1 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "Hadamard": {
                            "qubit": qubits[0],
                        }
                    }
                ]
            elif inst.name == "rz":
                if len(qubits) != 1 or len(params) != 1:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "RotateZ": {
                            "qubit": qubits[0],
                            "theta": float(params[0]),
                        }
                    }
                ]
            elif inst.name == "u":
                if len(qubits) != 1 or len(params) != 3:
                    raise AssertionError("Wrong number of arguments.")
                theta = float(params[0])
                phi = float(params[1])
                lam = float(params[2])
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "RotateZ": {
                            "qubit": qubits[0],
                            "theta": lam - pi / 2,
                        }
                    },
                    {
                        "RotateX": {
                            "qubit": qubits[0],
                            "theta": theta,
                        }
                    },
                    {
                        "RotateZ": {
                            "qubit": qubits[0],
                            "theta": phi + pi / 2,
                        }
                    },
                ]
            elif inst.name == "x":
                if len(qubits) != 1 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "PauliX": {
                            "qubit": qubits[0],
                        }
                    }
                ]
            elif inst.name == "y":
                if len(qubits) != 1 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "PauliY": {
                            "qubit": qubits[0],
                        }
                    }
                ]
            elif inst.name == "z":
                if len(qubits) != 1 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "PauliZ": {
                            "qubit": qubits[0],
                        }
                    }
                ]
            elif inst.name == "sx":
                if len(qubits) != 1 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "SqrtPauliX": {
                            "qubit": qubits[0],
                        }
                    }
                ]
            elif inst.name == "sxdg":
                if len(qubits) != 1 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "InvSqrtPauliX": {
                            "qubit": qubits[0],
                        }
                    }
                ]
            elif inst.name == "cx":
                if len(qubits) != 2 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "CNOT": {
                            "control": qubits[0],
                            "target": qubits[1],
                        }
                    }
                ]
            elif inst.name == "cy":
                if len(qubits) != 2 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "ControlledPauliY": {
                            "control": qubits[0],
                            "target": qubits[1],
                        }
                    }
                ]
            elif inst.name == "cz":
                if len(qubits) != 2 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "ControlledPauliZ": {
                            "control": qubits[0],
                            "target": qubits[1],
                        }
                    }
                ]
            elif inst.name == "cp":
                if len(qubits) != 2 or len(params) != 1:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "ControlledPhaseShift": {
                            "control": qubits[0],
                            "target": qubits[1],
                            "theta": float(params[0]),
                        }
                    }
                ]
            elif inst.name == "swap":
                if len(qubits) != 2 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "SWAP": {
                            "control": qubits[0],
                            "target": qubits[1],
                        }
                    }
                ]
            elif inst.name == "iswap":
                if len(qubits) != 2 or len(params) != 0:
                    raise AssertionError("Wrong number of arguments.")
                circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
                    "operations"
                ] += [
                    {
                        "ISwap": {
                            "control": qubits[0],
                            "target": qubits[1],
                        }
                    }
                ]
            else:
                raise RuntimeError("Operation '%s' not supported." % inst.name)

        circuit_dict["ClassicalRegister"]["measurement"]["circuits"][0][
            "operations"
        ] += [
            {
                "PragmaSetNumberOfMeasurements": {
                    "readout": "ro",
                    "number_measurements": options.shots,
                }
            }
        ]

        job_dict = {
            "backend": self.name,
            "dev": options.dev,
            "fusion_max_qubits": options.fusion_max_qubits,
            "seed_simulator": options.seed_simulator,
            "seed_compiler": options.seed_compiler,
            "pcz_theta": float(PCZGate().get_theta()),
            "use_extended_set": options.use_extended_set,
            "use_reverse_traversal": options.use_reverse_traversal,
            "extended_set_size": options.extended_set_size,
            "extended_set_weight": options.extended_set_weight,
            "reverse_traversal_iterations": options.reverse_traversal_iterations,
            "program": circuit_dict,
        }
        return job_dict

    def _submit_to_backend(
        self, job_dict: Dict[str, Any], session: requests.Session
    ) -> requests.Response:
        """Submit a simulation job to QRydDemo's API.

        Args:
            job_dict: Json-serializable dictionary describing the simulation job.
            session: Session object that manages the connection to the API server.

        Raises:
            requests.HTTPError: If the web API did not accept the request.
            RuntimeError: If the API could not create a simulation job.

        Returns:
            The response of the API.

        .. # noqa: DAR401
        .. # noqa: DAR402

        """
        response = session.post(self.url_base, json=job_dict)
        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            with suppress(BaseException):
                error = requests.HTTPError(
                    f"{error} ({error.response.json()['detail']})"
                )
            raise error
        if response.status_code != 201:
            raise RuntimeError("Error creating a new job on the QRydDemo server")
        return response


class QRydEmuCloudcompSquare(QRydBackend):
    """Backend for accessing a specific emulator.

    The emulator simulates *30 ideal qubits* arranged in a *5x6 square lattice* with
    nearest-neighbor connectivity. Quantum circuits are compiled to the gate set and
    connectivity of the Rydberg platform on our servers after submitting the
    circuits to QRydDemo's infrastructure.

    Typical usage example:

    .. testcode::

        from qiskit_qryd_provider import QRydProvider
        from qiskit import QuantumCircuit, execute
        import os

        provider = QRydProvider(os.getenv("QRYD_API_TOKEN"))
        backend = provider.get_backend("qryd_emu_cloudcomp_square")

        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        job = execute(qc, backend, shots=200, optimization_level=3)

    """

    def __init__(self, provider: "qiskit_qryd_provider.QRydProvider") -> None:
        """Initialize the backend.

        Args:
            provider: The provider that this backend comes from.

        """
        super().__init__(
            provider=provider,
            name="qryd_emu_cloudcomp_square",
            backend_version="1.0.0",
        )

        num_qubits = 30

        # Calculate edges
        edges = [
            (q1, q2)
            for q1, q2 in product(range(num_qubits), range(num_qubits))
            if q1 != q2
        ]

        # Create Target
        self._target = Target()

        # Add native gates
        meas_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(Measure(), meas_props)

        lam = Parameter("lambda")
        p_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(PhaseGate(lam), p_props)

        theta = Parameter("theta")
        phi = Parameter("phi")
        r_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RGate(theta, phi), r_props)

        theta = Parameter("theta")
        rx_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RXGate(theta), rx_props)

        theta = Parameter("theta")
        ry_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RYGate(theta), ry_props)

        pcz_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(PCZGate(), pcz_props)

        # Add additional gates: single qubit gates
        # see https://github.com/Qiskit/qiskit-aer/blob/bb47adcf2e49b1e486e9ed15b3d55b6c4a345b1b/qiskit/providers/aer/backends/backend_utils.py#L52  # noqa: E501

        h_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(HGate(), h_props)

        theta = Parameter("theta")
        rz_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RZGate(theta), rz_props)

        theta = Parameter("theta")
        phi = Parameter("phi")
        lam = Parameter("lambda")
        u_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(UGate(theta, phi, lam), u_props)

        x_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(XGate(), x_props)

        y_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(YGate(), y_props)

        z_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(ZGate(), z_props)

        sx_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(SXGate(), sx_props)

        sxdg_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(SXdgGate(), sxdg_props)

        # Add additional gates: controlled gates

        cx_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CXGate(), cx_props)

        cy_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CYGate(), cy_props)

        cz_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CZGate(), cz_props)

        theta = Parameter("theta")
        cp_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CPhaseGate(theta), cp_props)

        # Add additional gates: other two qubit unitaries

        swap_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(SwapGate(), swap_props)

        iswap_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(iSwapGate(), iswap_props)


class QRydEmuCloudcompTriangle(QRydBackend):
    """Backend for accessing a specific emulator.

    The emulator simulates *30 ideal qubits* arranged in a *triangle lattice* with
    nearest-neighbor connectivity. Quantum circuits are compiled to the gate set and
    connectivity of the Rydberg platform on our servers after submitting the
    circuits to QRydDemo's infrastructure.

    Typical usage example:

    .. testcode::

        from qiskit_qryd_provider import QRydProvider
        from qiskit import QuantumCircuit, execute
        import os

        provider = QRydProvider(os.getenv("QRYD_API_TOKEN"))
        backend = provider.get_backend("qryd_emu_cloudcomp_triangle")

        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        job = execute(qc, backend, shots=200, optimization_level=3)

    """

    def __init__(self, provider: "qiskit_qryd_provider.QRydProvider") -> None:
        """Initialize the backend.

        Args:
            provider: The provider that this backend comes from.

        """
        super().__init__(
            provider=provider,
            name="qryd_emu_cloudcomp_triangle",
            backend_version="1.0.0",
        )

        num_qubits = 30

        # Calculate edges
        edges = [
            (q1, q2)
            for q1, q2 in product(range(num_qubits), range(num_qubits))
            if q1 != q2
        ]

        # Create Target
        self._target = Target()

        # Add native gates
        meas_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(Measure(), meas_props)

        lam = Parameter("lambda")
        p_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(PhaseGate(lam), p_props)

        theta = Parameter("theta")
        phi = Parameter("phi")
        r_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RGate(theta, phi), r_props)

        theta = Parameter("theta")
        rx_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RXGate(theta), rx_props)

        theta = Parameter("theta")
        ry_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RYGate(theta), ry_props)

        pcz_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(PCZGate(), pcz_props)

        # Add additional gates: single qubit gates
        # see https://github.com/Qiskit/qiskit-aer/blob/bb47adcf2e49b1e486e9ed15b3d55b6c4a345b1b/qiskit/providers/aer/backends/backend_utils.py#L52  # noqa: E501

        h_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(HGate(), h_props)

        theta = Parameter("theta")
        rz_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RZGate(theta), rz_props)

        theta = Parameter("theta")
        phi = Parameter("phi")
        lam = Parameter("lambda")
        u_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(UGate(theta, phi, lam), u_props)

        x_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(XGate(), x_props)

        y_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(YGate(), y_props)

        z_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(ZGate(), z_props)

        sx_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(SXGate(), sx_props)

        sxdg_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(SXdgGate(), sxdg_props)

        # Add additional gates: controlled gates

        cx_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CXGate(), cx_props)

        cy_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CYGate(), cy_props)

        cz_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CZGate(), cz_props)

        theta = Parameter("theta")
        cp_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(CPhaseGate(theta), cp_props)

        # Add additional gates: other two qubit unitaries

        swap_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(SwapGate(), swap_props)

        iswap_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(iSwapGate(), iswap_props)


class QRydEmuLocalcompSquare(QRydBackend):
    """Backend for accessing a specific emulator.

    The emulator simulates *30 ideal qubits* arranged in a *5x6 square lattice* with
    nearest-neighbor connectivity. Quantum circuits are compiled to the gate set and
    connectivity of the Rydberg platform by Qiskit.

    Typical usage example:

    .. testcode::

        from qiskit_qryd_provider import QRydProvider
        from qiskit import QuantumCircuit, execute
        import os

        provider = QRydProvider(os.getenv("QRYD_API_TOKEN"))
        backend = provider.get_backend("qryd_emu_localcomp_square")

        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        job = execute(qc, backend, shots=200, optimization_level=3)

    """

    def __init__(self, provider: "qiskit_qryd_provider.QRydProvider") -> None:
        """Initialize the backend.

        Args:
            provider: The provider that this backend comes from.

        """
        super().__init__(
            provider=provider,
            name="qryd_emu_localcomp_square",
            backend_version="1.0.0",
        )

        si = 5
        sj = 6
        num_qubits = si * sj

        # Calculate edges
        edges = [[i + si * j, i + si * j + 1] for i in range(si - 1) for j in range(sj)]
        edges += [
            [i + si * j + 1, i + si * j] for i in range(si - 1) for j in range(sj)
        ]
        edges += [
            [i + si * j, i + si * j + si] for i in range(si) for j in range(sj - 1)
        ]
        edges += [
            [i + si * j + si, i + si * j] for i in range(si) for j in range(sj - 1)
        ]

        # Create Target
        self._target = Target()

        # Add native gates
        meas_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(Measure(), meas_props)

        lam = Parameter("lambda")
        p_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(PhaseGate(lam), p_props)

        theta = Parameter("theta")
        phi = Parameter("phi")
        r_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RGate(theta, phi), r_props)

        theta = Parameter("theta")
        rx_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RXGate(theta), rx_props)

        theta = Parameter("theta")
        ry_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RYGate(theta), ry_props)

        pcz_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(PCZGate(), pcz_props)


class QRydEmuLocalcompTriangle(QRydBackend):
    """Backend for accessing a specific emulator.

    The emulator simulates *30 ideal qubits* arranged in a *triangle lattice* with
    nearest-neighbor connectivity. Quantum circuits are compiled to the gate set and
    connectivity of the Rydberg platform by Qiskit.

    Typical usage example:

    .. testcode::

        from qiskit_qryd_provider import QRydProvider
        from qiskit import QuantumCircuit, execute
        import os

        provider = QRydProvider(os.getenv("QRYD_API_TOKEN"))
        backend = provider.get_backend("qryd_emu_localcomp_triangle")

        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        job = execute(qc, backend, shots=200, optimization_level=3)

    """

    def __init__(self, provider: "qiskit_qryd_provider.QRydProvider") -> None:
        """Initialize the backend.

        Args:
            provider: The provider that this backend comes from.

        """
        super().__init__(
            provider=provider,
            name="qryd_emu_localcomp_triangle",
            backend_version="1.0.0",
        )

        si = 5
        sj = 6
        num_qubits = si * sj

        # Calculate edges
        edges = [[i + si * j, i + si * j + 1] for i in range(si - 1) for j in range(sj)]
        edges += [
            [i + si * j + 1, i + si * j] for i in range(si - 1) for j in range(sj)
        ]
        edges += [
            [i + si * j, i + si * j + si]
            for i in range(si)
            for j in range(0, sj - 1, 2)
        ]
        edges += [
            [i + si * j + si, i + si * j]
            for i in range(si)
            for j in range(0, sj - 1, 2)
        ]
        edges += [
            [i + si * j, i + si * j + si - 1]
            for i in range(1, si)
            for j in range(1, sj - 1, 2)
        ]
        edges += [
            [i + si * j + si - 1, i + si * j]
            for i in range(1, si)
            for j in range(1, sj - 1, 2)
        ]
        edges += [
            [i + si * j, i + si * j + si + 1]
            for i in range(si - 1)
            for j in range(0, sj - 1, 2)
        ]
        edges += [
            [i + si * j + si + 1, i + si * j]
            for i in range(si - 1)
            for j in range(0, sj - 1, 2)
        ]
        edges += [
            [i + si * j, i + si * j + si + 1 - 1]
            for i in range(si - 1 + 1)
            for j in range(1, sj - 1, 2)
        ]
        edges += [
            [i + si * j + si + 1 - 1, i + si * j]
            for i in range(si - 1 + 1)
            for j in range(1, sj - 1, 2)
        ]

        # Create Target
        self._target = Target()

        # Add native gates
        meas_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(Measure(), meas_props)

        lam = Parameter("lambda")
        p_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(PhaseGate(lam), p_props)

        theta = Parameter("theta")
        phi = Parameter("phi")
        r_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RGate(theta, phi), r_props)

        theta = Parameter("theta")
        rx_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RXGate(theta), rx_props)

        theta = Parameter("theta")
        ry_props = {(qubit,): InstructionProperties() for qubit in range(num_qubits)}
        self._target.add_instruction(RYGate(theta), ry_props)

        pcz_props = {tuple(edge): InstructionProperties() for edge in edges}
        self._target.add_instruction(PCZGate(), pcz_props)
