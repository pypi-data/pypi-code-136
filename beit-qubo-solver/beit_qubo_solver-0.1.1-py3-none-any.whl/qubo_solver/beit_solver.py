from itertools import chain
from time import sleep
from typing import Any, Dict, Hashable, List, Mapping, Tuple, Union

import dimod
from dimod.exceptions import BinaryQuadraticModelStructureError
import numpy as np

from beit.qubo_solver.architecture import make_chimera_architecture
from beit.qubo_solver.qubo_instance import QuboInstance
from beit.qubo_solver.solver_connection import JobStatus, SolverConnection


class BEITSolver(dimod.Sampler, dimod.Structured):
    """
    This is an exact solver for QUBO. It works only with
    chimera architecture (max size being (8, 16, 4))
    """

    _TARGET_ARCHITECTURE = make_chimera_architecture()

    def __init__(self, solver_connection: SolverConnection):
        self._connection = solver_connection

    @property
    def edgelist(self) -> List[Tuple[Hashable, Hashable]]:
        return list(self._TARGET_ARCHITECTURE.edges)

    @property
    def nodelist(self) -> List[Hashable]:
        return list(self._TARGET_ARCHITECTURE.nodes)

    @property
    def parameters(self) -> Dict[str, Any]:
        return {}

    @property
    def properties(self) -> Dict[str, Any]:
        return {}

    def _check_instance_valid(self, qubo_instance: QuboInstance):
        wrong_nodes = set(chain.from_iterable(qubo_instance.keys())) - set(self.nodelist)
        if wrong_nodes:
            raise BinaryQuadraticModelStructureError(
                f"The following variables are not present in the nodelist: {' '.join(map(str, wrong_nodes))}"
            )
        wrong_edges = set(qubo_instance.keys()) - set(self.edgelist)
        if wrong_edges:
            raise BinaryQuadraticModelStructureError(
                f"The following edges are not present in the edgelist: {' '.join(map(str, wrong_edges))}"
            )

    def sample_qubo(self, qubo_instance: QuboInstance, **parameters):
        self._check_instance_valid(qubo_instance)
        job = self._connection.create_job(qubo_instance)
        while job.request_result() == JobStatus.PENDING:
            sleep(0.5) # Arbitrary number
        assert job.status == JobStatus.DONE # Otherwise it should've throw earlier.
        assert job.result is not None
        states = [result.state for result in job.result]
        energies = [result.energy for result in job.result]
        return dimod.SampleSet.from_samples(states, dimod.Vartype.BINARY, energies)
