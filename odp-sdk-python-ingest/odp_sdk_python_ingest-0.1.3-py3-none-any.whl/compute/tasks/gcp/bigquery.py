from timeit import timeit

from google.cloud import bigquery
from google.cloud.bigquery import DEFAULT_RETRY, ExtractJob
from google.api_core.retry import Retry
from datetime import datetime
import logging
import time

from prefect import Task, task
from prefect.utilities.gcp import get_bigquery_client
from prefect.utilities.tasks import defaults_from_attrs

from typing import *

LOG = logging.getLogger(__name__)

__all__ = ["BigQueryDeleteTableTask", "BigQueryTask", "BigQueryExtractTableTask"]


class BigQueryDeleteTableTask(Task):
    def __init__(
        self,
        table: Optional[str] = None,
        project: Optional[str] = None,
        retry: Retry = DEFAULT_RETRY,
        job_timeout: Optional[float] = None,
        raise_if_not_found: bool = True,
        **kwargs,
    ):
        self.table = table
        self.project = project
        self.retry = retry
        self.job_timeout = job_timeout
        self.raise_if_not_found = raise_if_not_found
        super().__init__(**kwargs)

    @defaults_from_attrs(
        "table",
        "project",
        "job_timeout",
        "raise_if_not_found",
    )
    def run(
        self,
        table: Optional[str] = None,
        project: Optional[str] = None,
        retry: Optional[Retry] = None,
        job_timeout: Optional[float] = None,
        raise_if_not_found: Optional[bool] = None,
        credentials: Optional[Dict] = None,
    ):
        client: bigquery.Client = get_bigquery_client(
            project=project, credentials=credentials
        )

        table_ref = bigquery.TableReference.from_string(f"{project}.{table}")

        created_time = datetime.now()
        client.delete_table(
            table=table_ref,
            retry=retry,
            timeout=job_timeout,
            not_found_ok=not raise_if_not_found,
        )

        return {
            "delete": "delete",
            "created": created_time,
            "started": created_time,
            "ended": datetime.now(),
            "job_id": None,
        }


class BigQueryExtractTableTask(Task):
    def __init__(
        self,
        source: Optional[str] = None,
        destination_uris: Optional[Union[str, List[str]]] = None,
        job_id: Optional[str] = None,
        job_id_prefix: Optional[str] = None,
        location: Optional[str] = "US",
        project: Optional[str] = None,
        job_config: Optional[Dict] = None,
        retry: Optional[Retry] = DEFAULT_RETRY,
        job_timeout: Optional[float] = None,
        wait_for_completion: Optional[bool] = True,
        source_type: Optional[str] = "Table",
        **kwargs,
    ):
        self.source = source
        self.destination_uris = destination_uris
        self.job_id = job_id
        self.job_id_prefix = job_id_prefix
        self.location = location
        self.project = project
        self.job_config = job_config
        self.retry = retry
        self.job_timeout = job_timeout
        self.wait_for_completion = wait_for_completion
        self.source_type = source_type
        super().__init__(**kwargs)

    @defaults_from_attrs(
        "source",
        "destination_uris",
        "job_id",
        "job_id_prefix",
        "location",
        "project",
        "job_config",
        "retry",
        "job_timeout",
        "wait_for_completion",
        "source_type",
    )
    def run(
        self,
        source: Optional[str] = None,
        destination_uris: Optional[Union[str, List[str]]] = None,
        job_id: Optional[str] = None,
        job_id_prefix: Optional[str] = None,
        location: Optional[str] = None,
        project: Optional[str] = None,
        job_config: Optional[Dict] = None,
        retry: Optional[Retry] = None,
        job_timeout: Optional[float] = None,
        wait_for_completion: Optional[bool] = None,
        source_type: Optional[str] = None,
        credentials: Optional[Dict] = None,
    ):
        client = get_bigquery_client(project=project, credentials=credentials)

        job_config = bigquery.ExtractJobConfig(**job_config)

        extract_job: ExtractJob = client.extract_table(
            source=source,
            destination_uris=destination_uris,
            job_id=job_id,
            job_id_prefix=job_id_prefix,
            location=location,
            project=project,
            job_config=job_config,
            retry=retry,
            timeout=job_timeout,
            source_type=source_type,
        )

        if wait_for_completion:
            t = time.time()
            while not extract_job.done():
                dt = time.time() - t
                if job_timeout and dt > job_timeout:
                    raise TimeoutError(
                        f"BigQuery export job expired after {dt:.3f} s (timeout={job_timeout:%.3f} s)"
                    )
                if int(dt) > 0 and int(dt) % 10 == 0:
                    LOG.info(
                        "Waiting for BigQuery export job to complete. dt=%.3f s", dt
                    )
                time.sleep(1 - (dt - int(dt)))

        extract_job.done()

        return {
            "job_type": "extract",
            "created": extract_job.created,
            "started": extract_job.started,
            "ended": extract_job.ended,
            "job_id": extract_job.job_id,
        }


class BigQueryTask(Task):
    """
    Task for executing queries against a Google BigQuery table and (optionally) returning
    the results.  Note that _all_ initialization settings can be provided / overwritten at runtime.

    Args:
        - query (str, optional): a string of the query to execute
        - query_params (list[tuple], optional): a list of 3-tuples specifying BigQuery query
            parameters; currently only scalar query parameters are supported.  See [the Google
            documentation](https://cloud.google.com/bigquery/docs/parameterized-queries#bigquery-query-params-python)
            for more details on how both the query and the query parameters should be formatted
        - project (str, optional): the project to initialize the BigQuery Client with; if not
            provided, will default to the one inferred from your credentials
        - location (str, optional): location of the dataset that will be queried; defaults to "US"
        - dry_run_max_bytes (int, optional): if provided, the maximum number of bytes the query
            is allowed to process; this will be determined by executing a dry run and raising a
            `ValueError` if the maximum is exceeded
        - dataset_dest (str, optional): the optional name of a destination dataset to write the
            query results to, if you don't want them returned; if provided, `table_dest` must
            also be provided
        - table_dest (str, optional): the optional name of a destination table to write the
            query results to, if you don't want them returned; if provided, `dataset_dest` must also be
            provided
        - to_dataframe (bool, optional): if provided, returns the results of the query as a pandas
            dataframe instead of a list of `bigquery.table.Row` objects. Defaults to False
        - job_config (dict, optional): an optional dictionary of job configuration parameters; note that
            the parameters provided here must be pickleable (e.g., dataset references will be rejected)
        - **kwargs (optional): additional kwargs to pass to the `Task` constructor
    """

    def __init__(
        self,
        query: str = None,
        query_params: List[tuple] = None,  # 3-tuples
        project: str = None,
        location: str = "US",
        dry_run_max_bytes: int = None,
        project_dest: str = None,
        dataset_dest: str = None,
        table_dest: str = None,
        to_dataframe: bool = False,
        suppress_result: bool = False,
        job_config: dict = None,
        **kwargs,
    ):
        self.query = query
        self.query_params = query_params
        self.project = project
        self.location = location
        self.dry_run_max_bytes = dry_run_max_bytes
        self.project_dest = project_dest
        self.dataset_dest = dataset_dest
        self.table_dest = table_dest
        self.to_dataframe = to_dataframe
        self.suppress_result = suppress_result
        self.job_config = job_config or {}
        super().__init__(**kwargs)

    @defaults_from_attrs(
        "query",
        "query_params",
        "project",
        "location",
        "dry_run_max_bytes",
        "project_dest",
        "dataset_dest",
        "table_dest",
        "to_dataframe",
        "suppress_result",
        "job_config",
    )
    def run(
        self,
        query: str = None,
        query_params: List[tuple] = None,
        project: str = None,
        location: str = "US",
        dry_run_max_bytes: int = None,
        credentials: dict = None,
        dataset_dest: str = None,
        table_dest: str = None,
        project_dest: str = None,
        credentials_dest: dict = None,
        to_dataframe: bool = False,
        suppress_result: bool = False,
        job_config: dict = None,
    ):
        """
        Run method for this Task.  Invoked by _calling_ this Task within a Flow context, after
        initialization.

        Args:
            - query (str, optional): a string of the query to execute
            - query_params (list[tuple], optional): a list of 3-tuples specifying BigQuery
                query parameters; currently only scalar query parameters are supported. See
                [the Google
                documentation](https://cloud.google.com/bigquery/docs/parameterized-queries#bigquery-query-params-python)
                for more details on how both the query and the query parameters should be
                formatted
            - project (str, optional): the project to initialize the BigQuery Client with; if
                not provided, will default to the one inferred from your credentials
            - location (str, optional): location of the dataset that will be queried; defaults
                to "US"
            - dry_run_max_bytes (int, optional): if provided, the maximum number of bytes the
                query is allowed to process; this will be determined by executing a dry run and
                raising a `ValueError` if the maximum is exceeded
            - credentials (dict, optional): a JSON document containing Google Cloud credentials.
                You should provide these at runtime with an upstream Secret task.  If not
                provided, Prefect will first check `context` for `GCP_CREDENTIALS` and lastly
                will use default Google client logic.
            - dataset_dest (str, optional): the optional name of a destination dataset to write the
                query results to, if you don't want them returned; if provided, `table_dest`
                must also be provided
            - table_dest (str, optional): the optional name of a destination table to write the
                query results to, if you don't want them returned; if provided, `dataset_dest` must also
                be provided
            - to_dataframe (bool, optional): if provided, returns the results of the query as a pandas
                dataframe instead of a list of `bigquery.table.Row` objects. Defaults to False
            - job_config (dict, optional): an optional dictionary of job configuration parameters; note
                that the parameters provided here must be pickleable (e.g., dataset references will be
                rejected)

        Raises:
            - ValueError: if the `query` is `None`
            - ValueError: if only one of `dataset_dest` / `table_dest` is provided
            - ValueError: if the query will execeed `dry_run_max_bytes`

        Returns:
            - list: a fully populated list of Query results, with one item per row
        """
        # check for any argument inconsistencies
        if query is None:
            raise ValueError("No query provided.")
        if sum([dataset_dest is None, table_dest is None]) == 1:
            raise ValueError(
                "Both `dataset_dest` and `table_dest` must be provided if writing to a "
                "destination table."
            )

        # create client
        client = get_bigquery_client(project=project, credentials=credentials)

        # setup jobconfig
        job_config = bigquery.QueryJobConfig(**job_config)
        if query_params is not None:
            hydrated_params = [
                bigquery.ScalarQueryParameter(*qp) for qp in query_params
            ]
            job_config.query_parameters = hydrated_params

        # perform dry_run if requested
        if dry_run_max_bytes is not None:
            old_info = dict(
                dry_run=job_config.dry_run, use_query_cache=job_config.use_query_cache
            )
            job_config.dry_run = True
            job_config.use_query_cache = False
            self.logger.debug("Performing a dry run...")
            query_job = client.query(query, location=location, job_config=job_config)
            if query_job.total_bytes_processed > dry_run_max_bytes:
                msg = (
                    "Query will process {0} bytes which is above the set maximum of {1} "
                    "for this task."
                ).format(query_job.total_bytes_processed, dry_run_max_bytes)
                raise ValueError(msg)
            job_config.dry_run = old_info["dry_run"]
            job_config.use_query_cache = old_info["use_query_cache"]

        # if writing to a destination table
        if dataset_dest is not None:

            client_dest = get_bigquery_client(
                project=project_dest or project,
                credentials=credentials_dest or credentials,
            )
            table_ref = client_dest.dataset(dataset_dest).table(table_dest)
            job_config.destination = table_ref

        query_job = client.query(query, location=location, job_config=job_config)
        result = query_job.result()

        # if not returning any query result
        if suppress_result:
            return {
                "total_bytes_processed": query_job.total_bytes_processed,
                "total_bytes_billed": query_job.total_bytes_billed,
                "created": query_job.created,
                "started": query_job.started,
                "ended": query_job.ended,
                "job_id": query_job.job_id,
                "job_type": "query",
            }
        # if returning the results as a dataframe
        elif to_dataframe:
            return result.to_dataframe()
        # else if returning as a list of bigquery.table.Row objects (default)
        else:
            return list(result)


@task(nout=True)
def bq_param(name, dtype, value):
    return name, dtype, value


@task()
def bq_table(project, dataset, table):
    dataset = bigquery.Dataset(f"{project}.{dataset}")
    return dataset.table(table)
