from dataclasses import dataclass

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class ClientSideEncryptionConfig:
    """Parameters to use for client side encryption.

    The following client side encryptions are supported:

        * :mod:`atoti-aws <atoti_aws>` plugin:

            * :class:`atoti_aws.AwsKeyPair`.
            * :class:`atoti_aws.AwsKmsConfig`.

        * :mod:`atoti-azure <atoti_azure>` plugin :

            * :class:`atoti_azure.AzureKeyPair`.

    """
