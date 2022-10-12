from typing import Mapping

EXPLAIN_QUERY_DOC = """Run the query but, instead of returning its result, return the explanation of how it was executed containing a summary, global timings, and the query plan with all the retrievals.

        See also:
            :meth:`{corresponding_method}` for the roles of the parameters.
        """

CLIENT_SIDE_ENCRYPTION_DOC = {
    "client_side_encryption": """client_side_encryption: The client side encryption configuration to use when loading data."""
}

_COLUMNS_KWARGS = {
    "columns": """columns: Mapping from file column names to table column names.
                When the mapping is not empty, columns of the file absent from the mapping keys will not be loaded.
                Other parameters accepting column names expect to be passed table column names (i.e. values of this mapping) and not file column names.""",
}

CSV_KWARGS = {
    "array_separator": """array_separator: The character separating array elements.

                If not ``None``, any field containing this separator will be parsed as an array.""",
    "encoding": """encoding: The encoding to use to read the CSV.""",
    "path": """path: The path to the CSV file to load.

                ``.gz``, ``.tar.gz`` and ``.zip`` files containing compressed CSV(s) are also supported.

                The path can also be a glob pattern (e.g. ``path/to/directory/**.*.csv``).""",
    "process_quotes": """process_quotes: Whether double quotes should be processed to follow the official CSV specification:

                * ``True``:

                    * Each field may or may not be enclosed in double quotes (however some programs, such as Microsoft Excel, do not use double quotes at all).
                      If fields are not enclosed with double quotes, then double quotes may not appear inside the fields.
                    * A double quote appearing inside a field must be escaped by preceding it with another double quote.
                    * Fields containing line breaks, double quotes, and commas should be enclosed in double-quotes.
                * ``False``: all double-quotes within a field will be treated as any regular character, following Excel's behavior.
                  In this mode, it is expected that fields are not enclosed in double quotes.
                  It is also not possible to have a line break inside a field.
                * ``None``: the behavior will be inferred in a preliminary partial read.""",
    "date_patterns": """date_patterns: A column name to `date pattern <https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/format/DateTimeFormatter.html>`__ mapping that can be used when the built-in date parsers fail to recognize the formatted dates in the passed files.""",
    "separator": """separator: The character separating the values of each line.

                If ``None``, the separator will be inferred in a preliminary partial read.""",
    **_COLUMNS_KWARGS,
}

PARQUET_KWARGS = {
    "path": """path: The path to the Parquet file.
                If a path pointing to a directory is provided, all of the files with the ``.parquet`` extension in the directory will be loaded into the same table and, as such, they are all expected to share the same schema.
                The path can also be a glob pattern (e.g. ``path/to/directory/**.*.parquet``).""",
    **_COLUMNS_KWARGS,
}

QUANTILE_DOC = """Return a measure equal to the requested quantile {what}.

    Here is how to obtain the same behavior as `these standard quantile calculation methods <https://en.wikipedia.org/wiki/Quantile#Estimating_quantiles_from_a_sample>`__:

    * R-1: ``mode="centered"`` and ``interpolation="lower"``
    * R-2: ``mode="centered"`` and ``interpolation="midpoint"``
    * R-3: ``mode="simple"`` and ``interpolation="nearest"``
    * R-4: ``mode="simple"`` and ``interpolation="linear"``
    * R-5: ``mode="centered"`` and ``interpolation="linear"``
    * R-6 (similar to Excel's ``PERCENTILE.EXC``): ``mode="exc"`` and ``interpolation="linear"``
    * R-7 (similar to Excel's ``PERCENTILE.INC``): ``mode="inc"`` and ``interpolation="linear"``
    * R-8 and R-9 are not supported

    The formulae given for the calculation of the quantile index assume a 1-based indexing system.

    Args:
        {measure_or_operand}: The {measure_or_operand} to get the quantile of.
        q: The quantile to take.
            Must be between ``0`` and ``1``.
            For instance, ``0.95`` is the 95th percentile and ``0.5`` is the median.
        mode: The method used to calculate the index of the quantile.
            Available options are, when searching for the *q* quantile of a vector ``X``:

            * ``simple``: ``len(X) * q``
            * ``centered``: ``len(X) * q + 0.5``
            * ``exc``: ``(len(X) + 1) * q``
            * ``inc``: ``(len(X) - 1) * q + 1``

        interpolation: If the quantile index is not an integer, the interpolation decides what value is returned.
            The different options are, considering a quantile index ``k`` with ``i < k < j`` for a sorted vector ``X``:

            * ``linear``: ``v = X[i] + (X[j] - X[i]) * (k - i)``
            * ``lower``: ``v = X[i]``
            * ``higher``: ``v = X[j]``
            * ``nearest``: ``v = X[i]`` or ``v = X[j]`` depending on which of ``i`` or ``j`` is closest to ``k``
            * ``midpoint``: ``v = (X[i] + X[j]) / 2``
"""

QUANTILE_INDEX_DOC = """Return a measure equal to the index of requested quantile {what}.

    Args:
        measure: The measure to get the quantile of.
        q: The quantile to take.
            Must be between ``0`` and ``1``.
            For instance, ``0.95`` is the 95th percentile and ``0.5`` is the median.
        mode: The method used to calculate the index of the quantile.
            Available options are, when searching for the *q* quantile of a vector ``X``:

            * ``simple``: ``len(X) * q``
            * ``centered``: ``len(X) * q + 0.5``
            * ``exc``: ``(len(X) + 1) * q``
            * ``inc``: ``(len(X) - 1) * q + 1``

        interpolation: If the quantile index is not an integer, the interpolation decides what value is returned.
            The different options are, considering a quantile index ``k`` with ``i < k < j`` for the original vector ``X``
            and the sorted vector ``Y``:

            * ``lowest``: the index in ``X`` of ``Y[i]``
            * ``highest``: the index in ``X`` of ``Y[j]``
            * ``nearest``: the index in ``X`` of ``Y[i]`` or ``Y[j]`` depending on which of ``i`` or ``j`` is closest to ``k``
"""

STD_DOC_KWARGS = {
    "op": "standard deviation",
    "population_excel": "STDEV.P",
    "population_formula": "\\sqrt{\\frac{\\sum_{i=1}^{n}(X_i - m)^{2}}{n}}",
    "sample_excel": "STDEV.S",
    "sample_formula": "\\sqrt{\\frac{\\sum_{i=1}^{n} (X_i - m)^{2}}{n - 1}}",
}
VAR_DOC_KWARGS = {
    "op": "variance",
    "population_excel": "VAR.P",
    "population_formula": "\\frac{\\sum_{i=1}^{n}(X_i - m)^{2}}{n}",
    "sample_excel": "VAR.S",
    "sample_formula": "\\frac{\\sum_{i=1}^{n} (X_i - m)^{2}}{n - 1}",
}

STD_AND_VAR_DOC = """Return a measure equal to the {op} {what}.

    Args:
        {measure_or_operand}: The {measure_or_operand} to get the {op} of.
        mode: One of the supported modes:

            * The ``sample`` {op}, similar to Excel's ``{sample_excel}``, is :math:`{sample_formula}` where ``m`` is the sample mean and ``n`` the size of the sample.
              Use this mode if the data represents a sample of the population.
            * The ``population`` {op}, similar to Excel's ``{population_excel}`` is :math:`{population_formula}` where ``m`` is the mean of the ``Xi`` elements and ``n`` the size of the population.
              Use this mode if the data represents the entire population.
"""

TABLE_APPEND_DOC = """Add one or multiple rows to the {what}.

        If a row with the same keys already exist in the {what}, it will be overridden by the passed one.

        Args:
            rows: The rows to add.
                Rows can either be:

                * Tuples of values in the correct order.
                * Column name to value mappings.

                All rows must share the shame shape.
"""

_KEYS_KWARGS = {
    "keys": """keys: The columns that will become keys of the table.

                Inserting a row containing key values equal to the ones of an existing row will replace the existing row with the new one.

                Key columns cannot have ``None`` as their :attr:`~atoti.Column.default_value`.
                """,
}

TABLE_CREATION_KWARGS = {
    "partitioning": """partitioning : The description of how the data will be split across partitions of the table.

                Default rules:

                * Only non-joined tables are automatically partitioned.
                * Tables are automatically partitioned by hashing their key columns.
                  If there are no key columns, all the dictionarized columns are hashed.
                * Joined tables can only use a sub-partitioning of the table referencing them.
                * Automatic partitioning is done modulo the number of available cores.

                Example:

                    ``hash4(country)`` splits the data across 4 partitions based on the :guilabel:`country` column's hash value.""",
    "table_name": """table_name: The name of the table to create.""",
    "default_values": """default_values: Mapping from column name to column :attr:`~atoti.Column.default_value`.""",
    **_KEYS_KWARGS,
}

TABLE_IADD_DOC = """Add a single row to the {what}."""

EXTERNAL_DATABASE_CONNECTION_INFO_KWARGS = {
    "password": """password: The password to connect to the database.

                Passing it in this separate parameter allows to avoid having it logged alongside the connection string.

                If ``None``, a password is expected to be present in the passed *url*."""
}

EXTERNAL_TABLE_KWARGS = {
    **_COLUMNS_KWARGS,
}

STANDARD_EXTERNAL_TABLE_OPTIONS_KWARGS: Mapping[str, str] = {
    **_KEYS_KWARGS,
    "array_conversion": "array_conversion: Option to convert some values spread over multiple columns or rows into array columns",
    "clustering_columns": """clustering_columns: The names of the columns used for clustering.

                          Feeding aggregate providers from an external database can result in very large queries to be run on this database.
                          Clustering columns split up queries made by DirectQuery to the external database when feeding aggregate providers.""",
}
