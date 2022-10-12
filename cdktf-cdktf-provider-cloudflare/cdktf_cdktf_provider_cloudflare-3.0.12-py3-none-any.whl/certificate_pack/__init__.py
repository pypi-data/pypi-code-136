'''
# `cloudflare_certificate_pack`

Refer to the Terraform Registory for docs: [`cloudflare_certificate_pack`](https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack).
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


class CertificatePack(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePack",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack cloudflare_certificate_pack}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        certificate_authority: builtins.str,
        hosts: typing.Sequence[builtins.str],
        type: builtins.str,
        validation_method: builtins.str,
        validity_days: jsii.Number,
        zone_id: builtins.str,
        cloudflare_branding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        validation_errors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CertificatePackValidationErrors", typing.Dict[str, typing.Any]]]]] = None,
        validation_records: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CertificatePackValidationRecords", typing.Dict[str, typing.Any]]]]] = None,
        wait_for_active_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack cloudflare_certificate_pack} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_authority: Which certificate authority to issue the certificate pack. Available values: ``digicert``, ``lets_encrypt``, ``google``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#certificate_authority CertificatePack#certificate_authority}
        :param hosts: List of hostnames to provision the certificate pack for. The zone name must be included as a host. Note: If using Let's Encrypt, you cannot use individual subdomains and only a wildcard for subdomain is available. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#hosts CertificatePack#hosts}
        :param type: Certificate pack configuration type. Available values: ``advanced``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#type CertificatePack#type}
        :param validation_method: Which validation method to use in order to prove domain ownership. Available values: ``txt``, ``http``, ``email``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_method CertificatePack#validation_method}
        :param validity_days: How long the certificate is valid for. Note: If using Let's Encrypt, this value can only be 90 days. Available values: ``14``, ``30``, ``90``, ``365``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validity_days CertificatePack#validity_days}
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#zone_id CertificatePack#zone_id}
        :param cloudflare_branding: Whether or not to include Cloudflare branding. This will add ``sni.cloudflaressl.com`` as the Common Name if set to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cloudflare_branding CertificatePack#cloudflare_branding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#id CertificatePack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param validation_errors: validation_errors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_errors CertificatePack#validation_errors}
        :param validation_records: validation_records block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_records CertificatePack#validation_records}
        :param wait_for_active_status: Whether or not to wait for a certificate pack to reach status ``active`` during creation. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#wait_for_active_status CertificatePack#wait_for_active_status}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePack.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CertificatePackConfig(
            certificate_authority=certificate_authority,
            hosts=hosts,
            type=type,
            validation_method=validation_method,
            validity_days=validity_days,
            zone_id=zone_id,
            cloudflare_branding=cloudflare_branding,
            id=id,
            validation_errors=validation_errors,
            validation_records=validation_records,
            wait_for_active_status=wait_for_active_status,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putValidationErrors")
    def put_validation_errors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CertificatePackValidationErrors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePack.put_validation_errors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putValidationErrors", [value]))

    @jsii.member(jsii_name="putValidationRecords")
    def put_validation_records(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CertificatePackValidationRecords", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePack.put_validation_records)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putValidationRecords", [value]))

    @jsii.member(jsii_name="resetCloudflareBranding")
    def reset_cloudflare_branding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudflareBranding", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetValidationErrors")
    def reset_validation_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidationErrors", []))

    @jsii.member(jsii_name="resetValidationRecords")
    def reset_validation_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidationRecords", []))

    @jsii.member(jsii_name="resetWaitForActiveStatus")
    def reset_wait_for_active_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForActiveStatus", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="validationErrors")
    def validation_errors(self) -> "CertificatePackValidationErrorsList":
        return typing.cast("CertificatePackValidationErrorsList", jsii.get(self, "validationErrors"))

    @builtins.property
    @jsii.member(jsii_name="validationRecords")
    def validation_records(self) -> "CertificatePackValidationRecordsList":
        return typing.cast("CertificatePackValidationRecordsList", jsii.get(self, "validationRecords"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityInput")
    def certificate_authority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudflareBrandingInput")
    def cloudflare_branding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cloudflareBrandingInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="validationErrorsInput")
    def validation_errors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationErrors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationErrors"]]], jsii.get(self, "validationErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="validationMethodInput")
    def validation_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="validationRecordsInput")
    def validation_records_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationRecords"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationRecords"]]], jsii.get(self, "validationRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="validityDaysInput")
    def validity_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "validityDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForActiveStatusInput")
    def wait_for_active_status_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForActiveStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthority")
    def certificate_authority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthority"))

    @certificate_authority.setter
    def certificate_authority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "certificate_authority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthority", value)

    @builtins.property
    @jsii.member(jsii_name="cloudflareBranding")
    def cloudflare_branding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cloudflareBranding"))

    @cloudflare_branding.setter
    def cloudflare_branding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "cloudflare_branding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudflareBranding", value)

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "hosts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="validationMethod")
    def validation_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validationMethod"))

    @validation_method.setter
    def validation_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "validation_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="validityDays")
    def validity_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "validityDays"))

    @validity_days.setter
    def validity_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "validity_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validityDays", value)

    @builtins.property
    @jsii.member(jsii_name="waitForActiveStatus")
    def wait_for_active_status(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitForActiveStatus"))

    @wait_for_active_status.setter
    def wait_for_active_status(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "wait_for_active_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForActiveStatus", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePack, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_authority": "certificateAuthority",
        "hosts": "hosts",
        "type": "type",
        "validation_method": "validationMethod",
        "validity_days": "validityDays",
        "zone_id": "zoneId",
        "cloudflare_branding": "cloudflareBranding",
        "id": "id",
        "validation_errors": "validationErrors",
        "validation_records": "validationRecords",
        "wait_for_active_status": "waitForActiveStatus",
    },
)
class CertificatePackConfig(cdktf.TerraformMetaArguments):
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
        certificate_authority: builtins.str,
        hosts: typing.Sequence[builtins.str],
        type: builtins.str,
        validation_method: builtins.str,
        validity_days: jsii.Number,
        zone_id: builtins.str,
        cloudflare_branding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        validation_errors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CertificatePackValidationErrors", typing.Dict[str, typing.Any]]]]] = None,
        validation_records: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CertificatePackValidationRecords", typing.Dict[str, typing.Any]]]]] = None,
        wait_for_active_status: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_authority: Which certificate authority to issue the certificate pack. Available values: ``digicert``, ``lets_encrypt``, ``google``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#certificate_authority CertificatePack#certificate_authority}
        :param hosts: List of hostnames to provision the certificate pack for. The zone name must be included as a host. Note: If using Let's Encrypt, you cannot use individual subdomains and only a wildcard for subdomain is available. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#hosts CertificatePack#hosts}
        :param type: Certificate pack configuration type. Available values: ``advanced``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#type CertificatePack#type}
        :param validation_method: Which validation method to use in order to prove domain ownership. Available values: ``txt``, ``http``, ``email``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_method CertificatePack#validation_method}
        :param validity_days: How long the certificate is valid for. Note: If using Let's Encrypt, this value can only be 90 days. Available values: ``14``, ``30``, ``90``, ``365``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validity_days CertificatePack#validity_days}
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#zone_id CertificatePack#zone_id}
        :param cloudflare_branding: Whether or not to include Cloudflare branding. This will add ``sni.cloudflaressl.com`` as the Common Name if set to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cloudflare_branding CertificatePack#cloudflare_branding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#id CertificatePack#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param validation_errors: validation_errors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_errors CertificatePack#validation_errors}
        :param validation_records: validation_records block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_records CertificatePack#validation_records}
        :param wait_for_active_status: Whether or not to wait for a certificate pack to reach status ``active`` during creation. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#wait_for_active_status CertificatePack#wait_for_active_status}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePackConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_authority", value=certificate_authority, expected_type=type_hints["certificate_authority"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument validation_method", value=validation_method, expected_type=type_hints["validation_method"])
            check_type(argname="argument validity_days", value=validity_days, expected_type=type_hints["validity_days"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument cloudflare_branding", value=cloudflare_branding, expected_type=type_hints["cloudflare_branding"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument validation_errors", value=validation_errors, expected_type=type_hints["validation_errors"])
            check_type(argname="argument validation_records", value=validation_records, expected_type=type_hints["validation_records"])
            check_type(argname="argument wait_for_active_status", value=wait_for_active_status, expected_type=type_hints["wait_for_active_status"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_authority": certificate_authority,
            "hosts": hosts,
            "type": type,
            "validation_method": validation_method,
            "validity_days": validity_days,
            "zone_id": zone_id,
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
        if cloudflare_branding is not None:
            self._values["cloudflare_branding"] = cloudflare_branding
        if id is not None:
            self._values["id"] = id
        if validation_errors is not None:
            self._values["validation_errors"] = validation_errors
        if validation_records is not None:
            self._values["validation_records"] = validation_records
        if wait_for_active_status is not None:
            self._values["wait_for_active_status"] = wait_for_active_status

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
    def certificate_authority(self) -> builtins.str:
        '''Which certificate authority to issue the certificate pack. Available values: ``digicert``, ``lets_encrypt``, ``google``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#certificate_authority CertificatePack#certificate_authority}
        '''
        result = self._values.get("certificate_authority")
        assert result is not None, "Required property 'certificate_authority' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hosts(self) -> typing.List[builtins.str]:
        '''List of hostnames to provision the certificate pack for.

        The zone name must be included as a host. Note: If using Let's Encrypt, you cannot use individual subdomains and only a wildcard for subdomain is available.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#hosts CertificatePack#hosts}
        '''
        result = self._values.get("hosts")
        assert result is not None, "Required property 'hosts' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Certificate pack configuration type. Available values: ``advanced``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#type CertificatePack#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validation_method(self) -> builtins.str:
        '''Which validation method to use in order to prove domain ownership. Available values: ``txt``, ``http``, ``email``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_method CertificatePack#validation_method}
        '''
        result = self._values.get("validation_method")
        assert result is not None, "Required property 'validation_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity_days(self) -> jsii.Number:
        '''How long the certificate is valid for.

        Note: If using Let's Encrypt, this value can only be 90 days. Available values: ``14``, ``30``, ``90``, ``365``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validity_days CertificatePack#validity_days}
        '''
        result = self._values.get("validity_days")
        assert result is not None, "Required property 'validity_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#zone_id CertificatePack#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudflare_branding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to include Cloudflare branding. This will add ``sni.cloudflaressl.com`` as the Common Name if set to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cloudflare_branding CertificatePack#cloudflare_branding}
        '''
        result = self._values.get("cloudflare_branding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#id CertificatePack#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation_errors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationErrors"]]]:
        '''validation_errors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_errors CertificatePack#validation_errors}
        '''
        result = self._values.get("validation_errors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationErrors"]]], result)

    @builtins.property
    def validation_records(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationRecords"]]]:
        '''validation_records block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#validation_records CertificatePack#validation_records}
        '''
        result = self._values.get("validation_records")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CertificatePackValidationRecords"]]], result)

    @builtins.property
    def wait_for_active_status(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to wait for a certificate pack to reach status ``active`` during creation. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#wait_for_active_status CertificatePack#wait_for_active_status}
        '''
        result = self._values.get("wait_for_active_status")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificatePackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackValidationErrors",
    jsii_struct_bases=[],
    name_mapping={},
)
class CertificatePackValidationErrors:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificatePackValidationErrors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CertificatePackValidationErrorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackValidationErrorsList",
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
            type_hints = typing.get_type_hints(CertificatePackValidationErrorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CertificatePackValidationErrorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePackValidationErrorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CertificatePackValidationErrorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationErrorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationErrorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationErrorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CertificatePackValidationErrors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CertificatePackValidationErrors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CertificatePackValidationErrors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationErrorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CertificatePackValidationErrorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackValidationErrorsOutputReference",
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
            type_hints = typing.get_type_hints(CertificatePackValidationErrorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CertificatePackValidationErrors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CertificatePackValidationErrors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CertificatePackValidationErrors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationErrorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackValidationRecords",
    jsii_struct_bases=[],
    name_mapping={
        "cname_name": "cnameName",
        "cname_target": "cnameTarget",
        "emails": "emails",
        "http_body": "httpBody",
        "http_url": "httpUrl",
        "txt_name": "txtName",
        "txt_value": "txtValue",
    },
)
class CertificatePackValidationRecords:
    def __init__(
        self,
        *,
        cname_name: typing.Optional[builtins.str] = None,
        cname_target: typing.Optional[builtins.str] = None,
        emails: typing.Optional[typing.Sequence[builtins.str]] = None,
        http_body: typing.Optional[builtins.str] = None,
        http_url: typing.Optional[builtins.str] = None,
        txt_name: typing.Optional[builtins.str] = None,
        txt_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cname_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cname_name CertificatePack#cname_name}.
        :param cname_target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cname_target CertificatePack#cname_target}.
        :param emails: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#emails CertificatePack#emails}.
        :param http_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#http_body CertificatePack#http_body}.
        :param http_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#http_url CertificatePack#http_url}.
        :param txt_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#txt_name CertificatePack#txt_name}.
        :param txt_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#txt_value CertificatePack#txt_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePackValidationRecords.__init__)
            check_type(argname="argument cname_name", value=cname_name, expected_type=type_hints["cname_name"])
            check_type(argname="argument cname_target", value=cname_target, expected_type=type_hints["cname_target"])
            check_type(argname="argument emails", value=emails, expected_type=type_hints["emails"])
            check_type(argname="argument http_body", value=http_body, expected_type=type_hints["http_body"])
            check_type(argname="argument http_url", value=http_url, expected_type=type_hints["http_url"])
            check_type(argname="argument txt_name", value=txt_name, expected_type=type_hints["txt_name"])
            check_type(argname="argument txt_value", value=txt_value, expected_type=type_hints["txt_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cname_name is not None:
            self._values["cname_name"] = cname_name
        if cname_target is not None:
            self._values["cname_target"] = cname_target
        if emails is not None:
            self._values["emails"] = emails
        if http_body is not None:
            self._values["http_body"] = http_body
        if http_url is not None:
            self._values["http_url"] = http_url
        if txt_name is not None:
            self._values["txt_name"] = txt_name
        if txt_value is not None:
            self._values["txt_value"] = txt_value

    @builtins.property
    def cname_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cname_name CertificatePack#cname_name}.'''
        result = self._values.get("cname_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cname_target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#cname_target CertificatePack#cname_target}.'''
        result = self._values.get("cname_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emails(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#emails CertificatePack#emails}.'''
        result = self._values.get("emails")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def http_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#http_body CertificatePack#http_body}.'''
        result = self._values.get("http_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#http_url CertificatePack#http_url}.'''
        result = self._values.get("http_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def txt_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#txt_name CertificatePack#txt_name}.'''
        result = self._values.get("txt_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def txt_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/certificate_pack#txt_value CertificatePack#txt_value}.'''
        result = self._values.get("txt_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificatePackValidationRecords(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CertificatePackValidationRecordsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackValidationRecordsList",
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
            type_hints = typing.get_type_hints(CertificatePackValidationRecordsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CertificatePackValidationRecordsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CertificatePackValidationRecordsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CertificatePackValidationRecordsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CertificatePackValidationRecords]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CertificatePackValidationRecords]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CertificatePackValidationRecords]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CertificatePackValidationRecordsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.certificatePack.CertificatePackValidationRecordsOutputReference",
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
            type_hints = typing.get_type_hints(CertificatePackValidationRecordsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCnameName")
    def reset_cname_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCnameName", []))

    @jsii.member(jsii_name="resetCnameTarget")
    def reset_cname_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCnameTarget", []))

    @jsii.member(jsii_name="resetEmails")
    def reset_emails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmails", []))

    @jsii.member(jsii_name="resetHttpBody")
    def reset_http_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpBody", []))

    @jsii.member(jsii_name="resetHttpUrl")
    def reset_http_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpUrl", []))

    @jsii.member(jsii_name="resetTxtName")
    def reset_txt_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTxtName", []))

    @jsii.member(jsii_name="resetTxtValue")
    def reset_txt_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTxtValue", []))

    @builtins.property
    @jsii.member(jsii_name="cnameNameInput")
    def cname_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameTargetInput")
    def cname_target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="emailsInput")
    def emails_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpBodyInput")
    def http_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlInput")
    def http_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="txtNameInput")
    def txt_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "txtNameInput"))

    @builtins.property
    @jsii.member(jsii_name="txtValueInput")
    def txt_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "txtValueInput"))

    @builtins.property
    @jsii.member(jsii_name="cnameName")
    def cname_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameName"))

    @cname_name.setter
    def cname_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "cname_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameName", value)

    @builtins.property
    @jsii.member(jsii_name="cnameTarget")
    def cname_target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cnameTarget"))

    @cname_target.setter
    def cname_target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "cname_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cnameTarget", value)

    @builtins.property
    @jsii.member(jsii_name="emails")
    def emails(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "emails"))

    @emails.setter
    def emails(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "emails").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emails", value)

    @builtins.property
    @jsii.member(jsii_name="httpBody")
    def http_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpBody"))

    @http_body.setter
    def http_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "http_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpBody", value)

    @builtins.property
    @jsii.member(jsii_name="httpUrl")
    def http_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpUrl"))

    @http_url.setter
    def http_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "http_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpUrl", value)

    @builtins.property
    @jsii.member(jsii_name="txtName")
    def txt_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "txtName"))

    @txt_name.setter
    def txt_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "txt_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "txtName", value)

    @builtins.property
    @jsii.member(jsii_name="txtValue")
    def txt_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "txtValue"))

    @txt_value.setter
    def txt_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "txt_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "txtValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CertificatePackValidationRecords, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CertificatePackValidationRecords, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CertificatePackValidationRecords, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CertificatePackValidationRecordsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CertificatePack",
    "CertificatePackConfig",
    "CertificatePackValidationErrors",
    "CertificatePackValidationErrorsList",
    "CertificatePackValidationErrorsOutputReference",
    "CertificatePackValidationRecords",
    "CertificatePackValidationRecordsList",
    "CertificatePackValidationRecordsOutputReference",
]

publication.publish()
