'''
# `azurerm_logic_app_integration_account_agreement`

Refer to the Terraform Registory for docs: [`azurerm_logic_app_integration_account_agreement`](https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement).
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


class LogicAppIntegrationAccountAgreement(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreement",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement azurerm_logic_app_integration_account_agreement}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        agreement_type: builtins.str,
        content: builtins.str,
        guest_identity: typing.Union["LogicAppIntegrationAccountAgreementGuestIdentity", typing.Dict[str, typing.Any]],
        guest_partner_name: builtins.str,
        host_identity: typing.Union["LogicAppIntegrationAccountAgreementHostIdentity", typing.Dict[str, typing.Any]],
        host_partner_name: builtins.str,
        integration_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LogicAppIntegrationAccountAgreementTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement azurerm_logic_app_integration_account_agreement} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param agreement_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#agreement_type LogicAppIntegrationAccountAgreement#agreement_type}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#content LogicAppIntegrationAccountAgreement#content}.
        :param guest_identity: guest_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#guest_identity LogicAppIntegrationAccountAgreement#guest_identity}
        :param guest_partner_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#guest_partner_name LogicAppIntegrationAccountAgreement#guest_partner_name}.
        :param host_identity: host_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#host_identity LogicAppIntegrationAccountAgreement#host_identity}
        :param host_partner_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#host_partner_name LogicAppIntegrationAccountAgreement#host_partner_name}.
        :param integration_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#integration_account_name LogicAppIntegrationAccountAgreement#integration_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#name LogicAppIntegrationAccountAgreement#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#resource_group_name LogicAppIntegrationAccountAgreement#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#id LogicAppIntegrationAccountAgreement#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#metadata LogicAppIntegrationAccountAgreement#metadata}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#timeouts LogicAppIntegrationAccountAgreement#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreement.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogicAppIntegrationAccountAgreementConfig(
            agreement_type=agreement_type,
            content=content,
            guest_identity=guest_identity,
            guest_partner_name=guest_partner_name,
            host_identity=host_identity,
            host_partner_name=host_partner_name,
            integration_account_name=integration_account_name,
            name=name,
            resource_group_name=resource_group_name,
            id=id,
            metadata=metadata,
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

    @jsii.member(jsii_name="putGuestIdentity")
    def put_guest_identity(
        self,
        *,
        qualifier: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#qualifier LogicAppIntegrationAccountAgreement#qualifier}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#value LogicAppIntegrationAccountAgreement#value}.
        '''
        value_ = LogicAppIntegrationAccountAgreementGuestIdentity(
            qualifier=qualifier, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putGuestIdentity", [value_]))

    @jsii.member(jsii_name="putHostIdentity")
    def put_host_identity(
        self,
        *,
        qualifier: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#qualifier LogicAppIntegrationAccountAgreement#qualifier}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#value LogicAppIntegrationAccountAgreement#value}.
        '''
        value_ = LogicAppIntegrationAccountAgreementHostIdentity(
            qualifier=qualifier, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putHostIdentity", [value_]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#create LogicAppIntegrationAccountAgreement#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#delete LogicAppIntegrationAccountAgreement#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#read LogicAppIntegrationAccountAgreement#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#update LogicAppIntegrationAccountAgreement#update}.
        '''
        value = LogicAppIntegrationAccountAgreementTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

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
    @jsii.member(jsii_name="guestIdentity")
    def guest_identity(
        self,
    ) -> "LogicAppIntegrationAccountAgreementGuestIdentityOutputReference":
        return typing.cast("LogicAppIntegrationAccountAgreementGuestIdentityOutputReference", jsii.get(self, "guestIdentity"))

    @builtins.property
    @jsii.member(jsii_name="hostIdentity")
    def host_identity(
        self,
    ) -> "LogicAppIntegrationAccountAgreementHostIdentityOutputReference":
        return typing.cast("LogicAppIntegrationAccountAgreementHostIdentityOutputReference", jsii.get(self, "hostIdentity"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LogicAppIntegrationAccountAgreementTimeoutsOutputReference":
        return typing.cast("LogicAppIntegrationAccountAgreementTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="agreementTypeInput")
    def agreement_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agreementTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="guestIdentityInput")
    def guest_identity_input(
        self,
    ) -> typing.Optional["LogicAppIntegrationAccountAgreementGuestIdentity"]:
        return typing.cast(typing.Optional["LogicAppIntegrationAccountAgreementGuestIdentity"], jsii.get(self, "guestIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="guestPartnerNameInput")
    def guest_partner_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guestPartnerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIdentityInput")
    def host_identity_input(
        self,
    ) -> typing.Optional["LogicAppIntegrationAccountAgreementHostIdentity"]:
        return typing.cast(typing.Optional["LogicAppIntegrationAccountAgreementHostIdentity"], jsii.get(self, "hostIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPartnerNameInput")
    def host_partner_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPartnerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationAccountNameInput")
    def integration_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LogicAppIntegrationAccountAgreementTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LogicAppIntegrationAccountAgreementTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="agreementType")
    def agreement_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agreementType"))

    @agreement_type.setter
    def agreement_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "agreement_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agreementType", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="guestPartnerName")
    def guest_partner_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guestPartnerName"))

    @guest_partner_name.setter
    def guest_partner_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "guest_partner_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guestPartnerName", value)

    @builtins.property
    @jsii.member(jsii_name="hostPartnerName")
    def host_partner_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPartnerName"))

    @host_partner_name.setter
    def host_partner_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "host_partner_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPartnerName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationAccountName")
    def integration_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationAccountName"))

    @integration_account_name.setter
    def integration_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "integration_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreement, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "agreement_type": "agreementType",
        "content": "content",
        "guest_identity": "guestIdentity",
        "guest_partner_name": "guestPartnerName",
        "host_identity": "hostIdentity",
        "host_partner_name": "hostPartnerName",
        "integration_account_name": "integrationAccountName",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "id": "id",
        "metadata": "metadata",
        "timeouts": "timeouts",
    },
)
class LogicAppIntegrationAccountAgreementConfig(cdktf.TerraformMetaArguments):
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
        agreement_type: builtins.str,
        content: builtins.str,
        guest_identity: typing.Union["LogicAppIntegrationAccountAgreementGuestIdentity", typing.Dict[str, typing.Any]],
        guest_partner_name: builtins.str,
        host_identity: typing.Union["LogicAppIntegrationAccountAgreementHostIdentity", typing.Dict[str, typing.Any]],
        host_partner_name: builtins.str,
        integration_account_name: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LogicAppIntegrationAccountAgreementTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param agreement_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#agreement_type LogicAppIntegrationAccountAgreement#agreement_type}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#content LogicAppIntegrationAccountAgreement#content}.
        :param guest_identity: guest_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#guest_identity LogicAppIntegrationAccountAgreement#guest_identity}
        :param guest_partner_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#guest_partner_name LogicAppIntegrationAccountAgreement#guest_partner_name}.
        :param host_identity: host_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#host_identity LogicAppIntegrationAccountAgreement#host_identity}
        :param host_partner_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#host_partner_name LogicAppIntegrationAccountAgreement#host_partner_name}.
        :param integration_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#integration_account_name LogicAppIntegrationAccountAgreement#integration_account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#name LogicAppIntegrationAccountAgreement#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#resource_group_name LogicAppIntegrationAccountAgreement#resource_group_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#id LogicAppIntegrationAccountAgreement#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#metadata LogicAppIntegrationAccountAgreement#metadata}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#timeouts LogicAppIntegrationAccountAgreement#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(guest_identity, dict):
            guest_identity = LogicAppIntegrationAccountAgreementGuestIdentity(**guest_identity)
        if isinstance(host_identity, dict):
            host_identity = LogicAppIntegrationAccountAgreementHostIdentity(**host_identity)
        if isinstance(timeouts, dict):
            timeouts = LogicAppIntegrationAccountAgreementTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument agreement_type", value=agreement_type, expected_type=type_hints["agreement_type"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument guest_identity", value=guest_identity, expected_type=type_hints["guest_identity"])
            check_type(argname="argument guest_partner_name", value=guest_partner_name, expected_type=type_hints["guest_partner_name"])
            check_type(argname="argument host_identity", value=host_identity, expected_type=type_hints["host_identity"])
            check_type(argname="argument host_partner_name", value=host_partner_name, expected_type=type_hints["host_partner_name"])
            check_type(argname="argument integration_account_name", value=integration_account_name, expected_type=type_hints["integration_account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "agreement_type": agreement_type,
            "content": content,
            "guest_identity": guest_identity,
            "guest_partner_name": guest_partner_name,
            "host_identity": host_identity,
            "host_partner_name": host_partner_name,
            "integration_account_name": integration_account_name,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if metadata is not None:
            self._values["metadata"] = metadata
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
    def agreement_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#agreement_type LogicAppIntegrationAccountAgreement#agreement_type}.'''
        result = self._values.get("agreement_type")
        assert result is not None, "Required property 'agreement_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#content LogicAppIntegrationAccountAgreement#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def guest_identity(self) -> "LogicAppIntegrationAccountAgreementGuestIdentity":
        '''guest_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#guest_identity LogicAppIntegrationAccountAgreement#guest_identity}
        '''
        result = self._values.get("guest_identity")
        assert result is not None, "Required property 'guest_identity' is missing"
        return typing.cast("LogicAppIntegrationAccountAgreementGuestIdentity", result)

    @builtins.property
    def guest_partner_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#guest_partner_name LogicAppIntegrationAccountAgreement#guest_partner_name}.'''
        result = self._values.get("guest_partner_name")
        assert result is not None, "Required property 'guest_partner_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_identity(self) -> "LogicAppIntegrationAccountAgreementHostIdentity":
        '''host_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#host_identity LogicAppIntegrationAccountAgreement#host_identity}
        '''
        result = self._values.get("host_identity")
        assert result is not None, "Required property 'host_identity' is missing"
        return typing.cast("LogicAppIntegrationAccountAgreementHostIdentity", result)

    @builtins.property
    def host_partner_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#host_partner_name LogicAppIntegrationAccountAgreement#host_partner_name}.'''
        result = self._values.get("host_partner_name")
        assert result is not None, "Required property 'host_partner_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#integration_account_name LogicAppIntegrationAccountAgreement#integration_account_name}.'''
        result = self._values.get("integration_account_name")
        assert result is not None, "Required property 'integration_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#name LogicAppIntegrationAccountAgreement#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#resource_group_name LogicAppIntegrationAccountAgreement#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#id LogicAppIntegrationAccountAgreement#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#metadata LogicAppIntegrationAccountAgreement#metadata}.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["LogicAppIntegrationAccountAgreementTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#timeouts LogicAppIntegrationAccountAgreement#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LogicAppIntegrationAccountAgreementTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountAgreementConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementGuestIdentity",
    jsii_struct_bases=[],
    name_mapping={"qualifier": "qualifier", "value": "value"},
)
class LogicAppIntegrationAccountAgreementGuestIdentity:
    def __init__(self, *, qualifier: builtins.str, value: builtins.str) -> None:
        '''
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#qualifier LogicAppIntegrationAccountAgreement#qualifier}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#value LogicAppIntegrationAccountAgreement#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementGuestIdentity.__init__)
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "qualifier": qualifier,
            "value": value,
        }

    @builtins.property
    def qualifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#qualifier LogicAppIntegrationAccountAgreement#qualifier}.'''
        result = self._values.get("qualifier")
        assert result is not None, "Required property 'qualifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#value LogicAppIntegrationAccountAgreement#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountAgreementGuestIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppIntegrationAccountAgreementGuestIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementGuestIdentityOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementGuestIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementGuestIdentityOutputReference, "qualifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementGuestIdentityOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogicAppIntegrationAccountAgreementGuestIdentity]:
        return typing.cast(typing.Optional[LogicAppIntegrationAccountAgreementGuestIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppIntegrationAccountAgreementGuestIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementGuestIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementHostIdentity",
    jsii_struct_bases=[],
    name_mapping={"qualifier": "qualifier", "value": "value"},
)
class LogicAppIntegrationAccountAgreementHostIdentity:
    def __init__(self, *, qualifier: builtins.str, value: builtins.str) -> None:
        '''
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#qualifier LogicAppIntegrationAccountAgreement#qualifier}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#value LogicAppIntegrationAccountAgreement#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementHostIdentity.__init__)
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "qualifier": qualifier,
            "value": value,
        }

    @builtins.property
    def qualifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#qualifier LogicAppIntegrationAccountAgreement#qualifier}.'''
        result = self._values.get("qualifier")
        assert result is not None, "Required property 'qualifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#value LogicAppIntegrationAccountAgreement#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountAgreementHostIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppIntegrationAccountAgreementHostIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementHostIdentityOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementHostIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementHostIdentityOutputReference, "qualifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementHostIdentityOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LogicAppIntegrationAccountAgreementHostIdentity]:
        return typing.cast(typing.Optional[LogicAppIntegrationAccountAgreementHostIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LogicAppIntegrationAccountAgreementHostIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementHostIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LogicAppIntegrationAccountAgreementTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#create LogicAppIntegrationAccountAgreement#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#delete LogicAppIntegrationAccountAgreement#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#read LogicAppIntegrationAccountAgreement#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#update LogicAppIntegrationAccountAgreement#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#create LogicAppIntegrationAccountAgreement#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#delete LogicAppIntegrationAccountAgreement#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#read LogicAppIntegrationAccountAgreement#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/logic_app_integration_account_agreement#update LogicAppIntegrationAccountAgreement#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicAppIntegrationAccountAgreementTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogicAppIntegrationAccountAgreementTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logicAppIntegrationAccountAgreement.LogicAppIntegrationAccountAgreementTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LogicAppIntegrationAccountAgreementTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogicAppIntegrationAccountAgreementTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogicAppIntegrationAccountAgreementTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogicAppIntegrationAccountAgreementTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogicAppIntegrationAccountAgreementTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogicAppIntegrationAccountAgreement",
    "LogicAppIntegrationAccountAgreementConfig",
    "LogicAppIntegrationAccountAgreementGuestIdentity",
    "LogicAppIntegrationAccountAgreementGuestIdentityOutputReference",
    "LogicAppIntegrationAccountAgreementHostIdentity",
    "LogicAppIntegrationAccountAgreementHostIdentityOutputReference",
    "LogicAppIntegrationAccountAgreementTimeouts",
    "LogicAppIntegrationAccountAgreementTimeoutsOutputReference",
]

publication.publish()
