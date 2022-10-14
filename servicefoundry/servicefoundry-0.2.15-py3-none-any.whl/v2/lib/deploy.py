import time
from typing import List, TypeVar

from pydantic import BaseModel
from rich.status import Status

from servicefoundry.auto_gen import models as auto_gen_models
from servicefoundry.lib.clients.service_foundry_client import (
    ServiceFoundryServiceClient,
)
from servicefoundry.lib.dao.workspace import get_workspace_by_fqn
from servicefoundry.logger import logger
from servicefoundry.v2.lib.models import (
    BuildResponse,
    Deployment,
    DeploymentTransitionStatus,
)
from servicefoundry.v2.lib.source import local_source_to_remote_source

Component = TypeVar("Component", bound=BaseModel)


def _upload_component_source_if_local(
    component: Component, workspace_fqn: str
) -> Component:
    if (
        hasattr(component, "image")
        and isinstance(component.image, auto_gen_models.Build)
        and isinstance(component.image.build_source, auto_gen_models.LocalSource)
    ):
        new_component = component.copy(deep=True)

        logger.info("Uploading code for %s '%s'", component.type, component.name)

        new_component.image.build_source = local_source_to_remote_source(
            local_source=component.image.build_source,
            workspace_fqn=workspace_fqn,
            component_name=component.name,
        )

        logger.debug("Uploaded code for %s '%s'", component.type, component.name)
        return new_component
    return component


def _log_hosts_for_services(deployment: Deployment):
    base_domain_url = deployment.baseDomainURL
    workspace_name = deployment.workspace.get("name", "")
    components = deployment.manifest.get("components", [])

    if not base_domain_url:
        logger.debug("Cannot print service hosts as baseDomainURL is empty")
        return

    if not workspace_name:
        logger.debug("Cannot print service hosts as workspace is empty")
        return

    for component in components:
        component_name = component.get("name", "")
        component_type = component.get("type", "")

        if component_type != "service":
            continue

        if not component_name:
            logger.debug("Cannot print service host as component name is empty")
            continue

        url = f"https://{component_name}-{workspace_name}.{base_domain_url}"
        logger.info(
            "Service '%s' will be available at\n'%s'\nafter successful deployment",
            component_name,
            url,
        )


def _log_application_dashboard_url(deployment: Deployment, log_message: str):
    application_id = deployment.applicationId

    # TODO: is there any simpler way to get this? :cry
    client = ServiceFoundryServiceClient.get_client()
    base_url = client.session.profile.server_config.base_url

    url = f"{base_url}/applications/{application_id}?tab=deployments"
    logger.info(log_message, url)


def _tail_build_logs(build_responses: List[BuildResponse]) -> None:
    client = ServiceFoundryServiceClient.get_client()

    # TODO: Explore other options like,
    # https://rich.readthedocs.io/en/stable/live.html#live-display
    # How does docker/compose does multiple build logs?
    for build_response in build_responses:
        logger.info("Tailing build logs for '%s'", build_response.componentName)
        client.tail_build_logs(build_response=build_response, wait=True)


def _deploy_wait_handler(deployment: Deployment):
    _log_application_dashboard_url(
        deployment=deployment,
        log_message=(
            "You can track the progress below or on the dashboard:- '%s'\n"
            "You can press Ctrl + C to exit the tailing of build logs "
            "and deployment will continue on the server"
        ),
    )
    with Status(status="Polling for deployment status") as spinner:
        last_status_printed = None
        client = ServiceFoundryServiceClient.get_client()
        start_time = time.monotonic()
        total_timeout_time: int = 300
        poll_interval_seconds = 5
        time_elapsed = 0

        for deployment_statuses in client.poll_deployment_statuses(
            application_id=deployment.applicationId,
            deployment_id=deployment.id,
            poll_after_secs=poll_interval_seconds,
        ):
            if len(deployment_statuses) == 0:
                logger.warning("Did not receive any deployment status")
                continue

            latest_deployment_status = deployment_statuses[-1]

            status_to_print = (
                latest_deployment_status.transition or latest_deployment_status.status
            )
            spinner.update(status=f"Current state: {status_to_print!r}")
            if status_to_print != last_status_printed:
                logger.info("State: %r", status_to_print)
                last_status_printed = status_to_print

            if latest_deployment_status.state.isTerminalState:
                break

            if (
                latest_deployment_status.transition
                == DeploymentTransitionStatus.BUILDING
            ):
                build_responses = client.get_deployment_build_response(
                    application_id=deployment.applicationId, deployment_id=deployment.id
                )
                _tail_build_logs(build_responses)

            time_elapsed = time.monotonic() - start_time
            if time_elapsed > total_timeout_time:
                logger.info("Polled server for %s secs.", int(time_elapsed))
                break


def deploy_application(
    application: auto_gen_models.Application,
    workspace_fqn: str,
    wait: bool = False,
) -> Deployment:
    logger.info("Deploying application '%s' to '%s'", application.name, workspace_fqn)

    # print(application.yaml())
    workspace_id = get_workspace_by_fqn(workspace_fqn).id
    updated_component_definitions = []

    for component in application.components:
        updated_component = _upload_component_source_if_local(
            component=component, workspace_fqn=workspace_fqn
        )
        updated_component_definitions.append(updated_component)

    new_application_definition = auto_gen_models.Application(
        name=application.name, components=updated_component_definitions
    )
    client = ServiceFoundryServiceClient.get_client()
    response = client.deploy_application(
        workspace_id=workspace_id, application=new_application_definition
    )
    logger.info(
        "🚀 Deployment started for application '%s'. Deployment FQN is '%s'.",
        application.name,
        response.fqn,
    )
    if wait:
        try:
            _deploy_wait_handler(deployment=response)
        except KeyboardInterrupt:
            logger.info("Ctrl-c executed. The deployment will still continue.")
    _log_application_dashboard_url(
        deployment=response,
        log_message="🚀 You can find the application on the dashboard:- '%s'",
    )
    # _log_hosts_for_services(deployment=response)
    return response


def deploy_component(
    component: Component, workspace_fqn: str, wait: bool = False
) -> Deployment:
    application = auto_gen_models.Application(
        name=component.name, components=[component]
    )
    return deploy_application(
        application=application,
        workspace_fqn=workspace_fqn,
        wait=wait,
    )
