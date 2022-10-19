'''
# replace this
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

__all__ = [
    "athena",
    "ec2",
    "glue",
    "glue_tables",
    "kinesis_firehose",
    "ram",
    "s3_buckets",
    "sso",
    "stacks",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import athena
from . import ec2
from . import glue
from . import glue_tables
from . import kinesis_firehose
from . import ram
from . import s3_buckets
from . import sso
from . import stacks
