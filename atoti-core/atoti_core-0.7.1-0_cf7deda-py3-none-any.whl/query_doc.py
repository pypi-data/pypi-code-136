QUERY_DOC = """Query the cube to retrieve the value of the passed measures on the given levels.

        In JupyterLab with the :mod:`atoti-jupyterlab <atoti_jupyterlab>` plugin installed, query results can be converted to interactive widgets with the :guilabel:`Convert to Widget Below` action available in the command palette or by right clicking on the representation of the returned Dataframe.

        {args}
"""

QUERY_ARGS_DOC = {
    "mode": """mode: The query mode.""",
    "pretty": """* ``"pretty"`` is best for queries returning small results:

                * A :class:`atoti_query.QueryResult` will be returned and its rows will be sorted according to the level order.""",
    "raw": """*  ``"raw"`` is best for benchmarks or large exports:

                * A faster and more efficient endpoint reducing the data transfer from Java to Python will be used.
                * A classic :class:`pandas.DataFrame` will be returned.
                * ``include_totals="True"`` will not be allowed.
                * The :guilabel:`Convert to Widget Below` action provided by the :mod:`atoti-jupyterlab <atoti_jupyterlab>` plugin will not be available.""",
    "timeout": """timeout: The amount of time the query execution can take before aborting it.""",
    "totals": """Totals can be useful but they make the DataFrame harder to work with since its index will have some empty values.""",
    "context": """context: Context values to use when executing the query.""",
}


def get_query_args_doc(*, is_query_session: bool) -> str:
    lines = (
        [
            'session = tt.QuerySession(f"http://localhost:{session.port}")',
            "cube = session.cubes[cube.name]",
        ]
        if is_query_session
        else []
    ) + ["h, l, m = cube.hierarchies, cube.levels, cube.measures"]
    example_lines = "\n                        ".join([f">>> {line}" for line in lines])
    default_context = (
        "\n\n                Defaults to :attr:`atoti.Cube.shared_context`."
    )

    return f"""Args:
            measures: The measures to query.
            filter: The filtering condition.
                Only conditions on level equality with a string are supported.

                Examples:

                    .. doctest:: query

                        >>> df = pd.DataFrame(
                        ...     columns=["Continent", "Country", "Currency", "Price"],
                        ...     data=[
                        ...         ("Europe", "France", "EUR", 200.0),
                        ...         ("Europe", "Germany", "EUR", 150.0),
                        ...         ("Europe", "United Kingdom", "GBP", 120.0),
                        ...         ("America", "United states", "USD", 240.0),
                        ...         ("America", "Mexico", "MXN", 270.0),
                        ...     ],
                        ... )
                        >>> table = session.read_pandas(
                        ...     df,
                        ...     keys=["Continent", "Country", "Currency"],
                        ...     table_name="Prices",
                        ... )
                        >>> cube = session.create_cube(table)
                        >>> del cube.hierarchies["Continent"]
                        >>> del cube.hierarchies["Country"]
                        >>> cube.hierarchies["Geography"] = [
                        ...     table["Continent"],
                        ...     table["Country"],
                        ... ]
                        {example_lines}

                        >>> cube.query(
                        ...     m["Price.SUM"],
                        ...     levels=[l["Country"]],
                        ...     filter=l["Continent"] == "Europe",
                        ... )
                                                 Price.SUM
                        Continent Country
                        Europe    France            200.00
                                  Germany           150.00
                                  United Kingdom    120.00


                        >>> cube.query(
                        ...     m["Price.SUM"],
                        ...     levels=[l["Country"], l["Currency"]],
                        ...     filter=(
                        ...         (l["Continent"] == "Europe")
                        ...         & (l["Currency"] == "EUR")
                        ...     ),
                        ... )
                                                   Price.SUM
                        Continent Country Currency
                        Europe    France  EUR         200.00
                                  Germany EUR         150.00

                        >>> cube.query(
                        ...     m["Price.SUM"],
                        ...     levels=[l["Country"]],
                        ...     filter=h["Geography"].isin(
                        ...         ("America",), ("Europe", "Germany")
                        ...     ),
                        ... )
                                                Price.SUM
                        Continent Country
                        America   Mexico           270.00
                                  United states    240.00
                        Europe    Germany          150.00

            include_totals: Whether the returned DataFrame should include the grand total and subtotals.
                {QUERY_ARGS_DOC["totals"]}

                Example:

                    .. doctest:: query

                            >>> cube.query(
                            ...     m["Price.SUM"],
                            ...     levels=[l["Country"], l["Currency"]],
                            ...     include_totals=True,
                            ... )
                                                              Price.SUM
                            Continent Country        Currency
                            Total                                980.00
                            America                              510.00
                                      Mexico                     270.00
                                                     MXN         270.00
                                      United states              240.00
                                                     USD         240.00
                            Europe                               470.00
                                      France                     200.00
                                                     EUR         200.00
                                      Germany                    150.00
                                                     EUR         150.00
                                      United Kingdom             120.00
                                                     GBP         120.00

            levels: The levels to split on.
                If ``None``, the value of the measures at the top of the cube is returned.
            scenario: The scenario to query.
            {QUERY_ARGS_DOC["timeout"]}
            {QUERY_ARGS_DOC["mode"]}

              {QUERY_ARGS_DOC["pretty"]}

                Example:

                    .. doctest:: query

                        >>> cube.query(
                        ...     m["Price.SUM"],
                        ...     levels=[l["Continent"]],
                        ...     mode="pretty",
                        ... )
                                  Price.SUM
                        Continent
                        America      510.00
                        Europe       470.00

              {QUERY_ARGS_DOC["raw"]}

                Example:

                    .. doctest:: query

                        >>> cube.query(
                        ...     m["Price.SUM"],
                        ...     levels=[l["Continent"]],
                        ...     mode="raw",
                        ... )
                          Continent  Price.SUM
                        0    Europe      470.0
                        1   America      510.0

            {QUERY_ARGS_DOC["context"] if is_query_session else QUERY_ARGS_DOC["context"] + default_context}
"""
