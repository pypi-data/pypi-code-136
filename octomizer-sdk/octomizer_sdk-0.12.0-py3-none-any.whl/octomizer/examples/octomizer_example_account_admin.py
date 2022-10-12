from datetime import datetime

from octomizer import client

ACCESS_TOKEN = "Token"
NEW_USER_FIRST = "First"
NEW_USER_LAST = "Last"
NEW_USER_EMAIL = "user@user.com"

client = client.OctomizerClient(access_token=ACCESS_TOKEN)
account_uuid = client.get_current_user().account_uuid

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# Add a new user.
new_user = client.add_user(
    given_name=NEW_USER_FIRST,
    family_name=NEW_USER_LAST,
    email=NEW_USER_EMAIL,
    account_uuid=account_uuid,
    is_own_account_admin=False,
    can_accelerate=True,
)
print(new_user)


# List users in your account.
users = client.list_users(account_uuid=account_uuid)
for user in users:
    print(user)


# Give an existing user admin permissions.
new_admin_user = client.update_user(
    user_uuid="some_uuid",  # you can find this uuid by listing users in your account.
    is_own_account_admin=True,
)
print(new_admin_user)


# Remove an existing user's permissions to accelerate.
non_accelerate_user = client.update_user(
    user_uuid="some_uuid",  # you can find this uuid by listing users in your account.
    can_accelerate=False,
)
print(non_accelerate_user)


# Deactivate an existing user.
deactivated_user = client.update_user(
    user_uuid="some_uuid",  # you can find this uuid by listing users in your account.
    active=False,
)
print(deactivated_user)

# Get usage data for the active user.
usageData = client.get_usage(
    start_time=datetime.min,  # defaults to the start of the current month.
    end_time=datetime.max,  # defaults to the end of the current month.
    account_uuid=account_uuid,
)
print(usageData)
