from unicodedata import name
import docker
from typing import Dict
from stochasticx.utils.logging import configure_logger


logger = configure_logger(__name__)


def exists_container(
    container_name: str
) -> bool:
    """Check if container already exists

    :param container_name: container name
    :return: if the container exists or not
    """
    
    client = docker.from_env()
    all_containers = client.containers.list(all=True)
    
    for container in all_containers:
        if container_name == container.name:
            return True
        
    return False


def start_container(
    docker_image: str,
    ports: Dict[str, str],
    container_name: str,
    detach: bool = True,
    gpu: bool = False
):
    """Starts a Docker container locally

    :param docker_image: the Docker image
    :param ports: a dictionary speciying the ports
    :param detach: detach it or not, defaults to True
    :param gpu: use GPUs or not, defaults to False
    """
    client = docker.from_env()
    
    if exists_container(container_name):
        logger.warning("Container {} already running. Stopping and removing it...")
        stop_and_remove_container(container_name)
    
    device_requests = []
    if gpu:
        device_requests = [
            docker.types.DeviceRequest(device_ids=["all"], capabilities=[['gpu']])
        ]

    try:
        container = client.containers.run(
            docker_image, 
            detach=detach,
            ports=ports,
            device_requests=device_requests,
            name=container_name
        )
    except docker.errors.DockerException as ex:
        logger.error(str(ex))
    
    return container.id


def stop_and_remove_container(container_name):
    """Stops and removes the container

    :param container_name: container name
    """
    try:
        client = docker.from_env()
        container = client.containers.get(container_name)
        container.stop()
        container.remove()
    except docker.errors.DockerException as ex:
        logger.error(str(ex))
        
        
def get_logs_container(container_name):
    """Get the logs of a Docker container

    :param container_name: container name
    :return: the logs
    """
    client = docker.from_env()
    
    if exists_container(container_name):
        return client.containers.get(container_name).logs().decode("utf-8")
    else:
        return "No logs\n"
    
def get_open_ports_container(container_name):
    """Get open ports of a Docker container

    :param container_name: container name
    :return: container ports
    """
    client = docker.from_env()
    postprocess_ports = {}
    
    if exists_container(container_name):
        ports = client.containers.get(container_name).ports
        
        for container_port, host_port in ports.items():
            postprocess_ports[container_port] = host_port[0].get("HostPort")
            
        return postprocess_ports
    else:
        return {}