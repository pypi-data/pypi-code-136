'''
# `azurerm_automation_runbook`

Refer to the Terraform Registory for docs: [`azurerm_automation_runbook`](https://www.terraform.io/docs/providers/azurerm/r/automation_runbook).
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


class AutomationRunbook(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook azurerm_automation_runbook}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        automation_account_name: builtins.str,
        location: builtins.str,
        log_progress: typing.Union[builtins.bool, cdktf.IResolvable],
        log_verbose: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        resource_group_name: builtins.str,
        runbook_type: builtins.str,
        content: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        job_schedule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutomationRunbookJobSchedule", typing.Dict[str, typing.Any]]]]] = None,
        publish_content_link: typing.Optional[typing.Union["AutomationRunbookPublishContentLink", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AutomationRunbookTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook azurerm_automation_runbook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param automation_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#automation_account_name AutomationRunbook#automation_account_name}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#location AutomationRunbook#location}.
        :param log_progress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#log_progress AutomationRunbook#log_progress}.
        :param log_verbose: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#log_verbose AutomationRunbook#log_verbose}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#name AutomationRunbook#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#resource_group_name AutomationRunbook#resource_group_name}.
        :param runbook_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#runbook_type AutomationRunbook#runbook_type}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#content AutomationRunbook#content}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#description AutomationRunbook#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#id AutomationRunbook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#job_schedule AutomationRunbook#job_schedule}.
        :param publish_content_link: publish_content_link block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#publish_content_link AutomationRunbook#publish_content_link}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#tags AutomationRunbook#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#timeouts AutomationRunbook#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbook.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AutomationRunbookConfig(
            automation_account_name=automation_account_name,
            location=location,
            log_progress=log_progress,
            log_verbose=log_verbose,
            name=name,
            resource_group_name=resource_group_name,
            runbook_type=runbook_type,
            content=content,
            description=description,
            id=id,
            job_schedule=job_schedule,
            publish_content_link=publish_content_link,
            tags=tags,
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

    @jsii.member(jsii_name="putJobSchedule")
    def put_job_schedule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutomationRunbookJobSchedule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbook.put_job_schedule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putJobSchedule", [value]))

    @jsii.member(jsii_name="putPublishContentLink")
    def put_publish_content_link(
        self,
        *,
        uri: builtins.str,
        hash: typing.Optional[typing.Union["AutomationRunbookPublishContentLinkHash", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#uri AutomationRunbook#uri}.
        :param hash: hash block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#hash AutomationRunbook#hash}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#version AutomationRunbook#version}.
        '''
        value = AutomationRunbookPublishContentLink(
            uri=uri, hash=hash, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putPublishContentLink", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#create AutomationRunbook#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#delete AutomationRunbook#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#read AutomationRunbook#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#update AutomationRunbook#update}.
        '''
        value = AutomationRunbookTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJobSchedule")
    def reset_job_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobSchedule", []))

    @jsii.member(jsii_name="resetPublishContentLink")
    def reset_publish_content_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishContentLink", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="jobSchedule")
    def job_schedule(self) -> "AutomationRunbookJobScheduleList":
        return typing.cast("AutomationRunbookJobScheduleList", jsii.get(self, "jobSchedule"))

    @builtins.property
    @jsii.member(jsii_name="publishContentLink")
    def publish_content_link(
        self,
    ) -> "AutomationRunbookPublishContentLinkOutputReference":
        return typing.cast("AutomationRunbookPublishContentLinkOutputReference", jsii.get(self, "publishContentLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "AutomationRunbookTimeoutsOutputReference":
        return typing.cast("AutomationRunbookTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="automationAccountNameInput")
    def automation_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "automationAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobScheduleInput")
    def job_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutomationRunbookJobSchedule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutomationRunbookJobSchedule"]]], jsii.get(self, "jobScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="logProgressInput")
    def log_progress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logProgressInput"))

    @builtins.property
    @jsii.member(jsii_name="logVerboseInput")
    def log_verbose_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logVerboseInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publishContentLinkInput")
    def publish_content_link_input(
        self,
    ) -> typing.Optional["AutomationRunbookPublishContentLink"]:
        return typing.cast(typing.Optional["AutomationRunbookPublishContentLink"], jsii.get(self, "publishContentLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="runbookTypeInput")
    def runbook_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runbookTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["AutomationRunbookTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AutomationRunbookTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="automationAccountName")
    def automation_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "automationAccountName"))

    @automation_account_name.setter
    def automation_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "automation_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automationAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="logProgress")
    def log_progress(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logProgress"))

    @log_progress.setter
    def log_progress(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "log_progress").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logProgress", value)

    @builtins.property
    @jsii.member(jsii_name="logVerbose")
    def log_verbose(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logVerbose"))

    @log_verbose.setter
    def log_verbose(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "log_verbose").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logVerbose", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="runbookType")
    def runbook_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runbookType"))

    @runbook_type.setter
    def runbook_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "runbook_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runbookType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbook, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "automation_account_name": "automationAccountName",
        "location": "location",
        "log_progress": "logProgress",
        "log_verbose": "logVerbose",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "runbook_type": "runbookType",
        "content": "content",
        "description": "description",
        "id": "id",
        "job_schedule": "jobSchedule",
        "publish_content_link": "publishContentLink",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class AutomationRunbookConfig(cdktf.TerraformMetaArguments):
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
        automation_account_name: builtins.str,
        location: builtins.str,
        log_progress: typing.Union[builtins.bool, cdktf.IResolvable],
        log_verbose: typing.Union[builtins.bool, cdktf.IResolvable],
        name: builtins.str,
        resource_group_name: builtins.str,
        runbook_type: builtins.str,
        content: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        job_schedule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AutomationRunbookJobSchedule", typing.Dict[str, typing.Any]]]]] = None,
        publish_content_link: typing.Optional[typing.Union["AutomationRunbookPublishContentLink", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["AutomationRunbookTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param automation_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#automation_account_name AutomationRunbook#automation_account_name}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#location AutomationRunbook#location}.
        :param log_progress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#log_progress AutomationRunbook#log_progress}.
        :param log_verbose: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#log_verbose AutomationRunbook#log_verbose}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#name AutomationRunbook#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#resource_group_name AutomationRunbook#resource_group_name}.
        :param runbook_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#runbook_type AutomationRunbook#runbook_type}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#content AutomationRunbook#content}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#description AutomationRunbook#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#id AutomationRunbook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_schedule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#job_schedule AutomationRunbook#job_schedule}.
        :param publish_content_link: publish_content_link block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#publish_content_link AutomationRunbook#publish_content_link}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#tags AutomationRunbook#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#timeouts AutomationRunbook#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(publish_content_link, dict):
            publish_content_link = AutomationRunbookPublishContentLink(**publish_content_link)
        if isinstance(timeouts, dict):
            timeouts = AutomationRunbookTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbookConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument automation_account_name", value=automation_account_name, expected_type=type_hints["automation_account_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument log_progress", value=log_progress, expected_type=type_hints["log_progress"])
            check_type(argname="argument log_verbose", value=log_verbose, expected_type=type_hints["log_verbose"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument runbook_type", value=runbook_type, expected_type=type_hints["runbook_type"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument job_schedule", value=job_schedule, expected_type=type_hints["job_schedule"])
            check_type(argname="argument publish_content_link", value=publish_content_link, expected_type=type_hints["publish_content_link"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "automation_account_name": automation_account_name,
            "location": location,
            "log_progress": log_progress,
            "log_verbose": log_verbose,
            "name": name,
            "resource_group_name": resource_group_name,
            "runbook_type": runbook_type,
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
        if content is not None:
            self._values["content"] = content
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if job_schedule is not None:
            self._values["job_schedule"] = job_schedule
        if publish_content_link is not None:
            self._values["publish_content_link"] = publish_content_link
        if tags is not None:
            self._values["tags"] = tags
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
    def automation_account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#automation_account_name AutomationRunbook#automation_account_name}.'''
        result = self._values.get("automation_account_name")
        assert result is not None, "Required property 'automation_account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#location AutomationRunbook#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_progress(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#log_progress AutomationRunbook#log_progress}.'''
        result = self._values.get("log_progress")
        assert result is not None, "Required property 'log_progress' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def log_verbose(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#log_verbose AutomationRunbook#log_verbose}.'''
        result = self._values.get("log_verbose")
        assert result is not None, "Required property 'log_verbose' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#name AutomationRunbook#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#resource_group_name AutomationRunbook#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runbook_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#runbook_type AutomationRunbook#runbook_type}.'''
        result = self._values.get("runbook_type")
        assert result is not None, "Required property 'runbook_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#content AutomationRunbook#content}.'''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#description AutomationRunbook#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#id AutomationRunbook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_schedule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutomationRunbookJobSchedule"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#job_schedule AutomationRunbook#job_schedule}.'''
        result = self._values.get("job_schedule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AutomationRunbookJobSchedule"]]], result)

    @builtins.property
    def publish_content_link(
        self,
    ) -> typing.Optional["AutomationRunbookPublishContentLink"]:
        '''publish_content_link block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#publish_content_link AutomationRunbook#publish_content_link}
        '''
        result = self._values.get("publish_content_link")
        return typing.cast(typing.Optional["AutomationRunbookPublishContentLink"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#tags AutomationRunbook#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["AutomationRunbookTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#timeouts AutomationRunbook#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AutomationRunbookTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRunbookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookJobSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "job_schedule_id": "jobScheduleId",
        "parameters": "parameters",
        "run_on": "runOn",
        "schedule_name": "scheduleName",
    },
)
class AutomationRunbookJobSchedule:
    def __init__(
        self,
        *,
        job_schedule_id: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        run_on: typing.Optional[builtins.str] = None,
        schedule_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param job_schedule_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#job_schedule_id AutomationRunbook#job_schedule_id}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#parameters AutomationRunbook#parameters}.
        :param run_on: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#run_on AutomationRunbook#run_on}.
        :param schedule_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#schedule_name AutomationRunbook#schedule_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbookJobSchedule.__init__)
            check_type(argname="argument job_schedule_id", value=job_schedule_id, expected_type=type_hints["job_schedule_id"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument run_on", value=run_on, expected_type=type_hints["run_on"])
            check_type(argname="argument schedule_name", value=schedule_name, expected_type=type_hints["schedule_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if job_schedule_id is not None:
            self._values["job_schedule_id"] = job_schedule_id
        if parameters is not None:
            self._values["parameters"] = parameters
        if run_on is not None:
            self._values["run_on"] = run_on
        if schedule_name is not None:
            self._values["schedule_name"] = schedule_name

    @builtins.property
    def job_schedule_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#job_schedule_id AutomationRunbook#job_schedule_id}.'''
        result = self._values.get("job_schedule_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#parameters AutomationRunbook#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def run_on(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#run_on AutomationRunbook#run_on}.'''
        result = self._values.get("run_on")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#schedule_name AutomationRunbook#schedule_name}.'''
        result = self._values.get("schedule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRunbookJobSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutomationRunbookJobScheduleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookJobScheduleList",
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
            type_hints = typing.get_type_hints(AutomationRunbookJobScheduleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AutomationRunbookJobScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbookJobScheduleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AutomationRunbookJobScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutomationRunbookJobSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutomationRunbookJobSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AutomationRunbookJobSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutomationRunbookJobScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookJobScheduleOutputReference",
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
            type_hints = typing.get_type_hints(AutomationRunbookJobScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetJobScheduleId")
    def reset_job_schedule_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobScheduleId", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetRunOn")
    def reset_run_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunOn", []))

    @jsii.member(jsii_name="resetScheduleName")
    def reset_schedule_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleName", []))

    @builtins.property
    @jsii.member(jsii_name="jobScheduleIdInput")
    def job_schedule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobScheduleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="runOnInput")
    def run_on_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runOnInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleNameInput")
    def schedule_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="jobScheduleId")
    def job_schedule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobScheduleId"))

    @job_schedule_id.setter
    def job_schedule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleOutputReference, "job_schedule_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobScheduleId", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleOutputReference, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="runOn")
    def run_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runOn"))

    @run_on.setter
    def run_on(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleOutputReference, "run_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runOn", value)

    @builtins.property
    @jsii.member(jsii_name="scheduleName")
    def schedule_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheduleName"))

    @schedule_name.setter
    def schedule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleOutputReference, "schedule_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutomationRunbookJobSchedule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutomationRunbookJobSchedule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutomationRunbookJobSchedule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookJobScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookPublishContentLink",
    jsii_struct_bases=[],
    name_mapping={"uri": "uri", "hash": "hash", "version": "version"},
)
class AutomationRunbookPublishContentLink:
    def __init__(
        self,
        *,
        uri: builtins.str,
        hash: typing.Optional[typing.Union["AutomationRunbookPublishContentLinkHash", typing.Dict[str, typing.Any]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#uri AutomationRunbook#uri}.
        :param hash: hash block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#hash AutomationRunbook#hash}
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#version AutomationRunbook#version}.
        '''
        if isinstance(hash, dict):
            hash = AutomationRunbookPublishContentLinkHash(**hash)
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbookPublishContentLink.__init__)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument hash", value=hash, expected_type=type_hints["hash"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "uri": uri,
        }
        if hash is not None:
            self._values["hash"] = hash
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#uri AutomationRunbook#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash(self) -> typing.Optional["AutomationRunbookPublishContentLinkHash"]:
        '''hash block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#hash AutomationRunbook#hash}
        '''
        result = self._values.get("hash")
        return typing.cast(typing.Optional["AutomationRunbookPublishContentLinkHash"], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#version AutomationRunbook#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRunbookPublishContentLink(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookPublishContentLinkHash",
    jsii_struct_bases=[],
    name_mapping={"algorithm": "algorithm", "value": "value"},
)
class AutomationRunbookPublishContentLinkHash:
    def __init__(self, *, algorithm: builtins.str, value: builtins.str) -> None:
        '''
        :param algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#algorithm AutomationRunbook#algorithm}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#value AutomationRunbook#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbookPublishContentLinkHash.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "algorithm": algorithm,
            "value": value,
        }

    @builtins.property
    def algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#algorithm AutomationRunbook#algorithm}.'''
        result = self._values.get("algorithm")
        assert result is not None, "Required property 'algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#value AutomationRunbook#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRunbookPublishContentLinkHash(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutomationRunbookPublishContentLinkHashOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookPublishContentLinkHashOutputReference",
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
            type_hints = typing.get_type_hints(AutomationRunbookPublishContentLinkHashOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookPublishContentLinkHashOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookPublishContentLinkHashOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AutomationRunbookPublishContentLinkHash]:
        return typing.cast(typing.Optional[AutomationRunbookPublishContentLinkHash], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutomationRunbookPublishContentLinkHash],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookPublishContentLinkHashOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AutomationRunbookPublishContentLinkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookPublishContentLinkOutputReference",
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
            type_hints = typing.get_type_hints(AutomationRunbookPublishContentLinkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHash")
    def put_hash(self, *, algorithm: builtins.str, value: builtins.str) -> None:
        '''
        :param algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#algorithm AutomationRunbook#algorithm}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#value AutomationRunbook#value}.
        '''
        value_ = AutomationRunbookPublishContentLinkHash(
            algorithm=algorithm, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putHash", [value_]))

    @jsii.member(jsii_name="resetHash")
    def reset_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHash", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="hash")
    def hash(self) -> AutomationRunbookPublishContentLinkHashOutputReference:
        return typing.cast(AutomationRunbookPublishContentLinkHashOutputReference, jsii.get(self, "hash"))

    @builtins.property
    @jsii.member(jsii_name="hashInput")
    def hash_input(self) -> typing.Optional[AutomationRunbookPublishContentLinkHash]:
        return typing.cast(typing.Optional[AutomationRunbookPublishContentLinkHash], jsii.get(self, "hashInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookPublishContentLinkOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookPublishContentLinkOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AutomationRunbookPublishContentLink]:
        return typing.cast(typing.Optional[AutomationRunbookPublishContentLink], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AutomationRunbookPublishContentLink],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookPublishContentLinkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class AutomationRunbookTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#create AutomationRunbook#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#delete AutomationRunbook#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#read AutomationRunbook#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#update AutomationRunbook#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AutomationRunbookTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#create AutomationRunbook#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#delete AutomationRunbook#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#read AutomationRunbook#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/automation_runbook#update AutomationRunbook#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRunbookTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutomationRunbookTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.automationRunbook.AutomationRunbookTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(AutomationRunbookTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AutomationRunbookTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AutomationRunbookTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AutomationRunbookTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AutomationRunbookTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AutomationRunbookTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AutomationRunbook",
    "AutomationRunbookConfig",
    "AutomationRunbookJobSchedule",
    "AutomationRunbookJobScheduleList",
    "AutomationRunbookJobScheduleOutputReference",
    "AutomationRunbookPublishContentLink",
    "AutomationRunbookPublishContentLinkHash",
    "AutomationRunbookPublishContentLinkHashOutputReference",
    "AutomationRunbookPublishContentLinkOutputReference",
    "AutomationRunbookTimeouts",
    "AutomationRunbookTimeoutsOutputReference",
]

publication.publish()
