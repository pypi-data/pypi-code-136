'''
# `data_google_privateca_certificate_authority`

Refer to the Terraform Registory for docs: [`data_google_privateca_certificate_authority`](https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority).
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


class DataGooglePrivatecaCertificateAuthority(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthority",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority google_privateca_certificate_authority}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        certificate_authority_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        pool: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority google_privateca_certificate_authority} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_authority_id: The user provided Resource ID for this Certificate Authority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#certificate_authority_id DataGooglePrivatecaCertificateAuthority#certificate_authority_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#id DataGooglePrivatecaCertificateAuthority#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Location of the CertificateAuthority. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#location DataGooglePrivatecaCertificateAuthority#location}
        :param pool: The name of the CaPool this Certificate Authority belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#pool DataGooglePrivatecaCertificateAuthority#pool}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#project DataGooglePrivatecaCertificateAuthority#project}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthority.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGooglePrivatecaCertificateAuthorityConfig(
            certificate_authority_id=certificate_authority_id,
            id=id,
            location=location,
            pool=pool,
            project=project,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCertificateAuthorityId")
    def reset_certificate_authority_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateAuthorityId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetPool")
    def reset_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPool", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessUrls")
    def access_urls(self) -> "DataGooglePrivatecaCertificateAuthorityAccessUrlsList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityAccessUrlsList", jsii.get(self, "accessUrls"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "DataGooglePrivatecaCertificateAuthorityConfigAList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigAList", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "deletionProtection"))

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @builtins.property
    @jsii.member(jsii_name="gcsBucket")
    def gcs_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcsBucket"))

    @builtins.property
    @jsii.member(jsii_name="ignoreActiveCertificatesOnDeletion")
    def ignore_active_certificates_on_deletion(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "ignoreActiveCertificatesOnDeletion"))

    @builtins.property
    @jsii.member(jsii_name="keySpec")
    def key_spec(self) -> "DataGooglePrivatecaCertificateAuthorityKeySpecList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityKeySpecList", jsii.get(self, "keySpec"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifetime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="pemCaCertificate")
    def pem_ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemCaCertificate"))

    @builtins.property
    @jsii.member(jsii_name="pemCaCertificates")
    def pem_ca_certificates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemCaCertificates"))

    @builtins.property
    @jsii.member(jsii_name="pemCsr")
    def pem_csr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemCsr"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="subordinateConfig")
    def subordinate_config(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthoritySubordinateConfigList":
        return typing.cast("DataGooglePrivatecaCertificateAuthoritySubordinateConfigList", jsii.get(self, "subordinateConfig"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityIdInput")
    def certificate_authority_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="poolInput")
    def pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityId")
    def certificate_authority_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityId"))

    @certificate_authority_id.setter
    def certificate_authority_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthority, "certificate_authority_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthority, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthority, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="pool")
    def pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pool"))

    @pool.setter
    def pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthority, "pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pool", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthority, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityAccessUrls",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityAccessUrls:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityAccessUrls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityAccessUrlsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityAccessUrlsList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityAccessUrlsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityAccessUrlsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityAccessUrlsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityAccessUrlsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityAccessUrlsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="caCertificateAccessUrl")
    def ca_certificate_access_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCertificateAccessUrl"))

    @builtins.property
    @jsii.member(jsii_name="crlAccessUrls")
    def crl_access_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "crlAccessUrls"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityAccessUrls]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityAccessUrls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityAccessUrls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_authority_id": "certificateAuthorityId",
        "id": "id",
        "location": "location",
        "pool": "pool",
        "project": "project",
    },
)
class DataGooglePrivatecaCertificateAuthorityConfig(cdktf.TerraformMetaArguments):
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
        certificate_authority_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        pool: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_authority_id: The user provided Resource ID for this Certificate Authority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#certificate_authority_id DataGooglePrivatecaCertificateAuthority#certificate_authority_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#id DataGooglePrivatecaCertificateAuthority#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Location of the CertificateAuthority. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#location DataGooglePrivatecaCertificateAuthority#location}
        :param pool: The name of the CaPool this Certificate Authority belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#pool DataGooglePrivatecaCertificateAuthority#pool}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#project DataGooglePrivatecaCertificateAuthority#project}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_authority_id", value=certificate_authority_id, expected_type=type_hints["certificate_authority_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument pool", value=pool, expected_type=type_hints["pool"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if certificate_authority_id is not None:
            self._values["certificate_authority_id"] = certificate_authority_id
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if pool is not None:
            self._values["pool"] = pool
        if project is not None:
            self._values["project"] = project

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
    def certificate_authority_id(self) -> typing.Optional[builtins.str]:
        '''The user provided Resource ID for this Certificate Authority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#certificate_authority_id DataGooglePrivatecaCertificateAuthority#certificate_authority_id}
        '''
        result = self._values.get("certificate_authority_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#id DataGooglePrivatecaCertificateAuthority#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Location of the CertificateAuthority. A full list of valid locations can be found by running 'gcloud privateca locations list'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#location DataGooglePrivatecaCertificateAuthority#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pool(self) -> typing.Optional[builtins.str]:
        '''The name of the CaPool this Certificate Authority belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#pool DataGooglePrivatecaCertificateAuthority#pool}
        '''
        result = self._values.get("pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_privateca_certificate_authority#project DataGooglePrivatecaCertificateAuthority#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigA",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigA:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigAList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigAList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigAList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigAOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigAList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigAOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigAList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigAList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigAList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigAOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="subjectConfig")
    def subject_config(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList", jsii.get(self, "subjectConfig"))

    @builtins.property
    @jsii.member(jsii_name="x509Config")
    def x509_config(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList", jsii.get(self, "x509Config"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigA]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList", jsii.get(self, "subjectAltName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dnsNames")
    def dns_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsNames"))

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @builtins.property
    @jsii.member(jsii_name="locality")
    def locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locality"))

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @builtins.property
    @jsii.member(jsii_name="province")
    def province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "province"))

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streetAddress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509Config",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509Config:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="objectIdPath")
    def object_id_path(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "objectIdPath"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "critical"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(
        self,
    ) -> DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList:
        return typing.cast(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="isCa")
    def is_ca(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isCa"))

    @builtins.property
    @jsii.member(jsii_name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIssuerPathLength"))

    @builtins.property
    @jsii.member(jsii_name="nonCa")
    def non_ca(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "nonCa"))

    @builtins.property
    @jsii.member(jsii_name="zeroMaxIssuerPathLength")
    def zero_max_issuer_path_length(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "zeroMaxIssuerPathLength"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="certSign")
    def cert_sign(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "certSign"))

    @builtins.property
    @jsii.member(jsii_name="contentCommitment")
    def content_commitment(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "contentCommitment"))

    @builtins.property
    @jsii.member(jsii_name="crlSign")
    def crl_sign(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "crlSign"))

    @builtins.property
    @jsii.member(jsii_name="dataEncipherment")
    def data_encipherment(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "dataEncipherment"))

    @builtins.property
    @jsii.member(jsii_name="decipherOnly")
    def decipher_only(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "decipherOnly"))

    @builtins.property
    @jsii.member(jsii_name="digitalSignature")
    def digital_signature(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "digitalSignature"))

    @builtins.property
    @jsii.member(jsii_name="encipherOnly")
    def encipher_only(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "encipherOnly"))

    @builtins.property
    @jsii.member(jsii_name="keyAgreement")
    def key_agreement(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "keyAgreement"))

    @builtins.property
    @jsii.member(jsii_name="keyEncipherment")
    def key_encipherment(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "keyEncipherment"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="clientAuth")
    def client_auth(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "clientAuth"))

    @builtins.property
    @jsii.member(jsii_name="codeSigning")
    def code_signing(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "codeSigning"))

    @builtins.property
    @jsii.member(jsii_name="emailProtection")
    def email_protection(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "emailProtection"))

    @builtins.property
    @jsii.member(jsii_name="ocspSigning")
    def ocsp_signing(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "ocspSigning"))

    @builtins.property
    @jsii.member(jsii_name="serverAuth")
    def server_auth(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "serverAuth"))

    @builtins.property
    @jsii.member(jsii_name="timeStamping")
    def time_stamping(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "timeStamping"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList:
        return typing.cast(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList:
        return typing.cast(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="objectIdPath")
    def object_id_path(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "objectIdPath"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList:
        return typing.cast(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServers")
    def aia_ocsp_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaOcspServers"))

    @builtins.property
    @jsii.member(jsii_name="caOptions")
    def ca_options(
        self,
    ) -> DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList:
        return typing.cast(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList, jsii.get(self, "caOptions"))

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList:
        return typing.cast(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList":
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList", jsii.get(self, "policyIds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509Config]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509Config], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509Config],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="objectIdPath")
    def object_id_path(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "objectIdPath"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityKeySpec",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthorityKeySpec:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthorityKeySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthorityKeySpecList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityKeySpecList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityKeySpecList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityKeySpecList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityKeySpecList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityKeySpecList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityKeySpecList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @builtins.property
    @jsii.member(jsii_name="cloudKmsKeyVersion")
    def cloud_kms_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudKmsKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthorityKeySpec]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthorityKeySpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthorityKeySpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthoritySubordinateConfig",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthoritySubordinateConfig:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthoritySubordinateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthoritySubordinateConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthoritySubordinateConfigList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthoritySubordinateConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthoritySubordinateConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="certificateAuthority")
    def certificate_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthority"))

    @builtins.property
    @jsii.member(jsii_name="pemIssuerChain")
    def pem_issuer_chain(
        self,
    ) -> "DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList":
        return typing.cast("DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList", jsii.get(self, "pemIssuerChain"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthoritySubordinateConfig]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthoritySubordinateConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthoritySubordinateConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGooglePrivatecaCertificateAuthority.DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference",
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
            type_hints = typing.get_type_hints(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="pemCertificates")
    def pem_certificates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemCertificates"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain]:
        return typing.cast(typing.Optional[DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGooglePrivatecaCertificateAuthority",
    "DataGooglePrivatecaCertificateAuthorityAccessUrls",
    "DataGooglePrivatecaCertificateAuthorityAccessUrlsList",
    "DataGooglePrivatecaCertificateAuthorityAccessUrlsOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfig",
    "DataGooglePrivatecaCertificateAuthorityConfigA",
    "DataGooglePrivatecaCertificateAuthorityConfigAList",
    "DataGooglePrivatecaCertificateAuthorityConfigAOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfig",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigList",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameList",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectList",
    "DataGooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509Config",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList",
    "DataGooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference",
    "DataGooglePrivatecaCertificateAuthorityKeySpec",
    "DataGooglePrivatecaCertificateAuthorityKeySpecList",
    "DataGooglePrivatecaCertificateAuthorityKeySpecOutputReference",
    "DataGooglePrivatecaCertificateAuthoritySubordinateConfig",
    "DataGooglePrivatecaCertificateAuthoritySubordinateConfigList",
    "DataGooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference",
    "DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain",
    "DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainList",
    "DataGooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference",
]

publication.publish()
