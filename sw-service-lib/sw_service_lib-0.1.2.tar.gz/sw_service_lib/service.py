import os
from dataclasses import dataclass
from typing import List, Optional

from fastapi import Request
from jose import jwt

from sw_service_lib import billing, job, resource
from sw_service_lib.billing import BillingTransaction
from sw_service_lib.error import StrangeworksError
from sw_service_lib.job import File, Job
from sw_service_lib.platform import API
from sw_service_lib.resource import Resource


@dataclass
class RequestContext:
    resource_token_id: str
    workspace_member_slug: str
    product_slug: str
    resource_slug: str
    job_id: Optional[str] = None
    resource_entitlements: Optional[List[str]] = None
    api: Optional[API] = None

    @staticmethod
    def new(
        workspace_member_slug: str,
        product_slug: str,
        resource_slug: str,
        resource_token_id: str = "",
        job_id: str = None,
        resource_entitlements: List[str] = None,
        api: API = None,
    ):
        return RequestContext(
            resource_token_id=resource_token_id,
            workspace_member_slug=workspace_member_slug,
            product_slug=product_slug,
            resource_slug=resource_slug,
            job_id=job_id,
            resource_entitlements=resource_entitlements,
            api=api,
        )

    @staticmethod
    def from_request(request: Request):
        token = request.headers.get("x-strangeworks-access-token")
        if not token:
            raise StrangeworksError.forbidden_error(
                message="request missing access token"
            )
        return RequestContext.from_jwt(token)

    @staticmethod
    def from_jwt(token: str):
        message = jwt.decode(token=token, key=None, options={"verify_signature": False})
        return RequestContext(
            resource_token_id=message["ResourceTokenID"],
            workspace_member_slug=message["WorkspaceMemberSlug"],
            product_slug=message["ProductSlug"],
            resource_slug=message["ResourceSlug"],
            resource_entitlements=message["ResourceEntitlements"],
        )


DEFAULT_PLATFORM_BASE_URL = "https://api.strangeworks.com"
api_key = os.getenv("SERVICE_LIB_API_KEY")
base_url = os.getenv("SERVICE_LIB_BASE_URL", DEFAULT_PLATFORM_BASE_URL)

_api = API(api_key=api_key, base_url=base_url)


def create_job(
    ctx: RequestContext,
    parent_job_slug: Optional[str] = None,
    service_identifier: Optional[str] = None,
    status: str = "CREATED",
    remote_status: Optional[str] = None,
    job_data_schema: Optional[str] = None,
    job_data: Optional[str] = None,
    **kvargs
) -> Job:
    """Create a job entry for the request

    This method should be called only after the service has either has a job in place
    which will be executed either immediately or within a given period of time.

    Parameters
    ----------
    ctx: RequestContext
        contains key-values specific to the current request.
    parent_job_slug: Optional[str]
        slug of the job which created this job.
    service_identifier: Optional[str]
        id typically generated as a result of making a request to an external system.
    status: Optional[str]
        status of the job. Refer to the  platform for possible values.
    remote_status: Optional[str]
        status of job that was initiated on an  external (non-Strangeworks) system.
    job_data_schema: Optional[str]
        link to the json schema describing job output.
    job_data: Optional[str]
        job output.
    """
    return job.create(
        api=ctx.api or _api,
        resource_slug=ctx.resource_slug,
        workspace_member_slug=ctx.workspace_member_slug,
        parent_job_slug=parent_job_slug,
        service_identifier=service_identifier,
        status=status,
        remote_status=remote_status,
        job_data_schema=job_data_schema,
        job_data=job_data,
    )


def update_job(
    ctx: RequestContext,
    job_slug: str,
    parent_job_slug: Optional[str] = None,
    service_identifier: Optional[str] = None,
    status: Optional[str] = None,
    remote_status: Optional[str] = None,
    job_data_schema: Optional[str] = None,
    job_data: Optional[str] = None,
    **kvargs
) -> Job:
    """Update the job identified by job_slug.


    Parameters
    ----------
    ctx: RequestContext
        contains key-values specific to the current request.
    job_slug: str
      slug of the job that needs values updated.
    parent_job_slug: Optional[str]
        slug of the job which created this job.
    service_identifier: Optional[str]
        id typically generated as a result of making a request to an external system.
    status: Optional[str]
        status of the job. Refer to the  platform for possible values.
    remote_status: Optional[str]
        status of job that was initiated on an  external (non-Strangeworks) system.
    job_data_schema: Optional[str]
        link to the json schema describing job output.
    job_data: Optional[str]
        job output.
    """
    return job.update(
        api=ctx.api or _api,
        resource_slug=ctx.resource_slug,
        job_slug=job_slug,
        parent_job_slug=parent_job_slug,
        service_identifier=service_identifier,
        status=status,
        remote_status=remote_status,
        job_data_schema=job_data_schema,
        job_data=job_data,
    )


def create_billing_transaction(
    ctx: RequestContext,
    job_slug: str,
    amount: float,
    unit: str = "USD",
    description: Optional[str] = None,
) -> BillingTransaction:
    """Create a billing transaction.

    Parameters
    ----------
    ctx: RequestContext
        contains key-values specific to the current request.
    job_slug: str
        used as identifier for the job.
    amount: float
        numerical amount. can be negative.
    unit: str
        describes the unit for the amount. for example, USD for currency.
    description: str
        a brief description that can be seen by the user.
    """
    return billing.create_transaction(
        api=ctx.api or _api,
        resource_slug=ctx.resource_slug,
        job_slug=job_slug,
        amount=amount,
        unit=unit,
        description=description,
    )


def request_job_clearance(
    ctx: RequestContext,
    amount: float,
    unit: str = "USD",
):
    """Request clearance from platform to run a job.

    Parameters
    ----------
    workspaceMemberSlug: str
            used to map workspace and user.
    amount: float
        numerical amount to indicate cost (negative amount) or credit(positive amount)
    unit: str
        unit for the amount
    """
    return billing.request_approval(
        api=ctx.api or _api,
        resource_slug=ctx.resource_slug,
        workspace_member_slug=ctx.workspace_member_slug,
        amount=amount,
        currency=unit,
    )


def get_resource(ctx: RequestContext) -> Resource:
    """Retrieve a resource definition.

    The resource slug, which is used to identify the resource entry, is retrieved
    from the request context object passed in.

    Parameters:
    ctx: RequestContext
        contains key-values specific to the current request.

    """
    return resource.get(api=_api, resource_slug=ctx.resource_slug)


def upload_job_file(
    ctx: RequestContext,
    job_slug: str,
    name: Optional[str],
    path: str,
) -> File:
    """Upload a file associated with a job.

    Parameters
    ----------
    ctx: RequestContext
        contains key-values specific to the current request.
    job_slug: str
        identifies which job the file is associated with.
    name: Optional[str]
        file name.
    path: str
        fully qualified path to the file.
    """
    return job.upload_file(
        api=ctx.api or _api,
        resource_slug=ctx.resource_slug,
        job_slug=job_slug,
        file_path=path,
        file_name=name,
    )


def get_job(ctx: RequestContext, job_slug: str) -> Job:
    """Get the job identified by job_slug.


    Parameters
    ----------
    ctx: RequestContext
        contains key-values specific to the current request.
    job_slug: str
        job_slug identifies the job which is fetched.
    """
    return job.get(api=ctx.api or _api, resource_slug=ctx.resource_slug, id=job_slug)


def get_job_by_service_identifier(ctx: RequestContext, service_identifier: str) -> Job:
    """Get the job identified by service_identifier.


    Parameters
    ----------
    ctx: RequestContext
        contains key-values specific to the current request.
    service_identifier: str
        service_identifier identifies the job which is fetched.
    """
    return job.get_by_remote_id(
        api=ctx.api or _api,
        resource_slug=ctx.resource_slug,
        id=service_identifier,
    )
