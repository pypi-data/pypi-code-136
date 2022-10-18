import time
from contextlib import suppress
from typing import TYPE_CHECKING

import requests
from qiskit.providers import JobError
from qiskit.providers import JobTimeoutError
from qiskit.providers import JobV1 as Job
from qiskit.providers.jobstatus import JobStatus
from qiskit.result import Result

if TYPE_CHECKING:
    import qiskit
    import qiskit_qryd_provider


class QRydJob(Job):
    """Job that is run on `QRydDemo`_'s infrastructure.

    .. _QRydDemo: https://thequantumlaend.de/qryddemo/

    This class provides methods for controlling the job, accessing its status and
    result. The class communicates with QRydDemo's infrastructure via our `web API
    <https://api.qryddemo.itp3.uni-stuttgart.de/docs>`_.
    The job runs asynchronously.

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

        print(job.result().get_counts())

    .. testoutput::
        :hide:

        ...

    """

    _async = True

    def __init__(
        self,
        backend: "qiskit_qryd_provider.QRydBackend",
        job_url: str,
        session: requests.Session,
        options: "qiskit.providers.Options",
        circuit: "qiskit.QuantumCircuit",
    ) -> None:
        """Initializes the asynchronous job.

        Args:
            backend: The backend used to run the job.
            job_url: URL to the API endpoint that points to the job created on the
                server.
            session: Session object that manages the connection to the API server.
            options: Options specified within the used backend.
            circuit: The QuantumCircuit that is submitted as a job.

        """
        super().__init__(backend, job_url.split("/")[-1])

        self._session = session
        self._job_url = job_url
        self._circuit = circuit
        self._memory = options.memory
        self._shots = options.shots

    def submit(self) -> None:
        """Not implemented.

        Please use :func:`QRydSimulator.run()
        <qiskit_qryd_provider.QRydSimulator.run>` or
        :external+qiskit:py:func:`~qiskit.execute_function.execute` to submit a job.

        Raises:
            NotImplementedError: If the method is called.

        """
        raise NotImplementedError("Please use QRydSimulator.run() to submit a job.")

    def cancel(self) -> bool:
        """Attempt to cancel the job.

        Returns:
            A boolean that indicates whether the cancellation has been successful.

        """
        response = self._session.delete(self._job_url)
        return response.status_code == 200

    def status(self) -> JobStatus:
        """Return the status of the job.

        Returns:
            The status.

        """
        result = self._get_job_status(self._job_url, self._session)
        if result["status"] == "running":
            status = JobStatus.RUNNING
        elif result["status"] == "completed":
            status = JobStatus.DONE
        elif result["status"] == "pending":
            status = JobStatus.QUEUED
        elif result["status"] == "cancelled":
            status = JobStatus.CANCELLED
        elif result["status"] == "initializing" or result["status"] == "compiling":
            status = JobStatus.INITIALIZING
        elif result["status"] == "completing":
            status = JobStatus.VALIDATING
        else:
            status = JobStatus.ERROR
        return status

    def result(self, timeout: float = None, wait: float = 0.2) -> Result:
        """Return the result of the job.

        Args:
            timeout: Time after which the method times out.
            wait: Time for which the method sleeps before making a new attempt to get
                the results from the web API.

        Raises:
            qiskit.providers.JobTimeoutError: If the method timed out.
            qiskit.providers.JobError: If the job failed.
            requests.HTTPError: If the web API did not accept a request.

        Returns:
            A Qiskit result object that contains the measurement outcomes.

            In addition, after converting the object to a dictionary,
            we can access the metadata of the job:
            :code:`meta = job.result().to_dict()["results"][0]["metadata"]`.

            * :code:`meta["device"]`:
              The device on which the job has been executed.
            * :code:`meta["method"]`:
              How the job has been executed.
            * :code:`meta["noise"]`:
              Details about the noise model.
            * :code:`meta["precision"]`:
              The considered numerical precision.
            * :code:`meta["num_qubits"]`:
              Number of qubits.
            * :code:`meta["num_clbits"]`:
              Number of classical bits.
            * :code:`meta["executed_single_qubit_gates"]`:
              Number of single-qubit gates.
            * :code:`meta["executed_two_qubit_gates"]`:
              Number of two-qubit gates.
            * :code:`meta["fusion_max_qubits"]`:
              Maximum number of fused gates.
            * :code:`meta["fusion_avg_qubits"]`:
              Average number of fused gates.
            * :code:`meta["fusion_generated_gates"]`:
              Number of gates after gate fusion.

            Moreover, we can read out the execution time
            :code:`job.result().to_dict()["results"][0]["time_taken"]`
            and the number of measurements performed
            :code:`job.result().to_dict()["results"][0]["shots"]`.

            If the circuit has been compiled in our cloud, we can obtain the
            compilation time via
            :code:`job.result().to_dict()["results"][0]["compilation_time"]`.

        .. .. # noqa: DAR402

        """
        result = self._wait_for_result(timeout, wait)
        return Result.from_dict(
            {
                "results": [
                    {
                        "success": True,
                        "metadata": {
                            "noise": result["noise"],
                            "method": result["method"],
                            "device": result["device"],
                            "precision": result["precision"],
                            "num_qubits": result["num_qubits"],
                            "num_clbits": result["num_clbits"],
                            "fusion_max_qubits": result["fusion_max_qubits"],
                            "fusion_avg_qubits": result["fusion_avg_qubits"],
                            "fusion_generated_gates": result["fusion_generated_gates"],
                            "executed_single_qubit_gates": result[
                                "executed_single_qubit_gates"
                            ],
                            "executed_two_qubit_gates": result[
                                "executed_two_qubit_gates"
                            ],
                        },
                        "shots": self._shots,
                        "data": result["data"],
                        "time_taken": result["time_taken"],
                        "compilation_time": result["compilation_time"],
                        "header": {
                            "memory_slots": self._circuit.num_clbits,
                            "name": self._circuit.name,
                        },
                    }
                ],
                "backend_name": self._backend.name,
                "backend_version": self._backend.backend_version,
                "job_id": self._job_id,
                "qobj_id": id(self._circuit),
                "success": True,
            }
        )

    def _wait_for_result(self, timeout: float = None, wait: float = 0.2) -> dict:
        """Wait for the result of the job.

        Args:
            timeout: Time after which the method times out.
            wait: Time for which the method sleeps before making a new attempt to get
                the results from the web API.

        Raises:
            JobTimeoutError: If the method timed out.
            JobError: If the job failed.
            requests.exceptions.HTTPError: If the web API did not accept a request.

        .. .. # noqa: DAR402

        Returns:
            A result object.

        """
        start_time = time.time()
        while True:
            elapsed = time.time() - start_time
            if timeout and elapsed >= timeout:
                raise JobTimeoutError("Timed out waiting for result")
            result = self._get_job_status(self._job_url, self._session)
            if result["status"] == "completed":
                break
            if result["status"] == "error":
                if result["msg"]:
                    raise JobError(f"Job error ({result['msg']})")
                else:
                    raise JobError("Job error")
            time.sleep(wait)
        return self._get_job_result(self._job_url, self._session)

    def _get_job_status(self, job_url: str, session: requests.Session) -> dict:
        """Ask the web API for the status of the job.

        Args:
            job_url: URL to the API endpoint that points to the job created on the
                server.
            session: Session object that manages the connection to the API server.

        Raises:
            requests.HTTPError: If the web API did not accept the request.

        Returns:
            The response of the web API.

        .. .. # noqa: DAR401
        .. .. # noqa: DAR402

        """
        response = session.get(job_url + "/status")
        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            with suppress(BaseException):
                error = requests.HTTPError(
                    f"{error} ({error.response.json()['detail']})"
                )
            raise error
        return response.json()

    def _get_job_result(self, job_url: str, session: requests.Session) -> dict:
        """Ask the web API for the result of the job.

        Args:
            job_url: URL to the API endpoint that points to the job created on the
                server.
            session: Session object that manages the connection to the API server.

        Raises:
            requests.HTTPError: If the web API did not accept the request.

        Returns:
            The response of the web API.

        .. .. # noqa: DAR401
        .. .. # noqa: DAR402

        """
        response = session.get(job_url + "/result")
        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            with suppress(BaseException):
                error = requests.HTTPError(
                    f"{error} ({error.response.json()['detail']})"
                )
            raise error
        return response.json()
