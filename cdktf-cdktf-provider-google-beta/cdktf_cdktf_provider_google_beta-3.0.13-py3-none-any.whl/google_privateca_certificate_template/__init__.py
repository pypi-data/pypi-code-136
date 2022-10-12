'''
# `google_privateca_certificate_template`

Refer to the Terraform Registory for docs: [`google_privateca_certificate_template`](https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template).
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


class GooglePrivatecaCertificateTemplate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template google_privateca_certificate_template}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity_constraints: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateIdentityConstraints", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        passthrough_extensions: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePassthroughExtensions", typing.Dict[str, typing.Any]]] = None,
        predefined_values: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValues", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template google_privateca_certificate_template} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#location GooglePrivatecaCertificateTemplate#location}
        :param name: The resource name for this CertificateTemplate in the format ``projects/*\\/locations/*\\/certificateTemplates/*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#name GooglePrivatecaCertificateTemplate#name}
        :param description: Optional. A human-readable description of scenarios this template is intended for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#description GooglePrivatecaCertificateTemplate#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#id GooglePrivatecaCertificateTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_constraints: identity_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#identity_constraints GooglePrivatecaCertificateTemplate#identity_constraints}
        :param labels: Optional. Labels with user-defined metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#labels GooglePrivatecaCertificateTemplate#labels}
        :param passthrough_extensions: passthrough_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#passthrough_extensions GooglePrivatecaCertificateTemplate#passthrough_extensions}
        :param predefined_values: predefined_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#predefined_values GooglePrivatecaCertificateTemplate#predefined_values}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#project GooglePrivatecaCertificateTemplate#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#timeouts GooglePrivatecaCertificateTemplate#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GooglePrivatecaCertificateTemplateConfig(
            location=location,
            name=name,
            description=description,
            id=id,
            identity_constraints=identity_constraints,
            labels=labels,
            passthrough_extensions=passthrough_extensions,
            predefined_values=predefined_values,
            project=project,
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

    @jsii.member(jsii_name="putIdentityConstraints")
    def put_identity_constraints(
        self,
        *,
        allow_subject_alt_names_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_subject_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        cel_expression: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow_subject_alt_names_passthrough: Required. If this is true, the SubjectAltNames extension may be copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#allow_subject_alt_names_passthrough GooglePrivatecaCertificateTemplate#allow_subject_alt_names_passthrough}
        :param allow_subject_passthrough: Required. If this is true, the Subject field may be copied from a certificate request into the signed certificate. Otherwise, the requested Subject will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#allow_subject_passthrough GooglePrivatecaCertificateTemplate#allow_subject_passthrough}
        :param cel_expression: cel_expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#cel_expression GooglePrivatecaCertificateTemplate#cel_expression}
        '''
        value = GooglePrivatecaCertificateTemplateIdentityConstraints(
            allow_subject_alt_names_passthrough=allow_subject_alt_names_passthrough,
            allow_subject_passthrough=allow_subject_passthrough,
            cel_expression=cel_expression,
        )

        return typing.cast(None, jsii.invoke(self, "putIdentityConstraints", [value]))

    @jsii.member(jsii_name="putPassthroughExtensions")
    def put_passthrough_extensions(
        self,
        *,
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        known_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#additional_extensions GooglePrivatecaCertificateTemplate#additional_extensions}
        :param known_extensions: Optional. A set of named X.509 extensions. Will be combined with additional_extensions to determine the full set of X.509 extensions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#known_extensions GooglePrivatecaCertificateTemplate#known_extensions}
        '''
        value = GooglePrivatecaCertificateTemplatePassthroughExtensions(
            additional_extensions=additional_extensions,
            known_extensions=known_extensions,
        )

        return typing.cast(None, jsii.invoke(self, "putPassthroughExtensions", [value]))

    @jsii.member(jsii_name="putPredefinedValues")
    def put_predefined_values(
        self,
        *,
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ca_options: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions", typing.Dict[str, typing.Any]]] = None,
        key_usage: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage", typing.Dict[str, typing.Any]]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#additional_extensions GooglePrivatecaCertificateTemplate#additional_extensions}
        :param aia_ocsp_servers: Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#aia_ocsp_servers GooglePrivatecaCertificateTemplate#aia_ocsp_servers}
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#ca_options GooglePrivatecaCertificateTemplate#ca_options}
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_usage GooglePrivatecaCertificateTemplate#key_usage}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#policy_ids GooglePrivatecaCertificateTemplate#policy_ids}
        '''
        value = GooglePrivatecaCertificateTemplatePredefinedValues(
            additional_extensions=additional_extensions,
            aia_ocsp_servers=aia_ocsp_servers,
            ca_options=ca_options,
            key_usage=key_usage,
            policy_ids=policy_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putPredefinedValues", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#create GooglePrivatecaCertificateTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#delete GooglePrivatecaCertificateTemplate#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#update GooglePrivatecaCertificateTemplate#update}.
        '''
        value = GooglePrivatecaCertificateTemplateTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityConstraints")
    def reset_identity_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityConstraints", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPassthroughExtensions")
    def reset_passthrough_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassthroughExtensions", []))

    @jsii.member(jsii_name="resetPredefinedValues")
    def reset_predefined_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredefinedValues", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="identityConstraints")
    def identity_constraints(
        self,
    ) -> "GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference":
        return typing.cast("GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference", jsii.get(self, "identityConstraints"))

    @builtins.property
    @jsii.member(jsii_name="passthroughExtensions")
    def passthrough_extensions(
        self,
    ) -> "GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference":
        return typing.cast("GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference", jsii.get(self, "passthroughExtensions"))

    @builtins.property
    @jsii.member(jsii_name="predefinedValues")
    def predefined_values(
        self,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference":
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference", jsii.get(self, "predefinedValues"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePrivatecaCertificateTemplateTimeoutsOutputReference":
        return typing.cast("GooglePrivatecaCertificateTemplateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="identityConstraintsInput")
    def identity_constraints_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplateIdentityConstraints"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplateIdentityConstraints"], jsii.get(self, "identityConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="passthroughExtensionsInput")
    def passthrough_extensions_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePassthroughExtensions"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePassthroughExtensions"], jsii.get(self, "passthroughExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="predefinedValuesInput")
    def predefined_values_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValues"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValues"], jsii.get(self, "predefinedValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplate, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplate, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplate, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateConfig",
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
        "description": "description",
        "id": "id",
        "identity_constraints": "identityConstraints",
        "labels": "labels",
        "passthrough_extensions": "passthroughExtensions",
        "predefined_values": "predefinedValues",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GooglePrivatecaCertificateTemplateConfig(cdktf.TerraformMetaArguments):
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
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity_constraints: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateIdentityConstraints", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        passthrough_extensions: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePassthroughExtensions", typing.Dict[str, typing.Any]]] = None,
        predefined_values: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValues", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#location GooglePrivatecaCertificateTemplate#location}
        :param name: The resource name for this CertificateTemplate in the format ``projects/*\\/locations/*\\/certificateTemplates/*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#name GooglePrivatecaCertificateTemplate#name}
        :param description: Optional. A human-readable description of scenarios this template is intended for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#description GooglePrivatecaCertificateTemplate#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#id GooglePrivatecaCertificateTemplate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_constraints: identity_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#identity_constraints GooglePrivatecaCertificateTemplate#identity_constraints}
        :param labels: Optional. Labels with user-defined metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#labels GooglePrivatecaCertificateTemplate#labels}
        :param passthrough_extensions: passthrough_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#passthrough_extensions GooglePrivatecaCertificateTemplate#passthrough_extensions}
        :param predefined_values: predefined_values block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#predefined_values GooglePrivatecaCertificateTemplate#predefined_values}
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#project GooglePrivatecaCertificateTemplate#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#timeouts GooglePrivatecaCertificateTemplate#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(identity_constraints, dict):
            identity_constraints = GooglePrivatecaCertificateTemplateIdentityConstraints(**identity_constraints)
        if isinstance(passthrough_extensions, dict):
            passthrough_extensions = GooglePrivatecaCertificateTemplatePassthroughExtensions(**passthrough_extensions)
        if isinstance(predefined_values, dict):
            predefined_values = GooglePrivatecaCertificateTemplatePredefinedValues(**predefined_values)
        if isinstance(timeouts, dict):
            timeouts = GooglePrivatecaCertificateTemplateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_constraints", value=identity_constraints, expected_type=type_hints["identity_constraints"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument passthrough_extensions", value=passthrough_extensions, expected_type=type_hints["passthrough_extensions"])
            check_type(argname="argument predefined_values", value=predefined_values, expected_type=type_hints["predefined_values"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if identity_constraints is not None:
            self._values["identity_constraints"] = identity_constraints
        if labels is not None:
            self._values["labels"] = labels
        if passthrough_extensions is not None:
            self._values["passthrough_extensions"] = passthrough_extensions
        if predefined_values is not None:
            self._values["predefined_values"] = predefined_values
        if project is not None:
            self._values["project"] = project
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
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#location GooglePrivatecaCertificateTemplate#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The resource name for this CertificateTemplate in the format ``projects/*\\/locations/*\\/certificateTemplates/*``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#name GooglePrivatecaCertificateTemplate#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional. A human-readable description of scenarios this template is intended for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#description GooglePrivatecaCertificateTemplate#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#id GooglePrivatecaCertificateTemplate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_constraints(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplateIdentityConstraints"]:
        '''identity_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#identity_constraints GooglePrivatecaCertificateTemplate#identity_constraints}
        '''
        result = self._values.get("identity_constraints")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplateIdentityConstraints"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. Labels with user-defined metadata.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#labels GooglePrivatecaCertificateTemplate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def passthrough_extensions(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePassthroughExtensions"]:
        '''passthrough_extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#passthrough_extensions GooglePrivatecaCertificateTemplate#passthrough_extensions}
        '''
        result = self._values.get("passthrough_extensions")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePassthroughExtensions"], result)

    @builtins.property
    def predefined_values(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValues"]:
        '''predefined_values block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#predefined_values GooglePrivatecaCertificateTemplate#predefined_values}
        '''
        result = self._values.get("predefined_values")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValues"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#project GooglePrivatecaCertificateTemplate#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GooglePrivatecaCertificateTemplateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#timeouts GooglePrivatecaCertificateTemplate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplateTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateIdentityConstraints",
    jsii_struct_bases=[],
    name_mapping={
        "allow_subject_alt_names_passthrough": "allowSubjectAltNamesPassthrough",
        "allow_subject_passthrough": "allowSubjectPassthrough",
        "cel_expression": "celExpression",
    },
)
class GooglePrivatecaCertificateTemplateIdentityConstraints:
    def __init__(
        self,
        *,
        allow_subject_alt_names_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        allow_subject_passthrough: typing.Union[builtins.bool, cdktf.IResolvable],
        cel_expression: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow_subject_alt_names_passthrough: Required. If this is true, the SubjectAltNames extension may be copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#allow_subject_alt_names_passthrough GooglePrivatecaCertificateTemplate#allow_subject_alt_names_passthrough}
        :param allow_subject_passthrough: Required. If this is true, the Subject field may be copied from a certificate request into the signed certificate. Otherwise, the requested Subject will be discarded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#allow_subject_passthrough GooglePrivatecaCertificateTemplate#allow_subject_passthrough}
        :param cel_expression: cel_expression block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#cel_expression GooglePrivatecaCertificateTemplate#cel_expression}
        '''
        if isinstance(cel_expression, dict):
            cel_expression = GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression(**cel_expression)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateIdentityConstraints.__init__)
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
        '''Required.

        If this is true, the SubjectAltNames extension may be copied from a certificate request into the signed certificate. Otherwise, the requested SubjectAltNames will be discarded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#allow_subject_alt_names_passthrough GooglePrivatecaCertificateTemplate#allow_subject_alt_names_passthrough}
        '''
        result = self._values.get("allow_subject_alt_names_passthrough")
        assert result is not None, "Required property 'allow_subject_alt_names_passthrough' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def allow_subject_passthrough(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Required.

        If this is true, the Subject field may be copied from a certificate request into the signed certificate. Otherwise, the requested Subject will be discarded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#allow_subject_passthrough GooglePrivatecaCertificateTemplate#allow_subject_passthrough}
        '''
        result = self._values.get("allow_subject_passthrough")
        assert result is not None, "Required property 'allow_subject_passthrough' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def cel_expression(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression"]:
        '''cel_expression block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#cel_expression GooglePrivatecaCertificateTemplate#cel_expression}
        '''
        result = self._values.get("cel_expression")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplateIdentityConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "expression": "expression",
        "location": "location",
        "title": "title",
    },
)
class GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        expression: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#description GooglePrivatecaCertificateTemplate#description}
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#expression GooglePrivatecaCertificateTemplate#expression}
        :param location: Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#location GooglePrivatecaCertificateTemplate#location}
        :param title: Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#title GooglePrivatecaCertificateTemplate#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if expression is not None:
            self._values["expression"] = expression
        if location is not None:
            self._values["location"] = location
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#description GooglePrivatecaCertificateTemplate#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Textual representation of an expression in Common Expression Language syntax.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#expression GooglePrivatecaCertificateTemplate#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Optional.

        String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#location GooglePrivatecaCertificateTemplate#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Optional.

        Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#title GooglePrivatecaCertificateTemplate#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCelExpression")
    def put_cel_expression(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        expression: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description: Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#description GooglePrivatecaCertificateTemplate#description}
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#expression GooglePrivatecaCertificateTemplate#expression}
        :param location: Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#location GooglePrivatecaCertificateTemplate#location}
        :param title: Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#title GooglePrivatecaCertificateTemplate#title}
        '''
        value = GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression(
            description=description,
            expression=expression,
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
    ) -> GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference:
        return typing.cast(GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference, jsii.get(self, "celExpression"))

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
    ) -> typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression], jsii.get(self, "celExpressionInput"))

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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference, "allow_subject_alt_names_passthrough").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference, "allow_subject_passthrough").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSubjectPassthrough", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraints]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplateIdentityConstraints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePassthroughExtensions",
    jsii_struct_bases=[],
    name_mapping={
        "additional_extensions": "additionalExtensions",
        "known_extensions": "knownExtensions",
    },
)
class GooglePrivatecaCertificateTemplatePassthroughExtensions:
    def __init__(
        self,
        *,
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        known_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#additional_extensions GooglePrivatecaCertificateTemplate#additional_extensions}
        :param known_extensions: Optional. A set of named X.509 extensions. Will be combined with additional_extensions to determine the full set of X.509 extensions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#known_extensions GooglePrivatecaCertificateTemplate#known_extensions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensions.__init__)
            check_type(argname="argument additional_extensions", value=additional_extensions, expected_type=type_hints["additional_extensions"])
            check_type(argname="argument known_extensions", value=known_extensions, expected_type=type_hints["known_extensions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_extensions is not None:
            self._values["additional_extensions"] = additional_extensions
        if known_extensions is not None:
            self._values["known_extensions"] = known_extensions

    @builtins.property
    def additional_extensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions"]]]:
        '''additional_extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#additional_extensions GooglePrivatecaCertificateTemplate#additional_extensions}
        '''
        result = self._values.get("additional_extensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions"]]], result)

    @builtins.property
    def known_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        A set of named X.509 extensions. Will be combined with additional_extensions to determine the full set of X.509 extensions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#known_extensions GooglePrivatecaCertificateTemplate#known_extensions}
        '''
        result = self._values.get("known_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePassthroughExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: Required. The parts of an OID path. The most significant parts of the path come first. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''Required. The parts of an OID path. The most significant parts of the path come first.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalExtensions")
    def put_additional_extensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference.put_additional_extensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalExtensions", [value]))

    @jsii.member(jsii_name="resetAdditionalExtensions")
    def reset_additional_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalExtensions", []))

    @jsii.member(jsii_name="resetKnownExtensions")
    def reset_known_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKnownExtensions", []))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList:
        return typing.cast(GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensionsInput")
    def additional_extensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions]]], jsii.get(self, "additionalExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="knownExtensionsInput")
    def known_extensions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "knownExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="knownExtensions")
    def known_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "knownExtensions"))

    @known_extensions.setter
    def known_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference, "known_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knownExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePassthroughExtensions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePassthroughExtensions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePassthroughExtensions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValues",
    jsii_struct_bases=[],
    name_mapping={
        "additional_extensions": "additionalExtensions",
        "aia_ocsp_servers": "aiaOcspServers",
        "ca_options": "caOptions",
        "key_usage": "keyUsage",
        "policy_ids": "policyIds",
    },
)
class GooglePrivatecaCertificateTemplatePredefinedValues:
    def __init__(
        self,
        *,
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ca_options: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions", typing.Dict[str, typing.Any]]] = None,
        key_usage: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage", typing.Dict[str, typing.Any]]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#additional_extensions GooglePrivatecaCertificateTemplate#additional_extensions}
        :param aia_ocsp_servers: Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#aia_ocsp_servers GooglePrivatecaCertificateTemplate#aia_ocsp_servers}
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#ca_options GooglePrivatecaCertificateTemplate#ca_options}
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_usage GooglePrivatecaCertificateTemplate#key_usage}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#policy_ids GooglePrivatecaCertificateTemplate#policy_ids}
        '''
        if isinstance(ca_options, dict):
            ca_options = GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions(**ca_options)
        if isinstance(key_usage, dict):
            key_usage = GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage(**key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValues.__init__)
            check_type(argname="argument additional_extensions", value=additional_extensions, expected_type=type_hints["additional_extensions"])
            check_type(argname="argument aia_ocsp_servers", value=aia_ocsp_servers, expected_type=type_hints["aia_ocsp_servers"])
            check_type(argname="argument ca_options", value=ca_options, expected_type=type_hints["ca_options"])
            check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            check_type(argname="argument policy_ids", value=policy_ids, expected_type=type_hints["policy_ids"])
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_extensions is not None:
            self._values["additional_extensions"] = additional_extensions
        if aia_ocsp_servers is not None:
            self._values["aia_ocsp_servers"] = aia_ocsp_servers
        if ca_options is not None:
            self._values["ca_options"] = ca_options
        if key_usage is not None:
            self._values["key_usage"] = key_usage
        if policy_ids is not None:
            self._values["policy_ids"] = policy_ids

    @builtins.property
    def additional_extensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions"]]]:
        '''additional_extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#additional_extensions GooglePrivatecaCertificateTemplate#additional_extensions}
        '''
        result = self._values.get("additional_extensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions"]]], result)

    @builtins.property
    def aia_ocsp_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#aia_ocsp_servers GooglePrivatecaCertificateTemplate#aia_ocsp_servers}
        '''
        result = self._values.get("aia_ocsp_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ca_options(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions"]:
        '''ca_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#ca_options GooglePrivatecaCertificateTemplate#ca_options}
        '''
        result = self._values.get("ca_options")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions"], result)

    @builtins.property
    def key_usage(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage"]:
        '''key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_usage GooglePrivatecaCertificateTemplate#key_usage}
        '''
        result = self._values.get("key_usage")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage"], result)

    @builtins.property
    def policy_ids(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds"]]]:
        '''policy_ids block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#policy_ids GooglePrivatecaCertificateTemplate#policy_ids}
        '''
        result = self._values.get("policy_ids")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={"object_id": "objectId", "value": "value", "critical": "critical"},
)
class GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions:
    def __init__(
        self,
        *,
        object_id: typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId", typing.Dict[str, typing.Any]],
        value: builtins.str,
        critical: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param object_id: object_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id GooglePrivatecaCertificateTemplate#object_id}
        :param value: Required. The value of this X.509 extension. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#value GooglePrivatecaCertificateTemplate#value}
        :param critical: Optional. Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#critical GooglePrivatecaCertificateTemplate#critical}
        '''
        if isinstance(object_id, dict):
            object_id = GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId(**object_id)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions.__init__)
            check_type(argname="argument object_id", value=object_id, expected_type=type_hints["object_id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id": object_id,
            "value": value,
        }
        if critical is not None:
            self._values["critical"] = critical

    @builtins.property
    def object_id(
        self,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId":
        '''object_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id GooglePrivatecaCertificateTemplate#object_id}
        '''
        result = self._values.get("object_id")
        assert result is not None, "Required property 'object_id' is missing"
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId", result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Required. The value of this X.509 extension.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#value GooglePrivatecaCertificateTemplate#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def critical(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#critical GooglePrivatecaCertificateTemplate#critical}
        '''
        result = self._values.get("critical")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: Required. The parts of an OID path. The most significant parts of the path come first. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''Required. The parts of an OID path. The most significant parts of the path come first.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectId")
    def put_object_id(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: Required. The parts of an OID path. The most significant parts of the path come first. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        value = GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId(
            object_id_path=object_id_path
        )

        return typing.cast(None, jsii.invoke(self, "putObjectId", [value]))

    @jsii.member(jsii_name="resetCritical")
    def reset_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCritical", []))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(
        self,
    ) -> GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference:
        return typing.cast(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference, jsii.get(self, "objectId"))

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
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId], jsii.get(self, "objectIdInput"))

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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference, "critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "critical", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions",
    jsii_struct_bases=[],
    name_mapping={"is_ca": "isCa", "max_issuer_path_length": "maxIssuerPathLength"},
)
class GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions:
    def __init__(
        self,
        *,
        is_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param is_ca: Optional. Refers to the "CA" X.509 extension, which is a boolean value. When this value is missing, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#is_ca GooglePrivatecaCertificateTemplate#is_ca}
        :param max_issuer_path_length: Optional. Refers to the path length restriction X.509 extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. If this value is missing, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#max_issuer_path_length GooglePrivatecaCertificateTemplate#max_issuer_path_length}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions.__init__)
            check_type(argname="argument is_ca", value=is_ca, expected_type=type_hints["is_ca"])
            check_type(argname="argument max_issuer_path_length", value=max_issuer_path_length, expected_type=type_hints["max_issuer_path_length"])
        self._values: typing.Dict[str, typing.Any] = {}
        if is_ca is not None:
            self._values["is_ca"] = is_ca
        if max_issuer_path_length is not None:
            self._values["max_issuer_path_length"] = max_issuer_path_length

    @builtins.property
    def is_ca(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional.

        Refers to the "CA" X.509 extension, which is a boolean value. When this value is missing, the extension will be omitted from the CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#is_ca GooglePrivatecaCertificateTemplate#is_ca}
        '''
        result = self._values.get("is_ca")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_issuer_path_length(self) -> typing.Optional[jsii.Number]:
        '''Optional.

        Refers to the path length restriction X.509 extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. If this value is missing, the max path length will be omitted from the CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#max_issuer_path_length GooglePrivatecaCertificateTemplate#max_issuer_path_length}
        '''
        result = self._values.get("max_issuer_path_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsCa")
    def reset_is_ca(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCa", []))

    @jsii.member(jsii_name="resetMaxIssuerPathLength")
    def reset_max_issuer_path_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIssuerPathLength", []))

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
    @jsii.member(jsii_name="isCa")
    def is_ca(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCa"))

    @is_ca.setter
    def is_ca(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference, "is_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCa", value)

    @builtins.property
    @jsii.member(jsii_name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIssuerPathLength"))

    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference, "max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage",
    jsii_struct_bases=[],
    name_mapping={
        "base_key_usage": "baseKeyUsage",
        "extended_key_usage": "extendedKeyUsage",
        "unknown_extended_key_usages": "unknownExtendedKeyUsages",
    },
)
class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage:
    def __init__(
        self,
        *,
        base_key_usage: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage", typing.Dict[str, typing.Any]]] = None,
        extended_key_usage: typing.Optional[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage", typing.Dict[str, typing.Any]]] = None,
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#base_key_usage GooglePrivatecaCertificateTemplate#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#extended_key_usage GooglePrivatecaCertificateTemplate#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#unknown_extended_key_usages GooglePrivatecaCertificateTemplate#unknown_extended_key_usages}
        '''
        if isinstance(base_key_usage, dict):
            base_key_usage = GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage(**base_key_usage)
        if isinstance(extended_key_usage, dict):
            extended_key_usage = GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage(**extended_key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage.__init__)
            check_type(argname="argument base_key_usage", value=base_key_usage, expected_type=type_hints["base_key_usage"])
            check_type(argname="argument extended_key_usage", value=extended_key_usage, expected_type=type_hints["extended_key_usage"])
            check_type(argname="argument unknown_extended_key_usages", value=unknown_extended_key_usages, expected_type=type_hints["unknown_extended_key_usages"])
        self._values: typing.Dict[str, typing.Any] = {}
        if base_key_usage is not None:
            self._values["base_key_usage"] = base_key_usage
        if extended_key_usage is not None:
            self._values["extended_key_usage"] = extended_key_usage
        if unknown_extended_key_usages is not None:
            self._values["unknown_extended_key_usages"] = unknown_extended_key_usages

    @builtins.property
    def base_key_usage(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage"]:
        '''base_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#base_key_usage GooglePrivatecaCertificateTemplate#base_key_usage}
        '''
        result = self._values.get("base_key_usage")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage"], result)

    @builtins.property
    def extended_key_usage(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage"]:
        '''extended_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#extended_key_usage GooglePrivatecaCertificateTemplate#extended_key_usage}
        '''
        result = self._values.get("extended_key_usage")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage"], result)

    @builtins.property
    def unknown_extended_key_usages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages"]]]:
        '''unknown_extended_key_usages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#unknown_extended_key_usages GooglePrivatecaCertificateTemplate#unknown_extended_key_usages}
        '''
        result = self._values.get("unknown_extended_key_usages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage",
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
class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage:
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
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#cert_sign GooglePrivatecaCertificateTemplate#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#content_commitment GooglePrivatecaCertificateTemplate#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#crl_sign GooglePrivatecaCertificateTemplate#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#data_encipherment GooglePrivatecaCertificateTemplate#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#decipher_only GooglePrivatecaCertificateTemplate#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#digital_signature GooglePrivatecaCertificateTemplate#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#encipher_only GooglePrivatecaCertificateTemplate#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_agreement GooglePrivatecaCertificateTemplate#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_encipherment GooglePrivatecaCertificateTemplate#key_encipherment}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#cert_sign GooglePrivatecaCertificateTemplate#cert_sign}
        '''
        result = self._values.get("cert_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def content_commitment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#content_commitment GooglePrivatecaCertificateTemplate#content_commitment}
        '''
        result = self._values.get("content_commitment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def crl_sign(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used sign certificate revocation lists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#crl_sign GooglePrivatecaCertificateTemplate#crl_sign}
        '''
        result = self._values.get("crl_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#data_encipherment GooglePrivatecaCertificateTemplate#data_encipherment}
        '''
        result = self._values.get("data_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def decipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to decipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#decipher_only GooglePrivatecaCertificateTemplate#decipher_only}
        '''
        result = self._values.get("decipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def digital_signature(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for digital signatures.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#digital_signature GooglePrivatecaCertificateTemplate#digital_signature}
        '''
        result = self._values.get("digital_signature")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#encipher_only GooglePrivatecaCertificateTemplate#encipher_only}
        '''
        result = self._values.get("encipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_agreement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used in a key agreement protocol.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_agreement GooglePrivatecaCertificateTemplate#key_agreement}
        '''
        result = self._values.get("key_agreement")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher other keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_encipherment GooglePrivatecaCertificateTemplate#key_encipherment}
        '''
        result = self._values.get("key_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "cert_sign").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "content_commitment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentCommitment", value)

    @builtins.property
    @jsii.member(jsii_name="crlSign")
    def crl_sign(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "crlSign"))

    @crl_sign.setter
    def crl_sign(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "crl_sign").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "data_encipherment").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "decipher_only").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "digital_signature").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "encipher_only").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "key_agreement").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "key_encipherment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyEncipherment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage",
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
class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage:
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
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#client_auth GooglePrivatecaCertificateTemplate#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#code_signing GooglePrivatecaCertificateTemplate#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#email_protection GooglePrivatecaCertificateTemplate#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#ocsp_signing GooglePrivatecaCertificateTemplate#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#server_auth GooglePrivatecaCertificateTemplate#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#time_stamping GooglePrivatecaCertificateTemplate#time_stamping}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#client_auth GooglePrivatecaCertificateTemplate#client_auth}
        '''
        result = self._values.get("client_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def code_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#code_signing GooglePrivatecaCertificateTemplate#code_signing}
        '''
        result = self._values.get("code_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def email_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#email_protection GooglePrivatecaCertificateTemplate#email_protection}
        '''
        result = self._values.get("email_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ocsp_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#ocsp_signing GooglePrivatecaCertificateTemplate#ocsp_signing}
        '''
        result = self._values.get("ocsp_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def server_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#server_auth GooglePrivatecaCertificateTemplate#server_auth}
        '''
        result = self._values.get("server_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def time_stamping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#time_stamping GooglePrivatecaCertificateTemplate#time_stamping}
        '''
        result = self._values.get("time_stamping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "client_auth").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "code_signing").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "email_protection").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "ocsp_signing").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "server_auth").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "time_stamping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeStamping", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference.__init__)
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
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#cert_sign GooglePrivatecaCertificateTemplate#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#content_commitment GooglePrivatecaCertificateTemplate#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#crl_sign GooglePrivatecaCertificateTemplate#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#data_encipherment GooglePrivatecaCertificateTemplate#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#decipher_only GooglePrivatecaCertificateTemplate#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#digital_signature GooglePrivatecaCertificateTemplate#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#encipher_only GooglePrivatecaCertificateTemplate#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_agreement GooglePrivatecaCertificateTemplate#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#key_encipherment GooglePrivatecaCertificateTemplate#key_encipherment}
        '''
        value = GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage(
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
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#client_auth GooglePrivatecaCertificateTemplate#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#code_signing GooglePrivatecaCertificateTemplate#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#email_protection GooglePrivatecaCertificateTemplate#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#ocsp_signing GooglePrivatecaCertificateTemplate#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#server_auth GooglePrivatecaCertificateTemplate#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#time_stamping GooglePrivatecaCertificateTemplate#time_stamping}
        '''
        value = GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage(
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference.put_unknown_extended_key_usages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUnknownExtendedKeyUsages", [value]))

    @jsii.member(jsii_name="resetBaseKeyUsage")
    def reset_base_key_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseKeyUsage", []))

    @jsii.member(jsii_name="resetExtendedKeyUsage")
    def reset_extended_key_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedKeyUsage", []))

    @jsii.member(jsii_name="resetUnknownExtendedKeyUsages")
    def reset_unknown_extended_key_usages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnknownExtendedKeyUsages", []))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsageInput")
    def base_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage], jsii.get(self, "baseKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsageInput")
    def extended_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage], jsii.get(self, "extendedKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsagesInput")
    def unknown_extended_key_usages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages"]]], jsii.get(self, "unknownExtendedKeyUsagesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: Required. The parts of an OID path. The most significant parts of the path come first. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''Required. The parts of an OID path. The most significant parts of the path come first.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalExtensions")
    def put_additional_extensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference.put_additional_extensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalExtensions", [value]))

    @jsii.member(jsii_name="putCaOptions")
    def put_ca_options(
        self,
        *,
        is_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param is_ca: Optional. Refers to the "CA" X.509 extension, which is a boolean value. When this value is missing, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#is_ca GooglePrivatecaCertificateTemplate#is_ca}
        :param max_issuer_path_length: Optional. Refers to the path length restriction X.509 extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. If this value is missing, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#max_issuer_path_length GooglePrivatecaCertificateTemplate#max_issuer_path_length}
        '''
        value = GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions(
            is_ca=is_ca, max_issuer_path_length=max_issuer_path_length
        )

        return typing.cast(None, jsii.invoke(self, "putCaOptions", [value]))

    @jsii.member(jsii_name="putKeyUsage")
    def put_key_usage(
        self,
        *,
        base_key_usage: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage, typing.Dict[str, typing.Any]]] = None,
        extended_key_usage: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage, typing.Dict[str, typing.Any]]] = None,
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#base_key_usage GooglePrivatecaCertificateTemplate#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#extended_key_usage GooglePrivatecaCertificateTemplate#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#unknown_extended_key_usages GooglePrivatecaCertificateTemplate#unknown_extended_key_usages}
        '''
        value = GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage(
            base_key_usage=base_key_usage,
            extended_key_usage=extended_key_usage,
            unknown_extended_key_usages=unknown_extended_key_usages,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyUsage", [value]))

    @jsii.member(jsii_name="putPolicyIds")
    def put_policy_ids(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference.put_policy_ids)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicyIds", [value]))

    @jsii.member(jsii_name="resetAdditionalExtensions")
    def reset_additional_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalExtensions", []))

    @jsii.member(jsii_name="resetAiaOcspServers")
    def reset_aia_ocsp_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAiaOcspServers", []))

    @jsii.member(jsii_name="resetCaOptions")
    def reset_ca_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaOptions", []))

    @jsii.member(jsii_name="resetKeyUsage")
    def reset_key_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyUsage", []))

    @jsii.member(jsii_name="resetPolicyIds")
    def reset_policy_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyIds", []))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList:
        return typing.cast(GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="caOptions")
    def ca_options(
        self,
    ) -> GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference:
        return typing.cast(GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference, jsii.get(self, "caOptions"))

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(
        self,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList":
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList", jsii.get(self, "policyIds"))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensionsInput")
    def additional_extensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions]]], jsii.get(self, "additionalExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServersInput")
    def aia_ocsp_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aiaOcspServersInput"))

    @builtins.property
    @jsii.member(jsii_name="caOptionsInput")
    def ca_options_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions], jsii.get(self, "caOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUsageInput")
    def key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage], jsii.get(self, "keyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdsInput")
    def policy_ids_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds"]]], jsii.get(self, "policyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServers")
    def aia_ocsp_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaOcspServers"))

    @aia_ocsp_servers.setter
    def aia_ocsp_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference, "aia_ocsp_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiaOcspServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValues]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateTemplatePredefinedValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: Required. The parts of an OID path. The most significant parts of the path come first. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''Required. The parts of an OID path. The most significant parts of the path come first.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#object_id_path GooglePrivatecaCertificateTemplate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePrivatecaCertificateTemplateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#create GooglePrivatecaCertificateTemplate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#delete GooglePrivatecaCertificateTemplate#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#update GooglePrivatecaCertificateTemplate#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#create GooglePrivatecaCertificateTemplate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#delete GooglePrivatecaCertificateTemplate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_template#update GooglePrivatecaCertificateTemplate#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTemplateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTemplateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateTemplate.GooglePrivatecaCertificateTemplateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTemplateTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateTemplateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateTemplateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateTemplateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTemplateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePrivatecaCertificateTemplate",
    "GooglePrivatecaCertificateTemplateConfig",
    "GooglePrivatecaCertificateTemplateIdentityConstraints",
    "GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpression",
    "GooglePrivatecaCertificateTemplateIdentityConstraintsCelExpressionOutputReference",
    "GooglePrivatecaCertificateTemplateIdentityConstraintsOutputReference",
    "GooglePrivatecaCertificateTemplatePassthroughExtensions",
    "GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensions",
    "GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsList",
    "GooglePrivatecaCertificateTemplatePassthroughExtensionsAdditionalExtensionsOutputReference",
    "GooglePrivatecaCertificateTemplatePassthroughExtensionsOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValues",
    "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensions",
    "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsList",
    "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectId",
    "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsObjectIdOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesAdditionalExtensionsOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesCaOptions",
    "GooglePrivatecaCertificateTemplatePredefinedValuesCaOptionsOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsage",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsage",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageBaseKeyUsageOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsage",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageExtendedKeyUsageOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsages",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesList",
    "GooglePrivatecaCertificateTemplatePredefinedValuesKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesOutputReference",
    "GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIds",
    "GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsList",
    "GooglePrivatecaCertificateTemplatePredefinedValuesPolicyIdsOutputReference",
    "GooglePrivatecaCertificateTemplateTimeouts",
    "GooglePrivatecaCertificateTemplateTimeoutsOutputReference",
]

publication.publish()
