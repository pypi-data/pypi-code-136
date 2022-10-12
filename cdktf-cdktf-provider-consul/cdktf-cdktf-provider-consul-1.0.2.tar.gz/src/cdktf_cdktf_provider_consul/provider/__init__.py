'''
# `provider`

Refer to the Terraform Registory for docs: [`consul`](https://www.terraform.io/docs/providers/consul).
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

from .._jsii import *

import cdktf
import constructs


class ConsulProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.provider.ConsulProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul consul}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        address: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        ca_path: typing.Optional[builtins.str] = None,
        ca_pem: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        cert_pem: typing.Optional[builtins.str] = None,
        datacenter: typing.Optional[builtins.str] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsulProviderHeader", typing.Dict[str, typing.Any]]]]] = None,
        http_auth: typing.Optional[builtins.str] = None,
        insecure_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_file: typing.Optional[builtins.str] = None,
        key_pem: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul consul} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#address ConsulProvider#address}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#alias ConsulProvider#alias}
        :param ca_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_file ConsulProvider#ca_file}.
        :param ca_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_path ConsulProvider#ca_path}.
        :param ca_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_pem ConsulProvider#ca_pem}.
        :param cert_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#cert_file ConsulProvider#cert_file}.
        :param cert_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#cert_pem ConsulProvider#cert_pem}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#datacenter ConsulProvider#datacenter}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#header ConsulProvider#header}
        :param http_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#http_auth ConsulProvider#http_auth}.
        :param insecure_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#insecure_https ConsulProvider#insecure_https}.
        :param key_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#key_file ConsulProvider#key_file}.
        :param key_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#key_pem ConsulProvider#key_pem}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#namespace ConsulProvider#namespace}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#scheme ConsulProvider#scheme}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#token ConsulProvider#token}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ConsulProviderConfig(
            address=address,
            alias=alias,
            ca_file=ca_file,
            ca_path=ca_path,
            ca_pem=ca_pem,
            cert_file=cert_file,
            cert_pem=cert_pem,
            datacenter=datacenter,
            header=header,
            http_auth=http_auth,
            insecure_https=insecure_https,
            key_file=key_file,
            key_pem=key_pem,
            namespace=namespace,
            scheme=scheme,
            token=token,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetCaFile")
    def reset_ca_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaFile", []))

    @jsii.member(jsii_name="resetCaPath")
    def reset_ca_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaPath", []))

    @jsii.member(jsii_name="resetCaPem")
    def reset_ca_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaPem", []))

    @jsii.member(jsii_name="resetCertFile")
    def reset_cert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertFile", []))

    @jsii.member(jsii_name="resetCertPem")
    def reset_cert_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertPem", []))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetHttpAuth")
    def reset_http_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpAuth", []))

    @jsii.member(jsii_name="resetInsecureHttps")
    def reset_insecure_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureHttps", []))

    @jsii.member(jsii_name="resetKeyFile")
    def reset_key_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyFile", []))

    @jsii.member(jsii_name="resetKeyPem")
    def reset_key_pem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyPem", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="caFileInput")
    def ca_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caFileInput"))

    @builtins.property
    @jsii.member(jsii_name="caPathInput")
    def ca_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPathInput"))

    @builtins.property
    @jsii.member(jsii_name="caPemInput")
    def ca_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPemInput"))

    @builtins.property
    @jsii.member(jsii_name="certFileInput")
    def cert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certFileInput"))

    @builtins.property
    @jsii.member(jsii_name="certPemInput")
    def cert_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certPemInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="httpAuthInput")
    def http_auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureHttpsInput")
    def insecure_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyFileInput")
    def key_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyFileInput"))

    @builtins.property
    @jsii.member(jsii_name="keyPemInput")
    def key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "address"))

    @address.setter
    def address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="caFile")
    def ca_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caFile"))

    @ca_file.setter
    def ca_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "ca_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caFile", value)

    @builtins.property
    @jsii.member(jsii_name="caPath")
    def ca_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPath"))

    @ca_path.setter
    def ca_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "ca_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caPath", value)

    @builtins.property
    @jsii.member(jsii_name="caPem")
    def ca_pem(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caPem"))

    @ca_pem.setter
    def ca_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "ca_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caPem", value)

    @builtins.property
    @jsii.member(jsii_name="certFile")
    def cert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certFile"))

    @cert_file.setter
    def cert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "cert_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certFile", value)

    @builtins.property
    @jsii.member(jsii_name="certPem")
    def cert_pem(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certPem"))

    @cert_pem.setter
    def cert_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "cert_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certPem", value)

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]], jsii.get(self, "header"))

    @header.setter
    def header(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="httpAuth")
    def http_auth(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpAuth"))

    @http_auth.setter
    def http_auth(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "http_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpAuth", value)

    @builtins.property
    @jsii.member(jsii_name="insecureHttps")
    def insecure_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureHttps"))

    @insecure_https.setter
    def insecure_https(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "insecure_https").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureHttps", value)

    @builtins.property
    @jsii.member(jsii_name="keyFile")
    def key_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyFile"))

    @key_file.setter
    def key_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "key_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyFile", value)

    @builtins.property
    @jsii.member(jsii_name="keyPem")
    def key_pem(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPem"))

    @key_pem.setter
    def key_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "key_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPem", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "token"))

    @token.setter
    def token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ConsulProvider, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.provider.ConsulProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "alias": "alias",
        "ca_file": "caFile",
        "ca_path": "caPath",
        "ca_pem": "caPem",
        "cert_file": "certFile",
        "cert_pem": "certPem",
        "datacenter": "datacenter",
        "header": "header",
        "http_auth": "httpAuth",
        "insecure_https": "insecureHttps",
        "key_file": "keyFile",
        "key_pem": "keyPem",
        "namespace": "namespace",
        "scheme": "scheme",
        "token": "token",
    },
)
class ConsulProviderConfig:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        ca_file: typing.Optional[builtins.str] = None,
        ca_path: typing.Optional[builtins.str] = None,
        ca_pem: typing.Optional[builtins.str] = None,
        cert_file: typing.Optional[builtins.str] = None,
        cert_pem: typing.Optional[builtins.str] = None,
        datacenter: typing.Optional[builtins.str] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ConsulProviderHeader", typing.Dict[str, typing.Any]]]]] = None,
        http_auth: typing.Optional[builtins.str] = None,
        insecure_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_file: typing.Optional[builtins.str] = None,
        key_pem: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#address ConsulProvider#address}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#alias ConsulProvider#alias}
        :param ca_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_file ConsulProvider#ca_file}.
        :param ca_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_path ConsulProvider#ca_path}.
        :param ca_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_pem ConsulProvider#ca_pem}.
        :param cert_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#cert_file ConsulProvider#cert_file}.
        :param cert_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#cert_pem ConsulProvider#cert_pem}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#datacenter ConsulProvider#datacenter}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#header ConsulProvider#header}
        :param http_auth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#http_auth ConsulProvider#http_auth}.
        :param insecure_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#insecure_https ConsulProvider#insecure_https}.
        :param key_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#key_file ConsulProvider#key_file}.
        :param key_pem: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#key_pem ConsulProvider#key_pem}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#namespace ConsulProvider#namespace}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#scheme ConsulProvider#scheme}.
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#token ConsulProvider#token}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulProviderConfig.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument ca_file", value=ca_file, expected_type=type_hints["ca_file"])
            check_type(argname="argument ca_path", value=ca_path, expected_type=type_hints["ca_path"])
            check_type(argname="argument ca_pem", value=ca_pem, expected_type=type_hints["ca_pem"])
            check_type(argname="argument cert_file", value=cert_file, expected_type=type_hints["cert_file"])
            check_type(argname="argument cert_pem", value=cert_pem, expected_type=type_hints["cert_pem"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument http_auth", value=http_auth, expected_type=type_hints["http_auth"])
            check_type(argname="argument insecure_https", value=insecure_https, expected_type=type_hints["insecure_https"])
            check_type(argname="argument key_file", value=key_file, expected_type=type_hints["key_file"])
            check_type(argname="argument key_pem", value=key_pem, expected_type=type_hints["key_pem"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if alias is not None:
            self._values["alias"] = alias
        if ca_file is not None:
            self._values["ca_file"] = ca_file
        if ca_path is not None:
            self._values["ca_path"] = ca_path
        if ca_pem is not None:
            self._values["ca_pem"] = ca_pem
        if cert_file is not None:
            self._values["cert_file"] = cert_file
        if cert_pem is not None:
            self._values["cert_pem"] = cert_pem
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if header is not None:
            self._values["header"] = header
        if http_auth is not None:
            self._values["http_auth"] = http_auth
        if insecure_https is not None:
            self._values["insecure_https"] = insecure_https
        if key_file is not None:
            self._values["key_file"] = key_file
        if key_pem is not None:
            self._values["key_pem"] = key_pem
        if namespace is not None:
            self._values["namespace"] = namespace
        if scheme is not None:
            self._values["scheme"] = scheme
        if token is not None:
            self._values["token"] = token

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#address ConsulProvider#address}.'''
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#alias ConsulProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_file ConsulProvider#ca_file}.'''
        result = self._values.get("ca_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_path ConsulProvider#ca_path}.'''
        result = self._values.get("ca_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_pem(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#ca_pem ConsulProvider#ca_pem}.'''
        result = self._values.get("ca_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#cert_file ConsulProvider#cert_file}.'''
        result = self._values.get("cert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cert_pem(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#cert_pem ConsulProvider#cert_pem}.'''
        result = self._values.get("cert_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#datacenter ConsulProvider#datacenter}.'''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#header ConsulProvider#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ConsulProviderHeader"]]], result)

    @builtins.property
    def http_auth(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#http_auth ConsulProvider#http_auth}.'''
        result = self._values.get("http_auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#insecure_https ConsulProvider#insecure_https}.'''
        result = self._values.get("insecure_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#key_file ConsulProvider#key_file}.'''
        result = self._values.get("key_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_pem(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#key_pem ConsulProvider#key_pem}.'''
        result = self._values.get("key_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#namespace ConsulProvider#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#scheme ConsulProvider#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#token ConsulProvider#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsulProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.provider.ConsulProviderHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ConsulProviderHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: The header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#name ConsulProvider#name}
        :param value: The header value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#value ConsulProvider#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ConsulProviderHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#name ConsulProvider#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The header value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul#value ConsulProvider#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsulProviderHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConsulProvider",
    "ConsulProviderConfig",
    "ConsulProviderHeader",
]

publication.publish()
