from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

import attrs
import pendulum

from tecton_core import specs
from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_core.query.node_interface import INDENT_BLOCK
from tecton_core.query.node_interface import NodeRef
from tecton_core.query.node_interface import QueryNode
from tecton_core.query.node_utils import AsofJoinInputContainer
from tecton_proto.args.pipeline_pb2 import DataSourceNode
from tecton_proto.data.feature_view_pb2 import MaterializationTimeRangePolicy

EFFECTIVE_TIMESTAMP = "_effective_timestamp"
EXPIRATION_TIMESTAMP = "_expiration_timestamp"


@attrs.frozen
class OdfvPipelineNode(QueryNode):
    """
    Evaluates an odfv pipeline on top of an input containing columns prefixed '_udf_internal' to be used as dependent feature view inputs. The _udf_internal contract is
    documented in pipeline_helper.py
    The input may also have other feature values. This ensures we can match multiple odfv features to the right rows based on request context without joining them.
    In order to make this possible, a namespace is also passed through at this point to ensure the odfv features do not conflict with other features.
    """

    input_node: NodeRef
    feature_definition_wrapper: FeatureDefinitionWrapper
    namespace: str

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Evaluate OnDemand Pipeline: {self.feature_definition_wrapper.name}\n"


@attrs.frozen
class FeatureViewPipelineNode(QueryNode):
    inputs_map: Dict[str, NodeRef]
    feature_definition_wrapper: FeatureDefinitionWrapper

    # Needed for correct behavior by tecton_sliding_window udf if it exists in the pipeline
    feature_time_limits: Optional[pendulum.Period]
    entities: Optional[Any] = None

    @property
    def schedule_interval(self) -> pendulum.Duration:
        # Note: elsewhere we set this to pendulum.Duration(seconds=fv_proto.materialization_params.schedule_interval.ToSeconds())
        # but that seemed wrong for bwafv
        return self.feature_definition_wrapper.batch_materialization_schedule

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return tuple(self.inputs_map.values())

    def as_str(self, verbose: bool):
        s = f"Evaluate Pipeline: {self.feature_definition_wrapper.name}"
        if verbose:
            s += f" with feature_time_limits {self.feature_time_limits}"
        s += "\n"
        return s

    def pretty_print(
        self,
        verbose: bool = False,
        indents: int = 0,
        indent_block: str = INDENT_BLOCK,
        show_ids: bool = True,
    ) -> str:
        # Build string representation of this node.
        s = self.pretty_print_self(verbose, indents, indent_block, show_ids)

        # Count the number of leading spaces.
        first_line = s.split("\n")[0]
        num_leading_spaces = len(first_line) - len(first_line.lstrip())

        # Recursively add ancestors.
        for k in self.inputs_map:
            # Add whitespace to match the number of leading spaces, then the name of the input.
            s += " " * num_leading_spaces
            s += f"- PipelineInput: {k}\n"

            # Then add the ancestor.
            s += self.inputs_map[k].pretty_print(verbose, indents + 1, indent_block, show_ids)
        return s


@attrs.frozen
class DataSourceScanNode(QueryNode):
    """
    DataSource + Filter
    We don't have a separate filter node to hide away the filter/partition interaction with raw_batch_translator
    """

    ds: specs.DataSourceSpec
    ds_node: Optional[DataSourceNode]  # value is set when used as an input to FV
    is_stream: bool = attrs.field()
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    # MyPy has a known issue on validators https://mypy.readthedocs.io/en/stable/additional_features.html#id1
    @is_stream.validator  # type: ignore
    def check_no_time_filter(self, _, is_stream: bool):
        if is_stream and (self.start_time is not None or self.end_time is not None):
            raise ValueError("Raw data filtering cannot be run on a stream source")

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return tuple()

    def as_str(self, verbose: bool):
        s = ""
        if self.start_time is not None or self.end_time is not None:
            s += f"TimeFilter: {self.start_time}:{self.end_time}\n"
        verb = "Read Stream" if self.is_stream else "Scan DataSource"
        s += f"{verb}: {self.ds.name}\n"
        return s


@attrs.frozen
class RawDataSourceScanNode(QueryNode):
    """
    DataSource + Filter
    We don't have a separate filter node to hide away the filter/partition interaction with raw_batch_translator
    """

    ds: specs.DataSourceSpec

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return tuple()

    def as_str(self, verbose: bool):
        s = ""
        verb = "Read Stream" if self.is_stream else "Scan DataSource (no post_processor)"
        s += f"{verb}: {self.ds.name}\n"
        return s


@attrs.frozen
class OfflineStoreScanNode(QueryNode):
    """
    Fetch values from offline store
    """

    feature_definition_wrapper: FeatureDefinitionWrapper
    time_filter: Optional[pendulum.Period] = None

    def as_str(self, verbose: bool):
        s = ""
        if self.time_filter is not None:
            s += f"TimeFilter: {self.time_filter}\n"
        s += f"Scan OfflineStore: {self.feature_definition_wrapper.name}"
        return s

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return tuple()


@attrs.frozen
class JoinNode(QueryNode):
    """
    A basic left join on 2 inputs
    """

    left: NodeRef
    right: NodeRef
    join_cols: List[str]
    how: str

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.left, self.right)

    def as_str(self, verbose: bool):
        # TODO: this is gonna look ugly
        return f"{self.how} Join" + (f" on {self.join_cols}:" if verbose else ":")


@attrs.frozen
class EntityFilterNode(QueryNode):
    """
    Filter the feature data by entities
    """

    feature_data: NodeRef
    entities: NodeRef

    # This is somewhat duplicative, but particularly useful for
    # display/debugging purposes.
    entity_cols: List[str]

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.feature_data, self.entities)

    def as_str(self, verbose: bool):
        # TODO: this is gonna look ugly
        return f"EntityFilter" + (f" on {self.entity_cols}:" if verbose else ":")


@attrs.frozen
class AsofJoinNode(QueryNode):
    """
    A "basic" asof join on 2 inputs
    """

    left_container: AsofJoinInputContainer
    right_container: AsofJoinInputContainer
    join_cols: List[str]

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.left_container.node, self.right_container.node)

    def as_str(self, verbose: bool):
        # TODO: this is gonna look ugly
        return "Asof Join:"


@attrs.frozen
class FullAggNode(QueryNode):
    """
    Performs full aggregations for each of the aggregates in fdw.trailing_time_window_aggregation.
    The full aggregations are applied for all the join keys in spine; otherwise new aggregations changed via
    expiring windows will not be generated.

    The resulting dataframe with contain all join keys in the spine.
    """

    input_node: NodeRef
    fdw: FeatureDefinitionWrapper = attrs.field()
    spine: Optional[NodeRef]
    respect_feature_start_time: bool

    @fdw.validator
    def check_is_aggregate(self, _, value):
        if not value.is_temporal_aggregate:
            raise ValueError("Cannot make a FullAggNode of a non-aggregate feature view")

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        if self.spine:
            return (
                self.spine,
                self.input_node,
            )
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if verbose:
            return (
                "FullAggNode: Set any feature values for rows with time < feature_start_time to null\n"
                + "Use window function to perform full aggregations; window range = agg.time_range range preceding -> current row\n"
                + "right-join against spine, with _anchor_time = aligned_spine_timestamp - 1 window, because raw data in a given time will only be accessible for retrieval by the end of the window. We also do some stuff to account for upstream_lateness, but we don't do anything to account for differences in slide_window and batch_schedule. And also this kind of assumes materialization happens instantaneously."
                if self.spine
                else "Perform Full Aggregates"
            )
        else:
            return "Perform Full Aggregates"


@attrs.frozen
class PartialAggNode(QueryNode):
    """
    Performs partial aggregations (i.e. generates tiles that are not rolled up) for each of the aggregates in
    fdw.trailing_time_window_aggregation. The tile start times are always included with column name
    `window_start_column_name`. The tile end times are only included if `window_end_column_name` is specified.
    `aggregation_anchor_time` is used to specify the offset for the partial aggregations.
    """

    input_node: NodeRef
    fdw: FeatureDefinitionWrapper
    window_start_column_name: str
    window_end_column_name: Optional[str]
    aggregation_anchor_time: Optional[datetime]

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if verbose:
            actions = [
                "Perform partial aggregations (i.e. generates tiles that are not rolled up).",
                f'Add column "{self.window_start_column_name}" as the start time of tiles.',
            ]
            if self.window_end_column_name:
                actions.append(f'Add column "{self.window_end_column_name}" as the end time of tiles.')
            if self.aggregation_anchor_time:
                actions.append(
                    f'Align column "{self.fdw.timestamp_key}" to the offset determined by {self.aggregation_anchor_time}.'
                )
            return "\n".join(actions)
        else:
            return "Perform partial aggregations."


@attrs.frozen
class SetAnchorTimeNode(QueryNode):
    """
    Augment a dataframe with an anchor time based on batch schedule (BFV) or slide window (WAFV)
    """

    input_node: NodeRef
    offline: bool
    feature_store_format_version: int
    batch_schedule_in_feature_store_specific_version_units: int
    tile_version_in_feature_store_specific_version_units: int
    timestamp_field: str
    for_retrieval: bool
    is_stream: bool
    data_delay_seconds: Optional[int] = 0

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if not verbose:
            return ""
        if self.for_retrieval:
            return "Add anchor time column _anchor_time: timestamp_col-data_delay-timestamp_col%batch_schedule - batch_schedule, because if you're querying at t, you would only see the data for the previous window and offset by the data delay"
        elif self.offline:
            return "Add anchor time column _anchor_time: timestamp_col-timestamp_col%batch_schedule"
        else:
            return "Add raw data end time column _materialized_raw_data_end_time: timestamp_col-timestamp_col%batch_schedule + batch_schedule. We assume feature_end_time==raw_data_end_time"


@attrs.frozen
class ConvertEpochToTimestampNode(QueryNode):
    """Convert epoch columns to timestamp columns.

    Attributes:
        input_node: The input node to be transformed.
        feature_store_formats: A dictionary mapping column names to feature store format versions. Each column in this
            dictionary will be converted from epoch to timestamp. Its feature store format version determines whether
            the timestamp is in seconds or nanoseconds.
    """

    input_node: NodeRef
    feature_store_formats: Dict[str, int]

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return (
            f"Convert columns {list(self.feature_store_formats.keys())} from epoch (either seconds or ns) to timestamp."
        )


@attrs.frozen
class RenameColsNode(QueryNode):
    """
    Rename columns according to `mapping`. No action is taken for columns mapped to `None`. Drop columns in `drop`.
    """

    input_node: NodeRef
    mapping: Optional[Dict[str, str]] = None
    drop: Optional[List[str]] = None

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        actions = []
        if self.mapping:
            actions.append(f"Rename columns with map {self.mapping}.")
        if self.drop:
            actions.append(f"Drop columns {self.drop}.")
        if not actions:
            actions.append("No columns are renamed or dropped.")
        return " ".join(actions)


@attrs.frozen
class DataNode(QueryNode):
    """Arbitrary data container (useful for testing and mock data).

    The executor node will need to typecheck and know how to handle the type of mock data.
    """

    data: Any

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return tuple()

    def as_str(self, verbose: bool):
        if verbose:
            return f"User-provided Data: type:{self.data.__class__}"
        else:
            return "User-provided Data"


@attrs.frozen
class MockDataSourceScanNode(QueryNode):
    """
    DataSource + Filter
    We don't have a separate filter node to hide away the filter/partition interaction with raw_batch_translator
    """

    data: NodeRef
    ds: specs.DataSourceSpec
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.data,)

    def as_str(self, verbose: bool):
        s = ""
        if self.start_time is not None or self.end_time is not None:
            s += f"TimeFilter: {self.start_time}:{self.end_time}\n"
        s += f"Read Mock DataSource: {self.ds.name}\n"
        return s


@attrs.frozen
class RespectFSTNode(QueryNode):
    """
    Null out all features outside of feature start time
    """

    input_node: NodeRef
    retrieval_time_col: str
    feature_start_time: pendulum.datetime
    features: List[str]

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Null out any values based on a FeatureStartTime of {self.feature_start_time}"


@attrs.frozen
class RespectTTLNode(QueryNode):
    """
    Null out all features with retrieval time > expiration time.
    """

    input_node: NodeRef
    retrieval_time_col: str
    expiration_time_col: str
    features: List[str]

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Null out any values where {self.retrieval_time_col} > {self.expiration_time_col}"


@attrs.frozen
class CustomFilterNode(QueryNode):
    input_node: NodeRef
    filter_str: str

    def as_str(self, verbose: bool):
        return f"Apply filter: ({self.filter_str})"

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)


@attrs.frozen
class TimeFilterNode(QueryNode):
    input_node: NodeRef
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    timestamp_field: str

    def as_str(self, verbose: bool):
        s = ""
        s += f"TimeFilter: {self.start_time}:{self.end_time}\n"
        return s

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)


@attrs.frozen
class FeatureTimeFilterNode(QueryNode):
    """
    Ensure the data being written by a materialization job to offline/online store only contains
    feature timestamps in the feature_data_time_limits range.
    """

    input_node: NodeRef
    feature_data_time_limits: pendulum.Period
    policy: MaterializationTimeRangePolicy
    timestamp_field: str

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if self.policy == MaterializationTimeRangePolicy.MATERIALIZATION_TIME_RANGE_POLICY_FAIL_IF_OUT_OF_RANGE:
            policy_str = "Assert time in range:"
        else:
            policy_str = "Apply:"
        return f"{policy_str} TimeFilter: {self.feature_data_time_limits}"


@attrs.frozen
class MetricsCollectorNode(QueryNode):
    """
    Collect metrics on features
    """

    input_node: NodeRef

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return "Collect metrics on features"


@attrs.frozen
class EffectiveTimestampNode(QueryNode):
    """
    Augment a dataframe with effective timestamp.
    Effective timestamp is calculated using window(timestamp, batch_schedule).end + data_delay
    """

    input_node: NodeRef
    timestamp_field: str
    effective_timestamp_name: str
    batch_schedule_seconds: int
    for_stream: bool
    data_delay_seconds: int
    is_temporal_aggregate: bool

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        if verbose:
            return (
                f"Calculate {self.effective_timestamp_name}: "
                f"Batch Schedule: {self.batch_schedule_seconds} seconds. "
                f"Data Delay: {self.data_delay_seconds} seconds. "
            )
        return "Effective Timestamp"


@attrs.frozen
class AddDurationNode(QueryNode):
    """Adds a duration to a timestamp field"""

    input_node: NodeRef
    timestamp_field: str
    duration: pendulum.Duration
    new_column_name: str

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Add {self.duration.in_words()} to {self.timestamp_field} as {self.new_column_name}"


@attrs.frozen
class StreamWatermarkNode(QueryNode):
    input_node: NodeRef
    time_column: str
    stream_watermark: str

    @property
    def inputs(self) -> Tuple[NodeRef, ...]:
        return (self.input_node,)

    def as_str(self, verbose: bool):
        return f"Set Stream Watermark {self.stream_watermark} on the DataFrame"
