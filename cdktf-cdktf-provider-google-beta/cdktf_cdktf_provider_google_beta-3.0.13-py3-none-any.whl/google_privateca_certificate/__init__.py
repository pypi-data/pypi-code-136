'''
# `google_privateca_certificate`

Refer to the Terraform Registory for docs: [`google_privateca_certificate`](https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate).
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


class GooglePrivatecaCertificate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate google_privateca_certificate}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        pool: builtins.str,
        certificate_authority: typing.Optional[builtins.str] = None,
        certificate_template: typing.Optional[builtins.str] = None,
        config: typing.Optional[typing.Union["GooglePrivatecaCertificateConfigA", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lifetime: typing.Optional[builtins.str] = None,
        pem_csr: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate google_privateca_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Location of the Certificate. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#location GooglePrivatecaCertificate#location}
        :param name: The name for this Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#name GooglePrivatecaCertificate#name}
        :param pool: The name of the CaPool this Certificate belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#pool GooglePrivatecaCertificate#pool}
        :param certificate_authority: The Certificate Authority ID that should issue the certificate. For example, to issue a Certificate from a Certificate Authority with resource name 'projects/my-project/locations/us-central1/caPools/my-pool/certificateAuthorities/my-ca', argument 'pool' should be set to 'projects/my-project/locations/us-central1/caPools/my-pool', argument 'certificate_authority' should be set to 'my-ca'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#certificate_authority GooglePrivatecaCertificate#certificate_authority}
        :param certificate_template: The resource name for a CertificateTemplate used to issue this certificate, in the format 'projects/*/locations/*/certificateTemplates/*'. If this is specified, the caller must have the necessary permission to use this template. If this is omitted, no template will be used. This template must be in the same location as the Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#certificate_template GooglePrivatecaCertificate#certificate_template}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#config GooglePrivatecaCertificate#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#id GooglePrivatecaCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels with user-defined metadata to apply to this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#labels GooglePrivatecaCertificate#labels}
        :param lifetime: The desired lifetime of the CA certificate. Used to create the "notBeforeTime" and "notAfterTime" fields inside an X.509 certificate. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#lifetime GooglePrivatecaCertificate#lifetime}
        :param pem_csr: Immutable. A pem-encoded X.509 certificate signing request (CSR). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#pem_csr GooglePrivatecaCertificate#pem_csr}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#project GooglePrivatecaCertificate#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#timeouts GooglePrivatecaCertificate#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = GooglePrivatecaCertificateConfig(
            location=location,
            name=name,
            pool=pool,
            certificate_authority=certificate_authority,
            certificate_template=certificate_template,
            config=config,
            id=id,
            labels=labels,
            lifetime=lifetime,
            pem_csr=pem_csr,
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

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        public_key: typing.Union["GooglePrivatecaCertificateConfigPublicKey", typing.Dict[str, typing.Any]],
        subject_config: typing.Union["GooglePrivatecaCertificateConfigSubjectConfig", typing.Dict[str, typing.Any]],
        x509_config: typing.Union["GooglePrivatecaCertificateConfigX509Config", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param public_key: public_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#public_key GooglePrivatecaCertificate#public_key}
        :param subject_config: subject_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject_config GooglePrivatecaCertificate#subject_config}
        :param x509_config: x509_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#x509_config GooglePrivatecaCertificate#x509_config}
        '''
        value = GooglePrivatecaCertificateConfigA(
            public_key=public_key,
            subject_config=subject_config,
            x509_config=x509_config,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#create GooglePrivatecaCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#delete GooglePrivatecaCertificate#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#update GooglePrivatecaCertificate#update}.
        '''
        value = GooglePrivatecaCertificateTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificateAuthority")
    def reset_certificate_authority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateAuthority", []))

    @jsii.member(jsii_name="resetCertificateTemplate")
    def reset_certificate_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateTemplate", []))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLifetime")
    def reset_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetime", []))

    @jsii.member(jsii_name="resetPemCsr")
    def reset_pem_csr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemCsr", []))

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
    @jsii.member(jsii_name="certificateDescription")
    def certificate_description(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionList", jsii.get(self, "certificateDescription"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "GooglePrivatecaCertificateConfigAOutputReference":
        return typing.cast("GooglePrivatecaCertificateConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="issuerCertificateAuthority")
    def issuer_certificate_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuerCertificateAuthority"))

    @builtins.property
    @jsii.member(jsii_name="pemCertificate")
    def pem_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemCertificate"))

    @builtins.property
    @jsii.member(jsii_name="pemCertificateChain")
    def pem_certificate_chain(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemCertificateChain"))

    @builtins.property
    @jsii.member(jsii_name="pemCertificates")
    def pem_certificates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemCertificates"))

    @builtins.property
    @jsii.member(jsii_name="revocationDetails")
    def revocation_details(self) -> "GooglePrivatecaCertificateRevocationDetailsList":
        return typing.cast("GooglePrivatecaCertificateRevocationDetailsList", jsii.get(self, "revocationDetails"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePrivatecaCertificateTimeoutsOutputReference":
        return typing.cast("GooglePrivatecaCertificateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityInput")
    def certificate_authority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateTemplateInput")
    def certificate_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["GooglePrivatecaCertificateConfigA"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigA"], jsii.get(self, "configInput"))

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
    @jsii.member(jsii_name="lifetimeInput")
    def lifetime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pemCsrInput")
    def pem_csr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemCsrInput"))

    @builtins.property
    @jsii.member(jsii_name="poolInput")
    def pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePrivatecaCertificateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePrivatecaCertificateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthority")
    def certificate_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthority"))

    @certificate_authority.setter
    def certificate_authority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "certificate_authority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthority", value)

    @builtins.property
    @jsii.member(jsii_name="certificateTemplate")
    def certificate_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateTemplate"))

    @certificate_template.setter
    def certificate_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "certificate_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifetime"))

    @lifetime.setter
    def lifetime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetime", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pemCsr")
    def pem_csr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemCsr"))

    @pem_csr.setter
    def pem_csr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "pem_csr").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemCsr", value)

    @builtins.property
    @jsii.member(jsii_name="pool")
    def pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pool"))

    @pool.setter
    def pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pool", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificate, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescription",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescription:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionCertFingerprint",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionCertFingerprint:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionCertFingerprint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="sha256Hash")
    def sha256_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha256Hash"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionCertFingerprint]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionCertFingerprint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionCertFingerprint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValues",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValues:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyUsageOptions")
    def key_usage_options(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList, jsii.get(self, "keyUsageOptions"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="obectId")
    def obect_id(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList, jsii.get(self, "obectId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValues]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionConfigValues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="aiaIssuingCertificateUrls")
    def aia_issuing_certificate_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaIssuingCertificateUrls"))

    @builtins.property
    @jsii.member(jsii_name="authorityKeyId")
    def authority_key_id(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList, jsii.get(self, "authorityKeyId"))

    @builtins.property
    @jsii.member(jsii_name="certFingerprint")
    def cert_fingerprint(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList, jsii.get(self, "certFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="configValues")
    def config_values(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionConfigValuesList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionConfigValuesList, jsii.get(self, "configValues"))

    @builtins.property
    @jsii.member(jsii_name="crlDistributionPoints")
    def crl_distribution_points(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "crlDistributionPoints"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionPublicKeyList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionPublicKeyList", jsii.get(self, "publicKey"))

    @builtins.property
    @jsii.member(jsii_name="subjectDescription")
    def subject_description(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList", jsii.get(self, "subjectDescription"))

    @builtins.property
    @jsii.member(jsii_name="subjectKeyId")
    def subject_key_id(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList", jsii.get(self, "subjectKeyId"))

    @builtins.property
    @jsii.member(jsii_name="x509Description")
    def x509_description(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList", jsii.get(self, "x509Description"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescription]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescription], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescription],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionPublicKey",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionPublicKey:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionPublicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionPublicKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionPublicKeyList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionPublicKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionPublicKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionPublicKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionPublicKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionPublicKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionPublicKey]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionPublicKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionPublicKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescription",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionSubjectDescription:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionSubjectDescription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hexSerialNumber")
    def hex_serial_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hexSerialNumber"))

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifetime"))

    @builtins.property
    @jsii.member(jsii_name="notAfterTime")
    def not_after_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notAfterTime"))

    @builtins.property
    @jsii.member(jsii_name="notBeforeTime")
    def not_before_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notBeforeTime"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList", jsii.get(self, "subjectAltName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescription]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescription], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescription],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference.__init__)
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
    @jsii.member(jsii_name="obectId")
    def obect_id(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList, jsii.get(self, "obectId"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="customSans")
    def custom_sans(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList, jsii.get(self, "customSans"))

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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509Description",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509Description:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509Description(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference.__init__)
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
    ) -> GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference.__init__)
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
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServers")
    def aia_ocsp_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaOcspServers"))

    @builtins.property
    @jsii.member(jsii_name="caOptions")
    def ca_options(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList, jsii.get(self, "caOptions"))

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList:
        return typing.cast(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(
        self,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList":
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList", jsii.get(self, "policyIds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509Description]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509Description], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509Description],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfig",
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
        "pool": "pool",
        "certificate_authority": "certificateAuthority",
        "certificate_template": "certificateTemplate",
        "config": "config",
        "id": "id",
        "labels": "labels",
        "lifetime": "lifetime",
        "pem_csr": "pemCsr",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GooglePrivatecaCertificateConfig(cdktf.TerraformMetaArguments):
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
        pool: builtins.str,
        certificate_authority: typing.Optional[builtins.str] = None,
        certificate_template: typing.Optional[builtins.str] = None,
        config: typing.Optional[typing.Union["GooglePrivatecaCertificateConfigA", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lifetime: typing.Optional[builtins.str] = None,
        pem_csr: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Location of the Certificate. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#location GooglePrivatecaCertificate#location}
        :param name: The name for this Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#name GooglePrivatecaCertificate#name}
        :param pool: The name of the CaPool this Certificate belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#pool GooglePrivatecaCertificate#pool}
        :param certificate_authority: The Certificate Authority ID that should issue the certificate. For example, to issue a Certificate from a Certificate Authority with resource name 'projects/my-project/locations/us-central1/caPools/my-pool/certificateAuthorities/my-ca', argument 'pool' should be set to 'projects/my-project/locations/us-central1/caPools/my-pool', argument 'certificate_authority' should be set to 'my-ca'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#certificate_authority GooglePrivatecaCertificate#certificate_authority}
        :param certificate_template: The resource name for a CertificateTemplate used to issue this certificate, in the format 'projects/*/locations/*/certificateTemplates/*'. If this is specified, the caller must have the necessary permission to use this template. If this is omitted, no template will be used. This template must be in the same location as the Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#certificate_template GooglePrivatecaCertificate#certificate_template}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#config GooglePrivatecaCertificate#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#id GooglePrivatecaCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels with user-defined metadata to apply to this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#labels GooglePrivatecaCertificate#labels}
        :param lifetime: The desired lifetime of the CA certificate. Used to create the "notBeforeTime" and "notAfterTime" fields inside an X.509 certificate. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#lifetime GooglePrivatecaCertificate#lifetime}
        :param pem_csr: Immutable. A pem-encoded X.509 certificate signing request (CSR). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#pem_csr GooglePrivatecaCertificate#pem_csr}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#project GooglePrivatecaCertificate#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#timeouts GooglePrivatecaCertificate#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = GooglePrivatecaCertificateConfigA(**config)
        if isinstance(timeouts, dict):
            timeouts = GooglePrivatecaCertificateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pool", value=pool, expected_type=type_hints["pool"])
            check_type(argname="argument certificate_authority", value=certificate_authority, expected_type=type_hints["certificate_authority"])
            check_type(argname="argument certificate_template", value=certificate_template, expected_type=type_hints["certificate_template"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument lifetime", value=lifetime, expected_type=type_hints["lifetime"])
            check_type(argname="argument pem_csr", value=pem_csr, expected_type=type_hints["pem_csr"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "pool": pool,
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
        if certificate_authority is not None:
            self._values["certificate_authority"] = certificate_authority
        if certificate_template is not None:
            self._values["certificate_template"] = certificate_template
        if config is not None:
            self._values["config"] = config
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if lifetime is not None:
            self._values["lifetime"] = lifetime
        if pem_csr is not None:
            self._values["pem_csr"] = pem_csr
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
        '''Location of the Certificate. A full list of valid locations can be found by running 'gcloud privateca locations list'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#location GooglePrivatecaCertificate#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for this Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#name GooglePrivatecaCertificate#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool(self) -> builtins.str:
        '''The name of the CaPool this Certificate belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#pool GooglePrivatecaCertificate#pool}
        '''
        result = self._values.get("pool")
        assert result is not None, "Required property 'pool' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_authority(self) -> typing.Optional[builtins.str]:
        '''The Certificate Authority ID that should issue the certificate.

        For example, to issue a Certificate from
        a Certificate Authority with resource name 'projects/my-project/locations/us-central1/caPools/my-pool/certificateAuthorities/my-ca',
        argument 'pool' should be set to 'projects/my-project/locations/us-central1/caPools/my-pool', argument 'certificate_authority'
        should be set to 'my-ca'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#certificate_authority GooglePrivatecaCertificate#certificate_authority}
        '''
        result = self._values.get("certificate_authority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_template(self) -> typing.Optional[builtins.str]:
        '''The resource name for a CertificateTemplate used to issue this certificate, in the format 'projects/*/locations/*/certificateTemplates/*'.

        If this is specified,
        the caller must have the necessary permission to use this template. If this is
        omitted, no template will be used. This template must be in the same location
        as the Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#certificate_template GooglePrivatecaCertificate#certificate_template}
        '''
        result = self._values.get("certificate_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def config(self) -> typing.Optional["GooglePrivatecaCertificateConfigA"]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#config GooglePrivatecaCertificate#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigA"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#id GooglePrivatecaCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels with user-defined metadata to apply to this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#labels GooglePrivatecaCertificate#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def lifetime(self) -> typing.Optional[builtins.str]:
        '''The desired lifetime of the CA certificate.

        Used to create the "notBeforeTime" and
        "notAfterTime" fields inside an X.509 certificate. A duration in seconds with up to nine
        fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#lifetime GooglePrivatecaCertificate#lifetime}
        '''
        result = self._values.get("lifetime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_csr(self) -> typing.Optional[builtins.str]:
        '''Immutable. A pem-encoded X.509 certificate signing request (CSR).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#pem_csr GooglePrivatecaCertificate#pem_csr}
        '''
        result = self._values.get("pem_csr")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#project GooglePrivatecaCertificate#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GooglePrivatecaCertificateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#timeouts GooglePrivatecaCertificate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "public_key": "publicKey",
        "subject_config": "subjectConfig",
        "x509_config": "x509Config",
    },
)
class GooglePrivatecaCertificateConfigA:
    def __init__(
        self,
        *,
        public_key: typing.Union["GooglePrivatecaCertificateConfigPublicKey", typing.Dict[str, typing.Any]],
        subject_config: typing.Union["GooglePrivatecaCertificateConfigSubjectConfig", typing.Dict[str, typing.Any]],
        x509_config: typing.Union["GooglePrivatecaCertificateConfigX509Config", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param public_key: public_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#public_key GooglePrivatecaCertificate#public_key}
        :param subject_config: subject_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject_config GooglePrivatecaCertificate#subject_config}
        :param x509_config: x509_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#x509_config GooglePrivatecaCertificate#x509_config}
        '''
        if isinstance(public_key, dict):
            public_key = GooglePrivatecaCertificateConfigPublicKey(**public_key)
        if isinstance(subject_config, dict):
            subject_config = GooglePrivatecaCertificateConfigSubjectConfig(**subject_config)
        if isinstance(x509_config, dict):
            x509_config = GooglePrivatecaCertificateConfigX509Config(**x509_config)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigA.__init__)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument subject_config", value=subject_config, expected_type=type_hints["subject_config"])
            check_type(argname="argument x509_config", value=x509_config, expected_type=type_hints["x509_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "public_key": public_key,
            "subject_config": subject_config,
            "x509_config": x509_config,
        }

    @builtins.property
    def public_key(self) -> "GooglePrivatecaCertificateConfigPublicKey":
        '''public_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#public_key GooglePrivatecaCertificate#public_key}
        '''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigPublicKey", result)

    @builtins.property
    def subject_config(self) -> "GooglePrivatecaCertificateConfigSubjectConfig":
        '''subject_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject_config GooglePrivatecaCertificate#subject_config}
        '''
        result = self._values.get("subject_config")
        assert result is not None, "Required property 'subject_config' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigSubjectConfig", result)

    @builtins.property
    def x509_config(self) -> "GooglePrivatecaCertificateConfigX509Config":
        '''x509_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#x509_config GooglePrivatecaCertificate#x509_config}
        '''
        result = self._values.get("x509_config")
        assert result is not None, "Required property 'x509_config' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigX509Config", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigAOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPublicKey")
    def put_public_key(
        self,
        *,
        format: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param format: The format of the public key. Currently, only PEM format is supported. Possible values: ["KEY_TYPE_UNSPECIFIED", "PEM"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#format GooglePrivatecaCertificate#format}
        :param key: Required. A public key. When this is specified in a request, the padding and encoding can be any of the options described by the respective 'KeyType' value. When this is generated by the service, it will always be an RFC 5280 SubjectPublicKeyInfo structure containing an algorithm identifier and a key. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key GooglePrivatecaCertificate#key}
        '''
        value = GooglePrivatecaCertificateConfigPublicKey(format=format, key=key)

        return typing.cast(None, jsii.invoke(self, "putPublicKey", [value]))

    @jsii.member(jsii_name="putSubjectConfig")
    def put_subject_config(
        self,
        *,
        subject: typing.Union["GooglePrivatecaCertificateConfigSubjectConfigSubject", typing.Dict[str, typing.Any]],
        subject_alt_name: typing.Optional[typing.Union["GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject GooglePrivatecaCertificate#subject}
        :param subject_alt_name: subject_alt_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject_alt_name GooglePrivatecaCertificate#subject_alt_name}
        '''
        value = GooglePrivatecaCertificateConfigSubjectConfig(
            subject=subject, subject_alt_name=subject_alt_name
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectConfig", [value]))

    @jsii.member(jsii_name="putX509Config")
    def put_x509_config(
        self,
        *,
        key_usage: typing.Union["GooglePrivatecaCertificateConfigX509ConfigKeyUsage", typing.Dict[str, typing.Any]],
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ca_options: typing.Optional[typing.Union["GooglePrivatecaCertificateConfigX509ConfigCaOptions", typing.Dict[str, typing.Any]]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_usage GooglePrivatecaCertificate#key_usage}
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#additional_extensions GooglePrivatecaCertificate#additional_extensions}
        :param aia_ocsp_servers: Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#aia_ocsp_servers GooglePrivatecaCertificate#aia_ocsp_servers}
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ca_options GooglePrivatecaCertificate#ca_options}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#policy_ids GooglePrivatecaCertificate#policy_ids}
        '''
        value = GooglePrivatecaCertificateConfigX509Config(
            key_usage=key_usage,
            additional_extensions=additional_extensions,
            aia_ocsp_servers=aia_ocsp_servers,
            ca_options=ca_options,
            policy_ids=policy_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putX509Config", [value]))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> "GooglePrivatecaCertificateConfigPublicKeyOutputReference":
        return typing.cast("GooglePrivatecaCertificateConfigPublicKeyOutputReference", jsii.get(self, "publicKey"))

    @builtins.property
    @jsii.member(jsii_name="subjectConfig")
    def subject_config(
        self,
    ) -> "GooglePrivatecaCertificateConfigSubjectConfigOutputReference":
        return typing.cast("GooglePrivatecaCertificateConfigSubjectConfigOutputReference", jsii.get(self, "subjectConfig"))

    @builtins.property
    @jsii.member(jsii_name="x509Config")
    def x509_config(
        self,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigOutputReference":
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigOutputReference", jsii.get(self, "x509Config"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigPublicKey"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigPublicKey"], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectConfigInput")
    def subject_config_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigSubjectConfig"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigSubjectConfig"], jsii.get(self, "subjectConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="x509ConfigInput")
    def x509_config_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigX509Config"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigX509Config"], jsii.get(self, "x509ConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GooglePrivatecaCertificateConfigA]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigPublicKey",
    jsii_struct_bases=[],
    name_mapping={"format": "format", "key": "key"},
)
class GooglePrivatecaCertificateConfigPublicKey:
    def __init__(
        self,
        *,
        format: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param format: The format of the public key. Currently, only PEM format is supported. Possible values: ["KEY_TYPE_UNSPECIFIED", "PEM"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#format GooglePrivatecaCertificate#format}
        :param key: Required. A public key. When this is specified in a request, the padding and encoding can be any of the options described by the respective 'KeyType' value. When this is generated by the service, it will always be an RFC 5280 SubjectPublicKeyInfo structure containing an algorithm identifier and a key. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key GooglePrivatecaCertificate#key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigPublicKey.__init__)
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[str, typing.Any] = {
            "format": format,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def format(self) -> builtins.str:
        '''The format of the public key. Currently, only PEM format is supported. Possible values: ["KEY_TYPE_UNSPECIFIED", "PEM"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#format GooglePrivatecaCertificate#format}
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Required.

        A public key. When this is specified in a request, the padding and encoding can be any of the options described by the respective 'KeyType' value. When this is generated by the service, it will always be an RFC 5280 SubjectPublicKeyInfo structure containing an algorithm identifier and a key. A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key GooglePrivatecaCertificate#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigPublicKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigPublicKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigPublicKeyOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigPublicKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigPublicKeyOutputReference, "format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigPublicKeyOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigPublicKey]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigPublicKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigPublicKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigPublicKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigSubjectConfig",
    jsii_struct_bases=[],
    name_mapping={"subject": "subject", "subject_alt_name": "subjectAltName"},
)
class GooglePrivatecaCertificateConfigSubjectConfig:
    def __init__(
        self,
        *,
        subject: typing.Union["GooglePrivatecaCertificateConfigSubjectConfigSubject", typing.Dict[str, typing.Any]],
        subject_alt_name: typing.Optional[typing.Union["GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject GooglePrivatecaCertificate#subject}
        :param subject_alt_name: subject_alt_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject_alt_name GooglePrivatecaCertificate#subject_alt_name}
        '''
        if isinstance(subject, dict):
            subject = GooglePrivatecaCertificateConfigSubjectConfigSubject(**subject)
        if isinstance(subject_alt_name, dict):
            subject_alt_name = GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName(**subject_alt_name)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigSubjectConfig.__init__)
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument subject_alt_name", value=subject_alt_name, expected_type=type_hints["subject_alt_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "subject": subject,
        }
        if subject_alt_name is not None:
            self._values["subject_alt_name"] = subject_alt_name

    @builtins.property
    def subject(self) -> "GooglePrivatecaCertificateConfigSubjectConfigSubject":
        '''subject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject GooglePrivatecaCertificate#subject}
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigSubjectConfigSubject", result)

    @builtins.property
    def subject_alt_name(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName"]:
        '''subject_alt_name block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#subject_alt_name GooglePrivatecaCertificate#subject_alt_name}
        '''
        result = self._values.get("subject_alt_name")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigSubjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigSubjectConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigSubjectConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigSubjectConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubject")
    def put_subject(
        self,
        *,
        common_name: builtins.str,
        organization: builtins.str,
        country_code: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        province: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_name: The common name of the distinguished name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#common_name GooglePrivatecaCertificate#common_name}
        :param organization: The organization of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#organization GooglePrivatecaCertificate#organization}
        :param country_code: The country code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#country_code GooglePrivatecaCertificate#country_code}
        :param locality: The locality or city of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#locality GooglePrivatecaCertificate#locality}
        :param organizational_unit: The organizational unit of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#organizational_unit GooglePrivatecaCertificate#organizational_unit}
        :param postal_code: The postal code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#postal_code GooglePrivatecaCertificate#postal_code}
        :param province: The province, territory, or regional state of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#province GooglePrivatecaCertificate#province}
        :param street_address: The street address of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#street_address GooglePrivatecaCertificate#street_address}
        '''
        value = GooglePrivatecaCertificateConfigSubjectConfigSubject(
            common_name=common_name,
            organization=organization,
            country_code=country_code,
            locality=locality,
            organizational_unit=organizational_unit,
            postal_code=postal_code,
            province=province,
            street_address=street_address,
        )

        return typing.cast(None, jsii.invoke(self, "putSubject", [value]))

    @jsii.member(jsii_name="putSubjectAltName")
    def put_subject_alt_name(
        self,
        *,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param dns_names: Contains only valid, fully-qualified host names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#dns_names GooglePrivatecaCertificate#dns_names}
        :param email_addresses: Contains only valid RFC 2822 E-mail addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#email_addresses GooglePrivatecaCertificate#email_addresses}
        :param ip_addresses: Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ip_addresses GooglePrivatecaCertificate#ip_addresses}
        :param uris: Contains only valid RFC 3986 URIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#uris GooglePrivatecaCertificate#uris}
        '''
        value = GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName(
            dns_names=dns_names,
            email_addresses=email_addresses,
            ip_addresses=ip_addresses,
            uris=uris,
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAltName", [value]))

    @jsii.member(jsii_name="resetSubjectAltName")
    def reset_subject_alt_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAltName", []))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(
        self,
    ) -> "GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference":
        return typing.cast("GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> "GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference":
        return typing.cast("GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference", jsii.get(self, "subjectAltName"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltNameInput")
    def subject_alt_name_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName"], jsii.get(self, "subjectAltNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigSubjectConfigSubject"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigSubjectConfigSubject"], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigSubjectConfig]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigSubjectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigSubjectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigSubjectConfigSubject",
    jsii_struct_bases=[],
    name_mapping={
        "common_name": "commonName",
        "organization": "organization",
        "country_code": "countryCode",
        "locality": "locality",
        "organizational_unit": "organizationalUnit",
        "postal_code": "postalCode",
        "province": "province",
        "street_address": "streetAddress",
    },
)
class GooglePrivatecaCertificateConfigSubjectConfigSubject:
    def __init__(
        self,
        *,
        common_name: builtins.str,
        organization: builtins.str,
        country_code: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        province: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param common_name: The common name of the distinguished name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#common_name GooglePrivatecaCertificate#common_name}
        :param organization: The organization of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#organization GooglePrivatecaCertificate#organization}
        :param country_code: The country code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#country_code GooglePrivatecaCertificate#country_code}
        :param locality: The locality or city of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#locality GooglePrivatecaCertificate#locality}
        :param organizational_unit: The organizational unit of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#organizational_unit GooglePrivatecaCertificate#organizational_unit}
        :param postal_code: The postal code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#postal_code GooglePrivatecaCertificate#postal_code}
        :param province: The province, territory, or regional state of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#province GooglePrivatecaCertificate#province}
        :param street_address: The street address of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#street_address GooglePrivatecaCertificate#street_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigSubjectConfigSubject.__init__)
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
            check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument province", value=province, expected_type=type_hints["province"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
        self._values: typing.Dict[str, typing.Any] = {
            "common_name": common_name,
            "organization": organization,
        }
        if country_code is not None:
            self._values["country_code"] = country_code
        if locality is not None:
            self._values["locality"] = locality
        if organizational_unit is not None:
            self._values["organizational_unit"] = organizational_unit
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if province is not None:
            self._values["province"] = province
        if street_address is not None:
            self._values["street_address"] = street_address

    @builtins.property
    def common_name(self) -> builtins.str:
        '''The common name of the distinguished name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#common_name GooglePrivatecaCertificate#common_name}
        '''
        result = self._values.get("common_name")
        assert result is not None, "Required property 'common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''The organization of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#organization GooglePrivatecaCertificate#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''The country code of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#country_code GooglePrivatecaCertificate#country_code}
        '''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''The locality or city of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#locality GooglePrivatecaCertificate#locality}
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''The organizational unit of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#organizational_unit GooglePrivatecaCertificate#organizational_unit}
        '''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''The postal code of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#postal_code GooglePrivatecaCertificate#postal_code}
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def province(self) -> typing.Optional[builtins.str]:
        '''The province, territory, or regional state of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#province GooglePrivatecaCertificate#province}
        '''
        result = self._values.get("province")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''The street address of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#street_address GooglePrivatecaCertificate#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigSubjectConfigSubject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName",
    jsii_struct_bases=[],
    name_mapping={
        "dns_names": "dnsNames",
        "email_addresses": "emailAddresses",
        "ip_addresses": "ipAddresses",
        "uris": "uris",
    },
)
class GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName:
    def __init__(
        self,
        *,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param dns_names: Contains only valid, fully-qualified host names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#dns_names GooglePrivatecaCertificate#dns_names}
        :param email_addresses: Contains only valid RFC 2822 E-mail addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#email_addresses GooglePrivatecaCertificate#email_addresses}
        :param ip_addresses: Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ip_addresses GooglePrivatecaCertificate#ip_addresses}
        :param uris: Contains only valid RFC 3986 URIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#uris GooglePrivatecaCertificate#uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName.__init__)
            check_type(argname="argument dns_names", value=dns_names, expected_type=type_hints["dns_names"])
            check_type(argname="argument email_addresses", value=email_addresses, expected_type=type_hints["email_addresses"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
            check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dns_names is not None:
            self._values["dns_names"] = dns_names
        if email_addresses is not None:
            self._values["email_addresses"] = email_addresses
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses
        if uris is not None:
            self._values["uris"] = uris

    @builtins.property
    def dns_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid, fully-qualified host names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#dns_names GooglePrivatecaCertificate#dns_names}
        '''
        result = self._values.get("dns_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid RFC 2822 E-mail addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#email_addresses GooglePrivatecaCertificate#email_addresses}
        '''
        result = self._values.get("email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ip_addresses GooglePrivatecaCertificate#ip_addresses}
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid RFC 3986 URIs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#uris GooglePrivatecaCertificate#uris}
        '''
        result = self._values.get("uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDnsNames")
    def reset_dns_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsNames", []))

    @jsii.member(jsii_name="resetEmailAddresses")
    def reset_email_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddresses", []))

    @jsii.member(jsii_name="resetIpAddresses")
    def reset_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddresses", []))

    @jsii.member(jsii_name="resetUris")
    def reset_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUris", []))

    @builtins.property
    @jsii.member(jsii_name="dnsNamesInput")
    def dns_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressesInput")
    def email_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressesInput")
    def ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="urisInput")
    def uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urisInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNames")
    def dns_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsNames"))

    @dns_names.setter
    def dns_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference, "dns_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsNames", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @email_addresses.setter
    def email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference, "email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference, "ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference, "uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCountryCode")
    def reset_country_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryCode", []))

    @jsii.member(jsii_name="resetLocality")
    def reset_locality(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocality", []))

    @jsii.member(jsii_name="resetOrganizationalUnit")
    def reset_organizational_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnit", []))

    @jsii.member(jsii_name="resetPostalCode")
    def reset_postal_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostalCode", []))

    @jsii.member(jsii_name="resetProvince")
    def reset_province(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvince", []))

    @jsii.member(jsii_name="resetStreetAddress")
    def reset_street_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreetAddress", []))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="countryCodeInput")
    def country_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="localityInput")
    def locality_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localityInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitInput")
    def organizational_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationalUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="postalCodeInput")
    def postal_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postalCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="provinceInput")
    def province_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provinceInput"))

    @builtins.property
    @jsii.member(jsii_name="streetAddressInput")
    def street_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streetAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="locality")
    def locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locality"))

    @locality.setter
    def locality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "locality").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locality", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "organizational_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "postal_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="province")
    def province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "province"))

    @province.setter
    def province(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "province").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "province", value)

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streetAddress"))

    @street_address.setter
    def street_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "street_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streetAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigSubjectConfigSubject]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigSubjectConfigSubject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigSubjectConfigSubject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509Config",
    jsii_struct_bases=[],
    name_mapping={
        "key_usage": "keyUsage",
        "additional_extensions": "additionalExtensions",
        "aia_ocsp_servers": "aiaOcspServers",
        "ca_options": "caOptions",
        "policy_ids": "policyIds",
    },
)
class GooglePrivatecaCertificateConfigX509Config:
    def __init__(
        self,
        *,
        key_usage: typing.Union["GooglePrivatecaCertificateConfigX509ConfigKeyUsage", typing.Dict[str, typing.Any]],
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ca_options: typing.Optional[typing.Union["GooglePrivatecaCertificateConfigX509ConfigCaOptions", typing.Dict[str, typing.Any]]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_usage GooglePrivatecaCertificate#key_usage}
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#additional_extensions GooglePrivatecaCertificate#additional_extensions}
        :param aia_ocsp_servers: Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#aia_ocsp_servers GooglePrivatecaCertificate#aia_ocsp_servers}
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ca_options GooglePrivatecaCertificate#ca_options}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#policy_ids GooglePrivatecaCertificate#policy_ids}
        '''
        if isinstance(key_usage, dict):
            key_usage = GooglePrivatecaCertificateConfigX509ConfigKeyUsage(**key_usage)
        if isinstance(ca_options, dict):
            ca_options = GooglePrivatecaCertificateConfigX509ConfigCaOptions(**ca_options)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509Config.__init__)
            check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            check_type(argname="argument additional_extensions", value=additional_extensions, expected_type=type_hints["additional_extensions"])
            check_type(argname="argument aia_ocsp_servers", value=aia_ocsp_servers, expected_type=type_hints["aia_ocsp_servers"])
            check_type(argname="argument ca_options", value=ca_options, expected_type=type_hints["ca_options"])
            check_type(argname="argument policy_ids", value=policy_ids, expected_type=type_hints["policy_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_usage": key_usage,
        }
        if additional_extensions is not None:
            self._values["additional_extensions"] = additional_extensions
        if aia_ocsp_servers is not None:
            self._values["aia_ocsp_servers"] = aia_ocsp_servers
        if ca_options is not None:
            self._values["ca_options"] = ca_options
        if policy_ids is not None:
            self._values["policy_ids"] = policy_ids

    @builtins.property
    def key_usage(self) -> "GooglePrivatecaCertificateConfigX509ConfigKeyUsage":
        '''key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_usage GooglePrivatecaCertificate#key_usage}
        '''
        result = self._values.get("key_usage")
        assert result is not None, "Required property 'key_usage' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigKeyUsage", result)

    @builtins.property
    def additional_extensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions"]]]:
        '''additional_extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#additional_extensions GooglePrivatecaCertificate#additional_extensions}
        '''
        result = self._values.get("additional_extensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions"]]], result)

    @builtins.property
    def aia_ocsp_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#aia_ocsp_servers GooglePrivatecaCertificate#aia_ocsp_servers}
        '''
        result = self._values.get("aia_ocsp_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ca_options(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateConfigX509ConfigCaOptions"]:
        '''ca_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ca_options GooglePrivatecaCertificate#ca_options}
        '''
        result = self._values.get("ca_options")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateConfigX509ConfigCaOptions"], result)

    @builtins.property
    def policy_ids(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigPolicyIds"]]]:
        '''policy_ids block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#policy_ids GooglePrivatecaCertificate#policy_ids}
        '''
        result = self._values.get("policy_ids")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigPolicyIds"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={"critical": "critical", "object_id": "objectId", "value": "value"},
)
class GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions:
    def __init__(
        self,
        *,
        critical: typing.Union[builtins.bool, cdktf.IResolvable],
        object_id: typing.Union["GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId", typing.Dict[str, typing.Any]],
        value: builtins.str,
    ) -> None:
        '''
        :param critical: Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#critical GooglePrivatecaCertificate#critical}
        :param object_id: object_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id GooglePrivatecaCertificate#object_id}
        :param value: The value of this X.509 extension. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#value GooglePrivatecaCertificate#value}
        '''
        if isinstance(object_id, dict):
            object_id = GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId(**object_id)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#critical GooglePrivatecaCertificate#critical}
        '''
        result = self._values.get("critical")
        assert result is not None, "Required property 'critical' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def object_id(
        self,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId":
        '''object_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id GooglePrivatecaCertificate#object_id}
        '''
        result = self._values.get("object_id")
        assert result is not None, "Required property 'object_id' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId", result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of this X.509 extension. A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#value GooglePrivatecaCertificate#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectId")
    def put_object_id(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        value = GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId(
            object_id_path=object_id_path
        )

        return typing.cast(None, jsii.invoke(self, "putObjectId", [value]))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(
        self,
    ) -> GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference:
        return typing.cast(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, jsii.get(self, "objectId"))

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
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId], jsii.get(self, "objectIdInput"))

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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference, "critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "critical", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigCaOptions",
    jsii_struct_bases=[],
    name_mapping={
        "is_ca": "isCa",
        "max_issuer_path_length": "maxIssuerPathLength",
        "non_ca": "nonCa",
        "zero_max_issuer_path_length": "zeroMaxIssuerPathLength",
    },
)
class GooglePrivatecaCertificateConfigX509ConfigCaOptions:
    def __init__(
        self,
        *,
        is_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
        non_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zero_max_issuer_path_length: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_ca: When true, the "CA" in Basic Constraints extension will be set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#is_ca GooglePrivatecaCertificate#is_ca}
        :param max_issuer_path_length: Refers to the "path length constraint" in Basic Constraints extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#max_issuer_path_length GooglePrivatecaCertificate#max_issuer_path_length}
        :param non_ca: When true, the "CA" in Basic Constraints extension will be set to false. If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#non_ca GooglePrivatecaCertificate#non_ca}
        :param zero_max_issuer_path_length: When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#zero_max_issuer_path_length GooglePrivatecaCertificate#zero_max_issuer_path_length}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigCaOptions.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#is_ca GooglePrivatecaCertificate#is_ca}
        '''
        result = self._values.get("is_ca")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_issuer_path_length(self) -> typing.Optional[jsii.Number]:
        '''Refers to the "path length constraint" in Basic Constraints extension.

        For a CA certificate, this value describes the depth of
        subordinate CA certificates that are allowed. If this value is less than 0, the request will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#max_issuer_path_length GooglePrivatecaCertificate#max_issuer_path_length}
        '''
        result = self._values.get("max_issuer_path_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def non_ca(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, the "CA" in Basic Constraints extension will be set to false.

        If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#non_ca GooglePrivatecaCertificate#non_ca}
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#zero_max_issuer_path_length GooglePrivatecaCertificate#zero_max_issuer_path_length}
        '''
        result = self._values.get("zero_max_issuer_path_length")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigCaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference, "is_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCa", value)

    @builtins.property
    @jsii.member(jsii_name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIssuerPathLength"))

    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference, "max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="nonCa")
    def non_ca(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nonCa"))

    @non_ca.setter
    def non_ca(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference, "non_ca").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference, "zero_max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zeroMaxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigCaOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigX509ConfigCaOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsage",
    jsii_struct_bases=[],
    name_mapping={
        "base_key_usage": "baseKeyUsage",
        "extended_key_usage": "extendedKeyUsage",
        "unknown_extended_key_usages": "unknownExtendedKeyUsages",
    },
)
class GooglePrivatecaCertificateConfigX509ConfigKeyUsage:
    def __init__(
        self,
        *,
        base_key_usage: typing.Union["GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage", typing.Dict[str, typing.Any]],
        extended_key_usage: typing.Union["GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage", typing.Dict[str, typing.Any]],
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#base_key_usage GooglePrivatecaCertificate#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#extended_key_usage GooglePrivatecaCertificate#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#unknown_extended_key_usages GooglePrivatecaCertificate#unknown_extended_key_usages}
        '''
        if isinstance(base_key_usage, dict):
            base_key_usage = GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage(**base_key_usage)
        if isinstance(extended_key_usage, dict):
            extended_key_usage = GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage(**extended_key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsage.__init__)
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
    ) -> "GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage":
        '''base_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#base_key_usage GooglePrivatecaCertificate#base_key_usage}
        '''
        result = self._values.get("base_key_usage")
        assert result is not None, "Required property 'base_key_usage' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage", result)

    @builtins.property
    def extended_key_usage(
        self,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage":
        '''extended_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#extended_key_usage GooglePrivatecaCertificate#extended_key_usage}
        '''
        result = self._values.get("extended_key_usage")
        assert result is not None, "Required property 'extended_key_usage' is missing"
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage", result)

    @builtins.property
    def unknown_extended_key_usages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]]:
        '''unknown_extended_key_usages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#unknown_extended_key_usages GooglePrivatecaCertificate#unknown_extended_key_usages}
        '''
        result = self._values.get("unknown_extended_key_usages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage",
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
class GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage:
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
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#cert_sign GooglePrivatecaCertificate#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#content_commitment GooglePrivatecaCertificate#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#crl_sign GooglePrivatecaCertificate#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#data_encipherment GooglePrivatecaCertificate#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#decipher_only GooglePrivatecaCertificate#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#digital_signature GooglePrivatecaCertificate#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#encipher_only GooglePrivatecaCertificate#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_agreement GooglePrivatecaCertificate#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_encipherment GooglePrivatecaCertificate#key_encipherment}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#cert_sign GooglePrivatecaCertificate#cert_sign}
        '''
        result = self._values.get("cert_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def content_commitment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#content_commitment GooglePrivatecaCertificate#content_commitment}
        '''
        result = self._values.get("content_commitment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def crl_sign(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used sign certificate revocation lists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#crl_sign GooglePrivatecaCertificate#crl_sign}
        '''
        result = self._values.get("crl_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#data_encipherment GooglePrivatecaCertificate#data_encipherment}
        '''
        result = self._values.get("data_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def decipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to decipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#decipher_only GooglePrivatecaCertificate#decipher_only}
        '''
        result = self._values.get("decipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def digital_signature(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for digital signatures.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#digital_signature GooglePrivatecaCertificate#digital_signature}
        '''
        result = self._values.get("digital_signature")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#encipher_only GooglePrivatecaCertificate#encipher_only}
        '''
        result = self._values.get("encipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_agreement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used in a key agreement protocol.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_agreement GooglePrivatecaCertificate#key_agreement}
        '''
        result = self._values.get("key_agreement")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher other keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_encipherment GooglePrivatecaCertificate#key_encipherment}
        '''
        result = self._values.get("key_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "cert_sign").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "content_commitment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentCommitment", value)

    @builtins.property
    @jsii.member(jsii_name="crlSign")
    def crl_sign(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "crlSign"))

    @crl_sign.setter
    def crl_sign(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "crl_sign").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "data_encipherment").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "decipher_only").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "digital_signature").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "encipher_only").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "key_agreement").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "key_encipherment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyEncipherment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage",
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
class GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage:
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
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#client_auth GooglePrivatecaCertificate#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#code_signing GooglePrivatecaCertificate#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#email_protection GooglePrivatecaCertificate#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ocsp_signing GooglePrivatecaCertificate#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#server_auth GooglePrivatecaCertificate#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#time_stamping GooglePrivatecaCertificate#time_stamping}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#client_auth GooglePrivatecaCertificate#client_auth}
        '''
        result = self._values.get("client_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def code_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#code_signing GooglePrivatecaCertificate#code_signing}
        '''
        result = self._values.get("code_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def email_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#email_protection GooglePrivatecaCertificate#email_protection}
        '''
        result = self._values.get("email_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ocsp_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ocsp_signing GooglePrivatecaCertificate#ocsp_signing}
        '''
        result = self._values.get("ocsp_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def server_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#server_auth GooglePrivatecaCertificate#server_auth}
        '''
        result = self._values.get("server_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def time_stamping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#time_stamping GooglePrivatecaCertificate#time_stamping}
        '''
        result = self._values.get("time_stamping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "client_auth").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "code_signing").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "email_protection").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "ocsp_signing").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "server_auth").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "time_stamping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeStamping", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference.__init__)
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
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#cert_sign GooglePrivatecaCertificate#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#content_commitment GooglePrivatecaCertificate#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#crl_sign GooglePrivatecaCertificate#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#data_encipherment GooglePrivatecaCertificate#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#decipher_only GooglePrivatecaCertificate#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#digital_signature GooglePrivatecaCertificate#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#encipher_only GooglePrivatecaCertificate#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_agreement GooglePrivatecaCertificate#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#key_encipherment GooglePrivatecaCertificate#key_encipherment}
        '''
        value = GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage(
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
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#client_auth GooglePrivatecaCertificate#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#code_signing GooglePrivatecaCertificate#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#email_protection GooglePrivatecaCertificate#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#ocsp_signing GooglePrivatecaCertificate#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#server_auth GooglePrivatecaCertificate#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#time_stamping GooglePrivatecaCertificate#time_stamping}
        '''
        value = GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage(
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference.put_unknown_extended_key_usages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUnknownExtendedKeyUsages", [value]))

    @jsii.member(jsii_name="resetUnknownExtendedKeyUsages")
    def reset_unknown_extended_key_usages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnknownExtendedKeyUsages", []))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsageInput")
    def base_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage], jsii.get(self, "baseKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsageInput")
    def extended_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage], jsii.get(self, "extendedKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsagesInput")
    def unknown_extended_key_usages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]], jsii.get(self, "unknownExtendedKeyUsagesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateConfigX509ConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalExtensions")
    def put_additional_extensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigOutputReference.put_additional_extensions)
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
        :param is_ca: When true, the "CA" in Basic Constraints extension will be set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#is_ca GooglePrivatecaCertificate#is_ca}
        :param max_issuer_path_length: Refers to the "path length constraint" in Basic Constraints extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#max_issuer_path_length GooglePrivatecaCertificate#max_issuer_path_length}
        :param non_ca: When true, the "CA" in Basic Constraints extension will be set to false. If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#non_ca GooglePrivatecaCertificate#non_ca}
        :param zero_max_issuer_path_length: When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#zero_max_issuer_path_length GooglePrivatecaCertificate#zero_max_issuer_path_length}
        '''
        value = GooglePrivatecaCertificateConfigX509ConfigCaOptions(
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
        base_key_usage: typing.Union[GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage, typing.Dict[str, typing.Any]],
        extended_key_usage: typing.Union[GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage, typing.Dict[str, typing.Any]],
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#base_key_usage GooglePrivatecaCertificate#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#extended_key_usage GooglePrivatecaCertificate#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#unknown_extended_key_usages GooglePrivatecaCertificate#unknown_extended_key_usages}
        '''
        value = GooglePrivatecaCertificateConfigX509ConfigKeyUsage(
            base_key_usage=base_key_usage,
            extended_key_usage=extended_key_usage,
            unknown_extended_key_usages=unknown_extended_key_usages,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyUsage", [value]))

    @jsii.member(jsii_name="putPolicyIds")
    def put_policy_ids(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateConfigX509ConfigPolicyIds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigOutputReference.put_policy_ids)
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

    @jsii.member(jsii_name="resetPolicyIds")
    def reset_policy_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyIds", []))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensions")
    def additional_extensions(
        self,
    ) -> GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList:
        return typing.cast(GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="caOptions")
    def ca_options(
        self,
    ) -> GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference:
        return typing.cast(GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference, jsii.get(self, "caOptions"))

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(self) -> "GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList":
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList", jsii.get(self, "policyIds"))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensionsInput")
    def additional_extensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions]]], jsii.get(self, "additionalExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServersInput")
    def aia_ocsp_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aiaOcspServersInput"))

    @builtins.property
    @jsii.member(jsii_name="caOptionsInput")
    def ca_options_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigCaOptions], jsii.get(self, "caOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUsageInput")
    def key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509ConfigKeyUsage], jsii.get(self, "keyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdsInput")
    def policy_ids_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigPolicyIds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateConfigX509ConfigPolicyIds"]]], jsii.get(self, "policyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServers")
    def aia_ocsp_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaOcspServers"))

    @aia_ocsp_servers.setter
    def aia_ocsp_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigOutputReference, "aia_ocsp_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiaOcspServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateConfigX509Config]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateConfigX509Config], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateConfigX509Config],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigPolicyIds",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateConfigX509ConfigPolicyIds:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigPolicyIds.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#object_id_path GooglePrivatecaCertificate#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateConfigX509ConfigPolicyIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigPolicyIds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigPolicyIds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateConfigX509ConfigPolicyIds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigPolicyIds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigPolicyIds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateConfigX509ConfigPolicyIds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateRevocationDetails",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateRevocationDetails:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateRevocationDetails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateRevocationDetailsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateRevocationDetailsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateRevocationDetailsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateRevocationDetailsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateRevocationDetailsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateRevocationDetailsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateRevocationDetailsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateRevocationDetailsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateRevocationDetailsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateRevocationDetailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateRevocationDetailsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateRevocationDetailsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="revocationState")
    def revocation_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revocationState"))

    @builtins.property
    @jsii.member(jsii_name="revocationTime")
    def revocation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revocationTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateRevocationDetails]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateRevocationDetails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateRevocationDetails],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateRevocationDetailsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePrivatecaCertificateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#create GooglePrivatecaCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#delete GooglePrivatecaCertificate#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#update GooglePrivatecaCertificate#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#create GooglePrivatecaCertificate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#delete GooglePrivatecaCertificate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate#update GooglePrivatecaCertificate#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificate.GooglePrivatecaCertificateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePrivatecaCertificate",
    "GooglePrivatecaCertificateCertificateDescription",
    "GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyId",
    "GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdList",
    "GooglePrivatecaCertificateCertificateDescriptionAuthorityKeyIdOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionCertFingerprint",
    "GooglePrivatecaCertificateCertificateDescriptionCertFingerprintList",
    "GooglePrivatecaCertificateCertificateDescriptionCertFingerprintOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValues",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsage",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsage",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptions",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageKeyUsageOptionsOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageBaseKeyUsageOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsage",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageExtendedKeyUsageOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsages",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectId",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesObectIdOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesList",
    "GooglePrivatecaCertificateCertificateDescriptionConfigValuesOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionList",
    "GooglePrivatecaCertificateCertificateDescriptionOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionPublicKey",
    "GooglePrivatecaCertificateCertificateDescriptionPublicKeyList",
    "GooglePrivatecaCertificateCertificateDescriptionPublicKeyOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescription",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionList",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubject",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltName",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSans",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansList",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectId",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdList",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansObectIdOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameCustomSansOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameList",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectAltNameOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectList",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectDescriptionSubjectOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectKeyId",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdList",
    "GooglePrivatecaCertificateCertificateDescriptionSubjectKeyIdOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509Description",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensions",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectId",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsObjectIdOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionAdditionalExtensionsOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptions",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionCaOptionsOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsage",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsage",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageBaseKeyUsageOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsage",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageExtendedKeyUsageOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsages",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionOutputReference",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIds",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsList",
    "GooglePrivatecaCertificateCertificateDescriptionX509DescriptionPolicyIdsOutputReference",
    "GooglePrivatecaCertificateConfig",
    "GooglePrivatecaCertificateConfigA",
    "GooglePrivatecaCertificateConfigAOutputReference",
    "GooglePrivatecaCertificateConfigPublicKey",
    "GooglePrivatecaCertificateConfigPublicKeyOutputReference",
    "GooglePrivatecaCertificateConfigSubjectConfig",
    "GooglePrivatecaCertificateConfigSubjectConfigOutputReference",
    "GooglePrivatecaCertificateConfigSubjectConfigSubject",
    "GooglePrivatecaCertificateConfigSubjectConfigSubjectAltName",
    "GooglePrivatecaCertificateConfigSubjectConfigSubjectAltNameOutputReference",
    "GooglePrivatecaCertificateConfigSubjectConfigSubjectOutputReference",
    "GooglePrivatecaCertificateConfigX509Config",
    "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensions",
    "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsList",
    "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectId",
    "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsObjectIdOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigAdditionalExtensionsOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigCaOptions",
    "GooglePrivatecaCertificateConfigX509ConfigCaOptionsOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsage",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsage",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageBaseKeyUsageOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsage",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsages",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList",
    "GooglePrivatecaCertificateConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigOutputReference",
    "GooglePrivatecaCertificateConfigX509ConfigPolicyIds",
    "GooglePrivatecaCertificateConfigX509ConfigPolicyIdsList",
    "GooglePrivatecaCertificateConfigX509ConfigPolicyIdsOutputReference",
    "GooglePrivatecaCertificateRevocationDetails",
    "GooglePrivatecaCertificateRevocationDetailsList",
    "GooglePrivatecaCertificateRevocationDetailsOutputReference",
    "GooglePrivatecaCertificateTimeouts",
    "GooglePrivatecaCertificateTimeoutsOutputReference",
]

publication.publish()
