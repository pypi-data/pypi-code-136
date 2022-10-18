from typing import List

import requests
from qiskit.providers import ProviderV1 as Provider
from qiskit.providers import QiskitBackendNotFoundError
from qiskit.providers.providerutils import filter_backends

from .qryd_backend import QRydBackend
from .qryd_backend import QRydEmuCloudcompSquare
from .qryd_backend import QRydEmuCloudcompTriangle
from .qryd_backend import QRydEmuLocalcompSquare
from .qryd_backend import QRydEmuLocalcompTriangle


class QRydProvider(Provider):
    """Provider for backends from the `QRydDemo`_ consortium.

    .. _QRydDemo: https://thequantumlaend.de/qryddemo/

    This class provides backends for accessing QRydDemo's cloud infrastructure with
    Qiskit. To access the infrastructure, a valid API token is required. The token can
    be obtained via our `online registration form
    <https://thequantumlaend.de/frontend/signup_form.php>`_.

    Different backends are available that are capable of running ideal simulations of
    quantum circuits on the GPU-based emulator of the QRydDemo consortium. An inclusion
    of noise models is planned for the future. Currently, the following backends are
    provided:

    * :class:`~qiskit_qryd_provider.QRydEmuLocalcompSquare`:
      emulator of 30 ideal qubits arranged in a 5x6 square lattice with
      nearest-neighbor connectivity, quantum circuits are compiled to the gate set of
      the Rydberg platform by Qiskit.
    * :class:`~qiskit_qryd_provider.QRydEmuLocalcompTriangle`:
      emulator of 30 ideal qubits arranged in a triangle lattice with
      nearest-neighbor connectivity, quantum circuits are compiled to the gate set of
      the Rydberg platform by Qiskit.
    * :class:`~qiskit_qryd_provider.QRydEmuCloudcompSquare`:
      emulator of 30 ideal qubits arranged in a 5x6 square lattice with
      nearest-neighbor connectivity, quantum circuits are compiled to the gate set of
      the Rydberg platform on our servers after submitting the circuits to QRydDemo's
      infrastructure.
    * :class:`~qiskit_qryd_provider.QRydEmuCloudcompTriangle`:
      emulator of 30 ideal qubits arranged in a triangle lattice with
      nearest-neighbor connectivity, quantum circuits are compiled to the gate set of
      the Rydberg platform on our servers after submitting the circuits to QRydDemo's
      infrastructure.

    Typical usage example:

    .. testcode::

        from qiskit_qryd_provider import QRydProvider
        import os

        provider = QRydProvider(os.getenv("QRYD_API_TOKEN"))
        backend = provider.get_backend("qryd_emu_localcomp_square")

    """

    def __init__(self, token: str) -> None:
        """Initialize the provider.

        Args:
            token: The QrydDemo Api token that can be obtained via our `online
                registration form
                <https://thequantumlaend.de/frontend/signup_form.php>`__.

        """
        super().__init__()
        self.session = requests.Session()
        self.session.headers.update({"X-API-Key": token})

    def get_backend(self, name: str = None, **kwargs) -> QRydBackend:
        """Return a single backend matching the specified filtering.

        Args:
            name: Name of the backend.
            **kwargs: Dict used for filtering.

        Returns:
            A backend matching the filtering.

        Raises:
            qiskit.providers.QiskitBackendNotFoundError: If no backend could be found or
                more than one backend matches the filtering criteria.

        .. # noqa: DAR401
        .. # noqa: DAR402

        """
        backends = self.backends(name, **kwargs)
        if len(backends) > 1:
            raise QiskitBackendNotFoundError("More than one backend matches criteria.")
        if not backends:
            raise QiskitBackendNotFoundError("No backend matches criteria.")

        return backends[0]

    def backends(self, name: str = None, **kwargs) -> List[QRydBackend]:
        """Return a list of backends matching the specified filtering.

        Args:
            name: Name of the backend.
            **kwargs: Dict used for filtering.

        Returns:
            A list of backends that match the filtering criteria.

        """
        backends = [
            QRydEmuCloudcompSquare(provider=self),
            QRydEmuCloudcompTriangle(provider=self),
            QRydEmuLocalcompSquare(provider=self),
            QRydEmuLocalcompTriangle(provider=self),
        ]  # type: List[QRydBackend]
        if name:
            backends = [backend for backend in backends if backend.name == name]
        return filter_backends(backends, **kwargs)
