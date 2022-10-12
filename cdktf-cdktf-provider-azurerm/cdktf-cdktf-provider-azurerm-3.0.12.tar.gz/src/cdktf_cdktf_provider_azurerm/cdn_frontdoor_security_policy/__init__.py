'''
# `azurerm_cdn_frontdoor_security_policy`

Refer to the Terraform Registory for docs: [`azurerm_cdn_frontdoor_security_policy`](https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy).
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


class CdnFrontdoorSecurityPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy azurerm_cdn_frontdoor_security_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cdn_frontdoor_profile_id: builtins.str,
        name: builtins.str,
        security_policies: typing.Union["CdnFrontdoorSecurityPolicySecurityPolicies", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorSecurityPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy azurerm_cdn_frontdoor_security_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cdn_frontdoor_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_profile_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_profile_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#name CdnFrontdoorSecurityPolicy#name}.
        :param security_policies: security_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#security_policies CdnFrontdoorSecurityPolicy#security_policies}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#id CdnFrontdoorSecurityPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#timeouts CdnFrontdoorSecurityPolicy#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnFrontdoorSecurityPolicyConfig(
            cdn_frontdoor_profile_id=cdn_frontdoor_profile_id,
            name=name,
            security_policies=security_policies,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSecurityPolicies")
    def put_security_policies(
        self,
        *,
        firewall: typing.Union["CdnFrontdoorSecurityPolicySecurityPoliciesFirewall", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param firewall: firewall block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#firewall CdnFrontdoorSecurityPolicy#firewall}
        '''
        value = CdnFrontdoorSecurityPolicySecurityPolicies(firewall=firewall)

        return typing.cast(None, jsii.invoke(self, "putSecurityPolicies", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#create CdnFrontdoorSecurityPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#delete CdnFrontdoorSecurityPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#read CdnFrontdoorSecurityPolicy#read}.
        '''
        value = CdnFrontdoorSecurityPolicyTimeouts(
            create=create, delete=delete, read=read
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="securityPolicies")
    def security_policies(
        self,
    ) -> "CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference":
        return typing.cast("CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference", jsii.get(self, "securityPolicies"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnFrontdoorSecurityPolicyTimeoutsOutputReference":
        return typing.cast("CdnFrontdoorSecurityPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorProfileIdInput")
    def cdn_frontdoor_profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorProfileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityPoliciesInput")
    def security_policies_input(
        self,
    ) -> typing.Optional["CdnFrontdoorSecurityPolicySecurityPolicies"]:
        return typing.cast(typing.Optional["CdnFrontdoorSecurityPolicySecurityPolicies"], jsii.get(self, "securityPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CdnFrontdoorSecurityPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnFrontdoorSecurityPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorProfileId")
    def cdn_frontdoor_profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorProfileId"))

    @cdn_frontdoor_profile_id.setter
    def cdn_frontdoor_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicy, "cdn_frontdoor_profile_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cdn_frontdoor_profile_id": "cdnFrontdoorProfileId",
        "name": "name",
        "security_policies": "securityPolicies",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class CdnFrontdoorSecurityPolicyConfig(cdktf.TerraformMetaArguments):
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
        cdn_frontdoor_profile_id: builtins.str,
        name: builtins.str,
        security_policies: typing.Union["CdnFrontdoorSecurityPolicySecurityPolicies", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorSecurityPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cdn_frontdoor_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_profile_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_profile_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#name CdnFrontdoorSecurityPolicy#name}.
        :param security_policies: security_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#security_policies CdnFrontdoorSecurityPolicy#security_policies}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#id CdnFrontdoorSecurityPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#timeouts CdnFrontdoorSecurityPolicy#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(security_policies, dict):
            security_policies = CdnFrontdoorSecurityPolicySecurityPolicies(**security_policies)
        if isinstance(timeouts, dict):
            timeouts = CdnFrontdoorSecurityPolicyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cdn_frontdoor_profile_id", value=cdn_frontdoor_profile_id, expected_type=type_hints["cdn_frontdoor_profile_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument security_policies", value=security_policies, expected_type=type_hints["security_policies"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cdn_frontdoor_profile_id": cdn_frontdoor_profile_id,
            "name": name,
            "security_policies": security_policies,
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
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def cdn_frontdoor_profile_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_profile_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_profile_id}.'''
        result = self._values.get("cdn_frontdoor_profile_id")
        assert result is not None, "Required property 'cdn_frontdoor_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#name CdnFrontdoorSecurityPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_policies(self) -> "CdnFrontdoorSecurityPolicySecurityPolicies":
        '''security_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#security_policies CdnFrontdoorSecurityPolicy#security_policies}
        '''
        result = self._values.get("security_policies")
        assert result is not None, "Required property 'security_policies' is missing"
        return typing.cast("CdnFrontdoorSecurityPolicySecurityPolicies", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#id CdnFrontdoorSecurityPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnFrontdoorSecurityPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#timeouts CdnFrontdoorSecurityPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnFrontdoorSecurityPolicyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorSecurityPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPolicies",
    jsii_struct_bases=[],
    name_mapping={"firewall": "firewall"},
)
class CdnFrontdoorSecurityPolicySecurityPolicies:
    def __init__(
        self,
        *,
        firewall: typing.Union["CdnFrontdoorSecurityPolicySecurityPoliciesFirewall", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param firewall: firewall block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#firewall CdnFrontdoorSecurityPolicy#firewall}
        '''
        if isinstance(firewall, dict):
            firewall = CdnFrontdoorSecurityPolicySecurityPoliciesFirewall(**firewall)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPolicies.__init__)
            check_type(argname="argument firewall", value=firewall, expected_type=type_hints["firewall"])
        self._values: typing.Dict[str, typing.Any] = {
            "firewall": firewall,
        }

    @builtins.property
    def firewall(self) -> "CdnFrontdoorSecurityPolicySecurityPoliciesFirewall":
        '''firewall block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#firewall CdnFrontdoorSecurityPolicy#firewall}
        '''
        result = self._values.get("firewall")
        assert result is not None, "Required property 'firewall' is missing"
        return typing.cast("CdnFrontdoorSecurityPolicySecurityPoliciesFirewall", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorSecurityPolicySecurityPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewall",
    jsii_struct_bases=[],
    name_mapping={
        "association": "association",
        "cdn_frontdoor_firewall_policy_id": "cdnFrontdoorFirewallPolicyId",
    },
)
class CdnFrontdoorSecurityPolicySecurityPoliciesFirewall:
    def __init__(
        self,
        *,
        association: typing.Union["CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation", typing.Dict[str, typing.Any]],
        cdn_frontdoor_firewall_policy_id: builtins.str,
    ) -> None:
        '''
        :param association: association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#association CdnFrontdoorSecurityPolicy#association}
        :param cdn_frontdoor_firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_firewall_policy_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_firewall_policy_id}.
        '''
        if isinstance(association, dict):
            association = CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation(**association)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewall.__init__)
            check_type(argname="argument association", value=association, expected_type=type_hints["association"])
            check_type(argname="argument cdn_frontdoor_firewall_policy_id", value=cdn_frontdoor_firewall_policy_id, expected_type=type_hints["cdn_frontdoor_firewall_policy_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "association": association,
            "cdn_frontdoor_firewall_policy_id": cdn_frontdoor_firewall_policy_id,
        }

    @builtins.property
    def association(
        self,
    ) -> "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation":
        '''association block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#association CdnFrontdoorSecurityPolicy#association}
        '''
        result = self._values.get("association")
        assert result is not None, "Required property 'association' is missing"
        return typing.cast("CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation", result)

    @builtins.property
    def cdn_frontdoor_firewall_policy_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_firewall_policy_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_firewall_policy_id}.'''
        result = self._values.get("cdn_frontdoor_firewall_policy_id")
        assert result is not None, "Required property 'cdn_frontdoor_firewall_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorSecurityPolicySecurityPoliciesFirewall(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation",
    jsii_struct_bases=[],
    name_mapping={"domain": "domain", "patterns_to_match": "patternsToMatch"},
)
class CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation:
    def __init__(
        self,
        *,
        domain: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain", typing.Dict[str, typing.Any]]]],
        patterns_to_match: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param domain: domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#domain CdnFrontdoorSecurityPolicy#domain}
        :param patterns_to_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#patterns_to_match CdnFrontdoorSecurityPolicy#patterns_to_match}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation.__init__)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument patterns_to_match", value=patterns_to_match, expected_type=type_hints["patterns_to_match"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain": domain,
            "patterns_to_match": patterns_to_match,
        }

    @builtins.property
    def domain(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain"]]:
        '''domain block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#domain CdnFrontdoorSecurityPolicy#domain}
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain"]], result)

    @builtins.property
    def patterns_to_match(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#patterns_to_match CdnFrontdoorSecurityPolicy#patterns_to_match}.'''
        result = self._values.get("patterns_to_match")
        assert result is not None, "Required property 'patterns_to_match' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain",
    jsii_struct_bases=[],
    name_mapping={"cdn_frontdoor_domain_id": "cdnFrontdoorDomainId"},
)
class CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain:
    def __init__(self, *, cdn_frontdoor_domain_id: builtins.str) -> None:
        '''
        :param cdn_frontdoor_domain_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_domain_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_domain_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain.__init__)
            check_type(argname="argument cdn_frontdoor_domain_id", value=cdn_frontdoor_domain_id, expected_type=type_hints["cdn_frontdoor_domain_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "cdn_frontdoor_domain_id": cdn_frontdoor_domain_id,
        }

    @builtins.property
    def cdn_frontdoor_domain_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_domain_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_domain_id}.'''
        result = self._values.get("cdn_frontdoor_domain_id")
        assert result is not None, "Required property 'cdn_frontdoor_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "active"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorDomainIdInput")
    def cdn_frontdoor_domain_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorDomainIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorDomainId")
    def cdn_frontdoor_domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorDomainId"))

    @cdn_frontdoor_domain_id.setter
    def cdn_frontdoor_domain_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference, "cdn_frontdoor_domain_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorDomainId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDomain")
    def put_domain(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference.put_domain)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDomain", [value]))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(
        self,
    ) -> CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList:
        return typing.cast(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain]]], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="patternsToMatchInput")
    def patterns_to_match_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternsToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="patternsToMatch")
    def patterns_to_match(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "patternsToMatch"))

    @patterns_to_match.setter
    def patterns_to_match(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference, "patterns_to_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patternsToMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation]:
        return typing.cast(typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAssociation")
    def put_association(
        self,
        *,
        domain: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain, typing.Dict[str, typing.Any]]]],
        patterns_to_match: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param domain: domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#domain CdnFrontdoorSecurityPolicy#domain}
        :param patterns_to_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#patterns_to_match CdnFrontdoorSecurityPolicy#patterns_to_match}.
        '''
        value = CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation(
            domain=domain, patterns_to_match=patterns_to_match
        )

        return typing.cast(None, jsii.invoke(self, "putAssociation", [value]))

    @builtins.property
    @jsii.member(jsii_name="association")
    def association(
        self,
    ) -> CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference:
        return typing.cast(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference, jsii.get(self, "association"))

    @builtins.property
    @jsii.member(jsii_name="associationInput")
    def association_input(
        self,
    ) -> typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation]:
        return typing.cast(typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation], jsii.get(self, "associationInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorFirewallPolicyIdInput")
    def cdn_frontdoor_firewall_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorFirewallPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorFirewallPolicyId")
    def cdn_frontdoor_firewall_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorFirewallPolicyId"))

    @cdn_frontdoor_firewall_policy_id.setter
    def cdn_frontdoor_firewall_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference, "cdn_frontdoor_firewall_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorFirewallPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewall]:
        return typing.cast(typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewall], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewall],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFirewall")
    def put_firewall(
        self,
        *,
        association: typing.Union[CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation, typing.Dict[str, typing.Any]],
        cdn_frontdoor_firewall_policy_id: builtins.str,
    ) -> None:
        '''
        :param association: association block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#association CdnFrontdoorSecurityPolicy#association}
        :param cdn_frontdoor_firewall_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#cdn_frontdoor_firewall_policy_id CdnFrontdoorSecurityPolicy#cdn_frontdoor_firewall_policy_id}.
        '''
        value = CdnFrontdoorSecurityPolicySecurityPoliciesFirewall(
            association=association,
            cdn_frontdoor_firewall_policy_id=cdn_frontdoor_firewall_policy_id,
        )

        return typing.cast(None, jsii.invoke(self, "putFirewall", [value]))

    @builtins.property
    @jsii.member(jsii_name="firewall")
    def firewall(
        self,
    ) -> CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference:
        return typing.cast(CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference, jsii.get(self, "firewall"))

    @builtins.property
    @jsii.member(jsii_name="firewallInput")
    def firewall_input(
        self,
    ) -> typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewall]:
        return typing.cast(typing.Optional[CdnFrontdoorSecurityPolicySecurityPoliciesFirewall], jsii.get(self, "firewallInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnFrontdoorSecurityPolicySecurityPolicies]:
        return typing.cast(typing.Optional[CdnFrontdoorSecurityPolicySecurityPolicies], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorSecurityPolicySecurityPolicies],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class CdnFrontdoorSecurityPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#create CdnFrontdoorSecurityPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#delete CdnFrontdoorSecurityPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#read CdnFrontdoorSecurityPolicy#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicyTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#create CdnFrontdoorSecurityPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#delete CdnFrontdoorSecurityPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_security_policy#read CdnFrontdoorSecurityPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorSecurityPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorSecurityPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorSecurityPolicy.CdnFrontdoorSecurityPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorSecurityPolicyTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorSecurityPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorSecurityPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorSecurityPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorSecurityPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnFrontdoorSecurityPolicy",
    "CdnFrontdoorSecurityPolicyConfig",
    "CdnFrontdoorSecurityPolicySecurityPolicies",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewall",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociation",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomain",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainList",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationDomainOutputReference",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallAssociationOutputReference",
    "CdnFrontdoorSecurityPolicySecurityPoliciesFirewallOutputReference",
    "CdnFrontdoorSecurityPolicySecurityPoliciesOutputReference",
    "CdnFrontdoorSecurityPolicyTimeouts",
    "CdnFrontdoorSecurityPolicyTimeoutsOutputReference",
]

publication.publish()
