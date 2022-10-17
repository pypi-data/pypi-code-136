from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Optional

from sw_service_lib.platform import API, Operation


@dataclass
class Job:
    id: str
    child_jobs: Optional[List]
    service_identifier: Optional[str]
    slug: Optional[str]
    resource: Optional[str]
    status: Optional[str]
    is_terminal_state: Optional[str]
    remote_status: Optional[str] = None
    job_data_schema: Optional[str] = None
    job_data: Optional[Dict[str, Any]] = None

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(res: dict):
        child_jobs: List[Job] = []
        if "childJobs" in res:
            for _, child_job in res["childJobs"]:
                child_jobs.append(Job.from_dict(child_job))

        return Job(
            id=res["id"],
            service_identifier=res["serviceIdentifier"],
            slug=res["slug"],
            resource=res["resource"] if "resource" in res else None,
            status=res["status"],
            is_terminal_state=res["isTerminalState"],
            remote_status=res["remoteStatus"],
            job_data_schema=res["jobDataSchema"],
            job_data=res["jobData"],
            child_jobs=child_jobs,
        )


@dataclass
class File:
    id: str
    slug: Optional[str] = None
    label: Optional[str] = None
    file_name: Optional[str] = None
    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict):
        return File(
            id=d["id"],
            slug=d["slug"],
            label=d["label"],
            url=d["url"],
            file_name=d["fileName"],
        )


create_request = Operation(
    query="""
        mutation jobCreate(
            $resource_slug: String!,
            $workspace_member_slug: String!,
            $parent_job_slug: String,
            $service_identifier: String,
            $status: JobStatus,
            $remote_status: String,
            $job_data_schema: String,
            $job_data: JSON) {
            jobCreate(input: {
                resourceSlug: $resource_slug,
                workspaceMemberSlug: $workspace_member_slug,
                parentJobSlug: $parent_job_slug,
                serviceIdentifier: $service_identifier,
                status: $status,
                remoteStatus: $remote_status,
                jobDataSchema: $job_data_schema,
                jobData: $job_data,
            }) {
                job {
                id
                serviceIdentifier
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
                }
            }
        }
        """,
)


def create(
    api: API,
    resource_slug: str,
    workspace_member_slug: str,
    parent_job_slug: Optional[str] = None,
    service_identifier: Optional[str] = None,
    status: Optional[str] = None,
    remote_status: Optional[str] = None,
    job_data_schema: Optional[str] = None,
    job_data: Optional[str] = None,
) -> Job:
    """Create a job entry

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        used as identifier for the resource.
    workspaceMemberSlug: str
        used to map workspace and user.
    parentJobSlug: Optional[str]
        slug of the job which created this job.
    service_identifier: Optional[str]
        id typically generated as a result of making a request to an external system.
    status: {Optionapstr
        status of the job. Refer to the  platform for possible values.
    remoteStatus: Optional[str]
        status of job that was initiated on an  external (non-Strangeworks) system.
    jobDataSchema: Optional[str]
        link to the json schema describing job output.
    jobData: Optional[str]
        job output.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=create_request,
        **locals(),
    )

    return Job.from_dict(platform_result["jobCreate"]["job"])


update_request = Operation(
    query="""
        mutation jobUpdate(
            $resource_slug: String!,
            $job_slug: String!,
            $parent_job_slug: String,
            $service_identifier: String,
            $status: JobStatus,
            $remote_status: String,
            $job_data_schema: String,
            $job_data: JSON) {
            jobUpdate(input: {
                resourceSlug: $resource_slug,
                jobSlug: $job_slug,
                parentJobSlug: $parent_job_slug,
                serviceIdentifier: $service_identifier,
                status: $status,
                remoteStatus: $remote_status,
                jobDataSchema: $job_data_schema,
                jobData: $job_data,
            }) {
                job {
                id
                serviceIdentifier
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
                }
            }
        }
        """,
)


def update(
    api: API,
    resource_slug: str,
    job_slug: str,
    parent_job_slug: Optional[str] = None,
    service_identifier: Optional[str] = None,
    status: Optional[str] = None,
    remote_status: Optional[str] = None,
    job_data_schema: Optional[str] = None,
    job_data: Optional[str] = None,
) -> Job:
    """Make an update to a job entry.

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        used as identifier for the resource.
    job_slug: str
        identifier used to retrieve the job.
    parent_job_slug: Optional[str]
        slug of the job which created this job.
    service_identifier: Optional[str]
        id typically generated as a result of making a request to an external system.
    status: {Optionapstr
        status of the job. Refer to the  platform for possible values.
    remote_status: Optional[str]
        status of job that was initiated on an  external (non-Strangeworks) system.
    job_data_schema: Optional[str]
        link to the json schema describing job output.
    job_data: Optional[str]
        job output.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=update_request,
        **locals(),
    )
    return Job.from_dict(platform_result["jobUpdate"]["job"])


def get_job_request(query: str, job_param_name: str) -> Operation:
    return Operation(
        query=f"""
        query {query} (
            $resource_slug: String!,
            $id: String!) {{
            {query}(
                resourceSlug: $resource_slug,
                {job_param_name}: $id
            )
            {{
                id
                childJobs {{
                    id
                }}
                serviceIdentifier
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
            }}
        }}
        """
    )


def get(
    api: API,
    resource_slug: str,
    id: str,
) -> Job:
    """Retrieve job info

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        identifier for the resource.
    id: str
        the job_slug identifier used to retrieve the job.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=get_job_request("job", "jobSlug"),
        **locals(),
    )
    return Job.from_dict(platform_result["job"])


def get_by_service_identifier(
    api: API,
    resource_slug: str,
    id: str,
) -> Job:
    """Retrieve job info

    Parameters
    ----------
    api: API
        provides access to the platform API.
    resource_slug: str
        identifier for the resource.
    id: str
        the service_identifier used to retrieve the job.

    Returns
    -------
    : Job
        The ``Job`` object
    """
    platform_result = api.execute(
        op=get_job_request("jobByServiceIdentifier", "serviceIdentifier"),
        **locals(),
    )
    return Job.from_dict(platform_result["jobByServiceIdentifier"])


upload_file_request = Operation(
    query="""
        mutation jobUploadFile(
            $resource_slug: String!,
            $job_slug: String!,
            $override_existing: Boolean!,
            $file_desc: Upload!,
            $file_name: String,
        ){
            jobUploadFile(
                input: {
                    resourceSlug: $resource_slug,
                    jobSlug: $job_slug,
                    shouldOverrideExistingFile: $override_existing,
                    file: $file_desc,
                    fileName: $file_name,
                }
            ){
                file {
                    id
                    slug
                    label
                    fileName
                    url
                    metaFileType
                    metaDateCreated
                    metaDateModified
                    metaSizeBytes
                    jsonSchema
                    dateCreated
                    dateUpdated
                }
            }
        }
        """,
    upload_files=True,
)


def upload_file(
    api: API,
    resource_slug: str,
    job_slug: str,
    file_path: str,
    file_name: Optional[str],
    override_existing: bool = False,
):
    """Upload a file associated with a job."""
    with open(file_path, "rb") as fd:
        platform_result = api.execute(
            op=upload_file_request,
            resource_slug=resource_slug,
            job_slug=job_slug,
            file_desc=fd,
            file_name=file_name,
            override_existing=override_existing,
        )
        return File.from_dict(platform_result["jobUploadFile"]["file"])
