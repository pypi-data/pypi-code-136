from typing import Any, Dict, Iterable, Mapping, Optional

from atoti_core import ReprJson, ReprJsonable

from ._delegate_mutable_mapping import DelegateMutableMapping
from ._java_api import JavaApi
from .table import Table


class Tables(DelegateMutableMapping[str, Table], ReprJsonable):
    """Manage the tables."""

    def __init__(self, java_api: JavaApi):
        self._java_api = java_api

    def _repr_json_(self) -> ReprJson:
        return (
            dict(
                sorted(
                    {
                        table.name: table._repr_json_()[0] for table in self.values()
                    }.items()
                )
            ),
            {"expanded": False, "root": "Tables"},
        )

    def _update(self, other: Mapping[str, Table], /) -> None:
        raise NotImplementedError(
            "Use `Session.create_table()` or other methods such as `Session.read_pandas()` to create a table."
        )

    def _get_underlying(self) -> Dict[str, Table]:
        return {
            table_name: self._unchecked_getitem(table_name)
            for table_name in self._java_api.get_table_names()
        }

    def __getitem__(self, key: str, /) -> Table:
        if key not in self._java_api.get_table_names():
            raise KeyError(key)
        return self._unchecked_getitem(key)

    def _unchecked_getitem(self, key: str, /) -> Table:
        return Table(_name=key, _java_api=self._java_api)

    def _delete_keys(self, keys: Optional[Iterable[str]] = None, /) -> None:
        keys = self._default_to_all_keys(keys)
        for key in keys:
            self._java_api.delete_table(key)

    @property
    def schema(self) -> Any:
        """Schema of the tables, as an SVG image in IPython, as a path to the image otherwise.

        Note:
            This requires `Graphviz <https://www.graphviz.org>`__ to be installed.

        """
        return self._java_api.generate_schema_graph()
