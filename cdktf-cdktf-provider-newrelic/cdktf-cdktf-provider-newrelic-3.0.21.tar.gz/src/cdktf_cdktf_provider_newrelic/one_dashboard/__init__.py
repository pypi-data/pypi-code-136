'''
# `newrelic_one_dashboard`

Refer to the Terraform Registory for docs: [`newrelic_one_dashboard`](https://www.terraform.io/docs/providers/newrelic/r/one_dashboard).
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


class OneDashboard(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboard",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard newrelic_one_dashboard}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        page: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPage", typing.Dict[str, typing.Any]]]],
        account_id: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard newrelic_one_dashboard} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The dashboard's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#name OneDashboard#name}
        :param page: page block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#page OneDashboard#page}
        :param account_id: The New Relic account ID where you want to create the dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        :param description: The dashboard's description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#description OneDashboard#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#id OneDashboard#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permissions: Determines who can see or edit the dashboard. Valid values are private, public_read_only, public_read_write. Defaults to public_read_only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#permissions OneDashboard#permissions}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboard.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OneDashboardConfig(
            name=name,
            page=page,
            account_id=account_id,
            description=description,
            id=id,
            permissions=permissions,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPage")
    def put_page(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPage", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboard.put_page)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPage", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @builtins.property
    @jsii.member(jsii_name="page")
    def page(self) -> "OneDashboardPageList":
        return typing.cast("OneDashboardPageList", jsii.get(self, "page"))

    @builtins.property
    @jsii.member(jsii_name="permalink")
    def permalink(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permalink"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pageInput")
    def page_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPage"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPage"]]], jsii.get(self, "pageInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboard, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboard, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboard, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboard, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboard, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "page": "page",
        "account_id": "accountId",
        "description": "description",
        "id": "id",
        "permissions": "permissions",
    },
)
class OneDashboardConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        page: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPage", typing.Dict[str, typing.Any]]]],
        account_id: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The dashboard's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#name OneDashboard#name}
        :param page: page block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#page OneDashboard#page}
        :param account_id: The New Relic account ID where you want to create the dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        :param description: The dashboard's description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#description OneDashboard#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#id OneDashboard#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param permissions: Determines who can see or edit the dashboard. Valid values are private, public_read_only, public_read_write. Defaults to public_read_only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#permissions OneDashboard#permissions}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument page", value=page, expected_type=type_hints["page"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "page": page,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if permissions is not None:
            self._values["permissions"] = permissions

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
    def name(self) -> builtins.str:
        '''The dashboard's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#name OneDashboard#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def page(self) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPage"]]:
        '''page block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#page OneDashboard#page}
        '''
        result = self._values.get("page")
        assert result is not None, "Required property 'page' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPage"]], result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The New Relic account ID where you want to create the dashboard.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The dashboard's description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#description OneDashboard#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#id OneDashboard#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''Determines who can see or edit the dashboard. Valid values are private, public_read_only, public_read_write. Defaults to public_read_only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#permissions OneDashboard#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPage",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "widget_area": "widgetArea",
        "widget_bar": "widgetBar",
        "widget_billboard": "widgetBillboard",
        "widget_bullet": "widgetBullet",
        "widget_funnel": "widgetFunnel",
        "widget_heatmap": "widgetHeatmap",
        "widget_histogram": "widgetHistogram",
        "widget_json": "widgetJson",
        "widget_line": "widgetLine",
        "widget_log_table": "widgetLogTable",
        "widget_markdown": "widgetMarkdown",
        "widget_pie": "widgetPie",
        "widget_stacked_bar": "widgetStackedBar",
        "widget_table": "widgetTable",
    },
)
class OneDashboardPage:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        widget_area: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetArea", typing.Dict[str, typing.Any]]]]] = None,
        widget_bar: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBar", typing.Dict[str, typing.Any]]]]] = None,
        widget_billboard: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBillboard", typing.Dict[str, typing.Any]]]]] = None,
        widget_bullet: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBullet", typing.Dict[str, typing.Any]]]]] = None,
        widget_funnel: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetFunnel", typing.Dict[str, typing.Any]]]]] = None,
        widget_heatmap: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetHeatmap", typing.Dict[str, typing.Any]]]]] = None,
        widget_histogram: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetHistogram", typing.Dict[str, typing.Any]]]]] = None,
        widget_json: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetJson", typing.Dict[str, typing.Any]]]]] = None,
        widget_line: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetLine", typing.Dict[str, typing.Any]]]]] = None,
        widget_log_table: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetLogTable", typing.Dict[str, typing.Any]]]]] = None,
        widget_markdown: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetMarkdown", typing.Dict[str, typing.Any]]]]] = None,
        widget_pie: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetPie", typing.Dict[str, typing.Any]]]]] = None,
        widget_stacked_bar: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetStackedBar", typing.Dict[str, typing.Any]]]]] = None,
        widget_table: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetTable", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: The dashboard page's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#name OneDashboard#name}
        :param description: The dashboard page's description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#description OneDashboard#description}
        :param widget_area: widget_area block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_area OneDashboard#widget_area}
        :param widget_bar: widget_bar block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_bar OneDashboard#widget_bar}
        :param widget_billboard: widget_billboard block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_billboard OneDashboard#widget_billboard}
        :param widget_bullet: widget_bullet block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_bullet OneDashboard#widget_bullet}
        :param widget_funnel: widget_funnel block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_funnel OneDashboard#widget_funnel}
        :param widget_heatmap: widget_heatmap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_heatmap OneDashboard#widget_heatmap}
        :param widget_histogram: widget_histogram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_histogram OneDashboard#widget_histogram}
        :param widget_json: widget_json block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_json OneDashboard#widget_json}
        :param widget_line: widget_line block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_line OneDashboard#widget_line}
        :param widget_log_table: widget_log_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_log_table OneDashboard#widget_log_table}
        :param widget_markdown: widget_markdown block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_markdown OneDashboard#widget_markdown}
        :param widget_pie: widget_pie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_pie OneDashboard#widget_pie}
        :param widget_stacked_bar: widget_stacked_bar block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_stacked_bar OneDashboard#widget_stacked_bar}
        :param widget_table: widget_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_table OneDashboard#widget_table}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPage.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument widget_area", value=widget_area, expected_type=type_hints["widget_area"])
            check_type(argname="argument widget_bar", value=widget_bar, expected_type=type_hints["widget_bar"])
            check_type(argname="argument widget_billboard", value=widget_billboard, expected_type=type_hints["widget_billboard"])
            check_type(argname="argument widget_bullet", value=widget_bullet, expected_type=type_hints["widget_bullet"])
            check_type(argname="argument widget_funnel", value=widget_funnel, expected_type=type_hints["widget_funnel"])
            check_type(argname="argument widget_heatmap", value=widget_heatmap, expected_type=type_hints["widget_heatmap"])
            check_type(argname="argument widget_histogram", value=widget_histogram, expected_type=type_hints["widget_histogram"])
            check_type(argname="argument widget_json", value=widget_json, expected_type=type_hints["widget_json"])
            check_type(argname="argument widget_line", value=widget_line, expected_type=type_hints["widget_line"])
            check_type(argname="argument widget_log_table", value=widget_log_table, expected_type=type_hints["widget_log_table"])
            check_type(argname="argument widget_markdown", value=widget_markdown, expected_type=type_hints["widget_markdown"])
            check_type(argname="argument widget_pie", value=widget_pie, expected_type=type_hints["widget_pie"])
            check_type(argname="argument widget_stacked_bar", value=widget_stacked_bar, expected_type=type_hints["widget_stacked_bar"])
            check_type(argname="argument widget_table", value=widget_table, expected_type=type_hints["widget_table"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if widget_area is not None:
            self._values["widget_area"] = widget_area
        if widget_bar is not None:
            self._values["widget_bar"] = widget_bar
        if widget_billboard is not None:
            self._values["widget_billboard"] = widget_billboard
        if widget_bullet is not None:
            self._values["widget_bullet"] = widget_bullet
        if widget_funnel is not None:
            self._values["widget_funnel"] = widget_funnel
        if widget_heatmap is not None:
            self._values["widget_heatmap"] = widget_heatmap
        if widget_histogram is not None:
            self._values["widget_histogram"] = widget_histogram
        if widget_json is not None:
            self._values["widget_json"] = widget_json
        if widget_line is not None:
            self._values["widget_line"] = widget_line
        if widget_log_table is not None:
            self._values["widget_log_table"] = widget_log_table
        if widget_markdown is not None:
            self._values["widget_markdown"] = widget_markdown
        if widget_pie is not None:
            self._values["widget_pie"] = widget_pie
        if widget_stacked_bar is not None:
            self._values["widget_stacked_bar"] = widget_stacked_bar
        if widget_table is not None:
            self._values["widget_table"] = widget_table

    @builtins.property
    def name(self) -> builtins.str:
        '''The dashboard page's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#name OneDashboard#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The dashboard page's description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#description OneDashboard#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def widget_area(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetArea"]]]:
        '''widget_area block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_area OneDashboard#widget_area}
        '''
        result = self._values.get("widget_area")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetArea"]]], result)

    @builtins.property
    def widget_bar(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBar"]]]:
        '''widget_bar block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_bar OneDashboard#widget_bar}
        '''
        result = self._values.get("widget_bar")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBar"]]], result)

    @builtins.property
    def widget_billboard(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBillboard"]]]:
        '''widget_billboard block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_billboard OneDashboard#widget_billboard}
        '''
        result = self._values.get("widget_billboard")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBillboard"]]], result)

    @builtins.property
    def widget_bullet(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBullet"]]]:
        '''widget_bullet block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_bullet OneDashboard#widget_bullet}
        '''
        result = self._values.get("widget_bullet")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBullet"]]], result)

    @builtins.property
    def widget_funnel(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetFunnel"]]]:
        '''widget_funnel block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_funnel OneDashboard#widget_funnel}
        '''
        result = self._values.get("widget_funnel")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetFunnel"]]], result)

    @builtins.property
    def widget_heatmap(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHeatmap"]]]:
        '''widget_heatmap block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_heatmap OneDashboard#widget_heatmap}
        '''
        result = self._values.get("widget_heatmap")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHeatmap"]]], result)

    @builtins.property
    def widget_histogram(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHistogram"]]]:
        '''widget_histogram block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_histogram OneDashboard#widget_histogram}
        '''
        result = self._values.get("widget_histogram")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHistogram"]]], result)

    @builtins.property
    def widget_json(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetJson"]]]:
        '''widget_json block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_json OneDashboard#widget_json}
        '''
        result = self._values.get("widget_json")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetJson"]]], result)

    @builtins.property
    def widget_line(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLine"]]]:
        '''widget_line block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_line OneDashboard#widget_line}
        '''
        result = self._values.get("widget_line")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLine"]]], result)

    @builtins.property
    def widget_log_table(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLogTable"]]]:
        '''widget_log_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_log_table OneDashboard#widget_log_table}
        '''
        result = self._values.get("widget_log_table")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLogTable"]]], result)

    @builtins.property
    def widget_markdown(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetMarkdown"]]]:
        '''widget_markdown block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_markdown OneDashboard#widget_markdown}
        '''
        result = self._values.get("widget_markdown")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetMarkdown"]]], result)

    @builtins.property
    def widget_pie(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetPie"]]]:
        '''widget_pie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_pie OneDashboard#widget_pie}
        '''
        result = self._values.get("widget_pie")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetPie"]]], result)

    @builtins.property
    def widget_stacked_bar(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetStackedBar"]]]:
        '''widget_stacked_bar block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_stacked_bar OneDashboard#widget_stacked_bar}
        '''
        result = self._values.get("widget_stacked_bar")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetStackedBar"]]], result)

    @builtins.property
    def widget_table(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetTable"]]]:
        '''widget_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#widget_table OneDashboard#widget_table}
        '''
        result = self._values.get("widget_table")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetTable"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageList",
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
            type_hints = typing.get_type_hints(OneDashboardPageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putWidgetArea")
    def put_widget_area(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetArea", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_area)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetArea", [value]))

    @jsii.member(jsii_name="putWidgetBar")
    def put_widget_bar(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBar", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_bar)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetBar", [value]))

    @jsii.member(jsii_name="putWidgetBillboard")
    def put_widget_billboard(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBillboard", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_billboard)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetBillboard", [value]))

    @jsii.member(jsii_name="putWidgetBullet")
    def put_widget_bullet(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBullet", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_bullet)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetBullet", [value]))

    @jsii.member(jsii_name="putWidgetFunnel")
    def put_widget_funnel(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetFunnel", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_funnel)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetFunnel", [value]))

    @jsii.member(jsii_name="putWidgetHeatmap")
    def put_widget_heatmap(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetHeatmap", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_heatmap)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetHeatmap", [value]))

    @jsii.member(jsii_name="putWidgetHistogram")
    def put_widget_histogram(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetHistogram", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_histogram)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetHistogram", [value]))

    @jsii.member(jsii_name="putWidgetJson")
    def put_widget_json(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetJson", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_json)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetJson", [value]))

    @jsii.member(jsii_name="putWidgetLine")
    def put_widget_line(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetLine", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_line)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetLine", [value]))

    @jsii.member(jsii_name="putWidgetLogTable")
    def put_widget_log_table(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetLogTable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_log_table)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetLogTable", [value]))

    @jsii.member(jsii_name="putWidgetMarkdown")
    def put_widget_markdown(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetMarkdown", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_markdown)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetMarkdown", [value]))

    @jsii.member(jsii_name="putWidgetPie")
    def put_widget_pie(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetPie", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_pie)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetPie", [value]))

    @jsii.member(jsii_name="putWidgetStackedBar")
    def put_widget_stacked_bar(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetStackedBar", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_stacked_bar)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetStackedBar", [value]))

    @jsii.member(jsii_name="putWidgetTable")
    def put_widget_table(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetTable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageOutputReference.put_widget_table)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWidgetTable", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetWidgetArea")
    def reset_widget_area(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetArea", []))

    @jsii.member(jsii_name="resetWidgetBar")
    def reset_widget_bar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetBar", []))

    @jsii.member(jsii_name="resetWidgetBillboard")
    def reset_widget_billboard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetBillboard", []))

    @jsii.member(jsii_name="resetWidgetBullet")
    def reset_widget_bullet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetBullet", []))

    @jsii.member(jsii_name="resetWidgetFunnel")
    def reset_widget_funnel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetFunnel", []))

    @jsii.member(jsii_name="resetWidgetHeatmap")
    def reset_widget_heatmap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetHeatmap", []))

    @jsii.member(jsii_name="resetWidgetHistogram")
    def reset_widget_histogram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetHistogram", []))

    @jsii.member(jsii_name="resetWidgetJson")
    def reset_widget_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetJson", []))

    @jsii.member(jsii_name="resetWidgetLine")
    def reset_widget_line(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetLine", []))

    @jsii.member(jsii_name="resetWidgetLogTable")
    def reset_widget_log_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetLogTable", []))

    @jsii.member(jsii_name="resetWidgetMarkdown")
    def reset_widget_markdown(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetMarkdown", []))

    @jsii.member(jsii_name="resetWidgetPie")
    def reset_widget_pie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetPie", []))

    @jsii.member(jsii_name="resetWidgetStackedBar")
    def reset_widget_stacked_bar(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetStackedBar", []))

    @jsii.member(jsii_name="resetWidgetTable")
    def reset_widget_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidgetTable", []))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @builtins.property
    @jsii.member(jsii_name="widgetArea")
    def widget_area(self) -> "OneDashboardPageWidgetAreaList":
        return typing.cast("OneDashboardPageWidgetAreaList", jsii.get(self, "widgetArea"))

    @builtins.property
    @jsii.member(jsii_name="widgetBar")
    def widget_bar(self) -> "OneDashboardPageWidgetBarList":
        return typing.cast("OneDashboardPageWidgetBarList", jsii.get(self, "widgetBar"))

    @builtins.property
    @jsii.member(jsii_name="widgetBillboard")
    def widget_billboard(self) -> "OneDashboardPageWidgetBillboardList":
        return typing.cast("OneDashboardPageWidgetBillboardList", jsii.get(self, "widgetBillboard"))

    @builtins.property
    @jsii.member(jsii_name="widgetBullet")
    def widget_bullet(self) -> "OneDashboardPageWidgetBulletList":
        return typing.cast("OneDashboardPageWidgetBulletList", jsii.get(self, "widgetBullet"))

    @builtins.property
    @jsii.member(jsii_name="widgetFunnel")
    def widget_funnel(self) -> "OneDashboardPageWidgetFunnelList":
        return typing.cast("OneDashboardPageWidgetFunnelList", jsii.get(self, "widgetFunnel"))

    @builtins.property
    @jsii.member(jsii_name="widgetHeatmap")
    def widget_heatmap(self) -> "OneDashboardPageWidgetHeatmapList":
        return typing.cast("OneDashboardPageWidgetHeatmapList", jsii.get(self, "widgetHeatmap"))

    @builtins.property
    @jsii.member(jsii_name="widgetHistogram")
    def widget_histogram(self) -> "OneDashboardPageWidgetHistogramList":
        return typing.cast("OneDashboardPageWidgetHistogramList", jsii.get(self, "widgetHistogram"))

    @builtins.property
    @jsii.member(jsii_name="widgetJson")
    def widget_json(self) -> "OneDashboardPageWidgetJsonList":
        return typing.cast("OneDashboardPageWidgetJsonList", jsii.get(self, "widgetJson"))

    @builtins.property
    @jsii.member(jsii_name="widgetLine")
    def widget_line(self) -> "OneDashboardPageWidgetLineList":
        return typing.cast("OneDashboardPageWidgetLineList", jsii.get(self, "widgetLine"))

    @builtins.property
    @jsii.member(jsii_name="widgetLogTable")
    def widget_log_table(self) -> "OneDashboardPageWidgetLogTableList":
        return typing.cast("OneDashboardPageWidgetLogTableList", jsii.get(self, "widgetLogTable"))

    @builtins.property
    @jsii.member(jsii_name="widgetMarkdown")
    def widget_markdown(self) -> "OneDashboardPageWidgetMarkdownList":
        return typing.cast("OneDashboardPageWidgetMarkdownList", jsii.get(self, "widgetMarkdown"))

    @builtins.property
    @jsii.member(jsii_name="widgetPie")
    def widget_pie(self) -> "OneDashboardPageWidgetPieList":
        return typing.cast("OneDashboardPageWidgetPieList", jsii.get(self, "widgetPie"))

    @builtins.property
    @jsii.member(jsii_name="widgetStackedBar")
    def widget_stacked_bar(self) -> "OneDashboardPageWidgetStackedBarList":
        return typing.cast("OneDashboardPageWidgetStackedBarList", jsii.get(self, "widgetStackedBar"))

    @builtins.property
    @jsii.member(jsii_name="widgetTable")
    def widget_table(self) -> "OneDashboardPageWidgetTableList":
        return typing.cast("OneDashboardPageWidgetTableList", jsii.get(self, "widgetTable"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetAreaInput")
    def widget_area_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetArea"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetArea"]]], jsii.get(self, "widgetAreaInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetBarInput")
    def widget_bar_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBar"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBar"]]], jsii.get(self, "widgetBarInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetBillboardInput")
    def widget_billboard_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBillboard"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBillboard"]]], jsii.get(self, "widgetBillboardInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetBulletInput")
    def widget_bullet_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBullet"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBullet"]]], jsii.get(self, "widgetBulletInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetFunnelInput")
    def widget_funnel_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetFunnel"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetFunnel"]]], jsii.get(self, "widgetFunnelInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetHeatmapInput")
    def widget_heatmap_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHeatmap"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHeatmap"]]], jsii.get(self, "widgetHeatmapInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetHistogramInput")
    def widget_histogram_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHistogram"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHistogram"]]], jsii.get(self, "widgetHistogramInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetJsonInput")
    def widget_json_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetJson"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetJson"]]], jsii.get(self, "widgetJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetLineInput")
    def widget_line_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLine"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLine"]]], jsii.get(self, "widgetLineInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetLogTableInput")
    def widget_log_table_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLogTable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLogTable"]]], jsii.get(self, "widgetLogTableInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetMarkdownInput")
    def widget_markdown_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetMarkdown"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetMarkdown"]]], jsii.get(self, "widgetMarkdownInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetPieInput")
    def widget_pie_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetPie"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetPie"]]], jsii.get(self, "widgetPieInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetStackedBarInput")
    def widget_stacked_bar_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetStackedBar"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetStackedBar"]]], jsii.get(self, "widgetStackedBarInput"))

    @builtins.property
    @jsii.member(jsii_name="widgetTableInput")
    def widget_table_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetTable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetTable"]]], jsii.get(self, "widgetTableInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetArea",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetArea:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetAreaNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetArea.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetAreaNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetAreaNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetArea(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetAreaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetAreaList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetAreaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetAreaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetArea]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetArea]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetArea]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetAreaNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetAreaNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetAreaNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetAreaNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetAreaNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetAreaNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetAreaNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetAreaNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetAreaNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetAreaNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetAreaNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetAreaNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetAreaNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetAreaNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetAreaNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetAreaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetAreaOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetAreaNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetAreaOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetAreaNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetAreaNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetAreaNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetAreaNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetArea, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetArea, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetArea, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetAreaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBar",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "filter_current_dashboard": "filterCurrentDashboard",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "linked_entity_guids": "linkedEntityGuids",
        "width": "width",
    },
)
class OneDashboardPageWidgetBar:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBarNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        filter_current_dashboard: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        linked_entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param filter_current_dashboard: Use this item to filter the current dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#filter_current_dashboard OneDashboard#filter_current_dashboard}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param linked_entity_guids: Related entities. Currently only supports Dashboard entities, but may allow other cases in the future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#linked_entity_guids OneDashboard#linked_entity_guids}
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBar.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument filter_current_dashboard", value=filter_current_dashboard, expected_type=type_hints["filter_current_dashboard"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument linked_entity_guids", value=linked_entity_guids, expected_type=type_hints["linked_entity_guids"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if filter_current_dashboard is not None:
            self._values["filter_current_dashboard"] = filter_current_dashboard
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if linked_entity_guids is not None:
            self._values["linked_entity_guids"] = linked_entity_guids
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBarNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBarNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_current_dashboard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use this item to filter the current dashboard.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#filter_current_dashboard OneDashboard#filter_current_dashboard}
        '''
        result = self._values.get("filter_current_dashboard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def linked_entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Related entities. Currently only supports Dashboard entities, but may allow other cases in the future.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#linked_entity_guids OneDashboard#linked_entity_guids}
        '''
        result = self._values.get("linked_entity_guids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetBar(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetBarList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBarList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetBarOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetBarOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBar]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBar]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBar]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBarNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetBarNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetBarNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetBarNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBarNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetBarNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetBarNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBarNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBarNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBarNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetBarNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBarNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetBarNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetBarNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetBarNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetBarOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBarOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetBarNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBarOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetFilterCurrentDashboard")
    def reset_filter_current_dashboard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterCurrentDashboard", []))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetLinkedEntityGuids")
    def reset_linked_entity_guids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedEntityGuids", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetBarNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetBarNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="filterCurrentDashboardInput")
    def filter_current_dashboard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "filterCurrentDashboardInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedEntityGuidsInput")
    def linked_entity_guids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linkedEntityGuidsInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBarNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBarNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="filterCurrentDashboard")
    def filter_current_dashboard(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "filterCurrentDashboard"))

    @filter_current_dashboard.setter
    def filter_current_dashboard(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "filter_current_dashboard").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterCurrentDashboard", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="linkedEntityGuids")
    def linked_entity_guids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "linkedEntityGuids"))

    @linked_entity_guids.setter
    def linked_entity_guids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "linked_entity_guids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedEntityGuids", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetBar, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetBar, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetBar, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBarOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBillboard",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "critical": "critical",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "warning": "warning",
        "width": "width",
    },
)
class OneDashboardPageWidgetBillboard:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBillboardNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        critical: typing.Optional[builtins.str] = None,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        warning: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param critical: The critical threshold value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#critical OneDashboard#critical}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param warning: The warning threshold value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#warning OneDashboard#warning}
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboard.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if critical is not None:
            self._values["critical"] = critical
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if warning is not None:
            self._values["warning"] = warning
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBillboardNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBillboardNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def critical(self) -> typing.Optional[builtins.str]:
        '''The critical threshold value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#critical OneDashboard#critical}
        '''
        result = self._values.get("critical")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def warning(self) -> typing.Optional[builtins.str]:
        '''The warning threshold value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#warning OneDashboard#warning}
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetBillboard(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetBillboardList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBillboardList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetBillboardOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetBillboardOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboard]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboard]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboard]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBillboardNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetBillboardNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetBillboardNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetBillboardNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBillboardNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetBillboardNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetBillboardNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboardNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboardNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboardNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetBillboardNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBillboardNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetBillboardNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetBillboardNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetBillboardNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetBillboardOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBillboardOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetBillboardNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBillboardOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetCritical")
    def reset_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCritical", []))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetBillboardNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetBillboardNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="criticalInput")
    def critical_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "criticalInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboardNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBillboardNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "critical"))

    @critical.setter
    def critical(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "critical").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "critical", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warning"))

    @warning.setter
    def warning(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "warning").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warning", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetBillboard, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetBillboard, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetBillboard, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBillboardOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBullet",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "limit": "limit",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetBullet:
    def __init__(
        self,
        *,
        column: jsii.Number,
        limit: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetBulletNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param limit: The maximum value for the visualization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#limit OneDashboard#limit}
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBullet.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "limit": limit,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def limit(self) -> jsii.Number:
        '''The maximum value for the visualization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#limit OneDashboard#limit}
        '''
        result = self._values.get("limit")
        assert result is not None, "Required property 'limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBulletNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetBulletNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetBullet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetBulletList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBulletList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetBulletOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetBulletOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBullet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBullet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBullet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBulletNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetBulletNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetBulletNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetBulletNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBulletNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetBulletNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetBulletNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBulletNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBulletNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBulletNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetBulletNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBulletNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetBulletNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetBulletNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetBulletNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetBulletOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetBulletOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetBulletNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetBulletOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetBulletNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetBulletNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="limitInput")
    def limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "limitInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBulletNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetBulletNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="limit")
    def limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "limit"))

    @limit.setter
    def limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "limit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "limit", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetBullet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetBullet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetBullet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetBulletOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetFunnel",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetFunnel:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetFunnelNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnel.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetFunnelNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetFunnelNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetFunnel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetFunnelList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetFunnelList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetFunnelOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetFunnelOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnel]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnel]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnel]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetFunnelNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetFunnelNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetFunnelNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetFunnelNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetFunnelNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetFunnelNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetFunnelNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnelNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnelNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnelNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetFunnelNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetFunnelNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetFunnelNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetFunnelNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetFunnelNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetFunnelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetFunnelOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetFunnelNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetFunnelOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetFunnelNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetFunnelNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnelNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetFunnelNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetFunnel, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetFunnel, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetFunnel, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetFunnelOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHeatmap",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetHeatmap:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetHeatmapNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmap.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHeatmapNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHeatmapNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetHeatmap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetHeatmapList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHeatmapList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetHeatmapOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetHeatmapOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmap]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmap]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmap]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHeatmapNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetHeatmapNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetHeatmapNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetHeatmapNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHeatmapNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetHeatmapNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetHeatmapNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmapNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmapNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmapNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetHeatmapNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHeatmapNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetHeatmapNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetHeatmapNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetHeatmapNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetHeatmapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHeatmapOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetHeatmapNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHeatmapOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetHeatmapNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetHeatmapNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmapNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHeatmapNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetHeatmap, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetHeatmap, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetHeatmap, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHeatmapOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHistogram",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetHistogram:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetHistogramNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogram.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHistogramNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetHistogramNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetHistogram(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetHistogramList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHistogramList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetHistogramOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetHistogramOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogram]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogram]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogram]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHistogramNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetHistogramNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetHistogramNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetHistogramNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHistogramNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetHistogramNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetHistogramNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogramNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogramNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogramNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetHistogramNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHistogramNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetHistogramNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetHistogramNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetHistogramNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetHistogramOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetHistogramOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetHistogramNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetHistogramOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetHistogramNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetHistogramNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogramNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetHistogramNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetHistogram, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetHistogram, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetHistogram, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetHistogramOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetJson",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetJson:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetJsonNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJson.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetJsonNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetJsonNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetJson(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetJsonList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetJsonList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetJsonOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetJsonOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJson]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJson]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJson]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetJsonNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetJsonNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetJsonNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetJsonNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetJsonNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetJsonNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetJsonNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJsonNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJsonNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJsonNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetJsonNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetJsonNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetJsonNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetJsonNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetJsonNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetJsonOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetJsonOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetJsonNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetJsonOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetJsonNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetJsonNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJsonNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetJsonNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetJson, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetJson, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetJson, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetJsonOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLine",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetLine:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetLineNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLine.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLineNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLineNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetLine(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetLineList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLineList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetLineOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetLineOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLine]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLine]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLine]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLineNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetLineNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetLineNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetLineNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLineNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetLineNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetLineNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLineNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLineNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLineNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetLineNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLineNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetLineNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetLineNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetLineNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetLineOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLineOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetLineNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLineOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetLineNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetLineNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLineNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLineNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetLine, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetLine, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetLine, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLineOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLogTable",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetLogTable:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetLogTableNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTable.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLogTableNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetLogTableNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetLogTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetLogTableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLogTableList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetLogTableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetLogTableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLogTableNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetLogTableNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetLogTableNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetLogTableNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLogTableNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetLogTableNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetLogTableNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTableNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTableNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTableNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetLogTableNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLogTableNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetLogTableNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetLogTableNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetLogTableNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetLogTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetLogTableOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetLogTableNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetLogTableOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetLogTableNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetLogTableNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTableNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetLogTableNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetLogTable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetLogTable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetLogTable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetLogTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetMarkdown",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "text": "text",
        "width": "width",
    },
)
class OneDashboardPageWidgetMarkdown:
    def __init__(
        self,
        *,
        column: jsii.Number,
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        text: typing.Optional[builtins.str] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param text: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#text OneDashboard#text}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetMarkdown.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if text is not None:
            self._values["text"] = text
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#text OneDashboard#text}.'''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetMarkdown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetMarkdownList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetMarkdownList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetMarkdownList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetMarkdownOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetMarkdownList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetMarkdownOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetMarkdown]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetMarkdown]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetMarkdown]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetMarkdownOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetMarkdownOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetMarkdownOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetMarkdown, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetMarkdown, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetMarkdown, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetMarkdownOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetPie",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "filter_current_dashboard": "filterCurrentDashboard",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "linked_entity_guids": "linkedEntityGuids",
        "width": "width",
    },
)
class OneDashboardPageWidgetPie:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetPieNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        filter_current_dashboard: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        linked_entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param filter_current_dashboard: Use this item to filter the current dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#filter_current_dashboard OneDashboard#filter_current_dashboard}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param linked_entity_guids: Related entities. Currently only supports Dashboard entities, but may allow other cases in the future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#linked_entity_guids OneDashboard#linked_entity_guids}
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPie.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument filter_current_dashboard", value=filter_current_dashboard, expected_type=type_hints["filter_current_dashboard"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument linked_entity_guids", value=linked_entity_guids, expected_type=type_hints["linked_entity_guids"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if filter_current_dashboard is not None:
            self._values["filter_current_dashboard"] = filter_current_dashboard
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if linked_entity_guids is not None:
            self._values["linked_entity_guids"] = linked_entity_guids
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetPieNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetPieNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_current_dashboard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use this item to filter the current dashboard.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#filter_current_dashboard OneDashboard#filter_current_dashboard}
        '''
        result = self._values.get("filter_current_dashboard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def linked_entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Related entities. Currently only supports Dashboard entities, but may allow other cases in the future.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#linked_entity_guids OneDashboard#linked_entity_guids}
        '''
        result = self._values.get("linked_entity_guids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetPie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetPieList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetPieList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetPieOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetPieOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPie]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPie]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPie]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetPieNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetPieNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetPieNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetPieNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetPieNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetPieNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetPieNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPieNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPieNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPieNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetPieNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetPieNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetPieNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetPieNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetPieNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetPieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetPieOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetPieNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetPieOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetFilterCurrentDashboard")
    def reset_filter_current_dashboard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterCurrentDashboard", []))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetLinkedEntityGuids")
    def reset_linked_entity_guids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedEntityGuids", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetPieNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetPieNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="filterCurrentDashboardInput")
    def filter_current_dashboard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "filterCurrentDashboardInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedEntityGuidsInput")
    def linked_entity_guids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linkedEntityGuidsInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPieNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetPieNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="filterCurrentDashboard")
    def filter_current_dashboard(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "filterCurrentDashboard"))

    @filter_current_dashboard.setter
    def filter_current_dashboard(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "filter_current_dashboard").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterCurrentDashboard", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="linkedEntityGuids")
    def linked_entity_guids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "linkedEntityGuids"))

    @linked_entity_guids.setter
    def linked_entity_guids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "linked_entity_guids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedEntityGuids", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetPie, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetPie, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetPie, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetPieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetStackedBar",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "width": "width",
    },
)
class OneDashboardPageWidgetStackedBar:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetStackedBarNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBar.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetStackedBarNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetStackedBarNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetStackedBar(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetStackedBarList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetStackedBarList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetStackedBarOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetStackedBarOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBar]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBar]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBar]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetStackedBarNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetStackedBarNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetStackedBarNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetStackedBarNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetStackedBarNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetStackedBarNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetStackedBarNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBarNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBarNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBarNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetStackedBarNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetStackedBarNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetStackedBarNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetStackedBarNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetStackedBarNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetStackedBarOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetStackedBarOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetStackedBarNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetStackedBarOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetStackedBarNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetStackedBarNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBarNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetStackedBarNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetStackedBar, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetStackedBar, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetStackedBar, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetStackedBarOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetTable",
    jsii_struct_bases=[],
    name_mapping={
        "column": "column",
        "nrql_query": "nrqlQuery",
        "row": "row",
        "title": "title",
        "filter_current_dashboard": "filterCurrentDashboard",
        "height": "height",
        "ignore_time_range": "ignoreTimeRange",
        "linked_entity_guids": "linkedEntityGuids",
        "width": "width",
    },
)
class OneDashboardPageWidgetTable:
    def __init__(
        self,
        *,
        column: jsii.Number,
        nrql_query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["OneDashboardPageWidgetTableNrqlQuery", typing.Dict[str, typing.Any]]]],
        row: jsii.Number,
        title: builtins.str,
        filter_current_dashboard: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        height: typing.Optional[jsii.Number] = None,
        ignore_time_range: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        linked_entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        width: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.
        :param nrql_query: nrql_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        :param row: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.
        :param title: A title for the widget. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        :param filter_current_dashboard: Use this item to filter the current dashboard. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#filter_current_dashboard OneDashboard#filter_current_dashboard}
        :param height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.
        :param ignore_time_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.
        :param linked_entity_guids: Related entities. Currently only supports Dashboard entities, but may allow other cases in the future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#linked_entity_guids OneDashboard#linked_entity_guids}
        :param width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTable.__init__)
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument nrql_query", value=nrql_query, expected_type=type_hints["nrql_query"])
            check_type(argname="argument row", value=row, expected_type=type_hints["row"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument filter_current_dashboard", value=filter_current_dashboard, expected_type=type_hints["filter_current_dashboard"])
            check_type(argname="argument height", value=height, expected_type=type_hints["height"])
            check_type(argname="argument ignore_time_range", value=ignore_time_range, expected_type=type_hints["ignore_time_range"])
            check_type(argname="argument linked_entity_guids", value=linked_entity_guids, expected_type=type_hints["linked_entity_guids"])
            check_type(argname="argument width", value=width, expected_type=type_hints["width"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "nrql_query": nrql_query,
            "row": row,
            "title": title,
        }
        if filter_current_dashboard is not None:
            self._values["filter_current_dashboard"] = filter_current_dashboard
        if height is not None:
            self._values["height"] = height
        if ignore_time_range is not None:
            self._values["ignore_time_range"] = ignore_time_range
        if linked_entity_guids is not None:
            self._values["linked_entity_guids"] = linked_entity_guids
        if width is not None:
            self._values["width"] = width

    @builtins.property
    def column(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#column OneDashboard#column}.'''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def nrql_query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetTableNrqlQuery"]]:
        '''nrql_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#nrql_query OneDashboard#nrql_query}
        '''
        result = self._values.get("nrql_query")
        assert result is not None, "Required property 'nrql_query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["OneDashboardPageWidgetTableNrqlQuery"]], result)

    @builtins.property
    def row(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#row OneDashboard#row}.'''
        result = self._values.get("row")
        assert result is not None, "Required property 'row' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title for the widget.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#title OneDashboard#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_current_dashboard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use this item to filter the current dashboard.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#filter_current_dashboard OneDashboard#filter_current_dashboard}
        '''
        result = self._values.get("filter_current_dashboard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def height(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#height OneDashboard#height}.'''
        result = self._values.get("height")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ignore_time_range(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#ignore_time_range OneDashboard#ignore_time_range}.'''
        result = self._values.get("ignore_time_range")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def linked_entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Related entities. Currently only supports Dashboard entities, but may allow other cases in the future.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#linked_entity_guids OneDashboard#linked_entity_guids}
        '''
        result = self._values.get("linked_entity_guids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def width(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#width OneDashboard#width}.'''
        result = self._values.get("width")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetTableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetTableList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "OneDashboardPageWidgetTableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetTableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetTableNrqlQuery",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "account_id": "accountId"},
)
class OneDashboardPageWidgetTableNrqlQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: The NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        :param account_id: The account id used for the NRQL query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableNrqlQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if account_id is not None:
            self._values["account_id"] = account_id

    @builtins.property
    def query(self) -> builtins.str:
        '''The NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#query OneDashboard#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The account id used for the NRQL query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/one_dashboard#account_id OneDashboard#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OneDashboardPageWidgetTableNrqlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OneDashboardPageWidgetTableNrqlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetTableNrqlQueryList",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableNrqlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OneDashboardPageWidgetTableNrqlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableNrqlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OneDashboardPageWidgetTableNrqlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTableNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTableNrqlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTableNrqlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetTableNrqlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetTableNrqlQueryOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableNrqlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryOutputReference, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetTableNrqlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetTableNrqlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetTableNrqlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableNrqlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OneDashboardPageWidgetTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.oneDashboard.OneDashboardPageWidgetTableOutputReference",
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
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNrqlQuery")
    def put_nrql_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[OneDashboardPageWidgetTableNrqlQuery, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OneDashboardPageWidgetTableOutputReference.put_nrql_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNrqlQuery", [value]))

    @jsii.member(jsii_name="resetFilterCurrentDashboard")
    def reset_filter_current_dashboard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterCurrentDashboard", []))

    @jsii.member(jsii_name="resetHeight")
    def reset_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeight", []))

    @jsii.member(jsii_name="resetIgnoreTimeRange")
    def reset_ignore_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreTimeRange", []))

    @jsii.member(jsii_name="resetLinkedEntityGuids")
    def reset_linked_entity_guids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkedEntityGuids", []))

    @jsii.member(jsii_name="resetWidth")
    def reset_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWidth", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQuery")
    def nrql_query(self) -> OneDashboardPageWidgetTableNrqlQueryList:
        return typing.cast(OneDashboardPageWidgetTableNrqlQueryList, jsii.get(self, "nrqlQuery"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="filterCurrentDashboardInput")
    def filter_current_dashboard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "filterCurrentDashboardInput"))

    @builtins.property
    @jsii.member(jsii_name="heightInput")
    def height_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "heightInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRangeInput")
    def ignore_time_range_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedEntityGuidsInput")
    def linked_entity_guids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linkedEntityGuidsInput"))

    @builtins.property
    @jsii.member(jsii_name="nrqlQueryInput")
    def nrql_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTableNrqlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[OneDashboardPageWidgetTableNrqlQuery]]], jsii.get(self, "nrqlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="rowInput")
    def row_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rowInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="widthInput")
    def width_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "widthInput"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "column"))

    @column.setter
    def column(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "column", value)

    @builtins.property
    @jsii.member(jsii_name="filterCurrentDashboard")
    def filter_current_dashboard(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "filterCurrentDashboard"))

    @filter_current_dashboard.setter
    def filter_current_dashboard(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "filter_current_dashboard").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterCurrentDashboard", value)

    @builtins.property
    @jsii.member(jsii_name="height")
    def height(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "height"))

    @height.setter
    def height(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "height").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "height", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreTimeRange")
    def ignore_time_range(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreTimeRange"))

    @ignore_time_range.setter
    def ignore_time_range(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "ignore_time_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreTimeRange", value)

    @builtins.property
    @jsii.member(jsii_name="linkedEntityGuids")
    def linked_entity_guids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "linkedEntityGuids"))

    @linked_entity_guids.setter
    def linked_entity_guids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "linked_entity_guids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedEntityGuids", value)

    @builtins.property
    @jsii.member(jsii_name="row")
    def row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "row"))

    @row.setter
    def row(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "row").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "row", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="width")
    def width(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "width"))

    @width.setter
    def width(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "width").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "width", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OneDashboardPageWidgetTable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OneDashboardPageWidgetTable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OneDashboardPageWidgetTable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OneDashboardPageWidgetTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OneDashboard",
    "OneDashboardConfig",
    "OneDashboardPage",
    "OneDashboardPageList",
    "OneDashboardPageOutputReference",
    "OneDashboardPageWidgetArea",
    "OneDashboardPageWidgetAreaList",
    "OneDashboardPageWidgetAreaNrqlQuery",
    "OneDashboardPageWidgetAreaNrqlQueryList",
    "OneDashboardPageWidgetAreaNrqlQueryOutputReference",
    "OneDashboardPageWidgetAreaOutputReference",
    "OneDashboardPageWidgetBar",
    "OneDashboardPageWidgetBarList",
    "OneDashboardPageWidgetBarNrqlQuery",
    "OneDashboardPageWidgetBarNrqlQueryList",
    "OneDashboardPageWidgetBarNrqlQueryOutputReference",
    "OneDashboardPageWidgetBarOutputReference",
    "OneDashboardPageWidgetBillboard",
    "OneDashboardPageWidgetBillboardList",
    "OneDashboardPageWidgetBillboardNrqlQuery",
    "OneDashboardPageWidgetBillboardNrqlQueryList",
    "OneDashboardPageWidgetBillboardNrqlQueryOutputReference",
    "OneDashboardPageWidgetBillboardOutputReference",
    "OneDashboardPageWidgetBullet",
    "OneDashboardPageWidgetBulletList",
    "OneDashboardPageWidgetBulletNrqlQuery",
    "OneDashboardPageWidgetBulletNrqlQueryList",
    "OneDashboardPageWidgetBulletNrqlQueryOutputReference",
    "OneDashboardPageWidgetBulletOutputReference",
    "OneDashboardPageWidgetFunnel",
    "OneDashboardPageWidgetFunnelList",
    "OneDashboardPageWidgetFunnelNrqlQuery",
    "OneDashboardPageWidgetFunnelNrqlQueryList",
    "OneDashboardPageWidgetFunnelNrqlQueryOutputReference",
    "OneDashboardPageWidgetFunnelOutputReference",
    "OneDashboardPageWidgetHeatmap",
    "OneDashboardPageWidgetHeatmapList",
    "OneDashboardPageWidgetHeatmapNrqlQuery",
    "OneDashboardPageWidgetHeatmapNrqlQueryList",
    "OneDashboardPageWidgetHeatmapNrqlQueryOutputReference",
    "OneDashboardPageWidgetHeatmapOutputReference",
    "OneDashboardPageWidgetHistogram",
    "OneDashboardPageWidgetHistogramList",
    "OneDashboardPageWidgetHistogramNrqlQuery",
    "OneDashboardPageWidgetHistogramNrqlQueryList",
    "OneDashboardPageWidgetHistogramNrqlQueryOutputReference",
    "OneDashboardPageWidgetHistogramOutputReference",
    "OneDashboardPageWidgetJson",
    "OneDashboardPageWidgetJsonList",
    "OneDashboardPageWidgetJsonNrqlQuery",
    "OneDashboardPageWidgetJsonNrqlQueryList",
    "OneDashboardPageWidgetJsonNrqlQueryOutputReference",
    "OneDashboardPageWidgetJsonOutputReference",
    "OneDashboardPageWidgetLine",
    "OneDashboardPageWidgetLineList",
    "OneDashboardPageWidgetLineNrqlQuery",
    "OneDashboardPageWidgetLineNrqlQueryList",
    "OneDashboardPageWidgetLineNrqlQueryOutputReference",
    "OneDashboardPageWidgetLineOutputReference",
    "OneDashboardPageWidgetLogTable",
    "OneDashboardPageWidgetLogTableList",
    "OneDashboardPageWidgetLogTableNrqlQuery",
    "OneDashboardPageWidgetLogTableNrqlQueryList",
    "OneDashboardPageWidgetLogTableNrqlQueryOutputReference",
    "OneDashboardPageWidgetLogTableOutputReference",
    "OneDashboardPageWidgetMarkdown",
    "OneDashboardPageWidgetMarkdownList",
    "OneDashboardPageWidgetMarkdownOutputReference",
    "OneDashboardPageWidgetPie",
    "OneDashboardPageWidgetPieList",
    "OneDashboardPageWidgetPieNrqlQuery",
    "OneDashboardPageWidgetPieNrqlQueryList",
    "OneDashboardPageWidgetPieNrqlQueryOutputReference",
    "OneDashboardPageWidgetPieOutputReference",
    "OneDashboardPageWidgetStackedBar",
    "OneDashboardPageWidgetStackedBarList",
    "OneDashboardPageWidgetStackedBarNrqlQuery",
    "OneDashboardPageWidgetStackedBarNrqlQueryList",
    "OneDashboardPageWidgetStackedBarNrqlQueryOutputReference",
    "OneDashboardPageWidgetStackedBarOutputReference",
    "OneDashboardPageWidgetTable",
    "OneDashboardPageWidgetTableList",
    "OneDashboardPageWidgetTableNrqlQuery",
    "OneDashboardPageWidgetTableNrqlQueryList",
    "OneDashboardPageWidgetTableNrqlQueryOutputReference",
    "OneDashboardPageWidgetTableOutputReference",
]

publication.publish()
