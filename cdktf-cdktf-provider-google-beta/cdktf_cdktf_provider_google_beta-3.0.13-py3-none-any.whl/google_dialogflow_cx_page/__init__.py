'''
# `google_dialogflow_cx_page`

Refer to the Terraform Registory for docs: [`google_dialogflow_cx_page`](https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page).
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


class GoogleDialogflowCxPage(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPage",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page google_dialogflow_cx_page}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        entry_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxPageEntryFulfillment", typing.Dict[str, typing.Any]]] = None,
        event_handlers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEventHandlers", typing.Dict[str, typing.Any]]]]] = None,
        form: typing.Optional[typing.Union["GoogleDialogflowCxPageForm", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxPageTimeouts", typing.Dict[str, typing.Any]]] = None,
        transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        transition_routes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageTransitionRoutes", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page google_dialogflow_cx_page} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: The human-readable name of the page, unique within the agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#display_name GoogleDialogflowCxPage#display_name}
        :param entry_fulfillment: entry_fulfillment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#entry_fulfillment GoogleDialogflowCxPage#entry_fulfillment}
        :param event_handlers: event_handlers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#event_handlers GoogleDialogflowCxPage#event_handlers}
        :param form: form block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#form GoogleDialogflowCxPage#form}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#id GoogleDialogflowCxPage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: The language of the following fields in page:. Page.entry_fulfillment.messages Page.entry_fulfillment.conditional_cases Page.event_handlers.trigger_fulfillment.messages Page.event_handlers.trigger_fulfillment.conditional_cases Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases Page.form.parameters.fill_behavior.reprompt_event_handlers.messages Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases Page.transition_routes.trigger_fulfillment.messages Page.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#language_code GoogleDialogflowCxPage#language_code}
        :param parent: The flow to create a page for. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#parent GoogleDialogflowCxPage#parent}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#timeouts GoogleDialogflowCxPage#timeouts}
        :param transition_route_groups: Ordered list of TransitionRouteGroups associated with the page. Transition route groups must be unique within a page. If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:projects//locations//agents//flows//transitionRouteGroups/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#transition_route_groups GoogleDialogflowCxPage#transition_route_groups}
        :param transition_routes: transition_routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#transition_routes GoogleDialogflowCxPage#transition_routes}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPage.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDialogflowCxPageConfig(
            display_name=display_name,
            entry_fulfillment=entry_fulfillment,
            event_handlers=event_handlers,
            form=form,
            id=id,
            language_code=language_code,
            parent=parent,
            timeouts=timeouts,
            transition_route_groups=transition_route_groups,
            transition_routes=transition_routes,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEntryFulfillment")
    def put_entry_fulfillment(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEntryFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        value = GoogleDialogflowCxPageEntryFulfillment(
            messages=messages,
            return_partial_responses=return_partial_responses,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putEntryFulfillment", [value]))

    @jsii.member(jsii_name="putEventHandlers")
    def put_event_handlers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEventHandlers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPage.put_event_handlers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventHandlers", [value]))

    @jsii.member(jsii_name="putForm")
    def put_form(
        self,
        *,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageFormParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#parameters GoogleDialogflowCxPage#parameters}
        '''
        value = GoogleDialogflowCxPageForm(parameters=parameters)

        return typing.cast(None, jsii.invoke(self, "putForm", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#create GoogleDialogflowCxPage#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#delete GoogleDialogflowCxPage#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#update GoogleDialogflowCxPage#update}.
        '''
        value = GoogleDialogflowCxPageTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTransitionRoutes")
    def put_transition_routes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageTransitionRoutes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPage.put_transition_routes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTransitionRoutes", [value]))

    @jsii.member(jsii_name="resetEntryFulfillment")
    def reset_entry_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntryFulfillment", []))

    @jsii.member(jsii_name="resetEventHandlers")
    def reset_event_handlers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventHandlers", []))

    @jsii.member(jsii_name="resetForm")
    def reset_form(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForm", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLanguageCode")
    def reset_language_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguageCode", []))

    @jsii.member(jsii_name="resetParent")
    def reset_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParent", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTransitionRouteGroups")
    def reset_transition_route_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitionRouteGroups", []))

    @jsii.member(jsii_name="resetTransitionRoutes")
    def reset_transition_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransitionRoutes", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="entryFulfillment")
    def entry_fulfillment(
        self,
    ) -> "GoogleDialogflowCxPageEntryFulfillmentOutputReference":
        return typing.cast("GoogleDialogflowCxPageEntryFulfillmentOutputReference", jsii.get(self, "entryFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="eventHandlers")
    def event_handlers(self) -> "GoogleDialogflowCxPageEventHandlersList":
        return typing.cast("GoogleDialogflowCxPageEventHandlersList", jsii.get(self, "eventHandlers"))

    @builtins.property
    @jsii.member(jsii_name="form")
    def form(self) -> "GoogleDialogflowCxPageFormOutputReference":
        return typing.cast("GoogleDialogflowCxPageFormOutputReference", jsii.get(self, "form"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDialogflowCxPageTimeoutsOutputReference":
        return typing.cast("GoogleDialogflowCxPageTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="transitionRoutes")
    def transition_routes(self) -> "GoogleDialogflowCxPageTransitionRoutesList":
        return typing.cast("GoogleDialogflowCxPageTransitionRoutesList", jsii.get(self, "transitionRoutes"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="entryFulfillmentInput")
    def entry_fulfillment_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEntryFulfillment"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEntryFulfillment"], jsii.get(self, "entryFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="eventHandlersInput")
    def event_handlers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEventHandlers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEventHandlers"]]], jsii.get(self, "eventHandlersInput"))

    @builtins.property
    @jsii.member(jsii_name="formInput")
    def form_input(self) -> typing.Optional["GoogleDialogflowCxPageForm"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageForm"], jsii.get(self, "formInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="languageCodeInput")
    def language_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDialogflowCxPageTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDialogflowCxPageTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionRouteGroupsInput")
    def transition_route_groups_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transitionRouteGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="transitionRoutesInput")
    def transition_routes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageTransitionRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageTransitionRoutes"]]], jsii.get(self, "transitionRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPage, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPage, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="languageCode")
    def language_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "languageCode"))

    @language_code.setter
    def language_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPage, "language_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "languageCode", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPage, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="transitionRouteGroups")
    def transition_route_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transitionRouteGroups"))

    @transition_route_groups.setter
    def transition_route_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPage, "transition_route_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitionRouteGroups", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "entry_fulfillment": "entryFulfillment",
        "event_handlers": "eventHandlers",
        "form": "form",
        "id": "id",
        "language_code": "languageCode",
        "parent": "parent",
        "timeouts": "timeouts",
        "transition_route_groups": "transitionRouteGroups",
        "transition_routes": "transitionRoutes",
    },
)
class GoogleDialogflowCxPageConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        entry_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxPageEntryFulfillment", typing.Dict[str, typing.Any]]] = None,
        event_handlers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEventHandlers", typing.Dict[str, typing.Any]]]]] = None,
        form: typing.Optional[typing.Union["GoogleDialogflowCxPageForm", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        language_code: typing.Optional[builtins.str] = None,
        parent: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDialogflowCxPageTimeouts", typing.Dict[str, typing.Any]]] = None,
        transition_route_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        transition_routes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageTransitionRoutes", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: The human-readable name of the page, unique within the agent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#display_name GoogleDialogflowCxPage#display_name}
        :param entry_fulfillment: entry_fulfillment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#entry_fulfillment GoogleDialogflowCxPage#entry_fulfillment}
        :param event_handlers: event_handlers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#event_handlers GoogleDialogflowCxPage#event_handlers}
        :param form: form block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#form GoogleDialogflowCxPage#form}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#id GoogleDialogflowCxPage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language_code: The language of the following fields in page:. Page.entry_fulfillment.messages Page.entry_fulfillment.conditional_cases Page.event_handlers.trigger_fulfillment.messages Page.event_handlers.trigger_fulfillment.conditional_cases Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases Page.form.parameters.fill_behavior.reprompt_event_handlers.messages Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases Page.transition_routes.trigger_fulfillment.messages Page.transition_routes.trigger_fulfillment.conditional_cases If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#language_code GoogleDialogflowCxPage#language_code}
        :param parent: The flow to create a page for. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#parent GoogleDialogflowCxPage#parent}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#timeouts GoogleDialogflowCxPage#timeouts}
        :param transition_route_groups: Ordered list of TransitionRouteGroups associated with the page. Transition route groups must be unique within a page. If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:projects//locations//agents//flows//transitionRouteGroups/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#transition_route_groups GoogleDialogflowCxPage#transition_route_groups}
        :param transition_routes: transition_routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#transition_routes GoogleDialogflowCxPage#transition_routes}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(entry_fulfillment, dict):
            entry_fulfillment = GoogleDialogflowCxPageEntryFulfillment(**entry_fulfillment)
        if isinstance(form, dict):
            form = GoogleDialogflowCxPageForm(**form)
        if isinstance(timeouts, dict):
            timeouts = GoogleDialogflowCxPageTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument entry_fulfillment", value=entry_fulfillment, expected_type=type_hints["entry_fulfillment"])
            check_type(argname="argument event_handlers", value=event_handlers, expected_type=type_hints["event_handlers"])
            check_type(argname="argument form", value=form, expected_type=type_hints["form"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument language_code", value=language_code, expected_type=type_hints["language_code"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument transition_route_groups", value=transition_route_groups, expected_type=type_hints["transition_route_groups"])
            check_type(argname="argument transition_routes", value=transition_routes, expected_type=type_hints["transition_routes"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
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
        if entry_fulfillment is not None:
            self._values["entry_fulfillment"] = entry_fulfillment
        if event_handlers is not None:
            self._values["event_handlers"] = event_handlers
        if form is not None:
            self._values["form"] = form
        if id is not None:
            self._values["id"] = id
        if language_code is not None:
            self._values["language_code"] = language_code
        if parent is not None:
            self._values["parent"] = parent
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if transition_route_groups is not None:
            self._values["transition_route_groups"] = transition_route_groups
        if transition_routes is not None:
            self._values["transition_routes"] = transition_routes

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
    def display_name(self) -> builtins.str:
        '''The human-readable name of the page, unique within the agent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#display_name GoogleDialogflowCxPage#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entry_fulfillment(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEntryFulfillment"]:
        '''entry_fulfillment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#entry_fulfillment GoogleDialogflowCxPage#entry_fulfillment}
        '''
        result = self._values.get("entry_fulfillment")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEntryFulfillment"], result)

    @builtins.property
    def event_handlers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEventHandlers"]]]:
        '''event_handlers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#event_handlers GoogleDialogflowCxPage#event_handlers}
        '''
        result = self._values.get("event_handlers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEventHandlers"]]], result)

    @builtins.property
    def form(self) -> typing.Optional["GoogleDialogflowCxPageForm"]:
        '''form block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#form GoogleDialogflowCxPage#form}
        '''
        result = self._values.get("form")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageForm"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#id GoogleDialogflowCxPage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language_code(self) -> typing.Optional[builtins.str]:
        '''The language of the following fields in page:.

        Page.entry_fulfillment.messages
        Page.entry_fulfillment.conditional_cases
        Page.event_handlers.trigger_fulfillment.messages
        Page.event_handlers.trigger_fulfillment.conditional_cases
        Page.form.parameters.fill_behavior.initial_prompt_fulfillment.messages
        Page.form.parameters.fill_behavior.initial_prompt_fulfillment.conditional_cases
        Page.form.parameters.fill_behavior.reprompt_event_handlers.messages
        Page.form.parameters.fill_behavior.reprompt_event_handlers.conditional_cases
        Page.transition_routes.trigger_fulfillment.messages
        Page.transition_routes.trigger_fulfillment.conditional_cases
        If not specified, the agent's default language is used. Many languages are supported. Note: languages must be enabled in the agent before they can be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#language_code GoogleDialogflowCxPage#language_code}
        '''
        result = self._values.get("language_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[builtins.str]:
        '''The flow to create a page for. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#parent GoogleDialogflowCxPage#parent}
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDialogflowCxPageTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#timeouts GoogleDialogflowCxPage#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageTimeouts"], result)

    @builtins.property
    def transition_route_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Ordered list of TransitionRouteGroups associated with the page.

        Transition route groups must be unique within a page.
        If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes.
        If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence.
        Format:projects//locations//agents//flows//transitionRouteGroups/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#transition_route_groups GoogleDialogflowCxPage#transition_route_groups}
        '''
        result = self._values.get("transition_route_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def transition_routes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageTransitionRoutes"]]]:
        '''transition_routes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#transition_routes GoogleDialogflowCxPage#transition_routes}
        '''
        result = self._values.get("transition_routes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageTransitionRoutes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillment",
    jsii_struct_bases=[],
    name_mapping={
        "messages": "messages",
        "return_partial_responses": "returnPartialResponses",
        "tag": "tag",
        "webhook": "webhook",
    },
)
class GoogleDialogflowCxPageEntryFulfillment:
    def __init__(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEntryFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillment.__init__)
            check_type(argname="argument messages", value=messages, expected_type=type_hints["messages"])
            check_type(argname="argument return_partial_responses", value=return_partial_responses, expected_type=type_hints["return_partial_responses"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[str, typing.Any] = {}
        if messages is not None:
            self._values["messages"] = messages
        if return_partial_responses is not None:
            self._values["return_partial_responses"] = return_partial_responses
        if tag is not None:
            self._values["tag"] = tag
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEntryFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEntryFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEntryFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillmentMessages",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageEntryFulfillmentMessages:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Union["GoogleDialogflowCxPageEntryFulfillmentMessagesText", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text: text block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if isinstance(text, dict):
            text = GoogleDialogflowCxPageEntryFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentMessages.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEntryFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEntryFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEntryFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageEntryFulfillmentMessagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentMessagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentMessagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEntryFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEntryFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEntryFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putText")
    def put_text(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        value = GoogleDialogflowCxPageEntryFulfillmentMessagesText(text=text)

        return typing.cast(None, jsii.invoke(self, "putText", [value]))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference":
        return typing.cast("GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEntryFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEntryFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageEntryFulfillmentMessages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageEntryFulfillmentMessages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageEntryFulfillmentMessages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageEntryFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentMessagesText.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEntryFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "text"))

    @text.setter
    def text(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageEntryFulfillmentMessagesText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageEntryFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageEntryFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageEntryFulfillmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEntryFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxPageEntryFulfillmentMessages, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEntryFulfillmentOutputReference.put_messages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="resetMessages")
    def reset_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessages", []))

    @jsii.member(jsii_name="resetReturnPartialResponses")
    def reset_return_partial_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnPartialResponses", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(self) -> GoogleDialogflowCxPageEntryFulfillmentMessagesList:
        return typing.cast(GoogleDialogflowCxPageEntryFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEntryFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEntryFulfillmentMessages]]], jsii.get(self, "messagesInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponsesInput")
    def return_partial_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnPartialResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponses")
    def return_partial_responses(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnPartialResponses"))

    @return_partial_responses.setter
    def return_partial_responses(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentOutputReference, "return_partial_responses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentOutputReference, "webhook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDialogflowCxPageEntryFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageEntryFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageEntryFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEntryFulfillmentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlers",
    jsii_struct_bases=[],
    name_mapping={
        "event": "event",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class GoogleDialogflowCxPageEventHandlers:
    def __init__(
        self,
        *,
        event: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxPageEventHandlersTriggerFulfillment", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param event: The name of the event to handle. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#event GoogleDialogflowCxPage#event}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_flow GoogleDialogflowCxPage#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_page GoogleDialogflowCxPage#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#trigger_fulfillment GoogleDialogflowCxPage#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = GoogleDialogflowCxPageEventHandlersTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlers.__init__)
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument target_flow", value=target_flow, expected_type=type_hints["target_flow"])
            check_type(argname="argument target_page", value=target_page, expected_type=type_hints["target_page"])
            check_type(argname="argument trigger_fulfillment", value=trigger_fulfillment, expected_type=type_hints["trigger_fulfillment"])
        self._values: typing.Dict[str, typing.Any] = {}
        if event is not None:
            self._values["event"] = event
        if target_flow is not None:
            self._values["target_flow"] = target_flow
        if target_page is not None:
            self._values["target_page"] = target_page
        if trigger_fulfillment is not None:
            self._values["trigger_fulfillment"] = trigger_fulfillment

    @builtins.property
    def event(self) -> typing.Optional[builtins.str]:
        '''The name of the event to handle.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#event GoogleDialogflowCxPage#event}
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_flow GoogleDialogflowCxPage#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_page GoogleDialogflowCxPage#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#trigger_fulfillment GoogleDialogflowCxPage#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEventHandlers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageEventHandlersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageEventHandlersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageEventHandlersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageEventHandlersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        value = GoogleDialogflowCxPageEventHandlersTriggerFulfillment(
            messages=messages,
            return_partial_responses=return_partial_responses,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerFulfillment", [value]))

    @jsii.member(jsii_name="resetEvent")
    def reset_event(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvent", []))

    @jsii.member(jsii_name="resetTargetFlow")
    def reset_target_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFlow", []))

    @jsii.member(jsii_name="resetTargetPage")
    def reset_target_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPage", []))

    @jsii.member(jsii_name="resetTriggerFulfillment")
    def reset_trigger_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerFulfillment", []))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference":
        return typing.cast("GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="eventInput")
    def event_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventInput"))

    @builtins.property
    @jsii.member(jsii_name="targetFlowInput")
    def target_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPageInput")
    def target_page_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPageInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillmentInput")
    def trigger_fulfillment_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillment"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "event"))

    @event.setter
    def event(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersOutputReference, "event").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersOutputReference, "target_flow").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersOutputReference, "target_page").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageEventHandlers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageEventHandlers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageEventHandlers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillment",
    jsii_struct_bases=[],
    name_mapping={
        "messages": "messages",
        "return_partial_responses": "returnPartialResponses",
        "tag": "tag",
        "webhook": "webhook",
    },
)
class GoogleDialogflowCxPageEventHandlersTriggerFulfillment:
    def __init__(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillment.__init__)
            check_type(argname="argument messages", value=messages, expected_type=type_hints["messages"])
            check_type(argname="argument return_partial_responses", value=return_partial_responses, expected_type=type_hints["return_partial_responses"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[str, typing.Any] = {}
        if messages is not None:
            self._values["messages"] = messages
        if return_partial_responses is not None:
            self._values["return_partial_responses"] = return_partial_responses
        if tag is not None:
            self._values["tag"] = tag
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEventHandlersTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Union["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text: text block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if isinstance(text, dict):
            text = GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putText")
    def put_text(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        value = GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText(
            text=text
        )

        return typing.cast(None, jsii.invoke(self, "putText", [value]))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "text"))

    @text.setter
    def text(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference.put_messages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="resetMessages")
    def reset_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessages", []))

    @jsii.member(jsii_name="resetReturnPartialResponses")
    def reset_return_partial_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnPartialResponses", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList:
        return typing.cast(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponsesInput")
    def return_partial_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnPartialResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponses")
    def return_partial_responses(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnPartialResponses"))

    @return_partial_responses.setter
    def return_partial_responses(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference, "return_partial_responses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference, "webhook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageEventHandlersTriggerFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageEventHandlersTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageEventHandlersTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageForm",
    jsii_struct_bases=[],
    name_mapping={"parameters": "parameters"},
)
class GoogleDialogflowCxPageForm:
    def __init__(
        self,
        *,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageFormParameters", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#parameters GoogleDialogflowCxPage#parameters}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageForm.__init__)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {}
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageFormParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#parameters GoogleDialogflowCxPage#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageFormParameters"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageForm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageFormOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageFormParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormOutputReference.put_parameters)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "GoogleDialogflowCxPageFormParametersList":
        return typing.cast("GoogleDialogflowCxPageFormParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageFormParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageFormParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDialogflowCxPageForm]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageForm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageForm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParameters",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "entity_type": "entityType",
        "fill_behavior": "fillBehavior",
        "is_list": "isList",
        "redact": "redact",
        "required": "required",
    },
)
class GoogleDialogflowCxPageFormParameters:
    def __init__(
        self,
        *,
        display_name: typing.Optional[builtins.str] = None,
        entity_type: typing.Optional[builtins.str] = None,
        fill_behavior: typing.Optional[typing.Union["GoogleDialogflowCxPageFormParametersFillBehavior", typing.Dict[str, typing.Any]]] = None,
        is_list: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        redact: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param display_name: The human-readable name of the parameter, unique within the form. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#display_name GoogleDialogflowCxPage#display_name}
        :param entity_type: The entity type of the parameter. Format: projects/-/locations/-/agents/-/entityTypes/ for system entity types (for example, projects/-/locations/-/agents/-/entityTypes/sys.date), or projects//locations//agents//entityTypes/ for developer entity types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#entity_type GoogleDialogflowCxPage#entity_type}
        :param fill_behavior: fill_behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#fill_behavior GoogleDialogflowCxPage#fill_behavior}
        :param is_list: Indicates whether the parameter represents a list of values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#is_list GoogleDialogflowCxPage#is_list}
        :param redact: Indicates whether the parameter content should be redacted in log. If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or entity type level redaction is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#redact GoogleDialogflowCxPage#redact}
        :param required: Indicates whether the parameter is required. Optional parameters will not trigger prompts; however, they are filled if the user specifies them. Required parameters must be filled before form filling concludes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#required GoogleDialogflowCxPage#required}
        '''
        if isinstance(fill_behavior, dict):
            fill_behavior = GoogleDialogflowCxPageFormParametersFillBehavior(**fill_behavior)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParameters.__init__)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            check_type(argname="argument fill_behavior", value=fill_behavior, expected_type=type_hints["fill_behavior"])
            check_type(argname="argument is_list", value=is_list, expected_type=type_hints["is_list"])
            check_type(argname="argument redact", value=redact, expected_type=type_hints["redact"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {}
        if display_name is not None:
            self._values["display_name"] = display_name
        if entity_type is not None:
            self._values["entity_type"] = entity_type
        if fill_behavior is not None:
            self._values["fill_behavior"] = fill_behavior
        if is_list is not None:
            self._values["is_list"] = is_list
        if redact is not None:
            self._values["redact"] = redact
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The human-readable name of the parameter, unique within the form.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#display_name GoogleDialogflowCxPage#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entity_type(self) -> typing.Optional[builtins.str]:
        '''The entity type of the parameter.

        Format: projects/-/locations/-/agents/-/entityTypes/ for system entity types (for example, projects/-/locations/-/agents/-/entityTypes/sys.date), or projects//locations//agents//entityTypes/ for developer entity types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#entity_type GoogleDialogflowCxPage#entity_type}
        '''
        result = self._values.get("entity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fill_behavior(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageFormParametersFillBehavior"]:
        '''fill_behavior block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#fill_behavior GoogleDialogflowCxPage#fill_behavior}
        '''
        result = self._values.get("fill_behavior")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageFormParametersFillBehavior"], result)

    @builtins.property
    def is_list(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the parameter represents a list of values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#is_list GoogleDialogflowCxPage#is_list}
        '''
        result = self._values.get("is_list")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def redact(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the parameter content should be redacted in log.

        If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or entity type level redaction is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#redact GoogleDialogflowCxPage#redact}
        '''
        result = self._values.get("redact")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the parameter is required.

        Optional parameters will not trigger prompts; however, they are filled if the user specifies them.
        Required parameters must be filled before form filling concludes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#required GoogleDialogflowCxPage#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageFormParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehavior",
    jsii_struct_bases=[],
    name_mapping={"initial_prompt_fulfillment": "initialPromptFulfillment"},
)
class GoogleDialogflowCxPageFormParametersFillBehavior:
    def __init__(
        self,
        *,
        initial_prompt_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param initial_prompt_fulfillment: initial_prompt_fulfillment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#initial_prompt_fulfillment GoogleDialogflowCxPage#initial_prompt_fulfillment}
        '''
        if isinstance(initial_prompt_fulfillment, dict):
            initial_prompt_fulfillment = GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment(**initial_prompt_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehavior.__init__)
            check_type(argname="argument initial_prompt_fulfillment", value=initial_prompt_fulfillment, expected_type=type_hints["initial_prompt_fulfillment"])
        self._values: typing.Dict[str, typing.Any] = {}
        if initial_prompt_fulfillment is not None:
            self._values["initial_prompt_fulfillment"] = initial_prompt_fulfillment

    @builtins.property
    def initial_prompt_fulfillment(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment"]:
        '''initial_prompt_fulfillment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#initial_prompt_fulfillment GoogleDialogflowCxPage#initial_prompt_fulfillment}
        '''
        result = self._values.get("initial_prompt_fulfillment")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageFormParametersFillBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment",
    jsii_struct_bases=[],
    name_mapping={
        "messages": "messages",
        "return_partial_responses": "returnPartialResponses",
        "tag": "tag",
        "webhook": "webhook",
    },
)
class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment:
    def __init__(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment.__init__)
            check_type(argname="argument messages", value=messages, expected_type=type_hints["messages"])
            check_type(argname="argument return_partial_responses", value=return_partial_responses, expected_type=type_hints["return_partial_responses"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[str, typing.Any] = {}
        if messages is not None:
            self._values["messages"] = messages
        if return_partial_responses is not None:
            self._values["return_partial_responses"] = return_partial_responses
        if tag is not None:
            self._values["tag"] = tag
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Union["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text: text block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if isinstance(text, dict):
            text = GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putText")
    def put_text(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        value = GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText(
            text=text
        )

        return typing.cast(None, jsii.invoke(self, "putText", [value]))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference":
        return typing.cast("GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "text"))

    @text.setter
    def text(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference.put_messages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="resetMessages")
    def reset_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessages", []))

    @jsii.member(jsii_name="resetReturnPartialResponses")
    def reset_return_partial_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnPartialResponses", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList:
        return typing.cast(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages]]], jsii.get(self, "messagesInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponsesInput")
    def return_partial_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnPartialResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponses")
    def return_partial_responses(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnPartialResponses"))

    @return_partial_responses.setter
    def return_partial_responses(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference, "return_partial_responses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference, "webhook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInitialPromptFulfillment")
    def put_initial_prompt_fulfillment(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages, typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        value = GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment(
            messages=messages,
            return_partial_responses=return_partial_responses,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putInitialPromptFulfillment", [value]))

    @jsii.member(jsii_name="resetInitialPromptFulfillment")
    def reset_initial_prompt_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialPromptFulfillment", []))

    @builtins.property
    @jsii.member(jsii_name="initialPromptFulfillment")
    def initial_prompt_fulfillment(
        self,
    ) -> GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference:
        return typing.cast(GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference, jsii.get(self, "initialPromptFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="initialPromptFulfillmentInput")
    def initial_prompt_fulfillment_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment], jsii.get(self, "initialPromptFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageFormParametersFillBehavior]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageFormParametersFillBehavior], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageFormParametersFillBehavior],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageFormParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageFormParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageFormParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageFormParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageFormParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageFormParametersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageFormParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFillBehavior")
    def put_fill_behavior(
        self,
        *,
        initial_prompt_fulfillment: typing.Optional[typing.Union[GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param initial_prompt_fulfillment: initial_prompt_fulfillment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#initial_prompt_fulfillment GoogleDialogflowCxPage#initial_prompt_fulfillment}
        '''
        value = GoogleDialogflowCxPageFormParametersFillBehavior(
            initial_prompt_fulfillment=initial_prompt_fulfillment
        )

        return typing.cast(None, jsii.invoke(self, "putFillBehavior", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEntityType")
    def reset_entity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityType", []))

    @jsii.member(jsii_name="resetFillBehavior")
    def reset_fill_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFillBehavior", []))

    @jsii.member(jsii_name="resetIsList")
    def reset_is_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsList", []))

    @jsii.member(jsii_name="resetRedact")
    def reset_redact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedact", []))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="fillBehavior")
    def fill_behavior(
        self,
    ) -> GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference:
        return typing.cast(GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference, jsii.get(self, "fillBehavior"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="entityTypeInput")
    def entity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fillBehaviorInput")
    def fill_behavior_input(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageFormParametersFillBehavior]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageFormParametersFillBehavior], jsii.get(self, "fillBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="isListInput")
    def is_list_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isListInput"))

    @builtins.property
    @jsii.member(jsii_name="redactInput")
    def redact_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "redactInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="entityType")
    def entity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityType"))

    @entity_type.setter
    def entity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersOutputReference, "entity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityType", value)

    @builtins.property
    @jsii.member(jsii_name="isList")
    def is_list(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isList"))

    @is_list.setter
    def is_list(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersOutputReference, "is_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isList", value)

    @builtins.property
    @jsii.member(jsii_name="redact")
    def redact(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "redact"))

    @redact.setter
    def redact(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersOutputReference, "redact").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redact", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersOutputReference, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageFormParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageFormParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageFormParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageFormParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDialogflowCxPageTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#create GoogleDialogflowCxPage#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#delete GoogleDialogflowCxPage#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#update GoogleDialogflowCxPage#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#create GoogleDialogflowCxPage#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#delete GoogleDialogflowCxPage#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#update GoogleDialogflowCxPage#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutes",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "intent": "intent",
        "target_flow": "targetFlow",
        "target_page": "targetPage",
        "trigger_fulfillment": "triggerFulfillment",
    },
)
class GoogleDialogflowCxPageTransitionRoutes:
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        intent: typing.Optional[builtins.str] = None,
        target_flow: typing.Optional[builtins.str] = None,
        target_page: typing.Optional[builtins.str] = None,
        trigger_fulfillment: typing.Optional[typing.Union["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param condition: The condition to evaluate against form parameters or session parameters. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#condition GoogleDialogflowCxPage#condition}
        :param intent: The unique identifier of an Intent. Format: projects//locations//agents//intents/. Indicates that the transition can only happen when the given intent is matched. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#intent GoogleDialogflowCxPage#intent}
        :param target_flow: The target flow to transition to. Format: projects//locations//agents//flows/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_flow GoogleDialogflowCxPage#target_flow}
        :param target_page: The target page to transition to. Format: projects//locations//agents//flows//pages/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_page GoogleDialogflowCxPage#target_page}
        :param trigger_fulfillment: trigger_fulfillment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#trigger_fulfillment GoogleDialogflowCxPage#trigger_fulfillment}
        '''
        if isinstance(trigger_fulfillment, dict):
            trigger_fulfillment = GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment(**trigger_fulfillment)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutes.__init__)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument intent", value=intent, expected_type=type_hints["intent"])
            check_type(argname="argument target_flow", value=target_flow, expected_type=type_hints["target_flow"])
            check_type(argname="argument target_page", value=target_page, expected_type=type_hints["target_page"])
            check_type(argname="argument trigger_fulfillment", value=trigger_fulfillment, expected_type=type_hints["trigger_fulfillment"])
        self._values: typing.Dict[str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if intent is not None:
            self._values["intent"] = intent
        if target_flow is not None:
            self._values["target_flow"] = target_flow
        if target_page is not None:
            self._values["target_page"] = target_page
        if trigger_fulfillment is not None:
            self._values["trigger_fulfillment"] = trigger_fulfillment

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''The condition to evaluate against form parameters or session parameters.

        At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#condition GoogleDialogflowCxPage#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def intent(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an Intent.

        Format: projects//locations//agents//intents/. Indicates that the transition can only happen when the given intent is matched. At least one of intent or condition must be specified. When both intent and condition are specified, the transition can only happen when both are fulfilled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#intent GoogleDialogflowCxPage#intent}
        '''
        result = self._values.get("intent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_flow(self) -> typing.Optional[builtins.str]:
        '''The target flow to transition to. Format: projects//locations//agents//flows/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_flow GoogleDialogflowCxPage#target_flow}
        '''
        result = self._values.get("target_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_page(self) -> typing.Optional[builtins.str]:
        '''The target page to transition to. Format: projects//locations//agents//flows//pages/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#target_page GoogleDialogflowCxPage#target_page}
        '''
        result = self._values.get("target_page")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_fulfillment(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment"]:
        '''trigger_fulfillment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#trigger_fulfillment GoogleDialogflowCxPage#trigger_fulfillment}
        '''
        result = self._values.get("trigger_fulfillment")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageTransitionRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageTransitionRoutesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageTransitionRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageTransitionRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageTransitionRoutesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTriggerFulfillment")
    def put_trigger_fulfillment(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        value = GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment(
            messages=messages,
            return_partial_responses=return_partial_responses,
            tag=tag,
            webhook=webhook,
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerFulfillment", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetIntent")
    def reset_intent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntent", []))

    @jsii.member(jsii_name="resetTargetFlow")
    def reset_target_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetFlow", []))

    @jsii.member(jsii_name="resetTargetPage")
    def reset_target_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetPage", []))

    @jsii.member(jsii_name="resetTriggerFulfillment")
    def reset_trigger_fulfillment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerFulfillment", []))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference":
        return typing.cast("GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference", jsii.get(self, "triggerFulfillment"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="intentInput")
    def intent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intentInput"))

    @builtins.property
    @jsii.member(jsii_name="targetFlowInput")
    def target_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetFlowInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPageInput")
    def target_page_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPageInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerFulfillmentInput")
    def trigger_fulfillment_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment"], jsii.get(self, "triggerFulfillmentInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesOutputReference, "condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="intent")
    def intent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "intent"))

    @intent.setter
    def intent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesOutputReference, "intent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intent", value)

    @builtins.property
    @jsii.member(jsii_name="targetFlow")
    def target_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetFlow"))

    @target_flow.setter
    def target_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesOutputReference, "target_flow").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetFlow", value)

    @builtins.property
    @jsii.member(jsii_name="targetPage")
    def target_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPage"))

    @target_page.setter
    def target_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesOutputReference, "target_page").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageTransitionRoutes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageTransitionRoutes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageTransitionRoutes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment",
    jsii_struct_bases=[],
    name_mapping={
        "messages": "messages",
        "return_partial_responses": "returnPartialResponses",
        "tag": "tag",
        "webhook": "webhook",
    },
)
class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment:
    def __init__(
        self,
        *,
        messages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages", typing.Dict[str, typing.Any]]]]] = None,
        return_partial_responses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
        webhook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param messages: messages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        :param return_partial_responses: Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs. If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        :param tag: The tag used by the webhook to identify which fulfillment is being called. This field is required if webhook is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        :param webhook: The webhook to call. Format: projects//locations//agents//webhooks/. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment.__init__)
            check_type(argname="argument messages", value=messages, expected_type=type_hints["messages"])
            check_type(argname="argument return_partial_responses", value=return_partial_responses, expected_type=type_hints["return_partial_responses"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
        self._values: typing.Dict[str, typing.Any] = {}
        if messages is not None:
            self._values["messages"] = messages
        if return_partial_responses is not None:
            self._values["return_partial_responses"] = return_partial_responses
        if tag is not None:
            self._values["tag"] = tag
        if webhook is not None:
            self._values["webhook"] = webhook

    @builtins.property
    def messages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages"]]]:
        '''messages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#messages GoogleDialogflowCxPage#messages}
        '''
        result = self._values.get("messages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages"]]], result)

    @builtins.property
    def return_partial_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether Dialogflow should return currently queued fulfillment response messages in streaming APIs.

        If a webhook is specified, it happens before Dialogflow invokes webhook. Warning: 1) This flag only affects streaming API. Responses are still queued and returned once in non-streaming API. 2) The flag can be enabled in any fulfillment but only the first 3 partial responses will be returned. You may only want to apply it to fulfillments that have slow webhooks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#return_partial_responses GoogleDialogflowCxPage#return_partial_responses}
        '''
        result = self._values.get("return_partial_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The tag used by the webhook to identify which fulfillment is being called.

        This field is required if webhook is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#tag GoogleDialogflowCxPage#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook(self) -> typing.Optional[builtins.str]:
        '''The webhook to call. Format: projects//locations//agents//webhooks/.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#webhook GoogleDialogflowCxPage#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Union["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param text: text block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if isinstance(text, dict):
            text = GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText(**text)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"]:
        '''text block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putText")
    def put_text(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        value = GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText(
            text=text
        )

        return typing.cast(None, jsii.invoke(self, "putText", [value]))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(
        self,
    ) -> "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference":
        return typing.cast("GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference", jsii.get(self, "text"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(
        self,
    ) -> typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"]:
        return typing.cast(typing.Optional["GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText"], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText",
    jsii_struct_bases=[],
    name_mapping={"text": "text"},
)
class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText:
    def __init__(
        self,
        *,
        text: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param text: A collection of text responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText.__init__)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {}
        if text is not None:
            self._values["text"] = text

    @builtins.property
    def text(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A collection of text responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dialogflow_cx_page#text GoogleDialogflowCxPage#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @builtins.property
    @jsii.member(jsii_name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "allowPlaybackInterruption"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "text"))

    @text.setter
    def text(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDialogflowCxPage.GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMessages")
    def put_messages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference.put_messages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessages", [value]))

    @jsii.member(jsii_name="resetMessages")
    def reset_messages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessages", []))

    @jsii.member(jsii_name="resetReturnPartialResponses")
    def reset_return_partial_responses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnPartialResponses", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @builtins.property
    @jsii.member(jsii_name="messages")
    def messages(
        self,
    ) -> GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList:
        return typing.cast(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList, jsii.get(self, "messages"))

    @builtins.property
    @jsii.member(jsii_name="messagesInput")
    def messages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages]]], jsii.get(self, "messagesInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponsesInput")
    def return_partial_responses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnPartialResponsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="returnPartialResponses")
    def return_partial_responses(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnPartialResponses"))

    @return_partial_responses.setter
    def return_partial_responses(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference, "return_partial_responses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnPartialResponses", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhook"))

    @webhook.setter
    def webhook(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference, "webhook").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhook", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment]:
        return typing.cast(typing.Optional[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDialogflowCxPage",
    "GoogleDialogflowCxPageConfig",
    "GoogleDialogflowCxPageEntryFulfillment",
    "GoogleDialogflowCxPageEntryFulfillmentMessages",
    "GoogleDialogflowCxPageEntryFulfillmentMessagesList",
    "GoogleDialogflowCxPageEntryFulfillmentMessagesOutputReference",
    "GoogleDialogflowCxPageEntryFulfillmentMessagesText",
    "GoogleDialogflowCxPageEntryFulfillmentMessagesTextOutputReference",
    "GoogleDialogflowCxPageEntryFulfillmentOutputReference",
    "GoogleDialogflowCxPageEventHandlers",
    "GoogleDialogflowCxPageEventHandlersList",
    "GoogleDialogflowCxPageEventHandlersOutputReference",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillment",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessages",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesList",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesOutputReference",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesText",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentMessagesTextOutputReference",
    "GoogleDialogflowCxPageEventHandlersTriggerFulfillmentOutputReference",
    "GoogleDialogflowCxPageForm",
    "GoogleDialogflowCxPageFormOutputReference",
    "GoogleDialogflowCxPageFormParameters",
    "GoogleDialogflowCxPageFormParametersFillBehavior",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillment",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessages",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesList",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesOutputReference",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesText",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentMessagesTextOutputReference",
    "GoogleDialogflowCxPageFormParametersFillBehaviorInitialPromptFulfillmentOutputReference",
    "GoogleDialogflowCxPageFormParametersFillBehaviorOutputReference",
    "GoogleDialogflowCxPageFormParametersList",
    "GoogleDialogflowCxPageFormParametersOutputReference",
    "GoogleDialogflowCxPageTimeouts",
    "GoogleDialogflowCxPageTimeoutsOutputReference",
    "GoogleDialogflowCxPageTransitionRoutes",
    "GoogleDialogflowCxPageTransitionRoutesList",
    "GoogleDialogflowCxPageTransitionRoutesOutputReference",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillment",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessages",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesList",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesOutputReference",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesText",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentMessagesTextOutputReference",
    "GoogleDialogflowCxPageTransitionRoutesTriggerFulfillmentOutputReference",
]

publication.publish()
