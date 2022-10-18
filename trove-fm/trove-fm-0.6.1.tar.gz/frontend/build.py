#!/usr/bin/env python

"""
This script will:
    1. build the React app in the Dev container (nodejs)
    2. copy the build artifact and build the Prod container (nginx)
    3. upload the newly built Prod container to the Cove repo

During this process, care will be taken to ensure that versioning is
appropriate.

Contact: brian.farrell@me.com

"""


import argparse
import json
import logging
import pathlib
import subprocess
import sys

import docker
from packaging import version


ERROR_DOCKER_API = 'Docker API Error'
ERROR_DOCKER_NOT_FOUND = 'Docker NotFound Error'
ERROR_DOCKER_BUILD = 'Docker Build Error'
ERROR_SYSTEM_COMMAND = 'System Command Error'
ERROR_VERSION = 'Version Error'

DEFAULT_REGISTRY = 'cove:5001'
DEFAULT_IMAGE_NAME = 'trove-cleaners-ui'
DOCKER_DEV_IMAGE = 'trove-poc_poc:latest'
DOCKER_BUILDER_CONTAINER_NAME = 'trove.poc.builder'

BASE_DIR = pathlib.Path(__file__).parent
PACKAGE_FILE = pathlib.Path('package.json')
PROD_DOCKERFILE = pathlib.Path('Prod.dockerfile')
DOCKER_COMPOSE_FILE = BASE_DIR.joinpath('..', 'docker-compose-dev.yaml')

LOG_FILE = str(BASE_DIR.joinpath('build.log'))

logging.basicConfig(
    format='%(asctime)s\t%(levelname)s\t%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

parser = argparse.ArgumentParser(
    prog='build',
    description='Build the React UI in a Docker container and upload to Cove.',
    conflict_handler='resolve',
    formatter_class=argparse.RawTextHelpFormatter,
    epilog='\n \n',
)

parser.add_argument(
    '-i', '--ignore-version',
    action='store_true',
    dest='ignore_flag',
    help="Ignore version check."
)

parser.add_argument(
    '-n', '--image-name',
    action='store',
    dest='image_name',
    nargs='?',
    const=DEFAULT_IMAGE_NAME,
    default=DEFAULT_IMAGE_NAME,
    help="Specify the name of the Docker container."
)

parser.add_argument(
    '--no-push',
    action='store_true',
    dest='no_push',
    help="Don't push the newly built container to the repo."
)

parser.add_argument(
    '--no-stop',
    action='store_true',
    dest='no_stop',
    help=f"Don't stop the builder container at the end of the build. (Useful for debugging)"
)

parser.add_argument(
    '-r', '--registry',
    action='store',
    dest='registry',
    nargs='?',
    const=DEFAULT_REGISTRY,
    default=DEFAULT_REGISTRY,
    help="Specify the Docker repo to use."
)


def shutdown_services(compose_file):
    error_message = f"Encountered an error while trying to shutdown services in {compose_file}"
    try:
        result = subprocess.run(['docker-compose', '-f', compose_file, 'down'], capture_output=True)
    except subprocess.CalledProcessError as e:
        raise BuildError(
            error_message,
            error_type=ERROR_SYSTEM_COMMAND,
            status_code=e.returncode,
            error_string=e.stderr
        )
    else:
        if result.returncode > 0:
            raise BuildError(
                error_message,
                error_type=ERROR_SYSTEM_COMMAND,
                status_code=result.returncode,
                error_string=result.stderr.decode()
            )
        else:
            logging.info(f"Shutdown services in {compose_file}")


def run_container(client, image, command, **kwargs):
    try:
        container = client.containers.run(image, command, **kwargs)
    except docker.errors.APIError as e:
        cname = kwargs.get('name')
        if e.response.status_code == 409:
            logging.warning(
                f"A container with the name {cname} is already running."
            )
        yes_answers = ["y", "yes"]
        stop_instance = input(f"\n\nDo you want to stop the {cname} container? (y/n) ").lower()
        if stop_instance in yes_answers:
            logging.info(f"Stopping {cname} container so we can start a new instance.")
            stop_target = get_container(client, cname)
            stop_target.stop()
            return run_container(client, image, command, **kwargs)
        else:
            message = f"The {cname} container will not be stopped. Build cannot continue."
            raise BuildError(message, error_type=ERROR_DOCKER_API)
    else:
        return container


def get_json(file):
    logging.info(f"Opening {file}")
    with open(file, 'r') as stream:
        data = json.load(stream)

    return data


def set_json(file, data):
    with open(file, 'w') as stream:
        json.dump(data, stream, indent=2)


def get_version(project_data, ignore_flag):
    current_version = version.parse(project_data.get("version"))
    last_version = version.parse(project_data.get("lastVersion"))

    if ignore_flag:
        logging.warning("Ignoring version number for this build!!!")
        return str(current_version)

    if current_version > last_version:
        return str(current_version)
    else:
        message = (
            f"Current version: {current_version} <= Last version: {last_version} "
            f"Please fix {str(PACKAGE_FILE)} before proceeding."
        )
        raise BuildError(message, error_type=ERROR_VERSION)


def update_last_version(project_data, current_version):
    project_data['lastVersion'] = current_version
    set_json(PACKAGE_FILE, project_data)
    logging.info(f"Updated lastVersion to {current_version} in {str(PACKAGE_FILE)}")


def remove_item(path):
    error_message = f"Encountered an error while trying to remove {path}"
    try:
        result = subprocess.run(["rm", "-rf", path], capture_output=True)
    except subprocess.CalledProcessError as e:
        raise BuildError(
            error_message,
            error_type=ERROR_SYSTEM_COMMAND,
            status_code=e.returncode,
            error_string=e.stderr
        )
    else:
        if result.returncode > 0:
            raise BuildError(
                error_message,
                error_type=ERROR_SYSTEM_COMMAND,
                status_code=result.returncode,
                error_string=result.stderr.decode()
            )
        else:
            logging.info(f"Removing build directory at {path}")


def get_container(client, name):
    container = None

    try:
        container = client.containers.get(name)
    except docker.errors.NotFound:
        message = (
            f"Docker could not find the container {name} "
            f"Please ensure that it is running, then try again."
        )
        raise BuildError(message, error_type=ERROR_DOCKER_NOT_FOUND)
    else:
        logging.info(f"Retrieved container {name}")

    return container


def run_command_in_container(client, command, container_name):
    container = get_container(client, container_name)

    try:
        _, stream = container.exec_run(command, stream=True, tty=True)
    except docker.errors.APIError as e:
        message = (
            f"An error occured while running command {command} in {container_name} "
            f"Please ensure that it is running, then try again."
        )
        raise BuildError(message, error_type=ERROR_DOCKER_API, error_string=str(e))
    else:
        for data in stream:
            print(data.decode())


def build_container(client, build_path, dockerfile, tag):
    logging.info(f"Building Docker Image: {tag}")

    try:
        image, build_logs = client.images.build(
            path=build_path,
            dockerfile=dockerfile,
            tag=tag,
            rm=True
        )
    except docker.errors.BuildError as e:
        message = (
            f"A Docker Build Error occured while building {build_path}/{dockerfile}"
        )
        es = f"\nReason:{e.msg}\n\nBuild Log:\n{e.build_log}"
        raise BuildError(message, error_type=ERROR_DOCKER_BUILD, error_string=str(es))
    except docker.errors.APIError as e:
        message = (
            f"An Unknown Error occurred while building {build_path}/{dockerfile}"
        )
        raise BuildError(message, error_type=ERROR_DOCKER_API, error_string=str(e))
    else:
        for line in build_logs:
            print(line.get('stream', ''))
        logging.info(f"Successfully built image {tag}")

        return image


def tag_image(source_image, target_image, image_tag):
    logging.info(f"Tagging new image with tag: {image_tag}")

    try:
        source_image.tag(target_image, image_tag)
    except docker.errors.APIError as e:
        message = f"\nDocker encountered an Unknown Error while tagging {image_tag}"
        raise BuildError(message, error_type=ERROR_DOCKER_API, error_string=str(e))
    else:
        logging.info(
            f"Successfully tagged new image with current version {target_image}:{image_tag}"
        )


def push_to_registry(client, repository, registry, tags):
    logging.info(f"Pushing {repository} to {registry}")

    for t in tags:
        try:
            result = client.images.push(repository, tag=t, stream=True, decode=True)
        except docker.errors.APIError as e:
            message = f"A Docker error occured while pushing {repository:t} to {registry}"
            raise BuildError(message, error_type=ERROR_DOCKER_API, error_string=str(e))
        else:
            logging.info(f"Successfully pushed {repository}:{t} to {registry}")
            for line in result:
                if line.get('aux', None) is not None:
                    pushed_tag = line['aux'].get('Tag')
                    pushed_digest = line['aux'].get('Digest')
                    logging.info(f"Pushed Image: {repository}:{pushed_tag}")
                    logging.info(f"Image Digest: {pushed_digest}")


def main():
    args = parser.parse_args()
    repository = f"{args.registry}/{args.image_name}"
    build_tag = f"{repository}:latest"
    build_container_start_cmd = ['tail', '-f', '/dev/null']
    project_data = get_json(PACKAGE_FILE)
    current_version = get_version(project_data, args.ignore_flag)
    build_dir = str(BASE_DIR.joinpath('build'))
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    remove_item(build_dir)

    shutdown_services(DOCKER_COMPOSE_FILE)

    logging.info(f"Starting Container {DOCKER_BUILDER_CONTAINER_NAME}")

    # IMPORTANT: Need to hard-code the string values for the environment variables below, as
    # for reasons unknown, when we use interpolated strings, the REACT_APP_API_SERVER value
    # gets cast as a tuple before it is set in the container.

    react_build_container = run_container(
        client,
        DOCKER_DEV_IMAGE,
        build_container_start_cmd,
        environment=[
            f"REACT_APP_API_SERVER=https://poc.trove.fm",
            f"REACT_APP_API_ENDPOINT=/api"
        ],
        name=DOCKER_BUILDER_CONTAINER_NAME,
        network_mode='host',
        volumes={
            str(BASE_DIR): {'bind': '/app', 'mode': 'rw'},
            'dev_poc_node_modules': {'bind': '/app/node_modules', 'mode': 'rw'}
        },
        detach=True,
        remove=True
    )

    logging.info(f"React Build container {react_build_container.status}")
    logging.info(f"Running React Build in {react_build_container.name}")
    logging.info(f"Building Version {current_version}")

    run_command_in_container(client, ["npm", "run", "build"], react_build_container.name)

    logging.info(f"React Build complete in {react_build_container.name}")

    new_image = build_container(
        client, build_path=str(BASE_DIR), dockerfile=str(PROD_DOCKERFILE), tag=build_tag
    )

    tag_image(new_image, repository, current_version)

    if args.no_push:
        logging.info(f"The --no-push argument was passed. Repositories will not be pushed.")
    else:
        push_to_registry(client, repository, args.registry, ['latest', current_version])

    if args.no_stop:
        logging.info(f"The --no-stop argument was passed. {react_build_container.name} will not be stopped.")
    else:
        logging.info(f"Stopping React Build container: {react_build_container.short_id}")
        react_build_container.stop()

    logging.info(f"React Build container {react_build_container.status}")

    update_last_version(project_data, current_version)

    logging.info("Build Completed Successfully")


class BuildError(Exception):
    """Exception raised for bad version"""

    def __init__(self, message, error_type=None, error_number=None, error_string=None, status_code=None):
        metadata = f"\n"

        if error_type:
            metadata += f"\nError Type: {error_type}"

        if error_number:
            metadata += f"\nError Number: {error_number}"

        if error_string:
            metadata += f"\nError String: {error_string}"

        metadata += "\nExiting...\n"

        self.message = message + metadata


if __name__ == "__main__":
    try:
        logging.info('---------- Build started ----------')
        logging.info(f"Running build from {BASE_DIR}")
        main()
    except BuildError as e:
        logging.error(e.message)
        sys.exit()
