'''
<div align="center">
	<br/>
	<br/>
  <h1>
	<img height="140" src="assets/alma-cdk-domain.svg" alt="Alma CDK Domain" />
  <br/>
  <br/>
  </h1>

```sh
npm i -D @alma-cdk/domain
```

  <div align="left">

Simplifies creation of subdomain with a TLS certificate and configuration with services like AWS CloudFront.

  </div>
  <br/>
</div><br/>

## 🚧   Project Stability

![experimental](https://img.shields.io/badge/stability-experimental-yellow)

This construct is still versioned with `v0` major version and breaking changes might be introduced if necessary (without a major version bump), though we aim to keep the API as stable as possible (even within `v0` development). We aim to publish `v1.0.0` soon and after that breaking changes will be introduced via major version bumps.

<br/>

## Getting Started

```python
import { Domain } from '@alma-cdk/domain';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
```

```python
const domain = new Domain(this, 'Domain', {
  zone: 'example.com', // retrieve the zone via lookup, or provide IHostedZone
  subdomain: 'foobar', // optional subdomain
});

const distribution = new cloudfront.Distribution(this, 'Distribution', {
  /* other cloudfront configuration values removed for brevity */

  certificate: domain.certificate, // reference to created ICertificate
  domainNames: [domain.fqdn], // foobar.example.com
  enableIpv6: domain.enableIpv6, // true by default – set enableIpv6 prop to false during new Domain()
})

// assign CloudFront distribution to given fqdn with A + AAAA records
domain.addTarget(new targets.CloudFrontTarget(distribution))
```

<br/>

### CloudFront helper

Instead of assigning `certificate`, `domainNames` and `enableIpv6` properties individually, you may choose to use the one-liner helper utility method `configureCloudFront()` to set all three values at once – don't forget to use `...` object spread syntax:

```python
const distribution = new cloudfront.Distribution(this, 'Distribution', {
  /* other cloudfront configuration values removed for brevity */

  // one-liner to configure certificate, domainNames and IPv6 support
  ...domain.configureCloudFront(),
})

// assign CloudFront distribution to given fqdn with A + AAAA records
domain.addTarget(new targets.CloudFrontTarget(distribution))
```

Note: The returned domain names configuration is `domainNames: [domain.fqdn]`, meaning this only works in scenarios where your CloudFront distribution has only single domain name.
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

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_route53
import constructs


@jsii.data_type(
    jsii_type="@alma-cdk/domain.DomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "zone": "zone",
        "certificate": "certificate",
        "enable_ipv6": "enableIpv6",
        "region": "region",
        "subdomain": "subdomain",
    },
)
class DomainProps:
    def __init__(
        self,
        *,
        zone: typing.Union[builtins.str, aws_cdk.aws_route53.IHostedZone],
        certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties to configure the domain (zone and certificate).

        :param zone: (experimental) Provide either a fully-qualified domain name as string to perform a hosted zone lookup or a previously defined hosted zone as ``route53.IHostedZone``.
        :param certificate: (experimental) Provide your own pre-existing certificate. If not provided, a new certificate will be created by default.
        :param enable_ipv6: (experimental) Set to false to disable IPv6 ``AAAA`` record creation. Default: true
        :param region: (experimental) AWS Region to deploy the certificate into. Defaults to ``us-east-1`` which is the only region where ACM certificates can be deployed to CloudFront. Default: "us-east-1"
        :param subdomain: (experimental) Provide subdomain or leave undefined to use the zone apex domain. If subdomain provided, the resulting FQDN will be ``subdomain.zone``.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DomainProps.__init__)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument enable_ipv6", value=enable_ipv6, expected_type=type_hints["enable_ipv6"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument subdomain", value=subdomain, expected_type=type_hints["subdomain"])
        self._values: typing.Dict[str, typing.Any] = {
            "zone": zone,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if enable_ipv6 is not None:
            self._values["enable_ipv6"] = enable_ipv6
        if region is not None:
            self._values["region"] = region
        if subdomain is not None:
            self._values["subdomain"] = subdomain

    @builtins.property
    def zone(self) -> typing.Union[builtins.str, aws_cdk.aws_route53.IHostedZone]:
        '''(experimental) Provide either a fully-qualified domain name as string to perform a hosted zone lookup or a previously defined hosted zone as ``route53.IHostedZone``.

        :stability: experimental
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(typing.Union[builtins.str, aws_cdk.aws_route53.IHostedZone], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        '''(experimental) Provide your own pre-existing certificate.

        If not provided, a new certificate will be created
        by default.

        :stability: experimental
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[aws_cdk.aws_certificatemanager.ICertificate], result)

    @builtins.property
    def enable_ipv6(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Set to false to disable IPv6 ``AAAA`` record creation.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("enable_ipv6")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''(experimental) AWS Region to deploy the certificate into.

        Defaults to ``us-east-1`` which is the only region where
        ACM certificates can be deployed to CloudFront.

        :default: "us-east-1"

        :stability: experimental
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdomain(self) -> typing.Optional[builtins.str]:
        '''(experimental) Provide subdomain or leave undefined to use the zone apex domain.

        If subdomain provided, the resulting FQDN will be ``subdomain.zone``.

        :stability: experimental
        '''
        result = self._values.get("subdomain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@alma-cdk/domain.ICloudFrontConfiguration")
class ICloudFrontConfiguration(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) Certificate Manager certificate.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="domainNames")
    def domain_names(self) -> typing.List[builtins.str]:
        '''(experimental) Alternative domain names for this distribution.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="enableIpv6")
    def enable_ipv6(self) -> builtins.bool:
        '''(experimental) Has IPv6 AAAA records been created.

        Can be used to conditionally configure IPv6 support
        to CloudFront distribution.

        :stability: experimental
        '''
        ...


class _ICloudFrontConfigurationProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/domain.ICloudFrontConfiguration"

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) Certificate Manager certificate.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_certificatemanager.ICertificate, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="domainNames")
    def domain_names(self) -> typing.List[builtins.str]:
        '''(experimental) Alternative domain names for this distribution.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domainNames"))

    @builtins.property
    @jsii.member(jsii_name="enableIpv6")
    def enable_ipv6(self) -> builtins.bool:
        '''(experimental) Has IPv6 AAAA records been created.

        Can be used to conditionally configure IPv6 support
        to CloudFront distribution.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "enableIpv6"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudFrontConfiguration).__jsii_proxy_class__ = lambda : _ICloudFrontConfigurationProxy


@jsii.interface(jsii_type="@alma-cdk/domain.IDomain")
class IDomain(typing_extensions.Protocol):
    '''(experimental) Interface contract implemented by Domain construct.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) Certificate Manager certificate.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="enableIpv6")
    def enable_ipv6(self) -> builtins.bool:
        '''(experimental) Has IPv6 AAAA records been created.

        Can be used to conditionally configure IPv6 support
        to CloudFront distribution.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        '''(experimental) Fully-qualified domain name.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        '''(experimental) Route53 hosted zone used to assign the domain into.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addTarget")
    def add_target(self, alias: aws_cdk.aws_route53.IAliasRecordTarget) -> None:
        '''(experimental) Assign an alias as record target with the fully-qualified domain name.

        This will create both ``A`` & ``AAAA`` DNS records, unless ``disableIpV6`` was set to ``true``
        during initialization of ``Domain`` construct (resulting in only ``A`` record being created).

        :param alias: Route53 alias record target used to assign as A/AAAA record value.

        :stability: experimental

        Example::

            domain.addTarget(new targets.CloudFrontTarget(distribution))
        '''
        ...


class _IDomainProxy:
    '''(experimental) Interface contract implemented by Domain construct.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@alma-cdk/domain.IDomain"

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) Certificate Manager certificate.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_certificatemanager.ICertificate, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="enableIpv6")
    def enable_ipv6(self) -> builtins.bool:
        '''(experimental) Has IPv6 AAAA records been created.

        Can be used to conditionally configure IPv6 support
        to CloudFront distribution.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "enableIpv6"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        '''(experimental) Fully-qualified domain name.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        '''(experimental) Route53 hosted zone used to assign the domain into.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_route53.IHostedZone, jsii.get(self, "zone"))

    @jsii.member(jsii_name="addTarget")
    def add_target(self, alias: aws_cdk.aws_route53.IAliasRecordTarget) -> None:
        '''(experimental) Assign an alias as record target with the fully-qualified domain name.

        This will create both ``A`` & ``AAAA`` DNS records, unless ``disableIpV6`` was set to ``true``
        during initialization of ``Domain`` construct (resulting in only ``A`` record being created).

        :param alias: Route53 alias record target used to assign as A/AAAA record value.

        :stability: experimental

        Example::

            domain.addTarget(new targets.CloudFrontTarget(distribution))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IDomain.add_target)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
        return typing.cast(None, jsii.invoke(self, "addTarget", [alias]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomain).__jsii_proxy_class__ = lambda : _IDomainProxy


@jsii.implements(IDomain)
class Domain(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@alma-cdk/domain.Domain",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        zone: typing.Union[builtins.str, aws_cdk.aws_route53.IHostedZone],
        certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate] = None,
        enable_ipv6: typing.Optional[builtins.bool] = None,
        region: typing.Optional[builtins.str] = None,
        subdomain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Initializing a ``new Domain`` construct instance will lookup the Route53 hosted zone and define ACM DNS-validated certificate.

        After initialization you must use ``assign(alias)`` method to to configure ``A``/``AAAA`` records
        with the ``alias`` as the record value.

        :param scope: -
        :param id: -
        :param zone: (experimental) Provide either a fully-qualified domain name as string to perform a hosted zone lookup or a previously defined hosted zone as ``route53.IHostedZone``.
        :param certificate: (experimental) Provide your own pre-existing certificate. If not provided, a new certificate will be created by default.
        :param enable_ipv6: (experimental) Set to false to disable IPv6 ``AAAA`` record creation. Default: true
        :param region: (experimental) AWS Region to deploy the certificate into. Defaults to ``us-east-1`` which is the only region where ACM certificates can be deployed to CloudFront. Default: "us-east-1"
        :param subdomain: (experimental) Provide subdomain or leave undefined to use the zone apex domain. If subdomain provided, the resulting FQDN will be ``subdomain.zone``.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Domain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DomainProps(
            zone=zone,
            certificate=certificate,
            enable_ipv6=enable_ipv6,
            region=region,
            subdomain=subdomain,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addTarget")
    def add_target(self, alias: aws_cdk.aws_route53.IAliasRecordTarget) -> None:
        '''(experimental) Assign an alias as record target with the fully-qualified domain name.

        This will create both ``A`` & ``AAAA`` DNS records, unless ``disableIpV6`` was set to ``true``
        during initialization of ``Domain`` construct (resulting in only ``A`` record being created).

        :param alias: Route53 alias record target used to assign as A/AAAA record value.

        :stability: experimental

        Example::

            domain.addTarget(new targets.CloudFrontTarget(distribution))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Domain.add_target)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
        return typing.cast(None, jsii.invoke(self, "addTarget", [alias]))

    @jsii.member(jsii_name="configureCloudFront")
    def configure_cloud_front(self) -> ICloudFrontConfiguration:
        '''(experimental) Helper method to configure CloudFront distribution with the domain, certificate and IPv6 support.

        :return: CloudFront configuration for certificate, domainNames and IPv6

        :stability: experimental
        '''
        return typing.cast(ICloudFrontConfiguration, jsii.invoke(self, "configureCloudFront", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> aws_cdk.aws_certificatemanager.ICertificate:
        '''(experimental) Certificate Manager certificate.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_certificatemanager.ICertificate, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="enableIpv6")
    def enable_ipv6(self) -> builtins.bool:
        '''(experimental) Has IPv6 AAAA records been created.

        Can be used to conditionally configure IPv6 support
        to CloudFront distribution.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "enableIpv6"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        '''(experimental) Fully-qualified domain name.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        '''(experimental) Route53 hosted zone used to assign the domain into.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_route53.IHostedZone, jsii.get(self, "zone"))


__all__ = [
    "Domain",
    "DomainProps",
    "ICloudFrontConfiguration",
    "IDomain",
]

publication.publish()
