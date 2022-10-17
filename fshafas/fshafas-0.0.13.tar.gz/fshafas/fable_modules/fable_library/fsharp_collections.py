from typing import (TypeVar, Callable, Any, Optional, Literal)
from .util import (IEqualityComparer_1, structural_hash, equals, physical_hash, IComparer_1, compare)

_T = TypeVar("_T")

_T_ = TypeVar("_T_")

def HashIdentity_FromFunctions(hash_1: Callable[[_T], int], eq: Callable[[_T, _T], bool]) -> IEqualityComparer_1[Any]:
    class ObjectExpr0(IEqualityComparer_1[Any]):
        def Equals(self, x: _T_, y: _T_, hash_1: Callable[[_T], int]=hash_1, eq: Callable[[_T, _T], bool]=eq) -> bool:
            return eq(x, y)

        def GetHashCode(self, x_1: Optional[_T_]=None, hash_1: Callable[[_T], int]=hash_1, eq: Callable[[_T, _T], bool]=eq) -> int:
            return hash_1(x_1)

    return ObjectExpr0()


def HashIdentity_Structural(__unit: Literal[None]=None) -> IEqualityComparer_1[Any]:
    def _arrow1(obj: Optional[_T]=None) -> int:
        return structural_hash(obj)

    def _arrow2(e: _T, e_1: _T) -> bool:
        return equals(e, e_1)

    return HashIdentity_FromFunctions(_arrow1, _arrow2)


def HashIdentity_Reference(__unit: Literal[None]=None) -> IEqualityComparer_1[Any]:
    def _arrow3(obj: Optional[_T]=None) -> int:
        return physical_hash(obj)

    def _arrow4(e: _T, e_1: _T) -> bool:
        return e == e_1

    return HashIdentity_FromFunctions(_arrow3, _arrow4)


def ComparisonIdentity_FromFunction(comparer: Callable[[_T, _T], int]) -> IComparer_1[_T]:
    class ObjectExpr5(IComparer_1[_T_]):
        def Compare(self, x: _T_, y: _T_, comparer: Callable[[_T, _T], int]=comparer) -> int:
            return comparer(x, y)

    return ObjectExpr5()


def ComparisonIdentity_Structural(__unit: Literal[None]=None) -> IComparer_1[Any]:
    def _arrow6(e: _T, e_1: _T) -> int:
        return compare(e, e_1)

    return ComparisonIdentity_FromFunction(_arrow6)


__all__ = ["HashIdentity_FromFunctions", "HashIdentity_Structural", "HashIdentity_Reference", "ComparisonIdentity_FromFunction", "ComparisonIdentity_Structural"]

