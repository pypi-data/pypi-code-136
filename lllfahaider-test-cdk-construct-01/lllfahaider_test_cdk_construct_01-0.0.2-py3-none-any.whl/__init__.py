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

import constructs


class S3Bucket(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="lllfahaider-test-cdk-construct-01.S3Bucket",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        read_access: builtins.bool,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param read_access: Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(S3Bucket.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = S3BucketProps(read_access=read_access)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="lllfahaider-test-cdk-construct-01.S3BucketProps",
    jsii_struct_bases=[],
    name_mapping={"read_access": "readAccess"},
)
class S3BucketProps:
    def __init__(self, *, read_access: builtins.bool) -> None:
        '''
        :param read_access: Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(S3BucketProps.__init__)
            check_type(argname="argument read_access", value=read_access, expected_type=type_hints["read_access"])
        self._values: typing.Dict[str, typing.Any] = {
            "read_access": read_access,
        }

    @builtins.property
    def read_access(self) -> builtins.bool:
        '''
        :default: false

        :memberof: S3BucketProps
        :type: {boolean}
        '''
        result = self._values.get("read_access")
        assert result is not None, "Required property 'read_access' is missing"
        return typing.cast(builtins.bool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "S3Bucket",
    "S3BucketProps",
]

publication.publish()
