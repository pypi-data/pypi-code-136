import difflib
import pprint
from typing import Any, Dict, List, Tuple

from click import ClickException

from anyscale.aws_iam_policies import (
    AMAZON_ECR_READONLY_ACCESS_POLICY_NAME,
    AMAZON_S3_FULL_ACCESS_POLICY_NAME,
    ANYSCALE_IAM_PERMISSIONS_EC2_INITIAL_RUN,
    ANYSCALE_IAM_PERMISSIONS_EC2_STEADY_STATE,
    ANYSCALE_IAM_POLICY_NAME_INITIAL_RUN,
    ANYSCALE_IAM_POLICY_NAME_STEADY_STATE,
    get_anyscale_aws_iam_assume_role_policy,
)
from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.models.create_cloud_resource import (
    CreateCloudResource,
)
from anyscale.conf import ANYSCALE_IAM_ROLE_NAME
from anyscale.util import (  # pylint:disable=private-import
    _get_role,
    _get_subnet,
    get_availability_zones,
)


# This needs to be kept in sync with the Ray autoscaler in
# https://github.com/ray-project/ray/blob/eb9c5d8fa70b1c360b821f82c7697e39ef94b25e/python/ray/autoscaler/_private/aws/config.py
# It should go away with the SSM refactor.
DEFAULT_RAY_IAM_ROLE = "ray-autoscaler-v1"


AWS_VPC_CIDR_BLOCK_MASK_MAX = 16
AWS_SUBNET_CIDR_BLOCK_MASK_MAX = 20


def compare_dicts_diff(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> str:
    """Returns a string representation of the difference of the two dictionaries.
    Example:

    Input:
    print(compare_dicts_diff({"a": {"c": 1}, "b": 2}, {"a": {"c": 2}, "d": 3}))

    Output:
    - {'a': {'c': 1}, 'b': 2}
    ?             ^    ^   ^

    + {'a': {'c': 2}, 'd': 3}
    ?             ^    ^   ^
    """

    return "\n" + "\n".join(
        difflib.ndiff(pprint.pformat(d1).splitlines(), pprint.pformat(d2).splitlines())
    )


def verify_aws_vpc(
    cloud_resource: CreateCloudResource, boto3_session: Any, logger: BlockLogger
) -> bool:
    logger.info("Verifying VPC ...")
    if not cloud_resource.aws_vpc_id:
        logger.error("Missing VPC id.")
        return False

    ec2 = boto3_session.resource("ec2")
    vpc = ec2.Vpc(cloud_resource.aws_vpc_id)
    if not vpc:
        logger.error(f"VPC with id {cloud_resource.aws_vpc_id} does not exist.")
        return False

    cidr_block = vpc.cidr_block
    if int(cidr_block.split("/")[-1]) > AWS_VPC_CIDR_BLOCK_MASK_MAX:
        logger.error(
            f"The cidr block range is too small for vpc with id {cloud_resource.aws_vpc_id}."
        )
        return False

    logger.info(f"VPC {cloud_resource.aws_vpc_id} verification succeeded.")
    return True


def _get_subnets_from_subnet_ids(subnet_ids: List[str], region: str) -> List[Any]:
    return [
        _get_subnet(subnet_arn=subnet_id, region=region) for subnet_id in subnet_ids
    ]


def verify_aws_subnets(
    cloud_resource: CreateCloudResource, region: str, logger: BlockLogger
) -> Tuple[bool, CreateCloudResource]:
    logger.info("Verifying subnets ...")
    if not cloud_resource.aws_subnet_ids:
        logger.error("Missing subnet IDs.")
        return False, None

    subnets = _get_subnets_from_subnet_ids(
        subnet_ids=cloud_resource.aws_subnet_ids, region=region
    )

    for subnet, subnet_id in zip(subnets, cloud_resource.aws_subnet_ids):
        if not subnet:
            logger.error(f"Subnet with id {subnet_id} does not exist.")
            return False, None

        cidr_block = subnet.cidr_block
        if int(cidr_block.split("/")[-1]) > AWS_SUBNET_CIDR_BLOCK_MASK_MAX:
            logger.error(
                f"The cidr block range is too small for subnet with id {subnet_id}."
            )
            return False, None

        if cloud_resource.aws_vpc_id and subnet.vpc_id != cloud_resource.aws_vpc_id:
            logger.error(
                f"The subnet {subnet_id} is not in a vpc of this cloud. The vpc of this subnet is {subnet.vpc_id} and the vpc of this cloud is {cloud_resource.aws_vpc_id}."
            )
            return False, None

    # verify that each availablity zone has a subnet
    subnet_availability_zones = set(subnet.availability_zone for subnet in subnets)
    availability_zones = get_availability_zones(region=region)
    availability_zones_without_subnet = [
        az for az in availability_zones if az not in subnet_availability_zones
    ]
    if availability_zones_without_subnet:
        logger.error(
            f"{region} has availability zones: {availability_zones}. Anyscale requires a subnet in every availability zone. Please provide a subnet for each of the following availability zones: {availability_zones_without_subnet}"
        )
        return False, None
    reordered_subnet_ids = [
        subnet.id
        for subnet in sorted(subnets, key=lambda subnet: subnet.availability_zone)
    ]
    cloud_resource.aws_subnet_ids = reordered_subnet_ids

    logger.info(f"Subnets {cloud_resource.aws_subnet_ids} verification succeeded.")
    return True, cloud_resource


def get_role_name_from_role_arn(role_arn: str) -> str:
    try:
        return role_arn.split("/")[1]
    except Exception:
        raise ClickException(f"Invalid role arn provided. {role_arn}")


def _get_roles_from_role_names(names: List[str], region: str) -> List[Any]:
    return [
        _get_role(role_name=iam_role_name, region=region) for iam_role_name in names
    ]


def verify_aws_iam_roles(
    cloud_resource: CreateCloudResource,
    region: str,
    anyscale_aws_account: str,
    logger: BlockLogger,
) -> bool:
    logger.info("Verifying IAM roles ...")
    if not cloud_resource.aws_iam_role_arns:
        logger.error("Missing IAM role arns.")
        return False

    role_names = [
        get_role_name_from_role_arn(arn) for arn in cloud_resource.aws_iam_role_arns
    ]

    roles = _get_roles_from_role_names(names=role_names, region=region)
    if not any((ANYSCALE_IAM_ROLE_NAME in role.role_name for role in roles)):
        logger.error(
            "IAM roles of this cloud resource do not contain anyscale iam role."
        )
        return False
    if not any((DEFAULT_RAY_IAM_ROLE in role.role_name for role in roles)):
        logger.error("IAM roles of this cloud resource do not contain ray iam role.")
        return False

    for role in roles:
        if not role:
            logger.error(f"IAM role with arn {role.arn} does not exist.")
            return False

        if ANYSCALE_IAM_ROLE_NAME in role.role_name:
            assume_role_policy_document = role.assume_role_policy_document
            # not verifying the statement external id condition because cloud_id is not added before cloud creation
            if (
                "Statement" in assume_role_policy_document
                and len(assume_role_policy_document["Statement"]) > 0
                and "Condition" in assume_role_policy_document["Statement"][0]
            ):
                del assume_role_policy_document["Statement"][0]["Condition"]
            expected_assume_role_policy_document = get_anyscale_aws_iam_assume_role_policy(
                anyscale_aws_account=anyscale_aws_account
            )
            if assume_role_policy_document != expected_assume_role_policy_document:
                logger.error(
                    f"Anyscale IAM role {role.arn} does not contain expected assume role policy."
                )
                logger.error(
                    compare_dicts_diff(
                        assume_role_policy_document,
                        expected_assume_role_policy_document,
                    )
                )
                return False

            for policy in role.policies.all():
                if policy.policy_name == ANYSCALE_IAM_POLICY_NAME_STEADY_STATE:
                    if (
                        policy.policy_document
                        != ANYSCALE_IAM_PERMISSIONS_EC2_STEADY_STATE
                    ):
                        logger.error(
                            f"IAM role {role.arn} policy verification failed for policy {ANYSCALE_IAM_POLICY_NAME_STEADY_STATE}."
                        )
                        logger.error(
                            compare_dicts_diff(
                                policy.policy_document,
                                ANYSCALE_IAM_PERMISSIONS_EC2_STEADY_STATE,
                            )
                        )
                        return False
                elif policy.policy_name == ANYSCALE_IAM_POLICY_NAME_INITIAL_RUN:
                    if (
                        policy.policy_document
                        != ANYSCALE_IAM_PERMISSIONS_EC2_INITIAL_RUN
                    ):
                        logger.error(
                            f"IAM role {role.arn} policy verification failed for policy {ANYSCALE_IAM_POLICY_NAME_INITIAL_RUN}."
                        )
                        logger.error(
                            compare_dicts_diff(
                                policy.policy_document,
                                ANYSCALE_IAM_PERMISSIONS_EC2_INITIAL_RUN,
                            )
                        )
                        return False
                else:
                    logger.info(
                        f"Unknown policy {policy.policy_name} for IAM role {role.arn}. Skipping policies verification."
                    )
        elif DEFAULT_RAY_IAM_ROLE in role.role_name:
            policy_names = [
                policy.policy_name for policy in role.attached_policies.all()
            ]
            if AMAZON_ECR_READONLY_ACCESS_POLICY_NAME not in policy_names:
                logger.error(
                    f"Ray role {role.arn} must contain policy {AMAZON_ECR_READONLY_ACCESS_POLICY_NAME}."
                )
                return False
            if AMAZON_S3_FULL_ACCESS_POLICY_NAME not in policy_names:
                logger.error(
                    f"Ray role {role.arn} must contain policy {AMAZON_S3_FULL_ACCESS_POLICY_NAME}."
                )
                return False
        else:
            logger.info(f"Unknown role {role.arn}. Skipping policies verification.")

    logger.info(f"IAM roles {cloud_resource.aws_iam_role_arns} verification succeeded.")
    return True


def verify_aws_security_groups(
    cloud_resource: CreateCloudResource, boto3_session: Any, logger: BlockLogger
) -> bool:
    logger.info("Verifying security groups ...")
    if not cloud_resource.aws_security_groups:
        logger.error("Missing security group IDs.")
        return False

    ec2 = boto3_session.resource("ec2")
    # Now we only have one security group defining inbound rules.
    anyscale_security_group_arn = cloud_resource.aws_security_groups[0]
    anyscale_security_group = ec2.SecurityGroup(anyscale_security_group_arn)
    if not anyscale_security_group:
        logger.error(
            f"Security group with id {anyscale_security_group_arn} does not exist."
        )
        return False
    inbound_ip_permissions = anyscale_security_group.ip_permissions
    # 443 is for HTTPS ingress
    # 22 is for SSH
    expected_open_ports = [443, 22]

    inbound_ip_permissions_with_specific_port = [
        ip_permission["FromPort"]
        for ip_permission in inbound_ip_permissions
        if "FromPort" in ip_permission
    ]
    inbound_sg_rule_with_self = []
    for sg_rule in inbound_ip_permissions:
        if sg_rule.get("IpProtocol") == "-1":
            inbound_sg_rule_with_self.extend(sg_rule.get("UserIdGroupPairs"))

    for port in expected_open_ports:
        if not any(
            (
                inbound_ip_permission_port == port
                for inbound_ip_permission_port in inbound_ip_permissions_with_specific_port
            )
        ):
            logger.error(
                f"Security group with id {anyscale_security_group_arn} does not contain inbound permission for port {port}."
            )
            return False

    if not any(
        sg_rule.get("GroupId") == anyscale_security_group_arn
        for sg_rule in inbound_sg_rule_with_self
    ):
        logger.error(
            f"Security group with id {anyscale_security_group_arn} does not contain inbound permission for all ports for traffic from the same security group."
        )
        return False

    if len(inbound_ip_permissions_with_specific_port) > len(expected_open_ports):
        logger.error(
            f"Security group with id {anyscale_security_group_arn} has too many inbound ip permissions. We are only expecting {expected_open_ports} to be open."
        )
        return False

    logger.info(
        f"Security group {cloud_resource.aws_security_groups} verification succeeded."
    )
    return True


def verify_aws_s3(
    cloud_resource: CreateCloudResource, boto3_session: Any, logger: BlockLogger
) -> bool:
    logger.info("Verifying S3 ...")
    if not cloud_resource.aws_s3_id:
        logger.error("Missing S3 ID.")
        return False

    s3 = boto3_session.resource("s3")
    bucket_name = cloud_resource.aws_s3_id.split(":")[-1]
    s3_bucket = s3.Bucket(bucket_name)
    if not s3_bucket:
        logger.error(f"S3 object with id {cloud_resource.aws_s3_id} does not exist.")
        return False

    logger.info(f"S3 {cloud_resource.aws_s3_id} verification succeeded.")
    return True


def verify_aws_efs(
    cloud_resource: CreateCloudResource, boto3_session: Any, logger: BlockLogger
) -> bool:
    logger.info("Verifying EFS ...")
    if not cloud_resource.aws_efs_id:
        logger.error("Missing EFS ID.")
        return False

    client = boto3_session.client("efs")
    response = client.describe_file_systems(FileSystemId=cloud_resource.aws_efs_id)
    if not response["FileSystems"]:
        logger.error(f"EFS with id {cloud_resource.aws_efs_id} does not exist.")
        return False

    logger.info(f"S3 {cloud_resource.aws_efs_id} verification succeeded.")
    return True


def verify_aws_cloudformation_stack(
    cloud_resource: CreateCloudResource, boto3_session: Any, logger: BlockLogger
) -> bool:
    logger.info("Verifying CloudFormation stack ...")
    if not cloud_resource.aws_cloudformation_stack_id:
        logger.error("Missing CloudFormation stack id.")
        return False

    cloudformation = boto3_session.resource("cloudformation")
    stack = cloudformation.Stack(cloud_resource.aws_cloudformation_stack_id)
    if not stack:
        logger.error(
            f"CloudFormation stack with id {cloud_resource.aws_cloudformation_stack_id} does not exist."
        )
        return False

    logger.info(
        f"CloudFormation stack {cloud_resource.aws_cloudformation_stack_id} verification succeeded."
    )
    return True
