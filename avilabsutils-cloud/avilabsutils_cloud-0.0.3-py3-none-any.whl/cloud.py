from collections import defaultdict
from pathlib import Path
from typing import Callable

import boto3
import click
from botocore.exceptions import WaiterError
from cprint import danger_print, info_print, warning_print
from shell import SSHConfig, SSHConfigEntry


def ec2_start(instance_name: str) -> None:
    ec2 = boto3.client("ec2")
    resp = ec2.describe_instances(
        Filters=[{"Name": "tag:Name", "Values": [instance_name]}]
    )

    if not resp["Reservations"]:
        danger_print(f"There are no instances with name {instance_name}!")
        return

    instances = resp["Reservations"][0]["Instances"]
    if (n_instances := len(instances)) != 1:
        warning_print(f"There {n_instances} instances with name {instance_name}.")
        input("Press [ENTER] to start all of them, CTRL-C to cancel.")

    instance_ids = [instance["InstanceId"] for instance in instances]
    states = [instance["State"] for instance in instances]
    not_stopped_instances = filter(
        lambda ins_state: ins_state[1]["Code"] != 80, zip(instance_ids, states)
    )
    for not_stopped_instance in not_stopped_instances:
        warning_print(
            f"{not_stopped_instance[0]} is in {not_stopped_instance[1]['Name']} state."
        )

    info_print("Starting instances.")
    ec2.start_instances(InstanceIds=instance_ids)

    try:
        waiter = ec2.get_waiter("instance_running")
        waiter.wait(InstanceIds=instance_ids)
    except WaiterError as werr:
        danger_print("Unable to start instances!")
        print(werr)
        return

    resp = ec2.describe_instances(InstanceIds=instance_ids)

    if not resp["Reservations"]:
        danger_print("Something went wrong. Did not get any instances this time!")
        return

    instances = resp["Reservations"][0]["Instances"]
    if len(instances) != n_instances:
        danger_print(
            f"Something went wrong. Got {len(instances)} this time instead of {n_instances} last time!"
        )
        return

    states = [instance["State"] for instance in instances]
    if any(map(lambda s: s["Code"] != 16, states)):
        danger_print("Not all instances are running!")
        return

    info_print("Adding entry to ssh config.")
    username_ami_map = {
        "amzn2": "ec2-user",
        "centos": "centos",
        "debian": "admin",
        "fedora": "fedora",
        "rhel": "root",
        "suse": "root",
        "ubuntu": "ubuntu",
    }
    default_username = "ec2-user"
    image_ids = set(instance["ImageId"] for instance in instances)
    images = ec2.describe_images(ImageIds=list(image_ids))
    usernames = {}
    for image in images["Images"]:
        image_id = image["ImageId"]
        image_name = image["Name"]
        # username = username_ami_map.get(image_name, default_username)
        usernames[image_id] = default_username
        for aminame, username in username_ami_map.items():
            if image_name.find(aminame) != -1:
                usernames[image_id] = username

    ssh_config_file_path = Path.home() / ".ssh" / "config"
    ssh_config_file_path.touch(exist_ok=True)
    ssh_config = SSHConfig.read(ssh_config_file_path)
    for i in range(len(instances)):
        instance = instances[i]
        instance_id = instance["InstanceId"]
        alias = f"{instance_name}_{i}" if i > 0 else instance_name

        entry = SSHConfigEntry()

        entry["User"] = usernames[instance["ImageId"]]

        keypath = Path.home() / ".ssh" / f"{instance['KeyName']}.pem"
        entry["IdentityFile"] = keypath
        if not keypath.exists() and not keypath.is_file():
            warning_print(
                f"{instance_id} key file {keypath} is missing. Remeber to create it later."
            )
        entry["IdentitiesOnly"] = "yes"

        entry["HostName"] = instance["PublicDnsName"]

        if ssh_config.contains_host(alias):
            warning_print(
                f"ssh config already contains an entry for {alias}. Skipping."
            )
            print(entry)
        else:
            ssh_config.add_host(alias, entry)
    ssh_config.write(ssh_config_file_path)


def ec2_stop(instance_name: str) -> None:
    ec2 = boto3.client("ec2")
    resp = ec2.describe_instances(
        Filters=[{"Name": "tag:Name", "Values": [instance_name]}]
    )

    if not resp["Reservations"]:
        danger_print(f"There are no instances with name {instance_name}!")
        return

    instances = resp["Reservations"][0]["Instances"]
    if (n_instances := len(instances)) != 1:
        warning_print(f"There {n_instances} instances with name {instance_name}.")
        input("Press [ENTER] to stop all of them, CTRL-C to cancel.")

    instance_ids = [instance["InstanceId"] for instance in instances]
    states = [instance["State"] for instance in instances]
    not_running_instances = filter(
        lambda ins_state: ins_state[1]["Code"] != 16, zip(instance_ids, states)
    )
    for not_running_instance in not_running_instances:
        warning_print(
            f"{not_running_instance[0]} is in {not_running_instance[1]['Name']} state."
        )

    info_print("Stopping instances.")
    ec2.stop_instances(InstanceIds=instance_ids)

    try:
        waiter = ec2.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=instance_ids)
    except WaiterError as werr:
        danger_print("Unable to start instances!")
        print(werr)
        return

    resp = ec2.describe_instances(InstanceIds=instance_ids)

    if not resp["Reservations"]:
        danger_print("Something went wrong. Did not get any instances this time!")
        return

    instances = resp["Reservations"][0]["Instances"]
    if len(instances) != n_instances:
        danger_print(
            f"Something went wrong. Got {len(instances)} this time instead of {n_instances} last time!"
        )
        return

    states = [instance["State"] for instance in instances]
    if any(map(lambda s: s["Code"] != 80, states)):
        danger_print("Not all instances have stopped!")
        return

    info_print("Removing entry from ssh config.")
    ssh_config_file_path = Path.home() / ".ssh" / "config"
    if not ssh_config_file_path.exists():
        return
    ssh_config = SSHConfig.read(ssh_config_file_path)
    for i in range(len(instances)):
        alias = f"{instance_name}_{i}" if i > 0 else instance_name
        if ssh_config.contains_host(alias):
            ssh_config.remove_host(alias)
    ssh_config.write(ssh_config_file_path)


ResourceType = str
TaskType = str
TaskFunc = Callable[..., None]


class Tasks:
    def __init__(self):
        self._tasks: dict[ResourceType, dict[TaskType, TaskFunc]] = defaultdict(dict)

    def __setitem__(self, key: tuple[ResourceType, TaskType], value: TaskFunc) -> None:
        resource, task = key
        if task in self._tasks[resource]:
            raise KeyError(f"{task} already set for {resource}!")
        self._tasks[resource][task] = value

    def __getitem__(self, key: tuple[ResourceType, TaskType]) -> TaskFunc:
        return self._tasks[key[0]][key[1]]


pass_tasks = click.make_pass_decorator(Tasks)


@click.group()
@click.version_option("0.0.2")
@click.pass_context
def main(ctx):
    """
    Augmentation to available public cloud CLIs when they are missing some functionality.
    """
    ctx.obj = Tasks()
    ctx.obj["ec2", "start"] = ec2_start
    ctx.obj["ec2", "stop"] = ec2_stop


@main.command()
@click.option(
    "--instance-name",
    type=str,
    required=True,
    help="The friendly name of the EC2 instance.",
)
@click.argument("task", type=str)
@pass_tasks
def ec2(tasks, instance_name: str, task: str) -> None:
    """
    \b
    Tools to manage AWS EC2 instances.
    Can do the following tasks:
      * start
      * stop
    """
    try:
        tasks["ec2", task](instance_name)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
