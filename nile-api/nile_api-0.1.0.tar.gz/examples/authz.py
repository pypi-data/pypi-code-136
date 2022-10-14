from pathlib import Path
import os
import json
import sys

from nile_api import AuthenticatedClient, Client
from nile_api.api.access import (
    create_policy, delete_policy, list_policies,
)
from nile_api.api.developers import login_developer
from nile_api.api.organizations import list_organizations
from nile_api.models.login_info import LoginInfo
from nile_api.models.create_policy_request import CreatePolicyRequest
from nile_api.models.action import Action
from nile_api.models.resource import Resource
from nile_api.models.subject import Subject


required_params = [
    "NILE_URL",
    "NILE_WORKSPACE",
    "NILE_DEVELOPER_EMAIL",
    "NILE_DEVELOPER_PASSWORD",
    "NILE_ORGANIZATION_NAME",
    "NILE_ENTITY_NAME"
    ]
for param in required_params:
    if not os.environ.get(param):
        sys.exit("Error: missing environment variable {}. See .env.defaults for more info and copy it to .env with your values".format(param))

NILE_URL = os.environ.get('NILE_URL')
NILE_WORKSPACE = os.environ.get('NILE_WORKSPACE')
NILE_DEVELOPER_EMAIL = os.environ.get('NILE_DEVELOPER_EMAIL')
NILE_DEVELOPER_PASSWORD = os.environ.get('NILE_DEVELOPER_PASSWORD')
NILE_ORGANIZATION_NAME = os.environ.get('NILE_ORGANIZATION_NAME')
NILE_ENTITY_NAME = os.environ.get('NILE_ENTITY_NAME')

f = Path(__file__).parent / 'users.json'
usersJson = json.load(open(f))

# Load first user only
index = 0
NILE_TENANT1_EMAIL = usersJson[0]['email']
NILE_TENANT_PASSWORD = usersJson[0]['password']


token = login_developer.sync(
    client=Client(base_url=NILE_URL),
    info=LoginInfo(
        email=NILE_DEVELOPER_EMAIL,
        password=NILE_DEVELOPER_PASSWORD,
    ),
)

client = AuthenticatedClient(base_url=NILE_URL, token=token.token)

organizations = list_organizations.sync(
    workspace=NILE_WORKSPACE,
    client=client,
)
org_id = next(
    organization.id
    for organization in organizations
    if organization.name == NILE_ORGANIZATION_NAME
)
print(f"Mapped organization name {NILE_ORGANIZATION_NAME} to ID {org_id}")


print("\nPolicies at start:")
policies_start = list_policies.sync(
    client=client,
    workspace=NILE_WORKSPACE,
    org=org_id,
)
print([each.name for each in policies_start])

# Create a new policy
data = CreatePolicyRequest(
    actions=[Action.DENY],
    resource=Resource(type=NILE_ENTITY_NAME),
    subject=Subject(email=NILE_TENANT1_EMAIL),
    )
print(f"\nCreating new policy {data}.")
policy = create_policy.sync(
    client=client,
    workspace=NILE_WORKSPACE,
    org=org_id,
    json_body=data,
)
print(policy)

print("\nPolicies post-create:")
print(list_policies.sync(client=client, workspace=NILE_WORKSPACE, org=org_id))

# Delete the policy just created
response = delete_policy.sync_detailed(
    client=client,
    workspace=NILE_WORKSPACE,
    org=org_id,
    policy_id=policy.id,
)
print("policy id {} is deleted".format(policy.id))

print("\nPolicies post-delete:")
policies_end = list_policies.sync(
    client=client,
    workspace=NILE_WORKSPACE,
    org=org_id,
)
print([each.name for each in policies_end])

if policies_start != policies_end:
    print("Something is wrong, policies at start should equal policies at end")
    sys.exit(1)
