'''
# `provider`

Refer to the Terraform Registory for docs: [`ad`](https://www.terraform.io/docs/providers/ad).
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


class AdProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ad.provider.AdProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ad ad}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        winrm_hostname: builtins.str,
        winrm_password: builtins.str,
        winrm_username: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        domain_controller: typing.Optional[builtins.str] = None,
        krb_conf: typing.Optional[builtins.str] = None,
        krb_keytab: typing.Optional[builtins.str] = None,
        krb_realm: typing.Optional[builtins.str] = None,
        krb_spn: typing.Optional[builtins.str] = None,
        winrm_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm_pass_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm_port: typing.Optional[jsii.Number] = None,
        winrm_proto: typing.Optional[builtins.str] = None,
        winrm_use_ntlm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ad ad} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param winrm_hostname: The hostname of the server we will use to run powershell scripts over WinRM. (Environment variable: AD_HOSTNAME). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_hostname AdProvider#winrm_hostname}
        :param winrm_password: The password used to authenticate to the server's WinRM service. (Environment variable: AD_PASSWORD). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_password AdProvider#winrm_password}
        :param winrm_username: The username used to authenticate to the server's WinRM service. (Environment variable: AD_USER). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_username AdProvider#winrm_username}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#alias AdProvider#alias}
        :param domain_controller: Use a specific domain controller. (default: none, environment variable: AD_DC). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#domain_controller AdProvider#domain_controller}
        :param krb_conf: Path to kerberos configuration file. (default: none, environment variable: AD_KRB_CONF). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_conf AdProvider#krb_conf}
        :param krb_keytab: Path to a keytab file to be used instead of a password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_keytab AdProvider#krb_keytab}
        :param krb_realm: The name of the kerberos realm (domain) we will use for authentication. (default: "", environment variable: AD_KRB_REALM). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_realm AdProvider#krb_realm}
        :param krb_spn: Alternative Service Principal Name. (default: none, environment variable: AD_KRB_SPN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_spn AdProvider#krb_spn}
        :param winrm_insecure: Trust unknown certificates. (default: false, environment variable: AD_WINRM_INSECURE). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_insecure AdProvider#winrm_insecure}
        :param winrm_pass_credentials: Pass credentials in WinRM session to create a System.Management.Automation.PSCredential. (default: false, environment variable: AD_WINRM_PASS_CREDENTIALS). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_pass_credentials AdProvider#winrm_pass_credentials}
        :param winrm_port: The port WinRM is listening for connections. (default: 5985, environment variable: AD_PORT). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_port AdProvider#winrm_port}
        :param winrm_proto: The WinRM protocol we will use. (default: http, environment variable: AD_PROTO). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_proto AdProvider#winrm_proto}
        :param winrm_use_ntlm: Use NTLM authentication. (default: false, environment variable: AD_WINRM_USE_NTLM). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_use_ntlm AdProvider#winrm_use_ntlm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AdProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AdProviderConfig(
            winrm_hostname=winrm_hostname,
            winrm_password=winrm_password,
            winrm_username=winrm_username,
            alias=alias,
            domain_controller=domain_controller,
            krb_conf=krb_conf,
            krb_keytab=krb_keytab,
            krb_realm=krb_realm,
            krb_spn=krb_spn,
            winrm_insecure=winrm_insecure,
            winrm_pass_credentials=winrm_pass_credentials,
            winrm_port=winrm_port,
            winrm_proto=winrm_proto,
            winrm_use_ntlm=winrm_use_ntlm,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetDomainController")
    def reset_domain_controller(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainController", []))

    @jsii.member(jsii_name="resetKrbConf")
    def reset_krb_conf(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKrbConf", []))

    @jsii.member(jsii_name="resetKrbKeytab")
    def reset_krb_keytab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKrbKeytab", []))

    @jsii.member(jsii_name="resetKrbRealm")
    def reset_krb_realm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKrbRealm", []))

    @jsii.member(jsii_name="resetKrbSpn")
    def reset_krb_spn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKrbSpn", []))

    @jsii.member(jsii_name="resetWinrmInsecure")
    def reset_winrm_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmInsecure", []))

    @jsii.member(jsii_name="resetWinrmPassCredentials")
    def reset_winrm_pass_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmPassCredentials", []))

    @jsii.member(jsii_name="resetWinrmPort")
    def reset_winrm_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmPort", []))

    @jsii.member(jsii_name="resetWinrmProto")
    def reset_winrm_proto(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmProto", []))

    @jsii.member(jsii_name="resetWinrmUseNtlm")
    def reset_winrm_use_ntlm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmUseNtlm", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="domainControllerInput")
    def domain_controller_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainControllerInput"))

    @builtins.property
    @jsii.member(jsii_name="krbConfInput")
    def krb_conf_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbConfInput"))

    @builtins.property
    @jsii.member(jsii_name="krbKeytabInput")
    def krb_keytab_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbKeytabInput"))

    @builtins.property
    @jsii.member(jsii_name="krbRealmInput")
    def krb_realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbRealmInput"))

    @builtins.property
    @jsii.member(jsii_name="krbSpnInput")
    def krb_spn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbSpnInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmHostnameInput")
    def winrm_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmInsecureInput")
    def winrm_insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "winrmInsecureInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmPassCredentialsInput")
    def winrm_pass_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "winrmPassCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmPasswordInput")
    def winrm_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmPortInput")
    def winrm_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "winrmPortInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmProtoInput")
    def winrm_proto_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmProtoInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmUseNtlmInput")
    def winrm_use_ntlm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "winrmUseNtlmInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmUsernameInput")
    def winrm_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="domainController")
    def domain_controller(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainController"))

    @domain_controller.setter
    def domain_controller(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "domain_controller").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainController", value)

    @builtins.property
    @jsii.member(jsii_name="krbConf")
    def krb_conf(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbConf"))

    @krb_conf.setter
    def krb_conf(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "krb_conf").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "krbConf", value)

    @builtins.property
    @jsii.member(jsii_name="krbKeytab")
    def krb_keytab(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbKeytab"))

    @krb_keytab.setter
    def krb_keytab(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "krb_keytab").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "krbKeytab", value)

    @builtins.property
    @jsii.member(jsii_name="krbRealm")
    def krb_realm(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbRealm"))

    @krb_realm.setter
    def krb_realm(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "krb_realm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "krbRealm", value)

    @builtins.property
    @jsii.member(jsii_name="krbSpn")
    def krb_spn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "krbSpn"))

    @krb_spn.setter
    def krb_spn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "krb_spn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "krbSpn", value)

    @builtins.property
    @jsii.member(jsii_name="winrmHostname")
    def winrm_hostname(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmHostname"))

    @winrm_hostname.setter
    def winrm_hostname(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmHostname", value)

    @builtins.property
    @jsii.member(jsii_name="winrmInsecure")
    def winrm_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "winrmInsecure"))

    @winrm_insecure.setter
    def winrm_insecure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmInsecure", value)

    @builtins.property
    @jsii.member(jsii_name="winrmPassCredentials")
    def winrm_pass_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "winrmPassCredentials"))

    @winrm_pass_credentials.setter
    def winrm_pass_credentials(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_pass_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmPassCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="winrmPassword")
    def winrm_password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmPassword"))

    @winrm_password.setter
    def winrm_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmPassword", value)

    @builtins.property
    @jsii.member(jsii_name="winrmPort")
    def winrm_port(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "winrmPort"))

    @winrm_port.setter
    def winrm_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmPort", value)

    @builtins.property
    @jsii.member(jsii_name="winrmProto")
    def winrm_proto(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmProto"))

    @winrm_proto.setter
    def winrm_proto(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_proto").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmProto", value)

    @builtins.property
    @jsii.member(jsii_name="winrmUseNtlm")
    def winrm_use_ntlm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "winrmUseNtlm"))

    @winrm_use_ntlm.setter
    def winrm_use_ntlm(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_use_ntlm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmUseNtlm", value)

    @builtins.property
    @jsii.member(jsii_name="winrmUsername")
    def winrm_username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "winrmUsername"))

    @winrm_username.setter
    def winrm_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AdProvider, "winrm_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "winrmUsername", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ad.provider.AdProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "winrm_hostname": "winrmHostname",
        "winrm_password": "winrmPassword",
        "winrm_username": "winrmUsername",
        "alias": "alias",
        "domain_controller": "domainController",
        "krb_conf": "krbConf",
        "krb_keytab": "krbKeytab",
        "krb_realm": "krbRealm",
        "krb_spn": "krbSpn",
        "winrm_insecure": "winrmInsecure",
        "winrm_pass_credentials": "winrmPassCredentials",
        "winrm_port": "winrmPort",
        "winrm_proto": "winrmProto",
        "winrm_use_ntlm": "winrmUseNtlm",
    },
)
class AdProviderConfig:
    def __init__(
        self,
        *,
        winrm_hostname: builtins.str,
        winrm_password: builtins.str,
        winrm_username: builtins.str,
        alias: typing.Optional[builtins.str] = None,
        domain_controller: typing.Optional[builtins.str] = None,
        krb_conf: typing.Optional[builtins.str] = None,
        krb_keytab: typing.Optional[builtins.str] = None,
        krb_realm: typing.Optional[builtins.str] = None,
        krb_spn: typing.Optional[builtins.str] = None,
        winrm_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm_pass_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm_port: typing.Optional[jsii.Number] = None,
        winrm_proto: typing.Optional[builtins.str] = None,
        winrm_use_ntlm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param winrm_hostname: The hostname of the server we will use to run powershell scripts over WinRM. (Environment variable: AD_HOSTNAME). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_hostname AdProvider#winrm_hostname}
        :param winrm_password: The password used to authenticate to the server's WinRM service. (Environment variable: AD_PASSWORD). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_password AdProvider#winrm_password}
        :param winrm_username: The username used to authenticate to the server's WinRM service. (Environment variable: AD_USER). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_username AdProvider#winrm_username}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#alias AdProvider#alias}
        :param domain_controller: Use a specific domain controller. (default: none, environment variable: AD_DC). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#domain_controller AdProvider#domain_controller}
        :param krb_conf: Path to kerberos configuration file. (default: none, environment variable: AD_KRB_CONF). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_conf AdProvider#krb_conf}
        :param krb_keytab: Path to a keytab file to be used instead of a password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_keytab AdProvider#krb_keytab}
        :param krb_realm: The name of the kerberos realm (domain) we will use for authentication. (default: "", environment variable: AD_KRB_REALM). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_realm AdProvider#krb_realm}
        :param krb_spn: Alternative Service Principal Name. (default: none, environment variable: AD_KRB_SPN). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_spn AdProvider#krb_spn}
        :param winrm_insecure: Trust unknown certificates. (default: false, environment variable: AD_WINRM_INSECURE). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_insecure AdProvider#winrm_insecure}
        :param winrm_pass_credentials: Pass credentials in WinRM session to create a System.Management.Automation.PSCredential. (default: false, environment variable: AD_WINRM_PASS_CREDENTIALS). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_pass_credentials AdProvider#winrm_pass_credentials}
        :param winrm_port: The port WinRM is listening for connections. (default: 5985, environment variable: AD_PORT). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_port AdProvider#winrm_port}
        :param winrm_proto: The WinRM protocol we will use. (default: http, environment variable: AD_PROTO). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_proto AdProvider#winrm_proto}
        :param winrm_use_ntlm: Use NTLM authentication. (default: false, environment variable: AD_WINRM_USE_NTLM). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_use_ntlm AdProvider#winrm_use_ntlm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AdProviderConfig.__init__)
            check_type(argname="argument winrm_hostname", value=winrm_hostname, expected_type=type_hints["winrm_hostname"])
            check_type(argname="argument winrm_password", value=winrm_password, expected_type=type_hints["winrm_password"])
            check_type(argname="argument winrm_username", value=winrm_username, expected_type=type_hints["winrm_username"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument domain_controller", value=domain_controller, expected_type=type_hints["domain_controller"])
            check_type(argname="argument krb_conf", value=krb_conf, expected_type=type_hints["krb_conf"])
            check_type(argname="argument krb_keytab", value=krb_keytab, expected_type=type_hints["krb_keytab"])
            check_type(argname="argument krb_realm", value=krb_realm, expected_type=type_hints["krb_realm"])
            check_type(argname="argument krb_spn", value=krb_spn, expected_type=type_hints["krb_spn"])
            check_type(argname="argument winrm_insecure", value=winrm_insecure, expected_type=type_hints["winrm_insecure"])
            check_type(argname="argument winrm_pass_credentials", value=winrm_pass_credentials, expected_type=type_hints["winrm_pass_credentials"])
            check_type(argname="argument winrm_port", value=winrm_port, expected_type=type_hints["winrm_port"])
            check_type(argname="argument winrm_proto", value=winrm_proto, expected_type=type_hints["winrm_proto"])
            check_type(argname="argument winrm_use_ntlm", value=winrm_use_ntlm, expected_type=type_hints["winrm_use_ntlm"])
        self._values: typing.Dict[str, typing.Any] = {
            "winrm_hostname": winrm_hostname,
            "winrm_password": winrm_password,
            "winrm_username": winrm_username,
        }
        if alias is not None:
            self._values["alias"] = alias
        if domain_controller is not None:
            self._values["domain_controller"] = domain_controller
        if krb_conf is not None:
            self._values["krb_conf"] = krb_conf
        if krb_keytab is not None:
            self._values["krb_keytab"] = krb_keytab
        if krb_realm is not None:
            self._values["krb_realm"] = krb_realm
        if krb_spn is not None:
            self._values["krb_spn"] = krb_spn
        if winrm_insecure is not None:
            self._values["winrm_insecure"] = winrm_insecure
        if winrm_pass_credentials is not None:
            self._values["winrm_pass_credentials"] = winrm_pass_credentials
        if winrm_port is not None:
            self._values["winrm_port"] = winrm_port
        if winrm_proto is not None:
            self._values["winrm_proto"] = winrm_proto
        if winrm_use_ntlm is not None:
            self._values["winrm_use_ntlm"] = winrm_use_ntlm

    @builtins.property
    def winrm_hostname(self) -> builtins.str:
        '''The hostname of the server we will use to run powershell scripts over WinRM. (Environment variable: AD_HOSTNAME).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_hostname AdProvider#winrm_hostname}
        '''
        result = self._values.get("winrm_hostname")
        assert result is not None, "Required property 'winrm_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def winrm_password(self) -> builtins.str:
        '''The password used to authenticate to the server's WinRM service. (Environment variable: AD_PASSWORD).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_password AdProvider#winrm_password}
        '''
        result = self._values.get("winrm_password")
        assert result is not None, "Required property 'winrm_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def winrm_username(self) -> builtins.str:
        '''The username used to authenticate to the server's WinRM service. (Environment variable: AD_USER).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_username AdProvider#winrm_username}
        '''
        result = self._values.get("winrm_username")
        assert result is not None, "Required property 'winrm_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#alias AdProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_controller(self) -> typing.Optional[builtins.str]:
        '''Use a specific domain controller. (default: none, environment variable: AD_DC).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#domain_controller AdProvider#domain_controller}
        '''
        result = self._values.get("domain_controller")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def krb_conf(self) -> typing.Optional[builtins.str]:
        '''Path to kerberos configuration file. (default: none, environment variable: AD_KRB_CONF).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_conf AdProvider#krb_conf}
        '''
        result = self._values.get("krb_conf")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def krb_keytab(self) -> typing.Optional[builtins.str]:
        '''Path to a keytab file to be used instead of a password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_keytab AdProvider#krb_keytab}
        '''
        result = self._values.get("krb_keytab")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def krb_realm(self) -> typing.Optional[builtins.str]:
        '''The name of the kerberos realm (domain) we will use for authentication. (default: "", environment variable: AD_KRB_REALM).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_realm AdProvider#krb_realm}
        '''
        result = self._values.get("krb_realm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def krb_spn(self) -> typing.Optional[builtins.str]:
        '''Alternative Service Principal Name. (default: none, environment variable: AD_KRB_SPN).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#krb_spn AdProvider#krb_spn}
        '''
        result = self._values.get("krb_spn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def winrm_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Trust unknown certificates. (default: false, environment variable: AD_WINRM_INSECURE).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_insecure AdProvider#winrm_insecure}
        '''
        result = self._values.get("winrm_insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def winrm_pass_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Pass credentials in WinRM session to create a System.Management.Automation.PSCredential. (default: false, environment variable: AD_WINRM_PASS_CREDENTIALS).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_pass_credentials AdProvider#winrm_pass_credentials}
        '''
        result = self._values.get("winrm_pass_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def winrm_port(self) -> typing.Optional[jsii.Number]:
        '''The port WinRM is listening for connections. (default: 5985, environment variable: AD_PORT).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_port AdProvider#winrm_port}
        '''
        result = self._values.get("winrm_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def winrm_proto(self) -> typing.Optional[builtins.str]:
        '''The WinRM protocol we will use. (default: http, environment variable: AD_PROTO).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_proto AdProvider#winrm_proto}
        '''
        result = self._values.get("winrm_proto")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def winrm_use_ntlm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use NTLM authentication. (default: false, environment variable: AD_WINRM_USE_NTLM).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ad#winrm_use_ntlm AdProvider#winrm_use_ntlm}
        '''
        result = self._values.get("winrm_use_ntlm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AdProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AdProvider",
    "AdProviderConfig",
]

publication.publish()
