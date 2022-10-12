from __future__ import annotations

from dataclasses import dataclass, field
from typing import (
    Any,
    Collection,
    Dict,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Optional,
    Protocol,
    Union,
)

import pandas as pd
from atoti_core import (
    BASE_SCENARIO_NAME,
    EMPTY_MAPPING,
    DataType,
    ImmutableMapping,
    IPythonKeyCompletions,
    LevelCoordinates,
    ReprJson,
    ReprJsonable,
    get_ipython_key_completions_for_mapping,
    is_temporal_type,
    keyword_only_dataclass,
)
from atoti_query import _ExecuteGaq, _QueryMdx
from typeguard import typechecked, typeguard_ignore

from ._aggregate_provider_description import AggregateProviderDescription
from ._hierarchy_arguments import HierarchyArguments
from ._java_api import JavaApi
from ._local_cube import LocalCube
from .agg import single_value
from .aggregate_provider import (
    AggregateProvider,
    AggregateProviders,
    to_python_condition,
)
from .aggregates_cache import AggregatesCache
from .column import Column
from .hierarchies import Hierarchies
from .hierarchy import Hierarchy
from .level import Level
from .levels import Levels
from .measures import Measures
from .table import Table
from .type import INT, DataType


class _ReadPandas(Protocol):
    def __call__(
        self,
        dataframe: pd.DataFrame,
        /,
        *,
        table_name: str,
        keys: Iterable[str] = (),
        partitioning: Optional[str] = None,
        types: Mapping[str, DataType] = EMPTY_MAPPING,
        **kwargs: Any,
    ) -> Table:
        ...


class Cube(LocalCube[Hierarchies, Levels, Measures]):
    """Cube of a :class:`atoti.Session`."""

    @typeguard_ignore
    def __init__(
        self,
        name: str,
        *,
        java_api: JavaApi,
        base_table: Table,
        session_name: Optional[str],
        query_mdx: _QueryMdx,
        execute_gaq: _ExecuteGaq,
        read_pandas: _ReadPandas,
    ):
        super().__init__(
            name,
            java_api=java_api,
            session_name=session_name,
            hierarchies=Hierarchies(
                _java_api=java_api,
                _cube_name=name,
                _create_hierarchy_from_arguments=self._create_hierarchy_from_arguments,
            ),
            level_function=lambda hierarchies: Levels(hierarchies),
            measures=Measures(java_api=java_api, cube_name=name),
            agg_cache=AggregatesCache(
                _cube_name=name,
                _set_capacity=java_api.set_aggregates_cache_capacity,
                _get_capacity=java_api.get_aggregates_cache_capacity,
            ),
            query_mdx=query_mdx,
            execute_gaq=execute_gaq,
        )
        self._base_table = base_table
        self._shared_context = CubeContext(_java_api=java_api, _cube=self)
        self._read_pandas = read_pandas
        self._aggregate_providers = AggregateProviders(
            cube_name=self.name,
            get_aggregate_provider=self._get_aggregate_provider,
            java_api=java_api,
        )

    @property
    def schema(self) -> Any:
        """Schema of the cube's tables, as an SVG image in IPython, as a path to the image otherwise.

        Note:
            This requires `Graphviz <https://www.graphviz.org>`__ to be installed.

        """
        return self._java_api.generate_schema_graph(cube_name=self.name)

    @property
    def shared_context(self) -> CubeContext:
        """Context values shared by all the users.

        Context values can also be set at query time, and per user, directly from the UI.
        The values in the shared context are the default ones for all the users.

        * ``queriesTimeLimit``

            The number of seconds after which a running query is cancelled and its resources reclaimed.
            Set to ``-1`` to remove the limit.
            Defaults to 30s.

        * ``queriesResultLimit.intermediateLimit``

            The limit number of point locations for a single intermediate result.
            This works as a safe-guard to prevent queries from consuming too much memory, which is especially useful when going to production with several simultaneous users on the same server.
            Set to ``-1`` to remove the limit.

            Default values are:

                * no limit in atoti.
                * ``1_000_000`` if the :mod:`atoti-plus <atoti_plus>` plugin is enabled.

        * ``queriesResultLimit.transientLimit``

            Similar to *intermediateLimit* but across all the intermediate results of the same query.
            Set to ``-1`` to remove the limit.

            Default values are:

                * no limit in atoti.
                * ``10_000_000`` if the :mod:`atoti-plus <atoti_plus>` plugin is enabled.

        Example:
            >>> df = pd.DataFrame(
            ...     columns=["City", "Price"],
            ...     data=[
            ...         ("London", 240.0),
            ...         ("New York", 270.0),
            ...         ("Paris", 200.0),
            ...     ],
            ... )
            >>> table = session.read_pandas(
            ...     df, keys=["City"], table_name="shared_context example"
            ... )
            >>> cube = session.create_cube(table)
            >>> cube.shared_context["queriesTimeLimit"] = 60
            >>> cube.shared_context["queriesResultLimit.intermediateLimit"] = 1000000
            >>> cube.shared_context["queriesResultLimit.transientLimit"] = 10000000
            >>> cube.shared_context
            {'queriesTimeLimit': '60', 'queriesResultLimit.transientLimit': '10000000', 'queriesResultLimit.intermediateLimit': '1000000'}

        """
        return self._shared_context

    def _get_aggregate_provider(
        self,
        description: AggregateProviderDescription,
        /,
    ) -> AggregateProvider:
        return AggregateProvider(
            key=description.key,
            levels=[
                self.levels[level_coordinates.key]
                for level_coordinates in description.levels_coordinates
            ],
            measures=[
                self.measures[measure_name]
                for measure_name in description.measures_names
            ],
            filter=to_python_condition(
                {
                    level_coordinates: tuple(values)
                    for level_coordinates, values in description.filters.items()
                }
            ),
            partitioning=description.partitioning,
        )

    @property
    def aggregate_providers(self) -> MutableMapping[str, AggregateProvider]:
        return self._aggregate_providers

    def _join_distributed_cluster(
        self, distributed_session_url: str, distributed_cube_name: str
    ) -> None:
        """Join the distributed cluster at the given address for the given distributed cube."""

        self._java_api.join_distributed_cluster(
            cube_name=self.name,
            distributed_session_url=distributed_session_url,
            distributed_cube_name=distributed_cube_name,
        )
        self._java_api.refresh()

    def _get_level_data_types(
        self, levels_coordinates: Iterable[LevelCoordinates]
    ) -> Dict[LevelCoordinates, DataType]:
        return {
            level_coordinates: (
                "Object"
                if level_coordinates == LevelCoordinates("Epoch", "Epoch", "Branch")
                else self.levels[level_coordinates.key].data_type
            )
            for level_coordinates in levels_coordinates
        }

    def create_parameter_simulation(
        self,
        name: str,
        *,
        measures: Optional[
            Mapping[str, Optional[Union[float, int, Iterable[int], Iterable[float]]]]
        ] = None,
        levels: Iterable[Level] = (),
        base_scenario_name: str = BASE_SCENARIO_NAME,
    ) -> Table:
        """Create a parameter simulation and its associated measures.

        Args:
            name: The name of the simulation.
              This is also the name of the corresponding table that will be created.
            measures: The mapping from the names of the created measures to their default value.
            levels: The levels to simulate on.
            base_scenario_name: The name of the base scenario.

        Example:

            >>> sales_table = session.read_csv(
            ...     f"{TUTORIAL_RESOURCES}/sales.csv",
            ...     table_name="Sales",
            ...     keys=["Sale ID"],
            ... )
            >>> shops_table = session.read_csv(
            ...     f"{TUTORIAL_RESOURCES}/shops.csv",
            ...     table_name="Shops",
            ...     keys=["Shop ID"],
            ... )
            >>> sales_table.join(shops_table, mapping={"Shop": "Shop ID"})
            >>> cube = session.create_cube(sales_table)
            >>> l, m = cube.levels, cube.measures

            Creating a parameter simulation on one level:

            >>> country_simulation = cube.create_parameter_simulation(
            ...     "Country simulation",
            ...     measures={"Country parameter": 1.0},
            ...     levels=[l["Country"]],
            ... )
            >>> country_simulation += ("France crash", "France", 0.8)
            >>> country_simulation.head()
                                  Country parameter
            Scenario     Country
            France crash France                 0.8

            * ``France crash`` is the name of the scenario.
            * ``France`` is the coordinate at which the value will be changed.
            * ``0.8`` is the value the :guilabel:`Country parameter` measure will have in this scenario.

            >>> m["Unparametrized turnover"] = tt.agg.sum(
            ...     sales_table["Unit price"] * sales_table["Quantity"]
            ... )
            >>> m["Turnover"] = tt.agg.sum(
            ...     m["Unparametrized turnover"] * m["Country parameter"],
            ...     scope=tt.OriginScope(l["Country"]),
            ... )
            >>> cube.query(m["Turnover"], levels=[l["Country simulation"]])
                                  Turnover
            Country simulation
            Base                961,463.00
            France crash        889,854.60

            Drilldown to the :guilabel:`Country` level for more details:

            >>> cube.query(
            ...     m["Unparametrized turnover"],
            ...     m["Country parameter"],
            ...     m["Turnover"],
            ...     levels=[l["Country simulation"], l["Country"]],
            ... )
                                       Unparametrized turnover Country parameter    Turnover
            Country simulation Country
            Base               France               358,042.00              1.00  358,042.00
                               USA                  603,421.00              1.00  603,421.00
            France crash       France               358,042.00               .80  286,433.60
                               USA                  603,421.00              1.00  603,421.00

            Creating a parameter simulation on multiple levels:

            >>> size_simulation = cube.create_parameter_simulation(
            ...     "Size simulation",
            ...     measures={"Size parameter": 1.0},
            ...     levels=[l["Country"], l["Shop size"]],
            ... )
            >>> size_simulation += (
            ...     "Going local",
            ...     None,  # ``None`` serves as a wildcard matching any member value.
            ...     "big",
            ...     0.8,
            ... )
            >>> size_simulation += ("Going local", "USA", "small", 1.2)
            >>> m["Turnover"] = tt.agg.sum(
            ...     m["Unparametrized turnover"]
            ...     * m["Country parameter"]
            ...     * m["Size parameter"],
            ...     scope=tt.OriginScope(l["Country"], l["Shop size"]),
            ... )
            >>> cube.query(
            ...     m["Turnover"],
            ...     levels=[l["Size simulation"], l["Shop size"]],
            ... )
                                         Turnover
            Size simulation Shop size
            Base            big        120,202.00
                            medium     356,779.00
                            small      484,482.00
            Going local     big         96,161.60
                            medium     356,779.00
                            small      547,725.20

            When several rules contain ``None``, the one where the first ``None`` appears last takes precedence.

            >>> size_simulation += ("Going France and Local", "France", None, 2)
            >>> size_simulation += ("Going France and Local", None, "small", 10)
            >>> cube.query(
            ...     m["Unparametrized turnover"],
            ...     m["Turnover"],
            ...     levels=[l["Country"], l["Shop size"]],
            ...     filter=l["Size simulation"] == "Going France and Local",
            ... )
                              Unparametrized turnover      Turnover
            Country Shop size
            France  big                     47,362.00     94,724.00
                    medium                 142,414.00    284,828.00
                    small                  168,266.00    336,532.00
            USA     big                     72,840.00     72,840.00
                    medium                 214,365.00    214,365.00
                    small                  316,216.00  3,162,160.00

            Creating a parameter simulation without levels:

            >>> crisis_simulation = cube.create_parameter_simulation(
            ...     "Global Simulation",
            ...     measures={"Global parameter": 1.0},
            ... )
            >>> crisis_simulation += ("Global Crisis", 0.9)
            >>> m["Turnover"] = m["Unparametrized turnover"] * m["Global parameter"]
            >>> cube.query(m["Turnover"], levels=[l["Global Simulation"]])
                                 Turnover
            Global Simulation
            Base               961,463.00
            Global Crisis      865,316.70

            Creating a parameter simulation with multiple measures:

            >>> multi_parameter_simulation = cube.create_parameter_simulation(
            ...     "Price And Quantity",
            ...     measures={
            ...         "Price parameter": 1.0,
            ...         "Quantity parameter": 1.0,
            ...     },
            ... )
            >>> multi_parameter_simulation += ("Price Up Quantity Down", 1.2, 0.8)
            >>> m["Simulated Price"] = (
            ...     tt.agg.single_value(sales_table["Unit price"])
            ...     * m["Price parameter"]
            ... )
            >>> m["Simulated Quantity"] = (
            ...     tt.agg.single_value(sales_table["Quantity"])
            ...     * m["Quantity parameter"]
            ... )
            >>> m["Turnover"] = tt.agg.sum_product(
            ...     m["Simulated Price"],
            ...     m["Simulated Quantity"],
            ...     scope=tt.OriginScope(l["Sale ID"]),
            ... )
            >>> cube.query(m["Turnover"], levels=[l["Price And Quantity"]])
                                      Turnover
            Price And Quantity
            Base                    961,463.00
            Price Up Quantity Down  923,004.48



        """
        if measures is None:
            raise ValueError(
                "At least one measure and its default value must be passed."
            )

        if any(level.name == "Scenario" for level in levels):
            raise ValueError(
                'Levels with the name "Scenario" cannot be used in parameter simulations.'
            )

        self._java_api.create_parameter_simulation(
            cube_name=self.name,
            simulation_name=name,
            levels_coordinates=[level._coordinates for level in levels],
            base_scenario_name=base_scenario_name,
            measures=measures,
        )
        return Table(_name=name, _java_api=self._java_api)

    def create_parameter_hierarchy_from_column(self, name: str, column: Column) -> None:
        """Create a single-level hierarchy which dynamically takes its members from a column.

        Args:
            name: Name given to the created dimension, hierarchy and its single level.
            column: Column from which to take members.

        Example:
            >>> df = pd.DataFrame(
            ...     {
            ...         "Seller": ["Seller_1", "Seller_1", "Seller_2", "Seller_2"],
            ...         "ProductId": ["aBk3", "ceJ4", "aBk3", "ceJ4"],
            ...         "Price": [2.5, 49.99, 3.0, 54.99],
            ...     }
            ... )
            >>> table = session.read_pandas(df, table_name="Seller")
            >>> cube = session.create_cube(table)
            >>> l, m = cube.levels, cube.measures
            >>> cube.create_parameter_hierarchy_from_column(
            ...     "Competitor", table["Seller"]
            ... )
            >>> m["Price"] = tt.agg.single_value(table["Price"])
            >>> m["Competitor price"] = tt.at(
            ...     m["Price"], l["Seller"] == l["Competitor"]
            ... )
            >>> cube.query(
            ...     m["Competitor price"],
            ...     levels=[l["Seller"], l["ProductId"]],
            ... )
                               Competitor price
            Seller   ProductId
            Seller_1 aBk3                  2.50
                     ceJ4                 49.99
            Seller_2 aBk3                  2.50
                     ceJ4                 49.99
            >>> cube.query(
            ...     m["Competitor price"],
            ...     levels=[l["Seller"], l["ProductId"]],
            ...     filter=l["Competitor"] == "Seller_2",
            ... )
                               Competitor price
            Seller   ProductId
            Seller_1 aBk3                  3.00
                     ceJ4                 54.99
            Seller_2 aBk3                  3.00
                     ceJ4                 54.99
        """
        self._java_api.create_analysis_hierarchy(
            name,
            cube_name=self.name,
            table_name=column._table_name,
            column_name=column.name,
        )
        self._java_api.refresh()

    def create_parameter_hierarchy_from_members(
        self,
        name: str,
        members: Collection[Any],
        *,
        data_type: Optional[DataType] = None,
        index_measure_name: Optional[str] = None,
    ) -> None:
        """Create a single-level hierarchy with the given members.

        It can be used as a parameter hierarchy in advanced analyzes.

        Args:
            name: The name of hierarchy and its single level.
            members: The members of the hierarchy.
            data_type: The type with which the members will be stored.
                Automatically inferred by default.
            index_measure_name: The name of the indexing measure to create for this hierarchy, if any.

        Example:
            >>> df = pd.DataFrame(
            ...     {
            ...         "Seller": ["Seller_1", "Seller_2", "Seller_3"],
            ...         "Prices": [
            ...             [2.5, 49.99, 3.0, 54.99],
            ...             [2.6, 50.99, 2.8, 57.99],
            ...             [2.99, 44.99, 3.6, 59.99],
            ...         ],
            ...     }
            ... )
            >>> table = session.read_pandas(df, table_name="Seller prices")
            >>> cube = session.create_cube(table)
            >>> l, m = cube.levels, cube.measures
            >>> cube.create_parameter_hierarchy_from_members(
            ...     "ProductID",
            ...     ["aBk3", "ceJ4", "aBk5", "ceJ9"],
            ...     index_measure_name="Product index",
            ... )
            >>> m["Prices"] = tt.agg.single_value(table["Prices"])
            >>> m["Product price"] = m["Prices"][m["Product index"]]
            >>> cube.query(
            ...     m["Product price"],
            ...     levels=[l["Seller"], l["ProductID"]],
            ... )
                               Product price
            Seller   ProductID
            Seller_1 aBk3               2.50
                     aBk5               3.00
                     ceJ4              49.99
                     ceJ9              54.99
            Seller_2 aBk3               2.60
                     aBk5               2.80
                     ceJ4              50.99
                     ceJ9              57.99
            Seller_3 aBk3               2.99
                     aBk5               3.60
                     ceJ4              44.99
                     ceJ9              59.99

        """
        index_column = f"{name} index"
        parameter_df = pd.DataFrame({name: members})
        types: Dict[str, DataType] = {}
        if index_measure_name is not None:
            parameter_df[index_column] = list(range(len(members)))
            types[index_column] = INT

        if data_type:
            types[name] = data_type
        elif all(
            isinstance(member, int) and -(2**31) <= member < 2**31
            for member in members
        ):
            types[name] = INT

        parameter_table = self._read_pandas(
            parameter_df,
            table_name=name,
            keys=[name],
            types=types,
            is_parameter_table=True,
        )

        self._base_table.join(parameter_table, mapping={})

        if index_measure_name is not None:
            self.measures[index_measure_name] = single_value(
                parameter_table[index_column]
            )

        self.hierarchies[name, name].slicing = True

        self._java_api.refresh()

    def create_date_hierarchy(
        self,
        name: str,
        *,
        column: Column,
        levels: Mapping[str, str] = ImmutableMapping(
            {"Year": "y", "Month": "M", "Day": "d"}
        ),
    ) -> None:
        """Create a multilevel date hierarchy based on a date column.

        The new levels are created by matching a `date pattern <https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/time/format/DateTimeFormatter.html#patterns>`_.
        Here is a non-exhaustive list of patterns that can be used:

            +---------+-----------------------------+---------+-----------------------------------+
            | Pattern | Description                 | Type    | Examples                          |
            +=========+=============================+=========+===================================+
            | y       | Year                        | Integer | ``2001, 2005, 2020``              |
            +---------+-----------------------------+---------+-----------------------------------+
            | yyyy    | 4-digits year               | String  | ``"2001", "2005", "2020"``        |
            +---------+-----------------------------+---------+-----------------------------------+
            | M       | Month of the year (1 based) | Integer | ``1, 5, 12``                      |
            +---------+-----------------------------+---------+-----------------------------------+
            | MM      | 2-digits month              | String  | ``"01", "05", "12"``              |
            +---------+-----------------------------+---------+-----------------------------------+
            | d       | Day of the month            | Integer | ``1, 15, 30``                     |
            +---------+-----------------------------+---------+-----------------------------------+
            | dd      | 2-digits day of the month   | String  | ``"01", "15", "30"``              |
            +---------+-----------------------------+---------+-----------------------------------+
            | w       | Week number                 | Integer | ``1, 12, 51``                     |
            +---------+-----------------------------+---------+-----------------------------------+
            | Q       | Quarter                     | Integer | ``1, 2, 3, 4``                    |
            +---------+-----------------------------+---------+-----------------------------------+
            | QQQ     | Quarter prefixed with Q     | String  | ``"Q1", "Q2", "Q3", "Q4"``        |
            +---------+-----------------------------+---------+-----------------------------------+
            | H       | Hour of day (0-23)          | Integer | ``0, 12, 23``                     |
            +---------+-----------------------------+---------+-----------------------------------+
            | HH      | 2-digits hour of day        | String  | ``"00", "12", "23"``              |
            +---------+-----------------------------+---------+-----------------------------------+
            | m       | Minute of hour              | Integer | ``0, 30, 59``                     |
            +---------+-----------------------------+---------+-----------------------------------+
            | mm      | 2-digits minute of hour     | String  | ``"00", "30", "59"``              |
            +---------+-----------------------------+---------+-----------------------------------+
            | s       | Second of minute            | Integer | ``0, 5, 55``                      |
            +---------+-----------------------------+---------+-----------------------------------+
            | ss      | 2-digits second of minute   | String  | ``"00", "05", "55"``              |
            +---------+-----------------------------+---------+-----------------------------------+

        Args:
            name: The name of the hierarchy to create.
            column: A table column containing a date or a datetime.
            levels: The mapping from the names of the levels to the patterns from which they will be created.

        Example:
            >>> from datetime import date
            >>> df = pd.DataFrame(
            ...     columns=["Date", "Quantity"],
            ...     data=[
            ...         (date(2020, 1, 10), 150.0),
            ...         (date(2020, 1, 20), 240.0),
            ...         (date(2019, 3, 17), 270.0),
            ...         (date(2019, 12, 12), 200.0),
            ...     ],
            ... )
            >>> table = session.read_pandas(
            ...     df, keys=["Date"], table_name="create_date_hierarchy example"
            ... )
            >>> cube = session.create_cube(table)
            >>> l, m = cube.levels, cube.measures
            >>> cube.create_date_hierarchy("Date parts", column=table["Date"])
            >>> cube.query(
            ...     m["Quantity.SUM"],
            ...     include_totals=True,
            ...     levels=[l["Year"], l["Month"], l["Day"]],
            ... )
                            Quantity.SUM
            Year  Month Day
            Total                 860.00
            2019                  470.00
                  3               270.00
                        17        270.00
                  12              200.00
                        12        200.00
            2020                  390.00
                  1               390.00
                        10        150.00
                        20        240.00

            The full date can also be added back as the last level of the hierarchy:

            >>> h = cube.hierarchies
            >>> h["Date parts"] = {**h["Date parts"].levels, "Date": table["Date"]}
            >>> cube.query(
            ...     m["Quantity.SUM"],
            ...     include_totals=True,
            ...     levels=[l["Date parts", "Date"]],
            ... )
                                       Quantity.SUM
            Year  Month Day Date
            Total                            860.00
            2019                             470.00
                  3                          270.00
                        17                   270.00
                            2019-03-17       270.00
                  12                         200.00
                        12                   200.00
                            2019-12-12       200.00
            2020                             390.00
                  1                          390.00
                        10                   150.00
                            2020-01-10       150.00
                        20                   240.00
                            2020-01-20       240.00

            Data inserted into the table after the hierarchy creation will be automatically hierarchized:

            >>> table += (date(2021, 8, 30), 180.0)
            >>> cube.query(
            ...     m["Quantity.SUM"],
            ...     include_totals=True,
            ...     levels=[l["Date parts", "Date"]],
            ...     filter=l["Year"] == "2021",
            ... )
                                       Quantity.SUM
            Year  Month Day Date
            Total                            180.00
            2021                             180.00
                  8                          180.00
                        30                   180.00
                            2021-08-30       180.00

        """
        if not is_temporal_type(column.data_type):
            raise ValueError(
                f"Cannot create a date hierarchy from a column which is not temporal, column `{column.name}` is of type `{column.data_type}`."
            )
        self._java_api.create_date_hierarchy(
            cube_name=self.name,
            table_name=column._table_name,
            field=column.name,
            hierarchy_name=name,
            levels=levels,
        )
        self._java_api.refresh()

    def _create_hierarchy_from_arguments(
        self, arguments: HierarchyArguments
    ) -> Hierarchy:
        hierarchy = Hierarchy(
            _name=arguments.name,
            _levels_arguments=arguments.levels_arguments,
            _dimension=arguments.dimension,
            _slicing=arguments.slicing,
            _cube_name=self.name,
            _java_api=self._java_api,
            _visible=arguments.visible,
            _virtual=arguments.virtual,
        )
        return hierarchy


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class CubeContext(MutableMapping[str, str], ReprJsonable):
    """Manage the shared context of a cube."""

    _java_api: JavaApi = field(repr=False)
    _cube: Cube = field(repr=False)

    def _get_values(self) -> Dict[str, str]:
        return self._java_api.get_shared_context_values(self._cube.name)

    @typechecked
    def __getitem__(self, key: str) -> str:
        return self._get_values()[key]

    @typechecked
    def __setitem__(self, key: str, value: Any) -> None:
        self._java_api.set_shared_context_value(
            cube_name=self._cube.name,
            key=key,
            value=str(value),
        )
        self._java_api.refresh()

    @typechecked
    def __delitem__(self, key: str) -> None:
        raise ValueError("Cannot delete context value.")

    def __iter__(self) -> Iterator[str]:
        return iter(self._get_values())

    def __len__(self) -> int:
        return len(self._get_values())

    def _ipython_key_completions_(self) -> IPythonKeyCompletions:
        return get_ipython_key_completions_for_mapping(self._get_values())

    def __str__(self) -> str:
        return str(self._get_values())

    def __repr__(self) -> str:
        return repr(self._get_values())

    def _repr_json_(self) -> ReprJson:
        return (
            self._get_values(),
            {"expanded": True, "root": "Shared Context Values"},
        )
