'''
# `azurerm_api_management_api_operation`

Refer to the Terraform Registory for docs: [`azurerm_api_management_api_operation`](https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation).
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


class ApiManagementApiOperation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation azurerm_api_management_api_operation}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_name: builtins.str,
        api_name: builtins.str,
        display_name: builtins.str,
        method: builtins.str,
        operation_id: builtins.str,
        resource_group_name: builtins.str,
        url_template: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        request: typing.Optional[typing.Union["ApiManagementApiOperationRequest", typing.Dict[str, typing.Any]]] = None,
        response: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponse", typing.Dict[str, typing.Any]]]]] = None,
        template_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationTemplateParameter", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementApiOperationTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation azurerm_api_management_api_operation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#api_management_name ApiManagementApiOperation#api_management_name}.
        :param api_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#api_name ApiManagementApiOperation#api_name}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#display_name ApiManagementApiOperation#display_name}.
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#method ApiManagementApiOperation#method}.
        :param operation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#operation_id ApiManagementApiOperation#operation_id}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#resource_group_name ApiManagementApiOperation#resource_group_name}.
        :param url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#url_template ApiManagementApiOperation#url_template}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#id ApiManagementApiOperation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param request: request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#request ApiManagementApiOperation#request}
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#response ApiManagementApiOperation#response}
        :param template_parameter: template_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#template_parameter ApiManagementApiOperation#template_parameter}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#timeouts ApiManagementApiOperation#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementApiOperationConfig(
            api_management_name=api_management_name,
            api_name=api_name,
            display_name=display_name,
            method=method,
            operation_id=operation_id,
            resource_group_name=resource_group_name,
            url_template=url_template,
            description=description,
            id=id,
            request=request,
            response=response,
            template_parameter=template_parameter,
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

    @jsii.member(jsii_name="putRequest")
    def put_request(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestHeader", typing.Dict[str, typing.Any]]]]] = None,
        query_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestQueryParameter", typing.Dict[str, typing.Any]]]]] = None,
        representation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestRepresentation", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#header ApiManagementApiOperation#header}
        :param query_parameter: query_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#query_parameter ApiManagementApiOperation#query_parameter}
        :param representation: representation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#representation ApiManagementApiOperation#representation}
        '''
        value = ApiManagementApiOperationRequest(
            description=description,
            header=header,
            query_parameter=query_parameter,
            representation=representation,
        )

        return typing.cast(None, jsii.invoke(self, "putRequest", [value]))

    @jsii.member(jsii_name="putResponse")
    def put_response(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponse", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperation.put_response)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponse", [value]))

    @jsii.member(jsii_name="putTemplateParameter")
    def put_template_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationTemplateParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperation.put_template_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTemplateParameter", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#create ApiManagementApiOperation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#delete ApiManagementApiOperation#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#read ApiManagementApiOperation#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#update ApiManagementApiOperation#update}.
        '''
        value = ApiManagementApiOperationTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRequest")
    def reset_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequest", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @jsii.member(jsii_name="resetTemplateParameter")
    def reset_template_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateParameter", []))

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
    @jsii.member(jsii_name="request")
    def request(self) -> "ApiManagementApiOperationRequestOutputReference":
        return typing.cast("ApiManagementApiOperationRequestOutputReference", jsii.get(self, "request"))

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> "ApiManagementApiOperationResponseList":
        return typing.cast("ApiManagementApiOperationResponseList", jsii.get(self, "response"))

    @builtins.property
    @jsii.member(jsii_name="templateParameter")
    def template_parameter(self) -> "ApiManagementApiOperationTemplateParameterList":
        return typing.cast("ApiManagementApiOperationTemplateParameterList", jsii.get(self, "templateParameter"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementApiOperationTimeoutsOutputReference":
        return typing.cast("ApiManagementApiOperationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementNameInput")
    def api_management_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiNameInput")
    def api_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiNameInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="operationIdInput")
    def operation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requestInput")
    def request_input(self) -> typing.Optional["ApiManagementApiOperationRequest"]:
        return typing.cast(typing.Optional["ApiManagementApiOperationRequest"], jsii.get(self, "requestInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponse"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponse"]]], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="templateParameterInput")
    def template_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationTemplateParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationTemplateParameter"]]], jsii.get(self, "templateParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementApiOperationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementApiOperationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlTemplateInput")
    def url_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementName")
    def api_management_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementName"))

    @api_management_name.setter
    def api_management_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "api_management_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementName", value)

    @builtins.property
    @jsii.member(jsii_name="apiName")
    def api_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiName"))

    @api_name.setter
    def api_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "api_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="operationId")
    def operation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationId"))

    @operation_id.setter
    def operation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "operation_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="urlTemplate")
    def url_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlTemplate"))

    @url_template.setter
    def url_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperation, "url_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlTemplate", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_management_name": "apiManagementName",
        "api_name": "apiName",
        "display_name": "displayName",
        "method": "method",
        "operation_id": "operationId",
        "resource_group_name": "resourceGroupName",
        "url_template": "urlTemplate",
        "description": "description",
        "id": "id",
        "request": "request",
        "response": "response",
        "template_parameter": "templateParameter",
        "timeouts": "timeouts",
    },
)
class ApiManagementApiOperationConfig(cdktf.TerraformMetaArguments):
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
        api_management_name: builtins.str,
        api_name: builtins.str,
        display_name: builtins.str,
        method: builtins.str,
        operation_id: builtins.str,
        resource_group_name: builtins.str,
        url_template: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        request: typing.Optional[typing.Union["ApiManagementApiOperationRequest", typing.Dict[str, typing.Any]]] = None,
        response: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponse", typing.Dict[str, typing.Any]]]]] = None,
        template_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationTemplateParameter", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementApiOperationTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#api_management_name ApiManagementApiOperation#api_management_name}.
        :param api_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#api_name ApiManagementApiOperation#api_name}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#display_name ApiManagementApiOperation#display_name}.
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#method ApiManagementApiOperation#method}.
        :param operation_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#operation_id ApiManagementApiOperation#operation_id}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#resource_group_name ApiManagementApiOperation#resource_group_name}.
        :param url_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#url_template ApiManagementApiOperation#url_template}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#id ApiManagementApiOperation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param request: request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#request ApiManagementApiOperation#request}
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#response ApiManagementApiOperation#response}
        :param template_parameter: template_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#template_parameter ApiManagementApiOperation#template_parameter}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#timeouts ApiManagementApiOperation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(request, dict):
            request = ApiManagementApiOperationRequest(**request)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementApiOperationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_management_name", value=api_management_name, expected_type=type_hints["api_management_name"])
            check_type(argname="argument api_name", value=api_name, expected_type=type_hints["api_name"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument operation_id", value=operation_id, expected_type=type_hints["operation_id"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument url_template", value=url_template, expected_type=type_hints["url_template"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
            check_type(argname="argument template_parameter", value=template_parameter, expected_type=type_hints["template_parameter"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_management_name": api_management_name,
            "api_name": api_name,
            "display_name": display_name,
            "method": method,
            "operation_id": operation_id,
            "resource_group_name": resource_group_name,
            "url_template": url_template,
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
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response
        if template_parameter is not None:
            self._values["template_parameter"] = template_parameter
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
    def api_management_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#api_management_name ApiManagementApiOperation#api_management_name}.'''
        result = self._values.get("api_management_name")
        assert result is not None, "Required property 'api_management_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#api_name ApiManagementApiOperation#api_name}.'''
        result = self._values.get("api_name")
        assert result is not None, "Required property 'api_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#display_name ApiManagementApiOperation#display_name}.'''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#method ApiManagementApiOperation#method}.'''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operation_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#operation_id ApiManagementApiOperation#operation_id}.'''
        result = self._values.get("operation_id")
        assert result is not None, "Required property 'operation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#resource_group_name ApiManagementApiOperation#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url_template(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#url_template ApiManagementApiOperation#url_template}.'''
        result = self._values.get("url_template")
        assert result is not None, "Required property 'url_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#id ApiManagementApiOperation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request(self) -> typing.Optional["ApiManagementApiOperationRequest"]:
        '''request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#request ApiManagementApiOperation#request}
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional["ApiManagementApiOperationRequest"], result)

    @builtins.property
    def response(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponse"]]]:
        '''response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#response ApiManagementApiOperation#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponse"]]], result)

    @builtins.property
    def template_parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationTemplateParameter"]]]:
        '''template_parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#template_parameter ApiManagementApiOperation#template_parameter}
        '''
        result = self._values.get("template_parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationTemplateParameter"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementApiOperationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#timeouts ApiManagementApiOperation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementApiOperationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequest",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "header": "header",
        "query_parameter": "queryParameter",
        "representation": "representation",
    },
)
class ApiManagementApiOperationRequest:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestHeader", typing.Dict[str, typing.Any]]]]] = None,
        query_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestQueryParameter", typing.Dict[str, typing.Any]]]]] = None,
        representation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestRepresentation", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#header ApiManagementApiOperation#header}
        :param query_parameter: query_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#query_parameter ApiManagementApiOperation#query_parameter}
        :param representation: representation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#representation ApiManagementApiOperation#representation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequest.__init__)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument query_parameter", value=query_parameter, expected_type=type_hints["query_parameter"])
            check_type(argname="argument representation", value=representation, expected_type=type_hints["representation"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if header is not None:
            self._values["header"] = header
        if query_parameter is not None:
            self._values["query_parameter"] = query_parameter
        if representation is not None:
            self._values["representation"] = representation

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#header ApiManagementApiOperation#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestHeader"]]], result)

    @builtins.property
    def query_parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestQueryParameter"]]]:
        '''query_parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#query_parameter ApiManagementApiOperation#query_parameter}
        '''
        result = self._values.get("query_parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestQueryParameter"]]], result)

    @builtins.property
    def representation(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentation"]]]:
        '''representation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#representation ApiManagementApiOperation#representation}
        '''
        result = self._values.get("representation")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentation"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestHeader",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "required": "required",
        "type": "type",
        "default_value": "defaultValue",
        "description": "description",
        "example": "example",
        "schema_id": "schemaId",
        "type_name": "typeName",
        "values": "values",
    },
)
class ApiManagementApiOperationRequestHeader:
    def __init__(
        self,
        *,
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        type: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestHeaderExample", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "required": required,
            "type": type,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if description is not None:
            self._values["description"] = description
        if example is not None:
            self._values["example"] = example
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestHeaderExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestHeaderExample"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestHeaderExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationRequestHeaderExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestHeaderExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationRequestHeaderExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestHeaderExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestHeaderExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestHeaderExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeaderExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeaderExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeaderExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestHeaderExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestHeaderExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestHeaderExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestHeaderExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestHeaderExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestHeaderList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestHeaderOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationRequestHeaderExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestHeaderOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> ApiManagementApiOperationRequestHeaderExampleList:
        return typing.cast(ApiManagementApiOperationRequestHeaderExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeaderExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeaderExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "default_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationRequestHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putQueryParameter")
    def put_query_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestQueryParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestOutputReference.put_query_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParameter", [value]))

    @jsii.member(jsii_name="putRepresentation")
    def put_representation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestRepresentation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestOutputReference.put_representation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRepresentation", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetQueryParameter")
    def reset_query_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParameter", []))

    @jsii.member(jsii_name="resetRepresentation")
    def reset_representation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepresentation", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> ApiManagementApiOperationRequestHeaderList:
        return typing.cast(ApiManagementApiOperationRequestHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="queryParameter")
    def query_parameter(self) -> "ApiManagementApiOperationRequestQueryParameterList":
        return typing.cast("ApiManagementApiOperationRequestQueryParameterList", jsii.get(self, "queryParameter"))

    @builtins.property
    @jsii.member(jsii_name="representation")
    def representation(self) -> "ApiManagementApiOperationRequestRepresentationList":
        return typing.cast("ApiManagementApiOperationRequestRepresentationList", jsii.get(self, "representation"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParameterInput")
    def query_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestQueryParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestQueryParameter"]]], jsii.get(self, "queryParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="representationInput")
    def representation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentation"]]], jsii.get(self, "representationInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementApiOperationRequest]:
        return typing.cast(typing.Optional[ApiManagementApiOperationRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiOperationRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestQueryParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "required": "required",
        "type": "type",
        "default_value": "defaultValue",
        "description": "description",
        "example": "example",
        "schema_id": "schemaId",
        "type_name": "typeName",
        "values": "values",
    },
)
class ApiManagementApiOperationRequestQueryParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        type: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestQueryParameterExample", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "required": required,
            "type": type,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if description is not None:
            self._values["description"] = description
        if example is not None:
            self._values["example"] = example
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestQueryParameterExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestQueryParameterExample"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestQueryParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestQueryParameterExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationRequestQueryParameterExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestQueryParameterExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationRequestQueryParameterExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestQueryParameterExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestQueryParameterExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestQueryParameterExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameterExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameterExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestQueryParameterExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestQueryParameterExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestQueryParameterExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestQueryParameterExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestQueryParameterExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestQueryParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestQueryParameterList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestQueryParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestQueryParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestQueryParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestQueryParameterOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationRequestQueryParameterExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestQueryParameterOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> ApiManagementApiOperationRequestQueryParameterExampleList:
        return typing.cast(ApiManagementApiOperationRequestQueryParameterExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestQueryParameterExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "default_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestQueryParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestQueryParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestQueryParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestQueryParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentation",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "example": "example",
        "form_parameter": "formParameter",
        "schema_id": "schemaId",
        "type_name": "typeName",
    },
)
class ApiManagementApiOperationRequestRepresentation:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestRepresentationExample", typing.Dict[str, typing.Any]]]]] = None,
        form_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestRepresentationFormParameter", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#content_type ApiManagementApiOperation#content_type}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param form_parameter: form_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#form_parameter ApiManagementApiOperation#form_parameter}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentation.__init__)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument form_parameter", value=form_parameter, expected_type=type_hints["form_parameter"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type": content_type,
        }
        if example is not None:
            self._values["example"] = example
        if form_parameter is not None:
            self._values["form_parameter"] = form_parameter
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#content_type ApiManagementApiOperation#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentationExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentationExample"]]], result)

    @builtins.property
    def form_parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentationFormParameter"]]]:
        '''form_parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#form_parameter ApiManagementApiOperation#form_parameter}
        '''
        result = self._values.get("form_parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentationFormParameter"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestRepresentation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationRequestRepresentationExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestRepresentationExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationRequestRepresentationExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestRepresentationExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestRepresentationExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestRepresentationExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationFormParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "required": "required",
        "type": "type",
        "default_value": "defaultValue",
        "description": "description",
        "example": "example",
        "schema_id": "schemaId",
        "type_name": "typeName",
        "values": "values",
    },
)
class ApiManagementApiOperationRequestRepresentationFormParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        type: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationRequestRepresentationFormParameterExample", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "required": required,
            "type": type,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if description is not None:
            self._values["description"] = description
        if example is not None:
            self._values["example"] = example
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentationFormParameterExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationRequestRepresentationFormParameterExample"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestRepresentationFormParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationFormParameterExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationRequestRepresentationFormParameterExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationRequestRepresentationFormParameterExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationRequestRepresentationFormParameterExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationFormParameterExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameterExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameterExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameterExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameterExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameterExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestRepresentationFormParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationFormParameterList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestRepresentationFormParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestRepresentationFormParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestRepresentationFormParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationFormParameterOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameterExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(
        self,
    ) -> ApiManagementApiOperationRequestRepresentationFormParameterExampleList:
        return typing.cast(ApiManagementApiOperationRequestRepresentationFormParameterExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameterExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "default_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationFormParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestRepresentationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationRequestRepresentationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationRequestRepresentationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationRequestRepresentationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationRequestRepresentationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationRequestRepresentationExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="putFormParameter")
    def put_form_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationRequestRepresentationFormParameter, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationRequestRepresentationOutputReference.put_form_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFormParameter", [value]))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetFormParameter")
    def reset_form_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormParameter", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> ApiManagementApiOperationRequestRepresentationExampleList:
        return typing.cast(ApiManagementApiOperationRequestRepresentationExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="formParameter")
    def form_parameter(
        self,
    ) -> ApiManagementApiOperationRequestRepresentationFormParameterList:
        return typing.cast(ApiManagementApiOperationRequestRepresentationFormParameterList, jsii.get(self, "formParameter"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="formParameterInput")
    def form_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationRequestRepresentationFormParameter]]], jsii.get(self, "formParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationRequestRepresentation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationRequestRepresentationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponse",
    jsii_struct_bases=[],
    name_mapping={
        "status_code": "statusCode",
        "description": "description",
        "header": "header",
        "representation": "representation",
    },
)
class ApiManagementApiOperationResponse:
    def __init__(
        self,
        *,
        status_code: jsii.Number,
        description: typing.Optional[builtins.str] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseHeader", typing.Dict[str, typing.Any]]]]] = None,
        representation: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseRepresentation", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#status_code ApiManagementApiOperation#status_code}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#header ApiManagementApiOperation#header}
        :param representation: representation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#representation ApiManagementApiOperation#representation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponse.__init__)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument representation", value=representation, expected_type=type_hints["representation"])
        self._values: typing.Dict[str, typing.Any] = {
            "status_code": status_code,
        }
        if description is not None:
            self._values["description"] = description
        if header is not None:
            self._values["header"] = header
        if representation is not None:
            self._values["representation"] = representation

    @builtins.property
    def status_code(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#status_code ApiManagementApiOperation#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#header ApiManagementApiOperation#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseHeader"]]], result)

    @builtins.property
    def representation(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentation"]]]:
        '''representation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#representation ApiManagementApiOperation#representation}
        '''
        result = self._values.get("representation")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentation"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseHeader",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "required": "required",
        "type": "type",
        "default_value": "defaultValue",
        "description": "description",
        "example": "example",
        "schema_id": "schemaId",
        "type_name": "typeName",
        "values": "values",
    },
)
class ApiManagementApiOperationResponseHeader:
    def __init__(
        self,
        *,
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        type: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseHeaderExample", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "required": required,
            "type": type,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if description is not None:
            self._values["description"] = description
        if example is not None:
            self._values["example"] = example
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseHeaderExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseHeaderExample"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponseHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseHeaderExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationResponseHeaderExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponseHeaderExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationResponseHeaderExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseHeaderExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseHeaderExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseHeaderExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeaderExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeaderExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeaderExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseHeaderExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseHeaderExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponseHeaderExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponseHeaderExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponseHeaderExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseHeaderList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseHeaderOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationResponseHeaderExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseHeaderOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> ApiManagementApiOperationResponseHeaderExampleList:
        return typing.cast(ApiManagementApiOperationResponseHeaderExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeaderExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeaderExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "default_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponseHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponseHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponseHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponse]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponse]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponse]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationResponseHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putRepresentation")
    def put_representation(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseRepresentation", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseOutputReference.put_representation)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRepresentation", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetRepresentation")
    def reset_representation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepresentation", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> ApiManagementApiOperationResponseHeaderList:
        return typing.cast(ApiManagementApiOperationResponseHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="representation")
    def representation(self) -> "ApiManagementApiOperationResponseRepresentationList":
        return typing.cast("ApiManagementApiOperationResponseRepresentationList", jsii.get(self, "representation"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="representationInput")
    def representation_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentation"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentation"]]], jsii.get(self, "representationInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponse, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponse, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponse, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentation",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "example": "example",
        "form_parameter": "formParameter",
        "schema_id": "schemaId",
        "type_name": "typeName",
    },
)
class ApiManagementApiOperationResponseRepresentation:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseRepresentationExample", typing.Dict[str, typing.Any]]]]] = None,
        form_parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseRepresentationFormParameter", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#content_type ApiManagementApiOperation#content_type}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param form_parameter: form_parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#form_parameter ApiManagementApiOperation#form_parameter}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentation.__init__)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument form_parameter", value=form_parameter, expected_type=type_hints["form_parameter"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type": content_type,
        }
        if example is not None:
            self._values["example"] = example
        if form_parameter is not None:
            self._values["form_parameter"] = form_parameter
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#content_type ApiManagementApiOperation#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentationExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentationExample"]]], result)

    @builtins.property
    def form_parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentationFormParameter"]]]:
        '''form_parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#form_parameter ApiManagementApiOperation#form_parameter}
        '''
        result = self._values.get("form_parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentationFormParameter"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponseRepresentation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationResponseRepresentationExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponseRepresentationExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationResponseRepresentationExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseRepresentationExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseRepresentationExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseRepresentationExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationFormParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "required": "required",
        "type": "type",
        "default_value": "defaultValue",
        "description": "description",
        "example": "example",
        "schema_id": "schemaId",
        "type_name": "typeName",
        "values": "values",
    },
)
class ApiManagementApiOperationResponseRepresentationFormParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        type: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationResponseRepresentationFormParameterExample", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "required": required,
            "type": type,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if description is not None:
            self._values["description"] = description
        if example is not None:
            self._values["example"] = example
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentationFormParameterExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationResponseRepresentationFormParameterExample"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponseRepresentationFormParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationFormParameterExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationResponseRepresentationFormParameterExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationResponseRepresentationFormParameterExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationResponseRepresentationFormParameterExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationFormParameterExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameterExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameterExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameterExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameterExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameterExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseRepresentationFormParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationFormParameterList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseRepresentationFormParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseRepresentationFormParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseRepresentationFormParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationFormParameterOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameterExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(
        self,
    ) -> ApiManagementApiOperationResponseRepresentationFormParameterExampleList:
        return typing.cast(ApiManagementApiOperationResponseRepresentationFormParameterExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameterExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "default_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationFormParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseRepresentationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationResponseRepresentationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationResponseRepresentationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentation]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationResponseRepresentationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationResponseRepresentationOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationResponseRepresentationExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="putFormParameter")
    def put_form_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationResponseRepresentationFormParameter, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationResponseRepresentationOutputReference.put_form_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFormParameter", [value]))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetFormParameter")
    def reset_form_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormParameter", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> ApiManagementApiOperationResponseRepresentationExampleList:
        return typing.cast(ApiManagementApiOperationResponseRepresentationExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="formParameter")
    def form_parameter(
        self,
    ) -> ApiManagementApiOperationResponseRepresentationFormParameterList:
        return typing.cast(ApiManagementApiOperationResponseRepresentationFormParameterList, jsii.get(self, "formParameter"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="formParameterInput")
    def form_parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationResponseRepresentationFormParameter]]], jsii.get(self, "formParameterInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentation, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentation, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationResponseRepresentation, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationResponseRepresentationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTemplateParameter",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "required": "required",
        "type": "type",
        "default_value": "defaultValue",
        "description": "description",
        "example": "example",
        "schema_id": "schemaId",
        "type_name": "typeName",
        "values": "values",
    },
)
class ApiManagementApiOperationTemplateParameter:
    def __init__(
        self,
        *,
        name: builtins.str,
        required: typing.Union[builtins.bool, cdktf.IResolvable],
        type: builtins.str,
        default_value: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        example: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiOperationTemplateParameterExample", typing.Dict[str, typing.Any]]]]] = None,
        schema_id: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.
        :param default_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param example: example block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        :param schema_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.
        :param type_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameter.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument example", value=example, expected_type=type_hints["example"])
            check_type(argname="argument schema_id", value=schema_id, expected_type=type_hints["schema_id"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "required": required,
            "type": type,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if description is not None:
            self._values["description"] = description
        if example is not None:
            self._values["example"] = example
        if schema_id is not None:
            self._values["schema_id"] = schema_id
        if type_name is not None:
            self._values["type_name"] = type_name
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#required ApiManagementApiOperation#required}.'''
        result = self._values.get("required")
        assert result is not None, "Required property 'required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type ApiManagementApiOperation#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#default_value ApiManagementApiOperation#default_value}.'''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def example(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationTemplateParameterExample"]]]:
        '''example block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#example ApiManagementApiOperation#example}
        '''
        result = self._values.get("example")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiOperationTemplateParameterExample"]]], result)

    @builtins.property
    def schema_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#schema_id ApiManagementApiOperation#schema_id}.'''
        result = self._values.get("schema_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#type_name ApiManagementApiOperation#type_name}.'''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#values ApiManagementApiOperation#values}.'''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationTemplateParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTemplateParameterExample",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "external_value": "externalValue",
        "summary": "summary",
        "value": "value",
    },
)
class ApiManagementApiOperationTemplateParameterExample:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        external_value: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.
        :param external_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.
        :param summary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterExample.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument external_value", value=external_value, expected_type=type_hints["external_value"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if external_value is not None:
            self._values["external_value"] = external_value
        if summary is not None:
            self._values["summary"] = summary
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#name ApiManagementApiOperation#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#description ApiManagementApiOperation#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#external_value ApiManagementApiOperation#external_value}.'''
        result = self._values.get("external_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#summary ApiManagementApiOperation#summary}.'''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#value ApiManagementApiOperation#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationTemplateParameterExample(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationTemplateParameterExampleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTemplateParameterExampleList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterExampleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationTemplateParameterExampleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterExampleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationTemplateParameterExampleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameterExample]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameterExample]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationTemplateParameterExampleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTemplateParameterExampleOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterExampleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExternalValue")
    def reset_external_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalValue", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalValueInput")
    def external_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalValueInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="externalValue")
    def external_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalValue"))

    @external_value.setter
    def external_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleOutputReference, "external_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleOutputReference, "summary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationTemplateParameterExample, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationTemplateParameterExample, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationTemplateParameterExample, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterExampleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationTemplateParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTemplateParameterList",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiOperationTemplateParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiOperationTemplateParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiOperationTemplateParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTemplateParameterOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExample")
    def put_example(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiOperationTemplateParameterExample, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationTemplateParameterOutputReference.put_example)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExample", [value]))

    @jsii.member(jsii_name="resetDefaultValue")
    def reset_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultValue", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExample")
    def reset_example(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExample", []))

    @jsii.member(jsii_name="resetSchemaId")
    def reset_schema_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaId", []))

    @jsii.member(jsii_name="resetTypeName")
    def reset_type_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeName", []))

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="example")
    def example(self) -> ApiManagementApiOperationTemplateParameterExampleList:
        return typing.cast(ApiManagementApiOperationTemplateParameterExampleList, jsii.get(self, "example"))

    @builtins.property
    @jsii.member(jsii_name="defaultValueInput")
    def default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultValueInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="exampleInput")
    def example_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameterExample]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiOperationTemplateParameterExample]]], jsii.get(self, "exampleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaIdInput")
    def schema_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeNameInput")
    def type_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "default_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="schemaId")
    def schema_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaId"))

    @schema_id.setter
    def schema_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "schema_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "type_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationTemplateParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationTemplateParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationTemplateParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTemplateParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementApiOperationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#create ApiManagementApiOperation#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#delete ApiManagementApiOperation#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#read ApiManagementApiOperation#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#update ApiManagementApiOperation#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiOperationTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#create ApiManagementApiOperation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#delete ApiManagementApiOperation#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#read ApiManagementApiOperation#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_operation#update ApiManagementApiOperation#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiOperationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiOperationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiOperation.ApiManagementApiOperationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiOperationTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiOperationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiOperationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiOperationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiOperationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementApiOperation",
    "ApiManagementApiOperationConfig",
    "ApiManagementApiOperationRequest",
    "ApiManagementApiOperationRequestHeader",
    "ApiManagementApiOperationRequestHeaderExample",
    "ApiManagementApiOperationRequestHeaderExampleList",
    "ApiManagementApiOperationRequestHeaderExampleOutputReference",
    "ApiManagementApiOperationRequestHeaderList",
    "ApiManagementApiOperationRequestHeaderOutputReference",
    "ApiManagementApiOperationRequestOutputReference",
    "ApiManagementApiOperationRequestQueryParameter",
    "ApiManagementApiOperationRequestQueryParameterExample",
    "ApiManagementApiOperationRequestQueryParameterExampleList",
    "ApiManagementApiOperationRequestQueryParameterExampleOutputReference",
    "ApiManagementApiOperationRequestQueryParameterList",
    "ApiManagementApiOperationRequestQueryParameterOutputReference",
    "ApiManagementApiOperationRequestRepresentation",
    "ApiManagementApiOperationRequestRepresentationExample",
    "ApiManagementApiOperationRequestRepresentationExampleList",
    "ApiManagementApiOperationRequestRepresentationExampleOutputReference",
    "ApiManagementApiOperationRequestRepresentationFormParameter",
    "ApiManagementApiOperationRequestRepresentationFormParameterExample",
    "ApiManagementApiOperationRequestRepresentationFormParameterExampleList",
    "ApiManagementApiOperationRequestRepresentationFormParameterExampleOutputReference",
    "ApiManagementApiOperationRequestRepresentationFormParameterList",
    "ApiManagementApiOperationRequestRepresentationFormParameterOutputReference",
    "ApiManagementApiOperationRequestRepresentationList",
    "ApiManagementApiOperationRequestRepresentationOutputReference",
    "ApiManagementApiOperationResponse",
    "ApiManagementApiOperationResponseHeader",
    "ApiManagementApiOperationResponseHeaderExample",
    "ApiManagementApiOperationResponseHeaderExampleList",
    "ApiManagementApiOperationResponseHeaderExampleOutputReference",
    "ApiManagementApiOperationResponseHeaderList",
    "ApiManagementApiOperationResponseHeaderOutputReference",
    "ApiManagementApiOperationResponseList",
    "ApiManagementApiOperationResponseOutputReference",
    "ApiManagementApiOperationResponseRepresentation",
    "ApiManagementApiOperationResponseRepresentationExample",
    "ApiManagementApiOperationResponseRepresentationExampleList",
    "ApiManagementApiOperationResponseRepresentationExampleOutputReference",
    "ApiManagementApiOperationResponseRepresentationFormParameter",
    "ApiManagementApiOperationResponseRepresentationFormParameterExample",
    "ApiManagementApiOperationResponseRepresentationFormParameterExampleList",
    "ApiManagementApiOperationResponseRepresentationFormParameterExampleOutputReference",
    "ApiManagementApiOperationResponseRepresentationFormParameterList",
    "ApiManagementApiOperationResponseRepresentationFormParameterOutputReference",
    "ApiManagementApiOperationResponseRepresentationList",
    "ApiManagementApiOperationResponseRepresentationOutputReference",
    "ApiManagementApiOperationTemplateParameter",
    "ApiManagementApiOperationTemplateParameterExample",
    "ApiManagementApiOperationTemplateParameterExampleList",
    "ApiManagementApiOperationTemplateParameterExampleOutputReference",
    "ApiManagementApiOperationTemplateParameterList",
    "ApiManagementApiOperationTemplateParameterOutputReference",
    "ApiManagementApiOperationTimeouts",
    "ApiManagementApiOperationTimeoutsOutputReference",
]

publication.publish()
