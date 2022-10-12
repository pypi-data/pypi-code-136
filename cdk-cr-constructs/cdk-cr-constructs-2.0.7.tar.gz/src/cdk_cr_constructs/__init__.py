'''
## `cdk-cr-constructs`

This Construct is collect custom resource

### Example for CustomResourceGetEIP

```python
import { App, Stack, CfnOutput, Duration, aws_iam } from 'aws-cdk-lib';
import { CustomResourceGetEIP } from 'cdk-cr-constructs';
const env = {
  region: process.env.CDK_DEFAULT_REGION,
  account: process.env.CDK_DEFAULT_ACCOUNT,
};
const app = new App();
const stack = new Stack(app, 'testing-stack', { env });
const getips = new CustomResourceGetEIP(stack, 'CustomResourceGetEIP', {
  /**
   * Discory us-east-1 Elastic Ips.
   */
  regions: ['us-east-1'],
  /**
   * Add Company Ips.
   */
  companyIps: ['1.2.3.4'],
});
const role = new aws_iam.Role(stack, 'DemoRole', {
  assumedBy: new aws_iam.AccountRootPrincipal(),
});
/**
 * Example create an assume role, allow all action from ip address.
*/
role.addToPolicy(new aws_iam.PolicyStatement({
  effect: aws_iam.Effect.ALLOW,
  resources: ['*'],
  actions: ['*'],
  conditions: {
    IpAddress: {
      'aws:SourceIp': this.getIps(),
    },
  },
}));
```
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

import aws_cdk
import constructs


class CustomResourceGetEIP(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-cr-constructs.CustomResourceGetEIP",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        props: typing.Optional["ICustomResourceGetEIPOptions"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CustomResourceGetEIP.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getips")
    def getips(self) -> typing.List[builtins.str]:
        '''
        :return: Token.asList(this.outputs.getAtt('IP_LIST'));

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "getips", []))

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(self) -> aws_cdk.CustomResource:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.CustomResource, jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(self, value: aws_cdk.CustomResource) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomResourceGetEIP, "outputs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputs", value)


@jsii.interface(jsii_type="cdk-cr-constructs.ICustomResourceGetEIPOptions")
class ICustomResourceGetEIPOptions(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="companyIps")
    def company_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        ...

    @company_ips.setter
    def company_ips(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        ...

    @regions.setter
    def regions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...


class _ICustomResourceGetEIPOptionsProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "cdk-cr-constructs.ICustomResourceGetEIPOptions"

    @builtins.property
    @jsii.member(jsii_name="companyIps")
    def company_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "companyIps"))

    @company_ips.setter
    def company_ips(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ICustomResourceGetEIPOptions, "company_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyIps", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ICustomResourceGetEIPOptions, "regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomResourceGetEIPOptions).__jsii_proxy_class__ = lambda : _ICustomResourceGetEIPOptionsProxy


__all__ = [
    "CustomResourceGetEIP",
    "ICustomResourceGetEIPOptions",
]

publication.publish()
