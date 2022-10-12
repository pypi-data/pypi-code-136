'''
# `google_privateca_certificate_authority`

Refer to the Terraform Registory for docs: [`google_privateca_certificate_authority`](https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority).
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


class GooglePrivatecaCertificateAuthority(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthority",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority google_privateca_certificate_authority}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        certificate_authority_id: builtins.str,
        config: typing.Union["GooglePrivatecaCertificateAuthorityConfigA", typing.Dict[str, typing.Any]],
        key_spec: typing.Union["GooglePrivatecaCertificateAuthorityKeySpec", typing.Dict[str, typing.Any]],
        location: builtins.str,
        pool: builtins.str,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        gcs_bucket: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_active_certificates_on_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lifetime: typing.Optional[builtins.str] = None,
        pem_ca_certificate: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        subordinate_config: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthoritySubordinateConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthorityTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority google_privateca_certificate_authority} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_authority_id: The user provided Resource ID for this Certificate Authority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#certificate_authority_id GooglePrivatecaCertificateAuthority#certificate_authority_id}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#config GooglePrivatecaCertificateAuthority#config}
        :param key_spec: key_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_spec GooglePrivatecaCertificateAuthority#key_spec}
        :param location: Location of the CertificateAuthority. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#location GooglePrivatecaCertificateAuthority#location}
        :param pool: The name of the CaPool this Certificate Authority belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pool GooglePrivatecaCertificateAuthority#pool}
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#deletion_protection GooglePrivatecaCertificateAuthority#deletion_protection}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#desired_state GooglePrivatecaCertificateAuthority#desired_state}.
        :param gcs_bucket: The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs. This must be a bucket name, without any prefixes (such as 'gs://') or suffixes (such as '.googleapis.com'). For example, to use a bucket named my-bucket, you would simply specify 'my-bucket'. If not specified, a managed bucket will be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#gcs_bucket GooglePrivatecaCertificateAuthority#gcs_bucket}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#id GooglePrivatecaCertificateAuthority#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_active_certificates_on_deletion: This field allows the CA to be deleted even if the CA has active certs. Active certs include both unrevoked and unexpired certs. Use with care. Defaults to 'false'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ignore_active_certificates_on_deletion GooglePrivatecaCertificateAuthority#ignore_active_certificates_on_deletion}
        :param labels: Labels with user-defined metadata. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#labels GooglePrivatecaCertificateAuthority#labels}
        :param lifetime: The desired lifetime of the CA certificate. Used to create the "notBeforeTime" and "notAfterTime" fields inside an X.509 certificate. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#lifetime GooglePrivatecaCertificateAuthority#lifetime}
        :param pem_ca_certificate: The signed CA certificate issued from the subordinated CA's CSR. This is needed when activating the subordiante CA with a third party issuer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_ca_certificate GooglePrivatecaCertificateAuthority#pem_ca_certificate}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#project GooglePrivatecaCertificateAuthority#project}.
        :param subordinate_config: subordinate_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subordinate_config GooglePrivatecaCertificateAuthority#subordinate_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#timeouts GooglePrivatecaCertificateAuthority#timeouts}
        :param type: The Type of this CertificateAuthority. ~> **Note:** For 'SUBORDINATE' Certificate Authorities, they need to be activated before they can issue certificates. Default value: "SELF_SIGNED" Possible values: ["SELF_SIGNED", "SUBORDINATE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#type GooglePrivatecaCertificateAuthority#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthority.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = GooglePrivatecaCertificateAuthorityConfig(
            certificate_authority_id=certificate_authority_id,
            config=config,
            key_spec=key_spec,
            location=location,
            pool=pool,
            deletion_protection=deletion_protection,
            desired_state=desired_state,
            gcs_bucket=gcs_bucket,
            id=id,
            ignore_active_certificates_on_deletion=ignore_active_certificates_on_deletion,
            labels=labels,
            lifetime=lifetime,
            pem_ca_certificate=pem_ca_certificate,
            project=project,
            subordinate_config=subordinate_config,
            timeouts=timeouts,
            type=type,
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
        subject_config: typing.Union["GooglePrivatecaCertificateAuthorityConfigSubjectConfig", typing.Dict[str, typing.Any]],
        x509_config: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509Config", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param subject_config: subject_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject_config GooglePrivatecaCertificateAuthority#subject_config}
        :param x509_config: x509_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#x509_config GooglePrivatecaCertificateAuthority#x509_config}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigA(
            subject_config=subject_config, x509_config=x509_config
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="putKeySpec")
    def put_key_spec(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        cloud_kms_key_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param algorithm: The algorithm to use for creating a managed Cloud KMS key for a for a simplified experience. All managed keys will be have their ProtectionLevel as HSM. Possible values: ["SIGN_HASH_ALGORITHM_UNSPECIFIED", "RSA_PSS_2048_SHA256", "RSA_PSS_3072_SHA256", "RSA_PSS_4096_SHA256", "RSA_PKCS1_2048_SHA256", "RSA_PKCS1_3072_SHA256", "RSA_PKCS1_4096_SHA256", "EC_P256_SHA256", "EC_P384_SHA384"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#algorithm GooglePrivatecaCertificateAuthority#algorithm}
        :param cloud_kms_key_version: The resource name for an existing Cloud KMS CryptoKeyVersion in the format 'projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#cloud_kms_key_version GooglePrivatecaCertificateAuthority#cloud_kms_key_version}
        '''
        value = GooglePrivatecaCertificateAuthorityKeySpec(
            algorithm=algorithm, cloud_kms_key_version=cloud_kms_key_version
        )

        return typing.cast(None, jsii.invoke(self, "putKeySpec", [value]))

    @jsii.member(jsii_name="putSubordinateConfig")
    def put_subordinate_config(
        self,
        *,
        certificate_authority: typing.Optional[builtins.str] = None,
        pem_issuer_chain: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate_authority: This can refer to a CertificateAuthority that was used to create a subordinate CertificateAuthority. This field is used for information and usability purposes only. The resource name is in the format 'projects/*/locations/*/caPools/*/certificateAuthorities/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#certificate_authority GooglePrivatecaCertificateAuthority#certificate_authority}
        :param pem_issuer_chain: pem_issuer_chain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_issuer_chain GooglePrivatecaCertificateAuthority#pem_issuer_chain}
        '''
        value = GooglePrivatecaCertificateAuthoritySubordinateConfig(
            certificate_authority=certificate_authority,
            pem_issuer_chain=pem_issuer_chain,
        )

        return typing.cast(None, jsii.invoke(self, "putSubordinateConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#create GooglePrivatecaCertificateAuthority#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#delete GooglePrivatecaCertificateAuthority#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#update GooglePrivatecaCertificateAuthority#update}.
        '''
        value = GooglePrivatecaCertificateAuthorityTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetGcsBucket")
    def reset_gcs_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcsBucket", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreActiveCertificatesOnDeletion")
    def reset_ignore_active_certificates_on_deletion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreActiveCertificatesOnDeletion", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLifetime")
    def reset_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifetime", []))

    @jsii.member(jsii_name="resetPemCaCertificate")
    def reset_pem_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemCaCertificate", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSubordinateConfig")
    def reset_subordinate_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubordinateConfig", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessUrls")
    def access_urls(self) -> "GooglePrivatecaCertificateAuthorityAccessUrlsList":
        return typing.cast("GooglePrivatecaCertificateAuthorityAccessUrlsList", jsii.get(self, "accessUrls"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "GooglePrivatecaCertificateAuthorityConfigAOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="keySpec")
    def key_spec(self) -> "GooglePrivatecaCertificateAuthorityKeySpecOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityKeySpecOutputReference", jsii.get(self, "keySpec"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="pemCaCertificates")
    def pem_ca_certificates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemCaCertificates"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="subordinateConfig")
    def subordinate_config(
        self,
    ) -> "GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference", jsii.get(self, "subordinateConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GooglePrivatecaCertificateAuthorityTimeoutsOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityIdInput")
    def certificate_authority_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityConfigA"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsBucketInput")
    def gcs_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gcsBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreActiveCertificatesOnDeletionInput")
    def ignore_active_certificates_on_deletion_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreActiveCertificatesOnDeletionInput"))

    @builtins.property
    @jsii.member(jsii_name="keySpecInput")
    def key_spec_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityKeySpec"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityKeySpec"], jsii.get(self, "keySpecInput"))

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
    @jsii.member(jsii_name="pemCaCertificateInput")
    def pem_ca_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pemCaCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="poolInput")
    def pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="subordinateConfigInput")
    def subordinate_config_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfig"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfig"], jsii.get(self, "subordinateConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GooglePrivatecaCertificateAuthorityTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GooglePrivatecaCertificateAuthorityTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityId")
    def certificate_authority_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityId"))

    @certificate_authority_id.setter
    def certificate_authority_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "certificate_authority_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityId", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "deletion_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "desired_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="gcsBucket")
    def gcs_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcsBucket"))

    @gcs_bucket.setter
    def gcs_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "gcs_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcsBucket", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreActiveCertificatesOnDeletion")
    def ignore_active_certificates_on_deletion(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreActiveCertificatesOnDeletion"))

    @ignore_active_certificates_on_deletion.setter
    def ignore_active_certificates_on_deletion(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "ignore_active_certificates_on_deletion").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreActiveCertificatesOnDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="lifetime")
    def lifetime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifetime"))

    @lifetime.setter
    def lifetime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifetime", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="pemCaCertificate")
    def pem_ca_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pemCaCertificate"))

    @pem_ca_certificate.setter
    def pem_ca_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "pem_ca_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemCaCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="pool")
    def pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pool"))

    @pool.setter
    def pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pool", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthority, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityAccessUrls",
    jsii_struct_bases=[],
    name_mapping={},
)
class GooglePrivatecaCertificateAuthorityAccessUrls:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityAccessUrls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityAccessUrlsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityAccessUrlsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityAccessUrlsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityAccessUrlsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityAccessUrlsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityAccessUrlsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityAccessUrlsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference.__init__)
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
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityAccessUrls]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityAccessUrls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityAccessUrls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfig",
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
        "config": "config",
        "key_spec": "keySpec",
        "location": "location",
        "pool": "pool",
        "deletion_protection": "deletionProtection",
        "desired_state": "desiredState",
        "gcs_bucket": "gcsBucket",
        "id": "id",
        "ignore_active_certificates_on_deletion": "ignoreActiveCertificatesOnDeletion",
        "labels": "labels",
        "lifetime": "lifetime",
        "pem_ca_certificate": "pemCaCertificate",
        "project": "project",
        "subordinate_config": "subordinateConfig",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class GooglePrivatecaCertificateAuthorityConfig(cdktf.TerraformMetaArguments):
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
        certificate_authority_id: builtins.str,
        config: typing.Union["GooglePrivatecaCertificateAuthorityConfigA", typing.Dict[str, typing.Any]],
        key_spec: typing.Union["GooglePrivatecaCertificateAuthorityKeySpec", typing.Dict[str, typing.Any]],
        location: builtins.str,
        pool: builtins.str,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        gcs_bucket: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_active_certificates_on_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lifetime: typing.Optional[builtins.str] = None,
        pem_ca_certificate: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        subordinate_config: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthoritySubordinateConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthorityTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_authority_id: The user provided Resource ID for this Certificate Authority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#certificate_authority_id GooglePrivatecaCertificateAuthority#certificate_authority_id}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#config GooglePrivatecaCertificateAuthority#config}
        :param key_spec: key_spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_spec GooglePrivatecaCertificateAuthority#key_spec}
        :param location: Location of the CertificateAuthority. A full list of valid locations can be found by running 'gcloud privateca locations list'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#location GooglePrivatecaCertificateAuthority#location}
        :param pool: The name of the CaPool this Certificate Authority belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pool GooglePrivatecaCertificateAuthority#pool}
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#deletion_protection GooglePrivatecaCertificateAuthority#deletion_protection}.
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#desired_state GooglePrivatecaCertificateAuthority#desired_state}.
        :param gcs_bucket: The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs. This must be a bucket name, without any prefixes (such as 'gs://') or suffixes (such as '.googleapis.com'). For example, to use a bucket named my-bucket, you would simply specify 'my-bucket'. If not specified, a managed bucket will be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#gcs_bucket GooglePrivatecaCertificateAuthority#gcs_bucket}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#id GooglePrivatecaCertificateAuthority#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_active_certificates_on_deletion: This field allows the CA to be deleted even if the CA has active certs. Active certs include both unrevoked and unexpired certs. Use with care. Defaults to 'false'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ignore_active_certificates_on_deletion GooglePrivatecaCertificateAuthority#ignore_active_certificates_on_deletion}
        :param labels: Labels with user-defined metadata. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#labels GooglePrivatecaCertificateAuthority#labels}
        :param lifetime: The desired lifetime of the CA certificate. Used to create the "notBeforeTime" and "notAfterTime" fields inside an X.509 certificate. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#lifetime GooglePrivatecaCertificateAuthority#lifetime}
        :param pem_ca_certificate: The signed CA certificate issued from the subordinated CA's CSR. This is needed when activating the subordiante CA with a third party issuer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_ca_certificate GooglePrivatecaCertificateAuthority#pem_ca_certificate}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#project GooglePrivatecaCertificateAuthority#project}.
        :param subordinate_config: subordinate_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subordinate_config GooglePrivatecaCertificateAuthority#subordinate_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#timeouts GooglePrivatecaCertificateAuthority#timeouts}
        :param type: The Type of this CertificateAuthority. ~> **Note:** For 'SUBORDINATE' Certificate Authorities, they need to be activated before they can issue certificates. Default value: "SELF_SIGNED" Possible values: ["SELF_SIGNED", "SUBORDINATE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#type GooglePrivatecaCertificateAuthority#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = GooglePrivatecaCertificateAuthorityConfigA(**config)
        if isinstance(key_spec, dict):
            key_spec = GooglePrivatecaCertificateAuthorityKeySpec(**key_spec)
        if isinstance(subordinate_config, dict):
            subordinate_config = GooglePrivatecaCertificateAuthoritySubordinateConfig(**subordinate_config)
        if isinstance(timeouts, dict):
            timeouts = GooglePrivatecaCertificateAuthorityTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_authority_id", value=certificate_authority_id, expected_type=type_hints["certificate_authority_id"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument key_spec", value=key_spec, expected_type=type_hints["key_spec"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument pool", value=pool, expected_type=type_hints["pool"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument gcs_bucket", value=gcs_bucket, expected_type=type_hints["gcs_bucket"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_active_certificates_on_deletion", value=ignore_active_certificates_on_deletion, expected_type=type_hints["ignore_active_certificates_on_deletion"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument lifetime", value=lifetime, expected_type=type_hints["lifetime"])
            check_type(argname="argument pem_ca_certificate", value=pem_ca_certificate, expected_type=type_hints["pem_ca_certificate"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument subordinate_config", value=subordinate_config, expected_type=type_hints["subordinate_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_authority_id": certificate_authority_id,
            "config": config,
            "key_spec": key_spec,
            "location": location,
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
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if gcs_bucket is not None:
            self._values["gcs_bucket"] = gcs_bucket
        if id is not None:
            self._values["id"] = id
        if ignore_active_certificates_on_deletion is not None:
            self._values["ignore_active_certificates_on_deletion"] = ignore_active_certificates_on_deletion
        if labels is not None:
            self._values["labels"] = labels
        if lifetime is not None:
            self._values["lifetime"] = lifetime
        if pem_ca_certificate is not None:
            self._values["pem_ca_certificate"] = pem_ca_certificate
        if project is not None:
            self._values["project"] = project
        if subordinate_config is not None:
            self._values["subordinate_config"] = subordinate_config
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

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
    def certificate_authority_id(self) -> builtins.str:
        '''The user provided Resource ID for this Certificate Authority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#certificate_authority_id GooglePrivatecaCertificateAuthority#certificate_authority_id}
        '''
        result = self._values.get("certificate_authority_id")
        assert result is not None, "Required property 'certificate_authority_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> "GooglePrivatecaCertificateAuthorityConfigA":
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#config GooglePrivatecaCertificateAuthority#config}
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigA", result)

    @builtins.property
    def key_spec(self) -> "GooglePrivatecaCertificateAuthorityKeySpec":
        '''key_spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_spec GooglePrivatecaCertificateAuthority#key_spec}
        '''
        result = self._values.get("key_spec")
        assert result is not None, "Required property 'key_spec' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityKeySpec", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Location of the CertificateAuthority. A full list of valid locations can be found by running 'gcloud privateca locations list'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#location GooglePrivatecaCertificateAuthority#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool(self) -> builtins.str:
        '''The name of the CaPool this Certificate Authority belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pool GooglePrivatecaCertificateAuthority#pool}
        '''
        result = self._values.get("pool")
        assert result is not None, "Required property 'pool' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#deletion_protection GooglePrivatecaCertificateAuthority#deletion_protection}.'''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#desired_state GooglePrivatecaCertificateAuthority#desired_state}.'''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcs_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs.

        This must be a bucket name, without any prefixes
        (such as 'gs://') or suffixes (such as '.googleapis.com'). For example, to use a bucket named
        my-bucket, you would simply specify 'my-bucket'. If not specified, a managed bucket will be
        created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#gcs_bucket GooglePrivatecaCertificateAuthority#gcs_bucket}
        '''
        result = self._values.get("gcs_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#id GooglePrivatecaCertificateAuthority#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_active_certificates_on_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''This field allows the CA to be deleted even if the CA has active certs.

        Active certs include both unrevoked and unexpired certs.
        Use with care. Defaults to 'false'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ignore_active_certificates_on_deletion GooglePrivatecaCertificateAuthority#ignore_active_certificates_on_deletion}
        '''
        result = self._values.get("ignore_active_certificates_on_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels with user-defined metadata.

        An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass":
        "1.3kg", "count": "3" }.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#labels GooglePrivatecaCertificateAuthority#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def lifetime(self) -> typing.Optional[builtins.str]:
        '''The desired lifetime of the CA certificate.

        Used to create the "notBeforeTime" and
        "notAfterTime" fields inside an X.509 certificate. A duration in seconds with up to nine
        fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#lifetime GooglePrivatecaCertificateAuthority#lifetime}
        '''
        result = self._values.get("lifetime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_ca_certificate(self) -> typing.Optional[builtins.str]:
        '''The signed CA certificate issued from the subordinated CA's CSR.

        This is needed when activating the subordiante CA with a third party issuer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_ca_certificate GooglePrivatecaCertificateAuthority#pem_ca_certificate}
        '''
        result = self._values.get("pem_ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#project GooglePrivatecaCertificateAuthority#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subordinate_config(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfig"]:
        '''subordinate_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subordinate_config GooglePrivatecaCertificateAuthority#subordinate_config}
        '''
        result = self._values.get("subordinate_config")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfig"], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#timeouts GooglePrivatecaCertificateAuthority#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The Type of this CertificateAuthority.

        ~> **Note:** For 'SUBORDINATE' Certificate Authorities, they need to
        be activated before they can issue certificates. Default value: "SELF_SIGNED" Possible values: ["SELF_SIGNED", "SUBORDINATE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#type GooglePrivatecaCertificateAuthority#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigA",
    jsii_struct_bases=[],
    name_mapping={"subject_config": "subjectConfig", "x509_config": "x509Config"},
)
class GooglePrivatecaCertificateAuthorityConfigA:
    def __init__(
        self,
        *,
        subject_config: typing.Union["GooglePrivatecaCertificateAuthorityConfigSubjectConfig", typing.Dict[str, typing.Any]],
        x509_config: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509Config", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param subject_config: subject_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject_config GooglePrivatecaCertificateAuthority#subject_config}
        :param x509_config: x509_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#x509_config GooglePrivatecaCertificateAuthority#x509_config}
        '''
        if isinstance(subject_config, dict):
            subject_config = GooglePrivatecaCertificateAuthorityConfigSubjectConfig(**subject_config)
        if isinstance(x509_config, dict):
            x509_config = GooglePrivatecaCertificateAuthorityConfigX509Config(**x509_config)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigA.__init__)
            check_type(argname="argument subject_config", value=subject_config, expected_type=type_hints["subject_config"])
            check_type(argname="argument x509_config", value=x509_config, expected_type=type_hints["x509_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "subject_config": subject_config,
            "x509_config": x509_config,
        }

    @builtins.property
    def subject_config(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigSubjectConfig":
        '''subject_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject_config GooglePrivatecaCertificateAuthority#subject_config}
        '''
        result = self._values.get("subject_config")
        assert result is not None, "Required property 'subject_config' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigSubjectConfig", result)

    @builtins.property
    def x509_config(self) -> "GooglePrivatecaCertificateAuthorityConfigX509Config":
        '''x509_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#x509_config GooglePrivatecaCertificateAuthority#x509_config}
        '''
        result = self._values.get("x509_config")
        assert result is not None, "Required property 'x509_config' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509Config", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigAOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectConfig")
    def put_subject_config(
        self,
        *,
        subject: typing.Union["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject", typing.Dict[str, typing.Any]],
        subject_alt_name: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject GooglePrivatecaCertificateAuthority#subject}
        :param subject_alt_name: subject_alt_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject_alt_name GooglePrivatecaCertificateAuthority#subject_alt_name}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigSubjectConfig(
            subject=subject, subject_alt_name=subject_alt_name
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectConfig", [value]))

    @jsii.member(jsii_name="putX509Config")
    def put_x509_config(
        self,
        *,
        ca_options: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions", typing.Dict[str, typing.Any]],
        key_usage: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage", typing.Dict[str, typing.Any]],
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ca_options GooglePrivatecaCertificateAuthority#ca_options}
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_usage GooglePrivatecaCertificateAuthority#key_usage}
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#additional_extensions GooglePrivatecaCertificateAuthority#additional_extensions}
        :param aia_ocsp_servers: Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#aia_ocsp_servers GooglePrivatecaCertificateAuthority#aia_ocsp_servers}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#policy_ids GooglePrivatecaCertificateAuthority#policy_ids}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigX509Config(
            ca_options=ca_options,
            key_usage=key_usage,
            additional_extensions=additional_extensions,
            aia_ocsp_servers=aia_ocsp_servers,
            policy_ids=policy_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putX509Config", [value]))

    @builtins.property
    @jsii.member(jsii_name="subjectConfig")
    def subject_config(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference", jsii.get(self, "subjectConfig"))

    @builtins.property
    @jsii.member(jsii_name="x509Config")
    def x509_config(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference", jsii.get(self, "x509Config"))

    @builtins.property
    @jsii.member(jsii_name="subjectConfigInput")
    def subject_config_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfig"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfig"], jsii.get(self, "subjectConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="x509ConfigInput")
    def x509_config_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityConfigX509Config"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityConfigX509Config"], jsii.get(self, "x509ConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigA]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigSubjectConfig",
    jsii_struct_bases=[],
    name_mapping={"subject": "subject", "subject_alt_name": "subjectAltName"},
)
class GooglePrivatecaCertificateAuthorityConfigSubjectConfig:
    def __init__(
        self,
        *,
        subject: typing.Union["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject", typing.Dict[str, typing.Any]],
        subject_alt_name: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject GooglePrivatecaCertificateAuthority#subject}
        :param subject_alt_name: subject_alt_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject_alt_name GooglePrivatecaCertificateAuthority#subject_alt_name}
        '''
        if isinstance(subject, dict):
            subject = GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject(**subject)
        if isinstance(subject_alt_name, dict):
            subject_alt_name = GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName(**subject_alt_name)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigSubjectConfig.__init__)
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument subject_alt_name", value=subject_alt_name, expected_type=type_hints["subject_alt_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "subject": subject,
        }
        if subject_alt_name is not None:
            self._values["subject_alt_name"] = subject_alt_name

    @builtins.property
    def subject(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject":
        '''subject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject GooglePrivatecaCertificateAuthority#subject}
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject", result)

    @builtins.property
    def subject_alt_name(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName"]:
        '''subject_alt_name block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#subject_alt_name GooglePrivatecaCertificateAuthority#subject_alt_name}
        '''
        result = self._values.get("subject_alt_name")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigSubjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference.__init__)
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
        :param common_name: The common name of the distinguished name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#common_name GooglePrivatecaCertificateAuthority#common_name}
        :param organization: The organization of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#organization GooglePrivatecaCertificateAuthority#organization}
        :param country_code: The country code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#country_code GooglePrivatecaCertificateAuthority#country_code}
        :param locality: The locality or city of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#locality GooglePrivatecaCertificateAuthority#locality}
        :param organizational_unit: The organizational unit of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#organizational_unit GooglePrivatecaCertificateAuthority#organizational_unit}
        :param postal_code: The postal code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#postal_code GooglePrivatecaCertificateAuthority#postal_code}
        :param province: The province, territory, or regional state of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#province GooglePrivatecaCertificateAuthority#province}
        :param street_address: The street address of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#street_address GooglePrivatecaCertificateAuthority#street_address}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject(
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
        :param dns_names: Contains only valid, fully-qualified host names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#dns_names GooglePrivatecaCertificateAuthority#dns_names}
        :param email_addresses: Contains only valid RFC 2822 E-mail addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#email_addresses GooglePrivatecaCertificateAuthority#email_addresses}
        :param ip_addresses: Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ip_addresses GooglePrivatecaCertificateAuthority#ip_addresses}
        :param uris: Contains only valid RFC 3986 URIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#uris GooglePrivatecaCertificateAuthority#uris}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName(
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
    ) -> "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltName")
    def subject_alt_name(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference", jsii.get(self, "subjectAltName"))

    @builtins.property
    @jsii.member(jsii_name="subjectAltNameInput")
    def subject_alt_name_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName"], jsii.get(self, "subjectAltNameInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject"], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfig]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject",
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
class GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject:
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
        :param common_name: The common name of the distinguished name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#common_name GooglePrivatecaCertificateAuthority#common_name}
        :param organization: The organization of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#organization GooglePrivatecaCertificateAuthority#organization}
        :param country_code: The country code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#country_code GooglePrivatecaCertificateAuthority#country_code}
        :param locality: The locality or city of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#locality GooglePrivatecaCertificateAuthority#locality}
        :param organizational_unit: The organizational unit of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#organizational_unit GooglePrivatecaCertificateAuthority#organizational_unit}
        :param postal_code: The postal code of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#postal_code GooglePrivatecaCertificateAuthority#postal_code}
        :param province: The province, territory, or regional state of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#province GooglePrivatecaCertificateAuthority#province}
        :param street_address: The street address of the subject. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#street_address GooglePrivatecaCertificateAuthority#street_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#common_name GooglePrivatecaCertificateAuthority#common_name}
        '''
        result = self._values.get("common_name")
        assert result is not None, "Required property 'common_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''The organization of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#organization GooglePrivatecaCertificateAuthority#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''The country code of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#country_code GooglePrivatecaCertificateAuthority#country_code}
        '''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''The locality or city of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#locality GooglePrivatecaCertificateAuthority#locality}
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''The organizational unit of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#organizational_unit GooglePrivatecaCertificateAuthority#organizational_unit}
        '''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''The postal code of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#postal_code GooglePrivatecaCertificateAuthority#postal_code}
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def province(self) -> typing.Optional[builtins.str]:
        '''The province, territory, or regional state of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#province GooglePrivatecaCertificateAuthority#province}
        '''
        result = self._values.get("province")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[builtins.str]:
        '''The street address of the subject.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#street_address GooglePrivatecaCertificateAuthority#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName",
    jsii_struct_bases=[],
    name_mapping={
        "dns_names": "dnsNames",
        "email_addresses": "emailAddresses",
        "ip_addresses": "ipAddresses",
        "uris": "uris",
    },
)
class GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName:
    def __init__(
        self,
        *,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        email_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param dns_names: Contains only valid, fully-qualified host names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#dns_names GooglePrivatecaCertificateAuthority#dns_names}
        :param email_addresses: Contains only valid RFC 2822 E-mail addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#email_addresses GooglePrivatecaCertificateAuthority#email_addresses}
        :param ip_addresses: Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ip_addresses GooglePrivatecaCertificateAuthority#ip_addresses}
        :param uris: Contains only valid RFC 3986 URIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#uris GooglePrivatecaCertificateAuthority#uris}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#dns_names GooglePrivatecaCertificateAuthority#dns_names}
        '''
        result = self._values.get("dns_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def email_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid RFC 2822 E-mail addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#email_addresses GooglePrivatecaCertificateAuthority#email_addresses}
        '''
        result = self._values.get("email_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid 32-bit IPv4 addresses or RFC 4291 IPv6 addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ip_addresses GooglePrivatecaCertificateAuthority#ip_addresses}
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Contains only valid RFC 3986 URIs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#uris GooglePrivatecaCertificateAuthority#uris}
        '''
        result = self._values.get("uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference, "dns_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsNames", value)

    @builtins.property
    @jsii.member(jsii_name="emailAddresses")
    def email_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emailAddresses"))

    @email_addresses.setter
    def email_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference, "email_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference, "ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference, "uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "country_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="locality")
    def locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locality"))

    @locality.setter
    def locality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "locality").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locality", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "organizational_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "postal_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="province")
    def province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "province"))

    @province.setter
    def province(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "province").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "province", value)

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streetAddress"))

    @street_address.setter
    def street_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "street_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streetAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509Config",
    jsii_struct_bases=[],
    name_mapping={
        "ca_options": "caOptions",
        "key_usage": "keyUsage",
        "additional_extensions": "additionalExtensions",
        "aia_ocsp_servers": "aiaOcspServers",
        "policy_ids": "policyIds",
    },
)
class GooglePrivatecaCertificateAuthorityConfigX509Config:
    def __init__(
        self,
        *,
        ca_options: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions", typing.Dict[str, typing.Any]],
        key_usage: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage", typing.Dict[str, typing.Any]],
        additional_extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions", typing.Dict[str, typing.Any]]]]] = None,
        aia_ocsp_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        policy_ids: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ca_options: ca_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ca_options GooglePrivatecaCertificateAuthority#ca_options}
        :param key_usage: key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_usage GooglePrivatecaCertificateAuthority#key_usage}
        :param additional_extensions: additional_extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#additional_extensions GooglePrivatecaCertificateAuthority#additional_extensions}
        :param aia_ocsp_servers: Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#aia_ocsp_servers GooglePrivatecaCertificateAuthority#aia_ocsp_servers}
        :param policy_ids: policy_ids block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#policy_ids GooglePrivatecaCertificateAuthority#policy_ids}
        '''
        if isinstance(ca_options, dict):
            ca_options = GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions(**ca_options)
        if isinstance(key_usage, dict):
            key_usage = GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage(**key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509Config.__init__)
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
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions":
        '''ca_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ca_options GooglePrivatecaCertificateAuthority#ca_options}
        '''
        result = self._values.get("ca_options")
        assert result is not None, "Required property 'ca_options' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions", result)

    @builtins.property
    def key_usage(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage":
        '''key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_usage GooglePrivatecaCertificateAuthority#key_usage}
        '''
        result = self._values.get("key_usage")
        assert result is not None, "Required property 'key_usage' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage", result)

    @builtins.property
    def additional_extensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions"]]]:
        '''additional_extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#additional_extensions GooglePrivatecaCertificateAuthority#additional_extensions}
        '''
        result = self._values.get("additional_extensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions"]]], result)

    @builtins.property
    def aia_ocsp_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the "Authority Information Access" extension in the certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#aia_ocsp_servers GooglePrivatecaCertificateAuthority#aia_ocsp_servers}
        '''
        result = self._values.get("aia_ocsp_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def policy_ids(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds"]]]:
        '''policy_ids block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#policy_ids GooglePrivatecaCertificateAuthority#policy_ids}
        '''
        result = self._values.get("policy_ids")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions",
    jsii_struct_bases=[],
    name_mapping={"critical": "critical", "object_id": "objectId", "value": "value"},
)
class GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions:
    def __init__(
        self,
        *,
        critical: typing.Union[builtins.bool, cdktf.IResolvable],
        object_id: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId", typing.Dict[str, typing.Any]],
        value: builtins.str,
    ) -> None:
        '''
        :param critical: Indicates whether or not this extension is critical (i.e., if the client does not know how to handle this extension, the client should consider this to be an error). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#critical GooglePrivatecaCertificateAuthority#critical}
        :param object_id: object_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id GooglePrivatecaCertificateAuthority#object_id}
        :param value: The value of this X.509 extension. A base64-encoded string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#value GooglePrivatecaCertificateAuthority#value}
        '''
        if isinstance(object_id, dict):
            object_id = GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId(**object_id)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#critical GooglePrivatecaCertificateAuthority#critical}
        '''
        result = self._values.get("critical")
        assert result is not None, "Required property 'critical' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def object_id(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId":
        '''object_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id GooglePrivatecaCertificateAuthority#object_id}
        '''
        result = self._values.get("object_id")
        assert result is not None, "Required property 'object_id' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId", result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of this X.509 extension. A base64-encoded string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#value GooglePrivatecaCertificateAuthority#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putObjectId")
    def put_object_id(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId(
            object_id_path=object_id_path
        )

        return typing.cast(None, jsii.invoke(self, "putObjectId", [value]))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(
        self,
    ) -> GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference:
        return typing.cast(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference, jsii.get(self, "objectId"))

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
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId], jsii.get(self, "objectIdInput"))

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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference, "critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "critical", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions",
    jsii_struct_bases=[],
    name_mapping={
        "is_ca": "isCa",
        "max_issuer_path_length": "maxIssuerPathLength",
        "non_ca": "nonCa",
        "zero_max_issuer_path_length": "zeroMaxIssuerPathLength",
    },
)
class GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions:
    def __init__(
        self,
        *,
        is_ca: typing.Union[builtins.bool, cdktf.IResolvable],
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
        non_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zero_max_issuer_path_length: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_ca: When true, the "CA" in Basic Constraints extension will be set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#is_ca GooglePrivatecaCertificateAuthority#is_ca}
        :param max_issuer_path_length: Refers to the "path length constraint" in Basic Constraints extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#max_issuer_path_length GooglePrivatecaCertificateAuthority#max_issuer_path_length}
        :param non_ca: When true, the "CA" in Basic Constraints extension will be set to false. If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#non_ca GooglePrivatecaCertificateAuthority#non_ca}
        :param zero_max_issuer_path_length: When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#zero_max_issuer_path_length GooglePrivatecaCertificateAuthority#zero_max_issuer_path_length}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions.__init__)
            check_type(argname="argument is_ca", value=is_ca, expected_type=type_hints["is_ca"])
            check_type(argname="argument max_issuer_path_length", value=max_issuer_path_length, expected_type=type_hints["max_issuer_path_length"])
            check_type(argname="argument non_ca", value=non_ca, expected_type=type_hints["non_ca"])
            check_type(argname="argument zero_max_issuer_path_length", value=zero_max_issuer_path_length, expected_type=type_hints["zero_max_issuer_path_length"])
        self._values: typing.Dict[str, typing.Any] = {
            "is_ca": is_ca,
        }
        if max_issuer_path_length is not None:
            self._values["max_issuer_path_length"] = max_issuer_path_length
        if non_ca is not None:
            self._values["non_ca"] = non_ca
        if zero_max_issuer_path_length is not None:
            self._values["zero_max_issuer_path_length"] = zero_max_issuer_path_length

    @builtins.property
    def is_ca(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''When true, the "CA" in Basic Constraints extension will be set to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#is_ca GooglePrivatecaCertificateAuthority#is_ca}
        '''
        result = self._values.get("is_ca")
        assert result is not None, "Required property 'is_ca' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def max_issuer_path_length(self) -> typing.Optional[jsii.Number]:
        '''Refers to the "path length constraint" in Basic Constraints extension.

        For a CA certificate, this value describes the depth of
        subordinate CA certificates that are allowed. If this value is less than 0, the request will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#max_issuer_path_length GooglePrivatecaCertificateAuthority#max_issuer_path_length}
        '''
        result = self._values.get("max_issuer_path_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def non_ca(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, the "CA" in Basic Constraints extension will be set to false.

        If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#non_ca GooglePrivatecaCertificateAuthority#non_ca}
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#zero_max_issuer_path_length GooglePrivatecaCertificateAuthority#zero_max_issuer_path_length}
        '''
        result = self._values.get("zero_max_issuer_path_length")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, "is_ca").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCa", value)

    @builtins.property
    @jsii.member(jsii_name="maxIssuerPathLength")
    def max_issuer_path_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIssuerPathLength"))

    @max_issuer_path_length.setter
    def max_issuer_path_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, "max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="nonCa")
    def non_ca(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nonCa"))

    @non_ca.setter
    def non_ca(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, "non_ca").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, "zero_max_issuer_path_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zeroMaxIssuerPathLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage",
    jsii_struct_bases=[],
    name_mapping={
        "base_key_usage": "baseKeyUsage",
        "extended_key_usage": "extendedKeyUsage",
        "unknown_extended_key_usages": "unknownExtendedKeyUsages",
    },
)
class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage:
    def __init__(
        self,
        *,
        base_key_usage: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage", typing.Dict[str, typing.Any]],
        extended_key_usage: typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage", typing.Dict[str, typing.Any]],
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#base_key_usage GooglePrivatecaCertificateAuthority#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#extended_key_usage GooglePrivatecaCertificateAuthority#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#unknown_extended_key_usages GooglePrivatecaCertificateAuthority#unknown_extended_key_usages}
        '''
        if isinstance(base_key_usage, dict):
            base_key_usage = GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage(**base_key_usage)
        if isinstance(extended_key_usage, dict):
            extended_key_usage = GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage(**extended_key_usage)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage.__init__)
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
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage":
        '''base_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#base_key_usage GooglePrivatecaCertificateAuthority#base_key_usage}
        '''
        result = self._values.get("base_key_usage")
        assert result is not None, "Required property 'base_key_usage' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage", result)

    @builtins.property
    def extended_key_usage(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage":
        '''extended_key_usage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#extended_key_usage GooglePrivatecaCertificateAuthority#extended_key_usage}
        '''
        result = self._values.get("extended_key_usage")
        assert result is not None, "Required property 'extended_key_usage' is missing"
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage", result)

    @builtins.property
    def unknown_extended_key_usages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]]:
        '''unknown_extended_key_usages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#unknown_extended_key_usages GooglePrivatecaCertificateAuthority#unknown_extended_key_usages}
        '''
        result = self._values.get("unknown_extended_key_usages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage",
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
class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage:
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
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#cert_sign GooglePrivatecaCertificateAuthority#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#content_commitment GooglePrivatecaCertificateAuthority#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#crl_sign GooglePrivatecaCertificateAuthority#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#data_encipherment GooglePrivatecaCertificateAuthority#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#decipher_only GooglePrivatecaCertificateAuthority#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#digital_signature GooglePrivatecaCertificateAuthority#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#encipher_only GooglePrivatecaCertificateAuthority#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_agreement GooglePrivatecaCertificateAuthority#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_encipherment GooglePrivatecaCertificateAuthority#key_encipherment}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#cert_sign GooglePrivatecaCertificateAuthority#cert_sign}
        '''
        result = self._values.get("cert_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def content_commitment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#content_commitment GooglePrivatecaCertificateAuthority#content_commitment}
        '''
        result = self._values.get("content_commitment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def crl_sign(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used sign certificate revocation lists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#crl_sign GooglePrivatecaCertificateAuthority#crl_sign}
        '''
        result = self._values.get("crl_sign")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#data_encipherment GooglePrivatecaCertificateAuthority#data_encipherment}
        '''
        result = self._values.get("data_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def decipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to decipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#decipher_only GooglePrivatecaCertificateAuthority#decipher_only}
        '''
        result = self._values.get("decipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def digital_signature(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used for digital signatures.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#digital_signature GooglePrivatecaCertificateAuthority#digital_signature}
        '''
        result = self._values.get("digital_signature")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encipher_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#encipher_only GooglePrivatecaCertificateAuthority#encipher_only}
        '''
        result = self._values.get("encipher_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_agreement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used in a key agreement protocol.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_agreement GooglePrivatecaCertificateAuthority#key_agreement}
        '''
        result = self._values.get("key_agreement")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_encipherment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The key may be used to encipher other keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_encipherment GooglePrivatecaCertificateAuthority#key_encipherment}
        '''
        result = self._values.get("key_encipherment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "cert_sign").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "content_commitment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentCommitment", value)

    @builtins.property
    @jsii.member(jsii_name="crlSign")
    def crl_sign(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "crlSign"))

    @crl_sign.setter
    def crl_sign(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "crl_sign").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "data_encipherment").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "decipher_only").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "digital_signature").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "encipher_only").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "key_agreement").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "key_encipherment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyEncipherment", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage",
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
class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage:
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
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#client_auth GooglePrivatecaCertificateAuthority#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#code_signing GooglePrivatecaCertificateAuthority#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#email_protection GooglePrivatecaCertificateAuthority#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ocsp_signing GooglePrivatecaCertificateAuthority#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#server_auth GooglePrivatecaCertificateAuthority#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#time_stamping GooglePrivatecaCertificateAuthority#time_stamping}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#client_auth GooglePrivatecaCertificateAuthority#client_auth}
        '''
        result = self._values.get("client_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def code_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#code_signing GooglePrivatecaCertificateAuthority#code_signing}
        '''
        result = self._values.get("code_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def email_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#email_protection GooglePrivatecaCertificateAuthority#email_protection}
        '''
        result = self._values.get("email_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ocsp_signing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ocsp_signing GooglePrivatecaCertificateAuthority#ocsp_signing}
        '''
        result = self._values.get("ocsp_signing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def server_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#server_auth GooglePrivatecaCertificateAuthority#server_auth}
        '''
        result = self._values.get("server_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def time_stamping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#time_stamping GooglePrivatecaCertificateAuthority#time_stamping}
        '''
        result = self._values.get("time_stamping")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "client_auth").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "code_signing").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "email_protection").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "ocsp_signing").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "server_auth").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "time_stamping").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeStamping", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference.__init__)
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
        :param cert_sign: The key may be used to sign certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#cert_sign GooglePrivatecaCertificateAuthority#cert_sign}
        :param content_commitment: The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#content_commitment GooglePrivatecaCertificateAuthority#content_commitment}
        :param crl_sign: The key may be used sign certificate revocation lists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#crl_sign GooglePrivatecaCertificateAuthority#crl_sign}
        :param data_encipherment: The key may be used to encipher data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#data_encipherment GooglePrivatecaCertificateAuthority#data_encipherment}
        :param decipher_only: The key may be used to decipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#decipher_only GooglePrivatecaCertificateAuthority#decipher_only}
        :param digital_signature: The key may be used for digital signatures. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#digital_signature GooglePrivatecaCertificateAuthority#digital_signature}
        :param encipher_only: The key may be used to encipher only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#encipher_only GooglePrivatecaCertificateAuthority#encipher_only}
        :param key_agreement: The key may be used in a key agreement protocol. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_agreement GooglePrivatecaCertificateAuthority#key_agreement}
        :param key_encipherment: The key may be used to encipher other keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#key_encipherment GooglePrivatecaCertificateAuthority#key_encipherment}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage(
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
        :param client_auth: Corresponds to OID 1.3.6.1.5.5.7.3.2. Officially described as "TLS WWW client authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#client_auth GooglePrivatecaCertificateAuthority#client_auth}
        :param code_signing: Corresponds to OID 1.3.6.1.5.5.7.3.3. Officially described as "Signing of downloadable executable code client authentication". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#code_signing GooglePrivatecaCertificateAuthority#code_signing}
        :param email_protection: Corresponds to OID 1.3.6.1.5.5.7.3.4. Officially described as "Email protection". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#email_protection GooglePrivatecaCertificateAuthority#email_protection}
        :param ocsp_signing: Corresponds to OID 1.3.6.1.5.5.7.3.9. Officially described as "Signing OCSP responses". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#ocsp_signing GooglePrivatecaCertificateAuthority#ocsp_signing}
        :param server_auth: Corresponds to OID 1.3.6.1.5.5.7.3.1. Officially described as "TLS WWW server authentication", though regularly used for non-WWW TLS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#server_auth GooglePrivatecaCertificateAuthority#server_auth}
        :param time_stamping: Corresponds to OID 1.3.6.1.5.5.7.3.8. Officially described as "Binding the hash of an object to a time". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#time_stamping GooglePrivatecaCertificateAuthority#time_stamping}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage(
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference.put_unknown_extended_key_usages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUnknownExtendedKeyUsages", [value]))

    @jsii.member(jsii_name="resetUnknownExtendedKeyUsages")
    def reset_unknown_extended_key_usages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnknownExtendedKeyUsages", []))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsage")
    def base_key_usage(
        self,
    ) -> GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference, jsii.get(self, "baseKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsage")
    def extended_key_usage(
        self,
    ) -> GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference, jsii.get(self, "extendedKeyUsage"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsages")
    def unknown_extended_key_usages(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList", jsii.get(self, "unknownExtendedKeyUsages"))

    @builtins.property
    @jsii.member(jsii_name="baseKeyUsageInput")
    def base_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage], jsii.get(self, "baseKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedKeyUsageInput")
    def extended_key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage], jsii.get(self, "extendedKeyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="unknownExtendedKeyUsagesInput")
    def unknown_extended_key_usages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages"]]], jsii.get(self, "unknownExtendedKeyUsagesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalExtensions")
    def put_additional_extensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference.put_additional_extensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalExtensions", [value]))

    @jsii.member(jsii_name="putCaOptions")
    def put_ca_options(
        self,
        *,
        is_ca: typing.Union[builtins.bool, cdktf.IResolvable],
        max_issuer_path_length: typing.Optional[jsii.Number] = None,
        non_ca: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zero_max_issuer_path_length: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param is_ca: When true, the "CA" in Basic Constraints extension will be set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#is_ca GooglePrivatecaCertificateAuthority#is_ca}
        :param max_issuer_path_length: Refers to the "path length constraint" in Basic Constraints extension. For a CA certificate, this value describes the depth of subordinate CA certificates that are allowed. If this value is less than 0, the request will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#max_issuer_path_length GooglePrivatecaCertificateAuthority#max_issuer_path_length}
        :param non_ca: When true, the "CA" in Basic Constraints extension will be set to false. If both 'is_ca' and 'non_ca' are unset, the extension will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#non_ca GooglePrivatecaCertificateAuthority#non_ca}
        :param zero_max_issuer_path_length: When true, the "path length constraint" in Basic Constraints extension will be set to 0. if both 'max_issuer_path_length' and 'zero_max_issuer_path_length' are unset, the max path length will be omitted from the CA certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#zero_max_issuer_path_length GooglePrivatecaCertificateAuthority#zero_max_issuer_path_length}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions(
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
        base_key_usage: typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage, typing.Dict[str, typing.Any]],
        extended_key_usage: typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage, typing.Dict[str, typing.Any]],
        unknown_extended_key_usages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param base_key_usage: base_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#base_key_usage GooglePrivatecaCertificateAuthority#base_key_usage}
        :param extended_key_usage: extended_key_usage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#extended_key_usage GooglePrivatecaCertificateAuthority#extended_key_usage}
        :param unknown_extended_key_usages: unknown_extended_key_usages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#unknown_extended_key_usages GooglePrivatecaCertificateAuthority#unknown_extended_key_usages}
        '''
        value = GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage(
            base_key_usage=base_key_usage,
            extended_key_usage=extended_key_usage,
            unknown_extended_key_usages=unknown_extended_key_usages,
        )

        return typing.cast(None, jsii.invoke(self, "putKeyUsage", [value]))

    @jsii.member(jsii_name="putPolicyIds")
    def put_policy_ids(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference.put_policy_ids)
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
    ) -> GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList:
        return typing.cast(GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList, jsii.get(self, "additionalExtensions"))

    @builtins.property
    @jsii.member(jsii_name="caOptions")
    def ca_options(
        self,
    ) -> GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference:
        return typing.cast(GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference, jsii.get(self, "caOptions"))

    @builtins.property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(
        self,
    ) -> GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference:
        return typing.cast(GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference, jsii.get(self, "keyUsage"))

    @builtins.property
    @jsii.member(jsii_name="policyIds")
    def policy_ids(
        self,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList":
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList", jsii.get(self, "policyIds"))

    @builtins.property
    @jsii.member(jsii_name="additionalExtensionsInput")
    def additional_extensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions]]], jsii.get(self, "additionalExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServersInput")
    def aia_ocsp_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aiaOcspServersInput"))

    @builtins.property
    @jsii.member(jsii_name="caOptionsInput")
    def ca_options_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions], jsii.get(self, "caOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUsageInput")
    def key_usage_input(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage], jsii.get(self, "keyUsageInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdsInput")
    def policy_ids_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds"]]], jsii.get(self, "policyIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="aiaOcspServers")
    def aia_ocsp_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aiaOcspServers"))

    @aia_ocsp_servers.setter
    def aia_ocsp_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference, "aia_ocsp_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiaOcspServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509Config]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509Config], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityConfigX509Config],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds",
    jsii_struct_bases=[],
    name_mapping={"object_id_path": "objectIdPath"},
)
class GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds:
    def __init__(self, *, object_id_path: typing.Sequence[jsii.Number]) -> None:
        '''
        :param object_id_path: An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds.__init__)
            check_type(argname="argument object_id_path", value=object_id_path, expected_type=type_hints["object_id_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_id_path": object_id_path,
        }

    @builtins.property
    def object_id_path(self) -> typing.List[jsii.Number]:
        '''An ObjectId specifies an object identifier (OID). These provide context and describe types in ASN.1 messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#object_id_path GooglePrivatecaCertificateAuthority#object_id_path}
        '''
        result = self._values.get("object_id_path")
        assert result is not None, "Required property 'object_id_path' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference, "object_id_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectIdPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityKeySpec",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "cloud_kms_key_version": "cloudKmsKeyVersion",
    },
)
class GooglePrivatecaCertificateAuthorityKeySpec:
    def __init__(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        cloud_kms_key_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param algorithm: The algorithm to use for creating a managed Cloud KMS key for a for a simplified experience. All managed keys will be have their ProtectionLevel as HSM. Possible values: ["SIGN_HASH_ALGORITHM_UNSPECIFIED", "RSA_PSS_2048_SHA256", "RSA_PSS_3072_SHA256", "RSA_PSS_4096_SHA256", "RSA_PKCS1_2048_SHA256", "RSA_PKCS1_3072_SHA256", "RSA_PKCS1_4096_SHA256", "EC_P256_SHA256", "EC_P384_SHA384"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#algorithm GooglePrivatecaCertificateAuthority#algorithm}
        :param cloud_kms_key_version: The resource name for an existing Cloud KMS CryptoKeyVersion in the format 'projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#cloud_kms_key_version GooglePrivatecaCertificateAuthority#cloud_kms_key_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityKeySpec.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument cloud_kms_key_version", value=cloud_kms_key_version, expected_type=type_hints["cloud_kms_key_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if cloud_kms_key_version is not None:
            self._values["cloud_kms_key_version"] = cloud_kms_key_version

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        '''The algorithm to use for creating a managed Cloud KMS key for a for a simplified experience.

        All managed keys will be have their ProtectionLevel as HSM. Possible values: ["SIGN_HASH_ALGORITHM_UNSPECIFIED", "RSA_PSS_2048_SHA256", "RSA_PSS_3072_SHA256", "RSA_PSS_4096_SHA256", "RSA_PKCS1_2048_SHA256", "RSA_PKCS1_3072_SHA256", "RSA_PKCS1_4096_SHA256", "EC_P256_SHA256", "EC_P384_SHA384"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#algorithm GooglePrivatecaCertificateAuthority#algorithm}
        '''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_kms_key_version(self) -> typing.Optional[builtins.str]:
        '''The resource name for an existing Cloud KMS CryptoKeyVersion in the format 'projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#cloud_kms_key_version GooglePrivatecaCertificateAuthority#cloud_kms_key_version}
        '''
        result = self._values.get("cloud_kms_key_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityKeySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityKeySpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityKeySpecOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityKeySpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetCloudKmsKeyVersion")
    def reset_cloud_kms_key_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudKmsKeyVersion", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudKmsKeyVersionInput")
    def cloud_kms_key_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudKmsKeyVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityKeySpecOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="cloudKmsKeyVersion")
    def cloud_kms_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudKmsKeyVersion"))

    @cloud_kms_key_version.setter
    def cloud_kms_key_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityKeySpecOutputReference, "cloud_kms_key_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudKmsKeyVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthorityKeySpec]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthorityKeySpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthorityKeySpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityKeySpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthoritySubordinateConfig",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority": "certificateAuthority",
        "pem_issuer_chain": "pemIssuerChain",
    },
)
class GooglePrivatecaCertificateAuthoritySubordinateConfig:
    def __init__(
        self,
        *,
        certificate_authority: typing.Optional[builtins.str] = None,
        pem_issuer_chain: typing.Optional[typing.Union["GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate_authority: This can refer to a CertificateAuthority that was used to create a subordinate CertificateAuthority. This field is used for information and usability purposes only. The resource name is in the format 'projects/*/locations/*/caPools/*/certificateAuthorities/*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#certificate_authority GooglePrivatecaCertificateAuthority#certificate_authority}
        :param pem_issuer_chain: pem_issuer_chain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_issuer_chain GooglePrivatecaCertificateAuthority#pem_issuer_chain}
        '''
        if isinstance(pem_issuer_chain, dict):
            pem_issuer_chain = GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain(**pem_issuer_chain)
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthoritySubordinateConfig.__init__)
            check_type(argname="argument certificate_authority", value=certificate_authority, expected_type=type_hints["certificate_authority"])
            check_type(argname="argument pem_issuer_chain", value=pem_issuer_chain, expected_type=type_hints["pem_issuer_chain"])
        self._values: typing.Dict[str, typing.Any] = {}
        if certificate_authority is not None:
            self._values["certificate_authority"] = certificate_authority
        if pem_issuer_chain is not None:
            self._values["pem_issuer_chain"] = pem_issuer_chain

    @builtins.property
    def certificate_authority(self) -> typing.Optional[builtins.str]:
        '''This can refer to a CertificateAuthority that was used to create a subordinate CertificateAuthority.

        This field is used for information
        and usability purposes only. The resource name is in the format
        'projects/*/locations/*/caPools/*/certificateAuthorities/*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#certificate_authority GooglePrivatecaCertificateAuthority#certificate_authority}
        '''
        result = self._values.get("certificate_authority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_issuer_chain(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain"]:
        '''pem_issuer_chain block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_issuer_chain GooglePrivatecaCertificateAuthority#pem_issuer_chain}
        '''
        result = self._values.get("pem_issuer_chain")
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthoritySubordinateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPemIssuerChain")
    def put_pem_issuer_chain(
        self,
        *,
        pem_certificates: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param pem_certificates: Expected to be in leaf-to-root order according to RFC 5246. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_certificates GooglePrivatecaCertificateAuthority#pem_certificates}
        '''
        value = GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain(
            pem_certificates=pem_certificates
        )

        return typing.cast(None, jsii.invoke(self, "putPemIssuerChain", [value]))

    @jsii.member(jsii_name="resetCertificateAuthority")
    def reset_certificate_authority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateAuthority", []))

    @jsii.member(jsii_name="resetPemIssuerChain")
    def reset_pem_issuer_chain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemIssuerChain", []))

    @builtins.property
    @jsii.member(jsii_name="pemIssuerChain")
    def pem_issuer_chain(
        self,
    ) -> "GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference":
        return typing.cast("GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference", jsii.get(self, "pemIssuerChain"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityInput")
    def certificate_authority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityInput"))

    @builtins.property
    @jsii.member(jsii_name="pemIssuerChainInput")
    def pem_issuer_chain_input(
        self,
    ) -> typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain"]:
        return typing.cast(typing.Optional["GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain"], jsii.get(self, "pemIssuerChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthority")
    def certificate_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthority"))

    @certificate_authority.setter
    def certificate_authority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference, "certificate_authority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthoritySubordinateConfig]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthoritySubordinateConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthoritySubordinateConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain",
    jsii_struct_bases=[],
    name_mapping={"pem_certificates": "pemCertificates"},
)
class GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain:
    def __init__(
        self,
        *,
        pem_certificates: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param pem_certificates: Expected to be in leaf-to-root order according to RFC 5246. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_certificates GooglePrivatecaCertificateAuthority#pem_certificates}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain.__init__)
            check_type(argname="argument pem_certificates", value=pem_certificates, expected_type=type_hints["pem_certificates"])
        self._values: typing.Dict[str, typing.Any] = {}
        if pem_certificates is not None:
            self._values["pem_certificates"] = pem_certificates

    @builtins.property
    def pem_certificates(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Expected to be in leaf-to-root order according to RFC 5246.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#pem_certificates GooglePrivatecaCertificateAuthority#pem_certificates}
        '''
        result = self._values.get("pem_certificates")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPemCertificates")
    def reset_pem_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemCertificates", []))

    @builtins.property
    @jsii.member(jsii_name="pemCertificatesInput")
    def pem_certificates_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pemCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="pemCertificates")
    def pem_certificates(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemCertificates"))

    @pem_certificates.setter
    def pem_certificates(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference, "pem_certificates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemCertificates", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain]:
        return typing.cast(typing.Optional[GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GooglePrivatecaCertificateAuthorityTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#create GooglePrivatecaCertificateAuthority#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#delete GooglePrivatecaCertificateAuthority#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#update GooglePrivatecaCertificateAuthority#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#create GooglePrivatecaCertificateAuthority#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#delete GooglePrivatecaCertificateAuthority#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_privateca_certificate_authority#update GooglePrivatecaCertificateAuthority#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GooglePrivatecaCertificateAuthorityTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GooglePrivatecaCertificateAuthorityTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googlePrivatecaCertificateAuthority.GooglePrivatecaCertificateAuthorityTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GooglePrivatecaCertificateAuthorityTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GooglePrivatecaCertificateAuthorityTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GooglePrivatecaCertificateAuthorityTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GooglePrivatecaCertificateAuthority",
    "GooglePrivatecaCertificateAuthorityAccessUrls",
    "GooglePrivatecaCertificateAuthorityAccessUrlsList",
    "GooglePrivatecaCertificateAuthorityAccessUrlsOutputReference",
    "GooglePrivatecaCertificateAuthorityConfig",
    "GooglePrivatecaCertificateAuthorityConfigA",
    "GooglePrivatecaCertificateAuthorityConfigAOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigSubjectConfig",
    "GooglePrivatecaCertificateAuthorityConfigSubjectConfigOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubject",
    "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltName",
    "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectAltNameOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigSubjectConfigSubjectOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509Config",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensions",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsList",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectId",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsObjectIdOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigAdditionalExtensionsOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptions",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigCaOptionsOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsage",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsage",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageBaseKeyUsageOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsage",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageExtendedKeyUsageOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsages",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesList",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigKeyUsageUnknownExtendedKeyUsagesOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigOutputReference",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIds",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsList",
    "GooglePrivatecaCertificateAuthorityConfigX509ConfigPolicyIdsOutputReference",
    "GooglePrivatecaCertificateAuthorityKeySpec",
    "GooglePrivatecaCertificateAuthorityKeySpecOutputReference",
    "GooglePrivatecaCertificateAuthoritySubordinateConfig",
    "GooglePrivatecaCertificateAuthoritySubordinateConfigOutputReference",
    "GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChain",
    "GooglePrivatecaCertificateAuthoritySubordinateConfigPemIssuerChainOutputReference",
    "GooglePrivatecaCertificateAuthorityTimeouts",
    "GooglePrivatecaCertificateAuthorityTimeoutsOutputReference",
]

publication.publish()
