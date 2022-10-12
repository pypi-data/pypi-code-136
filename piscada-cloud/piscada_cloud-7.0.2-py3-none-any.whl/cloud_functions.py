"""Template classes for cloud functions.

This module has a collection of Cloud function template classes that can be practical to inherit from.
An example usage is shown at the bottom of the file, and is used when running the file.

This module contains these classes:
    * CloudFunctionBase
"""
import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple, Union
from uuid import UUID

from pandas import DataFrame, Timestamp

from piscada_cloud.data import get_historic_values, write_value
from piscada_cloud.mappings import Mapping, MappingTable, Parameter, Tag


def _get_provided_tags_set(tag_dict: Dict[Union[UUID, str], Union[Tag, List[Tag]]]):
    provided_tags = []
    for key, tag in tag_dict.items():
        if isinstance(tag, Tag):
            provided_tags.append(tag)
        elif isinstance(tag, list):
            provided_tags.extend(tag)
        else:
            raise RuntimeError(
                (
                    "Misconfigured Tag. All values in `self.input_tags` and `self.output_tags` should be of type Tag or List[Tag]. "
                    f"Got {tag} of type {type(tag)} for key {key}."
                )
            )
    return set(provided_tags)


def _get_provided_parameters_set(parameters_dict: Dict[Union[UUID, str], Parameter]):
    provided_parameters = set()
    for key, parameter in parameters_dict.items():
        if isinstance(parameter, Parameter):
            provided_parameters.add(parameter.value)
        elif isinstance(parameter, list):
            for parameter_list_item in parameter:
                provided_parameters.add(parameter_list_item if isinstance(parameter_list_item, str) else parameter_list_item.value)
        elif isinstance(parameter, str):
            provided_parameters.add(parameter)
        else:
            raise RuntimeError(
                (
                    "Misconfigured Parameters. All values in `self.parameters` should be of type Parameter or List[Parameter]. "
                    f"Got {parameter} for {key} of type {type(parameter)}."
                )
            )
    return provided_parameters


def get_meaning_values(
    mapping: Mapping, mapping_table: MappingTable, meaning_title_as_key: bool = False
) -> Tuple[Dict[Union[UUID, str], Union[Tag, List[Tag]]], Dict[Union[UUID, str], Union[Tag, List[Tag]]], Dict[Union[UUID, str], Union[Parameter, List[Parameter]]]]:
    """Get dicts of input tags, output tags and parameters, with meaning uuid or title as keys.

    Parameters
    ----------
    mapping: Mapping
        A Mapping from which we get the meanings.
    mapping_table: MappingTable
        A MappingTable from which we get the values.
    fail_on_missing: bool
        A flag indicating if an error should be raised if the mapping table does not hold a value for the meaning.
    meaning_title_as_key: bool
        Flag determining if the keys should be the meanings title (True) or uuid (False).

    Returns
    -------
    input_tags: Dict[Union[UUID, str], Union[Tag, List[Tag]]]
        Dictionary of input tags, with meaning uuid as key.
    output_tags: Dict[Union[UUID, str], Union[Tag, List[Tag]]]
        Dictionary of output tags, with meaning uuid as key.
    parameters: Dict[Union[UUID, str], Union[Tag, List[Tag]]]
        Dictionary of parameters, with meaning uuid as key.

    Raises
    ------
    NotImplementedError
        If the meaning type is not supported.
    """
    key = lambda meaning: meaning.title if meaning_title_as_key else meaning.uuid
    input_tags: dict = {}
    output_tags: dict = {}
    parameters: dict = {}
    for meaning in mapping.meanings:
        if meaning.type.startswith("input"):
            input_tags[key(meaning)] = mapping_table.get_tag(meaning.uuid, multiple=meaning.type.endswith("list"))
        elif meaning.type.startswith("output"):
            output_tags[key(meaning)] = mapping_table.get_tag(meaning.uuid, multiple=meaning.type.endswith("list"))
        elif meaning.type.startswith("parameter"):
            parameters[key(meaning)] = mapping_table.get_parameter(meaning.uuid, multiple=meaning.type.endswith("list"))
        else:
            raise NotImplementedError(f"Unable to handle meanings of type {meaning.type}")
    return input_tags, output_tags, parameters


class CloudFunctionBase(ABC):
    """
    Base class holding most common steps for most cloud functions.

    This class works as a skeleton for other classes to inherit from and expand.
    Some of the methods are required, and will raise an `NotImplemetedError` if not overridden in the subclass.

    While most methods are optional, some will need to be overridden in order to make any sense, e.g. `compute_status()`.
    Methods required to be overridden:
        - `compute_status()`
    """

    # pylint: disable=too-many-instance-attributes, too-many-arguments

    def __init__(
        self, mapping: Mapping, mapping_table: MappingTable, now: Optional[datetime] = None, fail_on_missing_value: bool = True, meaning_title_as_key: bool = False
    ):
        """
        Set up and check input arguments.

        Save input arguments as properties in addition to setting up placeholders for expected values.

        Parameters
        ----------
        mapping_table: MappingTable
        input_tags: Dict[UUID, Union[Tag, List[Tag]]]
        output_tags: Dict[UUID, Union[Tag, List[Tag]]]
        parmaters: Dict[UUID, Union[Parameter, List[Parameter]]]
        now : datetime
            Timestamp of evaluation
        fail_on_missing_meaning: bool
            Determine if the function will fail if there are any missing tags or parameters
        """
        self.now: datetime = now if isinstance(now, datetime) else datetime.now(tz=timezone.utc)
        self.mapping_table = mapping_table
        self.input_tags, self.output_tags, self.parameters = get_meaning_values(mapping, mapping_table, meaning_title_as_key)
        self.last_state: int = 0
        self.last_run: datetime
        self.last_error_start: datetime
        self.df: DataFrame
        if fail_on_missing_value:
            self.validate_values()

    def validate_values(self):
        """
        Check if any values in self.input_tags, self.output_tags or self.parameters are None.

        First check if any tag/parameter  is `None` or empty list.
        Then check if the tag/parameter is in the mapping_tables.

        Raises
        ------
        RuntimeError
            If any tag mapping in `self.input_tags`, `self.output_tags` or `self.parameters` contains `None` or empty lists, or if they aren't in the mapping table.
        """
        provided_tags = _get_provided_tags_set({**self.input_tags, **self.output_tags})
        mapping_table_tags = {tag_mapping.tag for tag_mapping in self.mapping_table.tag_mappings}
        if len(missing_tags := mapping_table_tags - provided_tags) > 0:
            raise RuntimeError("Missing Tags: " + ", ".join(str(tag) for tag in missing_tags))
        if len(tags_not_in_mapping := provided_tags - mapping_table_tags) > 0:
            raise RuntimeError("Tags are not in tag_mapping: " + ", ".join(str(tag) for tag in tags_not_in_mapping))

        provided_parameters = _get_provided_parameters_set(self.parameters)
        mapping_table_parameters = set(parameter.value for parameter in self.mapping_table.parameters)
        missing_parameters = mapping_table_parameters - provided_parameters
        parameters_not_in_mapping = provided_parameters - mapping_table_parameters
        if len(missing_parameters) > 0:
            raise RuntimeError("Missing Parameters: " + ", ".join(str(parameter) for parameter in missing_parameters))
        if len(parameters_not_in_mapping) > 0:
            raise RuntimeError("Parameters are not in mapping_table: " + ", ".join(str(parameter) for parameter in parameters_not_in_mapping))

    def update_last_run(self, error_tag: Union[str, UUID] = "ERROR", initial_window: timedelta = timedelta(minutes=30)) -> Union[Dict[str, str], str]:
        """
        Fetch the last error entry from the `error_tag` and update `self.last_run` and `self.last_state` accordingly.

        If there are no previous entries, set `self.last_run` to be `initial_window` before `self.now`.

        Parameters
        ----------
        error_tag : str
            Key in `self.output_tags` holding the tag to fetch error states from. Defaults to "ERROR".
        initial_window : timedelta
            Time span to look back in time for the initial run. Defaults to 30 minutes.

        Returns
        -------
        Union[Dict[str, str], str]
            Status report for logging. One line for every attribute set.
        """
        log = {}
        if isinstance(output_tag := self.output_tags[error_tag], Tag):
            status_tag = output_tag
        else:
            raise ValueError(f"The error tag should be a single Tag. Got {status_tag}")
        df_status = get_historic_values(self.now, self.now, [status_tag])
        if df_status is not None and not df_status.empty:
            self.last_run = df_status.index.max().to_pydatetime()
            self.last_state = int(df_status.iloc[-1][str(status_tag)])
            log["last_run"] = str(self.last_run)
            log["last_state"] = str(self.last_state)
            if self.last_state:
                self.last_error_start = self.last_run
            else:
                df_err = get_historic_values(self.last_run - timedelta(milliseconds=1), self.last_run - timedelta(milliseconds=1), [status_tag])
                if df_err is not None and not df_err.empty:
                    self.last_error_start = df_err.index.max().to_pydatetime()
            log["last_error_start"] = str(self.last_error_start) if hasattr(self, "last_error_start") else "Not set."
            return log

        # If we have never run before, look back `initial_window` from now.
        self.last_run = self.now - initial_window
        self.last_error_start = self.last_run
        return f"No last run found. Set last run and last error start to {self.last_run}."

    def update_data(self, additional_timedelta: timedelta = timedelta(0), max_time_range: timedelta = timedelta(hours=2)) -> str:
        """
        Fetch data for the tags in `self.input_tags` and store the resulting dataframe in `self.df`.

        By default data will be fetched from the time of the last run until now.
        The parameter `additional_timedelta` can be set to change the starting point of this query.

        Parameters
        ----------
        additional_timedelta : timedelta
            Move the stating point for the query.

        Returns
        -------
        str
            Status report for logging.
        """
        time_range_adjustment_warning = ""
        start = self.last_run - additional_timedelta
        if self.now - start > max_time_range:
            start = self.now - max_time_range
            time_range_adjustment_warning = f"Last run is too long ago. Adjusting `start` to fit `max_time_range` ({max_time_range})."
        self.df = get_historic_values(start, self.now, list(_get_provided_tags_set(self.input_tags)))
        if self.df is not None and not self.df.empty:
            return time_range_adjustment_warning + f"Retrieved {len(self.df)} rows of data in the period {self.df.index.min()} to {self.df.index.max()}."
        return time_range_adjustment_warning + f"ERROR: Could not retrieved data for the period {start} to {self.now}."

    @abstractmethod
    def calculate_status(self) -> str:
        """
        Calculate status from values in `self.df` and add it as a column.

        Returns
        -------
        str
            Status report for logging.
        """

    def send_status_changes(self, error_tag: str = "ERROR", status_column: str = "status") -> Union[Dict[str, str], str]:
        """
        Send status changes since last run.

        If there are no changes since the last run, send the same value as from the last run.

        Parameters
        ----------
        error_tag : str
            Key in `self.output_tags` holding the tag to fetch error states from. Defaults to "Error".
        status_column : str
            Name of column holding the status in `self.df`. Defaults to "status".

        Raises
        ------
        RuntimeError
            If post requests are denied by the server.

        Returns
        -------
        Union[Dict[str, str], str]
            Status report for logging. One line for every state change written to database.
        """
        log = {}
        if not isinstance(output_tag := self.output_tags[error_tag], Tag):
            raise ValueError(f"'error_tag' must refer to a single tag. Output tag {error_tag} has type {type(output_tag)}")
        new = self.df.loc[self.df.index > self.last_run, status_column]
        status_changes = new != new.shift(1)
        if not status_changes.empty:
            status_changes[0] = new[0] != self.last_state
            updates = new[status_changes]
            if not updates.empty:
                for timestamp, state in updates.iteritems():
                    response = write_value(output_tag, state, int(timestamp.timestamp() * 1000))
                    if response.status_code < 200 or response.status_code >= 300:
                        raise RuntimeError(f"Could not send state change {timestamp}: {str(output_tag)} - {state}. Reason: {response.reason}")
                    if state:
                        self.last_error_start = timestamp.to_pydatetime()
                    log[str(timestamp)] = f"Sent status change: {state} to tag {str(output_tag)}"
                return log
        response = write_value(output_tag, self.last_state, int(self.last_run.timestamp() * 1000))
        if response.status_code < 200 or response.status_code >= 300:
            raise RuntimeError(f"No status changes. Could not send last state {self.last_run}: {str(output_tag)} - {self.last_state}. Reason: {response.reason}")
        return f"No status changes. Sent last calculated state: {self.last_run}: {str(output_tag)} - {self.last_state}"

    def send_visualization_data(
        self, tag: Tag, df: Optional[DataFrame] = None, value: Union[str, List[Union[str, Tag]], Tag, None] = None, visualization_type: Optional[str] = None
    ) -> str:
        """Send JSON formatted string used for visualization.

        If a dataframe is provided, it will be serialized.

        Parameters
        ----------
        tag: Tag
            Tag to which we send the post request.
        df: DataFrame
            DataFrame containing the results.
        value: Union[str, Tag, List[str, Tag], None]
            Value that cannot be expressed by a dataframe.
        visualization_type: Optional[str]
            Spesific visualization that should be used. Must be one of ["auto", "bars", "histogram", "line", "pie", "scatter", "table", "text"].
        """
        if (df is None and value is None) or (df is not None and value is not None):
            raise ValueError("Exactly one of 'df' and 'value' must be provided")
        if not isinstance(tag, Tag):
            raise TypeError("'tag' must be of type Tag")
        valid_visualization_types = ["auto", "bars", "histogram", "line", "pie", "scatter", "table", "text"]
        if visualization_type is not None and visualization_type not in valid_visualization_types:
            raise ValueError(f"Visualization_type must be one of {valid_visualization_types}")
        if visualization_type == "text" and value is None:
            raise ValueError("value must be provided when visualization_type is 'text'")

        if df is not None and self.last_error_start > self.last_run:
            if len(df) > 100:
                logging.warning("Sending large DataFrame for mapping table %s", self.mapping_table)
            df_json = df.to_json(orient="split", date_format="iso")
            if visualization_type is not None:
                df_dict = json.loads(df_json)
                df_dict["visualization_type"] = visualization_type
                df_json = json.dumps(df_dict)
            response = write_value(tag, value=df_json, timestamp=int(self.last_error_start.timestamp() * 1000))
        elif isinstance(value, str):
            response = write_value(tag, value, timestamp=int(self.last_error_start.timestamp() * 1000))
        else:
            value = json.dumps(value, cls=VisualizationDataEncoder)
            response = write_value(tag, value, timestamp=int(self.last_error_start.timestamp() * 1000))
        if response.status_code < 200 or response.status_code >= 300:
            raise RuntimeError(f"Could not send visualization data. Reason: {response.reason}. {response.text}")
        return "Sent visualization data"


class VisualizationDataEncoder(json.JSONEncoder):
    """JSON encoder able to handle Tag, Timestamp and UUID."""

    def default(self, o: Any) -> Any:
        """Serialize object 'o'."""
        if isinstance(o, Tag):
            return f'{{"controller-uuid": "{o.controller_id}", "name": "{o.name}", "path": "{o.path}", "uuid": "{o.uuid}"}}'
        if isinstance(o, Timestamp):
            return o.isoformat()
        if isinstance(o, UUID):
            return str(o)
        return super().default(o)
