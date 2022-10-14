from typing import Any, Optional, Union, Type

# Explicit conversion support
VType = Union[Type[str], Type[int], Type[float], Type[bool]]


class Backend:
    """
    Base class representing a key-value store/backend.
    """

    name: str

    def get(self, key: str, v_type: VType = str, **kwargs) -> Optional[VType]:
        """
        Returns value found at key in key-value backend.
        Type conversion is handled by _cast method.
        """
        return self._cast(self._get(key, **kwargs), v_type, **kwargs)

    def _get(self, key: str, **kwargs) -> Optional[VType]:
        """
        Returns raw value found at key in key-value backend.
        Defaults to None if key not found in store.
        """
        return NotImplementedError

    def _cast(self, v: Any, v_type: VType = str, **kwargs) -> Optional[VType]:
        """
        Convert value into type as defined by kwargs['type'] parameter.
        Supported types defined in VType = Union[str, bool, float, int].
        Default conversion type is `str`.
        If value is None, returns None.
        """
        if v_type not in [str, bool, float, int]:
            raise Exception(
                f"Unsupported type {v_type} conversion. Support for {VType}"
            )

        if v is None:
            return v

        if isinstance(v, v_type):
            # Right type
            return v

        # Mismatch: value is not None and type is incorrect
        if isinstance(v, str):
            if v_type == bool:
                v = True if "t" in v.lower() else False
                return v
            if v_type == int:
                v = int(v)
                return v
            if v_type == float:
                v = float(v)
                return v

        else:
            raise Exception(
                "Type conversion cannot be achieved when input variable is not a string"
            )
