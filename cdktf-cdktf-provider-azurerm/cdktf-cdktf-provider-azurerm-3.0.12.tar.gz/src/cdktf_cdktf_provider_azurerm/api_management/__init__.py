'''
# `azurerm_api_management`

Refer to the Terraform Registory for docs: [`azurerm_api_management`](https://www.terraform.io/docs/providers/azurerm/r/api_management).
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


class ApiManagement(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagement",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management azurerm_api_management}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        publisher_email: builtins.str,
        publisher_name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        additional_location: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementAdditionalLocation", typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCertificate", typing.Dict[str, typing.Any]]]]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gateway_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hostname_configuration: typing.Optional[typing.Union["ApiManagementHostnameConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ApiManagementIdentity", typing.Dict[str, typing.Any]]] = None,
        min_api_version: typing.Optional[builtins.str] = None,
        notification_sender_email: typing.Optional[builtins.str] = None,
        policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementPolicy", typing.Dict[str, typing.Any]]]]] = None,
        protocols: typing.Optional[typing.Union["ApiManagementProtocols", typing.Dict[str, typing.Any]]] = None,
        public_ip_address_id: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security: typing.Optional[typing.Union["ApiManagementSecurity", typing.Dict[str, typing.Any]]] = None,
        sign_in: typing.Optional[typing.Union["ApiManagementSignIn", typing.Dict[str, typing.Any]]] = None,
        sign_up: typing.Optional[typing.Union["ApiManagementSignUp", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenant_access: typing.Optional[typing.Union["ApiManagementTenantAccess", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_configuration: typing.Optional[typing.Union["ApiManagementVirtualNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        virtual_network_type: typing.Optional[builtins.str] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management azurerm_api_management} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#location ApiManagement#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#name ApiManagement#name}.
        :param publisher_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#publisher_email ApiManagement#publisher_email}.
        :param publisher_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#publisher_name ApiManagement#publisher_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#resource_group_name ApiManagement#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sku_name ApiManagement#sku_name}.
        :param additional_location: additional_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#additional_location ApiManagement#additional_location}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#client_certificate_enabled ApiManagement#client_certificate_enabled}.
        :param gateway_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#gateway_disabled ApiManagement#gateway_disabled}.
        :param hostname_configuration: hostname_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#hostname_configuration ApiManagement#hostname_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#id ApiManagement#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#identity ApiManagement#identity}
        :param min_api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#min_api_version ApiManagement#min_api_version}.
        :param notification_sender_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#notification_sender_email ApiManagement#notification_sender_email}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#policy ApiManagement#policy}.
        :param protocols: protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#protocols ApiManagement#protocols}
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_ip_address_id ApiManagement#public_ip_address_id}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_network_access_enabled ApiManagement#public_network_access_enabled}.
        :param security: security block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#security ApiManagement#security}
        :param sign_in: sign_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sign_in ApiManagement#sign_in}
        :param sign_up: sign_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sign_up ApiManagement#sign_up}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tags ApiManagement#tags}.
        :param tenant_access: tenant_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tenant_access ApiManagement#tenant_access}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#timeouts ApiManagement#timeouts}
        :param virtual_network_configuration: virtual_network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_configuration ApiManagement#virtual_network_configuration}
        :param virtual_network_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_type ApiManagement#virtual_network_type}.
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#zones ApiManagement#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagement.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementConfig(
            location=location,
            name=name,
            publisher_email=publisher_email,
            publisher_name=publisher_name,
            resource_group_name=resource_group_name,
            sku_name=sku_name,
            additional_location=additional_location,
            certificate=certificate,
            client_certificate_enabled=client_certificate_enabled,
            gateway_disabled=gateway_disabled,
            hostname_configuration=hostname_configuration,
            id=id,
            identity=identity,
            min_api_version=min_api_version,
            notification_sender_email=notification_sender_email,
            policy=policy,
            protocols=protocols,
            public_ip_address_id=public_ip_address_id,
            public_network_access_enabled=public_network_access_enabled,
            security=security,
            sign_in=sign_in,
            sign_up=sign_up,
            tags=tags,
            tenant_access=tenant_access,
            timeouts=timeouts,
            virtual_network_configuration=virtual_network_configuration,
            virtual_network_type=virtual_network_type,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdditionalLocation")
    def put_additional_location(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementAdditionalLocation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagement.put_additional_location)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalLocation", [value]))

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagement.put_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putHostnameConfiguration")
    def put_hostname_configuration(
        self,
        *,
        developer_portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationDeveloperPortal", typing.Dict[str, typing.Any]]]]] = None,
        management: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationManagement", typing.Dict[str, typing.Any]]]]] = None,
        portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationPortal", typing.Dict[str, typing.Any]]]]] = None,
        proxy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationProxy", typing.Dict[str, typing.Any]]]]] = None,
        scm: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationScm", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param developer_portal: developer_portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#developer_portal ApiManagement#developer_portal}
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#management ApiManagement#management}
        :param portal: portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#portal ApiManagement#portal}
        :param proxy: proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#proxy ApiManagement#proxy}
        :param scm: scm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#scm ApiManagement#scm}
        '''
        value = ApiManagementHostnameConfiguration(
            developer_portal=developer_portal,
            management=management,
            portal=portal,
            proxy=proxy,
            scm=scm,
        )

        return typing.cast(None, jsii.invoke(self, "putHostnameConfiguration", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#type ApiManagement#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#identity_ids ApiManagement#identity_ids}.
        '''
        value = ApiManagementIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagement.put_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="putProtocols")
    def put_protocols(
        self,
        *,
        enable_http2: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_http2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_http2 ApiManagement#enable_http2}.
        '''
        value = ApiManagementProtocols(enable_http2=enable_http2)

        return typing.cast(None, jsii.invoke(self, "putProtocols", [value]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        *,
        enable_backend_ssl30: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_backend_tls10: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_backend_tls11: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_frontend_ssl30: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_frontend_tls10: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_frontend_tls11: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes128_cbc_sha256_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes128_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes128_gcm_sha256_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes256_cbc_sha256_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes256_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        triple_des_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_backend_ssl30: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_ssl30 ApiManagement#enable_backend_ssl30}.
        :param enable_backend_tls10: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_tls10 ApiManagement#enable_backend_tls10}.
        :param enable_backend_tls11: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_tls11 ApiManagement#enable_backend_tls11}.
        :param enable_frontend_ssl30: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_ssl30 ApiManagement#enable_frontend_ssl30}.
        :param enable_frontend_tls10: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_tls10 ApiManagement#enable_frontend_tls10}.
        :param enable_frontend_tls11: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_tls11 ApiManagement#enable_frontend_tls11}.
        :param tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled}.
        :param tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled}.
        :param tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled}.
        :param tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled}.
        :param tls_rsa_with_aes128_cbc_sha256_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_cbc_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes128_cbc_sha256_ciphers_enabled}.
        :param tls_rsa_with_aes128_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_rsa_with_aes128_cbc_sha_ciphers_enabled}.
        :param tls_rsa_with_aes128_gcm_sha256_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_gcm_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes128_gcm_sha256_ciphers_enabled}.
        :param tls_rsa_with_aes256_cbc_sha256_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes256_cbc_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes256_cbc_sha256_ciphers_enabled}.
        :param tls_rsa_with_aes256_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_rsa_with_aes256_cbc_sha_ciphers_enabled}.
        :param triple_des_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#triple_des_ciphers_enabled ApiManagement#triple_des_ciphers_enabled}.
        '''
        value = ApiManagementSecurity(
            enable_backend_ssl30=enable_backend_ssl30,
            enable_backend_tls10=enable_backend_tls10,
            enable_backend_tls11=enable_backend_tls11,
            enable_frontend_ssl30=enable_frontend_ssl30,
            enable_frontend_tls10=enable_frontend_tls10,
            enable_frontend_tls11=enable_frontend_tls11,
            tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled=tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled,
            tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled=tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled,
            tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled=tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled,
            tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled=tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled,
            tls_rsa_with_aes128_cbc_sha256_ciphers_enabled=tls_rsa_with_aes128_cbc_sha256_ciphers_enabled,
            tls_rsa_with_aes128_cbc_sha_ciphers_enabled=tls_rsa_with_aes128_cbc_sha_ciphers_enabled,
            tls_rsa_with_aes128_gcm_sha256_ciphers_enabled=tls_rsa_with_aes128_gcm_sha256_ciphers_enabled,
            tls_rsa_with_aes256_cbc_sha256_ciphers_enabled=tls_rsa_with_aes256_cbc_sha256_ciphers_enabled,
            tls_rsa_with_aes256_cbc_sha_ciphers_enabled=tls_rsa_with_aes256_cbc_sha_ciphers_enabled,
            triple_des_ciphers_enabled=triple_des_ciphers_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putSecurity", [value]))

    @jsii.member(jsii_name="putSignIn")
    def put_sign_in(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        '''
        value = ApiManagementSignIn(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putSignIn", [value]))

    @jsii.member(jsii_name="putSignUp")
    def put_sign_up(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        terms_of_service: typing.Union["ApiManagementSignUpTermsOfService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        :param terms_of_service: terms_of_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#terms_of_service ApiManagement#terms_of_service}
        '''
        value = ApiManagementSignUp(enabled=enabled, terms_of_service=terms_of_service)

        return typing.cast(None, jsii.invoke(self, "putSignUp", [value]))

    @jsii.member(jsii_name="putTenantAccess")
    def put_tenant_access(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        '''
        value = ApiManagementTenantAccess(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putTenantAccess", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#create ApiManagement#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#delete ApiManagement#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#read ApiManagement#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#update ApiManagement#update}.
        '''
        value = ApiManagementTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVirtualNetworkConfiguration")
    def put_virtual_network_configuration(self, *, subnet_id: builtins.str) -> None:
        '''
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#subnet_id ApiManagement#subnet_id}.
        '''
        value = ApiManagementVirtualNetworkConfiguration(subnet_id=subnet_id)

        return typing.cast(None, jsii.invoke(self, "putVirtualNetworkConfiguration", [value]))

    @jsii.member(jsii_name="resetAdditionalLocation")
    def reset_additional_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalLocation", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetClientCertificateEnabled")
    def reset_client_certificate_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCertificateEnabled", []))

    @jsii.member(jsii_name="resetGatewayDisabled")
    def reset_gateway_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayDisabled", []))

    @jsii.member(jsii_name="resetHostnameConfiguration")
    def reset_hostname_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostnameConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetMinApiVersion")
    def reset_min_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinApiVersion", []))

    @jsii.member(jsii_name="resetNotificationSenderEmail")
    def reset_notification_sender_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationSenderEmail", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetProtocols")
    def reset_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocols", []))

    @jsii.member(jsii_name="resetPublicIpAddressId")
    def reset_public_ip_address_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpAddressId", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetSecurity")
    def reset_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurity", []))

    @jsii.member(jsii_name="resetSignIn")
    def reset_sign_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignIn", []))

    @jsii.member(jsii_name="resetSignUp")
    def reset_sign_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignUp", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTenantAccess")
    def reset_tenant_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantAccess", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVirtualNetworkConfiguration")
    def reset_virtual_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkConfiguration", []))

    @jsii.member(jsii_name="resetVirtualNetworkType")
    def reset_virtual_network_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkType", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="additionalLocation")
    def additional_location(self) -> "ApiManagementAdditionalLocationList":
        return typing.cast("ApiManagementAdditionalLocationList", jsii.get(self, "additionalLocation"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> "ApiManagementCertificateList":
        return typing.cast("ApiManagementCertificateList", jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="developerPortalUrl")
    def developer_portal_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "developerPortalUrl"))

    @builtins.property
    @jsii.member(jsii_name="gatewayRegionalUrl")
    def gateway_regional_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayRegionalUrl"))

    @builtins.property
    @jsii.member(jsii_name="gatewayUrl")
    def gateway_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayUrl"))

    @builtins.property
    @jsii.member(jsii_name="hostnameConfiguration")
    def hostname_configuration(
        self,
    ) -> "ApiManagementHostnameConfigurationOutputReference":
        return typing.cast("ApiManagementHostnameConfigurationOutputReference", jsii.get(self, "hostnameConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "ApiManagementIdentityOutputReference":
        return typing.cast("ApiManagementIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="managementApiUrl")
    def management_api_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managementApiUrl"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "ApiManagementPolicyList":
        return typing.cast("ApiManagementPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="portalUrl")
    def portal_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portalUrl"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddresses")
    def private_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> "ApiManagementProtocolsOutputReference":
        return typing.cast("ApiManagementProtocolsOutputReference", jsii.get(self, "protocols"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddresses")
    def public_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="scmUrl")
    def scm_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scmUrl"))

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> "ApiManagementSecurityOutputReference":
        return typing.cast("ApiManagementSecurityOutputReference", jsii.get(self, "security"))

    @builtins.property
    @jsii.member(jsii_name="signIn")
    def sign_in(self) -> "ApiManagementSignInOutputReference":
        return typing.cast("ApiManagementSignInOutputReference", jsii.get(self, "signIn"))

    @builtins.property
    @jsii.member(jsii_name="signUp")
    def sign_up(self) -> "ApiManagementSignUpOutputReference":
        return typing.cast("ApiManagementSignUpOutputReference", jsii.get(self, "signUp"))

    @builtins.property
    @jsii.member(jsii_name="tenantAccess")
    def tenant_access(self) -> "ApiManagementTenantAccessOutputReference":
        return typing.cast("ApiManagementTenantAccessOutputReference", jsii.get(self, "tenantAccess"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementTimeoutsOutputReference":
        return typing.cast("ApiManagementTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkConfiguration")
    def virtual_network_configuration(
        self,
    ) -> "ApiManagementVirtualNetworkConfigurationOutputReference":
        return typing.cast("ApiManagementVirtualNetworkConfigurationOutputReference", jsii.get(self, "virtualNetworkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="additionalLocationInput")
    def additional_location_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementAdditionalLocation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementAdditionalLocation"]]], jsii.get(self, "additionalLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementCertificate"]]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateEnabledInput")
    def client_certificate_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "clientCertificateEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayDisabledInput")
    def gateway_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "gatewayDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameConfigurationInput")
    def hostname_configuration_input(
        self,
    ) -> typing.Optional["ApiManagementHostnameConfiguration"]:
        return typing.cast(typing.Optional["ApiManagementHostnameConfiguration"], jsii.get(self, "hostnameConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["ApiManagementIdentity"]:
        return typing.cast(typing.Optional["ApiManagementIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="minApiVersionInput")
    def min_api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minApiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationSenderEmailInput")
    def notification_sender_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationSenderEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolsInput")
    def protocols_input(self) -> typing.Optional["ApiManagementProtocols"]:
        return typing.cast(typing.Optional["ApiManagementProtocols"], jsii.get(self, "protocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherEmailInput")
    def publisher_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherNameInput")
    def publisher_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(self) -> typing.Optional["ApiManagementSecurity"]:
        return typing.cast(typing.Optional["ApiManagementSecurity"], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="signInInput")
    def sign_in_input(self) -> typing.Optional["ApiManagementSignIn"]:
        return typing.cast(typing.Optional["ApiManagementSignIn"], jsii.get(self, "signInInput"))

    @builtins.property
    @jsii.member(jsii_name="signUpInput")
    def sign_up_input(self) -> typing.Optional["ApiManagementSignUp"]:
        return typing.cast(typing.Optional["ApiManagementSignUp"], jsii.get(self, "signUpInput"))

    @builtins.property
    @jsii.member(jsii_name="skuNameInput")
    def sku_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantAccessInput")
    def tenant_access_input(self) -> typing.Optional["ApiManagementTenantAccess"]:
        return typing.cast(typing.Optional["ApiManagementTenantAccess"], jsii.get(self, "tenantAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkConfigurationInput")
    def virtual_network_configuration_input(
        self,
    ) -> typing.Optional["ApiManagementVirtualNetworkConfiguration"]:
        return typing.cast(typing.Optional["ApiManagementVirtualNetworkConfiguration"], jsii.get(self, "virtualNetworkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkTypeInput")
    def virtual_network_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertificateEnabled")
    def client_certificate_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "clientCertificateEnabled"))

    @client_certificate_enabled.setter
    def client_certificate_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "client_certificate_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayDisabled")
    def gateway_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "gatewayDisabled"))

    @gateway_disabled.setter
    def gateway_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "gateway_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="minApiVersion")
    def min_api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minApiVersion"))

    @min_api_version.setter
    def min_api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "min_api_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minApiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationSenderEmail")
    def notification_sender_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationSenderEmail"))

    @notification_sender_email.setter
    def notification_sender_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "notification_sender_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationSenderEmail", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="publisherEmail")
    def publisher_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisherEmail"))

    @publisher_email.setter
    def publisher_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "publisher_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisherEmail", value)

    @builtins.property
    @jsii.member(jsii_name="publisherName")
    def publisher_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisherName"))

    @publisher_name.setter
    def publisher_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "publisher_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisherName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="skuName")
    def sku_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skuName"))

    @sku_name.setter
    def sku_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "sku_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skuName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkType")
    def virtual_network_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkType"))

    @virtual_network_type.setter
    def virtual_network_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "virtual_network_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkType", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagement, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementAdditionalLocation",
    jsii_struct_bases=[],
    name_mapping={
        "location": "location",
        "capacity": "capacity",
        "gateway_disabled": "gatewayDisabled",
        "public_ip_address_id": "publicIpAddressId",
        "virtual_network_configuration": "virtualNetworkConfiguration",
        "zones": "zones",
    },
)
class ApiManagementAdditionalLocation:
    def __init__(
        self,
        *,
        location: builtins.str,
        capacity: typing.Optional[jsii.Number] = None,
        gateway_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_ip_address_id: typing.Optional[builtins.str] = None,
        virtual_network_configuration: typing.Optional[typing.Union["ApiManagementAdditionalLocationVirtualNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#location ApiManagement#location}.
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#capacity ApiManagement#capacity}.
        :param gateway_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#gateway_disabled ApiManagement#gateway_disabled}.
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_ip_address_id ApiManagement#public_ip_address_id}.
        :param virtual_network_configuration: virtual_network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_configuration ApiManagement#virtual_network_configuration}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#zones ApiManagement#zones}.
        '''
        if isinstance(virtual_network_configuration, dict):
            virtual_network_configuration = ApiManagementAdditionalLocationVirtualNetworkConfiguration(**virtual_network_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementAdditionalLocation.__init__)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument gateway_disabled", value=gateway_disabled, expected_type=type_hints["gateway_disabled"])
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument virtual_network_configuration", value=virtual_network_configuration, expected_type=type_hints["virtual_network_configuration"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
        }
        if capacity is not None:
            self._values["capacity"] = capacity
        if gateway_disabled is not None:
            self._values["gateway_disabled"] = gateway_disabled
        if public_ip_address_id is not None:
            self._values["public_ip_address_id"] = public_ip_address_id
        if virtual_network_configuration is not None:
            self._values["virtual_network_configuration"] = virtual_network_configuration
        if zones is not None:
            self._values["zones"] = zones

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#location ApiManagement#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#capacity ApiManagement#capacity}.'''
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def gateway_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#gateway_disabled ApiManagement#gateway_disabled}.'''
        result = self._values.get("gateway_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_ip_address_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_ip_address_id ApiManagement#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_network_configuration(
        self,
    ) -> typing.Optional["ApiManagementAdditionalLocationVirtualNetworkConfiguration"]:
        '''virtual_network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_configuration ApiManagement#virtual_network_configuration}
        '''
        result = self._values.get("virtual_network_configuration")
        return typing.cast(typing.Optional["ApiManagementAdditionalLocationVirtualNetworkConfiguration"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#zones ApiManagement#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementAdditionalLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementAdditionalLocationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementAdditionalLocationList",
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
            type_hints = typing.get_type_hints(ApiManagementAdditionalLocationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementAdditionalLocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementAdditionalLocationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementAdditionalLocationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementAdditionalLocation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementAdditionalLocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementAdditionalLocation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementAdditionalLocationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementAdditionalLocationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementAdditionalLocationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVirtualNetworkConfiguration")
    def put_virtual_network_configuration(self, *, subnet_id: builtins.str) -> None:
        '''
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#subnet_id ApiManagement#subnet_id}.
        '''
        value = ApiManagementAdditionalLocationVirtualNetworkConfiguration(
            subnet_id=subnet_id
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualNetworkConfiguration", [value]))

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @jsii.member(jsii_name="resetGatewayDisabled")
    def reset_gateway_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayDisabled", []))

    @jsii.member(jsii_name="resetPublicIpAddressId")
    def reset_public_ip_address_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpAddressId", []))

    @jsii.member(jsii_name="resetVirtualNetworkConfiguration")
    def reset_virtual_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNetworkConfiguration", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @builtins.property
    @jsii.member(jsii_name="gatewayRegionalUrl")
    def gateway_regional_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayRegionalUrl"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddresses")
    def private_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddresses")
    def public_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkConfiguration")
    def virtual_network_configuration(
        self,
    ) -> "ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference":
        return typing.cast("ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference", jsii.get(self, "virtualNetworkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayDisabledInput")
    def gateway_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "gatewayDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkConfigurationInput")
    def virtual_network_configuration_input(
        self,
    ) -> typing.Optional["ApiManagementAdditionalLocationVirtualNetworkConfiguration"]:
        return typing.cast(typing.Optional["ApiManagementAdditionalLocationVirtualNetworkConfiguration"], jsii.get(self, "virtualNetworkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayDisabled")
    def gateway_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "gatewayDisabled"))

    @gateway_disabled.setter
    def gateway_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationOutputReference, "gateway_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationOutputReference, "public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationOutputReference, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementAdditionalLocation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementAdditionalLocation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementAdditionalLocation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementAdditionalLocationVirtualNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={"subnet_id": "subnetId"},
)
class ApiManagementAdditionalLocationVirtualNetworkConfiguration:
    def __init__(self, *, subnet_id: builtins.str) -> None:
        '''
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#subnet_id ApiManagement#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementAdditionalLocationVirtualNetworkConfiguration.__init__)
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnet_id": subnet_id,
        }

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#subnet_id ApiManagement#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementAdditionalLocationVirtualNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementAdditionalLocationVirtualNetworkConfiguration]:
        return typing.cast(typing.Optional[ApiManagementAdditionalLocationVirtualNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementAdditionalLocationVirtualNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "encoded_certificate": "encodedCertificate",
        "store_name": "storeName",
        "certificate_password": "certificatePassword",
    },
)
class ApiManagementCertificate:
    def __init__(
        self,
        *,
        encoded_certificate: builtins.str,
        store_name: builtins.str,
        certificate_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param encoded_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#encoded_certificate ApiManagement#encoded_certificate}.
        :param store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#store_name ApiManagement#store_name}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCertificate.__init__)
            check_type(argname="argument encoded_certificate", value=encoded_certificate, expected_type=type_hints["encoded_certificate"])
            check_type(argname="argument store_name", value=store_name, expected_type=type_hints["store_name"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
        self._values: typing.Dict[str, typing.Any] = {
            "encoded_certificate": encoded_certificate,
            "store_name": store_name,
        }
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password

    @builtins.property
    def encoded_certificate(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#encoded_certificate ApiManagement#encoded_certificate}.'''
        result = self._values.get("encoded_certificate")
        assert result is not None, "Required property 'encoded_certificate' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def store_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#store_name ApiManagement#store_name}.'''
        result = self._values.get("store_name")
        assert result is not None, "Required property 'store_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementCertificateList",
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
            type_hints = typing.get_type_hints(ApiManagementCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApiManagementCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementCertificateOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="encodedCertificateInput")
    def encoded_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodedCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="storeNameInput")
    def store_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="encodedCertificate")
    def encoded_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encodedCertificate"))

    @encoded_certificate.setter
    def encoded_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateOutputReference, "encoded_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encodedCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="storeName")
    def store_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storeName"))

    @store_name.setter
    def store_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateOutputReference, "store_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementConfig",
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
        "publisher_email": "publisherEmail",
        "publisher_name": "publisherName",
        "resource_group_name": "resourceGroupName",
        "sku_name": "skuName",
        "additional_location": "additionalLocation",
        "certificate": "certificate",
        "client_certificate_enabled": "clientCertificateEnabled",
        "gateway_disabled": "gatewayDisabled",
        "hostname_configuration": "hostnameConfiguration",
        "id": "id",
        "identity": "identity",
        "min_api_version": "minApiVersion",
        "notification_sender_email": "notificationSenderEmail",
        "policy": "policy",
        "protocols": "protocols",
        "public_ip_address_id": "publicIpAddressId",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "security": "security",
        "sign_in": "signIn",
        "sign_up": "signUp",
        "tags": "tags",
        "tenant_access": "tenantAccess",
        "timeouts": "timeouts",
        "virtual_network_configuration": "virtualNetworkConfiguration",
        "virtual_network_type": "virtualNetworkType",
        "zones": "zones",
    },
)
class ApiManagementConfig(cdktf.TerraformMetaArguments):
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
        publisher_email: builtins.str,
        publisher_name: builtins.str,
        resource_group_name: builtins.str,
        sku_name: builtins.str,
        additional_location: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementAdditionalLocation, typing.Dict[str, typing.Any]]]]] = None,
        certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementCertificate, typing.Dict[str, typing.Any]]]]] = None,
        client_certificate_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gateway_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hostname_configuration: typing.Optional[typing.Union["ApiManagementHostnameConfiguration", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["ApiManagementIdentity", typing.Dict[str, typing.Any]]] = None,
        min_api_version: typing.Optional[builtins.str] = None,
        notification_sender_email: typing.Optional[builtins.str] = None,
        policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementPolicy", typing.Dict[str, typing.Any]]]]] = None,
        protocols: typing.Optional[typing.Union["ApiManagementProtocols", typing.Dict[str, typing.Any]]] = None,
        public_ip_address_id: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security: typing.Optional[typing.Union["ApiManagementSecurity", typing.Dict[str, typing.Any]]] = None,
        sign_in: typing.Optional[typing.Union["ApiManagementSignIn", typing.Dict[str, typing.Any]]] = None,
        sign_up: typing.Optional[typing.Union["ApiManagementSignUp", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tenant_access: typing.Optional[typing.Union["ApiManagementTenantAccess", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementTimeouts", typing.Dict[str, typing.Any]]] = None,
        virtual_network_configuration: typing.Optional[typing.Union["ApiManagementVirtualNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        virtual_network_type: typing.Optional[builtins.str] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#location ApiManagement#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#name ApiManagement#name}.
        :param publisher_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#publisher_email ApiManagement#publisher_email}.
        :param publisher_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#publisher_name ApiManagement#publisher_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#resource_group_name ApiManagement#resource_group_name}.
        :param sku_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sku_name ApiManagement#sku_name}.
        :param additional_location: additional_location block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#additional_location ApiManagement#additional_location}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}
        :param client_certificate_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#client_certificate_enabled ApiManagement#client_certificate_enabled}.
        :param gateway_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#gateway_disabled ApiManagement#gateway_disabled}.
        :param hostname_configuration: hostname_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#hostname_configuration ApiManagement#hostname_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#id ApiManagement#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#identity ApiManagement#identity}
        :param min_api_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#min_api_version ApiManagement#min_api_version}.
        :param notification_sender_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#notification_sender_email ApiManagement#notification_sender_email}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#policy ApiManagement#policy}.
        :param protocols: protocols block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#protocols ApiManagement#protocols}
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_ip_address_id ApiManagement#public_ip_address_id}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_network_access_enabled ApiManagement#public_network_access_enabled}.
        :param security: security block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#security ApiManagement#security}
        :param sign_in: sign_in block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sign_in ApiManagement#sign_in}
        :param sign_up: sign_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sign_up ApiManagement#sign_up}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tags ApiManagement#tags}.
        :param tenant_access: tenant_access block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tenant_access ApiManagement#tenant_access}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#timeouts ApiManagement#timeouts}
        :param virtual_network_configuration: virtual_network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_configuration ApiManagement#virtual_network_configuration}
        :param virtual_network_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_type ApiManagement#virtual_network_type}.
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#zones ApiManagement#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(hostname_configuration, dict):
            hostname_configuration = ApiManagementHostnameConfiguration(**hostname_configuration)
        if isinstance(identity, dict):
            identity = ApiManagementIdentity(**identity)
        if isinstance(protocols, dict):
            protocols = ApiManagementProtocols(**protocols)
        if isinstance(security, dict):
            security = ApiManagementSecurity(**security)
        if isinstance(sign_in, dict):
            sign_in = ApiManagementSignIn(**sign_in)
        if isinstance(sign_up, dict):
            sign_up = ApiManagementSignUp(**sign_up)
        if isinstance(tenant_access, dict):
            tenant_access = ApiManagementTenantAccess(**tenant_access)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementTimeouts(**timeouts)
        if isinstance(virtual_network_configuration, dict):
            virtual_network_configuration = ApiManagementVirtualNetworkConfiguration(**virtual_network_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher_email", value=publisher_email, expected_type=type_hints["publisher_email"])
            check_type(argname="argument publisher_name", value=publisher_name, expected_type=type_hints["publisher_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku_name", value=sku_name, expected_type=type_hints["sku_name"])
            check_type(argname="argument additional_location", value=additional_location, expected_type=type_hints["additional_location"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument client_certificate_enabled", value=client_certificate_enabled, expected_type=type_hints["client_certificate_enabled"])
            check_type(argname="argument gateway_disabled", value=gateway_disabled, expected_type=type_hints["gateway_disabled"])
            check_type(argname="argument hostname_configuration", value=hostname_configuration, expected_type=type_hints["hostname_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument min_api_version", value=min_api_version, expected_type=type_hints["min_api_version"])
            check_type(argname="argument notification_sender_email", value=notification_sender_email, expected_type=type_hints["notification_sender_email"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument sign_in", value=sign_in, expected_type=type_hints["sign_in"])
            check_type(argname="argument sign_up", value=sign_up, expected_type=type_hints["sign_up"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tenant_access", value=tenant_access, expected_type=type_hints["tenant_access"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument virtual_network_configuration", value=virtual_network_configuration, expected_type=type_hints["virtual_network_configuration"])
            check_type(argname="argument virtual_network_type", value=virtual_network_type, expected_type=type_hints["virtual_network_type"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "publisher_email": publisher_email,
            "publisher_name": publisher_name,
            "resource_group_name": resource_group_name,
            "sku_name": sku_name,
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
        if additional_location is not None:
            self._values["additional_location"] = additional_location
        if certificate is not None:
            self._values["certificate"] = certificate
        if client_certificate_enabled is not None:
            self._values["client_certificate_enabled"] = client_certificate_enabled
        if gateway_disabled is not None:
            self._values["gateway_disabled"] = gateway_disabled
        if hostname_configuration is not None:
            self._values["hostname_configuration"] = hostname_configuration
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if min_api_version is not None:
            self._values["min_api_version"] = min_api_version
        if notification_sender_email is not None:
            self._values["notification_sender_email"] = notification_sender_email
        if policy is not None:
            self._values["policy"] = policy
        if protocols is not None:
            self._values["protocols"] = protocols
        if public_ip_address_id is not None:
            self._values["public_ip_address_id"] = public_ip_address_id
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if security is not None:
            self._values["security"] = security
        if sign_in is not None:
            self._values["sign_in"] = sign_in
        if sign_up is not None:
            self._values["sign_up"] = sign_up
        if tags is not None:
            self._values["tags"] = tags
        if tenant_access is not None:
            self._values["tenant_access"] = tenant_access
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if virtual_network_configuration is not None:
            self._values["virtual_network_configuration"] = virtual_network_configuration
        if virtual_network_type is not None:
            self._values["virtual_network_type"] = virtual_network_type
        if zones is not None:
            self._values["zones"] = zones

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#location ApiManagement#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#name ApiManagement#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher_email(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#publisher_email ApiManagement#publisher_email}.'''
        result = self._values.get("publisher_email")
        assert result is not None, "Required property 'publisher_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#publisher_name ApiManagement#publisher_name}.'''
        result = self._values.get("publisher_name")
        assert result is not None, "Required property 'publisher_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#resource_group_name ApiManagement#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sku_name ApiManagement#sku_name}.'''
        result = self._values.get("sku_name")
        assert result is not None, "Required property 'sku_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_location(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementAdditionalLocation]]]:
        '''additional_location block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#additional_location ApiManagement#additional_location}
        '''
        result = self._values.get("additional_location")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementAdditionalLocation]]], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCertificate]]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementCertificate]]], result)

    @builtins.property
    def client_certificate_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#client_certificate_enabled ApiManagement#client_certificate_enabled}.'''
        result = self._values.get("client_certificate_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gateway_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#gateway_disabled ApiManagement#gateway_disabled}.'''
        result = self._values.get("gateway_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hostname_configuration(
        self,
    ) -> typing.Optional["ApiManagementHostnameConfiguration"]:
        '''hostname_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#hostname_configuration ApiManagement#hostname_configuration}
        '''
        result = self._values.get("hostname_configuration")
        return typing.cast(typing.Optional["ApiManagementHostnameConfiguration"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#id ApiManagement#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["ApiManagementIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#identity ApiManagement#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["ApiManagementIdentity"], result)

    @builtins.property
    def min_api_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#min_api_version ApiManagement#min_api_version}.'''
        result = self._values.get("min_api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_sender_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#notification_sender_email ApiManagement#notification_sender_email}.'''
        result = self._values.get("notification_sender_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementPolicy"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#policy ApiManagement#policy}.'''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementPolicy"]]], result)

    @builtins.property
    def protocols(self) -> typing.Optional["ApiManagementProtocols"]:
        '''protocols block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#protocols ApiManagement#protocols}
        '''
        result = self._values.get("protocols")
        return typing.cast(typing.Optional["ApiManagementProtocols"], result)

    @builtins.property
    def public_ip_address_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_ip_address_id ApiManagement#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#public_network_access_enabled ApiManagement#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security(self) -> typing.Optional["ApiManagementSecurity"]:
        '''security block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#security ApiManagement#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional["ApiManagementSecurity"], result)

    @builtins.property
    def sign_in(self) -> typing.Optional["ApiManagementSignIn"]:
        '''sign_in block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sign_in ApiManagement#sign_in}
        '''
        result = self._values.get("sign_in")
        return typing.cast(typing.Optional["ApiManagementSignIn"], result)

    @builtins.property
    def sign_up(self) -> typing.Optional["ApiManagementSignUp"]:
        '''sign_up block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#sign_up ApiManagement#sign_up}
        '''
        result = self._values.get("sign_up")
        return typing.cast(typing.Optional["ApiManagementSignUp"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tags ApiManagement#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tenant_access(self) -> typing.Optional["ApiManagementTenantAccess"]:
        '''tenant_access block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tenant_access ApiManagement#tenant_access}
        '''
        result = self._values.get("tenant_access")
        return typing.cast(typing.Optional["ApiManagementTenantAccess"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#timeouts ApiManagement#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementTimeouts"], result)

    @builtins.property
    def virtual_network_configuration(
        self,
    ) -> typing.Optional["ApiManagementVirtualNetworkConfiguration"]:
        '''virtual_network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_configuration ApiManagement#virtual_network_configuration}
        '''
        result = self._values.get("virtual_network_configuration")
        return typing.cast(typing.Optional["ApiManagementVirtualNetworkConfiguration"], result)

    @builtins.property
    def virtual_network_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#virtual_network_type ApiManagement#virtual_network_type}.'''
        result = self._values.get("virtual_network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#zones ApiManagement#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "developer_portal": "developerPortal",
        "management": "management",
        "portal": "portal",
        "proxy": "proxy",
        "scm": "scm",
    },
)
class ApiManagementHostnameConfiguration:
    def __init__(
        self,
        *,
        developer_portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationDeveloperPortal", typing.Dict[str, typing.Any]]]]] = None,
        management: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationManagement", typing.Dict[str, typing.Any]]]]] = None,
        portal: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationPortal", typing.Dict[str, typing.Any]]]]] = None,
        proxy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationProxy", typing.Dict[str, typing.Any]]]]] = None,
        scm: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationScm", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param developer_portal: developer_portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#developer_portal ApiManagement#developer_portal}
        :param management: management block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#management ApiManagement#management}
        :param portal: portal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#portal ApiManagement#portal}
        :param proxy: proxy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#proxy ApiManagement#proxy}
        :param scm: scm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#scm ApiManagement#scm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfiguration.__init__)
            check_type(argname="argument developer_portal", value=developer_portal, expected_type=type_hints["developer_portal"])
            check_type(argname="argument management", value=management, expected_type=type_hints["management"])
            check_type(argname="argument portal", value=portal, expected_type=type_hints["portal"])
            check_type(argname="argument proxy", value=proxy, expected_type=type_hints["proxy"])
            check_type(argname="argument scm", value=scm, expected_type=type_hints["scm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if developer_portal is not None:
            self._values["developer_portal"] = developer_portal
        if management is not None:
            self._values["management"] = management
        if portal is not None:
            self._values["portal"] = portal
        if proxy is not None:
            self._values["proxy"] = proxy
        if scm is not None:
            self._values["scm"] = scm

    @builtins.property
    def developer_portal(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationDeveloperPortal"]]]:
        '''developer_portal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#developer_portal ApiManagement#developer_portal}
        '''
        result = self._values.get("developer_portal")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationDeveloperPortal"]]], result)

    @builtins.property
    def management(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationManagement"]]]:
        '''management block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#management ApiManagement#management}
        '''
        result = self._values.get("management")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationManagement"]]], result)

    @builtins.property
    def portal(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationPortal"]]]:
        '''portal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#portal ApiManagement#portal}
        '''
        result = self._values.get("portal")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationPortal"]]], result)

    @builtins.property
    def proxy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationProxy"]]]:
        '''proxy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#proxy ApiManagement#proxy}
        '''
        result = self._values.get("proxy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationProxy"]]], result)

    @builtins.property
    def scm(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationScm"]]]:
        '''scm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#scm ApiManagement#scm}
        '''
        result = self._values.get("scm")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationScm"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementHostnameConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationDeveloperPortal",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementHostnameConfigurationDeveloperPortal:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationDeveloperPortal.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementHostnameConfigurationDeveloperPortal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementHostnameConfigurationDeveloperPortalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationDeveloperPortalList",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationDeveloperPortalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementHostnameConfigurationDeveloperPortalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationDeveloperPortalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementHostnameConfigurationDeveloperPortalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationDeveloperPortal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationDeveloperPortal]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationDeveloperPortal]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementHostnameConfigurationDeveloperPortalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationDeveloperPortalOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationDeveloperPortalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementHostnameConfigurationDeveloperPortal, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementHostnameConfigurationDeveloperPortal, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementHostnameConfigurationDeveloperPortal, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationDeveloperPortalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationManagement",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementHostnameConfigurationManagement:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationManagement.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementHostnameConfigurationManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementHostnameConfigurationManagementList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationManagementList",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationManagementList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementHostnameConfigurationManagementOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationManagementList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementHostnameConfigurationManagementOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationManagement]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationManagement]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationManagement]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementHostnameConfigurationManagementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationManagementOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationManagementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementHostnameConfigurationManagement, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementHostnameConfigurationManagement, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementHostnameConfigurationManagement, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationManagementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementHostnameConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeveloperPortal")
    def put_developer_portal(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementHostnameConfigurationDeveloperPortal, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationOutputReference.put_developer_portal)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeveloperPortal", [value]))

    @jsii.member(jsii_name="putManagement")
    def put_management(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementHostnameConfigurationManagement, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationOutputReference.put_management)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagement", [value]))

    @jsii.member(jsii_name="putPortal")
    def put_portal(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationPortal", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationOutputReference.put_portal)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPortal", [value]))

    @jsii.member(jsii_name="putProxy")
    def put_proxy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationProxy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationOutputReference.put_proxy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProxy", [value]))

    @jsii.member(jsii_name="putScm")
    def put_scm(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementHostnameConfigurationScm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationOutputReference.put_scm)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScm", [value]))

    @jsii.member(jsii_name="resetDeveloperPortal")
    def reset_developer_portal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperPortal", []))

    @jsii.member(jsii_name="resetManagement")
    def reset_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagement", []))

    @jsii.member(jsii_name="resetPortal")
    def reset_portal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortal", []))

    @jsii.member(jsii_name="resetProxy")
    def reset_proxy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxy", []))

    @jsii.member(jsii_name="resetScm")
    def reset_scm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScm", []))

    @builtins.property
    @jsii.member(jsii_name="developerPortal")
    def developer_portal(self) -> ApiManagementHostnameConfigurationDeveloperPortalList:
        return typing.cast(ApiManagementHostnameConfigurationDeveloperPortalList, jsii.get(self, "developerPortal"))

    @builtins.property
    @jsii.member(jsii_name="management")
    def management(self) -> ApiManagementHostnameConfigurationManagementList:
        return typing.cast(ApiManagementHostnameConfigurationManagementList, jsii.get(self, "management"))

    @builtins.property
    @jsii.member(jsii_name="portal")
    def portal(self) -> "ApiManagementHostnameConfigurationPortalList":
        return typing.cast("ApiManagementHostnameConfigurationPortalList", jsii.get(self, "portal"))

    @builtins.property
    @jsii.member(jsii_name="proxy")
    def proxy(self) -> "ApiManagementHostnameConfigurationProxyList":
        return typing.cast("ApiManagementHostnameConfigurationProxyList", jsii.get(self, "proxy"))

    @builtins.property
    @jsii.member(jsii_name="scm")
    def scm(self) -> "ApiManagementHostnameConfigurationScmList":
        return typing.cast("ApiManagementHostnameConfigurationScmList", jsii.get(self, "scm"))

    @builtins.property
    @jsii.member(jsii_name="developerPortalInput")
    def developer_portal_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationDeveloperPortal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationDeveloperPortal]]], jsii.get(self, "developerPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="managementInput")
    def management_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationManagement]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationManagement]]], jsii.get(self, "managementInput"))

    @builtins.property
    @jsii.member(jsii_name="portalInput")
    def portal_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationPortal"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationPortal"]]], jsii.get(self, "portalInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyInput")
    def proxy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationProxy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationProxy"]]], jsii.get(self, "proxyInput"))

    @builtins.property
    @jsii.member(jsii_name="scmInput")
    def scm_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationScm"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementHostnameConfigurationScm"]]], jsii.get(self, "scmInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementHostnameConfiguration]:
        return typing.cast(typing.Optional[ApiManagementHostnameConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementHostnameConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationPortal",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementHostnameConfigurationPortal:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationPortal.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementHostnameConfigurationPortal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementHostnameConfigurationPortalList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationPortalList",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationPortalList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementHostnameConfigurationPortalOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationPortalList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementHostnameConfigurationPortalOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationPortal]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationPortal]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationPortal]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementHostnameConfigurationPortalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationPortalOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationPortalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementHostnameConfigurationPortal, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementHostnameConfigurationPortal, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementHostnameConfigurationPortal, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationPortalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationProxy",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "default_ssl_binding": "defaultSslBinding",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementHostnameConfigurationProxy:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        default_ssl_binding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.
        :param default_ssl_binding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#default_ssl_binding ApiManagement#default_ssl_binding}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationProxy.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument default_ssl_binding", value=default_ssl_binding, expected_type=type_hints["default_ssl_binding"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if default_ssl_binding is not None:
            self._values["default_ssl_binding"] = default_ssl_binding
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ssl_binding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#default_ssl_binding ApiManagement#default_ssl_binding}.'''
        result = self._values.get("default_ssl_binding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementHostnameConfigurationProxy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementHostnameConfigurationProxyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationProxyList",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationProxyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementHostnameConfigurationProxyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationProxyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementHostnameConfigurationProxyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationProxy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationProxy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationProxy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementHostnameConfigurationProxyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationProxyOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationProxyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetDefaultSslBinding")
    def reset_default_ssl_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSslBinding", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSslBindingInput")
    def default_ssl_binding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultSslBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSslBinding")
    def default_ssl_binding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "defaultSslBinding"))

    @default_ssl_binding.setter
    def default_ssl_binding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "default_ssl_binding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSslBinding", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementHostnameConfigurationProxy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementHostnameConfigurationProxy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementHostnameConfigurationProxy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationProxyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationScm",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "certificate": "certificate",
        "certificate_password": "certificatePassword",
        "key_vault_id": "keyVaultId",
        "negotiate_client_certificate": "negotiateClientCertificate",
        "ssl_keyvault_identity_client_id": "sslKeyvaultIdentityClientId",
    },
)
class ApiManagementHostnameConfigurationScm:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        certificate: typing.Optional[builtins.str] = None,
        certificate_password: typing.Optional[builtins.str] = None,
        key_vault_id: typing.Optional[builtins.str] = None,
        negotiate_client_certificate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssl_keyvault_identity_client_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.
        :param certificate_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.
        :param negotiate_client_certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.
        :param ssl_keyvault_identity_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationScm.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_password", value=certificate_password, expected_type=type_hints["certificate_password"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
            check_type(argname="argument negotiate_client_certificate", value=negotiate_client_certificate, expected_type=type_hints["negotiate_client_certificate"])
            check_type(argname="argument ssl_keyvault_identity_client_id", value=ssl_keyvault_identity_client_id, expected_type=type_hints["ssl_keyvault_identity_client_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if certificate_password is not None:
            self._values["certificate_password"] = certificate_password
        if key_vault_id is not None:
            self._values["key_vault_id"] = key_vault_id
        if negotiate_client_certificate is not None:
            self._values["negotiate_client_certificate"] = negotiate_client_certificate
        if ssl_keyvault_identity_client_id is not None:
            self._values["ssl_keyvault_identity_client_id"] = ssl_keyvault_identity_client_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#host_name ApiManagement#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate ApiManagement#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#certificate_password ApiManagement#certificate_password}.'''
        result = self._values.get("certificate_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#key_vault_id ApiManagement#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def negotiate_client_certificate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#negotiate_client_certificate ApiManagement#negotiate_client_certificate}.'''
        result = self._values.get("negotiate_client_certificate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssl_keyvault_identity_client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#ssl_keyvault_identity_client_id ApiManagement#ssl_keyvault_identity_client_id}.'''
        result = self._values.get("ssl_keyvault_identity_client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementHostnameConfigurationScm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementHostnameConfigurationScmList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationScmList",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationScmList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementHostnameConfigurationScmOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationScmList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementHostnameConfigurationScmOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationScm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationScm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementHostnameConfigurationScm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementHostnameConfigurationScmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementHostnameConfigurationScmOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementHostnameConfigurationScmOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetCertificatePassword")
    def reset_certificate_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificatePassword", []))

    @jsii.member(jsii_name="resetKeyVaultId")
    def reset_key_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultId", []))

    @jsii.member(jsii_name="resetNegotiateClientCertificate")
    def reset_negotiate_client_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegotiateClientCertificate", []))

    @jsii.member(jsii_name="resetSslKeyvaultIdentityClientId")
    def reset_ssl_keyvault_identity_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslKeyvaultIdentityClientId", []))

    @builtins.property
    @jsii.member(jsii_name="certificateSource")
    def certificate_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateSource"))

    @builtins.property
    @jsii.member(jsii_name="certificateStatus")
    def certificate_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStatus"))

    @builtins.property
    @jsii.member(jsii_name="expiry")
    def expiry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiry"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="certificatePasswordInput")
    def certificate_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificateInput")
    def negotiate_client_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negotiateClientCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientIdInput")
    def ssl_keyvault_identity_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslKeyvaultIdentityClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePassword")
    def certificate_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificatePassword"))

    @certificate_password.setter
    def certificate_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "certificate_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePassword", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="negotiateClientCertificate")
    def negotiate_client_certificate(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negotiateClientCertificate"))

    @negotiate_client_certificate.setter
    def negotiate_client_certificate(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "negotiate_client_certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negotiateClientCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="sslKeyvaultIdentityClientId")
    def ssl_keyvault_identity_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslKeyvaultIdentityClientId"))

    @ssl_keyvault_identity_client_id.setter
    def ssl_keyvault_identity_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "ssl_keyvault_identity_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslKeyvaultIdentityClientId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementHostnameConfigurationScm, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementHostnameConfigurationScm, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementHostnameConfigurationScm, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementHostnameConfigurationScmOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class ApiManagementIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#type ApiManagement#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#identity_ids ApiManagement#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#type ApiManagement#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#identity_ids ApiManagement#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementIdentityOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementIdentity]:
        return typing.cast(typing.Optional[ApiManagementIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementPolicy",
    jsii_struct_bases=[],
    name_mapping={"xml_content": "xmlContent", "xml_link": "xmlLink"},
)
class ApiManagementPolicy:
    def __init__(
        self,
        *,
        xml_content: typing.Optional[builtins.str] = None,
        xml_link: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param xml_content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#xml_content ApiManagement#xml_content}.
        :param xml_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#xml_link ApiManagement#xml_link}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementPolicy.__init__)
            check_type(argname="argument xml_content", value=xml_content, expected_type=type_hints["xml_content"])
            check_type(argname="argument xml_link", value=xml_link, expected_type=type_hints["xml_link"])
        self._values: typing.Dict[str, typing.Any] = {}
        if xml_content is not None:
            self._values["xml_content"] = xml_content
        if xml_link is not None:
            self._values["xml_link"] = xml_link

    @builtins.property
    def xml_content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#xml_content ApiManagement#xml_content}.'''
        result = self._values.get("xml_content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def xml_link(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#xml_link ApiManagement#xml_link}.'''
        result = self._values.get("xml_link")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementPolicyList",
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
            type_hints = typing.get_type_hints(ApiManagementPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApiManagementPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetXmlContent")
    def reset_xml_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXmlContent", []))

    @jsii.member(jsii_name="resetXmlLink")
    def reset_xml_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXmlLink", []))

    @builtins.property
    @jsii.member(jsii_name="xmlContentInput")
    def xml_content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "xmlContentInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlLinkInput")
    def xml_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "xmlLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlContent")
    def xml_content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xmlContent"))

    @xml_content.setter
    def xml_content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyOutputReference, "xml_content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xmlContent", value)

    @builtins.property
    @jsii.member(jsii_name="xmlLink")
    def xml_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xmlLink"))

    @xml_link.setter
    def xml_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyOutputReference, "xml_link").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xmlLink", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementProtocols",
    jsii_struct_bases=[],
    name_mapping={"enable_http2": "enableHttp2"},
)
class ApiManagementProtocols:
    def __init__(
        self,
        *,
        enable_http2: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_http2: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_http2 ApiManagement#enable_http2}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementProtocols.__init__)
            check_type(argname="argument enable_http2", value=enable_http2, expected_type=type_hints["enable_http2"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_http2 is not None:
            self._values["enable_http2"] = enable_http2

    @builtins.property
    def enable_http2(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_http2 ApiManagement#enable_http2}.'''
        result = self._values.get("enable_http2")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementProtocols(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementProtocolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementProtocolsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementProtocolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableHttp2")
    def reset_enable_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableHttp2", []))

    @builtins.property
    @jsii.member(jsii_name="enableHttp2Input")
    def enable_http2_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableHttp2Input"))

    @builtins.property
    @jsii.member(jsii_name="enableHttp2")
    def enable_http2(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableHttp2"))

    @enable_http2.setter
    def enable_http2(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementProtocolsOutputReference, "enable_http2").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableHttp2", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementProtocols]:
        return typing.cast(typing.Optional[ApiManagementProtocols], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementProtocols]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementProtocolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSecurity",
    jsii_struct_bases=[],
    name_mapping={
        "enable_backend_ssl30": "enableBackendSsl30",
        "enable_backend_tls10": "enableBackendTls10",
        "enable_backend_tls11": "enableBackendTls11",
        "enable_frontend_ssl30": "enableFrontendSsl30",
        "enable_frontend_tls10": "enableFrontendTls10",
        "enable_frontend_tls11": "enableFrontendTls11",
        "tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled": "tlsEcdheEcdsaWithAes128CbcShaCiphersEnabled",
        "tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled": "tlsEcdheEcdsaWithAes256CbcShaCiphersEnabled",
        "tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled": "tlsEcdheRsaWithAes128CbcShaCiphersEnabled",
        "tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled": "tlsEcdheRsaWithAes256CbcShaCiphersEnabled",
        "tls_rsa_with_aes128_cbc_sha256_ciphers_enabled": "tlsRsaWithAes128CbcSha256CiphersEnabled",
        "tls_rsa_with_aes128_cbc_sha_ciphers_enabled": "tlsRsaWithAes128CbcShaCiphersEnabled",
        "tls_rsa_with_aes128_gcm_sha256_ciphers_enabled": "tlsRsaWithAes128GcmSha256CiphersEnabled",
        "tls_rsa_with_aes256_cbc_sha256_ciphers_enabled": "tlsRsaWithAes256CbcSha256CiphersEnabled",
        "tls_rsa_with_aes256_cbc_sha_ciphers_enabled": "tlsRsaWithAes256CbcShaCiphersEnabled",
        "triple_des_ciphers_enabled": "tripleDesCiphersEnabled",
    },
)
class ApiManagementSecurity:
    def __init__(
        self,
        *,
        enable_backend_ssl30: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_backend_tls10: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_backend_tls11: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_frontend_ssl30: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_frontend_tls10: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_frontend_tls11: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes128_cbc_sha256_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes128_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes128_gcm_sha256_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes256_cbc_sha256_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tls_rsa_with_aes256_cbc_sha_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        triple_des_ciphers_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_backend_ssl30: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_ssl30 ApiManagement#enable_backend_ssl30}.
        :param enable_backend_tls10: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_tls10 ApiManagement#enable_backend_tls10}.
        :param enable_backend_tls11: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_tls11 ApiManagement#enable_backend_tls11}.
        :param enable_frontend_ssl30: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_ssl30 ApiManagement#enable_frontend_ssl30}.
        :param enable_frontend_tls10: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_tls10 ApiManagement#enable_frontend_tls10}.
        :param enable_frontend_tls11: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_tls11 ApiManagement#enable_frontend_tls11}.
        :param tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled}.
        :param tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled}.
        :param tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled}.
        :param tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled}.
        :param tls_rsa_with_aes128_cbc_sha256_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_cbc_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes128_cbc_sha256_ciphers_enabled}.
        :param tls_rsa_with_aes128_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_rsa_with_aes128_cbc_sha_ciphers_enabled}.
        :param tls_rsa_with_aes128_gcm_sha256_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_gcm_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes128_gcm_sha256_ciphers_enabled}.
        :param tls_rsa_with_aes256_cbc_sha256_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes256_cbc_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes256_cbc_sha256_ciphers_enabled}.
        :param tls_rsa_with_aes256_cbc_sha_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_rsa_with_aes256_cbc_sha_ciphers_enabled}.
        :param triple_des_ciphers_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#triple_des_ciphers_enabled ApiManagement#triple_des_ciphers_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementSecurity.__init__)
            check_type(argname="argument enable_backend_ssl30", value=enable_backend_ssl30, expected_type=type_hints["enable_backend_ssl30"])
            check_type(argname="argument enable_backend_tls10", value=enable_backend_tls10, expected_type=type_hints["enable_backend_tls10"])
            check_type(argname="argument enable_backend_tls11", value=enable_backend_tls11, expected_type=type_hints["enable_backend_tls11"])
            check_type(argname="argument enable_frontend_ssl30", value=enable_frontend_ssl30, expected_type=type_hints["enable_frontend_ssl30"])
            check_type(argname="argument enable_frontend_tls10", value=enable_frontend_tls10, expected_type=type_hints["enable_frontend_tls10"])
            check_type(argname="argument enable_frontend_tls11", value=enable_frontend_tls11, expected_type=type_hints["enable_frontend_tls11"])
            check_type(argname="argument tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled", value=tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled, expected_type=type_hints["tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled"])
            check_type(argname="argument tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled", value=tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled, expected_type=type_hints["tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled"])
            check_type(argname="argument tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled", value=tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled, expected_type=type_hints["tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled"])
            check_type(argname="argument tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled", value=tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled, expected_type=type_hints["tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled"])
            check_type(argname="argument tls_rsa_with_aes128_cbc_sha256_ciphers_enabled", value=tls_rsa_with_aes128_cbc_sha256_ciphers_enabled, expected_type=type_hints["tls_rsa_with_aes128_cbc_sha256_ciphers_enabled"])
            check_type(argname="argument tls_rsa_with_aes128_cbc_sha_ciphers_enabled", value=tls_rsa_with_aes128_cbc_sha_ciphers_enabled, expected_type=type_hints["tls_rsa_with_aes128_cbc_sha_ciphers_enabled"])
            check_type(argname="argument tls_rsa_with_aes128_gcm_sha256_ciphers_enabled", value=tls_rsa_with_aes128_gcm_sha256_ciphers_enabled, expected_type=type_hints["tls_rsa_with_aes128_gcm_sha256_ciphers_enabled"])
            check_type(argname="argument tls_rsa_with_aes256_cbc_sha256_ciphers_enabled", value=tls_rsa_with_aes256_cbc_sha256_ciphers_enabled, expected_type=type_hints["tls_rsa_with_aes256_cbc_sha256_ciphers_enabled"])
            check_type(argname="argument tls_rsa_with_aes256_cbc_sha_ciphers_enabled", value=tls_rsa_with_aes256_cbc_sha_ciphers_enabled, expected_type=type_hints["tls_rsa_with_aes256_cbc_sha_ciphers_enabled"])
            check_type(argname="argument triple_des_ciphers_enabled", value=triple_des_ciphers_enabled, expected_type=type_hints["triple_des_ciphers_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_backend_ssl30 is not None:
            self._values["enable_backend_ssl30"] = enable_backend_ssl30
        if enable_backend_tls10 is not None:
            self._values["enable_backend_tls10"] = enable_backend_tls10
        if enable_backend_tls11 is not None:
            self._values["enable_backend_tls11"] = enable_backend_tls11
        if enable_frontend_ssl30 is not None:
            self._values["enable_frontend_ssl30"] = enable_frontend_ssl30
        if enable_frontend_tls10 is not None:
            self._values["enable_frontend_tls10"] = enable_frontend_tls10
        if enable_frontend_tls11 is not None:
            self._values["enable_frontend_tls11"] = enable_frontend_tls11
        if tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled is not None:
            self._values["tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled"] = tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled
        if tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled is not None:
            self._values["tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled"] = tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled
        if tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled is not None:
            self._values["tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled"] = tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled
        if tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled is not None:
            self._values["tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled"] = tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled
        if tls_rsa_with_aes128_cbc_sha256_ciphers_enabled is not None:
            self._values["tls_rsa_with_aes128_cbc_sha256_ciphers_enabled"] = tls_rsa_with_aes128_cbc_sha256_ciphers_enabled
        if tls_rsa_with_aes128_cbc_sha_ciphers_enabled is not None:
            self._values["tls_rsa_with_aes128_cbc_sha_ciphers_enabled"] = tls_rsa_with_aes128_cbc_sha_ciphers_enabled
        if tls_rsa_with_aes128_gcm_sha256_ciphers_enabled is not None:
            self._values["tls_rsa_with_aes128_gcm_sha256_ciphers_enabled"] = tls_rsa_with_aes128_gcm_sha256_ciphers_enabled
        if tls_rsa_with_aes256_cbc_sha256_ciphers_enabled is not None:
            self._values["tls_rsa_with_aes256_cbc_sha256_ciphers_enabled"] = tls_rsa_with_aes256_cbc_sha256_ciphers_enabled
        if tls_rsa_with_aes256_cbc_sha_ciphers_enabled is not None:
            self._values["tls_rsa_with_aes256_cbc_sha_ciphers_enabled"] = tls_rsa_with_aes256_cbc_sha_ciphers_enabled
        if triple_des_ciphers_enabled is not None:
            self._values["triple_des_ciphers_enabled"] = triple_des_ciphers_enabled

    @builtins.property
    def enable_backend_ssl30(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_ssl30 ApiManagement#enable_backend_ssl30}.'''
        result = self._values.get("enable_backend_ssl30")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_backend_tls10(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_tls10 ApiManagement#enable_backend_tls10}.'''
        result = self._values.get("enable_backend_tls10")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_backend_tls11(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_backend_tls11 ApiManagement#enable_backend_tls11}.'''
        result = self._values.get("enable_backend_tls11")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_frontend_ssl30(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_ssl30 ApiManagement#enable_frontend_ssl30}.'''
        result = self._values.get("enable_frontend_ssl30")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_frontend_tls10(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_tls10 ApiManagement#enable_frontend_tls10}.'''
        result = self._values.get("enable_frontend_tls10")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_frontend_tls11(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enable_frontend_tls11 ApiManagement#enable_frontend_tls11}.'''
        result = self._values.get("enable_frontend_tls11")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled}.'''
        result = self._values.get("tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled}.'''
        result = self._values.get("tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled}.'''
        result = self._values.get("tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled}.'''
        result = self._values.get("tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_rsa_with_aes128_cbc_sha256_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_cbc_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes128_cbc_sha256_ciphers_enabled}.'''
        result = self._values.get("tls_rsa_with_aes128_cbc_sha256_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_rsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_cbc_sha_ciphers_enabled ApiManagement#tls_rsa_with_aes128_cbc_sha_ciphers_enabled}.'''
        result = self._values.get("tls_rsa_with_aes128_cbc_sha_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_rsa_with_aes128_gcm_sha256_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes128_gcm_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes128_gcm_sha256_ciphers_enabled}.'''
        result = self._values.get("tls_rsa_with_aes128_gcm_sha256_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_rsa_with_aes256_cbc_sha256_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes256_cbc_sha256_ciphers_enabled ApiManagement#tls_rsa_with_aes256_cbc_sha256_ciphers_enabled}.'''
        result = self._values.get("tls_rsa_with_aes256_cbc_sha256_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tls_rsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#tls_rsa_with_aes256_cbc_sha_ciphers_enabled ApiManagement#tls_rsa_with_aes256_cbc_sha_ciphers_enabled}.'''
        result = self._values.get("tls_rsa_with_aes256_cbc_sha_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def triple_des_ciphers_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#triple_des_ciphers_enabled ApiManagement#triple_des_ciphers_enabled}.'''
        result = self._values.get("triple_des_ciphers_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementSecurityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSecurityOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementSecurityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableBackendSsl30")
    def reset_enable_backend_ssl30(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBackendSsl30", []))

    @jsii.member(jsii_name="resetEnableBackendTls10")
    def reset_enable_backend_tls10(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBackendTls10", []))

    @jsii.member(jsii_name="resetEnableBackendTls11")
    def reset_enable_backend_tls11(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBackendTls11", []))

    @jsii.member(jsii_name="resetEnableFrontendSsl30")
    def reset_enable_frontend_ssl30(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFrontendSsl30", []))

    @jsii.member(jsii_name="resetEnableFrontendTls10")
    def reset_enable_frontend_tls10(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFrontendTls10", []))

    @jsii.member(jsii_name="resetEnableFrontendTls11")
    def reset_enable_frontend_tls11(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableFrontendTls11", []))

    @jsii.member(jsii_name="resetTlsEcdheEcdsaWithAes128CbcShaCiphersEnabled")
    def reset_tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsEcdheEcdsaWithAes128CbcShaCiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsEcdheEcdsaWithAes256CbcShaCiphersEnabled")
    def reset_tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsEcdheEcdsaWithAes256CbcShaCiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsEcdheRsaWithAes128CbcShaCiphersEnabled")
    def reset_tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsEcdheRsaWithAes128CbcShaCiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsEcdheRsaWithAes256CbcShaCiphersEnabled")
    def reset_tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsEcdheRsaWithAes256CbcShaCiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsRsaWithAes128CbcSha256CiphersEnabled")
    def reset_tls_rsa_with_aes128_cbc_sha256_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsRsaWithAes128CbcSha256CiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsRsaWithAes128CbcShaCiphersEnabled")
    def reset_tls_rsa_with_aes128_cbc_sha_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsRsaWithAes128CbcShaCiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsRsaWithAes128GcmSha256CiphersEnabled")
    def reset_tls_rsa_with_aes128_gcm_sha256_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsRsaWithAes128GcmSha256CiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsRsaWithAes256CbcSha256CiphersEnabled")
    def reset_tls_rsa_with_aes256_cbc_sha256_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsRsaWithAes256CbcSha256CiphersEnabled", []))

    @jsii.member(jsii_name="resetTlsRsaWithAes256CbcShaCiphersEnabled")
    def reset_tls_rsa_with_aes256_cbc_sha_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsRsaWithAes256CbcShaCiphersEnabled", []))

    @jsii.member(jsii_name="resetTripleDesCiphersEnabled")
    def reset_triple_des_ciphers_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTripleDesCiphersEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enableBackendSsl30Input")
    def enable_backend_ssl30_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBackendSsl30Input"))

    @builtins.property
    @jsii.member(jsii_name="enableBackendTls10Input")
    def enable_backend_tls10_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBackendTls10Input"))

    @builtins.property
    @jsii.member(jsii_name="enableBackendTls11Input")
    def enable_backend_tls11_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBackendTls11Input"))

    @builtins.property
    @jsii.member(jsii_name="enableFrontendSsl30Input")
    def enable_frontend_ssl30_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableFrontendSsl30Input"))

    @builtins.property
    @jsii.member(jsii_name="enableFrontendTls10Input")
    def enable_frontend_tls10_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableFrontendTls10Input"))

    @builtins.property
    @jsii.member(jsii_name="enableFrontendTls11Input")
    def enable_frontend_tls11_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableFrontendTls11Input"))

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheEcdsaWithAes128CbcShaCiphersEnabledInput")
    def tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsEcdheEcdsaWithAes128CbcShaCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheEcdsaWithAes256CbcShaCiphersEnabledInput")
    def tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsEcdheEcdsaWithAes256CbcShaCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheRsaWithAes128CbcShaCiphersEnabledInput")
    def tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsEcdheRsaWithAes128CbcShaCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheRsaWithAes256CbcShaCiphersEnabledInput")
    def tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsEcdheRsaWithAes256CbcShaCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes128CbcSha256CiphersEnabledInput")
    def tls_rsa_with_aes128_cbc_sha256_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsRsaWithAes128CbcSha256CiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes128CbcShaCiphersEnabledInput")
    def tls_rsa_with_aes128_cbc_sha_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsRsaWithAes128CbcShaCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes128GcmSha256CiphersEnabledInput")
    def tls_rsa_with_aes128_gcm_sha256_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsRsaWithAes128GcmSha256CiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes256CbcSha256CiphersEnabledInput")
    def tls_rsa_with_aes256_cbc_sha256_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsRsaWithAes256CbcSha256CiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes256CbcShaCiphersEnabledInput")
    def tls_rsa_with_aes256_cbc_sha_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsRsaWithAes256CbcShaCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tripleDesCiphersEnabledInput")
    def triple_des_ciphers_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tripleDesCiphersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBackendSsl30")
    def enable_backend_ssl30(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBackendSsl30"))

    @enable_backend_ssl30.setter
    def enable_backend_ssl30(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "enable_backend_ssl30").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBackendSsl30", value)

    @builtins.property
    @jsii.member(jsii_name="enableBackendTls10")
    def enable_backend_tls10(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBackendTls10"))

    @enable_backend_tls10.setter
    def enable_backend_tls10(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "enable_backend_tls10").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBackendTls10", value)

    @builtins.property
    @jsii.member(jsii_name="enableBackendTls11")
    def enable_backend_tls11(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBackendTls11"))

    @enable_backend_tls11.setter
    def enable_backend_tls11(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "enable_backend_tls11").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBackendTls11", value)

    @builtins.property
    @jsii.member(jsii_name="enableFrontendSsl30")
    def enable_frontend_ssl30(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableFrontendSsl30"))

    @enable_frontend_ssl30.setter
    def enable_frontend_ssl30(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "enable_frontend_ssl30").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFrontendSsl30", value)

    @builtins.property
    @jsii.member(jsii_name="enableFrontendTls10")
    def enable_frontend_tls10(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableFrontendTls10"))

    @enable_frontend_tls10.setter
    def enable_frontend_tls10(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "enable_frontend_tls10").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFrontendTls10", value)

    @builtins.property
    @jsii.member(jsii_name="enableFrontendTls11")
    def enable_frontend_tls11(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableFrontendTls11"))

    @enable_frontend_tls11.setter
    def enable_frontend_tls11(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "enable_frontend_tls11").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableFrontendTls11", value)

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheEcdsaWithAes128CbcShaCiphersEnabled")
    def tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsEcdheEcdsaWithAes128CbcShaCiphersEnabled"))

    @tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled.setter
    def tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_ecdhe_ecdsa_with_aes128_cbc_sha_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsEcdheEcdsaWithAes128CbcShaCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheEcdsaWithAes256CbcShaCiphersEnabled")
    def tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsEcdheEcdsaWithAes256CbcShaCiphersEnabled"))

    @tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled.setter
    def tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_ecdhe_ecdsa_with_aes256_cbc_sha_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsEcdheEcdsaWithAes256CbcShaCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheRsaWithAes128CbcShaCiphersEnabled")
    def tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsEcdheRsaWithAes128CbcShaCiphersEnabled"))

    @tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled.setter
    def tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_ecdhe_rsa_with_aes128_cbc_sha_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsEcdheRsaWithAes128CbcShaCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsEcdheRsaWithAes256CbcShaCiphersEnabled")
    def tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsEcdheRsaWithAes256CbcShaCiphersEnabled"))

    @tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled.setter
    def tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_ecdhe_rsa_with_aes256_cbc_sha_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsEcdheRsaWithAes256CbcShaCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes128CbcSha256CiphersEnabled")
    def tls_rsa_with_aes128_cbc_sha256_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsRsaWithAes128CbcSha256CiphersEnabled"))

    @tls_rsa_with_aes128_cbc_sha256_ciphers_enabled.setter
    def tls_rsa_with_aes128_cbc_sha256_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_rsa_with_aes128_cbc_sha256_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsRsaWithAes128CbcSha256CiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes128CbcShaCiphersEnabled")
    def tls_rsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsRsaWithAes128CbcShaCiphersEnabled"))

    @tls_rsa_with_aes128_cbc_sha_ciphers_enabled.setter
    def tls_rsa_with_aes128_cbc_sha_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_rsa_with_aes128_cbc_sha_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsRsaWithAes128CbcShaCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes128GcmSha256CiphersEnabled")
    def tls_rsa_with_aes128_gcm_sha256_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsRsaWithAes128GcmSha256CiphersEnabled"))

    @tls_rsa_with_aes128_gcm_sha256_ciphers_enabled.setter
    def tls_rsa_with_aes128_gcm_sha256_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_rsa_with_aes128_gcm_sha256_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsRsaWithAes128GcmSha256CiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes256CbcSha256CiphersEnabled")
    def tls_rsa_with_aes256_cbc_sha256_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsRsaWithAes256CbcSha256CiphersEnabled"))

    @tls_rsa_with_aes256_cbc_sha256_ciphers_enabled.setter
    def tls_rsa_with_aes256_cbc_sha256_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_rsa_with_aes256_cbc_sha256_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsRsaWithAes256CbcSha256CiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tlsRsaWithAes256CbcShaCiphersEnabled")
    def tls_rsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsRsaWithAes256CbcShaCiphersEnabled"))

    @tls_rsa_with_aes256_cbc_sha_ciphers_enabled.setter
    def tls_rsa_with_aes256_cbc_sha_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "tls_rsa_with_aes256_cbc_sha_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsRsaWithAes256CbcShaCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tripleDesCiphersEnabled")
    def triple_des_ciphers_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tripleDesCiphersEnabled"))

    @triple_des_ciphers_enabled.setter
    def triple_des_ciphers_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "triple_des_ciphers_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tripleDesCiphersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementSecurity]:
        return typing.cast(typing.Optional[ApiManagementSecurity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementSecurity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSecurityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSignIn",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ApiManagementSignIn:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementSignIn.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementSignIn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementSignInOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSignInOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementSignInOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignInOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementSignIn]:
        return typing.cast(typing.Optional[ApiManagementSignIn], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementSignIn]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignInOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSignUp",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "terms_of_service": "termsOfService"},
)
class ApiManagementSignUp:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        terms_of_service: typing.Union["ApiManagementSignUpTermsOfService", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        :param terms_of_service: terms_of_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#terms_of_service ApiManagement#terms_of_service}
        '''
        if isinstance(terms_of_service, dict):
            terms_of_service = ApiManagementSignUpTermsOfService(**terms_of_service)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementSignUp.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument terms_of_service", value=terms_of_service, expected_type=type_hints["terms_of_service"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
            "terms_of_service": terms_of_service,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def terms_of_service(self) -> "ApiManagementSignUpTermsOfService":
        '''terms_of_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#terms_of_service ApiManagement#terms_of_service}
        '''
        result = self._values.get("terms_of_service")
        assert result is not None, "Required property 'terms_of_service' is missing"
        return typing.cast("ApiManagementSignUpTermsOfService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementSignUp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementSignUpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSignUpOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementSignUpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTermsOfService")
    def put_terms_of_service(
        self,
        *,
        consent_required: typing.Union[builtins.bool, cdktf.IResolvable],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consent_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#consent_required ApiManagement#consent_required}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#text ApiManagement#text}.
        '''
        value = ApiManagementSignUpTermsOfService(
            consent_required=consent_required, enabled=enabled, text=text
        )

        return typing.cast(None, jsii.invoke(self, "putTermsOfService", [value]))

    @builtins.property
    @jsii.member(jsii_name="termsOfService")
    def terms_of_service(self) -> "ApiManagementSignUpTermsOfServiceOutputReference":
        return typing.cast("ApiManagementSignUpTermsOfServiceOutputReference", jsii.get(self, "termsOfService"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="termsOfServiceInput")
    def terms_of_service_input(
        self,
    ) -> typing.Optional["ApiManagementSignUpTermsOfService"]:
        return typing.cast(typing.Optional["ApiManagementSignUpTermsOfService"], jsii.get(self, "termsOfServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignUpOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementSignUp]:
        return typing.cast(typing.Optional[ApiManagementSignUp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementSignUp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignUpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSignUpTermsOfService",
    jsii_struct_bases=[],
    name_mapping={
        "consent_required": "consentRequired",
        "enabled": "enabled",
        "text": "text",
    },
)
class ApiManagementSignUpTermsOfService:
    def __init__(
        self,
        *,
        consent_required: typing.Union[builtins.bool, cdktf.IResolvable],
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        text: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param consent_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#consent_required ApiManagement#consent_required}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#text ApiManagement#text}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementSignUpTermsOfService.__init__)
            check_type(argname="argument consent_required", value=consent_required, expected_type=type_hints["consent_required"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {
            "consent_required": consent_required,
            "enabled": enabled,
        }
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def consent_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#consent_required ApiManagement#consent_required}.'''
        result = self._values.get("consent_required")
        assert result is not None, "Required property 'consent_required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#text ApiManagement#text}.'''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementSignUpTermsOfService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementSignUpTermsOfServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementSignUpTermsOfServiceOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementSignUpTermsOfServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="consentRequiredInput")
    def consent_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "consentRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="consentRequired")
    def consent_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "consentRequired"))

    @consent_required.setter
    def consent_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignUpTermsOfServiceOutputReference, "consent_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consentRequired", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignUpTermsOfServiceOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignUpTermsOfServiceOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementSignUpTermsOfService]:
        return typing.cast(typing.Optional[ApiManagementSignUpTermsOfService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementSignUpTermsOfService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementSignUpTermsOfServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementTenantAccess",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ApiManagementTenantAccess:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementTenantAccess.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#enabled ApiManagement#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementTenantAccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementTenantAccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementTenantAccessOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementTenantAccessOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="secondaryKey")
    def secondary_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryKey"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementTenantAccessOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementTenantAccess]:
        return typing.cast(typing.Optional[ApiManagementTenantAccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiManagementTenantAccess]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementTenantAccessOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#create ApiManagement#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#delete ApiManagement#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#read ApiManagement#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#update ApiManagement#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#create ApiManagement#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#delete ApiManagement#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#read ApiManagement#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#update ApiManagement#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementTimeoutsOutputReference.__init__)
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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementVirtualNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={"subnet_id": "subnetId"},
)
class ApiManagementVirtualNetworkConfiguration:
    def __init__(self, *, subnet_id: builtins.str) -> None:
        '''
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#subnet_id ApiManagement#subnet_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementVirtualNetworkConfiguration.__init__)
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnet_id": subnet_id,
        }

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management#subnet_id ApiManagement#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementVirtualNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementVirtualNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagement.ApiManagementVirtualNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementVirtualNetworkConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementVirtualNetworkConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementVirtualNetworkConfiguration]:
        return typing.cast(typing.Optional[ApiManagementVirtualNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementVirtualNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementVirtualNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagement",
    "ApiManagementAdditionalLocation",
    "ApiManagementAdditionalLocationList",
    "ApiManagementAdditionalLocationOutputReference",
    "ApiManagementAdditionalLocationVirtualNetworkConfiguration",
    "ApiManagementAdditionalLocationVirtualNetworkConfigurationOutputReference",
    "ApiManagementCertificate",
    "ApiManagementCertificateList",
    "ApiManagementCertificateOutputReference",
    "ApiManagementConfig",
    "ApiManagementHostnameConfiguration",
    "ApiManagementHostnameConfigurationDeveloperPortal",
    "ApiManagementHostnameConfigurationDeveloperPortalList",
    "ApiManagementHostnameConfigurationDeveloperPortalOutputReference",
    "ApiManagementHostnameConfigurationManagement",
    "ApiManagementHostnameConfigurationManagementList",
    "ApiManagementHostnameConfigurationManagementOutputReference",
    "ApiManagementHostnameConfigurationOutputReference",
    "ApiManagementHostnameConfigurationPortal",
    "ApiManagementHostnameConfigurationPortalList",
    "ApiManagementHostnameConfigurationPortalOutputReference",
    "ApiManagementHostnameConfigurationProxy",
    "ApiManagementHostnameConfigurationProxyList",
    "ApiManagementHostnameConfigurationProxyOutputReference",
    "ApiManagementHostnameConfigurationScm",
    "ApiManagementHostnameConfigurationScmList",
    "ApiManagementHostnameConfigurationScmOutputReference",
    "ApiManagementIdentity",
    "ApiManagementIdentityOutputReference",
    "ApiManagementPolicy",
    "ApiManagementPolicyList",
    "ApiManagementPolicyOutputReference",
    "ApiManagementProtocols",
    "ApiManagementProtocolsOutputReference",
    "ApiManagementSecurity",
    "ApiManagementSecurityOutputReference",
    "ApiManagementSignIn",
    "ApiManagementSignInOutputReference",
    "ApiManagementSignUp",
    "ApiManagementSignUpOutputReference",
    "ApiManagementSignUpTermsOfService",
    "ApiManagementSignUpTermsOfServiceOutputReference",
    "ApiManagementTenantAccess",
    "ApiManagementTenantAccessOutputReference",
    "ApiManagementTimeouts",
    "ApiManagementTimeoutsOutputReference",
    "ApiManagementVirtualNetworkConfiguration",
    "ApiManagementVirtualNetworkConfigurationOutputReference",
]

publication.publish()
