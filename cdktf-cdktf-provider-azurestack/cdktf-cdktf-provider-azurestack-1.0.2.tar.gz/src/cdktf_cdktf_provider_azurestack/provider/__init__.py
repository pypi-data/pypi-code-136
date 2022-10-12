'''
# `provider`

Refer to the Terraform Registory for docs: [`azurestack`](https://www.terraform.io/docs/providers/azurestack).
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


class AzurestackProvider(
    cdktf.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack azurestack}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        features: typing.Union["AzurestackProviderFeatures", typing.Dict[str, typing.Any]],
        alias: typing.Optional[builtins.str] = None,
        arm_endpoint: typing.Optional[builtins.str] = None,
        auxiliary_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_certificate_password: typing.Optional[builtins.str] = None,
        client_certificate_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        disable_correlation_request_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata_host: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        skip_provider_registration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack azurestack} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param features: features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#features AzurestackProvider#features}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#alias AzurestackProvider#alias}
        :param arm_endpoint: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#arm_endpoint AzurestackProvider#arm_endpoint}
        :param auxiliary_tenant_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#auxiliary_tenant_ids AzurestackProvider#auxiliary_tenant_ids}.
        :param client_certificate_password: The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_password AzurestackProvider#client_certificate_password}
        :param client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_path AzurestackProvider#client_certificate_path}
        :param client_id: The Client ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_id AzurestackProvider#client_id}
        :param client_secret: The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_secret AzurestackProvider#client_secret}
        :param disable_correlation_request_id: This will disable the x-ms-correlation-request-id header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#disable_correlation_request_id AzurestackProvider#disable_correlation_request_id}
        :param environment: The Cloud Environment which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#environment AzurestackProvider#environment}
        :param metadata_host: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#metadata_host AzurestackProvider#metadata_host}
        :param msi_endpoint: The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#msi_endpoint AzurestackProvider#msi_endpoint}
        :param skip_provider_registration: Should the AzureStack Provider skip registering all of the Resource Providers that it supports, if they're not already registered? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_provider_registration AzurestackProvider#skip_provider_registration}
        :param subscription_id: The Subscription ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#subscription_id AzurestackProvider#subscription_id}
        :param tenant_id: The Tenant ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#tenant_id AzurestackProvider#tenant_id}
        :param use_msi: Allowed Managed Service Identity be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#use_msi AzurestackProvider#use_msi}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzurestackProvider.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = AzurestackProviderConfig(
            features=features,
            alias=alias,
            arm_endpoint=arm_endpoint,
            auxiliary_tenant_ids=auxiliary_tenant_ids,
            client_certificate_password=client_certificate_password,
            client_certificate_path=client_certificate_path,
            client_id=client_id,
            client_secret=client_secret,
            disable_correlation_request_id=disable_correlation_request_id,
            environment=environment,
            metadata_host=metadata_host,
            msi_endpoint=msi_endpoint,
            skip_provider_registration=skip_provider_registration,
            subscription_id=subscription_id,
            tenant_id=tenant_id,
            use_msi=use_msi,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetArmEndpoint")
    def reset_arm_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArmEndpoint", []))

    @jsii.member(jsii_name="resetAuxiliaryTenantIds")
    def reset_auxiliary_tenant_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuxiliaryTenantIds", []))

    @jsii.member(jsii_name="resetClientCertificatePassword")
    def reset_client_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePassword", []))

    @jsii.member(jsii_name="resetClientCertificatePath")
    def reset_client_certificate_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificatePath", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetDisableCorrelationRequestId")
    def reset_disable_correlation_request_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableCorrelationRequestId", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetMetadataHost")
    def reset_metadata_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataHost", []))

    @jsii.member(jsii_name="resetMsiEndpoint")
    def reset_msi_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsiEndpoint", []))

    @jsii.member(jsii_name="resetSkipProviderRegistration")
    def reset_skip_provider_registration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipProviderRegistration", []))

    @jsii.member(jsii_name="resetSubscriptionId")
    def reset_subscription_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @jsii.member(jsii_name="resetUseMsi")
    def reset_use_msi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseMsi", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="armEndpointInput")
    def arm_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "armEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="auxiliaryTenantIdsInput")
    def auxiliary_tenant_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auxiliaryTenantIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePasswordInput")
    def client_certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePathInput")
    def client_certificate_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePathInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="disableCorrelationRequestIdInput")
    def disable_correlation_request_id_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableCorrelationRequestIdInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="featuresInput")
    def features_input(self) -> typing.Optional["AzurestackProviderFeatures"]:
        return typing.cast(typing.Optional["AzurestackProviderFeatures"], jsii.get(self, "featuresInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataHostInput")
    def metadata_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataHostInput"))

    @builtins.property
    @jsii.member(jsii_name="msiEndpointInput")
    def msi_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="skipProviderRegistrationInput")
    def skip_provider_registration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipProviderRegistrationInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useMsiInput")
    def use_msi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useMsiInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="armEndpoint")
    def arm_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "armEndpoint"))

    @arm_endpoint.setter
    def arm_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "arm_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "armEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="auxiliaryTenantIds")
    def auxiliary_tenant_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "auxiliaryTenantIds"))

    @auxiliary_tenant_ids.setter
    def auxiliary_tenant_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "auxiliary_tenant_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auxiliaryTenantIds", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePassword")
    def client_certificate_password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePassword"))

    @client_certificate_password.setter
    def client_certificate_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "client_certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificatePath")
    def client_certificate_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificatePath"))

    @client_certificate_path.setter
    def client_certificate_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "client_certificate_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificatePath", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="disableCorrelationRequestId")
    def disable_correlation_request_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableCorrelationRequestId"))

    @disable_correlation_request_id.setter
    def disable_correlation_request_id(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "disable_correlation_request_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableCorrelationRequestId", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="features")
    def features(self) -> typing.Optional["AzurestackProviderFeatures"]:
        return typing.cast(typing.Optional["AzurestackProviderFeatures"], jsii.get(self, "features"))

    @features.setter
    def features(self, value: typing.Optional["AzurestackProviderFeatures"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "features").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "features", value)

    @builtins.property
    @jsii.member(jsii_name="metadataHost")
    def metadata_host(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataHost"))

    @metadata_host.setter
    def metadata_host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "metadata_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataHost", value)

    @builtins.property
    @jsii.member(jsii_name="msiEndpoint")
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiEndpoint"))

    @msi_endpoint.setter
    def msi_endpoint(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "msi_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "msiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="skipProviderRegistration")
    def skip_provider_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipProviderRegistration"))

    @skip_provider_registration.setter
    def skip_provider_registration(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "skip_provider_registration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipProviderRegistration", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "subscription_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="useMsi")
    def use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useMsi"))

    @use_msi.setter
    def use_msi(
        self,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AzurestackProvider, "use_msi").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useMsi", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "features": "features",
        "alias": "alias",
        "arm_endpoint": "armEndpoint",
        "auxiliary_tenant_ids": "auxiliaryTenantIds",
        "client_certificate_password": "clientCertificatePassword",
        "client_certificate_path": "clientCertificatePath",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "disable_correlation_request_id": "disableCorrelationRequestId",
        "environment": "environment",
        "metadata_host": "metadataHost",
        "msi_endpoint": "msiEndpoint",
        "skip_provider_registration": "skipProviderRegistration",
        "subscription_id": "subscriptionId",
        "tenant_id": "tenantId",
        "use_msi": "useMsi",
    },
)
class AzurestackProviderConfig:
    def __init__(
        self,
        *,
        features: typing.Union["AzurestackProviderFeatures", typing.Dict[str, typing.Any]],
        alias: typing.Optional[builtins.str] = None,
        arm_endpoint: typing.Optional[builtins.str] = None,
        auxiliary_tenant_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        client_certificate_password: typing.Optional[builtins.str] = None,
        client_certificate_path: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        disable_correlation_request_id: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        metadata_host: typing.Optional[builtins.str] = None,
        msi_endpoint: typing.Optional[builtins.str] = None,
        skip_provider_registration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        use_msi: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param features: features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#features AzurestackProvider#features}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#alias AzurestackProvider#alias}
        :param arm_endpoint: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#arm_endpoint AzurestackProvider#arm_endpoint}
        :param auxiliary_tenant_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#auxiliary_tenant_ids AzurestackProvider#auxiliary_tenant_ids}.
        :param client_certificate_password: The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_password AzurestackProvider#client_certificate_password}
        :param client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_path AzurestackProvider#client_certificate_path}
        :param client_id: The Client ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_id AzurestackProvider#client_id}
        :param client_secret: The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_secret AzurestackProvider#client_secret}
        :param disable_correlation_request_id: This will disable the x-ms-correlation-request-id header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#disable_correlation_request_id AzurestackProvider#disable_correlation_request_id}
        :param environment: The Cloud Environment which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#environment AzurestackProvider#environment}
        :param metadata_host: The Hostname which should be used for the Azure Metadata Service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#metadata_host AzurestackProvider#metadata_host}
        :param msi_endpoint: The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#msi_endpoint AzurestackProvider#msi_endpoint}
        :param skip_provider_registration: Should the AzureStack Provider skip registering all of the Resource Providers that it supports, if they're not already registered? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_provider_registration AzurestackProvider#skip_provider_registration}
        :param subscription_id: The Subscription ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#subscription_id AzurestackProvider#subscription_id}
        :param tenant_id: The Tenant ID which should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#tenant_id AzurestackProvider#tenant_id}
        :param use_msi: Allowed Managed Service Identity be used for Authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#use_msi AzurestackProvider#use_msi}
        '''
        if isinstance(features, dict):
            features = AzurestackProviderFeatures(**features)
        if __debug__:
            type_hints = typing.get_type_hints(AzurestackProviderConfig.__init__)
            check_type(argname="argument features", value=features, expected_type=type_hints["features"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument arm_endpoint", value=arm_endpoint, expected_type=type_hints["arm_endpoint"])
            check_type(argname="argument auxiliary_tenant_ids", value=auxiliary_tenant_ids, expected_type=type_hints["auxiliary_tenant_ids"])
            check_type(argname="argument client_certificate_password", value=client_certificate_password, expected_type=type_hints["client_certificate_password"])
            check_type(argname="argument client_certificate_path", value=client_certificate_path, expected_type=type_hints["client_certificate_path"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument disable_correlation_request_id", value=disable_correlation_request_id, expected_type=type_hints["disable_correlation_request_id"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument metadata_host", value=metadata_host, expected_type=type_hints["metadata_host"])
            check_type(argname="argument msi_endpoint", value=msi_endpoint, expected_type=type_hints["msi_endpoint"])
            check_type(argname="argument skip_provider_registration", value=skip_provider_registration, expected_type=type_hints["skip_provider_registration"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument use_msi", value=use_msi, expected_type=type_hints["use_msi"])
        self._values: typing.Dict[str, typing.Any] = {
            "features": features,
        }
        if alias is not None:
            self._values["alias"] = alias
        if arm_endpoint is not None:
            self._values["arm_endpoint"] = arm_endpoint
        if auxiliary_tenant_ids is not None:
            self._values["auxiliary_tenant_ids"] = auxiliary_tenant_ids
        if client_certificate_password is not None:
            self._values["client_certificate_password"] = client_certificate_password
        if client_certificate_path is not None:
            self._values["client_certificate_path"] = client_certificate_path
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if disable_correlation_request_id is not None:
            self._values["disable_correlation_request_id"] = disable_correlation_request_id
        if environment is not None:
            self._values["environment"] = environment
        if metadata_host is not None:
            self._values["metadata_host"] = metadata_host
        if msi_endpoint is not None:
            self._values["msi_endpoint"] = msi_endpoint
        if skip_provider_registration is not None:
            self._values["skip_provider_registration"] = skip_provider_registration
        if subscription_id is not None:
            self._values["subscription_id"] = subscription_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if use_msi is not None:
            self._values["use_msi"] = use_msi

    @builtins.property
    def features(self) -> "AzurestackProviderFeatures":
        '''features block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#features AzurestackProvider#features}
        '''
        result = self._values.get("features")
        assert result is not None, "Required property 'features' is missing"
        return typing.cast("AzurestackProviderFeatures", result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#alias AzurestackProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arm_endpoint(self) -> typing.Optional[builtins.str]:
        '''The Hostname which should be used for the Azure Metadata Service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#arm_endpoint AzurestackProvider#arm_endpoint}
        '''
        result = self._values.get("arm_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auxiliary_tenant_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#auxiliary_tenant_ids AzurestackProvider#auxiliary_tenant_ids}.'''
        result = self._values.get("auxiliary_tenant_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def client_certificate_password(self) -> typing.Optional[builtins.str]:
        '''The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_password AzurestackProvider#client_certificate_password}
        '''
        result = self._values.get("client_certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_certificate_path(self) -> typing.Optional[builtins.str]:
        '''The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_certificate_path AzurestackProvider#client_certificate_path}
        '''
        result = self._values.get("client_certificate_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''The Client ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_id AzurestackProvider#client_id}
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#client_secret AzurestackProvider#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_correlation_request_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''This will disable the x-ms-correlation-request-id header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#disable_correlation_request_id AzurestackProvider#disable_correlation_request_id}
        '''
        result = self._values.get("disable_correlation_request_id")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The Cloud Environment which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#environment AzurestackProvider#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_host(self) -> typing.Optional[builtins.str]:
        '''The Hostname which should be used for the Azure Metadata Service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#metadata_host AzurestackProvider#metadata_host}
        '''
        result = self._values.get("metadata_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msi_endpoint(self) -> typing.Optional[builtins.str]:
        '''The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#msi_endpoint AzurestackProvider#msi_endpoint}
        '''
        result = self._values.get("msi_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_provider_registration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should the AzureStack Provider skip registering all of the Resource Providers that it supports, if they're not already registered?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_provider_registration AzurestackProvider#skip_provider_registration}
        '''
        result = self._values.get("skip_provider_registration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subscription_id(self) -> typing.Optional[builtins.str]:
        '''The Subscription ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#subscription_id AzurestackProvider#subscription_id}
        '''
        result = self._values.get("subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''The Tenant ID which should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#tenant_id AzurestackProvider#tenant_id}
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_msi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allowed Managed Service Identity be used for Authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#use_msi AzurestackProvider#use_msi}
        '''
        result = self._values.get("use_msi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeatures",
    jsii_struct_bases=[],
    name_mapping={
        "resource_group": "resourceGroup",
        "virtual_machine": "virtualMachine",
        "virtual_machine_scale_set": "virtualMachineScaleSet",
    },
)
class AzurestackProviderFeatures:
    def __init__(
        self,
        *,
        resource_group: typing.Optional[typing.Union["AzurestackProviderFeaturesResourceGroup", typing.Dict[str, typing.Any]]] = None,
        virtual_machine: typing.Optional[typing.Union["AzurestackProviderFeaturesVirtualMachine", typing.Dict[str, typing.Any]]] = None,
        virtual_machine_scale_set: typing.Optional[typing.Union["AzurestackProviderFeaturesVirtualMachineScaleSet", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param resource_group: resource_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#resource_group AzurestackProvider#resource_group}
        :param virtual_machine: virtual_machine block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine AzurestackProvider#virtual_machine}
        :param virtual_machine_scale_set: virtual_machine_scale_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine_scale_set AzurestackProvider#virtual_machine_scale_set}
        '''
        if isinstance(resource_group, dict):
            resource_group = AzurestackProviderFeaturesResourceGroup(**resource_group)
        if isinstance(virtual_machine, dict):
            virtual_machine = AzurestackProviderFeaturesVirtualMachine(**virtual_machine)
        if isinstance(virtual_machine_scale_set, dict):
            virtual_machine_scale_set = AzurestackProviderFeaturesVirtualMachineScaleSet(**virtual_machine_scale_set)
        if __debug__:
            type_hints = typing.get_type_hints(AzurestackProviderFeatures.__init__)
            check_type(argname="argument resource_group", value=resource_group, expected_type=type_hints["resource_group"])
            check_type(argname="argument virtual_machine", value=virtual_machine, expected_type=type_hints["virtual_machine"])
            check_type(argname="argument virtual_machine_scale_set", value=virtual_machine_scale_set, expected_type=type_hints["virtual_machine_scale_set"])
        self._values: typing.Dict[str, typing.Any] = {}
        if resource_group is not None:
            self._values["resource_group"] = resource_group
        if virtual_machine is not None:
            self._values["virtual_machine"] = virtual_machine
        if virtual_machine_scale_set is not None:
            self._values["virtual_machine_scale_set"] = virtual_machine_scale_set

    @builtins.property
    def resource_group(
        self,
    ) -> typing.Optional["AzurestackProviderFeaturesResourceGroup"]:
        '''resource_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#resource_group AzurestackProvider#resource_group}
        '''
        result = self._values.get("resource_group")
        return typing.cast(typing.Optional["AzurestackProviderFeaturesResourceGroup"], result)

    @builtins.property
    def virtual_machine(
        self,
    ) -> typing.Optional["AzurestackProviderFeaturesVirtualMachine"]:
        '''virtual_machine block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine AzurestackProvider#virtual_machine}
        '''
        result = self._values.get("virtual_machine")
        return typing.cast(typing.Optional["AzurestackProviderFeaturesVirtualMachine"], result)

    @builtins.property
    def virtual_machine_scale_set(
        self,
    ) -> typing.Optional["AzurestackProviderFeaturesVirtualMachineScaleSet"]:
        '''virtual_machine_scale_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#virtual_machine_scale_set AzurestackProvider#virtual_machine_scale_set}
        '''
        result = self._values.get("virtual_machine_scale_set")
        return typing.cast(typing.Optional["AzurestackProviderFeaturesVirtualMachineScaleSet"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeaturesResourceGroup",
    jsii_struct_bases=[],
    name_mapping={
        "prevent_deletion_if_contains_resources": "preventDeletionIfContainsResources",
    },
)
class AzurestackProviderFeaturesResourceGroup:
    def __init__(
        self,
        *,
        prevent_deletion_if_contains_resources: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param prevent_deletion_if_contains_resources: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#prevent_deletion_if_contains_resources AzurestackProvider#prevent_deletion_if_contains_resources}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzurestackProviderFeaturesResourceGroup.__init__)
            check_type(argname="argument prevent_deletion_if_contains_resources", value=prevent_deletion_if_contains_resources, expected_type=type_hints["prevent_deletion_if_contains_resources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if prevent_deletion_if_contains_resources is not None:
            self._values["prevent_deletion_if_contains_resources"] = prevent_deletion_if_contains_resources

    @builtins.property
    def prevent_deletion_if_contains_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#prevent_deletion_if_contains_resources AzurestackProvider#prevent_deletion_if_contains_resources}.'''
        result = self._values.get("prevent_deletion_if_contains_resources")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeaturesResourceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeaturesVirtualMachine",
    jsii_struct_bases=[],
    name_mapping={
        "delete_os_disk_on_deletion": "deleteOsDiskOnDeletion",
        "graceful_shutdown": "gracefulShutdown",
        "skip_shutdown_and_force_delete": "skipShutdownAndForceDelete",
    },
)
class AzurestackProviderFeaturesVirtualMachine:
    def __init__(
        self,
        *,
        delete_os_disk_on_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        graceful_shutdown: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_shutdown_and_force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param delete_os_disk_on_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#delete_os_disk_on_deletion AzurestackProvider#delete_os_disk_on_deletion}.
        :param graceful_shutdown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#graceful_shutdown AzurestackProvider#graceful_shutdown}.
        :param skip_shutdown_and_force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_shutdown_and_force_delete AzurestackProvider#skip_shutdown_and_force_delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzurestackProviderFeaturesVirtualMachine.__init__)
            check_type(argname="argument delete_os_disk_on_deletion", value=delete_os_disk_on_deletion, expected_type=type_hints["delete_os_disk_on_deletion"])
            check_type(argname="argument graceful_shutdown", value=graceful_shutdown, expected_type=type_hints["graceful_shutdown"])
            check_type(argname="argument skip_shutdown_and_force_delete", value=skip_shutdown_and_force_delete, expected_type=type_hints["skip_shutdown_and_force_delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if delete_os_disk_on_deletion is not None:
            self._values["delete_os_disk_on_deletion"] = delete_os_disk_on_deletion
        if graceful_shutdown is not None:
            self._values["graceful_shutdown"] = graceful_shutdown
        if skip_shutdown_and_force_delete is not None:
            self._values["skip_shutdown_and_force_delete"] = skip_shutdown_and_force_delete

    @builtins.property
    def delete_os_disk_on_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#delete_os_disk_on_deletion AzurestackProvider#delete_os_disk_on_deletion}.'''
        result = self._values.get("delete_os_disk_on_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def graceful_shutdown(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#graceful_shutdown AzurestackProvider#graceful_shutdown}.'''
        result = self._values.get("graceful_shutdown")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def skip_shutdown_and_force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#skip_shutdown_and_force_delete AzurestackProvider#skip_shutdown_and_force_delete}.'''
        result = self._values.get("skip_shutdown_and_force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeaturesVirtualMachine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.provider.AzurestackProviderFeaturesVirtualMachineScaleSet",
    jsii_struct_bases=[],
    name_mapping={
        "roll_instances_when_required": "rollInstancesWhenRequired",
        "force_delete": "forceDelete",
        "scale_to_zero_before_deletion": "scaleToZeroBeforeDeletion",
    },
)
class AzurestackProviderFeaturesVirtualMachineScaleSet:
    def __init__(
        self,
        *,
        roll_instances_when_required: typing.Union[builtins.bool, cdktf.IResolvable],
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scale_to_zero_before_deletion: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param roll_instances_when_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#roll_instances_when_required AzurestackProvider#roll_instances_when_required}.
        :param force_delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#force_delete AzurestackProvider#force_delete}.
        :param scale_to_zero_before_deletion: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#scale_to_zero_before_deletion AzurestackProvider#scale_to_zero_before_deletion}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AzurestackProviderFeaturesVirtualMachineScaleSet.__init__)
            check_type(argname="argument roll_instances_when_required", value=roll_instances_when_required, expected_type=type_hints["roll_instances_when_required"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument scale_to_zero_before_deletion", value=scale_to_zero_before_deletion, expected_type=type_hints["scale_to_zero_before_deletion"])
        self._values: typing.Dict[str, typing.Any] = {
            "roll_instances_when_required": roll_instances_when_required,
        }
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if scale_to_zero_before_deletion is not None:
            self._values["scale_to_zero_before_deletion"] = scale_to_zero_before_deletion

    @builtins.property
    def roll_instances_when_required(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#roll_instances_when_required AzurestackProvider#roll_instances_when_required}.'''
        result = self._values.get("roll_instances_when_required")
        assert result is not None, "Required property 'roll_instances_when_required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#force_delete AzurestackProvider#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scale_to_zero_before_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack#scale_to_zero_before_deletion AzurestackProvider#scale_to_zero_before_deletion}.'''
        result = self._values.get("scale_to_zero_before_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AzurestackProviderFeaturesVirtualMachineScaleSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AzurestackProvider",
    "AzurestackProviderConfig",
    "AzurestackProviderFeatures",
    "AzurestackProviderFeaturesResourceGroup",
    "AzurestackProviderFeaturesVirtualMachine",
    "AzurestackProviderFeaturesVirtualMachineScaleSet",
]

publication.publish()
