'''
# `tls_self_signed_cert`

Refer to the Terraform Registory for docs: [`tls_self_signed_cert`](https://www.terraform.io/docs/providers/tls/r/self_signed_cert).
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


class SelfSignedCert(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tls.selfSignedCert.SelfSignedCert",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert tls_self_signed_cert}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allowed_uses: typing.Sequence[builtins.str],
        private_key_pem: builtins.str,
        validity_period_hours: jsii.Number,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        early_renewal_hours: typing.Optional[jsii.Number] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        is_ca_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        set_authority_key_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        set_subject_key_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subject: typing.Optional[typing.Union["SelfSignedCertSubject", typing.Dict[str, typing.Any]]] = None,
        uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert tls_self_signed_cert} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param allowed_uses: List of key usages allowed for the issued certificate. Values are defined in `RFC 5280 <https://datatracker.ietf.org/doc/html/rfc5280>`_ and combine flags defined by both `Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3>`_ and `Extended Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_. Accepted values: ``any_extended``, ``cert_signing``, ``client_auth``, ``code_signing``, ``content_commitment``, ``crl_signing``, ``data_encipherment``, ``decipher_only``, ``digital_signature``, ``email_protection``, ``encipher_only``, ``ipsec_end_system``, ``ipsec_tunnel``, ``ipsec_user``, ``key_agreement``, ``key_encipherment``, ``microsoft_commercial_code_signing``, ``microsoft_kernel_code_signing``, ``microsoft_server_gated_crypto``, ``netscape_server_gated_crypto``, ``ocsp_signing``, ``server_auth``, ``timestamping``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#allowed_uses SelfSignedCert#allowed_uses}
        :param private_key_pem: Private key in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format, that the certificate will belong to. This can be read from a separate file using the ```file`` <https://www.terraform.io/language/functions/file>`_ interpolation function. Only an irreversible secure hash of the private key will be stored in the Terraform state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#private_key_pem SelfSignedCert#private_key_pem}
        :param validity_period_hours: Number of hours, after initial issuing, that the certificate will remain valid for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#validity_period_hours SelfSignedCert#validity_period_hours}
        :param dns_names: List of DNS names for which a certificate is being requested (i.e. certificate subjects). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#dns_names SelfSignedCert#dns_names}
        :param early_renewal_hours: The resource will consider the certificate to have expired the given number of hours before its actual expiry time. This can be useful to deploy an updated certificate in advance of the expiration of the current certificate. However, the old certificate remains valid until its true expiration time, since this resource does not (and cannot) support certificate revocation. Also, this advance update can only be performed should the Terraform configuration be applied during the early renewal period. (default: ``0``) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#early_renewal_hours SelfSignedCert#early_renewal_hours}
        :param ip_addresses: List of IP addresses for which a certificate is being requested (i.e. certificate subjects). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#ip_addresses SelfSignedCert#ip_addresses}
        :param is_ca_certificate: Is the generated certificate representing a Certificate Authority (CA) (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#is_ca_certificate SelfSignedCert#is_ca_certificate}
        :param set_authority_key_id: Should the generated certificate include an `authority key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1>`_: for self-signed certificates this is the same value as the `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#set_authority_key_id SelfSignedCert#set_authority_key_id}
        :param set_subject_key_id: Should the generated certificate include a `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#set_subject_key_id SelfSignedCert#set_subject_key_id}
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#subject SelfSignedCert#subject}
        :param uris: List of URIs for which a certificate is being requested (i.e. certificate subjects). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#uris SelfSignedCert#uris}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SelfSignedCert.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SelfSignedCertConfig(
            allowed_uses=allowed_uses,
            private_key_pem=private_key_pem,
            validity_period_hours=validity_period_hours,
            dns_names=dns_names,
            early_renewal_hours=early_renewal_hours,
            ip_addresses=ip_addresses,
            is_ca_certificate=is_ca_certificate,
            set_authority_key_id=set_authority_key_id,
            set_subject_key_id=set_subject_key_id,
            subject=subject,
            uris=uris,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putSubject")
    def put_subject(
        self,
        *,
        common_name: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        province: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param common_name: Distinguished name: ``CN``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#common_name SelfSignedCert#common_name}
        :param country: Distinguished name: ``C``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#country SelfSignedCert#country}
        :param locality: Distinguished name: ``L``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#locality SelfSignedCert#locality}
        :param organization: Distinguished name: ``O``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#organization SelfSignedCert#organization}
        :param organizational_unit: Distinguished name: ``OU``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#organizational_unit SelfSignedCert#organizational_unit}
        :param postal_code: Distinguished name: ``PC``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#postal_code SelfSignedCert#postal_code}
        :param province: Distinguished name: ``ST``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#province SelfSignedCert#province}
        :param serial_number: Distinguished name: ``SERIALNUMBER``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#serial_number SelfSignedCert#serial_number}
        :param street_address: Distinguished name: ``STREET``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#street_address SelfSignedCert#street_address}
        '''
        value = SelfSignedCertSubject(
            common_name=common_name,
            country=country,
            locality=locality,
            organization=organization,
            organizational_unit=organizational_unit,
            postal_code=postal_code,
            province=province,
            serial_number=serial_number,
            street_address=street_address,
        )

        return typing.cast(None, jsii.invoke(self, "putSubject", [value]))

    @jsii.member(jsii_name="resetDnsNames")
    def reset_dns_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsNames", []))

    @jsii.member(jsii_name="resetEarlyRenewalHours")
    def reset_early_renewal_hours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEarlyRenewalHours", []))

    @jsii.member(jsii_name="resetIpAddresses")
    def reset_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddresses", []))

    @jsii.member(jsii_name="resetIsCaCertificate")
    def reset_is_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsCaCertificate", []))

    @jsii.member(jsii_name="resetSetAuthorityKeyId")
    def reset_set_authority_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetAuthorityKeyId", []))

    @jsii.member(jsii_name="resetSetSubjectKeyId")
    def reset_set_subject_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetSubjectKeyId", []))

    @jsii.member(jsii_name="resetSubject")
    def reset_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubject", []))

    @jsii.member(jsii_name="resetUris")
    def reset_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUris", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="certPem")
    def cert_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certPem"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="keyAlgorithm")
    def key_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyAlgorithm"))

    @builtins.property
    @jsii.member(jsii_name="readyForRenewal")
    def ready_for_renewal(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "readyForRenewal"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> "SelfSignedCertSubjectOutputReference":
        return typing.cast("SelfSignedCertSubjectOutputReference", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="validityEndTime")
    def validity_end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validityEndTime"))

    @builtins.property
    @jsii.member(jsii_name="validityStartTime")
    def validity_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validityStartTime"))

    @builtins.property
    @jsii.member(jsii_name="allowedUsesInput")
    def allowed_uses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedUsesInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNamesInput")
    def dns_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="earlyRenewalHoursInput")
    def early_renewal_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "earlyRenewalHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressesInput")
    def ip_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="isCaCertificateInput")
    def is_ca_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isCaCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyPemInput")
    def private_key_pem_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyPemInput"))

    @builtins.property
    @jsii.member(jsii_name="setAuthorityKeyIdInput")
    def set_authority_key_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "setAuthorityKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="setSubjectKeyIdInput")
    def set_subject_key_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "setSubjectKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional["SelfSignedCertSubject"]:
        return typing.cast(typing.Optional["SelfSignedCertSubject"], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="urisInput")
    def uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "urisInput"))

    @builtins.property
    @jsii.member(jsii_name="validityPeriodHoursInput")
    def validity_period_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "validityPeriodHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUses")
    def allowed_uses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedUses"))

    @allowed_uses.setter
    def allowed_uses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "allowed_uses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUses", value)

    @builtins.property
    @jsii.member(jsii_name="dnsNames")
    def dns_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsNames"))

    @dns_names.setter
    def dns_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "dns_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsNames", value)

    @builtins.property
    @jsii.member(jsii_name="earlyRenewalHours")
    def early_renewal_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "earlyRenewalHours"))

    @early_renewal_hours.setter
    def early_renewal_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "early_renewal_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "earlyRenewalHours", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddresses")
    def ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipAddresses"))

    @ip_addresses.setter
    def ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="isCaCertificate")
    def is_ca_certificate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isCaCertificate"))

    @is_ca_certificate.setter
    def is_ca_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "is_ca_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCaCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyPem")
    def private_key_pem(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyPem"))

    @private_key_pem.setter
    def private_key_pem(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "private_key_pem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyPem", value)

    @builtins.property
    @jsii.member(jsii_name="setAuthorityKeyId")
    def set_authority_key_id(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "setAuthorityKeyId"))

    @set_authority_key_id.setter
    def set_authority_key_id(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "set_authority_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setAuthorityKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="setSubjectKeyId")
    def set_subject_key_id(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "setSubjectKeyId"))

    @set_subject_key_id.setter
    def set_subject_key_id(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "set_subject_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setSubjectKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="uris")
    def uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "uris"))

    @uris.setter
    def uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uris", value)

    @builtins.property
    @jsii.member(jsii_name="validityPeriodHours")
    def validity_period_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "validityPeriodHours"))

    @validity_period_hours.setter
    def validity_period_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCert, "validity_period_hours").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validityPeriodHours", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tls.selfSignedCert.SelfSignedCertConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "allowed_uses": "allowedUses",
        "private_key_pem": "privateKeyPem",
        "validity_period_hours": "validityPeriodHours",
        "dns_names": "dnsNames",
        "early_renewal_hours": "earlyRenewalHours",
        "ip_addresses": "ipAddresses",
        "is_ca_certificate": "isCaCertificate",
        "set_authority_key_id": "setAuthorityKeyId",
        "set_subject_key_id": "setSubjectKeyId",
        "subject": "subject",
        "uris": "uris",
    },
)
class SelfSignedCertConfig(cdktf.TerraformMetaArguments):
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
        allowed_uses: typing.Sequence[builtins.str],
        private_key_pem: builtins.str,
        validity_period_hours: jsii.Number,
        dns_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        early_renewal_hours: typing.Optional[jsii.Number] = None,
        ip_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        is_ca_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        set_authority_key_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        set_subject_key_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subject: typing.Optional[typing.Union["SelfSignedCertSubject", typing.Dict[str, typing.Any]]] = None,
        uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param allowed_uses: List of key usages allowed for the issued certificate. Values are defined in `RFC 5280 <https://datatracker.ietf.org/doc/html/rfc5280>`_ and combine flags defined by both `Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3>`_ and `Extended Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_. Accepted values: ``any_extended``, ``cert_signing``, ``client_auth``, ``code_signing``, ``content_commitment``, ``crl_signing``, ``data_encipherment``, ``decipher_only``, ``digital_signature``, ``email_protection``, ``encipher_only``, ``ipsec_end_system``, ``ipsec_tunnel``, ``ipsec_user``, ``key_agreement``, ``key_encipherment``, ``microsoft_commercial_code_signing``, ``microsoft_kernel_code_signing``, ``microsoft_server_gated_crypto``, ``netscape_server_gated_crypto``, ``ocsp_signing``, ``server_auth``, ``timestamping``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#allowed_uses SelfSignedCert#allowed_uses}
        :param private_key_pem: Private key in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format, that the certificate will belong to. This can be read from a separate file using the ```file`` <https://www.terraform.io/language/functions/file>`_ interpolation function. Only an irreversible secure hash of the private key will be stored in the Terraform state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#private_key_pem SelfSignedCert#private_key_pem}
        :param validity_period_hours: Number of hours, after initial issuing, that the certificate will remain valid for. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#validity_period_hours SelfSignedCert#validity_period_hours}
        :param dns_names: List of DNS names for which a certificate is being requested (i.e. certificate subjects). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#dns_names SelfSignedCert#dns_names}
        :param early_renewal_hours: The resource will consider the certificate to have expired the given number of hours before its actual expiry time. This can be useful to deploy an updated certificate in advance of the expiration of the current certificate. However, the old certificate remains valid until its true expiration time, since this resource does not (and cannot) support certificate revocation. Also, this advance update can only be performed should the Terraform configuration be applied during the early renewal period. (default: ``0``) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#early_renewal_hours SelfSignedCert#early_renewal_hours}
        :param ip_addresses: List of IP addresses for which a certificate is being requested (i.e. certificate subjects). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#ip_addresses SelfSignedCert#ip_addresses}
        :param is_ca_certificate: Is the generated certificate representing a Certificate Authority (CA) (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#is_ca_certificate SelfSignedCert#is_ca_certificate}
        :param set_authority_key_id: Should the generated certificate include an `authority key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1>`_: for self-signed certificates this is the same value as the `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#set_authority_key_id SelfSignedCert#set_authority_key_id}
        :param set_subject_key_id: Should the generated certificate include a `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#set_subject_key_id SelfSignedCert#set_subject_key_id}
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#subject SelfSignedCert#subject}
        :param uris: List of URIs for which a certificate is being requested (i.e. certificate subjects). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#uris SelfSignedCert#uris}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(subject, dict):
            subject = SelfSignedCertSubject(**subject)
        if __debug__:
            type_hints = typing.get_type_hints(SelfSignedCertConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument allowed_uses", value=allowed_uses, expected_type=type_hints["allowed_uses"])
            check_type(argname="argument private_key_pem", value=private_key_pem, expected_type=type_hints["private_key_pem"])
            check_type(argname="argument validity_period_hours", value=validity_period_hours, expected_type=type_hints["validity_period_hours"])
            check_type(argname="argument dns_names", value=dns_names, expected_type=type_hints["dns_names"])
            check_type(argname="argument early_renewal_hours", value=early_renewal_hours, expected_type=type_hints["early_renewal_hours"])
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=type_hints["ip_addresses"])
            check_type(argname="argument is_ca_certificate", value=is_ca_certificate, expected_type=type_hints["is_ca_certificate"])
            check_type(argname="argument set_authority_key_id", value=set_authority_key_id, expected_type=type_hints["set_authority_key_id"])
            check_type(argname="argument set_subject_key_id", value=set_subject_key_id, expected_type=type_hints["set_subject_key_id"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument uris", value=uris, expected_type=type_hints["uris"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_uses": allowed_uses,
            "private_key_pem": private_key_pem,
            "validity_period_hours": validity_period_hours,
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
        if dns_names is not None:
            self._values["dns_names"] = dns_names
        if early_renewal_hours is not None:
            self._values["early_renewal_hours"] = early_renewal_hours
        if ip_addresses is not None:
            self._values["ip_addresses"] = ip_addresses
        if is_ca_certificate is not None:
            self._values["is_ca_certificate"] = is_ca_certificate
        if set_authority_key_id is not None:
            self._values["set_authority_key_id"] = set_authority_key_id
        if set_subject_key_id is not None:
            self._values["set_subject_key_id"] = set_subject_key_id
        if subject is not None:
            self._values["subject"] = subject
        if uris is not None:
            self._values["uris"] = uris

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
    def allowed_uses(self) -> typing.List[builtins.str]:
        '''List of key usages allowed for the issued certificate.

        Values are defined in `RFC 5280 <https://datatracker.ietf.org/doc/html/rfc5280>`_ and combine flags defined by both `Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3>`_ and `Extended Key Usages <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_. Accepted values: ``any_extended``, ``cert_signing``, ``client_auth``, ``code_signing``, ``content_commitment``, ``crl_signing``, ``data_encipherment``, ``decipher_only``, ``digital_signature``, ``email_protection``, ``encipher_only``, ``ipsec_end_system``, ``ipsec_tunnel``, ``ipsec_user``, ``key_agreement``, ``key_encipherment``, ``microsoft_commercial_code_signing``, ``microsoft_kernel_code_signing``, ``microsoft_server_gated_crypto``, ``netscape_server_gated_crypto``, ``ocsp_signing``, ``server_auth``, ``timestamping``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#allowed_uses SelfSignedCert#allowed_uses}
        '''
        result = self._values.get("allowed_uses")
        assert result is not None, "Required property 'allowed_uses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def private_key_pem(self) -> builtins.str:
        '''Private key in `PEM (RFC 1421) <https://datatracker.ietf.org/doc/html/rfc1421>`_ format, that the certificate will belong to. This can be read from a separate file using the ```file`` <https://www.terraform.io/language/functions/file>`_ interpolation function. Only an irreversible secure hash of the private key will be stored in the Terraform state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#private_key_pem SelfSignedCert#private_key_pem}
        '''
        result = self._values.get("private_key_pem")
        assert result is not None, "Required property 'private_key_pem' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity_period_hours(self) -> jsii.Number:
        '''Number of hours, after initial issuing, that the certificate will remain valid for.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#validity_period_hours SelfSignedCert#validity_period_hours}
        '''
        result = self._values.get("validity_period_hours")
        assert result is not None, "Required property 'validity_period_hours' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dns_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of DNS names for which a certificate is being requested (i.e. certificate subjects).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#dns_names SelfSignedCert#dns_names}
        '''
        result = self._values.get("dns_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def early_renewal_hours(self) -> typing.Optional[jsii.Number]:
        '''The resource will consider the certificate to have expired the given number of hours before its actual expiry time.

        This can be useful to deploy an updated certificate in advance of the expiration of the current certificate. However, the old certificate remains valid until its true expiration time, since this resource does not (and cannot) support certificate revocation. Also, this advance update can only be performed should the Terraform configuration be applied during the early renewal period. (default: ``0``)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#early_renewal_hours SelfSignedCert#early_renewal_hours}
        '''
        result = self._values.get("early_renewal_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ip_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IP addresses for which a certificate is being requested (i.e. certificate subjects).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#ip_addresses SelfSignedCert#ip_addresses}
        '''
        result = self._values.get("ip_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def is_ca_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Is the generated certificate representing a Certificate Authority (CA) (default: ``false``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#is_ca_certificate SelfSignedCert#is_ca_certificate}
        '''
        result = self._values.get("is_ca_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def set_authority_key_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the generated certificate include an `authority key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1>`_: for self-signed certificates this is the same value as the `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#set_authority_key_id SelfSignedCert#set_authority_key_id}
        '''
        result = self._values.get("set_authority_key_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def set_subject_key_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the generated certificate include a `subject key identifier <https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2>`_ (default: ``false``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#set_subject_key_id SelfSignedCert#set_subject_key_id}
        '''
        result = self._values.get("set_subject_key_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subject(self) -> typing.Optional["SelfSignedCertSubject"]:
        '''subject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#subject SelfSignedCert#subject}
        '''
        result = self._values.get("subject")
        return typing.cast(typing.Optional["SelfSignedCertSubject"], result)

    @builtins.property
    def uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of URIs for which a certificate is being requested (i.e. certificate subjects).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#uris SelfSignedCert#uris}
        '''
        result = self._values.get("uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SelfSignedCertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-tls.selfSignedCert.SelfSignedCertSubject",
    jsii_struct_bases=[],
    name_mapping={
        "common_name": "commonName",
        "country": "country",
        "locality": "locality",
        "organization": "organization",
        "organizational_unit": "organizationalUnit",
        "postal_code": "postalCode",
        "province": "province",
        "serial_number": "serialNumber",
        "street_address": "streetAddress",
    },
)
class SelfSignedCertSubject:
    def __init__(
        self,
        *,
        common_name: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        locality: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        organizational_unit: typing.Optional[builtins.str] = None,
        postal_code: typing.Optional[builtins.str] = None,
        province: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        street_address: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param common_name: Distinguished name: ``CN``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#common_name SelfSignedCert#common_name}
        :param country: Distinguished name: ``C``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#country SelfSignedCert#country}
        :param locality: Distinguished name: ``L``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#locality SelfSignedCert#locality}
        :param organization: Distinguished name: ``O``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#organization SelfSignedCert#organization}
        :param organizational_unit: Distinguished name: ``OU``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#organizational_unit SelfSignedCert#organizational_unit}
        :param postal_code: Distinguished name: ``PC``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#postal_code SelfSignedCert#postal_code}
        :param province: Distinguished name: ``ST``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#province SelfSignedCert#province}
        :param serial_number: Distinguished name: ``SERIALNUMBER``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#serial_number SelfSignedCert#serial_number}
        :param street_address: Distinguished name: ``STREET``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#street_address SelfSignedCert#street_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SelfSignedCertSubject.__init__)
            check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
            check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
            check_type(argname="argument province", value=province, expected_type=type_hints["province"])
            check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
            check_type(argname="argument street_address", value=street_address, expected_type=type_hints["street_address"])
        self._values: typing.Dict[str, typing.Any] = {}
        if common_name is not None:
            self._values["common_name"] = common_name
        if country is not None:
            self._values["country"] = country
        if locality is not None:
            self._values["locality"] = locality
        if organization is not None:
            self._values["organization"] = organization
        if organizational_unit is not None:
            self._values["organizational_unit"] = organizational_unit
        if postal_code is not None:
            self._values["postal_code"] = postal_code
        if province is not None:
            self._values["province"] = province
        if serial_number is not None:
            self._values["serial_number"] = serial_number
        if street_address is not None:
            self._values["street_address"] = street_address

    @builtins.property
    def common_name(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``CN``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#common_name SelfSignedCert#common_name}
        '''
        result = self._values.get("common_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``C``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#country SelfSignedCert#country}
        '''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locality(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``L``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#locality SelfSignedCert#locality}
        '''
        result = self._values.get("locality")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``O``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#organization SelfSignedCert#organization}
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organizational_unit(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``OU``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#organizational_unit SelfSignedCert#organizational_unit}
        '''
        result = self._values.get("organizational_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postal_code(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``PC``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#postal_code SelfSignedCert#postal_code}
        '''
        result = self._values.get("postal_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def province(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``ST``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#province SelfSignedCert#province}
        '''
        result = self._values.get("province")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''Distinguished name: ``SERIALNUMBER``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#serial_number SelfSignedCert#serial_number}
        '''
        result = self._values.get("serial_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def street_address(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Distinguished name: ``STREET``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tls/r/self_signed_cert#street_address SelfSignedCert#street_address}
        '''
        result = self._values.get("street_address")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SelfSignedCertSubject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SelfSignedCertSubjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tls.selfSignedCert.SelfSignedCertSubjectOutputReference",
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
            type_hints = typing.get_type_hints(SelfSignedCertSubjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCommonName")
    def reset_common_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonName", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetLocality")
    def reset_locality(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocality", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetOrganizationalUnit")
    def reset_organizational_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganizationalUnit", []))

    @jsii.member(jsii_name="resetPostalCode")
    def reset_postal_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostalCode", []))

    @jsii.member(jsii_name="resetProvince")
    def reset_province(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvince", []))

    @jsii.member(jsii_name="resetSerialNumber")
    def reset_serial_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSerialNumber", []))

    @jsii.member(jsii_name="resetStreetAddress")
    def reset_street_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStreetAddress", []))

    @builtins.property
    @jsii.member(jsii_name="commonNameInput")
    def common_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commonNameInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

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
    @jsii.member(jsii_name="serialNumberInput")
    def serial_number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serialNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="streetAddressInput")
    def street_address_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "streetAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="commonName")
    def common_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commonName"))

    @common_name.setter
    def common_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "common_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonName", value)

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "country").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="locality")
    def locality(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locality"))

    @locality.setter
    def locality(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "locality").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locality", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="organizationalUnit")
    def organizational_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organizationalUnit"))

    @organizational_unit.setter
    def organizational_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "organizational_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationalUnit", value)

    @builtins.property
    @jsii.member(jsii_name="postalCode")
    def postal_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postalCode"))

    @postal_code.setter
    def postal_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "postal_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postalCode", value)

    @builtins.property
    @jsii.member(jsii_name="province")
    def province(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "province"))

    @province.setter
    def province(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "province").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "province", value)

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serialNumber"))

    @serial_number.setter
    def serial_number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "serial_number").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serialNumber", value)

    @builtins.property
    @jsii.member(jsii_name="streetAddress")
    def street_address(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "streetAddress"))

    @street_address.setter
    def street_address(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "street_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streetAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SelfSignedCertSubject]:
        return typing.cast(typing.Optional[SelfSignedCertSubject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[SelfSignedCertSubject]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SelfSignedCertSubjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SelfSignedCert",
    "SelfSignedCertConfig",
    "SelfSignedCertSubject",
    "SelfSignedCertSubjectOutputReference",
]

publication.publish()
