'''
# `cloudflare_teams_account`

Refer to the Terraform Registory for docs: [`cloudflare_teams_account`](https://www.terraform.io/docs/providers/cloudflare/r/teams_account).
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


class TeamsAccount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account cloudflare_teams_account}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        activity_log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        antivirus: typing.Optional[typing.Union["TeamsAccountAntivirus", typing.Dict[str, typing.Any]]] = None,
        block_page: typing.Optional[typing.Union["TeamsAccountBlockPage", typing.Dict[str, typing.Any]]] = None,
        fips: typing.Optional[typing.Union["TeamsAccountFips", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union["TeamsAccountLogging", typing.Dict[str, typing.Any]]] = None,
        proxy: typing.Optional[typing.Union["TeamsAccountProxy", typing.Dict[str, typing.Any]]] = None,
        tls_decrypt_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        url_browser_isolation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account cloudflare_teams_account} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#account_id TeamsAccount#account_id}
        :param activity_log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#activity_log_enabled TeamsAccount#activity_log_enabled}.
        :param antivirus: antivirus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#antivirus TeamsAccount#antivirus}
        :param block_page: block_page block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#block_page TeamsAccount#block_page}
        :param fips: fips block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#fips TeamsAccount#fips}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#id TeamsAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#logging TeamsAccount#logging}
        :param proxy: proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#proxy TeamsAccount#proxy}
        :param tls_decrypt_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tls_decrypt_enabled TeamsAccount#tls_decrypt_enabled}.
        :param url_browser_isolation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#url_browser_isolation_enabled TeamsAccount#url_browser_isolation_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TeamsAccountConfig(
            account_id=account_id,
            activity_log_enabled=activity_log_enabled,
            antivirus=antivirus,
            block_page=block_page,
            fips=fips,
            id=id,
            logging=logging,
            proxy=proxy,
            tls_decrypt_enabled=tls_decrypt_enabled,
            url_browser_isolation_enabled=url_browser_isolation_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAntivirus")
    def put_antivirus(
        self,
        *,
        enabled_download_phase: typing.Union[builtins.bool, cdktf.IResolvable],
        enabled_upload_phase: typing.Union[builtins.bool, cdktf.IResolvable],
        fail_closed: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled_download_phase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled_download_phase TeamsAccount#enabled_download_phase}.
        :param enabled_upload_phase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled_upload_phase TeamsAccount#enabled_upload_phase}.
        :param fail_closed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#fail_closed TeamsAccount#fail_closed}.
        '''
        value = TeamsAccountAntivirus(
            enabled_download_phase=enabled_download_phase,
            enabled_upload_phase=enabled_upload_phase,
            fail_closed=fail_closed,
        )

        return typing.cast(None, jsii.invoke(self, "putAntivirus", [value]))

    @jsii.member(jsii_name="putBlockPage")
    def put_block_page(
        self,
        *,
        background_color: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        footer_text: typing.Optional[builtins.str] = None,
        header_text: typing.Optional[builtins.str] = None,
        logo_path: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param background_color: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#background_color TeamsAccount#background_color}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled TeamsAccount#enabled}.
        :param footer_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#footer_text TeamsAccount#footer_text}.
        :param header_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#header_text TeamsAccount#header_text}.
        :param logo_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#logo_path TeamsAccount#logo_path}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#name TeamsAccount#name}.
        '''
        value = TeamsAccountBlockPage(
            background_color=background_color,
            enabled=enabled,
            footer_text=footer_text,
            header_text=header_text,
            logo_path=logo_path,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putBlockPage", [value]))

    @jsii.member(jsii_name="putFips")
    def put_fips(
        self,
        *,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param tls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tls TeamsAccount#tls}.
        '''
        value = TeamsAccountFips(tls=tls)

        return typing.cast(None, jsii.invoke(self, "putFips", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        redact_pii: typing.Union[builtins.bool, cdktf.IResolvable],
        settings_by_rule_type: typing.Union["TeamsAccountLoggingSettingsByRuleType", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param redact_pii: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#redact_pii TeamsAccount#redact_pii}.
        :param settings_by_rule_type: settings_by_rule_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#settings_by_rule_type TeamsAccount#settings_by_rule_type}
        '''
        value = TeamsAccountLogging(
            redact_pii=redact_pii, settings_by_rule_type=settings_by_rule_type
        )

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putProxy")
    def put_proxy(
        self,
        *,
        tcp: typing.Union[builtins.bool, cdktf.IResolvable],
        udp: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param tcp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tcp TeamsAccount#tcp}.
        :param udp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#udp TeamsAccount#udp}.
        '''
        value = TeamsAccountProxy(tcp=tcp, udp=udp)

        return typing.cast(None, jsii.invoke(self, "putProxy", [value]))

    @jsii.member(jsii_name="resetActivityLogEnabled")
    def reset_activity_log_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivityLogEnabled", []))

    @jsii.member(jsii_name="resetAntivirus")
    def reset_antivirus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAntivirus", []))

    @jsii.member(jsii_name="resetBlockPage")
    def reset_block_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockPage", []))

    @jsii.member(jsii_name="resetFips")
    def reset_fips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFips", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetProxy")
    def reset_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxy", []))

    @jsii.member(jsii_name="resetTlsDecryptEnabled")
    def reset_tls_decrypt_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsDecryptEnabled", []))

    @jsii.member(jsii_name="resetUrlBrowserIsolationEnabled")
    def reset_url_browser_isolation_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlBrowserIsolationEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="antivirus")
    def antivirus(self) -> "TeamsAccountAntivirusOutputReference":
        return typing.cast("TeamsAccountAntivirusOutputReference", jsii.get(self, "antivirus"))

    @builtins.property
    @jsii.member(jsii_name="blockPage")
    def block_page(self) -> "TeamsAccountBlockPageOutputReference":
        return typing.cast("TeamsAccountBlockPageOutputReference", jsii.get(self, "blockPage"))

    @builtins.property
    @jsii.member(jsii_name="fips")
    def fips(self) -> "TeamsAccountFipsOutputReference":
        return typing.cast("TeamsAccountFipsOutputReference", jsii.get(self, "fips"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> "TeamsAccountLoggingOutputReference":
        return typing.cast("TeamsAccountLoggingOutputReference", jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="proxy")
    def proxy(self) -> "TeamsAccountProxyOutputReference":
        return typing.cast("TeamsAccountProxyOutputReference", jsii.get(self, "proxy"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="activityLogEnabledInput")
    def activity_log_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activityLogEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="antivirusInput")
    def antivirus_input(self) -> typing.Optional["TeamsAccountAntivirus"]:
        return typing.cast(typing.Optional["TeamsAccountAntivirus"], jsii.get(self, "antivirusInput"))

    @builtins.property
    @jsii.member(jsii_name="blockPageInput")
    def block_page_input(self) -> typing.Optional["TeamsAccountBlockPage"]:
        return typing.cast(typing.Optional["TeamsAccountBlockPage"], jsii.get(self, "blockPageInput"))

    @builtins.property
    @jsii.member(jsii_name="fipsInput")
    def fips_input(self) -> typing.Optional["TeamsAccountFips"]:
        return typing.cast(typing.Optional["TeamsAccountFips"], jsii.get(self, "fipsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional["TeamsAccountLogging"]:
        return typing.cast(typing.Optional["TeamsAccountLogging"], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyInput")
    def proxy_input(self) -> typing.Optional["TeamsAccountProxy"]:
        return typing.cast(typing.Optional["TeamsAccountProxy"], jsii.get(self, "proxyInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsDecryptEnabledInput")
    def tls_decrypt_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsDecryptEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="urlBrowserIsolationEnabledInput")
    def url_browser_isolation_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "urlBrowserIsolationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccount, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="activityLogEnabled")
    def activity_log_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "activityLogEnabled"))

    @activity_log_enabled.setter
    def activity_log_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccount, "activity_log_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activityLogEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccount, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tlsDecryptEnabled")
    def tls_decrypt_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsDecryptEnabled"))

    @tls_decrypt_enabled.setter
    def tls_decrypt_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccount, "tls_decrypt_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsDecryptEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="urlBrowserIsolationEnabled")
    def url_browser_isolation_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "urlBrowserIsolationEnabled"))

    @url_browser_isolation_enabled.setter
    def url_browser_isolation_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccount, "url_browser_isolation_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlBrowserIsolationEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountAntivirus",
    jsii_struct_bases=[],
    name_mapping={
        "enabled_download_phase": "enabledDownloadPhase",
        "enabled_upload_phase": "enabledUploadPhase",
        "fail_closed": "failClosed",
    },
)
class TeamsAccountAntivirus:
    def __init__(
        self,
        *,
        enabled_download_phase: typing.Union[builtins.bool, cdktf.IResolvable],
        enabled_upload_phase: typing.Union[builtins.bool, cdktf.IResolvable],
        fail_closed: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled_download_phase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled_download_phase TeamsAccount#enabled_download_phase}.
        :param enabled_upload_phase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled_upload_phase TeamsAccount#enabled_upload_phase}.
        :param fail_closed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#fail_closed TeamsAccount#fail_closed}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountAntivirus.__init__)
            check_type(argname="argument enabled_download_phase", value=enabled_download_phase, expected_type=type_hints["enabled_download_phase"])
            check_type(argname="argument enabled_upload_phase", value=enabled_upload_phase, expected_type=type_hints["enabled_upload_phase"])
            check_type(argname="argument fail_closed", value=fail_closed, expected_type=type_hints["fail_closed"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled_download_phase": enabled_download_phase,
            "enabled_upload_phase": enabled_upload_phase,
            "fail_closed": fail_closed,
        }

    @builtins.property
    def enabled_download_phase(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled_download_phase TeamsAccount#enabled_download_phase}.'''
        result = self._values.get("enabled_download_phase")
        assert result is not None, "Required property 'enabled_download_phase' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def enabled_upload_phase(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled_upload_phase TeamsAccount#enabled_upload_phase}.'''
        result = self._values.get("enabled_upload_phase")
        assert result is not None, "Required property 'enabled_upload_phase' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def fail_closed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#fail_closed TeamsAccount#fail_closed}.'''
        result = self._values.get("fail_closed")
        assert result is not None, "Required property 'fail_closed' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountAntivirus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountAntivirusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountAntivirusOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountAntivirusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledDownloadPhaseInput")
    def enabled_download_phase_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledDownloadPhaseInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledUploadPhaseInput")
    def enabled_upload_phase_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledUploadPhaseInput"))

    @builtins.property
    @jsii.member(jsii_name="failClosedInput")
    def fail_closed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failClosedInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledDownloadPhase")
    def enabled_download_phase(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledDownloadPhase"))

    @enabled_download_phase.setter
    def enabled_download_phase(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountAntivirusOutputReference, "enabled_download_phase").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledDownloadPhase", value)

    @builtins.property
    @jsii.member(jsii_name="enabledUploadPhase")
    def enabled_upload_phase(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabledUploadPhase"))

    @enabled_upload_phase.setter
    def enabled_upload_phase(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountAntivirusOutputReference, "enabled_upload_phase").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledUploadPhase", value)

    @builtins.property
    @jsii.member(jsii_name="failClosed")
    def fail_closed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failClosed"))

    @fail_closed.setter
    def fail_closed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountAntivirusOutputReference, "fail_closed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failClosed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamsAccountAntivirus]:
        return typing.cast(typing.Optional[TeamsAccountAntivirus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TeamsAccountAntivirus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountAntivirusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountBlockPage",
    jsii_struct_bases=[],
    name_mapping={
        "background_color": "backgroundColor",
        "enabled": "enabled",
        "footer_text": "footerText",
        "header_text": "headerText",
        "logo_path": "logoPath",
        "name": "name",
    },
)
class TeamsAccountBlockPage:
    def __init__(
        self,
        *,
        background_color: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        footer_text: typing.Optional[builtins.str] = None,
        header_text: typing.Optional[builtins.str] = None,
        logo_path: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param background_color: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#background_color TeamsAccount#background_color}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled TeamsAccount#enabled}.
        :param footer_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#footer_text TeamsAccount#footer_text}.
        :param header_text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#header_text TeamsAccount#header_text}.
        :param logo_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#logo_path TeamsAccount#logo_path}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#name TeamsAccount#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountBlockPage.__init__)
            check_type(argname="argument background_color", value=background_color, expected_type=type_hints["background_color"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument footer_text", value=footer_text, expected_type=type_hints["footer_text"])
            check_type(argname="argument header_text", value=header_text, expected_type=type_hints["header_text"])
            check_type(argname="argument logo_path", value=logo_path, expected_type=type_hints["logo_path"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if background_color is not None:
            self._values["background_color"] = background_color
        if enabled is not None:
            self._values["enabled"] = enabled
        if footer_text is not None:
            self._values["footer_text"] = footer_text
        if header_text is not None:
            self._values["header_text"] = header_text
        if logo_path is not None:
            self._values["logo_path"] = logo_path
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def background_color(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#background_color TeamsAccount#background_color}.'''
        result = self._values.get("background_color")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#enabled TeamsAccount#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def footer_text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#footer_text TeamsAccount#footer_text}.'''
        result = self._values.get("footer_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def header_text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#header_text TeamsAccount#header_text}.'''
        result = self._values.get("header_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logo_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#logo_path TeamsAccount#logo_path}.'''
        result = self._values.get("logo_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#name TeamsAccount#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountBlockPage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountBlockPageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountBlockPageOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountBlockPageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBackgroundColor")
    def reset_background_color(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackgroundColor", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFooterText")
    def reset_footer_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFooterText", []))

    @jsii.member(jsii_name="resetHeaderText")
    def reset_header_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaderText", []))

    @jsii.member(jsii_name="resetLogoPath")
    def reset_logo_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoPath", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="backgroundColorInput")
    def background_color_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backgroundColorInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="footerTextInput")
    def footer_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "footerTextInput"))

    @builtins.property
    @jsii.member(jsii_name="headerTextInput")
    def header_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerTextInput"))

    @builtins.property
    @jsii.member(jsii_name="logoPathInput")
    def logo_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logoPathInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="backgroundColor")
    def background_color(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backgroundColor"))

    @background_color.setter
    def background_color(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "background_color").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backgroundColor", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="footerText")
    def footer_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "footerText"))

    @footer_text.setter
    def footer_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "footer_text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "footerText", value)

    @builtins.property
    @jsii.member(jsii_name="headerText")
    def header_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerText"))

    @header_text.setter
    def header_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "header_text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerText", value)

    @builtins.property
    @jsii.member(jsii_name="logoPath")
    def logo_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoPath"))

    @logo_path.setter
    def logo_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "logo_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logoPath", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamsAccountBlockPage]:
        return typing.cast(typing.Optional[TeamsAccountBlockPage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TeamsAccountBlockPage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountBlockPageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "activity_log_enabled": "activityLogEnabled",
        "antivirus": "antivirus",
        "block_page": "blockPage",
        "fips": "fips",
        "id": "id",
        "logging": "logging",
        "proxy": "proxy",
        "tls_decrypt_enabled": "tlsDecryptEnabled",
        "url_browser_isolation_enabled": "urlBrowserIsolationEnabled",
    },
)
class TeamsAccountConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        account_id: builtins.str,
        activity_log_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        antivirus: typing.Optional[typing.Union[TeamsAccountAntivirus, typing.Dict[str, typing.Any]]] = None,
        block_page: typing.Optional[typing.Union[TeamsAccountBlockPage, typing.Dict[str, typing.Any]]] = None,
        fips: typing.Optional[typing.Union["TeamsAccountFips", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union["TeamsAccountLogging", typing.Dict[str, typing.Any]]] = None,
        proxy: typing.Optional[typing.Union["TeamsAccountProxy", typing.Dict[str, typing.Any]]] = None,
        tls_decrypt_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        url_browser_isolation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#account_id TeamsAccount#account_id}
        :param activity_log_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#activity_log_enabled TeamsAccount#activity_log_enabled}.
        :param antivirus: antivirus block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#antivirus TeamsAccount#antivirus}
        :param block_page: block_page block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#block_page TeamsAccount#block_page}
        :param fips: fips block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#fips TeamsAccount#fips}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#id TeamsAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#logging TeamsAccount#logging}
        :param proxy: proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#proxy TeamsAccount#proxy}
        :param tls_decrypt_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tls_decrypt_enabled TeamsAccount#tls_decrypt_enabled}.
        :param url_browser_isolation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#url_browser_isolation_enabled TeamsAccount#url_browser_isolation_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(antivirus, dict):
            antivirus = TeamsAccountAntivirus(**antivirus)
        if isinstance(block_page, dict):
            block_page = TeamsAccountBlockPage(**block_page)
        if isinstance(fips, dict):
            fips = TeamsAccountFips(**fips)
        if isinstance(logging, dict):
            logging = TeamsAccountLogging(**logging)
        if isinstance(proxy, dict):
            proxy = TeamsAccountProxy(**proxy)
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument activity_log_enabled", value=activity_log_enabled, expected_type=type_hints["activity_log_enabled"])
            check_type(argname="argument antivirus", value=antivirus, expected_type=type_hints["antivirus"])
            check_type(argname="argument block_page", value=block_page, expected_type=type_hints["block_page"])
            check_type(argname="argument fips", value=fips, expected_type=type_hints["fips"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument tls_decrypt_enabled", value=tls_decrypt_enabled, expected_type=type_hints["tls_decrypt_enabled"])
            check_type(argname="argument url_browser_isolation_enabled", value=url_browser_isolation_enabled, expected_type=type_hints["url_browser_isolation_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if activity_log_enabled is not None:
            self._values["activity_log_enabled"] = activity_log_enabled
        if antivirus is not None:
            self._values["antivirus"] = antivirus
        if block_page is not None:
            self._values["block_page"] = block_page
        if fips is not None:
            self._values["fips"] = fips
        if id is not None:
            self._values["id"] = id
        if logging is not None:
            self._values["logging"] = logging
        if proxy is not None:
            self._values["proxy"] = proxy
        if tls_decrypt_enabled is not None:
            self._values["tls_decrypt_enabled"] = tls_decrypt_enabled
        if url_browser_isolation_enabled is not None:
            self._values["url_browser_isolation_enabled"] = url_browser_isolation_enabled

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The account identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#account_id TeamsAccount#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def activity_log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#activity_log_enabled TeamsAccount#activity_log_enabled}.'''
        result = self._values.get("activity_log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def antivirus(self) -> typing.Optional[TeamsAccountAntivirus]:
        '''antivirus block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#antivirus TeamsAccount#antivirus}
        '''
        result = self._values.get("antivirus")
        return typing.cast(typing.Optional[TeamsAccountAntivirus], result)

    @builtins.property
    def block_page(self) -> typing.Optional[TeamsAccountBlockPage]:
        '''block_page block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#block_page TeamsAccount#block_page}
        '''
        result = self._values.get("block_page")
        return typing.cast(typing.Optional[TeamsAccountBlockPage], result)

    @builtins.property
    def fips(self) -> typing.Optional["TeamsAccountFips"]:
        '''fips block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#fips TeamsAccount#fips}
        '''
        result = self._values.get("fips")
        return typing.cast(typing.Optional["TeamsAccountFips"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#id TeamsAccount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(self) -> typing.Optional["TeamsAccountLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#logging TeamsAccount#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["TeamsAccountLogging"], result)

    @builtins.property
    def proxy(self) -> typing.Optional["TeamsAccountProxy"]:
        '''proxy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#proxy TeamsAccount#proxy}
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional["TeamsAccountProxy"], result)

    @builtins.property
    def tls_decrypt_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tls_decrypt_enabled TeamsAccount#tls_decrypt_enabled}.'''
        result = self._values.get("tls_decrypt_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def url_browser_isolation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#url_browser_isolation_enabled TeamsAccount#url_browser_isolation_enabled}.'''
        result = self._values.get("url_browser_isolation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountFips",
    jsii_struct_bases=[],
    name_mapping={"tls": "tls"},
)
class TeamsAccountFips:
    def __init__(
        self,
        *,
        tls: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param tls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tls TeamsAccount#tls}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountFips.__init__)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[str, typing.Any] = {}
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def tls(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tls TeamsAccount#tls}.'''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountFips(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountFipsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountFipsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountFipsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountFipsOutputReference, "tls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamsAccountFips]:
        return typing.cast(typing.Optional[TeamsAccountFips], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TeamsAccountFips]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountFipsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLogging",
    jsii_struct_bases=[],
    name_mapping={
        "redact_pii": "redactPii",
        "settings_by_rule_type": "settingsByRuleType",
    },
)
class TeamsAccountLogging:
    def __init__(
        self,
        *,
        redact_pii: typing.Union[builtins.bool, cdktf.IResolvable],
        settings_by_rule_type: typing.Union["TeamsAccountLoggingSettingsByRuleType", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param redact_pii: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#redact_pii TeamsAccount#redact_pii}.
        :param settings_by_rule_type: settings_by_rule_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#settings_by_rule_type TeamsAccount#settings_by_rule_type}
        '''
        if isinstance(settings_by_rule_type, dict):
            settings_by_rule_type = TeamsAccountLoggingSettingsByRuleType(**settings_by_rule_type)
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLogging.__init__)
            check_type(argname="argument redact_pii", value=redact_pii, expected_type=type_hints["redact_pii"])
            check_type(argname="argument settings_by_rule_type", value=settings_by_rule_type, expected_type=type_hints["settings_by_rule_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "redact_pii": redact_pii,
            "settings_by_rule_type": settings_by_rule_type,
        }

    @builtins.property
    def redact_pii(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#redact_pii TeamsAccount#redact_pii}.'''
        result = self._values.get("redact_pii")
        assert result is not None, "Required property 'redact_pii' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def settings_by_rule_type(self) -> "TeamsAccountLoggingSettingsByRuleType":
        '''settings_by_rule_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#settings_by_rule_type TeamsAccount#settings_by_rule_type}
        '''
        result = self._values.get("settings_by_rule_type")
        assert result is not None, "Required property 'settings_by_rule_type' is missing"
        return typing.cast("TeamsAccountLoggingSettingsByRuleType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSettingsByRuleType")
    def put_settings_by_rule_type(
        self,
        *,
        dns: typing.Union["TeamsAccountLoggingSettingsByRuleTypeDns", typing.Dict[str, typing.Any]],
        http: typing.Union["TeamsAccountLoggingSettingsByRuleTypeHttp", typing.Dict[str, typing.Any]],
        l4: typing.Union["TeamsAccountLoggingSettingsByRuleTypeL4", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#dns TeamsAccount#dns}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#http TeamsAccount#http}
        :param l4: l4 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#l4 TeamsAccount#l4}
        '''
        value = TeamsAccountLoggingSettingsByRuleType(dns=dns, http=http, l4=l4)

        return typing.cast(None, jsii.invoke(self, "putSettingsByRuleType", [value]))

    @builtins.property
    @jsii.member(jsii_name="settingsByRuleType")
    def settings_by_rule_type(
        self,
    ) -> "TeamsAccountLoggingSettingsByRuleTypeOutputReference":
        return typing.cast("TeamsAccountLoggingSettingsByRuleTypeOutputReference", jsii.get(self, "settingsByRuleType"))

    @builtins.property
    @jsii.member(jsii_name="redactPiiInput")
    def redact_pii_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "redactPiiInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsByRuleTypeInput")
    def settings_by_rule_type_input(
        self,
    ) -> typing.Optional["TeamsAccountLoggingSettingsByRuleType"]:
        return typing.cast(typing.Optional["TeamsAccountLoggingSettingsByRuleType"], jsii.get(self, "settingsByRuleTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="redactPii")
    def redact_pii(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "redactPii"))

    @redact_pii.setter
    def redact_pii(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingOutputReference, "redact_pii").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redactPii", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamsAccountLogging]:
        return typing.cast(typing.Optional[TeamsAccountLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TeamsAccountLogging]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleType",
    jsii_struct_bases=[],
    name_mapping={"dns": "dns", "http": "http", "l4": "l4"},
)
class TeamsAccountLoggingSettingsByRuleType:
    def __init__(
        self,
        *,
        dns: typing.Union["TeamsAccountLoggingSettingsByRuleTypeDns", typing.Dict[str, typing.Any]],
        http: typing.Union["TeamsAccountLoggingSettingsByRuleTypeHttp", typing.Dict[str, typing.Any]],
        l4: typing.Union["TeamsAccountLoggingSettingsByRuleTypeL4", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#dns TeamsAccount#dns}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#http TeamsAccount#http}
        :param l4: l4 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#l4 TeamsAccount#l4}
        '''
        if isinstance(dns, dict):
            dns = TeamsAccountLoggingSettingsByRuleTypeDns(**dns)
        if isinstance(http, dict):
            http = TeamsAccountLoggingSettingsByRuleTypeHttp(**http)
        if isinstance(l4, dict):
            l4 = TeamsAccountLoggingSettingsByRuleTypeL4(**l4)
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleType.__init__)
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument l4", value=l4, expected_type=type_hints["l4"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns": dns,
            "http": http,
            "l4": l4,
        }

    @builtins.property
    def dns(self) -> "TeamsAccountLoggingSettingsByRuleTypeDns":
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#dns TeamsAccount#dns}
        '''
        result = self._values.get("dns")
        assert result is not None, "Required property 'dns' is missing"
        return typing.cast("TeamsAccountLoggingSettingsByRuleTypeDns", result)

    @builtins.property
    def http(self) -> "TeamsAccountLoggingSettingsByRuleTypeHttp":
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#http TeamsAccount#http}
        '''
        result = self._values.get("http")
        assert result is not None, "Required property 'http' is missing"
        return typing.cast("TeamsAccountLoggingSettingsByRuleTypeHttp", result)

    @builtins.property
    def l4(self) -> "TeamsAccountLoggingSettingsByRuleTypeL4":
        '''l4 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#l4 TeamsAccount#l4}
        '''
        result = self._values.get("l4")
        assert result is not None, "Required property 'l4' is missing"
        return typing.cast("TeamsAccountLoggingSettingsByRuleTypeL4", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountLoggingSettingsByRuleType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeDns",
    jsii_struct_bases=[],
    name_mapping={"log_all": "logAll", "log_blocks": "logBlocks"},
)
class TeamsAccountLoggingSettingsByRuleTypeDns:
    def __init__(
        self,
        *,
        log_all: typing.Union[builtins.bool, cdktf.IResolvable],
        log_blocks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param log_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.
        :param log_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeDns.__init__)
            check_type(argname="argument log_all", value=log_all, expected_type=type_hints["log_all"])
            check_type(argname="argument log_blocks", value=log_blocks, expected_type=type_hints["log_blocks"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_all": log_all,
            "log_blocks": log_blocks,
        }

    @builtins.property
    def log_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.'''
        result = self._values.get("log_all")
        assert result is not None, "Required property 'log_all' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_blocks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.'''
        result = self._values.get("log_blocks")
        assert result is not None, "Required property 'log_blocks' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountLoggingSettingsByRuleTypeDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logAllInput")
    def log_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logAllInput"))

    @builtins.property
    @jsii.member(jsii_name="logBlocksInput")
    def log_blocks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="logAll")
    def log_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logAll"))

    @log_all.setter
    def log_all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference, "log_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAll", value)

    @builtins.property
    @jsii.member(jsii_name="logBlocks")
    def log_blocks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logBlocks"))

    @log_blocks.setter
    def log_blocks(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference, "log_blocks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TeamsAccountLoggingSettingsByRuleTypeDns]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleTypeDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TeamsAccountLoggingSettingsByRuleTypeDns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeHttp",
    jsii_struct_bases=[],
    name_mapping={"log_all": "logAll", "log_blocks": "logBlocks"},
)
class TeamsAccountLoggingSettingsByRuleTypeHttp:
    def __init__(
        self,
        *,
        log_all: typing.Union[builtins.bool, cdktf.IResolvable],
        log_blocks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param log_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.
        :param log_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeHttp.__init__)
            check_type(argname="argument log_all", value=log_all, expected_type=type_hints["log_all"])
            check_type(argname="argument log_blocks", value=log_blocks, expected_type=type_hints["log_blocks"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_all": log_all,
            "log_blocks": log_blocks,
        }

    @builtins.property
    def log_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.'''
        result = self._values.get("log_all")
        assert result is not None, "Required property 'log_all' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_blocks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.'''
        result = self._values.get("log_blocks")
        assert result is not None, "Required property 'log_blocks' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountLoggingSettingsByRuleTypeHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logAllInput")
    def log_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logAllInput"))

    @builtins.property
    @jsii.member(jsii_name="logBlocksInput")
    def log_blocks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="logAll")
    def log_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logAll"))

    @log_all.setter
    def log_all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference, "log_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAll", value)

    @builtins.property
    @jsii.member(jsii_name="logBlocks")
    def log_blocks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logBlocks"))

    @log_blocks.setter
    def log_blocks(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference, "log_blocks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TeamsAccountLoggingSettingsByRuleTypeHttp]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleTypeHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TeamsAccountLoggingSettingsByRuleTypeHttp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeL4",
    jsii_struct_bases=[],
    name_mapping={"log_all": "logAll", "log_blocks": "logBlocks"},
)
class TeamsAccountLoggingSettingsByRuleTypeL4:
    def __init__(
        self,
        *,
        log_all: typing.Union[builtins.bool, cdktf.IResolvable],
        log_blocks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param log_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.
        :param log_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeL4.__init__)
            check_type(argname="argument log_all", value=log_all, expected_type=type_hints["log_all"])
            check_type(argname="argument log_blocks", value=log_blocks, expected_type=type_hints["log_blocks"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_all": log_all,
            "log_blocks": log_blocks,
        }

    @builtins.property
    def log_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.'''
        result = self._values.get("log_all")
        assert result is not None, "Required property 'log_all' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_blocks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.'''
        result = self._values.get("log_blocks")
        assert result is not None, "Required property 'log_blocks' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountLoggingSettingsByRuleTypeL4(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountLoggingSettingsByRuleTypeL4OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeL4OutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeL4OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logAllInput")
    def log_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logAllInput"))

    @builtins.property
    @jsii.member(jsii_name="logBlocksInput")
    def log_blocks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="logAll")
    def log_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logAll"))

    @log_all.setter
    def log_all(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeL4OutputReference, "log_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAll", value)

    @builtins.property
    @jsii.member(jsii_name="logBlocks")
    def log_blocks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logBlocks"))

    @log_blocks.setter
    def log_blocks(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeL4OutputReference, "log_blocks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TeamsAccountLoggingSettingsByRuleTypeL4]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleTypeL4], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TeamsAccountLoggingSettingsByRuleTypeL4],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeL4OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TeamsAccountLoggingSettingsByRuleTypeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountLoggingSettingsByRuleTypeOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountLoggingSettingsByRuleTypeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDns")
    def put_dns(
        self,
        *,
        log_all: typing.Union[builtins.bool, cdktf.IResolvable],
        log_blocks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param log_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.
        :param log_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.
        '''
        value = TeamsAccountLoggingSettingsByRuleTypeDns(
            log_all=log_all, log_blocks=log_blocks
        )

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        log_all: typing.Union[builtins.bool, cdktf.IResolvable],
        log_blocks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param log_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.
        :param log_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.
        '''
        value = TeamsAccountLoggingSettingsByRuleTypeHttp(
            log_all=log_all, log_blocks=log_blocks
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putL4")
    def put_l4(
        self,
        *,
        log_all: typing.Union[builtins.bool, cdktf.IResolvable],
        log_blocks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param log_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_all TeamsAccount#log_all}.
        :param log_blocks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#log_blocks TeamsAccount#log_blocks}.
        '''
        value = TeamsAccountLoggingSettingsByRuleTypeL4(
            log_all=log_all, log_blocks=log_blocks
        )

        return typing.cast(None, jsii.invoke(self, "putL4", [value]))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference:
        return typing.cast(TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference, jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference:
        return typing.cast(TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="l4")
    def l4(self) -> TeamsAccountLoggingSettingsByRuleTypeL4OutputReference:
        return typing.cast(TeamsAccountLoggingSettingsByRuleTypeL4OutputReference, jsii.get(self, "l4"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[TeamsAccountLoggingSettingsByRuleTypeDns]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleTypeDns], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[TeamsAccountLoggingSettingsByRuleTypeHttp]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleTypeHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="l4Input")
    def l4_input(self) -> typing.Optional[TeamsAccountLoggingSettingsByRuleTypeL4]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleTypeL4], jsii.get(self, "l4Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamsAccountLoggingSettingsByRuleType]:
        return typing.cast(typing.Optional[TeamsAccountLoggingSettingsByRuleType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TeamsAccountLoggingSettingsByRuleType],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountLoggingSettingsByRuleTypeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountProxy",
    jsii_struct_bases=[],
    name_mapping={"tcp": "tcp", "udp": "udp"},
)
class TeamsAccountProxy:
    def __init__(
        self,
        *,
        tcp: typing.Union[builtins.bool, cdktf.IResolvable],
        udp: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param tcp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tcp TeamsAccount#tcp}.
        :param udp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#udp TeamsAccount#udp}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountProxy.__init__)
            check_type(argname="argument tcp", value=tcp, expected_type=type_hints["tcp"])
            check_type(argname="argument udp", value=udp, expected_type=type_hints["udp"])
        self._values: typing.Dict[str, typing.Any] = {
            "tcp": tcp,
            "udp": udp,
        }

    @builtins.property
    def tcp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#tcp TeamsAccount#tcp}.'''
        result = self._values.get("tcp")
        assert result is not None, "Required property 'tcp' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def udp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/teams_account#udp TeamsAccount#udp}.'''
        result = self._values.get("udp")
        assert result is not None, "Required property 'udp' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamsAccountProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TeamsAccountProxyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.teamsAccount.TeamsAccountProxyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TeamsAccountProxyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tcpInput")
    def tcp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tcpInput"))

    @builtins.property
    @jsii.member(jsii_name="udpInput")
    def udp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "udpInput"))

    @builtins.property
    @jsii.member(jsii_name="tcp")
    def tcp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tcp"))

    @tcp.setter
    def tcp(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountProxyOutputReference, "tcp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tcp", value)

    @builtins.property
    @jsii.member(jsii_name="udp")
    def udp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "udp"))

    @udp.setter
    def udp(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountProxyOutputReference, "udp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "udp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TeamsAccountProxy]:
        return typing.cast(typing.Optional[TeamsAccountProxy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TeamsAccountProxy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TeamsAccountProxyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TeamsAccount",
    "TeamsAccountAntivirus",
    "TeamsAccountAntivirusOutputReference",
    "TeamsAccountBlockPage",
    "TeamsAccountBlockPageOutputReference",
    "TeamsAccountConfig",
    "TeamsAccountFips",
    "TeamsAccountFipsOutputReference",
    "TeamsAccountLogging",
    "TeamsAccountLoggingOutputReference",
    "TeamsAccountLoggingSettingsByRuleType",
    "TeamsAccountLoggingSettingsByRuleTypeDns",
    "TeamsAccountLoggingSettingsByRuleTypeDnsOutputReference",
    "TeamsAccountLoggingSettingsByRuleTypeHttp",
    "TeamsAccountLoggingSettingsByRuleTypeHttpOutputReference",
    "TeamsAccountLoggingSettingsByRuleTypeL4",
    "TeamsAccountLoggingSettingsByRuleTypeL4OutputReference",
    "TeamsAccountLoggingSettingsByRuleTypeOutputReference",
    "TeamsAccountProxy",
    "TeamsAccountProxyOutputReference",
]

publication.publish()
