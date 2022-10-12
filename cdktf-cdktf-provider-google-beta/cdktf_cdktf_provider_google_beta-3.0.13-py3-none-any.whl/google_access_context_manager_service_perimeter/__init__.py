'''
# `google_access_context_manager_service_perimeter`

Refer to the Terraform Registory for docs: [`google_access_context_manager_service_perimeter`](https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter).
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


class GoogleAccessContextManagerServicePerimeter(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeter",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter google_access_context_manager_service_perimeter}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        parent: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        perimeter_type: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpec", typing.Dict[str, typing.Any]]] = None,
        status: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatus", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_explicit_dry_run_spec: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter google_access_context_manager_service_perimeter} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#name GoogleAccessContextManagerServicePerimeter#name}
        :param parent: The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#parent GoogleAccessContextManagerServicePerimeter#parent}
        :param title: Human readable title. Must be unique within the Policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#title GoogleAccessContextManagerServicePerimeter#title}
        :param description: Description of the ServicePerimeter and its use. Does not affect behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#description GoogleAccessContextManagerServicePerimeter#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#id GoogleAccessContextManagerServicePerimeter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param perimeter_type: Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies with many independent perimeters that need to share some data with a common perimeter, but should not be able to share data among themselves. Default value: "PERIMETER_TYPE_REGULAR" Possible values: ["PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#perimeter_type GoogleAccessContextManagerServicePerimeter#perimeter_type}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#spec GoogleAccessContextManagerServicePerimeter#spec}
        :param status: status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#status GoogleAccessContextManagerServicePerimeter#status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#timeouts GoogleAccessContextManagerServicePerimeter#timeouts}
        :param use_explicit_dry_run_spec: Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#use_explicit_dry_run_spec GoogleAccessContextManagerServicePerimeter#use_explicit_dry_run_spec}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeter.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAccessContextManagerServicePerimeterConfig(
            name=name,
            parent=parent,
            title=title,
            description=description,
            id=id,
            perimeter_type=perimeter_type,
            spec=spec,
            status=status,
            timeouts=timeouts,
            use_explicit_dry_run_spec=use_explicit_dry_run_spec,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        access_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
        egress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecEgressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        ingress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        restricted_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_accessible_services: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_levels: A list of AccessLevel resource names that allow resources within the ServicePerimeter to be accessed from the internet. AccessLevels listed must be in the same policy as this ServicePerimeter. Referencing a nonexistent AccessLevel is a syntax error. If no AccessLevel names are listed, resources within the perimeter can only be accessed via GCP calls with request origins within the perimeter. For Service Perimeter Bridge, must be empty. Format: accessPolicies/{policy_id}/accessLevels/{access_level_name} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_levels GoogleAccessContextManagerServicePerimeter#access_levels}
        :param egress_policies: egress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_policies GoogleAccessContextManagerServicePerimeter#egress_policies}
        :param ingress_policies: ingress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_policies GoogleAccessContextManagerServicePerimeter#ingress_policies}
        :param resources: A list of GCP resources that are inside of the service perimeter. Currently only projects are allowed. Format: projects/{project_number}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        :param restricted_services: GCP services that are subject to the Service Perimeter restrictions. Must contain a list of services. For example, if 'storage.googleapis.com' is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#restricted_services GoogleAccessContextManagerServicePerimeter#restricted_services}
        :param vpc_accessible_services: vpc_accessible_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#vpc_accessible_services GoogleAccessContextManagerServicePerimeter#vpc_accessible_services}
        '''
        value = GoogleAccessContextManagerServicePerimeterSpec(
            access_levels=access_levels,
            egress_policies=egress_policies,
            ingress_policies=ingress_policies,
            resources=resources,
            restricted_services=restricted_services,
            vpc_accessible_services=vpc_accessible_services,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putStatus")
    def put_status(
        self,
        *,
        access_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
        egress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusEgressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        ingress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        restricted_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_accessible_services: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_levels: A list of AccessLevel resource names that allow resources within the ServicePerimeter to be accessed from the internet. AccessLevels listed must be in the same policy as this ServicePerimeter. Referencing a nonexistent AccessLevel is a syntax error. If no AccessLevel names are listed, resources within the perimeter can only be accessed via GCP calls with request origins within the perimeter. For Service Perimeter Bridge, must be empty. Format: accessPolicies/{policy_id}/accessLevels/{access_level_name} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_levels GoogleAccessContextManagerServicePerimeter#access_levels}
        :param egress_policies: egress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_policies GoogleAccessContextManagerServicePerimeter#egress_policies}
        :param ingress_policies: ingress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_policies GoogleAccessContextManagerServicePerimeter#ingress_policies}
        :param resources: A list of GCP resources that are inside of the service perimeter. Currently only projects are allowed. Format: projects/{project_number}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        :param restricted_services: GCP services that are subject to the Service Perimeter restrictions. Must contain a list of services. For example, if 'storage.googleapis.com' is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#restricted_services GoogleAccessContextManagerServicePerimeter#restricted_services}
        :param vpc_accessible_services: vpc_accessible_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#vpc_accessible_services GoogleAccessContextManagerServicePerimeter#vpc_accessible_services}
        '''
        value = GoogleAccessContextManagerServicePerimeterStatus(
            access_levels=access_levels,
            egress_policies=egress_policies,
            ingress_policies=ingress_policies,
            resources=resources,
            restricted_services=restricted_services,
            vpc_accessible_services=vpc_accessible_services,
        )

        return typing.cast(None, jsii.invoke(self, "putStatus", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#create GoogleAccessContextManagerServicePerimeter#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#delete GoogleAccessContextManagerServicePerimeter#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#update GoogleAccessContextManagerServicePerimeter#update}.
        '''
        value = GoogleAccessContextManagerServicePerimeterTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPerimeterType")
    def reset_perimeter_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerimeterType", []))

    @jsii.member(jsii_name="resetSpec")
    def reset_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpec", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseExplicitDryRunSpec")
    def reset_use_explicit_dry_run_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseExplicitDryRunSpec", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "GoogleAccessContextManagerServicePerimeterSpecOutputReference":
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(
        self,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusOutputReference":
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusOutputReference", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference":
        return typing.cast("GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

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
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="perimeterTypeInput")
    def perimeter_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "perimeterTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpec"]:
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatus"]:
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatus"], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="useExplicitDryRunSpecInput")
    def use_explicit_dry_run_spec_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useExplicitDryRunSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)

    @builtins.property
    @jsii.member(jsii_name="perimeterType")
    def perimeter_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "perimeterType"))

    @perimeter_type.setter
    def perimeter_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "perimeter_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perimeterType", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="useExplicitDryRunSpec")
    def use_explicit_dry_run_spec(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useExplicitDryRunSpec"))

    @use_explicit_dry_run_spec.setter
    def use_explicit_dry_run_spec(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeter, "use_explicit_dry_run_spec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useExplicitDryRunSpec", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterConfig",
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
        "parent": "parent",
        "title": "title",
        "description": "description",
        "id": "id",
        "perimeter_type": "perimeterType",
        "spec": "spec",
        "status": "status",
        "timeouts": "timeouts",
        "use_explicit_dry_run_spec": "useExplicitDryRunSpec",
    },
)
class GoogleAccessContextManagerServicePerimeterConfig(cdktf.TerraformMetaArguments):
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
        parent: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        perimeter_type: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpec", typing.Dict[str, typing.Any]]] = None,
        status: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatus", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_explicit_dry_run_spec: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#name GoogleAccessContextManagerServicePerimeter#name}
        :param parent: The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#parent GoogleAccessContextManagerServicePerimeter#parent}
        :param title: Human readable title. Must be unique within the Policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#title GoogleAccessContextManagerServicePerimeter#title}
        :param description: Description of the ServicePerimeter and its use. Does not affect behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#description GoogleAccessContextManagerServicePerimeter#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#id GoogleAccessContextManagerServicePerimeter#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param perimeter_type: Specifies the type of the Perimeter. There are two types: regular and bridge. Regular Service Perimeter contains resources, access levels, and restricted services. Every resource can be in at most ONE regular Service Perimeter. In addition to being in a regular service perimeter, a resource can also be in zero or more perimeter bridges. A perimeter bridge only contains resources. Cross project operations are permitted if all effected resources share some perimeter (whether bridge or regular). Perimeter Bridge does not contain access levels or services: those are governed entirely by the regular perimeter that resource is in. Perimeter Bridges are typically useful when building more complex topologies with many independent perimeters that need to share some data with a common perimeter, but should not be able to share data among themselves. Default value: "PERIMETER_TYPE_REGULAR" Possible values: ["PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#perimeter_type GoogleAccessContextManagerServicePerimeter#perimeter_type}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#spec GoogleAccessContextManagerServicePerimeter#spec}
        :param status: status block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#status GoogleAccessContextManagerServicePerimeter#status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#timeouts GoogleAccessContextManagerServicePerimeter#timeouts}
        :param use_explicit_dry_run_spec: Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. useExplicitDryRunSpec must bet set to True if any of the fields in the spec are set to non-default values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#use_explicit_dry_run_spec GoogleAccessContextManagerServicePerimeter#use_explicit_dry_run_spec}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = GoogleAccessContextManagerServicePerimeterSpec(**spec)
        if isinstance(status, dict):
            status = GoogleAccessContextManagerServicePerimeterStatus(**status)
        if isinstance(timeouts, dict):
            timeouts = GoogleAccessContextManagerServicePerimeterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument perimeter_type", value=perimeter_type, expected_type=type_hints["perimeter_type"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_explicit_dry_run_spec", value=use_explicit_dry_run_spec, expected_type=type_hints["use_explicit_dry_run_spec"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "parent": parent,
            "title": title,
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
        if perimeter_type is not None:
            self._values["perimeter_type"] = perimeter_type
        if spec is not None:
            self._values["spec"] = spec
        if status is not None:
            self._values["status"] = status
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_explicit_dry_run_spec is not None:
            self._values["use_explicit_dry_run_spec"] = use_explicit_dry_run_spec

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
        '''Resource name for the ServicePerimeter. The short_name component must begin with a letter and only include alphanumeric and '_'. Format: accessPolicies/{policy_id}/servicePerimeters/{short_name}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#name GoogleAccessContextManagerServicePerimeter#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent(self) -> builtins.str:
        '''The AccessPolicy this ServicePerimeter lives in. Format: accessPolicies/{policy_id}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#parent GoogleAccessContextManagerServicePerimeter#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Human readable title. Must be unique within the Policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#title GoogleAccessContextManagerServicePerimeter#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the ServicePerimeter and its use. Does not affect behavior.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#description GoogleAccessContextManagerServicePerimeter#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#id GoogleAccessContextManagerServicePerimeter#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def perimeter_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of the Perimeter.

        There are two types: regular and
        bridge. Regular Service Perimeter contains resources, access levels,
        and restricted services. Every resource can be in at most
        ONE regular Service Perimeter.

        In addition to being in a regular service perimeter, a resource can also
        be in zero or more perimeter bridges. A perimeter bridge only contains
        resources. Cross project operations are permitted if all effected
        resources share some perimeter (whether bridge or regular). Perimeter
        Bridge does not contain access levels or services: those are governed
        entirely by the regular perimeter that resource is in.

        Perimeter Bridges are typically useful when building more complex
        topologies with many independent perimeters that need to share some data
        with a common perimeter, but should not be able to share data among
        themselves. Default value: "PERIMETER_TYPE_REGULAR" Possible values: ["PERIMETER_TYPE_REGULAR", "PERIMETER_TYPE_BRIDGE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#perimeter_type GoogleAccessContextManagerServicePerimeter#perimeter_type}
        '''
        result = self._values.get("perimeter_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spec(self) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpec"]:
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#spec GoogleAccessContextManagerServicePerimeter#spec}
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpec"], result)

    @builtins.property
    def status(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatus"]:
        '''status block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#status GoogleAccessContextManagerServicePerimeter#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatus"], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#timeouts GoogleAccessContextManagerServicePerimeter#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterTimeouts"], result)

    @builtins.property
    def use_explicit_dry_run_spec(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use explicit dry run spec flag.

        Ordinarily, a dry-run spec implicitly exists
        for all Service Perimeters, and that spec is identical to the status for those
        Service Perimeters. When this flag is set, it inhibits the generation of the
        implicit spec, thereby allowing the user to explicitly provide a
        configuration ("spec") to use in a dry-run version of the Service Perimeter.
        This allows the user to test changes to the enforced config ("status") without
        actually enforcing them. This testing is done through analyzing the differences
        between currently enforced and suggested restrictions. useExplicitDryRunSpec must
        bet set to True if any of the fields in the spec are set to non-default values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#use_explicit_dry_run_spec GoogleAccessContextManagerServicePerimeter#use_explicit_dry_run_spec}
        '''
        result = self._values.get("use_explicit_dry_run_spec")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpec",
    jsii_struct_bases=[],
    name_mapping={
        "access_levels": "accessLevels",
        "egress_policies": "egressPolicies",
        "ingress_policies": "ingressPolicies",
        "resources": "resources",
        "restricted_services": "restrictedServices",
        "vpc_accessible_services": "vpcAccessibleServices",
    },
)
class GoogleAccessContextManagerServicePerimeterSpec:
    def __init__(
        self,
        *,
        access_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
        egress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecEgressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        ingress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        restricted_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_accessible_services: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_levels: A list of AccessLevel resource names that allow resources within the ServicePerimeter to be accessed from the internet. AccessLevels listed must be in the same policy as this ServicePerimeter. Referencing a nonexistent AccessLevel is a syntax error. If no AccessLevel names are listed, resources within the perimeter can only be accessed via GCP calls with request origins within the perimeter. For Service Perimeter Bridge, must be empty. Format: accessPolicies/{policy_id}/accessLevels/{access_level_name} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_levels GoogleAccessContextManagerServicePerimeter#access_levels}
        :param egress_policies: egress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_policies GoogleAccessContextManagerServicePerimeter#egress_policies}
        :param ingress_policies: ingress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_policies GoogleAccessContextManagerServicePerimeter#ingress_policies}
        :param resources: A list of GCP resources that are inside of the service perimeter. Currently only projects are allowed. Format: projects/{project_number}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        :param restricted_services: GCP services that are subject to the Service Perimeter restrictions. Must contain a list of services. For example, if 'storage.googleapis.com' is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#restricted_services GoogleAccessContextManagerServicePerimeter#restricted_services}
        :param vpc_accessible_services: vpc_accessible_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#vpc_accessible_services GoogleAccessContextManagerServicePerimeter#vpc_accessible_services}
        '''
        if isinstance(vpc_accessible_services, dict):
            vpc_accessible_services = GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices(**vpc_accessible_services)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpec.__init__)
            check_type(argname="argument access_levels", value=access_levels, expected_type=type_hints["access_levels"])
            check_type(argname="argument egress_policies", value=egress_policies, expected_type=type_hints["egress_policies"])
            check_type(argname="argument ingress_policies", value=ingress_policies, expected_type=type_hints["ingress_policies"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument restricted_services", value=restricted_services, expected_type=type_hints["restricted_services"])
            check_type(argname="argument vpc_accessible_services", value=vpc_accessible_services, expected_type=type_hints["vpc_accessible_services"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_levels is not None:
            self._values["access_levels"] = access_levels
        if egress_policies is not None:
            self._values["egress_policies"] = egress_policies
        if ingress_policies is not None:
            self._values["ingress_policies"] = ingress_policies
        if resources is not None:
            self._values["resources"] = resources
        if restricted_services is not None:
            self._values["restricted_services"] = restricted_services
        if vpc_accessible_services is not None:
            self._values["vpc_accessible_services"] = vpc_accessible_services

    @builtins.property
    def access_levels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AccessLevel resource names that allow resources within the ServicePerimeter to be accessed from the internet.

        AccessLevels listed must be in the same policy as this
        ServicePerimeter. Referencing a nonexistent AccessLevel is a
        syntax error. If no AccessLevel names are listed, resources within
        the perimeter can only be accessed via GCP calls with request
        origins within the perimeter. For Service Perimeter Bridge, must
        be empty.

        Format: accessPolicies/{policy_id}/accessLevels/{access_level_name}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_levels GoogleAccessContextManagerServicePerimeter#access_levels}
        '''
        result = self._values.get("access_levels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def egress_policies(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecEgressPolicies"]]]:
        '''egress_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_policies GoogleAccessContextManagerServicePerimeter#egress_policies}
        '''
        result = self._values.get("egress_policies")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecEgressPolicies"]]], result)

    @builtins.property
    def ingress_policies(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPolicies"]]]:
        '''ingress_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_policies GoogleAccessContextManagerServicePerimeter#ingress_policies}
        '''
        result = self._values.get("ingress_policies")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPolicies"]]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of GCP resources that are inside of the service perimeter. Currently only projects are allowed. Format: projects/{project_number}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def restricted_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''GCP services that are subject to the Service Perimeter restrictions.

        Must contain a list of services. For example, if
        'storage.googleapis.com' is specified, access to the storage
        buckets inside the perimeter must meet the perimeter's access
        restrictions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#restricted_services GoogleAccessContextManagerServicePerimeter#restricted_services}
        '''
        result = self._values.get("restricted_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_accessible_services(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices"]:
        '''vpc_accessible_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#vpc_accessible_services GoogleAccessContextManagerServicePerimeter#vpc_accessible_services}
        '''
        result = self._values.get("vpc_accessible_services")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPolicies",
    jsii_struct_bases=[],
    name_mapping={"egress_from": "egressFrom", "egress_to": "egressTo"},
)
class GoogleAccessContextManagerServicePerimeterSpecEgressPolicies:
    def __init__(
        self,
        *,
        egress_from: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom", typing.Dict[str, typing.Any]]] = None,
        egress_to: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param egress_from: egress_from block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_from GoogleAccessContextManagerServicePerimeter#egress_from}
        :param egress_to: egress_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_to GoogleAccessContextManagerServicePerimeter#egress_to}
        '''
        if isinstance(egress_from, dict):
            egress_from = GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom(**egress_from)
        if isinstance(egress_to, dict):
            egress_to = GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo(**egress_to)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPolicies.__init__)
            check_type(argname="argument egress_from", value=egress_from, expected_type=type_hints["egress_from"])
            check_type(argname="argument egress_to", value=egress_to, expected_type=type_hints["egress_to"])
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_from is not None:
            self._values["egress_from"] = egress_from
        if egress_to is not None:
            self._values["egress_to"] = egress_to

    @builtins.property
    def egress_from(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom"]:
        '''egress_from block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_from GoogleAccessContextManagerServicePerimeter#egress_from}
        '''
        result = self._values.get("egress_from")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom"], result)

    @builtins.property
    def egress_to(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo"]:
        '''egress_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_to GoogleAccessContextManagerServicePerimeter#egress_to}
        '''
        result = self._values.get("egress_to")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecEgressPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom",
    jsii_struct_bases=[],
    name_mapping={"identities": "identities", "identity_type": "identityType"},
)
class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom:
    def __init__(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this 'EgressPolicy'. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom.__init__)
            check_type(argname="argument identities", value=identities, expected_type=type_hints["identities"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identities is not None:
            self._values["identities"] = identities
        if identity_type is not None:
            self._values["identity_type"] = identity_type

    @builtins.property
    def identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identities that are allowed access through this 'EgressPolicy'.

        Should be in the format of email address. The email address should
        represent individual user or service account only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        '''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of identities that are allowed access to outside the  perimeter.

        If left unspecified, then members of 'identities' field will
        be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentities")
    def reset_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentities", []))

    @jsii.member(jsii_name="resetIdentityType")
    def reset_identity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityType", []))

    @builtins.property
    @jsii.member(jsii_name="identitiesInput")
    def identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="identityTypeInput")
    def identity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="identities")
    def identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identities"))

    @identities.setter
    def identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference, "identities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identities", value)

    @builtins.property
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference, "identity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo",
    jsii_struct_bases=[],
    name_mapping={
        "external_resources": "externalResources",
        "operations": "operations",
        "resources": "resources",
    },
)
class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo:
    def __init__(
        self,
        *,
        external_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param external_resources: A list of external resources that are allowed to be accessed. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#external_resources GoogleAccessContextManagerServicePerimeter#external_resources}
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', that match this to stanza. A request matches if it contains a resource in this list. If * is specified for resources, then this 'EgressTo' rule will authorize access to all resources outside the perimeter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo.__init__)
            check_type(argname="argument external_resources", value=external_resources, expected_type=type_hints["external_resources"])
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if external_resources is not None:
            self._values["external_resources"] = external_resources
        if operations is not None:
            self._values["operations"] = operations
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def external_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of external resources that are allowed to be accessed.

        A request
        matches if it contains an external resource in this list (Example:
        s3://bucket/path). Currently '*' is not allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#external_resources GoogleAccessContextManagerServicePerimeter#external_resources}
        '''
        result = self._values.get("external_resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def operations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations"]]]:
        '''operations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        '''
        result = self._values.get("operations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations"]]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of resources, currently only projects in the form  'projects/', that match this to stanza.

        A request matches
        if it contains a resource in this list. If * is specified for resources,
        then this 'EgressTo' rule will authorize access to all resources outside
        the perimeter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations",
    jsii_struct_bases=[],
    name_mapping={
        "method_selectors": "methodSelectors",
        "service_name": "serviceName",
    },
)
class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations:
    def __init__(
        self,
        *,
        method_selectors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors", typing.Dict[str, typing.Any]]]]] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method_selectors: method_selectors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        :param service_name: The name of the API whose methods or permissions the 'IngressPolicy' or 'EgressPolicy' want to allow. A single 'ApiOperation' with serviceName field set to '*' will allow all methods AND permissions for all services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations.__init__)
            check_type(argname="argument method_selectors", value=method_selectors, expected_type=type_hints["method_selectors"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method_selectors is not None:
            self._values["method_selectors"] = method_selectors
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def method_selectors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors"]]]:
        '''method_selectors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        '''
        result = self._values.get("method_selectors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors"]]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''The name of the API whose methods or permissions the 'IngressPolicy' or  'EgressPolicy' want to allow.

        A single 'ApiOperation' with serviceName
        field set to '*' will allow all methods AND permissions for all services.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "permission": "permission"},
)
class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors:
    def __init__(
        self,
        *,
        method: typing.Optional[builtins.str] = None,
        permission: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Value for 'method' should be a valid method name for the corresponding 'serviceName' in 'ApiOperation'. If '*' used as value for method, then ALL methods and permissions are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        :param permission: Value for permission should be a valid Cloud IAM permission for the corresponding 'serviceName' in 'ApiOperation'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if permission is not None:
            self._values["permission"] = permission

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Value for 'method' should be a valid method name for the corresponding  'serviceName' in 'ApiOperation'.

        If '*' used as value for method,
        then ALL methods and permissions are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permission(self) -> typing.Optional[builtins.str]:
        '''Value for permission should be a valid Cloud IAM permission for the  corresponding 'serviceName' in 'ApiOperation'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        result = self._values.get("permission")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetPermission")
    def reset_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermission", []))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference, "permission").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMethodSelectors")
    def put_method_selectors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference.put_method_selectors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMethodSelectors", [value]))

    @jsii.member(jsii_name="resetMethodSelectors")
    def reset_method_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethodSelectors", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="methodSelectors")
    def method_selectors(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList, jsii.get(self, "methodSelectors"))

    @builtins.property
    @jsii.member(jsii_name="methodSelectorsInput")
    def method_selectors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors]]], jsii.get(self, "methodSelectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOperations")
    def put_operations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference.put_operations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOperations", [value]))

    @jsii.member(jsii_name="resetExternalResources")
    def reset_external_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalResources", []))

    @jsii.member(jsii_name="resetOperations")
    def reset_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperations", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList, jsii.get(self, "operations"))

    @builtins.property
    @jsii.member(jsii_name="externalResourcesInput")
    def external_resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations]]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="externalResources")
    def external_resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalResources"))

    @external_resources.setter
    def external_resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference, "external_resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalResources", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEgressFrom")
    def put_egress_from(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this 'EgressPolicy'. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        value = GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom(
            identities=identities, identity_type=identity_type
        )

        return typing.cast(None, jsii.invoke(self, "putEgressFrom", [value]))

    @jsii.member(jsii_name="putEgressTo")
    def put_egress_to(
        self,
        *,
        external_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations, typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param external_resources: A list of external resources that are allowed to be accessed. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#external_resources GoogleAccessContextManagerServicePerimeter#external_resources}
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', that match this to stanza. A request matches if it contains a resource in this list. If * is specified for resources, then this 'EgressTo' rule will authorize access to all resources outside the perimeter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        value = GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo(
            external_resources=external_resources,
            operations=operations,
            resources=resources,
        )

        return typing.cast(None, jsii.invoke(self, "putEgressTo", [value]))

    @jsii.member(jsii_name="resetEgressFrom")
    def reset_egress_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressFrom", []))

    @jsii.member(jsii_name="resetEgressTo")
    def reset_egress_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressTo", []))

    @builtins.property
    @jsii.member(jsii_name="egressFrom")
    def egress_from(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference, jsii.get(self, "egressFrom"))

    @builtins.property
    @jsii.member(jsii_name="egressTo")
    def egress_to(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference, jsii.get(self, "egressTo"))

    @builtins.property
    @jsii.member(jsii_name="egressFromInput")
    def egress_from_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom], jsii.get(self, "egressFromInput"))

    @builtins.property
    @jsii.member(jsii_name="egressToInput")
    def egress_to_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo], jsii.get(self, "egressToInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPolicies",
    jsii_struct_bases=[],
    name_mapping={"ingress_from": "ingressFrom", "ingress_to": "ingressTo"},
)
class GoogleAccessContextManagerServicePerimeterSpecIngressPolicies:
    def __init__(
        self,
        *,
        ingress_from: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom", typing.Dict[str, typing.Any]]] = None,
        ingress_to: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ingress_from: ingress_from block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_from GoogleAccessContextManagerServicePerimeter#ingress_from}
        :param ingress_to: ingress_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_to GoogleAccessContextManagerServicePerimeter#ingress_to}
        '''
        if isinstance(ingress_from, dict):
            ingress_from = GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom(**ingress_from)
        if isinstance(ingress_to, dict):
            ingress_to = GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo(**ingress_to)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPolicies.__init__)
            check_type(argname="argument ingress_from", value=ingress_from, expected_type=type_hints["ingress_from"])
            check_type(argname="argument ingress_to", value=ingress_to, expected_type=type_hints["ingress_to"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ingress_from is not None:
            self._values["ingress_from"] = ingress_from
        if ingress_to is not None:
            self._values["ingress_to"] = ingress_to

    @builtins.property
    def ingress_from(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom"]:
        '''ingress_from block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_from GoogleAccessContextManagerServicePerimeter#ingress_from}
        '''
        result = self._values.get("ingress_from")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom"], result)

    @builtins.property
    def ingress_to(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo"]:
        '''ingress_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_to GoogleAccessContextManagerServicePerimeter#ingress_to}
        '''
        result = self._values.get("ingress_to")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecIngressPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom",
    jsii_struct_bases=[],
    name_mapping={
        "identities": "identities",
        "identity_type": "identityType",
        "sources": "sources",
    },
)
class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom:
    def __init__(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        :param sources: sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#sources GoogleAccessContextManagerServicePerimeter#sources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom.__init__)
            check_type(argname="argument identities", value=identities, expected_type=type_hints["identities"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identities is not None:
            self._values["identities"] = identities
        if identity_type is not None:
            self._values["identity_type"] = identity_type
        if sources is not None:
            self._values["sources"] = sources

    @builtins.property
    def identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identities that are allowed access through this ingress policy.

        Should be in the format of email address. The email address should represent
        individual user or service account only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        '''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of identities that are allowed access from outside the  perimeter.

        If left unspecified, then members of 'identities' field will be
        allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources"]]]:
        '''sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#sources GoogleAccessContextManagerServicePerimeter#sources}
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSources")
    def put_sources(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference.put_sources)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSources", [value]))

    @jsii.member(jsii_name="resetIdentities")
    def reset_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentities", []))

    @jsii.member(jsii_name="resetIdentityType")
    def reset_identity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityType", []))

    @jsii.member(jsii_name="resetSources")
    def reset_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSources", []))

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList":
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList", jsii.get(self, "sources"))

    @builtins.property
    @jsii.member(jsii_name="identitiesInput")
    def identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="identityTypeInput")
    def identity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources"]]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="identities")
    def identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identities"))

    @identities.setter
    def identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference, "identities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identities", value)

    @builtins.property
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference, "identity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources",
    jsii_struct_bases=[],
    name_mapping={"access_level": "accessLevel", "resource": "resource"},
)
class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources:
    def __init__(
        self,
        *,
        access_level: typing.Optional[builtins.str] = None,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_level: An 'AccessLevel' resource name that allow resources within the 'ServicePerimeters' to be accessed from the internet. 'AccessLevels' listed must be in the same policy as this 'ServicePerimeter'. Referencing a nonexistent 'AccessLevel' will cause an error. If no 'AccessLevel' names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example 'accessPolicies/MY_POLICY/accessLevels/MY_LEVEL.' If * is specified, then all IngressSources will be allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_level GoogleAccessContextManagerServicePerimeter#access_level}
        :param resource: A Google Cloud resource that is allowed to ingress the perimeter. Requests from these resources will be allowed to access perimeter data. Currently only projects are allowed. Format 'projects/{project_number}' The project may be in any Google Cloud organization, not just the organization that the perimeter is defined in. '*' is not allowed, the case of allowing all Google Cloud resources only is not supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resource GoogleAccessContextManagerServicePerimeter#resource}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources.__init__)
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_level is not None:
            self._values["access_level"] = access_level
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def access_level(self) -> typing.Optional[builtins.str]:
        '''An 'AccessLevel' resource name that allow resources within the  'ServicePerimeters' to be accessed from the internet.

        'AccessLevels' listed
        must be in the same policy as this 'ServicePerimeter'. Referencing a nonexistent
        'AccessLevel' will cause an error. If no 'AccessLevel' names are listed,
        resources within the perimeter can only be accessed via Google Cloud calls
        with request origins within the perimeter.
        Example 'accessPolicies/MY_POLICY/accessLevels/MY_LEVEL.'
        If * is specified, then all IngressSources will be allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_level GoogleAccessContextManagerServicePerimeter#access_level}
        '''
        result = self._values.get("access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''A Google Cloud resource that is allowed to ingress the perimeter.

        Requests from these resources will be allowed to access perimeter data.
        Currently only projects are allowed. Format 'projects/{project_number}'
        The project may be in any Google Cloud organization, not just the
        organization that the perimeter is defined in. '*' is not allowed, the case
        of allowing all Google Cloud resources only is not supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resource GoogleAccessContextManagerServicePerimeter#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccessLevel")
    def reset_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevel", []))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="accessLevelInput")
    def access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference, "access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo",
    jsii_struct_bases=[],
    name_mapping={"operations": "operations", "resources": "resources"},
)
class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo:
    def __init__(
        self,
        *,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', protected by this 'ServicePerimeter' that are allowed to be accessed by sources defined in the corresponding 'IngressFrom'. A request matches if it contains a resource in this list. If '*' is specified for resources, then this 'IngressTo' rule will authorize access to all resources inside the perimeter, provided that the request also matches the 'operations' field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo.__init__)
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if operations is not None:
            self._values["operations"] = operations
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def operations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations"]]]:
        '''operations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        '''
        result = self._values.get("operations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations"]]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of resources, currently only projects in the form  'projects/', protected by this 'ServicePerimeter' that are allowed to be accessed by sources defined in the corresponding 'IngressFrom'.

        A request matches if it contains
        a resource in this list. If '*' is specified for resources,
        then this 'IngressTo' rule will authorize access to all
        resources inside the perimeter, provided that the request
        also matches the 'operations' field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations",
    jsii_struct_bases=[],
    name_mapping={
        "method_selectors": "methodSelectors",
        "service_name": "serviceName",
    },
)
class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations:
    def __init__(
        self,
        *,
        method_selectors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors", typing.Dict[str, typing.Any]]]]] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method_selectors: method_selectors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        :param service_name: The name of the API whose methods or permissions the 'IngressPolicy' or 'EgressPolicy' want to allow. A single 'ApiOperation' with 'serviceName' field set to '*' will allow all methods AND permissions for all services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations.__init__)
            check_type(argname="argument method_selectors", value=method_selectors, expected_type=type_hints["method_selectors"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method_selectors is not None:
            self._values["method_selectors"] = method_selectors
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def method_selectors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors"]]]:
        '''method_selectors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        '''
        result = self._values.get("method_selectors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors"]]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''The name of the API whose methods or permissions the 'IngressPolicy' or  'EgressPolicy' want to allow.

        A single 'ApiOperation' with 'serviceName'
        field set to '*' will allow all methods AND permissions for all services.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "permission": "permission"},
)
class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors:
    def __init__(
        self,
        *,
        method: typing.Optional[builtins.str] = None,
        permission: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Value for method should be a valid method name for the corresponding serviceName in 'ApiOperation'. If '*' used as value for 'method', then ALL methods and permissions are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        :param permission: Value for permission should be a valid Cloud IAM permission for the corresponding 'serviceName' in 'ApiOperation'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if permission is not None:
            self._values["permission"] = permission

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Value for method should be a valid method name for the corresponding  serviceName in 'ApiOperation'.

        If '*' used as value for 'method', then
        ALL methods and permissions are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permission(self) -> typing.Optional[builtins.str]:
        '''Value for permission should be a valid Cloud IAM permission for the  corresponding 'serviceName' in 'ApiOperation'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        result = self._values.get("permission")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetPermission")
    def reset_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermission", []))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference, "permission").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMethodSelectors")
    def put_method_selectors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference.put_method_selectors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMethodSelectors", [value]))

    @jsii.member(jsii_name="resetMethodSelectors")
    def reset_method_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethodSelectors", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="methodSelectors")
    def method_selectors(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList, jsii.get(self, "methodSelectors"))

    @builtins.property
    @jsii.member(jsii_name="methodSelectorsInput")
    def method_selectors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors]]], jsii.get(self, "methodSelectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOperations")
    def put_operations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference.put_operations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOperations", [value]))

    @jsii.member(jsii_name="resetOperations")
    def reset_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperations", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList, jsii.get(self, "operations"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations]]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIngressFrom")
    def put_ingress_from(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        :param sources: sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#sources GoogleAccessContextManagerServicePerimeter#sources}
        '''
        value = GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom(
            identities=identities, identity_type=identity_type, sources=sources
        )

        return typing.cast(None, jsii.invoke(self, "putIngressFrom", [value]))

    @jsii.member(jsii_name="putIngressTo")
    def put_ingress_to(
        self,
        *,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations, typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', protected by this 'ServicePerimeter' that are allowed to be accessed by sources defined in the corresponding 'IngressFrom'. A request matches if it contains a resource in this list. If '*' is specified for resources, then this 'IngressTo' rule will authorize access to all resources inside the perimeter, provided that the request also matches the 'operations' field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        value = GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo(
            operations=operations, resources=resources
        )

        return typing.cast(None, jsii.invoke(self, "putIngressTo", [value]))

    @jsii.member(jsii_name="resetIngressFrom")
    def reset_ingress_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressFrom", []))

    @jsii.member(jsii_name="resetIngressTo")
    def reset_ingress_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressTo", []))

    @builtins.property
    @jsii.member(jsii_name="ingressFrom")
    def ingress_from(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference, jsii.get(self, "ingressFrom"))

    @builtins.property
    @jsii.member(jsii_name="ingressTo")
    def ingress_to(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference, jsii.get(self, "ingressTo"))

    @builtins.property
    @jsii.member(jsii_name="ingressFromInput")
    def ingress_from_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom], jsii.get(self, "ingressFromInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressToInput")
    def ingress_to_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo], jsii.get(self, "ingressToInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEgressPolicies")
    def put_egress_policies(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecOutputReference.put_egress_policies)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEgressPolicies", [value]))

    @jsii.member(jsii_name="putIngressPolicies")
    def put_ingress_policies(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecOutputReference.put_ingress_policies)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIngressPolicies", [value]))

    @jsii.member(jsii_name="putVpcAccessibleServices")
    def put_vpc_accessible_services(
        self,
        *,
        allowed_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_services: The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#allowed_services GoogleAccessContextManagerServicePerimeter#allowed_services}
        :param enable_restriction: Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#enable_restriction GoogleAccessContextManagerServicePerimeter#enable_restriction}
        '''
        value = GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices(
            allowed_services=allowed_services, enable_restriction=enable_restriction
        )

        return typing.cast(None, jsii.invoke(self, "putVpcAccessibleServices", [value]))

    @jsii.member(jsii_name="resetAccessLevels")
    def reset_access_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevels", []))

    @jsii.member(jsii_name="resetEgressPolicies")
    def reset_egress_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressPolicies", []))

    @jsii.member(jsii_name="resetIngressPolicies")
    def reset_ingress_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressPolicies", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @jsii.member(jsii_name="resetRestrictedServices")
    def reset_restricted_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictedServices", []))

    @jsii.member(jsii_name="resetVpcAccessibleServices")
    def reset_vpc_accessible_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcAccessibleServices", []))

    @builtins.property
    @jsii.member(jsii_name="egressPolicies")
    def egress_policies(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList, jsii.get(self, "egressPolicies"))

    @builtins.property
    @jsii.member(jsii_name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList, jsii.get(self, "ingressPolicies"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> "GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference":
        return typing.cast("GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference", jsii.get(self, "vpcAccessibleServices"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelsInput")
    def access_levels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="egressPoliciesInput")
    def egress_policies_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecEgressPolicies]]], jsii.get(self, "egressPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressPoliciesInput")
    def ingress_policies_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterSpecIngressPolicies]]], jsii.get(self, "ingressPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictedServicesInput")
    def restricted_services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restrictedServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessibleServicesInput")
    def vpc_accessible_services_input(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices"]:
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices"], jsii.get(self, "vpcAccessibleServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevels")
    def access_levels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessLevels"))

    @access_levels.setter
    def access_levels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecOutputReference, "access_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevels", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="restrictedServices")
    def restricted_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restrictedServices"))

    @restricted_services.setter
    def restricted_services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecOutputReference, "restricted_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictedServices", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpec]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_services": "allowedServices",
        "enable_restriction": "enableRestriction",
    },
)
class GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices:
    def __init__(
        self,
        *,
        allowed_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_services: The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#allowed_services GoogleAccessContextManagerServicePerimeter#allowed_services}
        :param enable_restriction: Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#enable_restriction GoogleAccessContextManagerServicePerimeter#enable_restriction}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices.__init__)
            check_type(argname="argument allowed_services", value=allowed_services, expected_type=type_hints["allowed_services"])
            check_type(argname="argument enable_restriction", value=enable_restriction, expected_type=type_hints["enable_restriction"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_services is not None:
            self._values["allowed_services"] = allowed_services
        if enable_restriction is not None:
            self._values["enable_restriction"] = enable_restriction

    @builtins.property
    def allowed_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#allowed_services GoogleAccessContextManagerServicePerimeter#allowed_services}
        '''
        result = self._values.get("allowed_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#enable_restriction GoogleAccessContextManagerServicePerimeter#enable_restriction}
        '''
        result = self._values.get("enable_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedServices")
    def reset_allowed_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedServices", []))

    @jsii.member(jsii_name="resetEnableRestriction")
    def reset_enable_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRestriction", []))

    @builtins.property
    @jsii.member(jsii_name="allowedServicesInput")
    def allowed_services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRestrictionInput")
    def enable_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedServices")
    def allowed_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedServices"))

    @allowed_services.setter
    def allowed_services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference, "allowed_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedServices", value)

    @builtins.property
    @jsii.member(jsii_name="enableRestriction")
    def enable_restriction(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableRestriction"))

    @enable_restriction.setter
    def enable_restriction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference, "enable_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatus",
    jsii_struct_bases=[],
    name_mapping={
        "access_levels": "accessLevels",
        "egress_policies": "egressPolicies",
        "ingress_policies": "ingressPolicies",
        "resources": "resources",
        "restricted_services": "restrictedServices",
        "vpc_accessible_services": "vpcAccessibleServices",
    },
)
class GoogleAccessContextManagerServicePerimeterStatus:
    def __init__(
        self,
        *,
        access_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
        egress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusEgressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        ingress_policies: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPolicies", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        restricted_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpc_accessible_services: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_levels: A list of AccessLevel resource names that allow resources within the ServicePerimeter to be accessed from the internet. AccessLevels listed must be in the same policy as this ServicePerimeter. Referencing a nonexistent AccessLevel is a syntax error. If no AccessLevel names are listed, resources within the perimeter can only be accessed via GCP calls with request origins within the perimeter. For Service Perimeter Bridge, must be empty. Format: accessPolicies/{policy_id}/accessLevels/{access_level_name} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_levels GoogleAccessContextManagerServicePerimeter#access_levels}
        :param egress_policies: egress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_policies GoogleAccessContextManagerServicePerimeter#egress_policies}
        :param ingress_policies: ingress_policies block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_policies GoogleAccessContextManagerServicePerimeter#ingress_policies}
        :param resources: A list of GCP resources that are inside of the service perimeter. Currently only projects are allowed. Format: projects/{project_number}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        :param restricted_services: GCP services that are subject to the Service Perimeter restrictions. Must contain a list of services. For example, if 'storage.googleapis.com' is specified, access to the storage buckets inside the perimeter must meet the perimeter's access restrictions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#restricted_services GoogleAccessContextManagerServicePerimeter#restricted_services}
        :param vpc_accessible_services: vpc_accessible_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#vpc_accessible_services GoogleAccessContextManagerServicePerimeter#vpc_accessible_services}
        '''
        if isinstance(vpc_accessible_services, dict):
            vpc_accessible_services = GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices(**vpc_accessible_services)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatus.__init__)
            check_type(argname="argument access_levels", value=access_levels, expected_type=type_hints["access_levels"])
            check_type(argname="argument egress_policies", value=egress_policies, expected_type=type_hints["egress_policies"])
            check_type(argname="argument ingress_policies", value=ingress_policies, expected_type=type_hints["ingress_policies"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument restricted_services", value=restricted_services, expected_type=type_hints["restricted_services"])
            check_type(argname="argument vpc_accessible_services", value=vpc_accessible_services, expected_type=type_hints["vpc_accessible_services"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_levels is not None:
            self._values["access_levels"] = access_levels
        if egress_policies is not None:
            self._values["egress_policies"] = egress_policies
        if ingress_policies is not None:
            self._values["ingress_policies"] = ingress_policies
        if resources is not None:
            self._values["resources"] = resources
        if restricted_services is not None:
            self._values["restricted_services"] = restricted_services
        if vpc_accessible_services is not None:
            self._values["vpc_accessible_services"] = vpc_accessible_services

    @builtins.property
    def access_levels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of AccessLevel resource names that allow resources within the ServicePerimeter to be accessed from the internet.

        AccessLevels listed must be in the same policy as this
        ServicePerimeter. Referencing a nonexistent AccessLevel is a
        syntax error. If no AccessLevel names are listed, resources within
        the perimeter can only be accessed via GCP calls with request
        origins within the perimeter. For Service Perimeter Bridge, must
        be empty.

        Format: accessPolicies/{policy_id}/accessLevels/{access_level_name}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_levels GoogleAccessContextManagerServicePerimeter#access_levels}
        '''
        result = self._values.get("access_levels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def egress_policies(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusEgressPolicies"]]]:
        '''egress_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_policies GoogleAccessContextManagerServicePerimeter#egress_policies}
        '''
        result = self._values.get("egress_policies")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusEgressPolicies"]]], result)

    @builtins.property
    def ingress_policies(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPolicies"]]]:
        '''ingress_policies block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_policies GoogleAccessContextManagerServicePerimeter#ingress_policies}
        '''
        result = self._values.get("ingress_policies")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPolicies"]]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of GCP resources that are inside of the service perimeter. Currently only projects are allowed. Format: projects/{project_number}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def restricted_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''GCP services that are subject to the Service Perimeter restrictions.

        Must contain a list of services. For example, if
        'storage.googleapis.com' is specified, access to the storage
        buckets inside the perimeter must meet the perimeter's access
        restrictions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#restricted_services GoogleAccessContextManagerServicePerimeter#restricted_services}
        '''
        result = self._values.get("restricted_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpc_accessible_services(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices"]:
        '''vpc_accessible_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#vpc_accessible_services GoogleAccessContextManagerServicePerimeter#vpc_accessible_services}
        '''
        result = self._values.get("vpc_accessible_services")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPolicies",
    jsii_struct_bases=[],
    name_mapping={"egress_from": "egressFrom", "egress_to": "egressTo"},
)
class GoogleAccessContextManagerServicePerimeterStatusEgressPolicies:
    def __init__(
        self,
        *,
        egress_from: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom", typing.Dict[str, typing.Any]]] = None,
        egress_to: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param egress_from: egress_from block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_from GoogleAccessContextManagerServicePerimeter#egress_from}
        :param egress_to: egress_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_to GoogleAccessContextManagerServicePerimeter#egress_to}
        '''
        if isinstance(egress_from, dict):
            egress_from = GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom(**egress_from)
        if isinstance(egress_to, dict):
            egress_to = GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo(**egress_to)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPolicies.__init__)
            check_type(argname="argument egress_from", value=egress_from, expected_type=type_hints["egress_from"])
            check_type(argname="argument egress_to", value=egress_to, expected_type=type_hints["egress_to"])
        self._values: typing.Dict[str, typing.Any] = {}
        if egress_from is not None:
            self._values["egress_from"] = egress_from
        if egress_to is not None:
            self._values["egress_to"] = egress_to

    @builtins.property
    def egress_from(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom"]:
        '''egress_from block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_from GoogleAccessContextManagerServicePerimeter#egress_from}
        '''
        result = self._values.get("egress_from")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom"], result)

    @builtins.property
    def egress_to(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo"]:
        '''egress_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#egress_to GoogleAccessContextManagerServicePerimeter#egress_to}
        '''
        result = self._values.get("egress_to")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusEgressPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom",
    jsii_struct_bases=[],
    name_mapping={"identities": "identities", "identity_type": "identityType"},
)
class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom:
    def __init__(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this 'EgressPolicy'. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom.__init__)
            check_type(argname="argument identities", value=identities, expected_type=type_hints["identities"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identities is not None:
            self._values["identities"] = identities
        if identity_type is not None:
            self._values["identity_type"] = identity_type

    @builtins.property
    def identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identities that are allowed access through this 'EgressPolicy'.

        Should be in the format of email address. The email address should
        represent individual user or service account only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        '''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of identities that are allowed access to outside the  perimeter.

        If left unspecified, then members of 'identities' field will
        be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentities")
    def reset_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentities", []))

    @jsii.member(jsii_name="resetIdentityType")
    def reset_identity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityType", []))

    @builtins.property
    @jsii.member(jsii_name="identitiesInput")
    def identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="identityTypeInput")
    def identity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="identities")
    def identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identities"))

    @identities.setter
    def identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference, "identities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identities", value)

    @builtins.property
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference, "identity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo",
    jsii_struct_bases=[],
    name_mapping={
        "external_resources": "externalResources",
        "operations": "operations",
        "resources": "resources",
    },
)
class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo:
    def __init__(
        self,
        *,
        external_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param external_resources: A list of external resources that are allowed to be accessed. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#external_resources GoogleAccessContextManagerServicePerimeter#external_resources}
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', that match this to stanza. A request matches if it contains a resource in this list. If * is specified for resources, then this 'EgressTo' rule will authorize access to all resources outside the perimeter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo.__init__)
            check_type(argname="argument external_resources", value=external_resources, expected_type=type_hints["external_resources"])
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if external_resources is not None:
            self._values["external_resources"] = external_resources
        if operations is not None:
            self._values["operations"] = operations
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def external_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of external resources that are allowed to be accessed.

        A request
        matches if it contains an external resource in this list (Example:
        s3://bucket/path). Currently '*' is not allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#external_resources GoogleAccessContextManagerServicePerimeter#external_resources}
        '''
        result = self._values.get("external_resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def operations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations"]]]:
        '''operations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        '''
        result = self._values.get("operations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations"]]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of resources, currently only projects in the form  'projects/', that match this to stanza.

        A request matches
        if it contains a resource in this list. If * is specified for resources,
        then this 'EgressTo' rule will authorize access to all resources outside
        the perimeter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations",
    jsii_struct_bases=[],
    name_mapping={
        "method_selectors": "methodSelectors",
        "service_name": "serviceName",
    },
)
class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations:
    def __init__(
        self,
        *,
        method_selectors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors", typing.Dict[str, typing.Any]]]]] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method_selectors: method_selectors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        :param service_name: The name of the API whose methods or permissions the 'IngressPolicy' or 'EgressPolicy' want to allow. A single 'ApiOperation' with serviceName field set to '*' will allow all methods AND permissions for all services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations.__init__)
            check_type(argname="argument method_selectors", value=method_selectors, expected_type=type_hints["method_selectors"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method_selectors is not None:
            self._values["method_selectors"] = method_selectors
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def method_selectors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors"]]]:
        '''method_selectors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        '''
        result = self._values.get("method_selectors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors"]]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''The name of the API whose methods or permissions the 'IngressPolicy' or  'EgressPolicy' want to allow.

        A single 'ApiOperation' with serviceName
        field set to '*' will allow all methods AND permissions for all services.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "permission": "permission"},
)
class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors:
    def __init__(
        self,
        *,
        method: typing.Optional[builtins.str] = None,
        permission: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Value for 'method' should be a valid method name for the corresponding 'serviceName' in 'ApiOperation'. If '*' used as value for method, then ALL methods and permissions are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        :param permission: Value for permission should be a valid Cloud IAM permission for the corresponding 'serviceName' in 'ApiOperation'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if permission is not None:
            self._values["permission"] = permission

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Value for 'method' should be a valid method name for the corresponding  'serviceName' in 'ApiOperation'.

        If '*' used as value for method,
        then ALL methods and permissions are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permission(self) -> typing.Optional[builtins.str]:
        '''Value for permission should be a valid Cloud IAM permission for the  corresponding 'serviceName' in 'ApiOperation'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        result = self._values.get("permission")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetPermission")
    def reset_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermission", []))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference, "permission").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMethodSelectors")
    def put_method_selectors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference.put_method_selectors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMethodSelectors", [value]))

    @jsii.member(jsii_name="resetMethodSelectors")
    def reset_method_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethodSelectors", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="methodSelectors")
    def method_selectors(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList, jsii.get(self, "methodSelectors"))

    @builtins.property
    @jsii.member(jsii_name="methodSelectorsInput")
    def method_selectors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors]]], jsii.get(self, "methodSelectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOperations")
    def put_operations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference.put_operations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOperations", [value]))

    @jsii.member(jsii_name="resetExternalResources")
    def reset_external_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalResources", []))

    @jsii.member(jsii_name="resetOperations")
    def reset_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperations", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList, jsii.get(self, "operations"))

    @builtins.property
    @jsii.member(jsii_name="externalResourcesInput")
    def external_resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations]]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="externalResources")
    def external_resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "externalResources"))

    @external_resources.setter
    def external_resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference, "external_resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalResources", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEgressFrom")
    def put_egress_from(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this 'EgressPolicy'. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access to outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        value = GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom(
            identities=identities, identity_type=identity_type
        )

        return typing.cast(None, jsii.invoke(self, "putEgressFrom", [value]))

    @jsii.member(jsii_name="putEgressTo")
    def put_egress_to(
        self,
        *,
        external_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations, typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param external_resources: A list of external resources that are allowed to be accessed. A request matches if it contains an external resource in this list (Example: s3://bucket/path). Currently '*' is not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#external_resources GoogleAccessContextManagerServicePerimeter#external_resources}
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', that match this to stanza. A request matches if it contains a resource in this list. If * is specified for resources, then this 'EgressTo' rule will authorize access to all resources outside the perimeter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        value = GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo(
            external_resources=external_resources,
            operations=operations,
            resources=resources,
        )

        return typing.cast(None, jsii.invoke(self, "putEgressTo", [value]))

    @jsii.member(jsii_name="resetEgressFrom")
    def reset_egress_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressFrom", []))

    @jsii.member(jsii_name="resetEgressTo")
    def reset_egress_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressTo", []))

    @builtins.property
    @jsii.member(jsii_name="egressFrom")
    def egress_from(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference, jsii.get(self, "egressFrom"))

    @builtins.property
    @jsii.member(jsii_name="egressTo")
    def egress_to(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference, jsii.get(self, "egressTo"))

    @builtins.property
    @jsii.member(jsii_name="egressFromInput")
    def egress_from_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom], jsii.get(self, "egressFromInput"))

    @builtins.property
    @jsii.member(jsii_name="egressToInput")
    def egress_to_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo], jsii.get(self, "egressToInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPolicies",
    jsii_struct_bases=[],
    name_mapping={"ingress_from": "ingressFrom", "ingress_to": "ingressTo"},
)
class GoogleAccessContextManagerServicePerimeterStatusIngressPolicies:
    def __init__(
        self,
        *,
        ingress_from: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom", typing.Dict[str, typing.Any]]] = None,
        ingress_to: typing.Optional[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ingress_from: ingress_from block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_from GoogleAccessContextManagerServicePerimeter#ingress_from}
        :param ingress_to: ingress_to block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_to GoogleAccessContextManagerServicePerimeter#ingress_to}
        '''
        if isinstance(ingress_from, dict):
            ingress_from = GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom(**ingress_from)
        if isinstance(ingress_to, dict):
            ingress_to = GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo(**ingress_to)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPolicies.__init__)
            check_type(argname="argument ingress_from", value=ingress_from, expected_type=type_hints["ingress_from"])
            check_type(argname="argument ingress_to", value=ingress_to, expected_type=type_hints["ingress_to"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ingress_from is not None:
            self._values["ingress_from"] = ingress_from
        if ingress_to is not None:
            self._values["ingress_to"] = ingress_to

    @builtins.property
    def ingress_from(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom"]:
        '''ingress_from block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_from GoogleAccessContextManagerServicePerimeter#ingress_from}
        '''
        result = self._values.get("ingress_from")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom"], result)

    @builtins.property
    def ingress_to(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo"]:
        '''ingress_to block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#ingress_to GoogleAccessContextManagerServicePerimeter#ingress_to}
        '''
        result = self._values.get("ingress_to")
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusIngressPolicies(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom",
    jsii_struct_bases=[],
    name_mapping={
        "identities": "identities",
        "identity_type": "identityType",
        "sources": "sources",
    },
)
class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom:
    def __init__(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        :param sources: sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#sources GoogleAccessContextManagerServicePerimeter#sources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom.__init__)
            check_type(argname="argument identities", value=identities, expected_type=type_hints["identities"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if identities is not None:
            self._values["identities"] = identities
        if identity_type is not None:
            self._values["identity_type"] = identity_type
        if sources is not None:
            self._values["sources"] = sources

    @builtins.property
    def identities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identities that are allowed access through this ingress policy.

        Should be in the format of email address. The email address should represent
        individual user or service account only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        '''
        result = self._values.get("identities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of identities that are allowed access from outside the  perimeter.

        If left unspecified, then members of 'identities' field will be
        allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources"]]]:
        '''sources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#sources GoogleAccessContextManagerServicePerimeter#sources}
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSources")
    def put_sources(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference.put_sources)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSources", [value]))

    @jsii.member(jsii_name="resetIdentities")
    def reset_identities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentities", []))

    @jsii.member(jsii_name="resetIdentityType")
    def reset_identity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityType", []))

    @jsii.member(jsii_name="resetSources")
    def reset_sources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSources", []))

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList":
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList", jsii.get(self, "sources"))

    @builtins.property
    @jsii.member(jsii_name="identitiesInput")
    def identities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="identityTypeInput")
    def identity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcesInput")
    def sources_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources"]]], jsii.get(self, "sourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="identities")
    def identities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identities"))

    @identities.setter
    def identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference, "identities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identities", value)

    @builtins.property
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference, "identity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources",
    jsii_struct_bases=[],
    name_mapping={"access_level": "accessLevel", "resource": "resource"},
)
class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources:
    def __init__(
        self,
        *,
        access_level: typing.Optional[builtins.str] = None,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_level: An 'AccessLevel' resource name that allow resources within the 'ServicePerimeters' to be accessed from the internet. 'AccessLevels' listed must be in the same policy as this 'ServicePerimeter'. Referencing a nonexistent 'AccessLevel' will cause an error. If no 'AccessLevel' names are listed, resources within the perimeter can only be accessed via Google Cloud calls with request origins within the perimeter. Example 'accessPolicies/MY_POLICY/accessLevels/MY_LEVEL.' If * is specified, then all IngressSources will be allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_level GoogleAccessContextManagerServicePerimeter#access_level}
        :param resource: A Google Cloud resource that is allowed to ingress the perimeter. Requests from these resources will be allowed to access perimeter data. Currently only projects are allowed. Format 'projects/{project_number}' The project may be in any Google Cloud organization, not just the organization that the perimeter is defined in. '*' is not allowed, the case of allowing all Google Cloud resources only is not supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resource GoogleAccessContextManagerServicePerimeter#resource}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources.__init__)
            check_type(argname="argument access_level", value=access_level, expected_type=type_hints["access_level"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {}
        if access_level is not None:
            self._values["access_level"] = access_level
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def access_level(self) -> typing.Optional[builtins.str]:
        '''An 'AccessLevel' resource name that allow resources within the  'ServicePerimeters' to be accessed from the internet.

        'AccessLevels' listed
        must be in the same policy as this 'ServicePerimeter'. Referencing a nonexistent
        'AccessLevel' will cause an error. If no 'AccessLevel' names are listed,
        resources within the perimeter can only be accessed via Google Cloud calls
        with request origins within the perimeter.
        Example 'accessPolicies/MY_POLICY/accessLevels/MY_LEVEL.'
        If * is specified, then all IngressSources will be allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#access_level GoogleAccessContextManagerServicePerimeter#access_level}
        '''
        result = self._values.get("access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''A Google Cloud resource that is allowed to ingress the perimeter.

        Requests from these resources will be allowed to access perimeter data.
        Currently only projects are allowed. Format 'projects/{project_number}'
        The project may be in any Google Cloud organization, not just the
        organization that the perimeter is defined in. '*' is not allowed, the case
        of allowing all Google Cloud resources only is not supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resource GoogleAccessContextManagerServicePerimeter#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccessLevel")
    def reset_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevel", []))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="accessLevelInput")
    def access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @access_level.setter
    def access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference, "access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo",
    jsii_struct_bases=[],
    name_mapping={"operations": "operations", "resources": "resources"},
)
class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo:
    def __init__(
        self,
        *,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations", typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', protected by this 'ServicePerimeter' that are allowed to be accessed by sources defined in the corresponding 'IngressFrom'. A request matches if it contains a resource in this list. If '*' is specified for resources, then this 'IngressTo' rule will authorize access to all resources inside the perimeter, provided that the request also matches the 'operations' field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo.__init__)
            check_type(argname="argument operations", value=operations, expected_type=type_hints["operations"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
        self._values: typing.Dict[str, typing.Any] = {}
        if operations is not None:
            self._values["operations"] = operations
        if resources is not None:
            self._values["resources"] = resources

    @builtins.property
    def operations(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations"]]]:
        '''operations block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        '''
        result = self._values.get("operations")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations"]]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of resources, currently only projects in the form  'projects/', protected by this 'ServicePerimeter' that are allowed to be accessed by sources defined in the corresponding 'IngressFrom'.

        A request matches if it contains
        a resource in this list. If '*' is specified for resources,
        then this 'IngressTo' rule will authorize access to all
        resources inside the perimeter, provided that the request
        also matches the 'operations' field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations",
    jsii_struct_bases=[],
    name_mapping={
        "method_selectors": "methodSelectors",
        "service_name": "serviceName",
    },
)
class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations:
    def __init__(
        self,
        *,
        method_selectors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors", typing.Dict[str, typing.Any]]]]] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method_selectors: method_selectors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        :param service_name: The name of the API whose methods or permissions the 'IngressPolicy' or 'EgressPolicy' want to allow. A single 'ApiOperation' with 'serviceName' field set to '*' will allow all methods AND permissions for all services. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations.__init__)
            check_type(argname="argument method_selectors", value=method_selectors, expected_type=type_hints["method_selectors"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method_selectors is not None:
            self._values["method_selectors"] = method_selectors
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def method_selectors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors"]]]:
        '''method_selectors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method_selectors GoogleAccessContextManagerServicePerimeter#method_selectors}
        '''
        result = self._values.get("method_selectors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors"]]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''The name of the API whose methods or permissions the 'IngressPolicy' or  'EgressPolicy' want to allow.

        A single 'ApiOperation' with 'serviceName'
        field set to '*' will allow all methods AND permissions for all services.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#service_name GoogleAccessContextManagerServicePerimeter#service_name}
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "permission": "permission"},
)
class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors:
    def __init__(
        self,
        *,
        method: typing.Optional[builtins.str] = None,
        permission: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Value for method should be a valid method name for the corresponding serviceName in 'ApiOperation'. If '*' used as value for 'method', then ALL methods and permissions are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        :param permission: Value for permission should be a valid Cloud IAM permission for the corresponding 'serviceName' in 'ApiOperation'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
        self._values: typing.Dict[str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if permission is not None:
            self._values["permission"] = permission

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Value for method should be a valid method name for the corresponding  serviceName in 'ApiOperation'.

        If '*' used as value for 'method', then
        ALL methods and permissions are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#method GoogleAccessContextManagerServicePerimeter#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permission(self) -> typing.Optional[builtins.str]:
        '''Value for permission should be a valid Cloud IAM permission for the  corresponding 'serviceName' in 'ApiOperation'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#permission GoogleAccessContextManagerServicePerimeter#permission}
        '''
        result = self._values.get("permission")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetPermission")
    def reset_permission(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermission", []))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference, "permission").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMethodSelectors")
    def put_method_selectors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference.put_method_selectors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMethodSelectors", [value]))

    @jsii.member(jsii_name="resetMethodSelectors")
    def reset_method_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethodSelectors", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="methodSelectors")
    def method_selectors(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList, jsii.get(self, "methodSelectors"))

    @builtins.property
    @jsii.member(jsii_name="methodSelectorsInput")
    def method_selectors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors]]], jsii.get(self, "methodSelectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference, "service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOperations")
    def put_operations(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference.put_operations)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOperations", [value]))

    @jsii.member(jsii_name="resetOperations")
    def reset_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperations", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @builtins.property
    @jsii.member(jsii_name="operations")
    def operations(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList, jsii.get(self, "operations"))

    @builtins.property
    @jsii.member(jsii_name="operationsInput")
    def operations_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations]]], jsii.get(self, "operationsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIngressFrom")
    def put_ingress_from(
        self,
        *,
        identities: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_type: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param identities: A list of identities that are allowed access through this ingress policy. Should be in the format of email address. The email address should represent individual user or service account only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identities GoogleAccessContextManagerServicePerimeter#identities}
        :param identity_type: Specifies the type of identities that are allowed access from outside the perimeter. If left unspecified, then members of 'identities' field will be allowed access. Possible values: ["IDENTITY_TYPE_UNSPECIFIED", "ANY_IDENTITY", "ANY_USER_ACCOUNT", "ANY_SERVICE_ACCOUNT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#identity_type GoogleAccessContextManagerServicePerimeter#identity_type}
        :param sources: sources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#sources GoogleAccessContextManagerServicePerimeter#sources}
        '''
        value = GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom(
            identities=identities, identity_type=identity_type, sources=sources
        )

        return typing.cast(None, jsii.invoke(self, "putIngressFrom", [value]))

    @jsii.member(jsii_name="putIngressTo")
    def put_ingress_to(
        self,
        *,
        operations: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations, typing.Dict[str, typing.Any]]]]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operations: operations block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#operations GoogleAccessContextManagerServicePerimeter#operations}
        :param resources: A list of resources, currently only projects in the form 'projects/', protected by this 'ServicePerimeter' that are allowed to be accessed by sources defined in the corresponding 'IngressFrom'. A request matches if it contains a resource in this list. If '*' is specified for resources, then this 'IngressTo' rule will authorize access to all resources inside the perimeter, provided that the request also matches the 'operations' field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#resources GoogleAccessContextManagerServicePerimeter#resources}
        '''
        value = GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo(
            operations=operations, resources=resources
        )

        return typing.cast(None, jsii.invoke(self, "putIngressTo", [value]))

    @jsii.member(jsii_name="resetIngressFrom")
    def reset_ingress_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressFrom", []))

    @jsii.member(jsii_name="resetIngressTo")
    def reset_ingress_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressTo", []))

    @builtins.property
    @jsii.member(jsii_name="ingressFrom")
    def ingress_from(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference, jsii.get(self, "ingressFrom"))

    @builtins.property
    @jsii.member(jsii_name="ingressTo")
    def ingress_to(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference, jsii.get(self, "ingressTo"))

    @builtins.property
    @jsii.member(jsii_name="ingressFromInput")
    def ingress_from_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom], jsii.get(self, "ingressFromInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressToInput")
    def ingress_to_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo], jsii.get(self, "ingressToInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerServicePerimeterStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEgressPolicies")
    def put_egress_policies(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusOutputReference.put_egress_policies)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEgressPolicies", [value]))

    @jsii.member(jsii_name="putIngressPolicies")
    def put_ingress_policies(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusOutputReference.put_ingress_policies)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIngressPolicies", [value]))

    @jsii.member(jsii_name="putVpcAccessibleServices")
    def put_vpc_accessible_services(
        self,
        *,
        allowed_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_services: The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#allowed_services GoogleAccessContextManagerServicePerimeter#allowed_services}
        :param enable_restriction: Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#enable_restriction GoogleAccessContextManagerServicePerimeter#enable_restriction}
        '''
        value = GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices(
            allowed_services=allowed_services, enable_restriction=enable_restriction
        )

        return typing.cast(None, jsii.invoke(self, "putVpcAccessibleServices", [value]))

    @jsii.member(jsii_name="resetAccessLevels")
    def reset_access_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevels", []))

    @jsii.member(jsii_name="resetEgressPolicies")
    def reset_egress_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressPolicies", []))

    @jsii.member(jsii_name="resetIngressPolicies")
    def reset_ingress_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressPolicies", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @jsii.member(jsii_name="resetRestrictedServices")
    def reset_restricted_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictedServices", []))

    @jsii.member(jsii_name="resetVpcAccessibleServices")
    def reset_vpc_accessible_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcAccessibleServices", []))

    @builtins.property
    @jsii.member(jsii_name="egressPolicies")
    def egress_policies(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList, jsii.get(self, "egressPolicies"))

    @builtins.property
    @jsii.member(jsii_name="ingressPolicies")
    def ingress_policies(
        self,
    ) -> GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList:
        return typing.cast(GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList, jsii.get(self, "ingressPolicies"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessibleServices")
    def vpc_accessible_services(
        self,
    ) -> "GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference":
        return typing.cast("GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference", jsii.get(self, "vpcAccessibleServices"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelsInput")
    def access_levels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="egressPoliciesInput")
    def egress_policies_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusEgressPolicies]]], jsii.get(self, "egressPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressPoliciesInput")
    def ingress_policies_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerServicePerimeterStatusIngressPolicies]]], jsii.get(self, "ingressPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictedServicesInput")
    def restricted_services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restrictedServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcAccessibleServicesInput")
    def vpc_accessible_services_input(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices"]:
        return typing.cast(typing.Optional["GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices"], jsii.get(self, "vpcAccessibleServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="accessLevels")
    def access_levels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessLevels"))

    @access_levels.setter
    def access_levels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusOutputReference, "access_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLevels", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="restrictedServices")
    def restricted_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restrictedServices"))

    @restricted_services.setter
    def restricted_services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusOutputReference, "restricted_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictedServices", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatus]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_services": "allowedServices",
        "enable_restriction": "enableRestriction",
    },
)
class GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices:
    def __init__(
        self,
        *,
        allowed_services: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_restriction: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_services: The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#allowed_services GoogleAccessContextManagerServicePerimeter#allowed_services}
        :param enable_restriction: Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#enable_restriction GoogleAccessContextManagerServicePerimeter#enable_restriction}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices.__init__)
            check_type(argname="argument allowed_services", value=allowed_services, expected_type=type_hints["allowed_services"])
            check_type(argname="argument enable_restriction", value=enable_restriction, expected_type=type_hints["enable_restriction"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_services is not None:
            self._values["allowed_services"] = allowed_services
        if enable_restriction is not None:
            self._values["enable_restriction"] = enable_restriction

    @builtins.property
    def allowed_services(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of APIs usable within the Service Perimeter. Must be empty unless 'enableRestriction' is True.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#allowed_services GoogleAccessContextManagerServicePerimeter#allowed_services}
        '''
        result = self._values.get("allowed_services")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_restriction(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to restrict API calls within the Service Perimeter to the list of APIs specified in 'allowedServices'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#enable_restriction GoogleAccessContextManagerServicePerimeter#enable_restriction}
        '''
        result = self._values.get("enable_restriction")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedServices")
    def reset_allowed_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedServices", []))

    @jsii.member(jsii_name="resetEnableRestriction")
    def reset_enable_restriction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRestriction", []))

    @builtins.property
    @jsii.member(jsii_name="allowedServicesInput")
    def allowed_services_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRestrictionInput")
    def enable_restriction_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableRestrictionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedServices")
    def allowed_services(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedServices"))

    @allowed_services.setter
    def allowed_services(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference, "allowed_services").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedServices", value)

    @builtins.property
    @jsii.member(jsii_name="enableRestriction")
    def enable_restriction(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableRestriction"))

    @enable_restriction.setter
    def enable_restriction(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference, "enable_restriction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRestriction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleAccessContextManagerServicePerimeterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#create GoogleAccessContextManagerServicePerimeter#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#delete GoogleAccessContextManagerServicePerimeter#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#update GoogleAccessContextManagerServicePerimeter#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#create GoogleAccessContextManagerServicePerimeter#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#delete GoogleAccessContextManagerServicePerimeter#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_service_perimeter#update GoogleAccessContextManagerServicePerimeter#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerServicePerimeterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerServicePerimeter.GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerServicePerimeterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAccessContextManagerServicePerimeter",
    "GoogleAccessContextManagerServicePerimeterConfig",
    "GoogleAccessContextManagerServicePerimeterSpec",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPolicies",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFrom",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressFromOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressTo",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperations",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsList",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectors",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsList",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsMethodSelectorsOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOperationsOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesEgressToOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesList",
    "GoogleAccessContextManagerServicePerimeterSpecEgressPoliciesOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPolicies",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFrom",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSources",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesList",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressFromSourcesOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressTo",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperations",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsList",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectors",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsList",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsMethodSelectorsOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOperationsOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesIngressToOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesList",
    "GoogleAccessContextManagerServicePerimeterSpecIngressPoliciesOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecOutputReference",
    "GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServices",
    "GoogleAccessContextManagerServicePerimeterSpecVpcAccessibleServicesOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatus",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPolicies",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFrom",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressFromOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressTo",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperations",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsList",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectors",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsList",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsMethodSelectorsOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOperationsOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesEgressToOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesList",
    "GoogleAccessContextManagerServicePerimeterStatusEgressPoliciesOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPolicies",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFrom",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSources",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesList",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressFromSourcesOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressTo",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperations",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsList",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectors",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsList",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsMethodSelectorsOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOperationsOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesIngressToOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesList",
    "GoogleAccessContextManagerServicePerimeterStatusIngressPoliciesOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusOutputReference",
    "GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServices",
    "GoogleAccessContextManagerServicePerimeterStatusVpcAccessibleServicesOutputReference",
    "GoogleAccessContextManagerServicePerimeterTimeouts",
    "GoogleAccessContextManagerServicePerimeterTimeoutsOutputReference",
]

publication.publish()
