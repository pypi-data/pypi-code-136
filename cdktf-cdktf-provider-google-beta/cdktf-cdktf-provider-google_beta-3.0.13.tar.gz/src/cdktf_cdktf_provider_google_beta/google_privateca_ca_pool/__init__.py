'''
# `google_privateca_ca_pool`

Refer to the Terraform Registory for docs: [`google_privateca_ca_pool`](https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool).
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


class GooglePrivatecaCaPool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool google_privateca_ca_pool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        tier: builtins.str,
        id: typing.Optional[builtins.str] = None,
        issuance_policy: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicy", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        publishing_options: typing.Optional[typing.Union["GooglePrivatecaCaPoolPublishingOptions", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCaPoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool google_privateca_ca_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Location of the CaPool. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#location GooglePrivatecaCaPool#location}
        :param name: The name for this CaPool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#name GooglePrivatecaCaPool#name}
        :param tier: The Tier of this CaPool. Possible values: ["ENTERPRISE", "DEVOPS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#tier GooglePrivatecaCaPool#tier}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#id GooglePrivatecaCaPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuance_policy: issuance_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#issuance_policy GooglePrivatecaCaPool#issuance_policy}
        :param labels: Labels with user-defined metadata. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#labels GooglePrivatecaCaPool#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#project GooglePrivatecaCaPool#project}.
        :param publishing_options: publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publishing_options GooglePrivatecaCaPool#publishing_options}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#timeouts GooglePrivatecaCaPool#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GooglePrivatecaCaPoolConfig(
            location=location,
            name=name,
            tier=tier,
            id=id,
            issuance_policy=issuance_policy,
            labels=labels,
            project=project,
            publishing_options=publishing_options,
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

    @jsii.member(jsii_name="putIssuancePolicy")
    def put_issuance_policy(
        self,
        *,
        allowed_issuance_modes: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes", typing.Dict[str, typing.Any]]] = None,
        allowed_key_types: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes", typing.Dict[str, typing.Any]]]]] = None,
        baseline_values: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValues", typing.Dict[str, typing.Any]]] = None,
        identity_constraints: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints", typing.Dict[str, typing.Any]]] = None,
        maximum_lifetime: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_issuance_modes: allowed_issuance_modes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allowed_issuance_modes GooglePrivatecaCaPool#allowed_issuance_modes}
        :param allowed_key_types: allowed_key_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allowed_key_types GooglePrivatecaCaPool#allowed_key_types}
        :param baseline_values: baseline_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#baseline_values GooglePrivatecaCaPool#baseline_values}
        :param identity_constraints: identity_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#identity_constraints GooglePrivatecaCaPool#identity_constraints}
        :param maximum_lifetime: The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate's requested maximumLifetime, the effective lifetime will be explicitly truncated to match it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#maximum_lifetime GooglePrivatecaCaPool#maximum_lifetime}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicy(
            allowed_issuance_modes=allowed_issuance_modes,
            allowed_key_types=allowed_key_types,
            baseline_values=baseline_values,
            identity_constraints=identity_constraints,
            maximum_lifetime=maximum_lifetime,
        )

        return typing.cast(None, jsii.invoke(self, "putIssuancePolicy", [value]))

    @jsii.member(jsii_name="putPublishingOptions")
    def put_publishing_options(
        self,
        *,
        publish_ca_cert: typing.Union[builtins.bool, cdktf.IResolvable],
        publish_crl: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param publish_ca_cert: When true, publishes each CertificateAuthority's CA certificate and includes its URL in the "Authority Information Access" X.509 extension in all issued Certificates. If this is false, the CA certificate will not be published and the corresponding X.509 extension will not be written in issued certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publish_ca_cert GooglePrivatecaCaPool#publish_ca_cert}
        :param publish_crl: When true, publishes each CertificateAuthority's CRL and includes its URL in the "CRL Distribution Points" X.509 extension in all issued Certificates. If this is false, CRLs will not be published and the corresponding X.509 extension will not be written in issued certificates. CRLs will expire 7 days from their creation. However, we will rebuild daily. CRLs are also rebuilt shortly after a certificate is revoked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publish_crl GooglePrivatecaCaPool#publish_crl}
        '''
        value = GooglePrivatecaCaPoolPublishingOptions(
            publish_ca_cert=publish_ca_cert, publish_crl=publish_crl
        )

        return typing.cast(None, jsii.invoke(self, "putPublishingOptions", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#create GooglePrivatecaCaPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#delete GooglePrivatecaCaPool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#update GooglePrivatecaCaPool#update}.
        '''
        value = GooglePrivatecaCaPoolTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssuancePolicy")
    def reset_issuance_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuancePolicy", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPublishingOptions")
    def reset_publishing_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishingOptions", []))

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
    @jsii.member(jsii_name="issuancePolicy")
    def issuance_policy(self) -> "GooglePrivatecaCaPoolIssuancePolicyOutputReference":
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyOutputReference", jsii.get(self, "issuancePolicy"))

    @builtins.property
    @jsii.member(jsii_name="publishingOptions")
    def publishing_options(
        self,
    ) -> "GooglePrivatecaCaPoolPublishingOptionsOutputReference":
        return typing.cast("GooglePrivatecaCaPoolPublishingOptionsOutputReference", jsii.get(self, "publishingOptions"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePrivatecaCaPoolTimeoutsOutputReference":
        return typing.cast("GooglePrivatecaCaPoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuancePolicyInput")
    def issuance_policy_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicy"]:
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicy"], jsii.get(self, "issuancePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="publishingOptionsInput")
    def publishing_options_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolPublishingOptions"]:
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolPublishingOptions"], jsii.get(self, "publishingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePrivatecaCaPoolTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePrivatecaCaPoolTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPool, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPool, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPool, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPool, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPool, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPool, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "tier": "tier",
        "id": "id",
        "issuance_policy": "issuancePolicy",
        "labels": "labels",
        "project": "project",
        "publishing_options": "publishingOptions",
        "timeouts": "timeouts",
    },
)
class GooglePrivatecaCaPoolConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        tier: builtins.str,
        id: typing.Optional[builtins.str] = None,
        issuance_policy: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicy", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        publishing_options: typing.Optional[typing.Union["GooglePrivatecaCaPoolPublishingOptions", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCaPoolTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Location of the CaPool. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#location GooglePrivatecaCaPool#location}
        :param name: The name for this CaPool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#name GooglePrivatecaCaPool#name}
        :param tier: The Tier of this CaPool. Possible values: ["ENTERPRISE", "DEVOPS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#tier GooglePrivatecaCaPool#tier}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#id GooglePrivatecaCaPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuance_policy: issuance_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#issuance_policy GooglePrivatecaCaPool#issuance_policy}
        :param labels: Labels with user-defined metadata. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#labels GooglePrivatecaCaPool#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#project GooglePrivatecaCaPool#project}.
        :param publishing_options: publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publishing_options GooglePrivatecaCaPool#publishing_options}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#timeouts GooglePrivatecaCaPool#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(issuance_policy, dict):
            issuance_policy = GooglePrivatecaCaPoolIssuancePolicy(**issuance_policy)
        if isinstance(publishing_options, dict):
            publishing_options = GooglePrivatecaCaPoolPublishingOptions(**publishing_options)
        if isinstance(timeouts, dict):
            timeouts = GooglePrivatecaCaPoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issuance_policy", value=issuance_policy, expected_type=type_hints["issuance_policy"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument publishing_options", value=publishing_options, expected_type=type_hints["publishing_options"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "tier": tier,
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
        if issuance_policy is not None:
            self._values["issuance_policy"] = issuance_policy
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
        if publishing_options is not None:
            self._values["publishing_options"] = publishing_options
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
    def location(self) -> builtins.str:
        '''Location of the CaPool. A full list of valid locations can be found by running 'gcloud privateca locations list'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#location GooglePrivatecaCaPool#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for this CaPool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#name GooglePrivatecaCaPool#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''The Tier of this CaPool. Possible values: ["ENTERPRISE", "DEVOPS"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#tier GooglePrivatecaCaPool#tier}
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#id GooglePrivatecaCaPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuance_policy(self) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicy"]:
        '''issuance_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#issuance_policy GooglePrivatecaCaPool#issuance_policy}
        '''
        result = self._values.get("issuance_policy")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicy"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels with user-defined metadata.

        An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass":
        "1.3kg", "count": "3" }.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#labels GooglePrivatecaCaPool#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#project GooglePrivatecaCaPool#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publishing_options(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolPublishingOptions"]:
        '''publishing_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publishing_options GooglePrivatecaCaPool#publishing_options}
        '''
        result = self._values.get("publishing_options")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolPublishingOptions"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GooglePrivatecaCaPoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#timeouts GooglePrivatecaCaPool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_issuance_modes": "allowedIssuanceModes",
        "allowed_key_types": "allowedKeyTypes",
        "baseline_values": "baselineValues",
        "identity_constraints": "identityConstraints",
        "maximum_lifetime": "maximumLifetime",
    },
)
class GooglePrivatecaCaPoolIssuancePolicy:
    def __init__(
        self,
        *,
        allowed_issuance_modes: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes", typing.Dict[str, typing.Any]]] = None,
        allowed_key_types: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes", typing.Dict[str, typing.Any]]]]] = None,
        baseline_values: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValues", typing.Dict[str, typing.Any]]] = None,
        identity_constraints: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints", typing.Dict[str, typing.Any]]] = None,
        maximum_lifetime: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_issuance_modes: allowed_issuance_modes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allowed_issuance_modes GooglePrivatecaCaPool#allowed_issuance_modes}
        :param allowed_key_types: allowed_key_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allowed_key_types GooglePrivatecaCaPool#allowed_key_types}
        :param baseline_values: baseline_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#baseline_values GooglePrivatecaCaPool#baseline_values}
        :param identity_constraints: identity_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#identity_constraints GooglePrivatecaCaPool#identity_constraints}
        :param maximum_lifetime: The maximum lifetime allowed for issued Certificates. Note that if the issuing CertificateAuthority expires before a Certificate's requested maximumLifetime, the effective lifetime will be explicitly truncated to match it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#maximum_lifetime GooglePrivatecaCaPool#maximum_lifetime}
        '''
        if isinstance(allowed_issuance_modes, dict):
            allowed_issuance_modes = GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes(**allowed_issuance_modes)
        if isinstance(baseline_values, dict):
            baseline_values = GooglePrivatecaCaPoolIssuancePolicyBaselineValues(**baseline_values)
        if isinstance(identity_constraints, dict):
            identity_constraints = GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints(**identity_constraints)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicy.__init__)
            check_type(argname="argument allowed_issuance_modes", value=allowed_issuance_modes, expected_type=type_hints["allowed_issuance_modes"])
            check_type(argname="argument allowed_key_types", value=allowed_key_types, expected_type=type_hints["allowed_key_types"])
            check_type(argname="argument baseline_values", value=baseline_values, expected_type=type_hints["baseline_values"])
            check_type(argname="argument identity_constraints", value=identity_constraints, expected_type=type_hints["identity_constraints"])
            check_type(argname="argument maximum_lifetime", value=maximum_lifetime, expected_type=type_hints["maximum_lifetime"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_issuance_modes is not None:
            self._values["allowed_issuance_modes"] = allowed_issuance_modes
        if allowed_key_types is not None:
            self._values["allowed_key_types"] = allowed_key_types
        if baseline_values is not None:
            self._values["baseline_values"] = baseline_values
        if identity_constraints is not None:
            self._values["identity_constraints"] = identity_constraints
        if maximum_lifetime is not None:
            self._values["maximum_lifetime"] = maximum_lifetime

    @builtins.property
    def allowed_issuance_modes(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes"]:
        '''allowed_issuance_modes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allowed_issuance_modes GooglePrivatecaCaPool#allowed_issuance_modes}
        '''
        result = self._values.get("allowed_issuance_modes")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes"], result)

    @builtins.property
    def allowed_key_types(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes"]]]:
        '''allowed_key_types block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allowed_key_types GooglePrivatecaCaPool#allowed_key_types}
        '''
        result = self._values.get("allowed_key_types")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes"]]], result)

    @builtins.property
    def baseline_values(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyBaselineValues"]:
        '''baseline_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#baseline_values GooglePrivatecaCaPool#baseline_values}
        '''
        result = self._values.get("baseline_values")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyBaselineValues"], result)

    @builtins.property
    def identity_constraints(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints"]:
        '''identity_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#identity_constraints GooglePrivatecaCaPool#identity_constraints}
        '''
        result = self._values.get("identity_constraints")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints"], result)

    @builtins.property
    def maximum_lifetime(self) -> typing.Optional[builtins.str]:
        '''The maximum lifetime allowed for issued Certificates.

        Note that if the issuing CertificateAuthority
        expires before a Certificate's requested maximumLifetime, the effective lifetime will be explicitly truncated to match it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#maximum_lifetime GooglePrivatecaCaPool#maximum_lifetime}
        '''
        result = self._values.get("maximum_lifetime")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes",
    jsii_struct_bases=[],
    name_mapping={
        "allow_config_based_issuance": "allowConfigBasedIssuance",
        "allow_csr_based_issuance": "allowCsrBasedIssuance",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes:
    def __init__(
        self,
        *,
        allow_config_based_issuance: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_csr_based_issuance: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param allow_config_based_issuance: When true, allows callers to create Certificates by specifying a CertificateConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_config_based_issuance GooglePrivatecaCaPool#allow_config_based_issuance}
        :param allow_csr_based_issuance: When true, allows callers to create Certificates by specifying a CSR. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_csr_based_issuance GooglePrivatecaCaPool#allow_csr_based_issuance}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes.__init__)
            check_type(argname="argument allow_config_based_issuance", value=allow_config_based_issuance, expected_type=type_hints["allow_config_based_issuance"])
            check_type(argname="argument allow_csr_based_issuance", value=allow_csr_based_issuance, expected_type=type_hints["allow_csr_based_issuance"])
        self._values: typing.Dict[str, typing.Any] = {
            "allow_config_based_issuance": allow_config_based_issuance,
            "allow_csr_based_issuance": allow_csr_based_issuance,
        }

    @builtins.property
    def allow_config_based_issuance(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When true, allows callers to create Certificates by specifying a CertificateConfig.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_config_based_issuance GooglePrivatecaCaPool#allow_config_based_issuance}
        '''
        result = self._values.get("allow_config_based_issuance")
        assert result is not None, "Required property 'allow_config_based_issuance' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def allow_csr_based_issuance(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When true, allows callers to create Certificates by specifying a CSR.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_csr_based_issuance GooglePrivatecaCaPool#allow_csr_based_issuance}
        '''
        result = self._values.get("allow_csr_based_issuance")
        assert result is not None, "Required property 'allow_csr_based_issuance' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowConfigBasedIssuanceInput")
    def allow_config_based_issuance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowConfigBasedIssuanceInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCsrBasedIssuanceInput")
    def allow_csr_based_issuance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCsrBasedIssuanceInput"))

    @builtins.property
    @jsii.member(jsii_name="allowConfigBasedIssuance")
    def allow_config_based_issuance(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowConfigBasedIssuance"))

    @allow_config_based_issuance.setter
    def allow_config_based_issuance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference, "allow_config_based_issuance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowConfigBasedIssuance", value)

    @builtins.property
    @jsii.member(jsii_name="allowCsrBasedIssuance")
    def allow_csr_based_issuance(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCsrBasedIssuance"))

    @allow_csr_based_issuance.setter
    def allow_csr_based_issuance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference, "allow_csr_based_issuance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCsrBasedIssuance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes",
    jsii_struct_bases=[],
    name_mapping={"elliptic_curve": "ellipticCurve", "rsa": "rsa"},
)
class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes:
    def __init__(
        self,
        *,
        elliptic_curve: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve", typing.Dict[str, typing.Any]]] = None,
        rsa: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elliptic_curve: elliptic_curve block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#elliptic_curve GooglePrivatecaCaPool#elliptic_curve}
        :param rsa: rsa block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#rsa GooglePrivatecaCaPool#rsa}
        '''
        if isinstance(elliptic_curve, dict):
            elliptic_curve = GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve(**elliptic_curve)
        if isinstance(rsa, dict):
            rsa = GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa(**rsa)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes.__init__)
            check_type(argname="argument elliptic_curve", value=elliptic_curve, expected_type=type_hints["elliptic_curve"])
            check_type(argname="argument rsa", value=rsa, expected_type=type_hints["rsa"])
        self._values: typing.Dict[str, typing.Any] = {}
        if elliptic_curve is not None:
            self._values["elliptic_curve"] = elliptic_curve
        if rsa is not None:
            self._values["rsa"] = rsa

    @builtins.property
    def elliptic_curve(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve"]:
        '''elliptic_curve block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#elliptic_curve GooglePrivatecaCaPool#elliptic_curve}
        '''
        result = self._values.get("elliptic_curve")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve"], result)

    @builtins.property
    def rsa(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa"]:
        '''rsa block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#rsa GooglePrivatecaCaPool#rsa}
        '''
        result = self._values.get("rsa")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve",
    jsii_struct_bases=[],
    name_mapping={"signature_algorithm": "signatureAlgorithm"},
)
class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve:
    def __init__(self, *, signature_algorithm: builtins.str) -> None:
        '''
        :param signature_algorithm: The algorithm used. Possible values: ["ECDSA_P256", "ECDSA_P384", "EDDSA_25519"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#signature_algorithm GooglePrivatecaCaPool#signature_algorithm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve.__init__)
            check_type(argname="argument signature_algorithm", value=signature_algorithm, expected_type=type_hints["signature_algorithm"])
        self._values: typing.Dict[str, typing.Any] = {
            "signature_algorithm": signature_algorithm,
        }

    @builtins.property
    def signature_algorithm(self) -> builtins.str:
        '''The algorithm used. Possible values: ["ECDSA_P256", "ECDSA_P384", "EDDSA_25519"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#signature_algorithm GooglePrivatecaCaPool#signature_algorithm}
        '''
        result = self._values.get("signature_algorithm")
        assert result is not None, "Required property 'signature_algorithm' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithmInput")
    def signature_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @signature_algorithm.setter
    def signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference, "signature_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signatureAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEllipticCurve")
    def put_elliptic_curve(self, *, signature_algorithm: builtins.str) -> None:
        '''
        :param signature_algorithm: The algorithm used. Possible values: ["ECDSA_P256", "ECDSA_P384", "EDDSA_25519"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#signature_algorithm GooglePrivatecaCaPool#signature_algorithm}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve(
            signature_algorithm=signature_algorithm
        )

        return typing.cast(None, jsii.invoke(self, "putEllipticCurve", [value]))

    @jsii.member(jsii_name="putRsa")
    def put_rsa(
        self,
        *,
        max_modulus_size: typing.Optional[builtins.str] = None,
        min_modulus_size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_modulus_size: The maximum allowed RSA modulus size, in bits. If this is not set, or if set to zero, the service will not enforce an explicit upper bound on RSA modulus sizes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#max_modulus_size GooglePrivatecaCaPool#max_modulus_size}
        :param min_modulus_size: The minimum allowed RSA modulus size, in bits. If this is not set, or if set to zero, the service-level min RSA modulus size will continue to apply. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#min_modulus_size GooglePrivatecaCaPool#min_modulus_size}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa(
            max_modulus_size=max_modulus_size, min_modulus_size=min_modulus_size
        )

        return typing.cast(None, jsii.invoke(self, "putRsa", [value]))

    @jsii.member(jsii_name="resetEllipticCurve")
    def reset_elliptic_curve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEllipticCurve", []))

    @jsii.member(jsii_name="resetRsa")
    def reset_rsa(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRsa", []))

    @builtins.property
    @jsii.member(jsii_name="ellipticCurve")
    def elliptic_curve(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference, jsii.get(self, "ellipticCurve"))

    @builtins.property
    @jsii.member(jsii_name="rsa")
    def rsa(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference":
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference", jsii.get(self, "rsa"))

    @builtins.property
    @jsii.member(jsii_name="ellipticCurveInput")
    def elliptic_curve_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve], jsii.get(self, "ellipticCurveInput"))

    @builtins.property
    @jsii.member(jsii_name="rsaInput")
    def rsa_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa"]:
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa"], jsii.get(self, "rsaInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa",
    jsii_struct_bases=[],
    name_mapping={
        "max_modulus_size": "maxModulusSize",
        "min_modulus_size": "minModulusSize",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa:
    def __init__(
        self,
        *,
        max_modulus_size: typing.Optional[builtins.str] = None,
        min_modulus_size: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_modulus_size: The maximum allowed RSA modulus size, in bits. If this is not set, or if set to zero, the service will not enforce an explicit upper bound on RSA modulus sizes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#max_modulus_size GooglePrivatecaCaPool#max_modulus_size}
        :param min_modulus_size: The minimum allowed RSA modulus size, in bits. If this is not set, or if set to zero, the service-level min RSA modulus size will continue to apply. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#min_modulus_size GooglePrivatecaCaPool#min_modulus_size}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa.__init__)
            check_type(argname="argument max_modulus_size", value=max_modulus_size, expected_type=type_hints["max_modulus_size"])
            check_type(argname="argument min_modulus_size", value=min_modulus_size, expected_type=type_hints["min_modulus_size"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_modulus_size is not None:
            self._values["max_modulus_size"] = max_modulus_size
        if min_modulus_size is not None:
            self._values["min_modulus_size"] = min_modulus_size

    @builtins.property
    def max_modulus_size(self) -> typing.Optional[builtins.str]:
        '''The maximum allowed RSA modulus size, in bits.

        If this is not set, or if set to zero, the
        service will not enforce an explicit upper bound on RSA modulus sizes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#max_modulus_size GooglePrivatecaCaPool#max_modulus_size}
        '''
        result = self._values.get("max_modulus_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_modulus_size(self) -> typing.Optional[builtins.str]:
        '''The minimum allowed RSA modulus size, in bits.

        If this is not set, or if set to zero, the
        service-level min RSA modulus size will continue to apply.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#min_modulus_size GooglePrivatecaCaPool#min_modulus_size}
        '''
        result = self._values.get("min_modulus_size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxModulusSize")
    def reset_max_modulus_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxModulusSize", []))

    @jsii.member(jsii_name="resetMinModulusSize")
    def reset_min_modulus_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinModulusSize", []))

    @builtins.property
    @jsii.member(jsii_name="maxModulusSizeInput")
    def max_modulus_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxModulusSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="minModulusSizeInput")
    def min_modulus_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minModulusSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxModulusSize")
    def max_modulus_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxModulusSize"))

    @max_modulus_size.setter
    def max_modulus_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference, "max_modulus_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxModulusSize", value)

    @builtins.property
    @jsii.member(jsii_name="minModulusSize")
    def min_modulus_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minModulusSize"))

    @min_modulus_size.setter
    def min_modulus_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference, "min_modulus_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minModulusSize", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValues",
    jsii_struct_bases=[],
    name_mapping={
        "ca_options": "caOptions",
        "key_usage": "keyUsage",
        "additional_extensions": "additionalExtensions",
        "aia_ocsp_servers": "aiaOcspServers",
        "policy_ids": "policyIds",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValues:
    def __init__(
        self,
        *,
        ca_options: typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions", typing.Dict[str, typing.Any]],
        key_usage: typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage", typing.Dict[str, typing.Any]],
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#ca_options GooglePrivatecaCaPool#ca_options}
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_usage GooglePrivatecaCaPool#key_usage}
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#additional_extensions GooglePrivatecaCaPool#additional_extensions}
        :param aia_ocsp_servers: Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#aia_ocsp_servers GooglePrivatecaCaPool#aia_ocsp_servers}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#policy_ids GooglePrivatecaCaPool#policy_ids}
        '''
        if isinstance(ca_options, dict):
            ca_options = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions(**ca_options)
        if isinstance(key_usage, dict):
            key_usage = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage(**key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValues.__init__)
            check_type(argname="argument ca_options", value=ca_options, expected_type=type_hints["ca_options"])
            check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            check_type(argname="argument additional_extensions", value=additional_extensions, expected_type=type_hints["additional_extensions"])
            check_type(argname="argument aia_ocsp_servers", value=aia_ocsp_servers, expected_type=type_hints["aia_ocsp_servers"])
            check_type(argname="argument policy_ids", value=policy_ids, expected_type=type_hints["policy_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "ca_options": ca_options,
            "key_usage": key_usage,
        }
        if additional_extensions is not None:
            self._values["additional_extensions"] = additional_extensions
        if aia_ocsp_servers is not None:
            self._values["aia_ocsp_servers"] = aia_ocsp_servers
        if policy_ids is not None:
            self._values["policy_ids"] = policy_ids

    @builtins.property
    def ca_options(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions":
        '''ca_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#ca_options GooglePrivatecaCaPool#ca_options}
        '''
        result = self._values.get("ca_options")
        assert result is not None, "Required property 'ca_options' is missing"
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions", result)

    @builtins.property
    def key_usage(self) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage":
        '''key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_usage GooglePrivatecaCaPool#key_usage}
        '''
        result = self._values.get("key_usage")
        assert result is not None, "Required property 'key_usage' is missing"
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage", result)

    @builtins.property
    def additional_extensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions"]]]:
        '''additional_extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#additional_extensions GooglePrivatecaCaPool#additional_extensions}
        '''
        result = self._values.get("additional_extensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions"]]], result)

    @builtins.property
    def aia_ocsp_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#aia_ocsp_servers GooglePrivatecaCaPool#aia_ocsp_servers}
        '''
        result = self._values.get("aia_ocsp_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def policy_ids(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds"]]]:
        '''policy_ids block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#policy_ids GooglePrivatecaCaPool#policy_ids}
        '''
        result = self._values.get("policy_ids")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={"critical": "critical", "object_id": "objectId", "value": "value"},
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions:
    def __init__(
        self,
        *,
        critical: typing.Union[builtins.bool, cdktf.IResolvable],
        object_id: typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId", typing.Dict[str, typing.Any]],
        value: builtins.str,
    ) -> None:
        '''
        :param critical: Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#critical GooglePrivatecaCaPool#critical}
        :param object_id: object_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id GooglePrivatecaCaPool#object_id}
        :param value: The value of this X.509 extension. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#value GooglePrivatecaCaPool#value}
        '''
        if isinstance(object_id, dict):
            object_id = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId(**object_id)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions.__init__)
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "critical": critical,
            "object_id": object_id,
            "value": value,
        }

    @builtins.property
    def critical(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#critical GooglePrivatecaCaPool#critical}
        '''
        result = self._values.get("critical")
        assert result is not None, "Required property 'critical' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def object_id(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId":
        '''object_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id GooglePrivatecaCaPool#object_id}
        '''
        result = self._values.get("object_id")
        assert result is not None, "Required property 'object_id' is missing"
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId", result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of this X.509 extension. A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#value GooglePrivatecaCaPool#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="objectIdPathInput")
    def object_id_path_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "objectIdPathInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdPath")
    def object_id_path(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "objectIdPath"))

    @object_id_path.setter
    def object_id_path(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectId")
    def put_object_id(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId(
            object_id_path=object_id_path
        )

        return typing.cast(None, jsii.invoke(self, "putObjectId", [value]))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="criticalInput")
    def critical_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "criticalInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdInput")
    def object_id_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId], jsii.get(self, "objectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "critical"))

    @critical.setter
    def critical(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference, "critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "critical", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions",
    jsii_struct_bases=[],
    name_mapping={
        "is_ca": "isCa",
        "max_issuer_path_length": "maxIssuerPathLength",
        "non_ca": "nonCa",
        "zero_max_issuer_path_length": "zeroMaxIssuerPathLength",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions:
    def __init__(
        self,
        *,
        is_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
        non_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zero_max_issuer_path_length: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_ca: When true, the "CA" in Basic Constraints extension will be set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#is_ca GooglePrivatecaCaPool#is_ca}
        :param max_issuer_path_length: Refers to the "path length constraint" in Basic Constraints extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#max_issuer_path_length GooglePrivatecaCaPool#max_issuer_path_length}
        :param non_ca: When true, the "CA" in Basic Constraints extension will be set to false. If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#non_ca GooglePrivatecaCaPool#non_ca}
        :param zero_max_issuer_path_length: When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#zero_max_issuer_path_length GooglePrivatecaCaPool#zero_max_issuer_path_length}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions.__init__)
            check_type(argname="argument is_ca", value=is_ca, expected_type=type_hints["is_ca"])
            check_type(argname="argument max_issuer_path_length", value=max_issuer_path_length, expected_type=type_hints["max_issuer_path_length"])
            check_type(argname="argument non_ca", value=non_ca, expected_type=type_hints["non_ca"])
            check_type(argname="argument zero_max_issuer_path_length", value=zero_max_issuer_path_length, expected_type=type_hints["zero_max_issuer_path_length"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_ca is not None:
            self._values["is_ca"] = is_ca
        if max_issuer_path_length is not None:
            self._values["max_issuer_path_length"] = max_issuer_path_length
        if non_ca is not None:
            self._values["non_ca"] = non_ca
        if zero_max_issuer_path_length is not None:
            self._values["zero_max_issuer_path_length"] = zero_max_issuer_path_length

    @builtins.property
    def is_ca(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, the "CA" in Basic Constraints extension will be set to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#is_ca GooglePrivatecaCaPool#is_ca}
        '''
        result = self._values.get("is_ca")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_issuer_path_length(self) -> typing.Optional[jsii.Number]:
        '''Refers to the "path length constraint" in Basic Constraints extension.

        For a CA certificate, this value describes the depth of
        subordinate CA certificates that are allowed. If this value is less than 0, the request will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#max_issuer_path_length GooglePrivatecaCaPool#max_issuer_path_length}
        '''
        result = self._values.get("max_issuer_path_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def non_ca(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, the "CA" in Basic Constraints extension will be set to false.

        If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#non_ca GooglePrivatecaCaPool#non_ca}
        '''
        result = self._values.get("non_ca")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def zero_max_issuer_path_length(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, the "path length constraint" in Basic Constraints extension will be set to 0.

        if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset,
        the max path length will be omitted from the CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#zero_max_issuer_path_length GooglePrivatecaCaPool#zero_max_issuer_path_length}
        '''
        result = self._values.get("zero_max_issuer_path_length")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsCa")
    def reset_is_ca(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCa", []))

    @jsii.member(jsii_name="resetMaxIssuerPathLength")
    def reset_max_issuer_path_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIssuerPathLength", []))

    @jsii.member(jsii_name="resetNonCa")
    def reset_non_ca(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonCa", []))

    @jsii.member(jsii_name="resetZeroMaxIssuerPathLength")
    def reset_zero_max_issuer_path_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZeroMaxIssuerPathLength", []))

    @builtins.property
    @jsii.member(jsii_name="isCaInput")
    def is_ca_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isCaInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIssuerPathLengthInput")
    def max_issuer_path_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIssuerPathLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="nonCaInput")
    def non_ca_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "nonCaInput"))

    @builtins.property
    @jsii.member(jsii_name="zeroMaxIssuerPathLengthInput")
    def zero_max_issuer_path_length_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "zeroMaxIssuerPathLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="isCa")
    def is_ca(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCa"))

    @is_ca.setter
    def is_ca(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference, "is_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCa", value)

    @builtins.property
    @jsii.member(jsii_name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIssuerPathLength"))

    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference, "max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="nonCa")
    def non_ca(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nonCa"))

    @non_ca.setter
    def non_ca(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference, "non_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonCa", value)

    @builtins.property
    @jsii.member(jsii_name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "zeroMaxIssuerPathLength"))

    @zero_max_issuer_path_length.setter
    def zero_max_issuer_path_length(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference, "zero_max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zeroMaxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage",
    jsii_struct_bases=[],
    name_mapping={
        "base_key_usage": "baseKeyUsage",
        "extended_key_usage": "extendedKeyUsage",
        "unknown_extended_key_usages": "unknownExtendedKeyUsages",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage:
    def __init__(
        self,
        *,
        base_key_usage: typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage", typing.Dict[str, typing.Any]],
        extended_key_usage: typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage", typing.Dict[str, typing.Any]],
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#base_key_usage GooglePrivatecaCaPool#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#extended_key_usage GooglePrivatecaCaPool#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#unknown_extended_key_usages GooglePrivatecaCaPool#unknown_extended_key_usages}
        '''
        if isinstance(base_key_usage, dict):
            base_key_usage = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage(**base_key_usage)
        if isinstance(extended_key_usage, dict):
            extended_key_usage = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage(**extended_key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage.__init__)
            check_type(argname="argument base_key_usage", value=base_key_usage, expected_type=type_hints["base_key_usage"])
            check_type(argname="argument extended_key_usage", value=extended_key_usage, expected_type=type_hints["extended_key_usage"])
            check_type(argname="argument unknown_extended_key_usages", value=unknown_extended_key_usages, expected_type=type_hints["unknown_extended_key_usages"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_key_usage": base_key_usage,
            "extended_key_usage": extended_key_usage,
        }
        if unknown_extended_key_usages is not None:
            self._values["unknown_extended_key_usages"] = unknown_extended_key_usages

    @builtins.property
    def base_key_usage(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage":
        '''base_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#base_key_usage GooglePrivatecaCaPool#base_key_usage}
        '''
        result = self._values.get("base_key_usage")
        assert result is not None, "Required property 'base_key_usage' is missing"
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage", result)

    @builtins.property
    def extended_key_usage(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage":
        '''extended_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#extended_key_usage GooglePrivatecaCaPool#extended_key_usage}
        '''
        result = self._values.get("extended_key_usage")
        assert result is not None, "Required property 'extended_key_usage' is missing"
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage", result)

    @builtins.property
    def unknown_extended_key_usages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages"]]]:
        '''unknown_extended_key_usages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#unknown_extended_key_usages GooglePrivatecaCaPool#unknown_extended_key_usages}
        '''
        result = self._values.get("unknown_extended_key_usages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage",
    jsii_struct_bases=[],
    name_mapping={
        "cert_sign": "certSign",
        "content_commitment": "contentCommitment",
        "crl_sign": "crlSign",
        "data_encipherment": "dataEncipherment",
        "decipher_only": "decipherOnly",
        "digital_signature": "digitalSignature",
        "encipher_only": "encipherOnly",
        "key_agreement": "keyAgreement",
        "key_encipherment": "keyEncipherment",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage:
    def __init__(
        self,
        *,
        cert_sign: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        content_commitment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        crl_sign: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_encipherment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        decipher_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        digital_signature: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encipher_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_agreement: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_encipherment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#cert_sign GooglePrivatecaCaPool#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#content_commitment GooglePrivatecaCaPool#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#crl_sign GooglePrivatecaCaPool#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#data_encipherment GooglePrivatecaCaPool#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#decipher_only GooglePrivatecaCaPool#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#digital_signature GooglePrivatecaCaPool#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#encipher_only GooglePrivatecaCaPool#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_agreement GooglePrivatecaCaPool#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_encipherment GooglePrivatecaCaPool#key_encipherment}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage.__init__)
            check_type(argname="argument cert_sign", value=cert_sign, expected_type=type_hints["cert_sign"])
            check_type(argname="argument content_commitment", value=content_commitment, expected_type=type_hints["content_commitment"])
            check_type(argname="argument crl_sign", value=crl_sign, expected_type=type_hints["crl_sign"])
            check_type(argname="argument data_encipherment", value=data_encipherment, expected_type=type_hints["data_encipherment"])
            check_type(argname="argument decipher_only", value=decipher_only, expected_type=type_hints["decipher_only"])
            check_type(argname="argument digital_signature", value=digital_signature, expected_type=type_hints["digital_signature"])
            check_type(argname="argument encipher_only", value=encipher_only, expected_type=type_hints["encipher_only"])
            check_type(argname="argument key_agreement", value=key_agreement, expected_type=type_hints["key_agreement"])
            check_type(argname="argument key_encipherment", value=key_encipherment, expected_type=type_hints["key_encipherment"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cert_sign is not None:
            self._values["cert_sign"] = cert_sign
        if content_commitment is not None:
            self._values["content_commitment"] = content_commitment
        if crl_sign is not None:
            self._values["crl_sign"] = crl_sign
        if data_encipherment is not None:
            self._values["data_encipherment"] = data_encipherment
        if decipher_only is not None:
            self._values["decipher_only"] = decipher_only
        if digital_signature is not None:
            self._values["digital_signature"] = digital_signature
        if encipher_only is not None:
            self._values["encipher_only"] = encipher_only
        if key_agreement is not None:
            self._values["key_agreement"] = key_agreement
        if key_encipherment is not None:
            self._values["key_encipherment"] = key_encipherment

    @builtins.property
    def cert_sign(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to sign certificates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#cert_sign GooglePrivatecaCaPool#cert_sign}
        '''
        result = self._values.get("cert_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def content_commitment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#content_commitment GooglePrivatecaCaPool#content_commitment}
        '''
        result = self._values.get("content_commitment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def crl_sign(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used sign certificate revocation lists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#crl_sign GooglePrivatecaCaPool#crl_sign}
        '''
        result = self._values.get("crl_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#data_encipherment GooglePrivatecaCaPool#data_encipherment}
        '''
        result = self._values.get("data_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def decipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to decipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#decipher_only GooglePrivatecaCaPool#decipher_only}
        '''
        result = self._values.get("decipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def digital_signature(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for digital signatures.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#digital_signature GooglePrivatecaCaPool#digital_signature}
        '''
        result = self._values.get("digital_signature")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#encipher_only GooglePrivatecaCaPool#encipher_only}
        '''
        result = self._values.get("encipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_agreement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used in a key agreement protocol.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_agreement GooglePrivatecaCaPool#key_agreement}
        '''
        result = self._values.get("key_agreement")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher other keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_encipherment GooglePrivatecaCaPool#key_encipherment}
        '''
        result = self._values.get("key_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCertSign")
    def reset_cert_sign(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertSign", []))

    @jsii.member(jsii_name="resetContentCommitment")
    def reset_content_commitment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentCommitment", []))

    @jsii.member(jsii_name="resetCrlSign")
    def reset_crl_sign(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrlSign", []))

    @jsii.member(jsii_name="resetDataEncipherment")
    def reset_data_encipherment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataEncipherment", []))

    @jsii.member(jsii_name="resetDecipherOnly")
    def reset_decipher_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecipherOnly", []))

    @jsii.member(jsii_name="resetDigitalSignature")
    def reset_digital_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigitalSignature", []))

    @jsii.member(jsii_name="resetEncipherOnly")
    def reset_encipher_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncipherOnly", []))

    @jsii.member(jsii_name="resetKeyAgreement")
    def reset_key_agreement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyAgreement", []))

    @jsii.member(jsii_name="resetKeyEncipherment")
    def reset_key_encipherment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyEncipherment", []))

    @builtins.property
    @jsii.member(jsii_name="certSignInput")
    def cert_sign_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "certSignInput"))

    @builtins.property
    @jsii.member(jsii_name="contentCommitmentInput")
    def content_commitment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "contentCommitmentInput"))

    @builtins.property
    @jsii.member(jsii_name="crlSignInput")
    def crl_sign_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "crlSignInput"))

    @builtins.property
    @jsii.member(jsii_name="dataEnciphermentInput")
    def data_encipherment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dataEnciphermentInput"))

    @builtins.property
    @jsii.member(jsii_name="decipherOnlyInput")
    def decipher_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "decipherOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="digitalSignatureInput")
    def digital_signature_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "digitalSignatureInput"))

    @builtins.property
    @jsii.member(jsii_name="encipherOnlyInput")
    def encipher_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encipherOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="keyAgreementInput")
    def key_agreement_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "keyAgreementInput"))

    @builtins.property
    @jsii.member(jsii_name="keyEnciphermentInput")
    def key_encipherment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "keyEnciphermentInput"))

    @builtins.property
    @jsii.member(jsii_name="certSign")
    def cert_sign(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "certSign"))

    @cert_sign.setter
    def cert_sign(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "cert_sign").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certSign", value)

    @builtins.property
    @jsii.member(jsii_name="contentCommitment")
    def content_commitment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "contentCommitment"))

    @content_commitment.setter
    def content_commitment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "content_commitment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentCommitment", value)

    @builtins.property
    @jsii.member(jsii_name="crlSign")
    def crl_sign(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "crlSign"))

    @crl_sign.setter
    def crl_sign(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "crl_sign").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crlSign", value)

    @builtins.property
    @jsii.member(jsii_name="dataEncipherment")
    def data_encipherment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dataEncipherment"))

    @data_encipherment.setter
    def data_encipherment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "data_encipherment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataEncipherment", value)

    @builtins.property
    @jsii.member(jsii_name="decipherOnly")
    def decipher_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "decipherOnly"))

    @decipher_only.setter
    def decipher_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "decipher_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decipherOnly", value)

    @builtins.property
    @jsii.member(jsii_name="digitalSignature")
    def digital_signature(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "digitalSignature"))

    @digital_signature.setter
    def digital_signature(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "digital_signature").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digitalSignature", value)

    @builtins.property
    @jsii.member(jsii_name="encipherOnly")
    def encipher_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encipherOnly"))

    @encipher_only.setter
    def encipher_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "encipher_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encipherOnly", value)

    @builtins.property
    @jsii.member(jsii_name="keyAgreement")
    def key_agreement(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "keyAgreement"))

    @key_agreement.setter
    def key_agreement(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "key_agreement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAgreement", value)

    @builtins.property
    @jsii.member(jsii_name="keyEncipherment")
    def key_encipherment(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "keyEncipherment"))

    @key_encipherment.setter
    def key_encipherment(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "key_encipherment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyEncipherment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage",
    jsii_struct_bases=[],
    name_mapping={
        "client_auth": "clientAuth",
        "code_signing": "codeSigning",
        "email_protection": "emailProtection",
        "ocsp_signing": "ocspSigning",
        "server_auth": "serverAuth",
        "time_stamping": "timeStamping",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage:
    def __init__(
        self,
        *,
        client_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        code_signing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        email_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ocsp_signing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        server_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        time_stamping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#client_auth GooglePrivatecaCaPool#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#code_signing GooglePrivatecaCaPool#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#email_protection GooglePrivatecaCaPool#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#ocsp_signing GooglePrivatecaCaPool#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#server_auth GooglePrivatecaCaPool#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#time_stamping GooglePrivatecaCaPool#time_stamping}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage.__init__)
            check_type(argname="argument client_auth", value=client_auth, expected_type=type_hints["client_auth"])
            check_type(argname="argument code_signing", value=code_signing, expected_type=type_hints["code_signing"])
            check_type(argname="argument email_protection", value=email_protection, expected_type=type_hints["email_protection"])
            check_type(argname="argument ocsp_signing", value=ocsp_signing, expected_type=type_hints["ocsp_signing"])
            check_type(argname="argument server_auth", value=server_auth, expected_type=type_hints["server_auth"])
            check_type(argname="argument time_stamping", value=time_stamping, expected_type=type_hints["time_stamping"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_auth is not None:
            self._values["client_auth"] = client_auth
        if code_signing is not None:
            self._values["code_signing"] = code_signing
        if email_protection is not None:
            self._values["email_protection"] = email_protection
        if ocsp_signing is not None:
            self._values["ocsp_signing"] = ocsp_signing
        if server_auth is not None:
            self._values["server_auth"] = server_auth
        if time_stamping is not None:
            self._values["time_stamping"] = time_stamping

    @builtins.property
    def client_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#client_auth GooglePrivatecaCaPool#client_auth}
        '''
        result = self._values.get("client_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def code_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#code_signing GooglePrivatecaCaPool#code_signing}
        '''
        result = self._values.get("code_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def email_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#email_protection GooglePrivatecaCaPool#email_protection}
        '''
        result = self._values.get("email_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ocsp_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#ocsp_signing GooglePrivatecaCaPool#ocsp_signing}
        '''
        result = self._values.get("ocsp_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def server_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#server_auth GooglePrivatecaCaPool#server_auth}
        '''
        result = self._values.get("server_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def time_stamping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#time_stamping GooglePrivatecaCaPool#time_stamping}
        '''
        result = self._values.get("time_stamping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientAuth")
    def reset_client_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAuth", []))

    @jsii.member(jsii_name="resetCodeSigning")
    def reset_code_signing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeSigning", []))

    @jsii.member(jsii_name="resetEmailProtection")
    def reset_email_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailProtection", []))

    @jsii.member(jsii_name="resetOcspSigning")
    def reset_ocsp_signing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOcspSigning", []))

    @jsii.member(jsii_name="resetServerAuth")
    def reset_server_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerAuth", []))

    @jsii.member(jsii_name="resetTimeStamping")
    def reset_time_stamping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeStamping", []))

    @builtins.property
    @jsii.member(jsii_name="clientAuthInput")
    def client_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "clientAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="codeSigningInput")
    def code_signing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "codeSigningInput"))

    @builtins.property
    @jsii.member(jsii_name="emailProtectionInput")
    def email_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emailProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="ocspSigningInput")
    def ocsp_signing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ocspSigningInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAuthInput")
    def server_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "serverAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="timeStampingInput")
    def time_stamping_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "timeStampingInput"))

    @builtins.property
    @jsii.member(jsii_name="clientAuth")
    def client_auth(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "clientAuth"))

    @client_auth.setter
    def client_auth(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "client_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAuth", value)

    @builtins.property
    @jsii.member(jsii_name="codeSigning")
    def code_signing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "codeSigning"))

    @code_signing.setter
    def code_signing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "code_signing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeSigning", value)

    @builtins.property
    @jsii.member(jsii_name="emailProtection")
    def email_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emailProtection"))

    @email_protection.setter
    def email_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "email_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailProtection", value)

    @builtins.property
    @jsii.member(jsii_name="ocspSigning")
    def ocsp_signing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ocspSigning"))

    @ocsp_signing.setter
    def ocsp_signing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "ocsp_signing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ocspSigning", value)

    @builtins.property
    @jsii.member(jsii_name="serverAuth")
    def server_auth(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "serverAuth"))

    @server_auth.setter
    def server_auth(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "server_auth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAuth", value)

    @builtins.property
    @jsii.member(jsii_name="timeStamping")
    def time_stamping(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "timeStamping"))

    @time_stamping.setter
    def time_stamping(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "time_stamping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeStamping", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBaseKeyUsage")
    def put_base_key_usage(
        self,
        *,
        cert_sign: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        content_commitment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        crl_sign: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data_encipherment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        decipher_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        digital_signature: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encipher_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_agreement: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_encipherment: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#cert_sign GooglePrivatecaCaPool#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#content_commitment GooglePrivatecaCaPool#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#crl_sign GooglePrivatecaCaPool#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#data_encipherment GooglePrivatecaCaPool#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#decipher_only GooglePrivatecaCaPool#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#digital_signature GooglePrivatecaCaPool#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#encipher_only GooglePrivatecaCaPool#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_agreement GooglePrivatecaCaPool#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_encipherment GooglePrivatecaCaPool#key_encipherment}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage(
            cert_sign=cert_sign,
            content_commitment=content_commitment,
            crl_sign=crl_sign,
            data_encipherment=data_encipherment,
            decipher_only=decipher_only,
            digital_signature=digital_signature,
            encipher_only=encipher_only,
            key_agreement=key_agreement,
            key_encipherment=key_encipherment,
        )

        return typing.cast(None, jsii.invoke(self, "putBaseKeyUsage", [value]))

    @jsii.member(jsii_name="putExtendedKeyUsage")
    def put_extended_key_usage(
        self,
        *,
        client_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        code_signing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        email_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ocsp_signing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        server_auth: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        time_stamping: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#client_auth GooglePrivatecaCaPool#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#code_signing GooglePrivatecaCaPool#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#email_protection GooglePrivatecaCaPool#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#ocsp_signing GooglePrivatecaCaPool#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#server_auth GooglePrivatecaCaPool#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#time_stamping GooglePrivatecaCaPool#time_stamping}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage(
            client_auth=client_auth,
            code_signing=code_signing,
            email_protection=email_protection,
            ocsp_signing=ocsp_signing,
            server_auth=server_auth,
            time_stamping=time_stamping,
        )

        return typing.cast(None, jsii.invoke(self, "putExtendedKeyUsage", [value]))

    @jsii.member(jsii_name="putUnknownExtendedKeyUsages")
    def put_unknown_extended_key_usages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference.put_unknown_extended_key_usages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUnknownExtendedKeyUsages", [value]))

    @jsii.member(jsii_name="resetUnknownExtendedKeyUsages")
    def reset_unknown_extended_key_usages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnknownExtendedKeyUsages", []))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsageInput")
    def base_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage], jsii.get(self, "baseKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsageInput")
    def extended_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage], jsii.get(self, "extendedKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsagesInput")
    def unknown_extended_key_usages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages"]]], jsii.get(self, "unknownExtendedKeyUsagesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="objectIdPathInput")
    def object_id_path_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "objectIdPathInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdPath")
    def object_id_path(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "objectIdPath"))

    @object_id_path.setter
    def object_id_path(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalExtensions")
    def put_additional_extensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference.put_additional_extensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalExtensions", [value]))

    @jsii.member(jsii_name="putCaOptions")
    def put_ca_options(
        self,
        *,
        is_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
        non_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zero_max_issuer_path_length: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_ca: When true, the "CA" in Basic Constraints extension will be set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#is_ca GooglePrivatecaCaPool#is_ca}
        :param max_issuer_path_length: Refers to the "path length constraint" in Basic Constraints extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#max_issuer_path_length GooglePrivatecaCaPool#max_issuer_path_length}
        :param non_ca: When true, the "CA" in Basic Constraints extension will be set to false. If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#non_ca GooglePrivatecaCaPool#non_ca}
        :param zero_max_issuer_path_length: When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#zero_max_issuer_path_length GooglePrivatecaCaPool#zero_max_issuer_path_length}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions(
            is_ca=is_ca,
            max_issuer_path_length=max_issuer_path_length,
            non_ca=non_ca,
            zero_max_issuer_path_length=zero_max_issuer_path_length,
        )

        return typing.cast(None, jsii.invoke(self, "putCaOptions", [value]))

    @jsii.member(jsii_name="putKeyUsage")
    def put_key_usage(
        self,
        *,
        base_key_usage: typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage, typing.Dict[str, typing.Any]],
        extended_key_usage: typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage, typing.Dict[str, typing.Any]],
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#base_key_usage GooglePrivatecaCaPool#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#extended_key_usage GooglePrivatecaCaPool#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#unknown_extended_key_usages GooglePrivatecaCaPool#unknown_extended_key_usages}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage(
            base_key_usage=base_key_usage,
            extended_key_usage=extended_key_usage,
            unknown_extended_key_usages=unknown_extended_key_usages,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyUsage", [value]))

    @jsii.member(jsii_name="putPolicyIds")
    def put_policy_ids(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference.put_policy_ids)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicyIds", [value]))

    @jsii.member(jsii_name="resetAdditionalExtensions")
    def reset_additional_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalExtensions", []))

    @jsii.member(jsii_name="resetAiaOcspServers")
    def reset_aia_ocsp_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAiaOcspServers", []))

    @jsii.member(jsii_name="resetPolicyIds")
    def reset_policy_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyIds", []))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="caOptions")
    def ca_options(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference, jsii.get(self, "caOptions"))

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(
        self,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList":
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList", jsii.get(self, "policyIds"))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensionsInput")
    def additional_extensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions]]], jsii.get(self, "additionalExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServersInput")
    def aia_ocsp_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aiaOcspServersInput"))

    @builtins.property
    @jsii.member(jsii_name="caOptionsInput")
    def ca_options_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions], jsii.get(self, "caOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUsageInput")
    def key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage], jsii.get(self, "keyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdsInput")
    def policy_ids_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds"]]], jsii.get(self, "policyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServers")
    def aia_ocsp_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaOcspServers"))

    @aia_ocsp_servers.setter
    def aia_ocsp_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference, "aia_ocsp_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiaOcspServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValues]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#object_id_path GooglePrivatecaCaPool#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="objectIdPathInput")
    def object_id_path_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "objectIdPathInput"))

    @builtins.property
    @jsii.member(jsii_name="objectIdPath")
    def object_id_path(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "objectIdPath"))

    @object_id_path.setter
    def object_id_path(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints",
    jsii_struct_bases=[],
    name_mapping={
        "allow_subject_alt_names_passthrough": "allowSubjectAltNamesPassthrough",
        "allow_subject_passthrough": "allowSubjectPassthrough",
        "cel_expression": "celExpression",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints:
    def __init__(
        self,
        *,
        allow_subject_alt_names_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_subject_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        cel_expression: typing.Optional[typing.Union["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow_subject_alt_names_passthrough: If this is set, the SubjectAltNames extension may be copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_subject_alt_names_passthrough GooglePrivatecaCaPool#allow_subject_alt_names_passthrough}
        :param allow_subject_passthrough: If this is set, the Subject field may be copied from a certificate request into the signed certificate. Otherwise, the requested Subject will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_subject_passthrough GooglePrivatecaCaPool#allow_subject_passthrough}
        :param cel_expression: cel_expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#cel_expression GooglePrivatecaCaPool#cel_expression}
        '''
        if isinstance(cel_expression, dict):
            cel_expression = GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression(**cel_expression)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints.__init__)
            check_type(argname="argument allow_subject_alt_names_passthrough", value=allow_subject_alt_names_passthrough, expected_type=type_hints["allow_subject_alt_names_passthrough"])
            check_type(argname="argument allow_subject_passthrough", value=allow_subject_passthrough, expected_type=type_hints["allow_subject_passthrough"])
            check_type(argname="argument cel_expression", value=cel_expression, expected_type=type_hints["cel_expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "allow_subject_alt_names_passthrough": allow_subject_alt_names_passthrough,
            "allow_subject_passthrough": allow_subject_passthrough,
        }
        if cel_expression is not None:
            self._values["cel_expression"] = cel_expression

    @builtins.property
    def allow_subject_alt_names_passthrough(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If this is set, the SubjectAltNames extension may be copied from a certificate request into the signed certificate.

        Otherwise, the requested SubjectAltNames will be discarded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_subject_alt_names_passthrough GooglePrivatecaCaPool#allow_subject_alt_names_passthrough}
        '''
        result = self._values.get("allow_subject_alt_names_passthrough")
        assert result is not None, "Required property 'allow_subject_alt_names_passthrough' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def allow_subject_passthrough(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If this is set, the Subject field may be copied from a certificate request into the signed certificate.

        Otherwise, the requested Subject will be discarded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_subject_passthrough GooglePrivatecaCaPool#allow_subject_passthrough}
        '''
        result = self._values.get("allow_subject_passthrough")
        assert result is not None, "Required property 'allow_subject_passthrough' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def cel_expression(
        self,
    ) -> typing.Optional["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression"]:
        '''cel_expression block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#cel_expression GooglePrivatecaCaPool#cel_expression}
        '''
        result = self._values.get("cel_expression")
        return typing.cast(typing.Optional["GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "description": "description",
        "location": "location",
        "title": "title",
    },
)
class GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression:
    def __init__(
        self,
        *,
        expression: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#expression GooglePrivatecaCaPool#expression}
        :param description: Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#description GooglePrivatecaCaPool#description}
        :param location: String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#location GooglePrivatecaCaPool#location}
        :param title: Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#title GooglePrivatecaCaPool#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def expression(self) -> builtins.str:
        '''Textual representation of an expression in Common Expression Language syntax.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#expression GooglePrivatecaCaPool#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the expression.

        This is a longer text which describes the expression, e.g. when hovered over it in a UI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#description GooglePrivatecaCaPool#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#location GooglePrivatecaCaPool#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#title GooglePrivatecaCaPool#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCelExpression")
    def put_cel_expression(
        self,
        *,
        expression: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#expression GooglePrivatecaCaPool#expression}
        :param description: Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#description GooglePrivatecaCaPool#description}
        :param location: String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#location GooglePrivatecaCaPool#location}
        :param title: Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#title GooglePrivatecaCaPool#title}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression(
            expression=expression,
            description=description,
            location=location,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putCelExpression", [value]))

    @jsii.member(jsii_name="resetCelExpression")
    def reset_cel_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCelExpression", []))

    @builtins.property
    @jsii.member(jsii_name="celExpression")
    def cel_expression(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference, jsii.get(self, "celExpression"))

    @builtins.property
    @jsii.member(jsii_name="allowSubjectAltNamesPassthroughInput")
    def allow_subject_alt_names_passthrough_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowSubjectAltNamesPassthroughInput"))

    @builtins.property
    @jsii.member(jsii_name="allowSubjectPassthroughInput")
    def allow_subject_passthrough_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowSubjectPassthroughInput"))

    @builtins.property
    @jsii.member(jsii_name="celExpressionInput")
    def cel_expression_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression], jsii.get(self, "celExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowSubjectAltNamesPassthrough")
    def allow_subject_alt_names_passthrough(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowSubjectAltNamesPassthrough"))

    @allow_subject_alt_names_passthrough.setter
    def allow_subject_alt_names_passthrough(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference, "allow_subject_alt_names_passthrough").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSubjectAltNamesPassthrough", value)

    @builtins.property
    @jsii.member(jsii_name="allowSubjectPassthrough")
    def allow_subject_passthrough(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowSubjectPassthrough"))

    @allow_subject_passthrough.setter
    def allow_subject_passthrough(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference, "allow_subject_passthrough").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSubjectPassthrough", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCaPoolIssuancePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolIssuancePolicyOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowedIssuanceModes")
    def put_allowed_issuance_modes(
        self,
        *,
        allow_config_based_issuance: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_csr_based_issuance: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param allow_config_based_issuance: When true, allows callers to create Certificates by specifying a CertificateConfig. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_config_based_issuance GooglePrivatecaCaPool#allow_config_based_issuance}
        :param allow_csr_based_issuance: When true, allows callers to create Certificates by specifying a CSR. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_csr_based_issuance GooglePrivatecaCaPool#allow_csr_based_issuance}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes(
            allow_config_based_issuance=allow_config_based_issuance,
            allow_csr_based_issuance=allow_csr_based_issuance,
        )

        return typing.cast(None, jsii.invoke(self, "putAllowedIssuanceModes", [value]))

    @jsii.member(jsii_name="putAllowedKeyTypes")
    def put_allowed_key_types(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolIssuancePolicyOutputReference.put_allowed_key_types)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedKeyTypes", [value]))

    @jsii.member(jsii_name="putBaselineValues")
    def put_baseline_values(
        self,
        *,
        ca_options: typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions, typing.Dict[str, typing.Any]],
        key_usage: typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage, typing.Dict[str, typing.Any]],
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions, typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#ca_options GooglePrivatecaCaPool#ca_options}
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#key_usage GooglePrivatecaCaPool#key_usage}
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#additional_extensions GooglePrivatecaCaPool#additional_extensions}
        :param aia_ocsp_servers: Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#aia_ocsp_servers GooglePrivatecaCaPool#aia_ocsp_servers}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#policy_ids GooglePrivatecaCaPool#policy_ids}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyBaselineValues(
            ca_options=ca_options,
            key_usage=key_usage,
            additional_extensions=additional_extensions,
            aia_ocsp_servers=aia_ocsp_servers,
            policy_ids=policy_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putBaselineValues", [value]))

    @jsii.member(jsii_name="putIdentityConstraints")
    def put_identity_constraints(
        self,
        *,
        allow_subject_alt_names_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_subject_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        cel_expression: typing.Optional[typing.Union[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow_subject_alt_names_passthrough: If this is set, the SubjectAltNames extension may be copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_subject_alt_names_passthrough GooglePrivatecaCaPool#allow_subject_alt_names_passthrough}
        :param allow_subject_passthrough: If this is set, the Subject field may be copied from a certificate request into the signed certificate. Otherwise, the requested Subject will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#allow_subject_passthrough GooglePrivatecaCaPool#allow_subject_passthrough}
        :param cel_expression: cel_expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#cel_expression GooglePrivatecaCaPool#cel_expression}
        '''
        value = GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints(
            allow_subject_alt_names_passthrough=allow_subject_alt_names_passthrough,
            allow_subject_passthrough=allow_subject_passthrough,
            cel_expression=cel_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putIdentityConstraints", [value]))

    @jsii.member(jsii_name="resetAllowedIssuanceModes")
    def reset_allowed_issuance_modes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedIssuanceModes", []))

    @jsii.member(jsii_name="resetAllowedKeyTypes")
    def reset_allowed_key_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedKeyTypes", []))

    @jsii.member(jsii_name="resetBaselineValues")
    def reset_baseline_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineValues", []))

    @jsii.member(jsii_name="resetIdentityConstraints")
    def reset_identity_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityConstraints", []))

    @jsii.member(jsii_name="resetMaximumLifetime")
    def reset_maximum_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="allowedIssuanceModes")
    def allowed_issuance_modes(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference, jsii.get(self, "allowedIssuanceModes"))

    @builtins.property
    @jsii.member(jsii_name="allowedKeyTypes")
    def allowed_key_types(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList, jsii.get(self, "allowedKeyTypes"))

    @builtins.property
    @jsii.member(jsii_name="baselineValues")
    def baseline_values(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference, jsii.get(self, "baselineValues"))

    @builtins.property
    @jsii.member(jsii_name="identityConstraints")
    def identity_constraints(
        self,
    ) -> GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference:
        return typing.cast(GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference, jsii.get(self, "identityConstraints"))

    @builtins.property
    @jsii.member(jsii_name="allowedIssuanceModesInput")
    def allowed_issuance_modes_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes], jsii.get(self, "allowedIssuanceModesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedKeyTypesInput")
    def allowed_key_types_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes]]], jsii.get(self, "allowedKeyTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineValuesInput")
    def baseline_values_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValues]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyBaselineValues], jsii.get(self, "baselineValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="identityConstraintsInput")
    def identity_constraints_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints], jsii.get(self, "identityConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumLifetimeInput")
    def maximum_lifetime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumLifetime")
    def maximum_lifetime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumLifetime"))

    @maximum_lifetime.setter
    def maximum_lifetime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyOutputReference, "maximum_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePrivatecaCaPoolIssuancePolicy]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolIssuancePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolIssuancePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolIssuancePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolPublishingOptions",
    jsii_struct_bases=[],
    name_mapping={"publish_ca_cert": "publishCaCert", "publish_crl": "publishCrl"},
)
class GooglePrivatecaCaPoolPublishingOptions:
    def __init__(
        self,
        *,
        publish_ca_cert: typing.Union[builtins.bool, cdktf.IResolvable],
        publish_crl: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param publish_ca_cert: When true, publishes each CertificateAuthority's CA certificate and includes its URL in the "Authority Information Access" X.509 extension in all issued Certificates. If this is false, the CA certificate will not be published and the corresponding X.509 extension will not be written in issued certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publish_ca_cert GooglePrivatecaCaPool#publish_ca_cert}
        :param publish_crl: When true, publishes each CertificateAuthority's CRL and includes its URL in the "CRL Distribution Points" X.509 extension in all issued Certificates. If this is false, CRLs will not be published and the corresponding X.509 extension will not be written in issued certificates. CRLs will expire 7 days from their creation. However, we will rebuild daily. CRLs are also rebuilt shortly after a certificate is revoked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publish_crl GooglePrivatecaCaPool#publish_crl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolPublishingOptions.__init__)
            check_type(argname="argument publish_ca_cert", value=publish_ca_cert, expected_type=type_hints["publish_ca_cert"])
            check_type(argname="argument publish_crl", value=publish_crl, expected_type=type_hints["publish_crl"])
        self._values: typing.Dict[str, typing.Any] = {
            "publish_ca_cert": publish_ca_cert,
            "publish_crl": publish_crl,
        }

    @builtins.property
    def publish_ca_cert(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When true, publishes each CertificateAuthority's CA certificate and includes its URL in the "Authority Information Access" X.509 extension in all issued Certificates. If this is false, the CA certificate will not be published and the corresponding X.509 extension will not be written in issued certificates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publish_ca_cert GooglePrivatecaCaPool#publish_ca_cert}
        '''
        result = self._values.get("publish_ca_cert")
        assert result is not None, "Required property 'publish_ca_cert' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def publish_crl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When true, publishes each CertificateAuthority's CRL and includes its URL in the "CRL Distribution Points" X.509 extension in all issued Certificates. If this is false, CRLs will not be published and the corresponding X.509 extension will not be written in issued certificates. CRLs will expire 7 days from their creation. However, we will rebuild daily. CRLs are also rebuilt shortly after a certificate is revoked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#publish_crl GooglePrivatecaCaPool#publish_crl}
        '''
        result = self._values.get("publish_crl")
        assert result is not None, "Required property 'publish_crl' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolPublishingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolPublishingOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolPublishingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolPublishingOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="publishCaCertInput")
    def publish_ca_cert_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishCaCertInput"))

    @builtins.property
    @jsii.member(jsii_name="publishCrlInput")
    def publish_crl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishCrlInput"))

    @builtins.property
    @jsii.member(jsii_name="publishCaCert")
    def publish_ca_cert(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publishCaCert"))

    @publish_ca_cert.setter
    def publish_ca_cert(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolPublishingOptionsOutputReference, "publish_ca_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishCaCert", value)

    @builtins.property
    @jsii.member(jsii_name="publishCrl")
    def publish_crl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publishCrl"))

    @publish_crl.setter
    def publish_crl(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolPublishingOptionsOutputReference, "publish_crl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishCrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePrivatecaCaPoolPublishingOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCaPoolPublishingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCaPoolPublishingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolPublishingOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePrivatecaCaPoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#create GooglePrivatecaCaPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#delete GooglePrivatecaCaPool#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#update GooglePrivatecaCaPool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#create GooglePrivatecaCaPool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#delete GooglePrivatecaCaPool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_ca_pool#update GooglePrivatecaCaPool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCaPoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCaPoolTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCaPool.GooglePrivatecaCaPoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCaPoolTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCaPoolTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCaPoolTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCaPoolTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCaPoolTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePrivatecaCaPool",
    "GooglePrivatecaCaPoolConfig",
    "GooglePrivatecaCaPoolIssuancePolicy",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModes",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedIssuanceModesOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypes",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurve",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesEllipticCurveOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesList",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsa",
    "GooglePrivatecaCaPoolIssuancePolicyAllowedKeyTypesRsaOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValues",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensions",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsList",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectId",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsObjectIdOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesAdditionalExtensionsOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptions",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesCaOptionsOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsage",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsage",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageBaseKeyUsageOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsage",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageExtendedKeyUsageOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsages",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesList",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIds",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsList",
    "GooglePrivatecaCaPoolIssuancePolicyBaselineValuesPolicyIdsOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyIdentityConstraints",
    "GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpression",
    "GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsCelExpressionOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyIdentityConstraintsOutputReference",
    "GooglePrivatecaCaPoolIssuancePolicyOutputReference",
    "GooglePrivatecaCaPoolPublishingOptions",
    "GooglePrivatecaCaPoolPublishingOptionsOutputReference",
    "GooglePrivatecaCaPoolTimeouts",
    "GooglePrivatecaCaPoolTimeoutsOutputReference",
]

publication.publish()
