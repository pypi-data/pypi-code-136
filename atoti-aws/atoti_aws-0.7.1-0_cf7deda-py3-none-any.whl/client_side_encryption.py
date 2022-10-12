from dataclasses import dataclass

from atoti_core import keyword_only_dataclass

import atoti as tt


@keyword_only_dataclass
@dataclass(frozen=True)
class _AwsClientSideEncryption:
    region: str
    """The AWS region to interact with."""


@keyword_only_dataclass
@dataclass(frozen=True)
class AwsKmsConfig(_AwsClientSideEncryption, tt.ClientSideEncryptionConfig):
    """KMS configuration to use for `client side encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__.

    The AWS KMS CMK must have been created in the same AWS region as the destination bucket (Cf. `AWS documentation <https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-config-for-kms-objects.html>`__).

    Example:

        >>> from atoti_aws import AwsKmsConfig
        >>> client_side_encryption_config = (
        ...     AwsKmsConfig(
        ...         region="eu-west-3",
        ...         key_id="key_id",
        ...     ),
        ... )
    """

    key_id: str
    """The ID to identify the key in KMS."""


@keyword_only_dataclass
@dataclass(frozen=True)
class AwsKeyPair(tt.KeyPair, _AwsClientSideEncryption, tt.ClientSideEncryptionConfig):
    """Key pair to use for `client side encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__.

    Example:

        >>> from atoti_aws import AwsKeyPair
        >>> client_side_encryption_config = (
        ...     AwsKeyPair(
        ...         region="eu-west-3",
        ...         private_key="private_key",
        ...         public_key="public_key",
        ...     ),
        ... )
    """
