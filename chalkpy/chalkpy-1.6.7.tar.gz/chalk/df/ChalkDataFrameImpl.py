import collections.abc
import datetime
import enum
import functools
import logging
from typing import Any, List, Sequence, Union

import pandas as pd

from chalk.df.ast_parser import parse_dataframe_getitem
from chalk.features import Feature
from chalk.features.feature import FeatureWrapper, Filter, TimeDelta, unwrap_feature
from chalk.utils.collections import ensure_tuple
from chalk.utils.duration import convert_datetime_to_pd

_logger = logging.getLogger(__name__)


def _feature_type_or_value(e: Union[Feature, FeatureWrapper]):
    if isinstance(e, FeatureWrapper):
        e = unwrap_feature(e)
    return e


class ChalkDataFrameImpl:
    def __init__(self, pandas_dataframe: pd.DataFrame):
        self.underlying = pandas_dataframe
        self.timestamp_feature = None
        # All columns in a ChalkDataFrameImpl must be UNPARSED features, since they interact with client code
        # Converting all column labels into Feature instances so column labels match how users
        # would index into the dataframe -- for example df[User.account.number]
        def _to_feature_with_path(col: Any):
            if isinstance(col, FeatureWrapper):
                col = unwrap_feature(col)
            if isinstance(col, Feature):
                return col
            if isinstance(col, str):
                return Feature.from_root_fqn(col)
            raise TypeError(
                f"Column {col} has unexpected type: {type(col).__name__}. Column types must be Feature instances or strings of Root FQNs."
            )

        pandas_dataframe.columns = pandas_dataframe.columns.map(_to_feature_with_path)
        for col in pandas_dataframe.columns:
            assert isinstance(col, Feature)
            if col.is_feature_time:
                self.timestamp_feature = col

    def _expect_scalar(self, v, name: str):
        if isinstance(v, pd.Series) and len(v) == 1:
            return v[0]
        if isinstance(v, pd.Series):
            raise ValueError(
                (
                    f"Cannot compute {name}. DataFrame contains {len(v)} features, and expected only one. "
                    f"Filter your DataFrame down to the feature for which you want to compute the {name} "
                    f"before calling .{name}()."
                )
            )
        return v

    def mean(self):
        return self._expect_scalar(self.underlying.mean(), "mean")

    def median(self):
        return self._expect_scalar(self.underlying.median(), "median")

    def mode(self):
        return self._expect_scalar(self.underlying.median(), "mode")

    def __eq__(self, other: object):
        if isinstance(other, ChalkDataFrameImpl):
            return other.underlying.equals(self.underlying)
        if isinstance(other, pd.DataFrame):
            return self.underlying.equals(other)
        return NotImplemented

    def sum(self):
        return self._expect_scalar(self.underlying.sum(), "sum")

    def max(self):
        return self._expect_scalar(self.underlying.max(), "max")

    def min(self):
        return self._expect_scalar(self.underlying.min(), "min")

    def count(self) -> int:
        return len(self.underlying)

    def __len__(self) -> int:
        return len(self.underlying)

    @property
    def is_empty(self) -> bool:
        return self.underlying.empty

    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty

    def keys(self):
        return self.underlying.keys()

    def iterrows(self):
        return self.underlying.iterrows()

    @property
    def iloc(self):
        return self.underlying.iloc()

    def __repr__(self):
        return repr(self.underlying)

    def _maybe_replace_timestamp_feature(self, f: Union[Feature, Any]):
        """Replace the ``CHALK_TS`` pseudo-feature with the actual timestamp column."""
        if not isinstance(f, Feature) or f.fqn != "__chalk__.CHALK_TS":
            return f
        if self.timestamp_feature is None:
            raise ValueError("DataFrame has no timestamp")
        return self.timestamp_feature

    def _maybe_convert_timedelta_to_timestamp(
        self, f: Union[TimeDelta, datetime.timedelta, Any], now: datetime.datetime
    ):
        """Convert timedeltas relative to ``now`` into absolute datetimes."""
        if isinstance(f, TimeDelta):
            f = f.to_std()
        if isinstance(f, datetime.timedelta):
            return convert_datetime_to_pd(now + f)
        return f

    def _parse_feature_or_value(self, f: Union[Feature, Any], now: datetime.datetime):
        """Parse a feature or value into the correct type that can be used for filtering."""
        f = _feature_type_or_value(f)
        f = self._maybe_convert_timedelta_to_timestamp(f, now)
        f = self._maybe_replace_timestamp_feature(f)
        if isinstance(f, enum.Enum):
            f = f.value
        return f

    def apply_filters(self, filters: Sequence[Filter], now: datetime.datetime) -> "ChalkDataFrameImpl":
        """Apply multiple filters on the dataframe.

        The filters will be joined together with AND.

        Args:
            filters: The filters
            now: The datetime to use for the current timestamp. Used to resolve relative
                timestamps in filters to absolute datetimes.

        Returns:
            A new dataframe with all filters applied.
        """
        underlying = self.underlying

        if len(filters) > 0:
            pandas_filters = [self._evaluate_filter(f, now) for f in filters]
            single_filter = functools.reduce(lambda a, b: a & b, pandas_filters)
            underlying = underlying[single_filter]

        return ChalkDataFrameImpl(underlying)

    def _evaluate_filter(self, f: Filter, now: datetime.datetime) -> pd.Series:
        """Evaluate a filter.

        Args:
            f (Filter): The filter.
            now (datetime.datetime): The datetime to use for the current timestamp. Used to resolve relative
                timestamps in filters to absolute datetimes.

        Returns:
            A series of boolean values that can be used to select the rows where the filter is truthy
        """
        # Passing `now` in explicitly instead of using datetime.datetime.now() so that multiple filters
        # relying on relative timestamps (e.g. before, after) will have the same "now" time.
        if f.operation == "not":
            assert f.rhs is None, "not has just one side"
            assert isinstance(f.lhs, Filter), "lhs must be a filter"
            return ~self._evaluate_filter(f.lhs, now)
        elif f.operation == "and":
            assert isinstance(f.rhs, Filter), "rhs must be a filter"
            assert isinstance(f.lhs, Filter), "lhs must be a filter"
            return self._evaluate_filter(f.lhs, now) & self._evaluate_filter(f.rhs, now)
        elif f.operation == "or":
            assert isinstance(f.rhs, Filter), "rhs must be a filter"
            assert isinstance(f.lhs, Filter), "lhs must be a filter"
            return self._evaluate_filter(f.lhs, now) | self._evaluate_filter(f.rhs, now)

        lhs = self._parse_feature_or_value(f.lhs, now)
        rhs = self._parse_feature_or_value(f.rhs, now)

        if isinstance(lhs, Feature):
            lhs = self.underlying[lhs]

        if isinstance(rhs, Feature):
            rhs = self.underlying[rhs]

        if rhs is None:
            assert isinstance(lhs, pd.Series)
            if f.operation == "==":
                return lhs.isnull()

            elif f.operation == "!=":
                return lhs.notnull()

        if isinstance(lhs, pd.Series) and lhs.dtype.name != "object" and isinstance(rhs, enum.Enum):
            rhs = rhs.value

        if isinstance(rhs, pd.Series) and rhs.dtype.name != "object" and isinstance(lhs, enum.Enum):
            lhs = lhs.value

        if f.operation == "==":
            ret = lhs == rhs
        elif f.operation == "!=":
            ret = lhs != rhs
        elif f.operation == ">=":
            ret = lhs >= rhs
        elif f.operation == ">":
            ret = lhs > rhs
        elif f.operation == "<":
            ret = lhs < rhs
        elif f.operation == "<=":
            ret = lhs <= rhs
        elif f.operation in ("in", "not in"):
            assert isinstance(lhs, pd.Series)
            assert isinstance(rhs, collections.abc.Iterable)
            new_rhs = []
            for x in rhs:
                if lhs.dtype.name != "object" and isinstance(x, enum.Enum):
                    new_rhs.append(x.value)
                else:
                    new_rhs.append(x)
            ret = lhs.isin(new_rhs)
            if f.operation == "not in":
                ret = ~ret
        else:
            raise ValueError(f'Unknown operation "{f.operation}"')
        assert isinstance(ret, pd.Series)
        return ret

    def __getitem__(self, item):
        has_bool_or_filter_value = any(isinstance(x, (bool, Filter)) for x in ensure_tuple(item))
        if has_bool_or_filter_value:
            # If we have a boolean or Filter value, then that means we need to ast-parse the caller since
            # python has already evaluated AND, OR, and IN operations into literal booleans or Filters
            # Skipping the parsing unless if we have need to for effeciency and to eliminate conflicts
            # with pytest
            item = parse_dataframe_getitem()
        try:
            projections: list[Feature] = []
            filters: List[Filter] = []
            slices = []
            for x in ensure_tuple(item):
                if isinstance(x, FeatureWrapper):
                    x = unwrap_feature(x)
                if isinstance(x, Feature):
                    projections.append(x)

                elif isinstance(x, Filter):
                    filters.append(x)

                elif isinstance(x, slice):
                    slices.append(x)

                elif isinstance(x, int):
                    raise ValueError("Indexing into the chalk.DataFrame is not yet supported")

                else:
                    raise ValueError(f'Indexed chalk.DataFrame with invalid type "{type(x).__name__}": {x}')

            now = datetime.datetime.now(tz=datetime.timezone.utc)
            self_filtered = self.apply_filters(filters, now)
            underlying = self_filtered.underlying
            if len(slices) > 0:
                underlying = underlying.iloc[tuple(slices)]

            # Do the projection
            underlying = underlying[projections] if len(projections) > 0 else underlying
            assert isinstance(underlying, pd.DataFrame)

            return ChalkDataFrameImpl(underlying)

        except KeyError:
            _logger.debug(f"Failed to get key: Had keys: {self.underlying.keys()}", exc_info=True)
            raise

    def to_pandas(self) -> Union[pd.DataFrame, pd.Series]:
        return self.underlying
