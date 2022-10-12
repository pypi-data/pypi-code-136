'''
# `cloudflare_ruleset`

Refer to the Terraform Registory for docs: [`cloudflare_ruleset`](https://www.terraform.io/docs/providers/cloudflare/r/ruleset).
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


class Ruleset(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.Ruleset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset cloudflare_ruleset}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        kind: builtins.str,
        name: builtins.str,
        phase: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRules", typing.Dict[str, typing.Any]]]]] = None,
        shareable_entitlement_name: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset cloudflare_ruleset} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param kind: Type of Ruleset to create. Available values: ``custom``, ``managed``, ``root``, ``schema``, ``zone``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#kind Ruleset#kind}
        :param name: Name of the ruleset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        :param phase: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_request_cache_settings``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_late_transform_managed``, ``http_request_main``, ``http_request_origin``, ``http_request_dynamic_redirect``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``http_response_headers_transform_managed``, ``magic_transit``, ``http_ratelimit``, ``http_request_sbfm``, ``http_config_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#phase Ruleset#phase}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#account_id Ruleset#account_id}
        :param description: Brief summary of the ruleset and its intended use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#description Ruleset#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        :param shareable_entitlement_name: Name of entitlement that is shareable between entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#shareable_entitlement_name Ruleset#shareable_entitlement_name}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#zone_id Ruleset#zone_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ruleset.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RulesetConfig(
            kind=kind,
            name=name,
            phase=phase,
            account_id=account_id,
            description=description,
            id=id,
            rules=rules,
            shareable_entitlement_name=shareable_entitlement_name,
            zone_id=zone_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Ruleset.put_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetShareableEntitlementName")
    def reset_shareable_entitlement_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShareableEntitlementName", []))

    @jsii.member(jsii_name="resetZoneId")
    def reset_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "RulesetRulesList":
        return typing.cast("RulesetRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="phaseInput")
    def phase_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phaseInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="shareableEntitlementNameInput")
    def shareable_entitlement_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareableEntitlementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phase")
    def phase(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phase"))

    @phase.setter
    def phase(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "phase").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phase", value)

    @builtins.property
    @jsii.member(jsii_name="shareableEntitlementName")
    def shareable_entitlement_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareableEntitlementName"))

    @shareable_entitlement_name.setter
    def shareable_entitlement_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "shareable_entitlement_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareableEntitlementName", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Ruleset, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "kind": "kind",
        "name": "name",
        "phase": "phase",
        "account_id": "accountId",
        "description": "description",
        "id": "id",
        "rules": "rules",
        "shareable_entitlement_name": "shareableEntitlementName",
        "zone_id": "zoneId",
    },
)
class RulesetConfig(cdktf.TerraformMetaArguments):
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
        kind: builtins.str,
        name: builtins.str,
        phase: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRules", typing.Dict[str, typing.Any]]]]] = None,
        shareable_entitlement_name: typing.Optional[builtins.str] = None,
        zone_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param kind: Type of Ruleset to create. Available values: ``custom``, ``managed``, ``root``, ``schema``, ``zone``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#kind Ruleset#kind}
        :param name: Name of the ruleset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        :param phase: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_request_cache_settings``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_late_transform_managed``, ``http_request_main``, ``http_request_origin``, ``http_request_dynamic_redirect``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``http_response_headers_transform_managed``, ``magic_transit``, ``http_ratelimit``, ``http_request_sbfm``, ``http_config_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#phase Ruleset#phase}
        :param account_id: The account identifier to target for the resource. Conflicts with ``zone_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#account_id Ruleset#account_id}
        :param description: Brief summary of the ruleset and its intended use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#description Ruleset#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        :param shareable_entitlement_name: Name of entitlement that is shareable between entities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#shareable_entitlement_name Ruleset#shareable_entitlement_name}
        :param zone_id: The zone identifier to target for the resource. Conflicts with ``account_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#zone_id Ruleset#zone_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phase", value=phase, expected_type=type_hints["phase"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument shareable_entitlement_name", value=shareable_entitlement_name, expected_type=type_hints["shareable_entitlement_name"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
            "phase": phase,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if rules is not None:
            self._values["rules"] = rules
        if shareable_entitlement_name is not None:
            self._values["shareable_entitlement_name"] = shareable_entitlement_name
        if zone_id is not None:
            self._values["zone_id"] = zone_id

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
    def kind(self) -> builtins.str:
        '''Type of Ruleset to create. Available values: ``custom``, ``managed``, ``root``, ``schema``, ``zone``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#kind Ruleset#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the ruleset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phase(self) -> builtins.str:
        '''Point in the request/response lifecycle where the ruleset will be created.

        Available values: ``ddos_l4``, ``ddos_l7``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_request_cache_settings``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_late_transform_managed``, ``http_request_main``, ``http_request_origin``, ``http_request_dynamic_redirect``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``http_response_headers_transform_managed``, ``magic_transit``, ``http_ratelimit``, ``http_request_sbfm``, ``http_config_settings``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#phase Ruleset#phase}
        '''
        result = self._values.get("phase")
        assert result is not None, "Required property 'phase' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The account identifier to target for the resource. Conflicts with ``zone_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#account_id Ruleset#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Brief summary of the ruleset and its intended use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#description Ruleset#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRules"]]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRules"]]], result)

    @builtins.property
    def shareable_entitlement_name(self) -> typing.Optional[builtins.str]:
        '''Name of entitlement that is shareable between entities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#shareable_entitlement_name Ruleset#shareable_entitlement_name}
        '''
        result = self._values.get("shareable_entitlement_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_id(self) -> typing.Optional[builtins.str]:
        '''The zone identifier to target for the resource. Conflicts with ``account_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#zone_id Ruleset#zone_id}
        '''
        result = self._values.get("zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRules",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "action": "action",
        "action_parameters": "actionParameters",
        "description": "description",
        "enabled": "enabled",
        "exposed_credential_check": "exposedCredentialCheck",
        "logging": "logging",
        "ratelimit": "ratelimit",
    },
)
class RulesetRules:
    def __init__(
        self,
        *,
        expression: builtins.str,
        action: typing.Optional[builtins.str] = None,
        action_parameters: typing.Optional[typing.Union["RulesetRulesActionParameters", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exposed_credential_check: typing.Optional[typing.Union["RulesetRulesExposedCredentialCheck", typing.Dict[str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["RulesetRulesLogging", typing.Dict[str, typing.Any]]] = None,
        ratelimit: typing.Optional[typing.Union["RulesetRulesRatelimit", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param expression: Criteria for an HTTP request to trigger the ruleset rule action. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param action: Action to perform in the ruleset rule. Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        :param action_parameters: action_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action_parameters Ruleset#action_parameters}
        :param description: Brief summary of the ruleset rule and its intended use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#description Ruleset#description}
        :param enabled: Whether the rule is active. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param exposed_credential_check: exposed_credential_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exposed_credential_check Ruleset#exposed_credential_check}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#logging Ruleset#logging}
        :param ratelimit: ratelimit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ratelimit Ruleset#ratelimit}
        '''
        if isinstance(action_parameters, dict):
            action_parameters = RulesetRulesActionParameters(**action_parameters)
        if isinstance(exposed_credential_check, dict):
            exposed_credential_check = RulesetRulesExposedCredentialCheck(**exposed_credential_check)
        if isinstance(logging, dict):
            logging = RulesetRulesLogging(**logging)
        if isinstance(ratelimit, dict):
            ratelimit = RulesetRulesRatelimit(**ratelimit)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRules.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument action_parameters", value=action_parameters, expected_type=type_hints["action_parameters"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument exposed_credential_check", value=exposed_credential_check, expected_type=type_hints["exposed_credential_check"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument ratelimit", value=ratelimit, expected_type=type_hints["ratelimit"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }
        if action is not None:
            self._values["action"] = action
        if action_parameters is not None:
            self._values["action_parameters"] = action_parameters
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if exposed_credential_check is not None:
            self._values["exposed_credential_check"] = exposed_credential_check
        if logging is not None:
            self._values["logging"] = logging
        if ratelimit is not None:
            self._values["ratelimit"] = ratelimit

    @builtins.property
    def expression(self) -> builtins.str:
        '''Criteria for an HTTP request to trigger the ruleset rule action.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the ruleset rule.

        Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_parameters(self) -> typing.Optional["RulesetRulesActionParameters"]:
        '''action_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action_parameters Ruleset#action_parameters}
        '''
        result = self._values.get("action_parameters")
        return typing.cast(typing.Optional["RulesetRulesActionParameters"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Brief summary of the ruleset rule and its intended use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#description Ruleset#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the rule is active.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exposed_credential_check(
        self,
    ) -> typing.Optional["RulesetRulesExposedCredentialCheck"]:
        '''exposed_credential_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exposed_credential_check Ruleset#exposed_credential_check}
        '''
        result = self._values.get("exposed_credential_check")
        return typing.cast(typing.Optional["RulesetRulesExposedCredentialCheck"], result)

    @builtins.property
    def logging(self) -> typing.Optional["RulesetRulesLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#logging Ruleset#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["RulesetRulesLogging"], result)

    @builtins.property
    def ratelimit(self) -> typing.Optional["RulesetRulesRatelimit"]:
        '''ratelimit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ratelimit Ruleset#ratelimit}
        '''
        result = self._values.get("ratelimit")
        return typing.cast(typing.Optional["RulesetRulesRatelimit"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParameters",
    jsii_struct_bases=[],
    name_mapping={
        "automatic_https_rewrites": "automaticHttpsRewrites",
        "autominify": "autominify",
        "bic": "bic",
        "browser_ttl": "browserTtl",
        "cache": "cache",
        "cache_key": "cacheKey",
        "content": "content",
        "content_type": "contentType",
        "cookie_fields": "cookieFields",
        "disable_apps": "disableApps",
        "disable_railgun": "disableRailgun",
        "disable_zaraz": "disableZaraz",
        "edge_ttl": "edgeTtl",
        "email_obfuscation": "emailObfuscation",
        "from_list": "fromList",
        "from_value": "fromValue",
        "headers": "headers",
        "host_header": "hostHeader",
        "hotlink_protection": "hotlinkProtection",
        "id": "id",
        "increment": "increment",
        "matched_data": "matchedData",
        "mirage": "mirage",
        "opportunistic_encryption": "opportunisticEncryption",
        "origin": "origin",
        "origin_error_page_passthru": "originErrorPagePassthru",
        "overrides": "overrides",
        "phases": "phases",
        "polish": "polish",
        "products": "products",
        "request_fields": "requestFields",
        "respect_strong_etags": "respectStrongEtags",
        "response": "response",
        "response_fields": "responseFields",
        "rocket_loader": "rocketLoader",
        "rules": "rules",
        "ruleset": "ruleset",
        "rulesets": "rulesets",
        "security_level": "securityLevel",
        "server_side_excludes": "serverSideExcludes",
        "serve_stale": "serveStale",
        "sni": "sni",
        "ssl": "ssl",
        "status_code": "statusCode",
        "sxg": "sxg",
        "uri": "uri",
        "version": "version",
    },
)
class RulesetRulesActionParameters:
    def __init__(
        self,
        *,
        automatic_https_rewrites: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autominify: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersAutominify", typing.Dict[str, typing.Any]]]]] = None,
        bic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        browser_ttl: typing.Optional[typing.Union["RulesetRulesActionParametersBrowserTtl", typing.Dict[str, typing.Any]]] = None,
        cache: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_key: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKey", typing.Dict[str, typing.Any]]] = None,
        content: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        cookie_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        disable_apps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_railgun: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_zaraz: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_ttl: typing.Optional[typing.Union["RulesetRulesActionParametersEdgeTtl", typing.Dict[str, typing.Any]]] = None,
        email_obfuscation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        from_list: typing.Optional[typing.Union["RulesetRulesActionParametersFromList", typing.Dict[str, typing.Any]]] = None,
        from_value: typing.Optional[typing.Union["RulesetRulesActionParametersFromValue", typing.Dict[str, typing.Any]]] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersHeaders", typing.Dict[str, typing.Any]]]]] = None,
        host_header: typing.Optional[builtins.str] = None,
        hotlink_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        increment: typing.Optional[jsii.Number] = None,
        matched_data: typing.Optional[typing.Union["RulesetRulesActionParametersMatchedData", typing.Dict[str, typing.Any]]] = None,
        mirage: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        opportunistic_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        origin: typing.Optional[typing.Union["RulesetRulesActionParametersOrigin", typing.Dict[str, typing.Any]]] = None,
        origin_error_page_passthru: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        overrides: typing.Optional[typing.Union["RulesetRulesActionParametersOverrides", typing.Dict[str, typing.Any]]] = None,
        phases: typing.Optional[typing.Sequence[builtins.str]] = None,
        polish: typing.Optional[builtins.str] = None,
        products: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        respect_strong_etags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        response: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersResponse", typing.Dict[str, typing.Any]]]]] = None,
        response_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        rocket_loader: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rules: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ruleset: typing.Optional[builtins.str] = None,
        rulesets: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_excludes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        serve_stale: typing.Optional[typing.Union["RulesetRulesActionParametersServeStale", typing.Dict[str, typing.Any]]] = None,
        sni: typing.Optional[typing.Union["RulesetRulesActionParametersSni", typing.Dict[str, typing.Any]]] = None,
        ssl: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
        sxg: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uri: typing.Optional[typing.Union["RulesetRulesActionParametersUri", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param automatic_https_rewrites: Turn on or off Cloudflare Automatic HTTPS rewrites. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#automatic_https_rewrites Ruleset#automatic_https_rewrites}
        :param autominify: autominify block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#autominify Ruleset#autominify}
        :param bic: Inspect the visitor's browser for headers commonly associated with spammers and certain bots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#bic Ruleset#bic}
        :param browser_ttl: browser_ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#browser_ttl Ruleset#browser_ttl}
        :param cache: Whether to cache if expression matches. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache Ruleset#cache}
        :param cache_key: cache_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_key Ruleset#cache_key}
        :param content: Content of the custom error response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content Ruleset#content}
        :param content_type: Content-Type of the custom error response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content_type Ruleset#content_type}
        :param cookie_fields: List of cookie values to include as part of custom fields logging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cookie_fields Ruleset#cookie_fields}
        :param disable_apps: Turn off all active Cloudflare Apps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_apps Ruleset#disable_apps}
        :param disable_railgun: Turn off railgun feature of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_railgun Ruleset#disable_railgun}
        :param disable_zaraz: Turn off zaraz feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_zaraz Ruleset#disable_zaraz}
        :param edge_ttl: edge_ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#edge_ttl Ruleset#edge_ttl}
        :param email_obfuscation: Turn on or off the Cloudflare Email Obfuscation feature of the Cloudflare Scrape Shield app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#email_obfuscation Ruleset#email_obfuscation}
        :param from_list: from_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from_list Ruleset#from_list}
        :param from_value: from_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from_value Ruleset#from_value}
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#headers Ruleset#headers}
        :param host_header: Host Header that request origin receives. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host_header Ruleset#host_header}
        :param hotlink_protection: Turn on or off the hotlink protection feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#hotlink_protection Ruleset#hotlink_protection}
        :param id: Identifier of the action parameter to modify. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param increment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#increment Ruleset#increment}.
        :param matched_data: matched_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#matched_data Ruleset#matched_data}
        :param mirage: Turn on or off Cloudflare Mirage of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mirage Ruleset#mirage}
        :param opportunistic_encryption: Turn on or off the Cloudflare Opportunistic Encryption feature of the Edge Certificates tab in the Cloudflare SSL/TLS app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#opportunistic_encryption Ruleset#opportunistic_encryption}
        :param origin: origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin Ruleset#origin}
        :param origin_error_page_passthru: Pass-through error page for origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin_error_page_passthru Ruleset#origin_error_page_passthru}
        :param overrides: overrides block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#overrides Ruleset#overrides}
        :param phases: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_request_cache_settings``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_late_transform_managed``, ``http_request_main``, ``http_request_origin``, ``http_request_dynamic_redirect``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``http_response_headers_transform_managed``, ``magic_transit``, ``http_ratelimit``, ``http_request_sbfm``, ``http_config_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#phases Ruleset#phases}
        :param polish: Apply options from the Polish feature of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#polish Ruleset#polish}
        :param products: Products to target with the actions. Available values: ``bic``, ``hot``, ``ratelimit``, ``securityLevel``, ``uablock``, ``waf``, ``zonelockdown``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#products Ruleset#products}
        :param request_fields: List of request headers to include as part of custom fields logging, in lowercase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#request_fields Ruleset#request_fields}
        :param respect_strong_etags: Respect strong ETags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#respect_strong_etags Ruleset#respect_strong_etags}
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#response Ruleset#response}
        :param response_fields: List of response headers to include as part of custom fields logging, in lowercase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#response_fields Ruleset#response_fields}
        :param rocket_loader: Turn on or off Cloudflare Rocket Loader in the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rocket_loader Ruleset#rocket_loader}
        :param rules: Map of managed WAF rule ID to comma-delimited string of ruleset rule IDs. Example: ``rules = { "efb7b8c949ac4650a09736fc376e9aee" = "5de7edfa648c4d6891dc3e7f84534ffa,e3a567afc347477d9702d9047e97d760" }``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        :param ruleset: Which ruleset ID to target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ruleset Ruleset#ruleset}
        :param rulesets: List of managed WAF rule IDs to target. Only valid when the ``"action"`` is set to skip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rulesets Ruleset#rulesets}
        :param security_level: Control options for the Security Level feature from the Security app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#security_level Ruleset#security_level}
        :param server_side_excludes: Turn on or off the Server Side Excludes feature of the Cloudflare Scrape Shield app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#server_side_excludes Ruleset#server_side_excludes}
        :param serve_stale: serve_stale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#serve_stale Ruleset#serve_stale}
        :param sni: sni block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sni Ruleset#sni}
        :param ssl: Control options for the SSL feature of the Edge Certificates tab in the Cloudflare SSL/TLS app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ssl Ruleset#ssl}
        :param status_code: HTTP status code of the custom error response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        :param sxg: Turn on or off the SXG feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sxg Ruleset#sxg}
        :param uri: uri block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#uri Ruleset#uri}
        :param version: Version of the ruleset to deploy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#version Ruleset#version}
        '''
        if isinstance(browser_ttl, dict):
            browser_ttl = RulesetRulesActionParametersBrowserTtl(**browser_ttl)
        if isinstance(cache_key, dict):
            cache_key = RulesetRulesActionParametersCacheKey(**cache_key)
        if isinstance(edge_ttl, dict):
            edge_ttl = RulesetRulesActionParametersEdgeTtl(**edge_ttl)
        if isinstance(from_list, dict):
            from_list = RulesetRulesActionParametersFromList(**from_list)
        if isinstance(from_value, dict):
            from_value = RulesetRulesActionParametersFromValue(**from_value)
        if isinstance(matched_data, dict):
            matched_data = RulesetRulesActionParametersMatchedData(**matched_data)
        if isinstance(origin, dict):
            origin = RulesetRulesActionParametersOrigin(**origin)
        if isinstance(overrides, dict):
            overrides = RulesetRulesActionParametersOverrides(**overrides)
        if isinstance(serve_stale, dict):
            serve_stale = RulesetRulesActionParametersServeStale(**serve_stale)
        if isinstance(sni, dict):
            sni = RulesetRulesActionParametersSni(**sni)
        if isinstance(uri, dict):
            uri = RulesetRulesActionParametersUri(**uri)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParameters.__init__)
            check_type(argname="argument automatic_https_rewrites", value=automatic_https_rewrites, expected_type=type_hints["automatic_https_rewrites"])
            check_type(argname="argument autominify", value=autominify, expected_type=type_hints["autominify"])
            check_type(argname="argument bic", value=bic, expected_type=type_hints["bic"])
            check_type(argname="argument browser_ttl", value=browser_ttl, expected_type=type_hints["browser_ttl"])
            check_type(argname="argument cache", value=cache, expected_type=type_hints["cache"])
            check_type(argname="argument cache_key", value=cache_key, expected_type=type_hints["cache_key"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument cookie_fields", value=cookie_fields, expected_type=type_hints["cookie_fields"])
            check_type(argname="argument disable_apps", value=disable_apps, expected_type=type_hints["disable_apps"])
            check_type(argname="argument disable_railgun", value=disable_railgun, expected_type=type_hints["disable_railgun"])
            check_type(argname="argument disable_zaraz", value=disable_zaraz, expected_type=type_hints["disable_zaraz"])
            check_type(argname="argument edge_ttl", value=edge_ttl, expected_type=type_hints["edge_ttl"])
            check_type(argname="argument email_obfuscation", value=email_obfuscation, expected_type=type_hints["email_obfuscation"])
            check_type(argname="argument from_list", value=from_list, expected_type=type_hints["from_list"])
            check_type(argname="argument from_value", value=from_value, expected_type=type_hints["from_value"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument hotlink_protection", value=hotlink_protection, expected_type=type_hints["hotlink_protection"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument increment", value=increment, expected_type=type_hints["increment"])
            check_type(argname="argument matched_data", value=matched_data, expected_type=type_hints["matched_data"])
            check_type(argname="argument mirage", value=mirage, expected_type=type_hints["mirage"])
            check_type(argname="argument opportunistic_encryption", value=opportunistic_encryption, expected_type=type_hints["opportunistic_encryption"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument origin_error_page_passthru", value=origin_error_page_passthru, expected_type=type_hints["origin_error_page_passthru"])
            check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
            check_type(argname="argument phases", value=phases, expected_type=type_hints["phases"])
            check_type(argname="argument polish", value=polish, expected_type=type_hints["polish"])
            check_type(argname="argument products", value=products, expected_type=type_hints["products"])
            check_type(argname="argument request_fields", value=request_fields, expected_type=type_hints["request_fields"])
            check_type(argname="argument respect_strong_etags", value=respect_strong_etags, expected_type=type_hints["respect_strong_etags"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
            check_type(argname="argument response_fields", value=response_fields, expected_type=type_hints["response_fields"])
            check_type(argname="argument rocket_loader", value=rocket_loader, expected_type=type_hints["rocket_loader"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument ruleset", value=ruleset, expected_type=type_hints["ruleset"])
            check_type(argname="argument rulesets", value=rulesets, expected_type=type_hints["rulesets"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument server_side_excludes", value=server_side_excludes, expected_type=type_hints["server_side_excludes"])
            check_type(argname="argument serve_stale", value=serve_stale, expected_type=type_hints["serve_stale"])
            check_type(argname="argument sni", value=sni, expected_type=type_hints["sni"])
            check_type(argname="argument ssl", value=ssl, expected_type=type_hints["ssl"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument sxg", value=sxg, expected_type=type_hints["sxg"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if automatic_https_rewrites is not None:
            self._values["automatic_https_rewrites"] = automatic_https_rewrites
        if autominify is not None:
            self._values["autominify"] = autominify
        if bic is not None:
            self._values["bic"] = bic
        if browser_ttl is not None:
            self._values["browser_ttl"] = browser_ttl
        if cache is not None:
            self._values["cache"] = cache
        if cache_key is not None:
            self._values["cache_key"] = cache_key
        if content is not None:
            self._values["content"] = content
        if content_type is not None:
            self._values["content_type"] = content_type
        if cookie_fields is not None:
            self._values["cookie_fields"] = cookie_fields
        if disable_apps is not None:
            self._values["disable_apps"] = disable_apps
        if disable_railgun is not None:
            self._values["disable_railgun"] = disable_railgun
        if disable_zaraz is not None:
            self._values["disable_zaraz"] = disable_zaraz
        if edge_ttl is not None:
            self._values["edge_ttl"] = edge_ttl
        if email_obfuscation is not None:
            self._values["email_obfuscation"] = email_obfuscation
        if from_list is not None:
            self._values["from_list"] = from_list
        if from_value is not None:
            self._values["from_value"] = from_value
        if headers is not None:
            self._values["headers"] = headers
        if host_header is not None:
            self._values["host_header"] = host_header
        if hotlink_protection is not None:
            self._values["hotlink_protection"] = hotlink_protection
        if id is not None:
            self._values["id"] = id
        if increment is not None:
            self._values["increment"] = increment
        if matched_data is not None:
            self._values["matched_data"] = matched_data
        if mirage is not None:
            self._values["mirage"] = mirage
        if opportunistic_encryption is not None:
            self._values["opportunistic_encryption"] = opportunistic_encryption
        if origin is not None:
            self._values["origin"] = origin
        if origin_error_page_passthru is not None:
            self._values["origin_error_page_passthru"] = origin_error_page_passthru
        if overrides is not None:
            self._values["overrides"] = overrides
        if phases is not None:
            self._values["phases"] = phases
        if polish is not None:
            self._values["polish"] = polish
        if products is not None:
            self._values["products"] = products
        if request_fields is not None:
            self._values["request_fields"] = request_fields
        if respect_strong_etags is not None:
            self._values["respect_strong_etags"] = respect_strong_etags
        if response is not None:
            self._values["response"] = response
        if response_fields is not None:
            self._values["response_fields"] = response_fields
        if rocket_loader is not None:
            self._values["rocket_loader"] = rocket_loader
        if rules is not None:
            self._values["rules"] = rules
        if ruleset is not None:
            self._values["ruleset"] = ruleset
        if rulesets is not None:
            self._values["rulesets"] = rulesets
        if security_level is not None:
            self._values["security_level"] = security_level
        if server_side_excludes is not None:
            self._values["server_side_excludes"] = server_side_excludes
        if serve_stale is not None:
            self._values["serve_stale"] = serve_stale
        if sni is not None:
            self._values["sni"] = sni
        if ssl is not None:
            self._values["ssl"] = ssl
        if status_code is not None:
            self._values["status_code"] = status_code
        if sxg is not None:
            self._values["sxg"] = sxg
        if uri is not None:
            self._values["uri"] = uri
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def automatic_https_rewrites(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off Cloudflare Automatic HTTPS rewrites.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#automatic_https_rewrites Ruleset#automatic_https_rewrites}
        '''
        result = self._values.get("automatic_https_rewrites")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autominify(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersAutominify"]]]:
        '''autominify block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#autominify Ruleset#autominify}
        '''
        result = self._values.get("autominify")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersAutominify"]]], result)

    @builtins.property
    def bic(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Inspect the visitor's browser for headers commonly associated with spammers and certain bots.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#bic Ruleset#bic}
        '''
        result = self._values.get("bic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def browser_ttl(self) -> typing.Optional["RulesetRulesActionParametersBrowserTtl"]:
        '''browser_ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#browser_ttl Ruleset#browser_ttl}
        '''
        result = self._values.get("browser_ttl")
        return typing.cast(typing.Optional["RulesetRulesActionParametersBrowserTtl"], result)

    @builtins.property
    def cache(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to cache if expression matches.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache Ruleset#cache}
        '''
        result = self._values.get("cache")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cache_key(self) -> typing.Optional["RulesetRulesActionParametersCacheKey"]:
        '''cache_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_key Ruleset#cache_key}
        '''
        result = self._values.get("cache_key")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKey"], result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Content of the custom error response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content Ruleset#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Content-Type of the custom error response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content_type Ruleset#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cookie_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of cookie values to include as part of custom fields logging.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cookie_fields Ruleset#cookie_fields}
        '''
        result = self._values.get("cookie_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disable_apps(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn off all active Cloudflare Apps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_apps Ruleset#disable_apps}
        '''
        result = self._values.get("disable_apps")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_railgun(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn off railgun feature of the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_railgun Ruleset#disable_railgun}
        '''
        result = self._values.get("disable_railgun")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_zaraz(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn off zaraz feature.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_zaraz Ruleset#disable_zaraz}
        '''
        result = self._values.get("disable_zaraz")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def edge_ttl(self) -> typing.Optional["RulesetRulesActionParametersEdgeTtl"]:
        '''edge_ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#edge_ttl Ruleset#edge_ttl}
        '''
        result = self._values.get("edge_ttl")
        return typing.cast(typing.Optional["RulesetRulesActionParametersEdgeTtl"], result)

    @builtins.property
    def email_obfuscation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off the Cloudflare Email Obfuscation feature of the Cloudflare Scrape Shield app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#email_obfuscation Ruleset#email_obfuscation}
        '''
        result = self._values.get("email_obfuscation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def from_list(self) -> typing.Optional["RulesetRulesActionParametersFromList"]:
        '''from_list block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from_list Ruleset#from_list}
        '''
        result = self._values.get("from_list")
        return typing.cast(typing.Optional["RulesetRulesActionParametersFromList"], result)

    @builtins.property
    def from_value(self) -> typing.Optional["RulesetRulesActionParametersFromValue"]:
        '''from_value block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from_value Ruleset#from_value}
        '''
        result = self._values.get("from_value")
        return typing.cast(typing.Optional["RulesetRulesActionParametersFromValue"], result)

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#headers Ruleset#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersHeaders"]]], result)

    @builtins.property
    def host_header(self) -> typing.Optional[builtins.str]:
        '''Host Header that request origin receives.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host_header Ruleset#host_header}
        '''
        result = self._values.get("host_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hotlink_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off the hotlink protection feature.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#hotlink_protection Ruleset#hotlink_protection}
        '''
        result = self._values.get("hotlink_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Identifier of the action parameter to modify.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def increment(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#increment Ruleset#increment}.'''
        result = self._values.get("increment")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matched_data(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersMatchedData"]:
        '''matched_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#matched_data Ruleset#matched_data}
        '''
        result = self._values.get("matched_data")
        return typing.cast(typing.Optional["RulesetRulesActionParametersMatchedData"], result)

    @builtins.property
    def mirage(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off Cloudflare Mirage of the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mirage Ruleset#mirage}
        '''
        result = self._values.get("mirage")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def opportunistic_encryption(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off the Cloudflare Opportunistic Encryption feature of the Edge Certificates tab in the Cloudflare SSL/TLS app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#opportunistic_encryption Ruleset#opportunistic_encryption}
        '''
        result = self._values.get("opportunistic_encryption")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def origin(self) -> typing.Optional["RulesetRulesActionParametersOrigin"]:
        '''origin block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin Ruleset#origin}
        '''
        result = self._values.get("origin")
        return typing.cast(typing.Optional["RulesetRulesActionParametersOrigin"], result)

    @builtins.property
    def origin_error_page_passthru(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Pass-through error page for origin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin_error_page_passthru Ruleset#origin_error_page_passthru}
        '''
        result = self._values.get("origin_error_page_passthru")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def overrides(self) -> typing.Optional["RulesetRulesActionParametersOverrides"]:
        '''overrides block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#overrides Ruleset#overrides}
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional["RulesetRulesActionParametersOverrides"], result)

    @builtins.property
    def phases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Point in the request/response lifecycle where the ruleset will be created.

        Available values: ``ddos_l4``, ``ddos_l7``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_request_cache_settings``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_late_transform_managed``, ``http_request_main``, ``http_request_origin``, ``http_request_dynamic_redirect``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``http_response_headers_transform_managed``, ``magic_transit``, ``http_ratelimit``, ``http_request_sbfm``, ``http_config_settings``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#phases Ruleset#phases}
        '''
        result = self._values.get("phases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def polish(self) -> typing.Optional[builtins.str]:
        '''Apply options from the Polish feature of the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#polish Ruleset#polish}
        '''
        result = self._values.get("polish")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def products(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Products to target with the actions. Available values: ``bic``, ``hot``, ``ratelimit``, ``securityLevel``, ``uablock``, ``waf``, ``zonelockdown``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#products Ruleset#products}
        '''
        result = self._values.get("products")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def request_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of request headers to include as part of custom fields logging, in lowercase.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#request_fields Ruleset#request_fields}
        '''
        result = self._values.get("request_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def respect_strong_etags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Respect strong ETags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#respect_strong_etags Ruleset#respect_strong_etags}
        '''
        result = self._values.get("respect_strong_etags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def response(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]]:
        '''response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#response Ruleset#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]], result)

    @builtins.property
    def response_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of response headers to include as part of custom fields logging, in lowercase.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#response_fields Ruleset#response_fields}
        '''
        result = self._values.get("response_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def rocket_loader(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off Cloudflare Rocket Loader in the Cloudflare Speed app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rocket_loader Ruleset#rocket_loader}
        '''
        result = self._values.get("rocket_loader")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of managed WAF rule ID to comma-delimited string of ruleset rule IDs.

        Example: ``rules = { "efb7b8c949ac4650a09736fc376e9aee" = "5de7edfa648c4d6891dc3e7f84534ffa,e3a567afc347477d9702d9047e97d760" }``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ruleset(self) -> typing.Optional[builtins.str]:
        '''Which ruleset ID to target.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ruleset Ruleset#ruleset}
        '''
        result = self._values.get("ruleset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rulesets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of managed WAF rule IDs to target. Only valid when the ``"action"`` is set to skip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rulesets Ruleset#rulesets}
        '''
        result = self._values.get("rulesets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''Control options for the Security Level feature from the Security app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#security_level Ruleset#security_level}
        '''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_excludes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off the Server Side Excludes feature of the Cloudflare Scrape Shield app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#server_side_excludes Ruleset#server_side_excludes}
        '''
        result = self._values.get("server_side_excludes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def serve_stale(self) -> typing.Optional["RulesetRulesActionParametersServeStale"]:
        '''serve_stale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#serve_stale Ruleset#serve_stale}
        '''
        result = self._values.get("serve_stale")
        return typing.cast(typing.Optional["RulesetRulesActionParametersServeStale"], result)

    @builtins.property
    def sni(self) -> typing.Optional["RulesetRulesActionParametersSni"]:
        '''sni block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sni Ruleset#sni}
        '''
        result = self._values.get("sni")
        return typing.cast(typing.Optional["RulesetRulesActionParametersSni"], result)

    @builtins.property
    def ssl(self) -> typing.Optional[builtins.str]:
        '''Control options for the SSL feature of the Edge Certificates tab in the Cloudflare SSL/TLS app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ssl Ruleset#ssl}
        '''
        result = self._values.get("ssl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''HTTP status code of the custom error response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sxg(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Turn on or off the SXG feature.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sxg Ruleset#sxg}
        '''
        result = self._values.get("sxg")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def uri(self) -> typing.Optional["RulesetRulesActionParametersUri"]:
        '''uri block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#uri Ruleset#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional["RulesetRulesActionParametersUri"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version of the ruleset to deploy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#version Ruleset#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAutominify",
    jsii_struct_bases=[],
    name_mapping={"css": "css", "html": "html", "js": "js"},
)
class RulesetRulesActionParametersAutominify:
    def __init__(
        self,
        *,
        css: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        html: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        js: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param css: SSL minification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#css Ruleset#css}
        :param html: HTML minification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#html Ruleset#html}
        :param js: JS minification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#js Ruleset#js}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersAutominify.__init__)
            check_type(argname="argument css", value=css, expected_type=type_hints["css"])
            check_type(argname="argument html", value=html, expected_type=type_hints["html"])
            check_type(argname="argument js", value=js, expected_type=type_hints["js"])
        self._values: typing.Dict[str, typing.Any] = {}
        if css is not None:
            self._values["css"] = css
        if html is not None:
            self._values["html"] = html
        if js is not None:
            self._values["js"] = js

    @builtins.property
    def css(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''SSL minification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#css Ruleset#css}
        '''
        result = self._values.get("css")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def html(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''HTML minification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#html Ruleset#html}
        '''
        result = self._values.get("html")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def js(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''JS minification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#js Ruleset#js}
        '''
        result = self._values.get("js")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersAutominify(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersAutominifyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAutominifyList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersAutominifyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersAutominifyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersAutominifyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersAutominifyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersAutominifyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersAutominifyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersAutominifyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCss")
    def reset_css(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCss", []))

    @jsii.member(jsii_name="resetHtml")
    def reset_html(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHtml", []))

    @jsii.member(jsii_name="resetJs")
    def reset_js(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJs", []))

    @builtins.property
    @jsii.member(jsii_name="cssInput")
    def css_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cssInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlInput")
    def html_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "htmlInput"))

    @builtins.property
    @jsii.member(jsii_name="jsInput")
    def js_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "jsInput"))

    @builtins.property
    @jsii.member(jsii_name="css")
    def css(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "css"))

    @css.setter
    def css(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyOutputReference, "css").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "css", value)

    @builtins.property
    @jsii.member(jsii_name="html")
    def html(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "html"))

    @html.setter
    def html(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyOutputReference, "html").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "html", value)

    @builtins.property
    @jsii.member(jsii_name="js")
    def js(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "js"))

    @js.setter
    def js(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyOutputReference, "js").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "js", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersAutominify, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersAutominify, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersAutominify, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersAutominifyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersBrowserTtl",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "default": "default"},
)
class RulesetRulesActionParametersBrowserTtl:
    def __init__(
        self,
        *,
        mode: builtins.str,
        default: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Mode of the browser TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mode Ruleset#mode}
        :param default: Default browser TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#default Ruleset#default}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersBrowserTtl.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode of the browser TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mode Ruleset#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default(self) -> typing.Optional[jsii.Number]:
        '''Default browser TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#default Ruleset#default}
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersBrowserTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersBrowserTtlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersBrowserTtlOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersBrowserTtlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "default"))

    @default.setter
    def default(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersBrowserTtlOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersBrowserTtlOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersBrowserTtl]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersBrowserTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersBrowserTtl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersBrowserTtlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKey",
    jsii_struct_bases=[],
    name_mapping={
        "cache_by_device_type": "cacheByDeviceType",
        "cache_deception_armor": "cacheDeceptionArmor",
        "custom_key": "customKey",
        "ignore_query_strings_order": "ignoreQueryStringsOrder",
    },
)
class RulesetRulesActionParametersCacheKey:
    def __init__(
        self,
        *,
        cache_by_device_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_deception_armor: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_key: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKeyCustomKey", typing.Dict[str, typing.Any]]] = None,
        ignore_query_strings_order: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cache_by_device_type: Cache by device type. Conflicts with "custom_key.user.device_type". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_by_device_type Ruleset#cache_by_device_type}
        :param cache_deception_armor: Cache deception armor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_deception_armor Ruleset#cache_deception_armor}
        :param custom_key: custom_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#custom_key Ruleset#custom_key}
        :param ignore_query_strings_order: Ignore query strings order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ignore_query_strings_order Ruleset#ignore_query_strings_order}
        '''
        if isinstance(custom_key, dict):
            custom_key = RulesetRulesActionParametersCacheKeyCustomKey(**custom_key)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKey.__init__)
            check_type(argname="argument cache_by_device_type", value=cache_by_device_type, expected_type=type_hints["cache_by_device_type"])
            check_type(argname="argument cache_deception_armor", value=cache_deception_armor, expected_type=type_hints["cache_deception_armor"])
            check_type(argname="argument custom_key", value=custom_key, expected_type=type_hints["custom_key"])
            check_type(argname="argument ignore_query_strings_order", value=ignore_query_strings_order, expected_type=type_hints["ignore_query_strings_order"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cache_by_device_type is not None:
            self._values["cache_by_device_type"] = cache_by_device_type
        if cache_deception_armor is not None:
            self._values["cache_deception_armor"] = cache_deception_armor
        if custom_key is not None:
            self._values["custom_key"] = custom_key
        if ignore_query_strings_order is not None:
            self._values["ignore_query_strings_order"] = ignore_query_strings_order

    @builtins.property
    def cache_by_device_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Cache by device type. Conflicts with "custom_key.user.device_type".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_by_device_type Ruleset#cache_by_device_type}
        '''
        result = self._values.get("cache_by_device_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cache_deception_armor(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Cache deception armor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_deception_armor Ruleset#cache_deception_armor}
        '''
        result = self._values.get("cache_deception_armor")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_key(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKey"]:
        '''custom_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#custom_key Ruleset#custom_key}
        '''
        result = self._values.get("custom_key")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKey"], result)

    @builtins.property
    def ignore_query_strings_order(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore query strings order.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ignore_query_strings_order Ruleset#ignore_query_strings_order}
        '''
        result = self._values.get("ignore_query_strings_order")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKey",
    jsii_struct_bases=[],
    name_mapping={
        "cookie": "cookie",
        "header": "header",
        "host": "host",
        "query_string": "queryString",
        "user": "user",
    },
)
class RulesetRulesActionParametersCacheKeyCustomKey:
    def __init__(
        self,
        *,
        cookie: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyCookie", typing.Dict[str, typing.Any]]] = None,
        header: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyHeader", typing.Dict[str, typing.Any]]] = None,
        host: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyHost", typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyQueryString", typing.Dict[str, typing.Any]]] = None,
        user: typing.Optional[typing.Union["RulesetRulesActionParametersCacheKeyCustomKeyUser", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cookie Ruleset#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#header Ruleset#header}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host Ruleset#host}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#query_string Ruleset#query_string}
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#user Ruleset#user}
        '''
        if isinstance(cookie, dict):
            cookie = RulesetRulesActionParametersCacheKeyCustomKeyCookie(**cookie)
        if isinstance(header, dict):
            header = RulesetRulesActionParametersCacheKeyCustomKeyHeader(**header)
        if isinstance(host, dict):
            host = RulesetRulesActionParametersCacheKeyCustomKeyHost(**host)
        if isinstance(query_string, dict):
            query_string = RulesetRulesActionParametersCacheKeyCustomKeyQueryString(**query_string)
        if isinstance(user, dict):
            user = RulesetRulesActionParametersCacheKeyCustomKeyUser(**user)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKey.__init__)
            check_type(argname="argument cookie", value=cookie, expected_type=type_hints["cookie"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cookie is not None:
            self._values["cookie"] = cookie
        if header is not None:
            self._values["header"] = header
        if host is not None:
            self._values["host"] = host
        if query_string is not None:
            self._values["query_string"] = query_string
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def cookie(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyCookie"]:
        '''cookie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cookie Ruleset#cookie}
        '''
        result = self._values.get("cookie")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyCookie"], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyHeader"]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#header Ruleset#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyHeader"], result)

    @builtins.property
    def host(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyHost"]:
        '''host block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host Ruleset#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyHost"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#query_string Ruleset#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"], result)

    @builtins.property
    def user(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyUser"]:
        '''user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#user Ruleset#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyUser"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyCookie",
    jsii_struct_bases=[],
    name_mapping={"check_presence": "checkPresence", "include": "include"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyCookie:
    def __init__(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: List of cookies to check for presence in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#check_presence Ruleset#check_presence}
        :param include: List of cookies to include in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyCookie.__init__)
            check_type(argname="argument check_presence", value=check_presence, expected_type=type_hints["check_presence"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {}
        if check_presence is not None:
            self._values["check_presence"] = check_presence
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def check_presence(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of cookies to check for presence in the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#check_presence Ruleset#check_presence}
        '''
        result = self._values.get("check_presence")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of cookies to include in the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckPresence")
    def reset_check_presence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckPresence", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="checkPresenceInput")
    def check_presence_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkPresenceInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkPresence")
    def check_presence(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkPresence"))

    @check_presence.setter
    def check_presence(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference, "check_presence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkPresence", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference, "include").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyCookie]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyCookie], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyCookie],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHeader",
    jsii_struct_bases=[],
    name_mapping={
        "check_presence": "checkPresence",
        "exclude_origin": "excludeOrigin",
        "include": "include",
    },
)
class RulesetRulesActionParametersCacheKeyCustomKeyHeader:
    def __init__(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude_origin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: List of headers to check for presence in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#check_presence Ruleset#check_presence}
        :param exclude_origin: Exclude the origin header from the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exclude_origin Ruleset#exclude_origin}
        :param include: List of headers to include in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyHeader.__init__)
            check_type(argname="argument check_presence", value=check_presence, expected_type=type_hints["check_presence"])
            check_type(argname="argument exclude_origin", value=exclude_origin, expected_type=type_hints["exclude_origin"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {}
        if check_presence is not None:
            self._values["check_presence"] = check_presence
        if exclude_origin is not None:
            self._values["exclude_origin"] = exclude_origin
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def check_presence(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of headers to check for presence in the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#check_presence Ruleset#check_presence}
        '''
        result = self._values.get("check_presence")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def exclude_origin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Exclude the origin header from the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exclude_origin Ruleset#exclude_origin}
        '''
        result = self._values.get("exclude_origin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of headers to include in the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckPresence")
    def reset_check_presence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckPresence", []))

    @jsii.member(jsii_name="resetExcludeOrigin")
    def reset_exclude_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludeOrigin", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="checkPresenceInput")
    def check_presence_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "checkPresenceInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeOriginInput")
    def exclude_origin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "excludeOriginInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="checkPresence")
    def check_presence(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "checkPresence"))

    @check_presence.setter
    def check_presence(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference, "check_presence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkPresence", value)

    @builtins.property
    @jsii.member(jsii_name="excludeOrigin")
    def exclude_origin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "excludeOrigin"))

    @exclude_origin.setter
    def exclude_origin(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference, "exclude_origin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeOrigin", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference, "include").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHeader]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHost",
    jsii_struct_bases=[],
    name_mapping={"resolved": "resolved"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyHost:
    def __init__(
        self,
        *,
        resolved: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param resolved: Resolve hostname to IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#resolved Ruleset#resolved}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyHost.__init__)
            check_type(argname="argument resolved", value=resolved, expected_type=type_hints["resolved"])
        self._values: typing.Dict[str, typing.Any] = {}
        if resolved is not None:
            self._values["resolved"] = resolved

    @builtins.property
    def resolved(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Resolve hostname to IP address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#resolved Ruleset#resolved}
        '''
        result = self._values.get("resolved")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetResolved")
    def reset_resolved(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolved", []))

    @builtins.property
    @jsii.member(jsii_name="resolvedInput")
    def resolved_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "resolvedInput"))

    @builtins.property
    @jsii.member(jsii_name="resolved")
    def resolved(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "resolved"))

    @resolved.setter
    def resolved(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference, "resolved").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolved", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHost]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHost], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHost],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersCacheKeyCustomKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCookie")
    def put_cookie(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: List of cookies to check for presence in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#check_presence Ruleset#check_presence}
        :param include: List of cookies to include in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        value = RulesetRulesActionParametersCacheKeyCustomKeyCookie(
            check_presence=check_presence, include=include
        )

        return typing.cast(None, jsii.invoke(self, "putCookie", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        *,
        check_presence: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude_origin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param check_presence: List of headers to check for presence in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#check_presence Ruleset#check_presence}
        :param exclude_origin: Exclude the origin header from the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exclude_origin Ruleset#exclude_origin}
        :param include: List of headers to include in the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        value = RulesetRulesActionParametersCacheKeyCustomKeyHeader(
            check_presence=check_presence,
            exclude_origin=exclude_origin,
            include=include,
        )

        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        *,
        resolved: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param resolved: Resolve hostname to IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#resolved Ruleset#resolved}
        '''
        value = RulesetRulesActionParametersCacheKeyCustomKeyHost(resolved=resolved)

        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: List of query string parameters to exclude from the custom key. Conflicts with "include". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exclude Ruleset#exclude}
        :param include: List of query string parameters to include in the custom key. Conflicts with "exclude". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        value = RulesetRulesActionParametersCacheKeyCustomKeyQueryString(
            exclude=exclude, include=include
        )

        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        *,
        device_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        geo: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lang: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param device_type: Add device type to the custom key. Conflicts with "cache_key.cache_by_device_type". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#device_type Ruleset#device_type}
        :param geo: Add geo data to the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#geo Ruleset#geo}
        :param lang: Add language data to the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#lang Ruleset#lang}
        '''
        value = RulesetRulesActionParametersCacheKeyCustomKeyUser(
            device_type=device_type, geo=geo, lang=lang
        )

        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="resetCookie")
    def reset_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookie", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="cookie")
    def cookie(
        self,
    ) -> RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference, jsii.get(self, "cookie"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(
        self,
    ) -> RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(
        self,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference":
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(
        self,
    ) -> "RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference":
        return typing.cast("RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="cookieInput")
    def cookie_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyCookie]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyCookie], jsii.get(self, "cookieInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHeader]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHeader], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHost]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyHost], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyQueryString"], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyUser"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersCacheKeyCustomKeyUser"], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKey]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKeyCustomKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyQueryString",
    jsii_struct_bases=[],
    name_mapping={"exclude": "exclude", "include": "include"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyQueryString:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param exclude: List of query string parameters to exclude from the custom key. Conflicts with "include". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exclude Ruleset#exclude}
        :param include: List of query string parameters to include in the custom key. Conflicts with "exclude". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyQueryString.__init__)
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of query string parameters to exclude from the custom key. Conflicts with "include".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#exclude Ruleset#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of query string parameters to include in the custom key. Conflicts with "exclude".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#include Ruleset#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includeInput"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference, "exclude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "include"))

    @include.setter
    def include(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference, "include").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "include", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyQueryString]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyQueryString], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyQueryString],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyUser",
    jsii_struct_bases=[],
    name_mapping={"device_type": "deviceType", "geo": "geo", "lang": "lang"},
)
class RulesetRulesActionParametersCacheKeyCustomKeyUser:
    def __init__(
        self,
        *,
        device_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        geo: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        lang: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param device_type: Add device type to the custom key. Conflicts with "cache_key.cache_by_device_type". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#device_type Ruleset#device_type}
        :param geo: Add geo data to the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#geo Ruleset#geo}
        :param lang: Add language data to the custom key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#lang Ruleset#lang}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyUser.__init__)
            check_type(argname="argument device_type", value=device_type, expected_type=type_hints["device_type"])
            check_type(argname="argument geo", value=geo, expected_type=type_hints["geo"])
            check_type(argname="argument lang", value=lang, expected_type=type_hints["lang"])
        self._values: typing.Dict[str, typing.Any] = {}
        if device_type is not None:
            self._values["device_type"] = device_type
        if geo is not None:
            self._values["geo"] = geo
        if lang is not None:
            self._values["lang"] = lang

    @builtins.property
    def device_type(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Add device type to the custom key. Conflicts with "cache_key.cache_by_device_type".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#device_type Ruleset#device_type}
        '''
        result = self._values.get("device_type")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def geo(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Add geo data to the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#geo Ruleset#geo}
        '''
        result = self._values.get("geo")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def lang(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Add language data to the custom key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#lang Ruleset#lang}
        '''
        result = self._values.get("lang")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersCacheKeyCustomKeyUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeviceType")
    def reset_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceType", []))

    @jsii.member(jsii_name="resetGeo")
    def reset_geo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeo", []))

    @jsii.member(jsii_name="resetLang")
    def reset_lang(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLang", []))

    @builtins.property
    @jsii.member(jsii_name="deviceTypeInput")
    def device_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="geoInput")
    def geo_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "geoInput"))

    @builtins.property
    @jsii.member(jsii_name="langInput")
    def lang_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "langInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceType")
    def device_type(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deviceType"))

    @device_type.setter
    def device_type(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference, "device_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceType", value)

    @builtins.property
    @jsii.member(jsii_name="geo")
    def geo(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "geo"))

    @geo.setter
    def geo(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference, "geo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geo", value)

    @builtins.property
    @jsii.member(jsii_name="lang")
    def lang(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lang"))

    @lang.setter
    def lang(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference, "lang").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lang", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyUser]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKeyCustomKeyUser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersCacheKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersCacheKeyOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersCacheKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomKey")
    def put_custom_key(
        self,
        *,
        cookie: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyCookie, typing.Dict[str, typing.Any]]] = None,
        header: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHeader, typing.Dict[str, typing.Any]]] = None,
        host: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyHost, typing.Dict[str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyQueryString, typing.Dict[str, typing.Any]]] = None,
        user: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKeyCustomKeyUser, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cookie Ruleset#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#header Ruleset#header}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host Ruleset#host}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#query_string Ruleset#query_string}
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#user Ruleset#user}
        '''
        value = RulesetRulesActionParametersCacheKeyCustomKey(
            cookie=cookie,
            header=header,
            host=host,
            query_string=query_string,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomKey", [value]))

    @jsii.member(jsii_name="resetCacheByDeviceType")
    def reset_cache_by_device_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheByDeviceType", []))

    @jsii.member(jsii_name="resetCacheDeceptionArmor")
    def reset_cache_deception_armor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheDeceptionArmor", []))

    @jsii.member(jsii_name="resetCustomKey")
    def reset_custom_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomKey", []))

    @jsii.member(jsii_name="resetIgnoreQueryStringsOrder")
    def reset_ignore_query_strings_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreQueryStringsOrder", []))

    @builtins.property
    @jsii.member(jsii_name="customKey")
    def custom_key(
        self,
    ) -> RulesetRulesActionParametersCacheKeyCustomKeyOutputReference:
        return typing.cast(RulesetRulesActionParametersCacheKeyCustomKeyOutputReference, jsii.get(self, "customKey"))

    @builtins.property
    @jsii.member(jsii_name="cacheByDeviceTypeInput")
    def cache_by_device_type_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheByDeviceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheDeceptionArmorInput")
    def cache_deception_armor_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheDeceptionArmorInput"))

    @builtins.property
    @jsii.member(jsii_name="customKeyInput")
    def custom_key_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersCacheKeyCustomKey]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKeyCustomKey], jsii.get(self, "customKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreQueryStringsOrderInput")
    def ignore_query_strings_order_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreQueryStringsOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheByDeviceType")
    def cache_by_device_type(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cacheByDeviceType"))

    @cache_by_device_type.setter
    def cache_by_device_type(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyOutputReference, "cache_by_device_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheByDeviceType", value)

    @builtins.property
    @jsii.member(jsii_name="cacheDeceptionArmor")
    def cache_deception_armor(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cacheDeceptionArmor"))

    @cache_deception_armor.setter
    def cache_deception_armor(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyOutputReference, "cache_deception_armor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheDeceptionArmor", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreQueryStringsOrder")
    def ignore_query_strings_order(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreQueryStringsOrder"))

    @ignore_query_strings_order.setter
    def ignore_query_strings_order(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyOutputReference, "ignore_query_strings_order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreQueryStringsOrder", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersCacheKey]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersCacheKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersCacheKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtl",
    jsii_struct_bases=[],
    name_mapping={
        "default": "default",
        "mode": "mode",
        "status_code_ttl": "statusCodeTtl",
    },
)
class RulesetRulesActionParametersEdgeTtl:
    def __init__(
        self,
        *,
        default: jsii.Number,
        mode: builtins.str,
        status_code_ttl: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtl", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default: Default edge TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#default Ruleset#default}
        :param mode: Mode of the edge TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mode Ruleset#mode}
        :param status_code_ttl: status_code_ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code_ttl Ruleset#status_code_ttl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtl.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument status_code_ttl", value=status_code_ttl, expected_type=type_hints["status_code_ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "default": default,
            "mode": mode,
        }
        if status_code_ttl is not None:
            self._values["status_code_ttl"] = status_code_ttl

    @builtins.property
    def default(self) -> jsii.Number:
        '''Default edge TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#default Ruleset#default}
        '''
        result = self._values.get("default")
        assert result is not None, "Required property 'default' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''Mode of the edge TTL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mode Ruleset#mode}
        '''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code_ttl(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]]:
        '''status_code_ttl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code_ttl Ruleset#status_code_ttl}
        '''
        result = self._values.get("status_code_ttl")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersEdgeTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersEdgeTtlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStatusCodeTtl")
    def put_status_code_ttl(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtl", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlOutputReference.put_status_code_ttl)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCodeTtl", [value]))

    @jsii.member(jsii_name="resetStatusCodeTtl")
    def reset_status_code_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCodeTtl", []))

    @builtins.property
    @jsii.member(jsii_name="statusCodeTtl")
    def status_code_ttl(self) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlList":
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlList", jsii.get(self, "statusCodeTtl"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeTtlInput")
    def status_code_ttl_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtl"]]], jsii.get(self, "statusCodeTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "default"))

    @default.setter
    def default(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersEdgeTtl]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersEdgeTtl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersEdgeTtl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtl",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "status_code": "statusCode",
        "status_code_range": "statusCodeRange",
    },
)
class RulesetRulesActionParametersEdgeTtlStatusCodeTtl:
    def __init__(
        self,
        *,
        value: jsii.Number,
        status_code: typing.Optional[jsii.Number] = None,
        status_code_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param value: Status code edge TTL value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        :param status_code: Status code for which the edge TTL is applied. Conflicts with "status_code_range". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        :param status_code_range: status_code_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code_range Ruleset#status_code_range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtl.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument status_code_range", value=status_code_range, expected_type=type_hints["status_code_range"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if status_code is not None:
            self._values["status_code"] = status_code
        if status_code_range is not None:
            self._values["status_code_range"] = status_code_range

    @builtins.property
    def value(self) -> jsii.Number:
        '''Status code edge TTL value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''Status code for which the edge TTL is applied. Conflicts with "status_code_range".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def status_code_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]]:
        '''status_code_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code_range Ruleset#status_code_range}
        '''
        result = self._values.get("status_code_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersEdgeTtlStatusCodeTtl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStatusCodeRange")
    def put_status_code_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference.put_status_code_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStatusCodeRange", [value]))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetStatusCodeRange")
    def reset_status_code_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCodeRange", []))

    @builtins.property
    @jsii.member(jsii_name="statusCodeRange")
    def status_code_range(
        self,
    ) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList":
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList", jsii.get(self, "statusCodeRange"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeRangeInput")
    def status_code_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange"]]], jsii.get(self, "statusCodeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtl, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtl, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtl, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange:
    def __init__(
        self,
        *,
        from_: typing.Optional[jsii.Number] = None,
        to: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param from_: From status code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from Ruleset#from}
        :param to: To status code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#to Ruleset#to}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange.__init__)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument to", value=to, expected_type=type_hints["to"])
        self._values: typing.Dict[str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[jsii.Number]:
        '''From status code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from Ruleset#from}
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def to(self) -> typing.Optional[jsii.Number]:
        '''To status code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#to Ruleset#to}
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFrom")
    def reset_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrom", []))

    @jsii.member(jsii_name="resetTo")
    def reset_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTo", []))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="toInput")
    def to_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference, "from_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @to.setter
    def to(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference, "to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "to", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromList",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name"},
)
class RulesetRulesActionParametersFromList:
    def __init__(self, *, key: builtins.str, name: builtins.str) -> None:
        '''
        :param key: Expression to use for the list lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#key Ruleset#key}
        :param name: Name of the list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersFromList.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "name": name,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Expression to use for the list lookup.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#key Ruleset#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersFromList(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersFromListOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromListOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersFromListOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromListOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromListOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersFromList]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersFromList], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersFromList],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromListOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValue",
    jsii_struct_bases=[],
    name_mapping={
        "preserve_query_string": "preserveQueryString",
        "status_code": "statusCode",
        "target_url": "targetUrl",
    },
)
class RulesetRulesActionParametersFromValue:
    def __init__(
        self,
        *,
        preserve_query_string: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status_code: typing.Optional[jsii.Number] = None,
        target_url: typing.Optional[typing.Union["RulesetRulesActionParametersFromValueTargetUrl", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preserve_query_string: Preserve query string for redirect URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#preserve_query_string Ruleset#preserve_query_string}
        :param status_code: Status code for redirect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        :param target_url: target_url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#target_url Ruleset#target_url}
        '''
        if isinstance(target_url, dict):
            target_url = RulesetRulesActionParametersFromValueTargetUrl(**target_url)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersFromValue.__init__)
            check_type(argname="argument preserve_query_string", value=preserve_query_string, expected_type=type_hints["preserve_query_string"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if preserve_query_string is not None:
            self._values["preserve_query_string"] = preserve_query_string
        if status_code is not None:
            self._values["status_code"] = status_code
        if target_url is not None:
            self._values["target_url"] = target_url

    @builtins.property
    def preserve_query_string(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Preserve query string for redirect URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#preserve_query_string Ruleset#preserve_query_string}
        '''
        result = self._values.get("preserve_query_string")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''Status code for redirect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_url(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersFromValueTargetUrl"]:
        '''target_url block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#target_url Ruleset#target_url}
        '''
        result = self._values.get("target_url")
        return typing.cast(typing.Optional["RulesetRulesActionParametersFromValueTargetUrl"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersFromValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersFromValueOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersFromValueOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetUrl")
    def put_target_url(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Conflicts with ``"value"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param value: Static value to provide as the HTTP request header value. Conflicts with ``"expression"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        value_ = RulesetRulesActionParametersFromValueTargetUrl(
            expression=expression, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putTargetUrl", [value_]))

    @jsii.member(jsii_name="resetPreserveQueryString")
    def reset_preserve_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveQueryString", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetTargetUrl")
    def reset_target_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="targetUrl")
    def target_url(
        self,
    ) -> "RulesetRulesActionParametersFromValueTargetUrlOutputReference":
        return typing.cast("RulesetRulesActionParametersFromValueTargetUrlOutputReference", jsii.get(self, "targetUrl"))

    @builtins.property
    @jsii.member(jsii_name="preserveQueryStringInput")
    def preserve_query_string_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveQueryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetUrlInput")
    def target_url_input(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersFromValueTargetUrl"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersFromValueTargetUrl"], jsii.get(self, "targetUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveQueryString")
    def preserve_query_string(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveQueryString"))

    @preserve_query_string.setter
    def preserve_query_string(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromValueOutputReference, "preserve_query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveQueryString", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromValueOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersFromValue]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersFromValue], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersFromValue],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromValueOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueTargetUrl",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression", "value": "value"},
)
class RulesetRulesActionParametersFromValueTargetUrl:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Conflicts with ``"value"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param value: Static value to provide as the HTTP request header value. Conflicts with ``"expression"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersFromValueTargetUrl.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Conflicts with ``"value"``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static value to provide as the HTTP request header value. Conflicts with ``"expression"``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersFromValueTargetUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersFromValueTargetUrlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersFromValueTargetUrlOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersFromValueTargetUrlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromValueTargetUrlOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromValueTargetUrlOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersFromValueTargetUrl]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersFromValueTargetUrl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersFromValueTargetUrl],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersFromValueTargetUrlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "name": "name",
        "operation": "operation",
        "value": "value",
    },
)
class RulesetRulesActionParametersHeaders:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Conflicts with ``"value"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param name: Name of the HTTP request header to target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        :param operation: Action to perform on the HTTP request header. Available values: ``remove``, ``set``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#operation Ruleset#operation}
        :param value: Static value to provide as the HTTP request header value. Conflicts with ``"expression"``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersHeaders.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if name is not None:
            self._values["name"] = name
        if operation is not None:
            self._values["operation"] = operation
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Use a value dynamically determined by the Firewall Rules expression language based on Wireshark display filters.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Conflicts with ``"value"``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the HTTP request header to target.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Action to perform on the HTTP request header. Available values: ``remove``, ``set``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#operation Ruleset#operation}
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static value to provide as the HTTP request header value. Conflicts with ``"expression"``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersHeadersList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersHeadersOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOperation")
    def reset_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperation", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operationInput")
    def operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersOutputReference, "operation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersMatchedData",
    jsii_struct_bases=[],
    name_mapping={"public_key": "publicKey"},
)
class RulesetRulesActionParametersMatchedData:
    def __init__(self, *, public_key: typing.Optional[builtins.str] = None) -> None:
        '''
        :param public_key: Public key to use within WAF Ruleset payload logging to view the HTTP request parameters. You can generate a public key `using the ``matched-data-cli`` command-line tool <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/command-line/generate-key-pair>`_ or `in the Cloudflare dashboard <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/configure>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#public_key Ruleset#public_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersMatchedData.__init__)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''Public key to use within WAF Ruleset payload logging to view the HTTP request parameters.

        You can generate a public key `using the ``matched-data-cli`` command-line tool <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/command-line/generate-key-pair>`_ or `in the Cloudflare dashboard <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/configure>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#public_key Ruleset#public_key}
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersMatchedData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersMatchedDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersMatchedDataOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersMatchedDataOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPublicKey")
    def reset_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKey", []))

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersMatchedDataOutputReference, "public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersMatchedData]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersMatchedData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersMatchedData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersMatchedDataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOrigin",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "port": "port"},
)
class RulesetRulesActionParametersOrigin:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host: Origin Hostname where request is sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host Ruleset#host}
        :param port: Origin Port where request is sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#port Ruleset#port}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOrigin.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Origin Hostname where request is sent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host Ruleset#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Origin Port where request is sent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#port Ruleset#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOrigin(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersOriginOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOriginOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOriginOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOriginOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOriginOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersOrigin]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersOrigin], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersOrigin],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOriginOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutominify")
    def put_autominify(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAutominify, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOutputReference.put_autominify)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAutominify", [value]))

    @jsii.member(jsii_name="putBrowserTtl")
    def put_browser_ttl(
        self,
        *,
        mode: builtins.str,
        default: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Mode of the browser TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mode Ruleset#mode}
        :param default: Default browser TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#default Ruleset#default}
        '''
        value = RulesetRulesActionParametersBrowserTtl(mode=mode, default=default)

        return typing.cast(None, jsii.invoke(self, "putBrowserTtl", [value]))

    @jsii.member(jsii_name="putCacheKey")
    def put_cache_key(
        self,
        *,
        cache_by_device_type: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_deception_armor: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_key: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKeyCustomKey, typing.Dict[str, typing.Any]]] = None,
        ignore_query_strings_order: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cache_by_device_type: Cache by device type. Conflicts with "custom_key.user.device_type". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_by_device_type Ruleset#cache_by_device_type}
        :param cache_deception_armor: Cache deception armor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_deception_armor Ruleset#cache_deception_armor}
        :param custom_key: custom_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#custom_key Ruleset#custom_key}
        :param ignore_query_strings_order: Ignore query strings order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ignore_query_strings_order Ruleset#ignore_query_strings_order}
        '''
        value = RulesetRulesActionParametersCacheKey(
            cache_by_device_type=cache_by_device_type,
            cache_deception_armor=cache_deception_armor,
            custom_key=custom_key,
            ignore_query_strings_order=ignore_query_strings_order,
        )

        return typing.cast(None, jsii.invoke(self, "putCacheKey", [value]))

    @jsii.member(jsii_name="putEdgeTtl")
    def put_edge_ttl(
        self,
        *,
        default: jsii.Number,
        mode: builtins.str,
        status_code_ttl: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersEdgeTtlStatusCodeTtl, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param default: Default edge TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#default Ruleset#default}
        :param mode: Mode of the edge TTL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mode Ruleset#mode}
        :param status_code_ttl: status_code_ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code_ttl Ruleset#status_code_ttl}
        '''
        value = RulesetRulesActionParametersEdgeTtl(
            default=default, mode=mode, status_code_ttl=status_code_ttl
        )

        return typing.cast(None, jsii.invoke(self, "putEdgeTtl", [value]))

    @jsii.member(jsii_name="putFromList")
    def put_from_list(self, *, key: builtins.str, name: builtins.str) -> None:
        '''
        :param key: Expression to use for the list lookup. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#key Ruleset#key}
        :param name: Name of the list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#name Ruleset#name}
        '''
        value = RulesetRulesActionParametersFromList(key=key, name=name)

        return typing.cast(None, jsii.invoke(self, "putFromList", [value]))

    @jsii.member(jsii_name="putFromValue")
    def put_from_value(
        self,
        *,
        preserve_query_string: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status_code: typing.Optional[jsii.Number] = None,
        target_url: typing.Optional[typing.Union[RulesetRulesActionParametersFromValueTargetUrl, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param preserve_query_string: Preserve query string for redirect URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#preserve_query_string Ruleset#preserve_query_string}
        :param status_code: Status code for redirect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        :param target_url: target_url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#target_url Ruleset#target_url}
        '''
        value = RulesetRulesActionParametersFromValue(
            preserve_query_string=preserve_query_string,
            status_code=status_code,
            target_url=target_url,
        )

        return typing.cast(None, jsii.invoke(self, "putFromValue", [value]))

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putMatchedData")
    def put_matched_data(
        self,
        *,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param public_key: Public key to use within WAF Ruleset payload logging to view the HTTP request parameters. You can generate a public key `using the ``matched-data-cli`` command-line tool <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/command-line/generate-key-pair>`_ or `in the Cloudflare dashboard <https://developers.cloudflare.com/waf/managed-rulesets/payload-logging/configure>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#public_key Ruleset#public_key}
        '''
        value = RulesetRulesActionParametersMatchedData(public_key=public_key)

        return typing.cast(None, jsii.invoke(self, "putMatchedData", [value]))

    @jsii.member(jsii_name="putOrigin")
    def put_origin(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param host: Origin Hostname where request is sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host Ruleset#host}
        :param port: Origin Port where request is sent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#port Ruleset#port}
        '''
        value = RulesetRulesActionParametersOrigin(host=host, port=port)

        return typing.cast(None, jsii.invoke(self, "putOrigin", [value]))

    @jsii.member(jsii_name="putOverrides")
    def put_overrides(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        categories: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesCategories", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesRules", typing.Dict[str, typing.Any]]]]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to perform in the rule-level override. Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        :param categories: categories block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#categories Ruleset#categories}
        :param enabled: Defines if the current ruleset-level override enables or disables the ruleset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        :param status: Defines if the current ruleset-level override enables or disables the ruleset. Available values: ``enabled``, ``disabled``. Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        value = RulesetRulesActionParametersOverrides(
            action=action,
            categories=categories,
            enabled=enabled,
            rules=rules,
            status=status,
        )

        return typing.cast(None, jsii.invoke(self, "putOverrides", [value]))

    @jsii.member(jsii_name="putResponse")
    def put_response(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersResponse", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOutputReference.put_response)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponse", [value]))

    @jsii.member(jsii_name="putServeStale")
    def put_serve_stale(
        self,
        *,
        disable_stale_while_updating: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param disable_stale_while_updating: Disable stale while updating. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_stale_while_updating Ruleset#disable_stale_while_updating}
        '''
        value = RulesetRulesActionParametersServeStale(
            disable_stale_while_updating=disable_stale_while_updating
        )

        return typing.cast(None, jsii.invoke(self, "putServeStale", [value]))

    @jsii.member(jsii_name="putSni")
    def put_sni(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Value to define for SNI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        value_ = RulesetRulesActionParametersSni(value=value)

        return typing.cast(None, jsii.invoke(self, "putSni", [value_]))

    @jsii.member(jsii_name="putUri")
    def put_uri(
        self,
        *,
        origin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path: typing.Optional[typing.Union["RulesetRulesActionParametersUriPath", typing.Dict[str, typing.Any]]] = None,
        query: typing.Optional[typing.Union["RulesetRulesActionParametersUriQuery", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param origin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin Ruleset#origin}.
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#path Ruleset#path}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#query Ruleset#query}
        '''
        value = RulesetRulesActionParametersUri(origin=origin, path=path, query=query)

        return typing.cast(None, jsii.invoke(self, "putUri", [value]))

    @jsii.member(jsii_name="resetAutomaticHttpsRewrites")
    def reset_automatic_https_rewrites(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticHttpsRewrites", []))

    @jsii.member(jsii_name="resetAutominify")
    def reset_autominify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutominify", []))

    @jsii.member(jsii_name="resetBic")
    def reset_bic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBic", []))

    @jsii.member(jsii_name="resetBrowserTtl")
    def reset_browser_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserTtl", []))

    @jsii.member(jsii_name="resetCache")
    def reset_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCache", []))

    @jsii.member(jsii_name="resetCacheKey")
    def reset_cache_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheKey", []))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetCookieFields")
    def reset_cookie_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieFields", []))

    @jsii.member(jsii_name="resetDisableApps")
    def reset_disable_apps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableApps", []))

    @jsii.member(jsii_name="resetDisableRailgun")
    def reset_disable_railgun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRailgun", []))

    @jsii.member(jsii_name="resetDisableZaraz")
    def reset_disable_zaraz(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableZaraz", []))

    @jsii.member(jsii_name="resetEdgeTtl")
    def reset_edge_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeTtl", []))

    @jsii.member(jsii_name="resetEmailObfuscation")
    def reset_email_obfuscation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailObfuscation", []))

    @jsii.member(jsii_name="resetFromList")
    def reset_from_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromList", []))

    @jsii.member(jsii_name="resetFromValue")
    def reset_from_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromValue", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetHostHeader")
    def reset_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeader", []))

    @jsii.member(jsii_name="resetHotlinkProtection")
    def reset_hotlink_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHotlinkProtection", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncrement")
    def reset_increment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncrement", []))

    @jsii.member(jsii_name="resetMatchedData")
    def reset_matched_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchedData", []))

    @jsii.member(jsii_name="resetMirage")
    def reset_mirage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirage", []))

    @jsii.member(jsii_name="resetOpportunisticEncryption")
    def reset_opportunistic_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpportunisticEncryption", []))

    @jsii.member(jsii_name="resetOrigin")
    def reset_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrigin", []))

    @jsii.member(jsii_name="resetOriginErrorPagePassthru")
    def reset_origin_error_page_passthru(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginErrorPagePassthru", []))

    @jsii.member(jsii_name="resetOverrides")
    def reset_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrides", []))

    @jsii.member(jsii_name="resetPhases")
    def reset_phases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhases", []))

    @jsii.member(jsii_name="resetPolish")
    def reset_polish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolish", []))

    @jsii.member(jsii_name="resetProducts")
    def reset_products(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProducts", []))

    @jsii.member(jsii_name="resetRequestFields")
    def reset_request_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestFields", []))

    @jsii.member(jsii_name="resetRespectStrongEtags")
    def reset_respect_strong_etags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRespectStrongEtags", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @jsii.member(jsii_name="resetResponseFields")
    def reset_response_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseFields", []))

    @jsii.member(jsii_name="resetRocketLoader")
    def reset_rocket_loader(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRocketLoader", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetRuleset")
    def reset_ruleset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuleset", []))

    @jsii.member(jsii_name="resetRulesets")
    def reset_rulesets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRulesets", []))

    @jsii.member(jsii_name="resetSecurityLevel")
    def reset_security_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityLevel", []))

    @jsii.member(jsii_name="resetServerSideExcludes")
    def reset_server_side_excludes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerSideExcludes", []))

    @jsii.member(jsii_name="resetServeStale")
    def reset_serve_stale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServeStale", []))

    @jsii.member(jsii_name="resetSni")
    def reset_sni(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSni", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @jsii.member(jsii_name="resetSxg")
    def reset_sxg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSxg", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="autominify")
    def autominify(self) -> RulesetRulesActionParametersAutominifyList:
        return typing.cast(RulesetRulesActionParametersAutominifyList, jsii.get(self, "autominify"))

    @builtins.property
    @jsii.member(jsii_name="browserTtl")
    def browser_ttl(self) -> RulesetRulesActionParametersBrowserTtlOutputReference:
        return typing.cast(RulesetRulesActionParametersBrowserTtlOutputReference, jsii.get(self, "browserTtl"))

    @builtins.property
    @jsii.member(jsii_name="cacheKey")
    def cache_key(self) -> RulesetRulesActionParametersCacheKeyOutputReference:
        return typing.cast(RulesetRulesActionParametersCacheKeyOutputReference, jsii.get(self, "cacheKey"))

    @builtins.property
    @jsii.member(jsii_name="edgeTtl")
    def edge_ttl(self) -> RulesetRulesActionParametersEdgeTtlOutputReference:
        return typing.cast(RulesetRulesActionParametersEdgeTtlOutputReference, jsii.get(self, "edgeTtl"))

    @builtins.property
    @jsii.member(jsii_name="fromList")
    def from_list(self) -> RulesetRulesActionParametersFromListOutputReference:
        return typing.cast(RulesetRulesActionParametersFromListOutputReference, jsii.get(self, "fromList"))

    @builtins.property
    @jsii.member(jsii_name="fromValue")
    def from_value(self) -> RulesetRulesActionParametersFromValueOutputReference:
        return typing.cast(RulesetRulesActionParametersFromValueOutputReference, jsii.get(self, "fromValue"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> RulesetRulesActionParametersHeadersList:
        return typing.cast(RulesetRulesActionParametersHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="matchedData")
    def matched_data(self) -> RulesetRulesActionParametersMatchedDataOutputReference:
        return typing.cast(RulesetRulesActionParametersMatchedDataOutputReference, jsii.get(self, "matchedData"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> RulesetRulesActionParametersOriginOutputReference:
        return typing.cast(RulesetRulesActionParametersOriginOutputReference, jsii.get(self, "origin"))

    @builtins.property
    @jsii.member(jsii_name="overrides")
    def overrides(self) -> "RulesetRulesActionParametersOverridesOutputReference":
        return typing.cast("RulesetRulesActionParametersOverridesOutputReference", jsii.get(self, "overrides"))

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> "RulesetRulesActionParametersResponseList":
        return typing.cast("RulesetRulesActionParametersResponseList", jsii.get(self, "response"))

    @builtins.property
    @jsii.member(jsii_name="serveStale")
    def serve_stale(self) -> "RulesetRulesActionParametersServeStaleOutputReference":
        return typing.cast("RulesetRulesActionParametersServeStaleOutputReference", jsii.get(self, "serveStale"))

    @builtins.property
    @jsii.member(jsii_name="sni")
    def sni(self) -> "RulesetRulesActionParametersSniOutputReference":
        return typing.cast("RulesetRulesActionParametersSniOutputReference", jsii.get(self, "sni"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> "RulesetRulesActionParametersUriOutputReference":
        return typing.cast("RulesetRulesActionParametersUriOutputReference", jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewritesInput")
    def automatic_https_rewrites_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticHttpsRewritesInput"))

    @builtins.property
    @jsii.member(jsii_name="autominifyInput")
    def autominify_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersAutominify]]], jsii.get(self, "autominifyInput"))

    @builtins.property
    @jsii.member(jsii_name="bicInput")
    def bic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bicInput"))

    @builtins.property
    @jsii.member(jsii_name="browserTtlInput")
    def browser_ttl_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersBrowserTtl]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersBrowserTtl], jsii.get(self, "browserTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheInput")
    def cache_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheKeyInput")
    def cache_key_input(self) -> typing.Optional[RulesetRulesActionParametersCacheKey]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersCacheKey], jsii.get(self, "cacheKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieFieldsInput")
    def cookie_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cookieFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="disableAppsInput")
    def disable_apps_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableAppsInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRailgunInput")
    def disable_railgun_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableRailgunInput"))

    @builtins.property
    @jsii.member(jsii_name="disableZarazInput")
    def disable_zaraz_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableZarazInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeTtlInput")
    def edge_ttl_input(self) -> typing.Optional[RulesetRulesActionParametersEdgeTtl]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersEdgeTtl], jsii.get(self, "edgeTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="emailObfuscationInput")
    def email_obfuscation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emailObfuscationInput"))

    @builtins.property
    @jsii.member(jsii_name="fromListInput")
    def from_list_input(self) -> typing.Optional[RulesetRulesActionParametersFromList]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersFromList], jsii.get(self, "fromListInput"))

    @builtins.property
    @jsii.member(jsii_name="fromValueInput")
    def from_value_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersFromValue]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersFromValue], jsii.get(self, "fromValueInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtectionInput")
    def hotlink_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hotlinkProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="incrementInput")
    def increment_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "incrementInput"))

    @builtins.property
    @jsii.member(jsii_name="matchedDataInput")
    def matched_data_input(
        self,
    ) -> typing.Optional[RulesetRulesActionParametersMatchedData]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersMatchedData], jsii.get(self, "matchedDataInput"))

    @builtins.property
    @jsii.member(jsii_name="mirageInput")
    def mirage_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mirageInput"))

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryptionInput")
    def opportunistic_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "opportunisticEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassthruInput")
    def origin_error_page_passthru_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "originErrorPagePassthruInput"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(self) -> typing.Optional[RulesetRulesActionParametersOrigin]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersOrigin], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="overridesInput")
    def overrides_input(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersOverrides"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersOverrides"], jsii.get(self, "overridesInput"))

    @builtins.property
    @jsii.member(jsii_name="phasesInput")
    def phases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "phasesInput"))

    @builtins.property
    @jsii.member(jsii_name="polishInput")
    def polish_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "polishInput"))

    @builtins.property
    @jsii.member(jsii_name="productsInput")
    def products_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "productsInput"))

    @builtins.property
    @jsii.member(jsii_name="requestFieldsInput")
    def request_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requestFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="respectStrongEtagsInput")
    def respect_strong_etags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "respectStrongEtagsInput"))

    @builtins.property
    @jsii.member(jsii_name="responseFieldsInput")
    def response_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersResponse"]]], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="rocketLoaderInput")
    def rocket_loader_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rocketLoaderInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesetInput")
    def ruleset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rulesetInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesetsInput")
    def rulesets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rulesetsInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="securityLevelInput")
    def security_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="serverSideExcludesInput")
    def server_side_excludes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serverSideExcludesInput"))

    @builtins.property
    @jsii.member(jsii_name="serveStaleInput")
    def serve_stale_input(
        self,
    ) -> typing.Optional["RulesetRulesActionParametersServeStale"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersServeStale"], jsii.get(self, "serveStaleInput"))

    @builtins.property
    @jsii.member(jsii_name="sniInput")
    def sni_input(self) -> typing.Optional["RulesetRulesActionParametersSni"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersSni"], jsii.get(self, "sniInput"))

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="sxgInput")
    def sxg_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sxgInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional["RulesetRulesActionParametersUri"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersUri"], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticHttpsRewrites")
    def automatic_https_rewrites(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticHttpsRewrites"))

    @automatic_https_rewrites.setter
    def automatic_https_rewrites(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "automatic_https_rewrites").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticHttpsRewrites", value)

    @builtins.property
    @jsii.member(jsii_name="bic")
    def bic(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bic"))

    @bic.setter
    def bic(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "bic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bic", value)

    @builtins.property
    @jsii.member(jsii_name="cache")
    def cache(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cache"))

    @cache.setter
    def cache(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "cache").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cache", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="cookieFields")
    def cookie_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cookieFields"))

    @cookie_fields.setter
    def cookie_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "cookie_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieFields", value)

    @builtins.property
    @jsii.member(jsii_name="disableApps")
    def disable_apps(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableApps"))

    @disable_apps.setter
    def disable_apps(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "disable_apps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableApps", value)

    @builtins.property
    @jsii.member(jsii_name="disableRailgun")
    def disable_railgun(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRailgun"))

    @disable_railgun.setter
    def disable_railgun(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "disable_railgun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRailgun", value)

    @builtins.property
    @jsii.member(jsii_name="disableZaraz")
    def disable_zaraz(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableZaraz"))

    @disable_zaraz.setter
    def disable_zaraz(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "disable_zaraz").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableZaraz", value)

    @builtins.property
    @jsii.member(jsii_name="emailObfuscation")
    def email_obfuscation(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emailObfuscation"))

    @email_obfuscation.setter
    def email_obfuscation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "email_obfuscation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailObfuscation", value)

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeader"))

    @host_header.setter
    def host_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "host_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostHeader", value)

    @builtins.property
    @jsii.member(jsii_name="hotlinkProtection")
    def hotlink_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hotlinkProtection"))

    @hotlink_protection.setter
    def hotlink_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "hotlink_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hotlinkProtection", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="increment")
    def increment(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "increment"))

    @increment.setter
    def increment(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "increment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "increment", value)

    @builtins.property
    @jsii.member(jsii_name="mirage")
    def mirage(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mirage"))

    @mirage.setter
    def mirage(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "mirage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirage", value)

    @builtins.property
    @jsii.member(jsii_name="opportunisticEncryption")
    def opportunistic_encryption(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "opportunisticEncryption"))

    @opportunistic_encryption.setter
    def opportunistic_encryption(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "opportunistic_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opportunisticEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="originErrorPagePassthru")
    def origin_error_page_passthru(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "originErrorPagePassthru"))

    @origin_error_page_passthru.setter
    def origin_error_page_passthru(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "origin_error_page_passthru").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originErrorPagePassthru", value)

    @builtins.property
    @jsii.member(jsii_name="phases")
    def phases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "phases"))

    @phases.setter
    def phases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "phases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phases", value)

    @builtins.property
    @jsii.member(jsii_name="polish")
    def polish(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "polish"))

    @polish.setter
    def polish(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "polish").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "polish", value)

    @builtins.property
    @jsii.member(jsii_name="products")
    def products(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "products"))

    @products.setter
    def products(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "products").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "products", value)

    @builtins.property
    @jsii.member(jsii_name="requestFields")
    def request_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requestFields"))

    @request_fields.setter
    def request_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "request_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestFields", value)

    @builtins.property
    @jsii.member(jsii_name="respectStrongEtags")
    def respect_strong_etags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "respectStrongEtags"))

    @respect_strong_etags.setter
    def respect_strong_etags(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "respect_strong_etags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "respectStrongEtags", value)

    @builtins.property
    @jsii.member(jsii_name="responseFields")
    def response_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseFields"))

    @response_fields.setter
    def response_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "response_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseFields", value)

    @builtins.property
    @jsii.member(jsii_name="rocketLoader")
    def rocket_loader(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rocketLoader"))

    @rocket_loader.setter
    def rocket_loader(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "rocket_loader").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rocketLoader", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "rules"))

    @rules.setter
    def rules(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "rules").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="ruleset")
    def ruleset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ruleset"))

    @ruleset.setter
    def ruleset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "ruleset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleset", value)

    @builtins.property
    @jsii.member(jsii_name="rulesets")
    def rulesets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rulesets"))

    @rulesets.setter
    def rulesets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "rulesets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rulesets", value)

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "security_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideExcludes")
    def server_side_excludes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serverSideExcludes"))

    @server_side_excludes.setter
    def server_side_excludes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "server_side_excludes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideExcludes", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssl"))

    @ssl.setter
    def ssl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="sxg")
    def sxg(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sxg"))

    @sxg.setter
    def sxg(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "sxg").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sxg", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParameters]:
        return typing.cast(typing.Optional[RulesetRulesActionParameters], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParameters],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverrides",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "categories": "categories",
        "enabled": "enabled",
        "rules": "rules",
        "status": "status",
    },
)
class RulesetRulesActionParametersOverrides:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        categories: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesCategories", typing.Dict[str, typing.Any]]]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesRules", typing.Dict[str, typing.Any]]]]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to perform in the rule-level override. Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        :param categories: categories block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#categories Ruleset#categories}
        :param enabled: Defines if the current ruleset-level override enables or disables the ruleset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        :param status: Defines if the current ruleset-level override enables or disables the ruleset. Available values: ``enabled``, ``disabled``. Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverrides.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument categories", value=categories, expected_type=type_hints["categories"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if categories is not None:
            self._values["categories"] = categories
        if enabled is not None:
            self._values["enabled"] = enabled
        if rules is not None:
            self._values["rules"] = rules
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the rule-level override.

        Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def categories(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersOverridesCategories"]]]:
        '''categories block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#categories Ruleset#categories}
        '''
        result = self._values.get("categories")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersOverridesCategories"]]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines if the current ruleset-level override enables or disables the ruleset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Defines if the current ruleset-level override enables or disables the ruleset. Available values: ``enabled``, ``disabled``. Defaults to ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesCategories",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "category": "category",
        "enabled": "enabled",
        "status": "status",
    },
)
class RulesetRulesActionParametersOverridesCategories:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        category: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to perform in the tag-level override. Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        :param category: Tag name to apply the ruleset rule override to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#category Ruleset#category}
        :param enabled: Defines if the current tag-level override enables or disables the ruleset rules with the specified tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param status: Defines if the current tag-level override enables or disables the ruleset rules with the specified tag. Available values: ``enabled``, ``disabled``. Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesCategories.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if category is not None:
            self._values["category"] = category
        if enabled is not None:
            self._values["enabled"] = enabled
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the tag-level override.

        Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def category(self) -> typing.Optional[builtins.str]:
        '''Tag name to apply the ruleset rule override to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#category Ruleset#category}
        '''
        result = self._values.get("category")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines if the current tag-level override enables or disables the ruleset rules with the specified tag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Defines if the current tag-level override enables or disables the ruleset rules with the specified tag.

        Available values: ``enabled``, ``disabled``. Defaults to ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOverridesCategories(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersOverridesCategoriesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesCategoriesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesCategoriesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersOverridesCategoriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesCategoriesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOverridesCategoriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersOverridesCategoriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesCategoriesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesCategoriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetCategory")
    def reset_category(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategory", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryInput")
    def category_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categoryInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="category")
    def category(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "category"))

    @category.setter
    def category(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesOutputReference, "category").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "category", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersOverridesCategories, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersOverridesCategories, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersOverridesCategories, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesCategoriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersOverridesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCategories")
    def put_categories(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersOverridesCategories, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesOutputReference.put_categories)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCategories", [value]))

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RulesetRulesActionParametersOverridesRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesOutputReference.put_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetCategories")
    def reset_categories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategories", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="categories")
    def categories(self) -> RulesetRulesActionParametersOverridesCategoriesList:
        return typing.cast(RulesetRulesActionParametersOverridesCategoriesList, jsii.get(self, "categories"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "RulesetRulesActionParametersOverridesRulesList":
        return typing.cast("RulesetRulesActionParametersOverridesRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="categoriesInput")
    def categories_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesCategories]]], jsii.get(self, "categoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RulesetRulesActionParametersOverridesRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersOverrides]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersOverrides], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersOverrides],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesRules",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "enabled": "enabled",
        "id": "id",
        "score_threshold": "scoreThreshold",
        "sensitivity_level": "sensitivityLevel",
        "status": "status",
    },
)
class RulesetRulesActionParametersOverridesRules:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        score_threshold: typing.Optional[jsii.Number] = None,
        sensitivity_level: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Action to perform in the rule-level override. Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        :param enabled: Defines if the current rule-level override enables or disables the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param id: Rule ID to apply the override to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param score_threshold: Anomaly score threshold to apply in the ruleset rule override. Only applicable to modsecurity-based rulesets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#score_threshold Ruleset#score_threshold}
        :param sensitivity_level: Sensitivity level for a ruleset rule override. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sensitivity_level Ruleset#sensitivity_level}
        :param status: Defines if the current rule-level override enables or disables the rule. Available values: ``enabled``, ``disabled``. Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesRules.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument score_threshold", value=score_threshold, expected_type=type_hints["score_threshold"])
            check_type(argname="argument sensitivity_level", value=sensitivity_level, expected_type=type_hints["sensitivity_level"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if score_threshold is not None:
            self._values["score_threshold"] = score_threshold
        if sensitivity_level is not None:
            self._values["sensitivity_level"] = sensitivity_level
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Action to perform in the rule-level override.

        Available values: ``block``, ``challenge``, ``ddos_dynamic``, ``execute``, ``force_connection_close``, ``js_challenge``, ``log``, ``log_custom_field``, ``managed_challenge``, ``redirect``, ``rewrite``, ``route``, ``score``, ``set_cache_settings``, ``set_config``, ``serve_error``, ``skip``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#action Ruleset#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defines if the current rule-level override enables or disables the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Rule ID to apply the override to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def score_threshold(self) -> typing.Optional[jsii.Number]:
        '''Anomaly score threshold to apply in the ruleset rule override. Only applicable to modsecurity-based rulesets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#score_threshold Ruleset#score_threshold}
        '''
        result = self._values.get("score_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sensitivity_level(self) -> typing.Optional[builtins.str]:
        '''Sensitivity level for a ruleset rule override.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sensitivity_level Ruleset#sensitivity_level}
        '''
        result = self._values.get("sensitivity_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Defines if the current rule-level override enables or disables the rule. Available values: ``enabled``, ``disabled``. Defaults to ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersOverridesRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersOverridesRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesRulesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersOverridesRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersOverridesRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersOverridesRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersOverridesRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersOverridesRulesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersOverridesRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetScoreThreshold")
    def reset_score_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScoreThreshold", []))

    @jsii.member(jsii_name="resetSensitivityLevel")
    def reset_sensitivity_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensitivityLevel", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="scoreThresholdInput")
    def score_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scoreThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="sensitivityLevelInput")
    def sensitivity_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sensitivityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="scoreThreshold")
    def score_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scoreThreshold"))

    @score_threshold.setter
    def score_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "score_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scoreThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="sensitivityLevel")
    def sensitivity_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sensitivityLevel"))

    @sensitivity_level.setter
    def sensitivity_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "sensitivity_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitivityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersOverridesRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersOverridesRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersOverridesRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersOverridesRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersResponse",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "status_code": "statusCode",
    },
)
class RulesetRulesActionParametersResponse:
    def __init__(
        self,
        *,
        content: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Body content to include in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content Ruleset#content}
        :param content_type: HTTP content type to send in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content_type Ruleset#content_type}
        :param status_code: HTTP status code to send in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersResponse.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {}
        if content is not None:
            self._values["content"] = content
        if content_type is not None:
            self._values["content_type"] = content_type
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Body content to include in the response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content Ruleset#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''HTTP content type to send in the response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content_type Ruleset#content_type}
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''HTTP status code to send in the response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersResponseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersResponseList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersResponseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RulesetRulesActionParametersResponseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersResponseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesActionParametersResponseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersResponse]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersResponse]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRulesActionParametersResponse]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesActionParametersResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersResponseOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRulesActionParametersResponse, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRulesActionParametersResponse, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRulesActionParametersResponse, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersServeStale",
    jsii_struct_bases=[],
    name_mapping={"disable_stale_while_updating": "disableStaleWhileUpdating"},
)
class RulesetRulesActionParametersServeStale:
    def __init__(
        self,
        *,
        disable_stale_while_updating: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param disable_stale_while_updating: Disable stale while updating. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_stale_while_updating Ruleset#disable_stale_while_updating}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersServeStale.__init__)
            check_type(argname="argument disable_stale_while_updating", value=disable_stale_while_updating, expected_type=type_hints["disable_stale_while_updating"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disable_stale_while_updating is not None:
            self._values["disable_stale_while_updating"] = disable_stale_while_updating

    @builtins.property
    def disable_stale_while_updating(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable stale while updating.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_stale_while_updating Ruleset#disable_stale_while_updating}
        '''
        result = self._values.get("disable_stale_while_updating")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersServeStale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersServeStaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersServeStaleOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersServeStaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisableStaleWhileUpdating")
    def reset_disable_stale_while_updating(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableStaleWhileUpdating", []))

    @builtins.property
    @jsii.member(jsii_name="disableStaleWhileUpdatingInput")
    def disable_stale_while_updating_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableStaleWhileUpdatingInput"))

    @builtins.property
    @jsii.member(jsii_name="disableStaleWhileUpdating")
    def disable_stale_while_updating(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableStaleWhileUpdating"))

    @disable_stale_while_updating.setter
    def disable_stale_while_updating(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersServeStaleOutputReference, "disable_stale_while_updating").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableStaleWhileUpdating", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersServeStale]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersServeStale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersServeStale],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersServeStaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersSni",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class RulesetRulesActionParametersSni:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Value to define for SNI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersSni.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value to define for SNI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersSni(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersSniOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersSniOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersSniOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersSniOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersSni]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersSni], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersSni],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersSniOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUri",
    jsii_struct_bases=[],
    name_mapping={"origin": "origin", "path": "path", "query": "query"},
)
class RulesetRulesActionParametersUri:
    def __init__(
        self,
        *,
        origin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        path: typing.Optional[typing.Union["RulesetRulesActionParametersUriPath", typing.Dict[str, typing.Any]]] = None,
        query: typing.Optional[typing.Union["RulesetRulesActionParametersUriQuery", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param origin: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin Ruleset#origin}.
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#path Ruleset#path}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#query Ruleset#query}
        '''
        if isinstance(path, dict):
            path = RulesetRulesActionParametersUriPath(**path)
        if isinstance(query, dict):
            query = RulesetRulesActionParametersUriQuery(**query)
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersUri.__init__)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {}
        if origin is not None:
            self._values["origin"] = origin
        if path is not None:
            self._values["path"] = path
        if query is not None:
            self._values["query"] = query

    @builtins.property
    def origin(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin Ruleset#origin}.'''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def path(self) -> typing.Optional["RulesetRulesActionParametersUriPath"]:
        '''path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#path Ruleset#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional["RulesetRulesActionParametersUriPath"], result)

    @builtins.property
    def query(self) -> typing.Optional["RulesetRulesActionParametersUriQuery"]:
        '''query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#query Ruleset#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["RulesetRulesActionParametersUriQuery"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersUri(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersUriOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersUriOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Expression that defines the updated (dynamic) value of the URI path or query string component. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param value: Static string value of the updated URI path or query string component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        value_ = RulesetRulesActionParametersUriPath(
            expression=expression, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPath", [value_]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Expression that defines the updated (dynamic) value of the URI path or query string component. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param value: Static string value of the updated URI path or query string component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        value_ = RulesetRulesActionParametersUriQuery(
            expression=expression, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putQuery", [value_]))

    @jsii.member(jsii_name="resetOrigin")
    def reset_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrigin", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "RulesetRulesActionParametersUriPathOutputReference":
        return typing.cast("RulesetRulesActionParametersUriPathOutputReference", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "RulesetRulesActionParametersUriQueryOutputReference":
        return typing.cast("RulesetRulesActionParametersUriQueryOutputReference", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional["RulesetRulesActionParametersUriPath"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersUriPath"], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional["RulesetRulesActionParametersUriQuery"]:
        return typing.cast(typing.Optional["RulesetRulesActionParametersUriQuery"], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "origin"))

    @origin.setter
    def origin(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriOutputReference, "origin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origin", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersUri]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersUri], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersUri],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriPath",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression", "value": "value"},
)
class RulesetRulesActionParametersUriPath:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Expression that defines the updated (dynamic) value of the URI path or query string component. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param value: Static string value of the updated URI path or query string component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersUriPath.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Expression that defines the updated (dynamic) value of the URI path or query string component.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static string value of the updated URI path or query string component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersUriPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersUriPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriPathOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersUriPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriPathOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriPathOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersUriPath]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersUriPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersUriPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriQuery",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression", "value": "value"},
)
class RulesetRulesActionParametersUriQuery:
    def __init__(
        self,
        *,
        expression: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Expression that defines the updated (dynamic) value of the URI path or query string component. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        :param value: Static string value of the updated URI path or query string component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesActionParametersUriQuery.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Expression that defines the updated (dynamic) value of the URI path or query string component.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#expression Ruleset#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Static string value of the updated URI path or query string component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#value Ruleset#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesActionParametersUriQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesActionParametersUriQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesActionParametersUriQueryOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesActionParametersUriQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriQueryOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriQueryOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesActionParametersUriQuery]:
        return typing.cast(typing.Optional[RulesetRulesActionParametersUriQuery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesActionParametersUriQuery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesActionParametersUriQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesExposedCredentialCheck",
    jsii_struct_bases=[],
    name_mapping={
        "password_expression": "passwordExpression",
        "username_expression": "usernameExpression",
    },
)
class RulesetRulesExposedCredentialCheck:
    def __init__(
        self,
        *,
        password_expression: typing.Optional[builtins.str] = None,
        username_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password_expression: Firewall Rules expression language based on Wireshark display filters for where to check for the "password" value. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#password_expression Ruleset#password_expression}
        :param username_expression: Firewall Rules expression language based on Wireshark display filters for where to check for the "username" value. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#username_expression Ruleset#username_expression}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesExposedCredentialCheck.__init__)
            check_type(argname="argument password_expression", value=password_expression, expected_type=type_hints["password_expression"])
            check_type(argname="argument username_expression", value=username_expression, expected_type=type_hints["username_expression"])
        self._values: typing.Dict[str, typing.Any] = {}
        if password_expression is not None:
            self._values["password_expression"] = password_expression
        if username_expression is not None:
            self._values["username_expression"] = username_expression

    @builtins.property
    def password_expression(self) -> typing.Optional[builtins.str]:
        '''Firewall Rules expression language based on Wireshark display filters for where to check for the "password" value.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#password_expression Ruleset#password_expression}
        '''
        result = self._values.get("password_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username_expression(self) -> typing.Optional[builtins.str]:
        '''Firewall Rules expression language based on Wireshark display filters for where to check for the "username" value.

        Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#username_expression Ruleset#username_expression}
        '''
        result = self._values.get("username_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesExposedCredentialCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesExposedCredentialCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesExposedCredentialCheckOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesExposedCredentialCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPasswordExpression")
    def reset_password_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordExpression", []))

    @jsii.member(jsii_name="resetUsernameExpression")
    def reset_username_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameExpression", []))

    @builtins.property
    @jsii.member(jsii_name="passwordExpressionInput")
    def password_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameExpressionInput")
    def username_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordExpression")
    def password_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordExpression"))

    @password_expression.setter
    def password_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesExposedCredentialCheckOutputReference, "password_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passwordExpression", value)

    @builtins.property
    @jsii.member(jsii_name="usernameExpression")
    def username_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernameExpression"))

    @username_expression.setter
    def username_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesExposedCredentialCheckOutputReference, "username_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameExpression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesExposedCredentialCheck]:
        return typing.cast(typing.Optional[RulesetRulesExposedCredentialCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RulesetRulesExposedCredentialCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesExposedCredentialCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RulesetRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RulesetRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RulesetRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesLogging",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "status": "status"},
)
class RulesetRulesLogging:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Override the default logging behavior when a rule is matched. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param status: Override the default logging behavior when a rule is matched. Available values: ``enabled``, ``disabled``. Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesLogging.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Override the default logging behavior when a rule is matched.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Override the default logging behavior when a rule is matched. Available values: ``enabled``, ``disabled``. Defaults to ``""``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesLoggingOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesLoggingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesLoggingOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesLoggingOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesLogging]:
        return typing.cast(typing.Optional[RulesetRulesLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RulesetRulesLogging]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesLoggingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RulesetRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putActionParameters")
    def put_action_parameters(
        self,
        *,
        automatic_https_rewrites: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autominify: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersAutominify, typing.Dict[str, typing.Any]]]]] = None,
        bic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        browser_ttl: typing.Optional[typing.Union[RulesetRulesActionParametersBrowserTtl, typing.Dict[str, typing.Any]]] = None,
        cache: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_key: typing.Optional[typing.Union[RulesetRulesActionParametersCacheKey, typing.Dict[str, typing.Any]]] = None,
        content: typing.Optional[builtins.str] = None,
        content_type: typing.Optional[builtins.str] = None,
        cookie_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        disable_apps: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_railgun: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_zaraz: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        edge_ttl: typing.Optional[typing.Union[RulesetRulesActionParametersEdgeTtl, typing.Dict[str, typing.Any]]] = None,
        email_obfuscation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        from_list: typing.Optional[typing.Union[RulesetRulesActionParametersFromList, typing.Dict[str, typing.Any]]] = None,
        from_value: typing.Optional[typing.Union[RulesetRulesActionParametersFromValue, typing.Dict[str, typing.Any]]] = None,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersHeaders, typing.Dict[str, typing.Any]]]]] = None,
        host_header: typing.Optional[builtins.str] = None,
        hotlink_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        increment: typing.Optional[jsii.Number] = None,
        matched_data: typing.Optional[typing.Union[RulesetRulesActionParametersMatchedData, typing.Dict[str, typing.Any]]] = None,
        mirage: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        opportunistic_encryption: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        origin: typing.Optional[typing.Union[RulesetRulesActionParametersOrigin, typing.Dict[str, typing.Any]]] = None,
        origin_error_page_passthru: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        overrides: typing.Optional[typing.Union[RulesetRulesActionParametersOverrides, typing.Dict[str, typing.Any]]] = None,
        phases: typing.Optional[typing.Sequence[builtins.str]] = None,
        polish: typing.Optional[builtins.str] = None,
        products: typing.Optional[typing.Sequence[builtins.str]] = None,
        request_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        respect_strong_etags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        response: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[RulesetRulesActionParametersResponse, typing.Dict[str, typing.Any]]]]] = None,
        response_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        rocket_loader: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        rules: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ruleset: typing.Optional[builtins.str] = None,
        rulesets: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_level: typing.Optional[builtins.str] = None,
        server_side_excludes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        serve_stale: typing.Optional[typing.Union[RulesetRulesActionParametersServeStale, typing.Dict[str, typing.Any]]] = None,
        sni: typing.Optional[typing.Union[RulesetRulesActionParametersSni, typing.Dict[str, typing.Any]]] = None,
        ssl: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
        sxg: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uri: typing.Optional[typing.Union[RulesetRulesActionParametersUri, typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param automatic_https_rewrites: Turn on or off Cloudflare Automatic HTTPS rewrites. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#automatic_https_rewrites Ruleset#automatic_https_rewrites}
        :param autominify: autominify block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#autominify Ruleset#autominify}
        :param bic: Inspect the visitor's browser for headers commonly associated with spammers and certain bots. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#bic Ruleset#bic}
        :param browser_ttl: browser_ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#browser_ttl Ruleset#browser_ttl}
        :param cache: Whether to cache if expression matches. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache Ruleset#cache}
        :param cache_key: cache_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cache_key Ruleset#cache_key}
        :param content: Content of the custom error response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content Ruleset#content}
        :param content_type: Content-Type of the custom error response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#content_type Ruleset#content_type}
        :param cookie_fields: List of cookie values to include as part of custom fields logging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#cookie_fields Ruleset#cookie_fields}
        :param disable_apps: Turn off all active Cloudflare Apps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_apps Ruleset#disable_apps}
        :param disable_railgun: Turn off railgun feature of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_railgun Ruleset#disable_railgun}
        :param disable_zaraz: Turn off zaraz feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#disable_zaraz Ruleset#disable_zaraz}
        :param edge_ttl: edge_ttl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#edge_ttl Ruleset#edge_ttl}
        :param email_obfuscation: Turn on or off the Cloudflare Email Obfuscation feature of the Cloudflare Scrape Shield app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#email_obfuscation Ruleset#email_obfuscation}
        :param from_list: from_list block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from_list Ruleset#from_list}
        :param from_value: from_value block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#from_value Ruleset#from_value}
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#headers Ruleset#headers}
        :param host_header: Host Header that request origin receives. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#host_header Ruleset#host_header}
        :param hotlink_protection: Turn on or off the hotlink protection feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#hotlink_protection Ruleset#hotlink_protection}
        :param id: Identifier of the action parameter to modify. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#id Ruleset#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param increment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#increment Ruleset#increment}.
        :param matched_data: matched_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#matched_data Ruleset#matched_data}
        :param mirage: Turn on or off Cloudflare Mirage of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mirage Ruleset#mirage}
        :param opportunistic_encryption: Turn on or off the Cloudflare Opportunistic Encryption feature of the Edge Certificates tab in the Cloudflare SSL/TLS app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#opportunistic_encryption Ruleset#opportunistic_encryption}
        :param origin: origin block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin Ruleset#origin}
        :param origin_error_page_passthru: Pass-through error page for origin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#origin_error_page_passthru Ruleset#origin_error_page_passthru}
        :param overrides: overrides block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#overrides Ruleset#overrides}
        :param phases: Point in the request/response lifecycle where the ruleset will be created. Available values: ``ddos_l4``, ``ddos_l7``, ``http_custom_errors``, ``http_log_custom_fields``, ``http_request_cache_settings``, ``http_request_firewall_custom``, ``http_request_firewall_managed``, ``http_request_late_transform``, ``http_request_late_transform_managed``, ``http_request_main``, ``http_request_origin``, ``http_request_dynamic_redirect``, ``http_request_redirect``, ``http_request_sanitize``, ``http_request_transform``, ``http_response_firewall_managed``, ``http_response_headers_transform``, ``http_response_headers_transform_managed``, ``magic_transit``, ``http_ratelimit``, ``http_request_sbfm``, ``http_config_settings``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#phases Ruleset#phases}
        :param polish: Apply options from the Polish feature of the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#polish Ruleset#polish}
        :param products: Products to target with the actions. Available values: ``bic``, ``hot``, ``ratelimit``, ``securityLevel``, ``uablock``, ``waf``, ``zonelockdown``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#products Ruleset#products}
        :param request_fields: List of request headers to include as part of custom fields logging, in lowercase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#request_fields Ruleset#request_fields}
        :param respect_strong_etags: Respect strong ETags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#respect_strong_etags Ruleset#respect_strong_etags}
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#response Ruleset#response}
        :param response_fields: List of response headers to include as part of custom fields logging, in lowercase. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#response_fields Ruleset#response_fields}
        :param rocket_loader: Turn on or off Cloudflare Rocket Loader in the Cloudflare Speed app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rocket_loader Ruleset#rocket_loader}
        :param rules: Map of managed WAF rule ID to comma-delimited string of ruleset rule IDs. Example: ``rules = { "efb7b8c949ac4650a09736fc376e9aee" = "5de7edfa648c4d6891dc3e7f84534ffa,e3a567afc347477d9702d9047e97d760" }``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rules Ruleset#rules}
        :param ruleset: Which ruleset ID to target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ruleset Ruleset#ruleset}
        :param rulesets: List of managed WAF rule IDs to target. Only valid when the ``"action"`` is set to skip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#rulesets Ruleset#rulesets}
        :param security_level: Control options for the Security Level feature from the Security app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#security_level Ruleset#security_level}
        :param server_side_excludes: Turn on or off the Server Side Excludes feature of the Cloudflare Scrape Shield app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#server_side_excludes Ruleset#server_side_excludes}
        :param serve_stale: serve_stale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#serve_stale Ruleset#serve_stale}
        :param sni: sni block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sni Ruleset#sni}
        :param ssl: Control options for the SSL feature of the Edge Certificates tab in the Cloudflare SSL/TLS app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#ssl Ruleset#ssl}
        :param status_code: HTTP status code of the custom error response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status_code Ruleset#status_code}
        :param sxg: Turn on or off the SXG feature. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#sxg Ruleset#sxg}
        :param uri: uri block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#uri Ruleset#uri}
        :param version: Version of the ruleset to deploy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#version Ruleset#version}
        '''
        value = RulesetRulesActionParameters(
            automatic_https_rewrites=automatic_https_rewrites,
            autominify=autominify,
            bic=bic,
            browser_ttl=browser_ttl,
            cache=cache,
            cache_key=cache_key,
            content=content,
            content_type=content_type,
            cookie_fields=cookie_fields,
            disable_apps=disable_apps,
            disable_railgun=disable_railgun,
            disable_zaraz=disable_zaraz,
            edge_ttl=edge_ttl,
            email_obfuscation=email_obfuscation,
            from_list=from_list,
            from_value=from_value,
            headers=headers,
            host_header=host_header,
            hotlink_protection=hotlink_protection,
            id=id,
            increment=increment,
            matched_data=matched_data,
            mirage=mirage,
            opportunistic_encryption=opportunistic_encryption,
            origin=origin,
            origin_error_page_passthru=origin_error_page_passthru,
            overrides=overrides,
            phases=phases,
            polish=polish,
            products=products,
            request_fields=request_fields,
            respect_strong_etags=respect_strong_etags,
            response=response,
            response_fields=response_fields,
            rocket_loader=rocket_loader,
            rules=rules,
            ruleset=ruleset,
            rulesets=rulesets,
            security_level=security_level,
            server_side_excludes=server_side_excludes,
            serve_stale=serve_stale,
            sni=sni,
            ssl=ssl,
            status_code=status_code,
            sxg=sxg,
            uri=uri,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putActionParameters", [value]))

    @jsii.member(jsii_name="putExposedCredentialCheck")
    def put_exposed_credential_check(
        self,
        *,
        password_expression: typing.Optional[builtins.str] = None,
        username_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password_expression: Firewall Rules expression language based on Wireshark display filters for where to check for the "password" value. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#password_expression Ruleset#password_expression}
        :param username_expression: Firewall Rules expression language based on Wireshark display filters for where to check for the "username" value. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#username_expression Ruleset#username_expression}
        '''
        value = RulesetRulesExposedCredentialCheck(
            password_expression=password_expression,
            username_expression=username_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putExposedCredentialCheck", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Override the default logging behavior when a rule is matched. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#enabled Ruleset#enabled}
        :param status: Override the default logging behavior when a rule is matched. Available values: ``enabled``, ``disabled``. Defaults to ``""``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#status Ruleset#status}
        '''
        value = RulesetRulesLogging(enabled=enabled, status=status)

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putRatelimit")
    def put_ratelimit(
        self,
        *,
        characteristics: typing.Optional[typing.Sequence[builtins.str]] = None,
        counting_expression: typing.Optional[builtins.str] = None,
        mitigation_timeout: typing.Optional[jsii.Number] = None,
        period: typing.Optional[jsii.Number] = None,
        requests_per_period: typing.Optional[jsii.Number] = None,
        requests_to_origin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param characteristics: List of parameters that define how Cloudflare tracks the request rate for this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#characteristics Ruleset#characteristics}
        :param counting_expression: Criteria for counting HTTP requests to trigger the Rate Limiting action. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#counting_expression Ruleset#counting_expression}
        :param mitigation_timeout: Once the request rate is reached, the Rate Limiting rule blocks further requests for the period of time defined in this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mitigation_timeout Ruleset#mitigation_timeout}
        :param period: The period of time to consider (in seconds) when evaluating the request rate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#period Ruleset#period}
        :param requests_per_period: The number of requests over the period of time that will trigger the Rate Limiting rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#requests_per_period Ruleset#requests_per_period}
        :param requests_to_origin: Whether to include requests to origin within the Rate Limiting count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#requests_to_origin Ruleset#requests_to_origin}
        '''
        value = RulesetRulesRatelimit(
            characteristics=characteristics,
            counting_expression=counting_expression,
            mitigation_timeout=mitigation_timeout,
            period=period,
            requests_per_period=requests_per_period,
            requests_to_origin=requests_to_origin,
        )

        return typing.cast(None, jsii.invoke(self, "putRatelimit", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetActionParameters")
    def reset_action_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionParameters", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExposedCredentialCheck")
    def reset_exposed_credential_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposedCredentialCheck", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetRatelimit")
    def reset_ratelimit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRatelimit", []))

    @builtins.property
    @jsii.member(jsii_name="actionParameters")
    def action_parameters(self) -> RulesetRulesActionParametersOutputReference:
        return typing.cast(RulesetRulesActionParametersOutputReference, jsii.get(self, "actionParameters"))

    @builtins.property
    @jsii.member(jsii_name="exposedCredentialCheck")
    def exposed_credential_check(
        self,
    ) -> RulesetRulesExposedCredentialCheckOutputReference:
        return typing.cast(RulesetRulesExposedCredentialCheckOutputReference, jsii.get(self, "exposedCredentialCheck"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> RulesetRulesLoggingOutputReference:
        return typing.cast(RulesetRulesLoggingOutputReference, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="ratelimit")
    def ratelimit(self) -> "RulesetRulesRatelimitOutputReference":
        return typing.cast("RulesetRulesRatelimitOutputReference", jsii.get(self, "ratelimit"))

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="actionParametersInput")
    def action_parameters_input(self) -> typing.Optional[RulesetRulesActionParameters]:
        return typing.cast(typing.Optional[RulesetRulesActionParameters], jsii.get(self, "actionParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="exposedCredentialCheckInput")
    def exposed_credential_check_input(
        self,
    ) -> typing.Optional[RulesetRulesExposedCredentialCheck]:
        return typing.cast(typing.Optional[RulesetRulesExposedCredentialCheck], jsii.get(self, "exposedCredentialCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[RulesetRulesLogging]:
        return typing.cast(typing.Optional[RulesetRulesLogging], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="ratelimitInput")
    def ratelimit_input(self) -> typing.Optional["RulesetRulesRatelimit"]:
        return typing.cast(typing.Optional["RulesetRulesRatelimit"], jsii.get(self, "ratelimitInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RulesetRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RulesetRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RulesetRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesRatelimit",
    jsii_struct_bases=[],
    name_mapping={
        "characteristics": "characteristics",
        "counting_expression": "countingExpression",
        "mitigation_timeout": "mitigationTimeout",
        "period": "period",
        "requests_per_period": "requestsPerPeriod",
        "requests_to_origin": "requestsToOrigin",
    },
)
class RulesetRulesRatelimit:
    def __init__(
        self,
        *,
        characteristics: typing.Optional[typing.Sequence[builtins.str]] = None,
        counting_expression: typing.Optional[builtins.str] = None,
        mitigation_timeout: typing.Optional[jsii.Number] = None,
        period: typing.Optional[jsii.Number] = None,
        requests_per_period: typing.Optional[jsii.Number] = None,
        requests_to_origin: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param characteristics: List of parameters that define how Cloudflare tracks the request rate for this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#characteristics Ruleset#characteristics}
        :param counting_expression: Criteria for counting HTTP requests to trigger the Rate Limiting action. Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#counting_expression Ruleset#counting_expression}
        :param mitigation_timeout: Once the request rate is reached, the Rate Limiting rule blocks further requests for the period of time defined in this field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mitigation_timeout Ruleset#mitigation_timeout}
        :param period: The period of time to consider (in seconds) when evaluating the request rate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#period Ruleset#period}
        :param requests_per_period: The number of requests over the period of time that will trigger the Rate Limiting rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#requests_per_period Ruleset#requests_per_period}
        :param requests_to_origin: Whether to include requests to origin within the Rate Limiting count. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#requests_to_origin Ruleset#requests_to_origin}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RulesetRulesRatelimit.__init__)
            check_type(argname="argument characteristics", value=characteristics, expected_type=type_hints["characteristics"])
            check_type(argname="argument counting_expression", value=counting_expression, expected_type=type_hints["counting_expression"])
            check_type(argname="argument mitigation_timeout", value=mitigation_timeout, expected_type=type_hints["mitigation_timeout"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument requests_per_period", value=requests_per_period, expected_type=type_hints["requests_per_period"])
            check_type(argname="argument requests_to_origin", value=requests_to_origin, expected_type=type_hints["requests_to_origin"])
        self._values: typing.Dict[str, typing.Any] = {}
        if characteristics is not None:
            self._values["characteristics"] = characteristics
        if counting_expression is not None:
            self._values["counting_expression"] = counting_expression
        if mitigation_timeout is not None:
            self._values["mitigation_timeout"] = mitigation_timeout
        if period is not None:
            self._values["period"] = period
        if requests_per_period is not None:
            self._values["requests_per_period"] = requests_per_period
        if requests_to_origin is not None:
            self._values["requests_to_origin"] = requests_to_origin

    @builtins.property
    def characteristics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of parameters that define how Cloudflare tracks the request rate for this rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#characteristics Ruleset#characteristics}
        '''
        result = self._values.get("characteristics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def counting_expression(self) -> typing.Optional[builtins.str]:
        '''Criteria for counting HTTP requests to trigger the Rate Limiting action.

        Uses the Firewall Rules expression language based on Wireshark display filters. Refer to the `Firewall Rules language <https://developers.cloudflare.com/firewall/cf-firewall-language>`_ documentation for all available fields, operators, and functions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#counting_expression Ruleset#counting_expression}
        '''
        result = self._values.get("counting_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mitigation_timeout(self) -> typing.Optional[jsii.Number]:
        '''Once the request rate is reached, the Rate Limiting rule blocks further requests for the period of time defined in this field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#mitigation_timeout Ruleset#mitigation_timeout}
        '''
        result = self._values.get("mitigation_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        '''The period of time to consider (in seconds) when evaluating the request rate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#period Ruleset#period}
        '''
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests_per_period(self) -> typing.Optional[jsii.Number]:
        '''The number of requests over the period of time that will trigger the Rate Limiting rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#requests_per_period Ruleset#requests_per_period}
        '''
        result = self._values.get("requests_per_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def requests_to_origin(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to include requests to origin within the Rate Limiting count.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/ruleset#requests_to_origin Ruleset#requests_to_origin}
        '''
        result = self._values.get("requests_to_origin")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetRulesRatelimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RulesetRulesRatelimitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.ruleset.RulesetRulesRatelimitOutputReference",
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
            type_hints = typing.get_type_hints(RulesetRulesRatelimitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCharacteristics")
    def reset_characteristics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCharacteristics", []))

    @jsii.member(jsii_name="resetCountingExpression")
    def reset_counting_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountingExpression", []))

    @jsii.member(jsii_name="resetMitigationTimeout")
    def reset_mitigation_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMitigationTimeout", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetRequestsPerPeriod")
    def reset_requests_per_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsPerPeriod", []))

    @jsii.member(jsii_name="resetRequestsToOrigin")
    def reset_requests_to_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestsToOrigin", []))

    @builtins.property
    @jsii.member(jsii_name="characteristicsInput")
    def characteristics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "characteristicsInput"))

    @builtins.property
    @jsii.member(jsii_name="countingExpressionInput")
    def counting_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countingExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="mitigationTimeoutInput")
    def mitigation_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mitigationTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsPerPeriodInput")
    def requests_per_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requestsPerPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="requestsToOriginInput")
    def requests_to_origin_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requestsToOriginInput"))

    @builtins.property
    @jsii.member(jsii_name="characteristics")
    def characteristics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "characteristics"))

    @characteristics.setter
    def characteristics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "characteristics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "characteristics", value)

    @builtins.property
    @jsii.member(jsii_name="countingExpression")
    def counting_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countingExpression"))

    @counting_expression.setter
    def counting_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "counting_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countingExpression", value)

    @builtins.property
    @jsii.member(jsii_name="mitigationTimeout")
    def mitigation_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mitigationTimeout"))

    @mitigation_timeout.setter
    def mitigation_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "mitigation_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mitigationTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="requestsPerPeriod")
    def requests_per_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requestsPerPeriod"))

    @requests_per_period.setter
    def requests_per_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "requests_per_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsPerPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="requestsToOrigin")
    def requests_to_origin(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requestsToOrigin"))

    @requests_to_origin.setter
    def requests_to_origin(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "requests_to_origin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestsToOrigin", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RulesetRulesRatelimit]:
        return typing.cast(typing.Optional[RulesetRulesRatelimit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RulesetRulesRatelimit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RulesetRulesRatelimitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Ruleset",
    "RulesetConfig",
    "RulesetRules",
    "RulesetRulesActionParameters",
    "RulesetRulesActionParametersAutominify",
    "RulesetRulesActionParametersAutominifyList",
    "RulesetRulesActionParametersAutominifyOutputReference",
    "RulesetRulesActionParametersBrowserTtl",
    "RulesetRulesActionParametersBrowserTtlOutputReference",
    "RulesetRulesActionParametersCacheKey",
    "RulesetRulesActionParametersCacheKeyCustomKey",
    "RulesetRulesActionParametersCacheKeyCustomKeyCookie",
    "RulesetRulesActionParametersCacheKeyCustomKeyCookieOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyHeader",
    "RulesetRulesActionParametersCacheKeyCustomKeyHeaderOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyHost",
    "RulesetRulesActionParametersCacheKeyCustomKeyHostOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyQueryString",
    "RulesetRulesActionParametersCacheKeyCustomKeyQueryStringOutputReference",
    "RulesetRulesActionParametersCacheKeyCustomKeyUser",
    "RulesetRulesActionParametersCacheKeyCustomKeyUserOutputReference",
    "RulesetRulesActionParametersCacheKeyOutputReference",
    "RulesetRulesActionParametersEdgeTtl",
    "RulesetRulesActionParametersEdgeTtlOutputReference",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtl",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlList",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlOutputReference",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRange",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeList",
    "RulesetRulesActionParametersEdgeTtlStatusCodeTtlStatusCodeRangeOutputReference",
    "RulesetRulesActionParametersFromList",
    "RulesetRulesActionParametersFromListOutputReference",
    "RulesetRulesActionParametersFromValue",
    "RulesetRulesActionParametersFromValueOutputReference",
    "RulesetRulesActionParametersFromValueTargetUrl",
    "RulesetRulesActionParametersFromValueTargetUrlOutputReference",
    "RulesetRulesActionParametersHeaders",
    "RulesetRulesActionParametersHeadersList",
    "RulesetRulesActionParametersHeadersOutputReference",
    "RulesetRulesActionParametersMatchedData",
    "RulesetRulesActionParametersMatchedDataOutputReference",
    "RulesetRulesActionParametersOrigin",
    "RulesetRulesActionParametersOriginOutputReference",
    "RulesetRulesActionParametersOutputReference",
    "RulesetRulesActionParametersOverrides",
    "RulesetRulesActionParametersOverridesCategories",
    "RulesetRulesActionParametersOverridesCategoriesList",
    "RulesetRulesActionParametersOverridesCategoriesOutputReference",
    "RulesetRulesActionParametersOverridesOutputReference",
    "RulesetRulesActionParametersOverridesRules",
    "RulesetRulesActionParametersOverridesRulesList",
    "RulesetRulesActionParametersOverridesRulesOutputReference",
    "RulesetRulesActionParametersResponse",
    "RulesetRulesActionParametersResponseList",
    "RulesetRulesActionParametersResponseOutputReference",
    "RulesetRulesActionParametersServeStale",
    "RulesetRulesActionParametersServeStaleOutputReference",
    "RulesetRulesActionParametersSni",
    "RulesetRulesActionParametersSniOutputReference",
    "RulesetRulesActionParametersUri",
    "RulesetRulesActionParametersUriOutputReference",
    "RulesetRulesActionParametersUriPath",
    "RulesetRulesActionParametersUriPathOutputReference",
    "RulesetRulesActionParametersUriQuery",
    "RulesetRulesActionParametersUriQueryOutputReference",
    "RulesetRulesExposedCredentialCheck",
    "RulesetRulesExposedCredentialCheckOutputReference",
    "RulesetRulesList",
    "RulesetRulesLogging",
    "RulesetRulesLoggingOutputReference",
    "RulesetRulesOutputReference",
    "RulesetRulesRatelimit",
    "RulesetRulesRatelimitOutputReference",
]

publication.publish()
