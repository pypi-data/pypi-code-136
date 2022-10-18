from typing import List, Optional, Union, _GenericAlias  # type: ignore[attr-defined]

from classiq.interface.generator.arith.arithmetic import RegisterUserInput
from classiq.interface.generator.synthesis_metrics import MetricsRegisterRole as Role

from classiq.exceptions import ClassiqQRegError


# This class is used for QReg, to support type-hint initialization
#   Due to the `size` property of QReg
class _GenericAliasWithSize(_GenericAlias, _root=True):  # type: ignore[call-arg]
    def __call__(self, *args, **kwargs):
        if self.size is not None:
            return super().__call__(*args, size=self.size, **kwargs)
        else:
            return super().__call__(*args, **kwargs)

    @property
    def role(self) -> Optional[Role]:
        return getattr(self.__origin__, "role", None)

    @property
    def size(self) -> Optional[int]:
        if len(self.__args__) == 1 and type(self.__args__[0]) is int:
            return self.__args__[0]
        return None


class Qubit:
    pass


class QReg:
    """Represents a logical sequence of qubits.
    The QReg can be used as an `in_wires` or `out_wires` argument to ModelDesigner function calls,
    assisting in model connectivity.
    """

    def __init__(self, size: int) -> None:
        """Initializes a new QReg with the specified number of qubits.

        Args:
            size (int): The number of qubits in the QReg.
        """
        if size <= 0:
            raise ClassiqQRegError(f"Cannot create {size} new qubits")
        self._qubits = [Qubit() for _ in range(size)]

    @classmethod
    def _from_qubits(cls, qubits: List[Qubit]) -> "QReg":
        if (
            not isinstance(qubits, list)
            or not all(isinstance(qubit, Qubit) for qubit in qubits)
            or len(qubits) == 0
        ):
            raise ClassiqQRegError(f"Cannot create QReg from {qubits}")
        qreg = cls(size=1)
        qreg._qubits = qubits
        return qreg

    def __getitem__(self, key: Union[int, slice]) -> "QReg":
        state = self._qubits[key]
        return QReg._from_qubits(state if isinstance(state, list) else [state])

    def __setitem__(self, key: Union[int, slice], value: "QReg") -> None:
        if isinstance(key, int) and len(value) != 1:
            raise ClassiqQRegError(
                f"Size mismatch: value size {len(value)}, expected size 1"
            )
        self._qubits[key] = value._qubits[0] if isinstance(key, int) else value._qubits  # type: ignore[call-overload]

    def __eq__(self, other) -> bool:
        return isinstance(other, QReg) and self._qubits == other._qubits

    @classmethod
    def concat(cls, left: "QReg", right: "QReg") -> "QReg":
        """Concatenate two QRegs.

        Args:
            left: The LHS QReg of the concatenation.
            right: The RHS QReg of the concatenation.

        Returns:
            A QReg representing the concatenation of the two given QRegs.

        """
        return cls._from_qubits(left._qubits + right._qubits)

    def __len__(self) -> int:
        return len(self._qubits)

    @property
    def qubits(self) -> List[Qubit]:
        return self._qubits

    def __class_getitem__(cls, params):
        # Supporting python 3.7+, thus returning `typing._GenericAlias` instead of `types.GenericAlias`
        if type(params) is int:
            return _GenericAliasWithSize(cls, params, inst=True, special=False)

        raise ClassiqQRegError(f"Invalid size: {params} ; int required")


# QReg with arithmetic properties
class QSFixed(QReg):
    is_signed: bool = True

    def __init__(self, size: int, fraction_places: int) -> None:
        self.fraction_places: int = fraction_places
        super().__init__(size=size)

    def to_register_user_input(self) -> RegisterUserInput:
        return RegisterUserInput(
            size=len(self),
            is_signed=self.is_signed,
            fraction_places=self.fraction_places,
        )


QFixed = QSFixed


class QUFixed(QFixed):
    is_signed: bool = False


class QSInt(QFixed):
    def __init__(self, size: int):
        super().__init__(size=size, fraction_places=0)


QInt = QSInt


class QUInt(QInt):
    is_signed: bool = False


# QReg with synthesis properties
class ZeroQReg(QReg):
    role: Role = Role.ZERO
    wire_to_zero: bool = True


class AuxQReg(ZeroQReg):
    role: Role = Role.AUXILIARY
