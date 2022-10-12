'''
# `provider`

Refer to the Terraform Registory for docs: [`newrelic`](https://www.terraform.io/docs/providers/newrelic).
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


class NewrelicProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.provider.NewrelicProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic newrelic}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account_id: jsii.Number,
        admin_api_key: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        infrastructure_api_url: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        insights_insert_key: typing.Optional[builtins.str] = None,
        insights_insert_url: typing.Optional[builtins.str] = None,
        insights_query_url: typing.Optional[builtins.str] = None,
        nerdgraph_api_url: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        synthetics_api_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic newrelic} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#account_id NewrelicProvider#account_id}.
        :param admin_api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#admin_api_key NewrelicProvider#admin_api_key}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#alias NewrelicProvider#alias}
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#api_key NewrelicProvider#api_key}.
        :param api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#api_url NewrelicProvider#api_url}.
        :param cacert_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#cacert_file NewrelicProvider#cacert_file}.
        :param infrastructure_api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#infrastructure_api_url NewrelicProvider#infrastructure_api_url}.
        :param insecure_skip_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insecure_skip_verify NewrelicProvider#insecure_skip_verify}.
        :param insights_insert_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_insert_key NewrelicProvider#insights_insert_key}.
        :param insights_insert_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_insert_url NewrelicProvider#insights_insert_url}.
        :param insights_query_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_query_url NewrelicProvider#insights_query_url}.
        :param nerdgraph_api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#nerdgraph_api_url NewrelicProvider#nerdgraph_api_url}.
        :param region: The data center for which your New Relic account is configured. Only one region per provider block is permitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#region NewrelicProvider#region}
        :param synthetics_api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#synthetics_api_url NewrelicProvider#synthetics_api_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NewrelicProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = NewrelicProviderConfig(
            account_id=account_id,
            admin_api_key=admin_api_key,
            alias=alias,
            api_key=api_key,
            api_url=api_url,
            cacert_file=cacert_file,
            infrastructure_api_url=infrastructure_api_url,
            insecure_skip_verify=insecure_skip_verify,
            insights_insert_key=insights_insert_key,
            insights_insert_url=insights_insert_url,
            insights_query_url=insights_query_url,
            nerdgraph_api_url=nerdgraph_api_url,
            region=region,
            synthetics_api_url=synthetics_api_url,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAdminApiKey")
    def reset_admin_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminApiKey", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetApiUrl")
    def reset_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiUrl", []))

    @jsii.member(jsii_name="resetCacertFile")
    def reset_cacert_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacertFile", []))

    @jsii.member(jsii_name="resetInfrastructureApiUrl")
    def reset_infrastructure_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInfrastructureApiUrl", []))

    @jsii.member(jsii_name="resetInsecureSkipVerify")
    def reset_insecure_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipVerify", []))

    @jsii.member(jsii_name="resetInsightsInsertKey")
    def reset_insights_insert_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsightsInsertKey", []))

    @jsii.member(jsii_name="resetInsightsInsertUrl")
    def reset_insights_insert_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsightsInsertUrl", []))

    @jsii.member(jsii_name="resetInsightsQueryUrl")
    def reset_insights_query_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsightsQueryUrl", []))

    @jsii.member(jsii_name="resetNerdgraphApiUrl")
    def reset_nerdgraph_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNerdgraphApiUrl", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSyntheticsApiUrl")
    def reset_synthetics_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyntheticsApiUrl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="adminApiKeyInput")
    def admin_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiUrlInput")
    def api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="cacertFileInput")
    def cacert_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacertFileInput"))

    @builtins.property
    @jsii.member(jsii_name="infrastructureApiUrlInput")
    def infrastructure_api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "infrastructureApiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerifyInput")
    def insecure_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="insightsInsertKeyInput")
    def insights_insert_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsInsertKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="insightsInsertUrlInput")
    def insights_insert_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsInsertUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="insightsQueryUrlInput")
    def insights_query_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsQueryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nerdgraphApiUrlInput")
    def nerdgraph_api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nerdgraphApiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="syntheticsApiUrlInput")
    def synthetics_api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syntheticsApiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="adminApiKey")
    def admin_api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminApiKey"))

    @admin_api_key.setter
    def admin_api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "admin_api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiUrl")
    def api_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiUrl"))

    @api_url.setter
    def api_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "api_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="cacertFile")
    def cacert_file(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacertFile"))

    @cacert_file.setter
    def cacert_file(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "cacert_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacertFile", value)

    @builtins.property
    @jsii.member(jsii_name="infrastructureApiUrl")
    def infrastructure_api_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "infrastructureApiUrl"))

    @infrastructure_api_url.setter
    def infrastructure_api_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "infrastructure_api_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureApiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerify")
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insecureSkipVerify"))

    @insecure_skip_verify.setter
    def insecure_skip_verify(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "insecure_skip_verify").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="insightsInsertKey")
    def insights_insert_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsInsertKey"))

    @insights_insert_key.setter
    def insights_insert_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "insights_insert_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightsInsertKey", value)

    @builtins.property
    @jsii.member(jsii_name="insightsInsertUrl")
    def insights_insert_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsInsertUrl"))

    @insights_insert_url.setter
    def insights_insert_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "insights_insert_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightsInsertUrl", value)

    @builtins.property
    @jsii.member(jsii_name="insightsQueryUrl")
    def insights_query_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "insightsQueryUrl"))

    @insights_query_url.setter
    def insights_query_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "insights_query_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insightsQueryUrl", value)

    @builtins.property
    @jsii.member(jsii_name="nerdgraphApiUrl")
    def nerdgraph_api_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nerdgraphApiUrl"))

    @nerdgraph_api_url.setter
    def nerdgraph_api_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "nerdgraph_api_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nerdgraphApiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="syntheticsApiUrl")
    def synthetics_api_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syntheticsApiUrl"))

    @synthetics_api_url.setter
    def synthetics_api_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NewrelicProvider, "synthetics_api_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syntheticsApiUrl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.provider.NewrelicProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "admin_api_key": "adminApiKey",
        "alias": "alias",
        "api_key": "apiKey",
        "api_url": "apiUrl",
        "cacert_file": "cacertFile",
        "infrastructure_api_url": "infrastructureApiUrl",
        "insecure_skip_verify": "insecureSkipVerify",
        "insights_insert_key": "insightsInsertKey",
        "insights_insert_url": "insightsInsertUrl",
        "insights_query_url": "insightsQueryUrl",
        "nerdgraph_api_url": "nerdgraphApiUrl",
        "region": "region",
        "synthetics_api_url": "syntheticsApiUrl",
    },
)
class NewrelicProviderConfig:
    def __init__(
        self,
        *,
        account_id: jsii.Number,
        admin_api_key: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        api_key: typing.Optional[builtins.str] = None,
        api_url: typing.Optional[builtins.str] = None,
        cacert_file: typing.Optional[builtins.str] = None,
        infrastructure_api_url: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        insights_insert_key: typing.Optional[builtins.str] = None,
        insights_insert_url: typing.Optional[builtins.str] = None,
        insights_query_url: typing.Optional[builtins.str] = None,
        nerdgraph_api_url: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        synthetics_api_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#account_id NewrelicProvider#account_id}.
        :param admin_api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#admin_api_key NewrelicProvider#admin_api_key}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#alias NewrelicProvider#alias}
        :param api_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#api_key NewrelicProvider#api_key}.
        :param api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#api_url NewrelicProvider#api_url}.
        :param cacert_file: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#cacert_file NewrelicProvider#cacert_file}.
        :param infrastructure_api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#infrastructure_api_url NewrelicProvider#infrastructure_api_url}.
        :param insecure_skip_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insecure_skip_verify NewrelicProvider#insecure_skip_verify}.
        :param insights_insert_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_insert_key NewrelicProvider#insights_insert_key}.
        :param insights_insert_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_insert_url NewrelicProvider#insights_insert_url}.
        :param insights_query_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_query_url NewrelicProvider#insights_query_url}.
        :param nerdgraph_api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#nerdgraph_api_url NewrelicProvider#nerdgraph_api_url}.
        :param region: The data center for which your New Relic account is configured. Only one region per provider block is permitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#region NewrelicProvider#region}
        :param synthetics_api_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#synthetics_api_url NewrelicProvider#synthetics_api_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NewrelicProviderConfig.__init__)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument admin_api_key", value=admin_api_key, expected_type=type_hints["admin_api_key"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument api_url", value=api_url, expected_type=type_hints["api_url"])
            check_type(argname="argument cacert_file", value=cacert_file, expected_type=type_hints["cacert_file"])
            check_type(argname="argument infrastructure_api_url", value=infrastructure_api_url, expected_type=type_hints["infrastructure_api_url"])
            check_type(argname="argument insecure_skip_verify", value=insecure_skip_verify, expected_type=type_hints["insecure_skip_verify"])
            check_type(argname="argument insights_insert_key", value=insights_insert_key, expected_type=type_hints["insights_insert_key"])
            check_type(argname="argument insights_insert_url", value=insights_insert_url, expected_type=type_hints["insights_insert_url"])
            check_type(argname="argument insights_query_url", value=insights_query_url, expected_type=type_hints["insights_query_url"])
            check_type(argname="argument nerdgraph_api_url", value=nerdgraph_api_url, expected_type=type_hints["nerdgraph_api_url"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument synthetics_api_url", value=synthetics_api_url, expected_type=type_hints["synthetics_api_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
        }
        if admin_api_key is not None:
            self._values["admin_api_key"] = admin_api_key
        if alias is not None:
            self._values["alias"] = alias
        if api_key is not None:
            self._values["api_key"] = api_key
        if api_url is not None:
            self._values["api_url"] = api_url
        if cacert_file is not None:
            self._values["cacert_file"] = cacert_file
        if infrastructure_api_url is not None:
            self._values["infrastructure_api_url"] = infrastructure_api_url
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if insights_insert_key is not None:
            self._values["insights_insert_key"] = insights_insert_key
        if insights_insert_url is not None:
            self._values["insights_insert_url"] = insights_insert_url
        if insights_query_url is not None:
            self._values["insights_query_url"] = insights_query_url
        if nerdgraph_api_url is not None:
            self._values["nerdgraph_api_url"] = nerdgraph_api_url
        if region is not None:
            self._values["region"] = region
        if synthetics_api_url is not None:
            self._values["synthetics_api_url"] = synthetics_api_url

    @builtins.property
    def account_id(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#account_id NewrelicProvider#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def admin_api_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#admin_api_key NewrelicProvider#admin_api_key}.'''
        result = self._values.get("admin_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#alias NewrelicProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#api_key NewrelicProvider#api_key}.'''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#api_url NewrelicProvider#api_url}.'''
        result = self._values.get("api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cacert_file(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#cacert_file NewrelicProvider#cacert_file}.'''
        result = self._values.get("cacert_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def infrastructure_api_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#infrastructure_api_url NewrelicProvider#infrastructure_api_url}.'''
        result = self._values.get("infrastructure_api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insecure_skip_verify NewrelicProvider#insecure_skip_verify}.'''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def insights_insert_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_insert_key NewrelicProvider#insights_insert_key}.'''
        result = self._values.get("insights_insert_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insights_insert_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_insert_url NewrelicProvider#insights_insert_url}.'''
        result = self._values.get("insights_insert_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insights_query_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#insights_query_url NewrelicProvider#insights_query_url}.'''
        result = self._values.get("insights_query_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nerdgraph_api_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#nerdgraph_api_url NewrelicProvider#nerdgraph_api_url}.'''
        result = self._values.get("nerdgraph_api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The data center for which your New Relic account is configured. Only one region per provider block is permitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#region NewrelicProvider#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthetics_api_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic#synthetics_api_url NewrelicProvider#synthetics_api_url}.'''
        result = self._values.get("synthetics_api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NewrelicProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "NewrelicProvider",
    "NewrelicProviderConfig",
]

publication.publish()
