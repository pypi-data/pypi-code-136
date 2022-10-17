from datetime import datetime
from typing import Any, Dict, List, Optional

import aiofiles
import aiohttp
import requests
from gql import Client, gql

from sw_service_lib.billing import BillingTransaction
from sw_service_lib.error import StrangeworksError
from sw_service_lib.job import File, Job
from sw_service_lib.resource import (
    Resource,
    ResourceConfiguration,
    ResourceConfigurationValueType,
)
from sw_service_lib.transport import StrangeworksTransport


# Default url and define setter
__root = "/services"
__url = "https://api.strangeworks.com"
__headers = {}
__api_token = None
__jwt_token = None
__token_refresh = None


def set_url(url: str):
    """ """
    global __url
    __url = url


def set_custom_headers(header: dict):
    global __headers
    __headers = header


def add_header(key: str, value: Any):
    global __headers
    __headers[key] = value


def set_api_token(api_token: str):
    global __api_token
    __api_token = api_token


"""
BILLING CLIENT
"""


def request_billing_approval(
    resourceSlug: str, workspaceMemberSlug: str, amount: float, currency: str
) -> bool:
    """
    precheck billing approval to ensure a
    """
    __request_billing_approval_query = gql(
        """
        query requestBillingApproval (
            $resourceSlug: String!,
            $workspaceMemberSlug: String!,
            $amount: Float!,
            $currency: Currency!,
        ){
            requestBillingApproval(
                resourceSlug: $resourceSlug,
                workspaceMemberSlug: $workspaceMemberSlug,
                amount: $amount,
                currency: $currency){
                isApproved
                rejectionMessage
            }
        }
    """
    )
    client = __new_client()
    res = client.execute(
        __request_billing_approval_query,
        variable_values={
            "resourceSlug": resourceSlug,
            "workspaceMemberSlug": workspaceMemberSlug,
            "amount": amount,
            "currency": currency,
        },
    )
    if not res["requestBillingApproval"]["isApproved"]:
        raise RuntimeError(res["rejectionMessage"])
    return True


def create_billing_transaction(
    resource_slug: str,
    job_slug: str,
    amount: float,
    unit: str,
    description: str,
    memo: str = None,
) -> BillingTransaction:
    """
    create a billing transaction associated to the resource
    """
    __create_billing_transaction_mutation = gql(
        """
        mutation billingTransactionCreate(
            $resourceSlug: String!,
            $jobSlug: String!,
            $amount: Float!,
            $unit: Currency!,
            $description: String!,
            $memo: String,
        ){
            billingTransactionCreate(input: {
                resourceSlug: $resourceSlug,
                jobSlug: $jobSlug,
                amount: $amount,
                unit: $unit,
                description: $description,
                memo: $memo,
            }){
                billingTransaction {
                    id
                    status
                    amount
                    unit
                    description
                    memo
                }
            }
        }
        """
    )
    client = __new_client()
    res = client.execute(
        __create_billing_transaction_mutation,
        variable_values={
            "resourceSlug": resource_slug,
            "jobSlug": job_slug,
            "amount": amount,
            "unit": unit,
            "description": description,
            "memo": memo,
        },
    )
    if not res["billingTransactionCreate"]:
        raise RuntimeError(res["errors"])
    return BillingTransaction.from_dict(
        res["billingTransactionCreate"]["billingTransaction"]
    )


"""
JOB CLIENT
"""


def create_job(
    resource_slug: str,
    workspace_member_slug: str,
    parent_job_slug: str = None,
    service_identifier: str = None,
    member_slug: str = None,
    status: str = None,
    remote_status: str = None,
    job_data_schema: str = None,
    job_data: dict = None,
) -> Job:
    """
    create a job associated with the resource
    """
    __create_job_mutation = gql(
        """
        mutation jobCreate(
            $resourceSlug: String!,
            $workspaceMemberSlug: String!,
            $parentJobSlug: String,
            $serviceIdentifier: String,
            $memberSlug: String,
            $status: JobStatus,
            $remoteStatus: String,
            $jobDataSchema: String,
            $jobData: JSON,
        ){
            jobCreate(input: {
                resourceSlug: $resourceSlug,
                workspaceMemberSlug: $workspaceMemberSlug,
                parentJobSlug: $parentJobSlug,
                serviceIdentifier: $serviceIdentifier,
                memberSlug: $memberSlug,
                status: $status,
                remoteStatus: $remoteStatus,
                jobDataSchema: $jobDataSchema,
                jobData: $jobData,
            }){
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
        """
    )
    client = __new_client()
    res = client.execute(
        __create_job_mutation,
        variable_values={
            "resourceSlug": resource_slug,
            "workspaceMemberSlug": workspace_member_slug,
            "parentJobSlug": parent_job_slug,
            "serviceIdentifier": service_identifier,
            "memberSlug": member_slug,
            "status": status,
            "remoteStatus": remote_status,
            "jobDataSchema": job_data_schema,
            "jobData": job_data,
        },
    )
    if not res["jobCreate"]:
        raise RuntimeError(res["errors"])
    return Job.from_dict(res["jobCreate"]["job"])


def update_job(
    resource_slug: str,
    job_slug: str,
    parent_job_slug: str = None,
    service_identifier: str = None,
    member_slug: str = None,
    status: str = None,
    remote_status: str = None,
    job_data_schema: str = None,
    job_data: dict = None,
) -> Job:
    """
    update a job owned by the resource
    """
    __update_job_mutation = gql(
        """
        mutation jobUpdate(
            $resourceSlug: String!,
            $jobSlug: String!,
            $parentJobSlug: String,
            $serviceIdentifier: String,
            $status: JobStatus,
            $remoteStatus: String,
            $jobDataSchema: String,
            $jobData: JSON,
        ){
            jobUpdate(input: {
                resourceSlug: $resourceSlug,
                jobSlug: $jobSlug,
                parentJobSlug: $parentJobSlug,
                serviceIdentifier: $serviceIdentifier,
                status: $status,
                remoteStatus: $remoteStatus,
                jobDataSchema: $jobDataSchema,
                jobData: $jobData,
            }){
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
        """
    )
    client = __new_client()
    res = client.execute(
        __update_job_mutation,
        variable_values={
            "resourceSlug": resource_slug,
            "jobSlug": job_slug,
            "parentJobSlug": parent_job_slug,
            "serviceIdentifier": service_identifier,
            "memberSlug": member_slug,
            "status": status,
            "remoteStatus": remote_status,
            "jobDataSchema": job_data_schema,
            "jobData": job_data,
        },
    )
    if not res["jobUpdate"]:
        raise RuntimeError(res["errors"])
    return Job.from_dict(res["jobUpdate"]["job"])


def upload_job_file(
    resource_slug: str,
    job_slug: str,
    file_name: str,
    file_path: str = None,
    file_url: str = None,
    should_override_existing_file: bool = False,
) -> File:
    """
    upload a job file either from local disk using file_path or from
    a location using file_url
    """
    __upload_job_file = gql(
        """
        mutation jobUploadFile(
            $resourceSlug: String!,
            $jobSlug: String!,
            $shouldOverrideExistingFile: Boolean!,
            $file: Upload!,
            $fileName: String,
        ){
            jobUploadFile(
                input: {
                    resourceSlug: $resourceSlug,
                    jobSlug: $jobSlug,
                    shouldOverrideExistingFile: $shouldOverrideExistingFile,
                    file: $file,
                    fileName: $fileName,
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
        """
    )
    client = __new_client()

    # upload file from url
    if file_url:

        async def downloaded_file(file_url):
            async with aiohttp.ClientSession() as http_client:
                async with http_client.get(file_url) as resp:
                    return resp

        res = client.execute(
            __upload_job_file,
            variable_values={
                "resourceSlug": resource_slug,
                "jobSlug": job_slug,
                "fileName": file_name,
                "shouldOverrideExistingFile": should_override_existing_file,
                "file": downloaded_file(file_url),
            },
            upload_files=True,
        )
        if not res["jobUploadFile"]:
            raise RuntimeError(res["errors"])
        return File.from_dict(res["jobUploadFile"]["file"])

    # throw error if neither file_path nor url are selected
    if not file_path:
        raise RuntimeError(
            "must include either file_path or file_url to upload job file"
        )

    # set up chunking function
    async def file_sender(file_name):
        async with aiofiles.open(file_name, "rb") as f:
            chunk = await f.read(64 * 1024)
            while chunk:
                yield chunk
                chunk = await f.read(64 * 1024)

    with open(file_path, "rb") as f:
        # upload file from disk
        res = client.execute(
            __upload_job_file,
            variable_values={
                "resourceSlug": resource_slug,
                "fileName": file_name,
                "jobSlug": job_slug,
                "shouldOverrideExistingFile": should_override_existing_file,
                "file": f,
            },
            upload_files=True,
        )
        if not res["jobUploadFile"]:
            raise RuntimeError(res["errors"])
        return File.from_dict(res["jobUploadFile"]["file"])


def fetch_job(resource_slug: str, job_slug: str) -> Job:
    """
    fetch a job by its slug, must be owned by
    the resource defined in the auth, though
    child jobs / parent jobs can also be fetched
    as part of the query
    """
    __get_job_query = gql(
        """
        query job ($resourceSlug: String!, $jobSlug: String!) {
            job(resourceSlug: $resourceSlug, jobSlug: $jobSlug){
                id
                childJobs {
                    id
                }
                serviceIdentifier
                slug
                status
                isTerminalState
                remoteStatus
                jobDataSchema
                jobData
            }
        }
    """
    )
    client = __new_client()
    res = client.execute(
        __get_job_query,
        variable_values={"resourceSlug": resource_slug, "jobSlug": job_slug},
    )
    if not res["job"]:
        raise RuntimeError(res["error"])
    return Job.from_dict(res["job"])


"""
RESOURCE CLIENT
"""


def store_resource_configuration(
    key: str,
    resource_slug: str,
    config_type: ResourceConfigurationValueType,
    is_editable: bool,
    is_visible: bool,
    is_internal: bool,
    value,
) -> ResourceConfiguration:
    """
    store a new resource configuration for the resource
    provided by the auth
    """

    __store_resource_configuration_mutation = gql(
        """
        mutation resourceStoreConfiguration(
            $key: String!,
            $resourceSlug: String!,
            $type: ResourceConfigurationValueType!,
            $isEditable: Boolean!,
            $isInternal: Boolean!,
            $valueBool: Boolean,
            $valueString: String,
            $valueSecure: String,
            $valueInt: Int,
            $valueJson: String,
            $valueDate: Time,
            $valueFloat: Float,
        ){
            resourceStoreConfiguration(
                input: {
                    resourceSlug: $resourceSlug,
                    configuration: {
                        key: $key,
                        type: $type,
                        isEditable: $isEditable,
                        isInternal: $isInternal,
                        valueBool: $valueBool,
                        valueString: $valueString,
                        valueSecure: $valueSecure,
                        valueInt: $valueInt,
                        valueJson: $valueJson,
                        valueDate: $valueDate,
                        valueFloat: $valueFloat,
                    }
                }
            ) {
                resourceConfiguration {
                    key
                    type
                    valueBool
                    valueString
                    valueSecure
                    valueInt
                    valueJson
                    valueDate
                    valueFloat
                    isEditable
                    isInternal
                }
            }
        }
        """
    )

    params = {
        "key": key,
        "resourceSlug": resource_slug,
        "type": config_type.name,
        "isEditable": is_editable,
        "isInternal": is_internal,
    }
    if config_type == ResourceConfigurationValueType.BOOL:
        params["valueBool"] = value
    elif config_type == ResourceConfigurationValueType.STRING:
        params["valueString"] = value
    elif config_type == ResourceConfigurationValueType.SECURE:
        params["valueSecure"] = value
    elif config_type == ResourceConfigurationValueType.INT:
        params["valueInt"] = value
    elif config_type == ResourceConfigurationValueType.JSON:
        params["valueJson"] = value
    elif config_type == ResourceConfigurationValueType.DATE:
        params["valueDate"] = value
    elif config_type == ResourceConfigurationValueType.FLOAT:
        params["valueFloat"] = value
    else:
        raise RuntimeError(
            "resource configuration value type must match one of the enums"
        )

    client = __new_client()
    res = client.execute(
        __store_resource_configuration_mutation, variable_values=params
    )
    if not res["resourceStoreConfiguration"]:
        raise RuntimeError(res["error"])
    return ResourceConfiguration.from_dict(
        res["resourceStoreConfiguration"]["resourceConfiguration"]
    )


def fetch_resource(
    slug: str,
) -> Resource:
    """
    fetches the resource w/ configuration from platform
    can only fetch resource associated with auth passed in
    """
    __fetch_resource_query = gql(
        """
        query resource($resourceSlug: String!) {
            resource(resourceSlug: $resourceSlug){

                id
                slug
                status
                isDeleted
                dateCreated
                dateUpdated
                configurations {
                    key
                    type
                    valueBool
                    valueString
                    valueSecure
                    valueInt
                    valueJson
                    valueDate
                    valueFloat
                    isEditable
                    isInternal
                }
            }
        }
    """
    )
    client = __new_client()
    res = client.execute(__fetch_resource_query, variable_values={"resourceSlug": slug})
    if not res["resource"]:
        raise RuntimeError(res["error"])
    return Resource.from_dict(res["resource"])


def resource_create(
    resource_activation_id: str,
    resource_status: str,
    api_route: Optional[str] = None,
    configurations: Optional[List[Dict[str, Any]]] = [],
) -> Resource:
    """
    Creates a new resource from an activation request.
    Optionaly set a specific api_route for the resource.
    Optionally create configurations for the resource.
    """
    __resource_create = gql(
        """
        mutation resourceCreate(
            $resourceActivationId: String!,
            $status: ResourceStatus!,
            $api_route: String,
            $resourceConfigurations: [StoreConfigurationInput!],
        ){
            resourceCreate(input: {
                resourceActivationId: $resourceActivationId,
                status: $status,
                api_route: $api_route,
                resourceConfigurations: $resourceConfigurations,
            }) {
                resource {
                id
                slug
                isDeleted
                status
                dateCreated
                dateUpdated
                configurations {
                    key
                    type
                    valueBool
                    valueString
                    valueSecure
                    valueInt
                    valueJson
                    valueDate
                    valueFloat
                    isEditable
                    isInternal
                }
              }
            }
        }
        """
    )
    client = __new_client()

    # as a form of "type" safety
    # converting between dict -> ResourceConfiguration -> dict
    # ResourceCOnfiguration.form_dict can dictate some rules
    configs = [ResourceConfiguration.from_dict(d).to_dict() for d in configurations]
    res = client.execute(
        __resource_create,
        variable_values={
            "resourceActivationId": resource_activation_id,
            "status": resource_status,
            "api_route": api_route,
            "resourceConfigurations": configs,
        },
    )
    if not res["resourceCreate"]:
        raise RuntimeError(res["errors"])
    return Resource.from_dict(res["resourceCreate"]["resource"])


def resource_update_api_route(resource_slug: str, api_route: str):
    """
    Update the resource's api route.
    """

    __update_api_route = gql(
        """
        mutation resourceUpdate($resourceSlug: String!, $api_route: String) {
            resourceUpdate(input: {
                resourceSlug: $resourceSlug,
                api_route: $api_route
            }) {
                resource {
                id
                slug
                isDeleted
                dateCreated
                dateUpdated
                configurations {
                    key
                    type
                    valueBool
                    valueString
                    valueSecure
                    valueInt
                    valueJson
                    valueDate
                    valueFloat
                    isEditable
                    isInternal
                }
              }
            }
        }
        """
    )
    client = __new_client()
    res = client.execute(
        __update_api_route,
        variable_values={
            "resourceSlug": resource_slug,
            "api_route": api_route,
        },
    )
    if not res["resourceUpdate"]:
        raise RuntimeError(res["errors"])
    return Resource.from_dict(res["resourceUpdate"]["resource"])


def resource_update_status(resource_slug: str, status: str):
    """
    Update the resource's status.
    """

    __update_status = gql(
        """
        mutation resourceUpdateStatus(
            $resourceSlug: String!,
            $status: ResourceStatus!,
        ){
            resourceUpdateStatus(input: {
                resourceSlug: $resourceSlug,
                status: $status
            }) {
                resource {
                id
                slug
                isDeleted
                dateCreated
                dateUpdated
                configurations {
                    key
                    type
                    valueBool
                    valueString
                    valueSecure
                    valueInt
                    valueJson
                    valueDate
                    valueFloat
                    isEditable
                    isInternal
                }
              }
            }
        }
        """
    )
    client = __new_client()
    res = client.execute(
        __update_status,
        variable_values={
            "resourceSlug": resource_slug,
            "status": status,
        },
    )
    if not res["resourceUpdateStatus"]:
        raise RuntimeError(res["errors"])
    return Resource.from_dict(res["resourceUpdateStatus"]["resource"])


def list_resources(statuses: Optional[List[str]] = []) -> List[Resource]:
    """
    list_resources returns all resources that the product owns.
    Optionally pass in a list of statuses to filter by.
    """
    __list_resources = gql(
        """
        query resources($status: [ResourceStatus!]){
            resources(status: $status) {
                id
                slug
                status
                isDeleted
                dateCreated
                dateUpdated
                configurations {
                    key
                    type
                    valueBool
                    valueString
                    valueSecure
                    valueInt
                    valueJson
                    valueDate
                    valueFloat
                    isEditable
                    isInternal
                }
            }
        }
        """
    )

    client = __new_client()
    res = client.execute(__list_resources, variable_values={"status": statuses})

    if "errors" in res:
        raise RuntimeError(res["errors"])
    return [Resource.from_dict(rsc) for rsc in res["resources"]]


# Create a new endpoint for each request, enforces narrow scope for auth
def __new_client() -> Client:
    global __jwt_token
    global __token_refresh
    if __jwt_token is None or __token_expired():
        __refresh_token()
    return Client(
        transport=StrangeworksTransport(base_url=__url + __root, api_key=__api_token)
    )


def __token_expired():
    global __token_refresh
    if __token_refresh is None:
        return False
    split = datetime.now() - __token_refresh
    if (split.seconds / 60) > 22:
        return True
    return False


def __refresh_token():
    global __jwt_token
    global __token_refresh
    url = f"{__url}/service/token"
    res = requests.post(url, json={"key": __api_token})
    if res.status_code != 200:
        raise StrangeworksError.user_error("invalid request to fetch token")
    body = res.json()
    __jwt_token = body["accessToken"]
    __token_refresh = datetime.now()
    add_header(key="Authorization", value=__jwt_token)
