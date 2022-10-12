'''
# `google_os_config_guest_policies`

Refer to the Terraform Registory for docs: [`google_os_config_guest_policies`](https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies).
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


class GoogleOsConfigGuestPolicies(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPolicies",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies google_os_config_guest_policies}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        assignment: typing.Union["GoogleOsConfigGuestPoliciesAssignment", typing.Dict[str, typing.Any]],
        guest_policy_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        etag: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        package_repositories: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositories", typing.Dict[str, typing.Any]]]]] = None,
        packages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesPackages", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        recipes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipes", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies google_os_config_guest_policies} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param assignment: assignment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#assignment GoogleOsConfigGuestPolicies#assignment}
        :param guest_policy_id: The logical name of the guest policy in the project with the following restrictions: Must contain only lowercase letters, numbers, and hyphens. Must start with a letter. Must be between 1-63 characters. Must end with a number or a letter. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#guest_policy_id GoogleOsConfigGuestPolicies#guest_policy_id}
        :param description: Description of the guest policy. Length of the description is limited to 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#description GoogleOsConfigGuestPolicies#description}
        :param etag: The etag for this guest policy. If this is provided on update, it must match the server's etag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#etag GoogleOsConfigGuestPolicies#etag}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param package_repositories: package_repositories block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#package_repositories GoogleOsConfigGuestPolicies#package_repositories}
        :param packages: packages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#packages GoogleOsConfigGuestPolicies#packages}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#project GoogleOsConfigGuestPolicies#project}.
        :param recipes: recipes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#recipes GoogleOsConfigGuestPolicies#recipes}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#timeouts GoogleOsConfigGuestPolicies#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPolicies.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleOsConfigGuestPoliciesConfig(
            assignment=assignment,
            guest_policy_id=guest_policy_id,
            description=description,
            etag=etag,
            id=id,
            package_repositories=package_repositories,
            packages=packages,
            project=project,
            recipes=recipes,
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

    @jsii.member(jsii_name="putAssignment")
    def put_assignment(
        self,
        *,
        group_labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesAssignmentGroupLabels", typing.Dict[str, typing.Any]]]]] = None,
        instance_name_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        os_types: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesAssignmentOsTypes", typing.Dict[str, typing.Any]]]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param group_labels: group_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#group_labels GoogleOsConfigGuestPolicies#group_labels}
        :param instance_name_prefixes: Targets VM instances whose name starts with one of these prefixes. Like labels, this is another way to group VM instances when targeting configs, for example prefix="prod-". Only supported for project-level policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#instance_name_prefixes GoogleOsConfigGuestPolicies#instance_name_prefixes}
        :param instances: Targets any of the instances specified. Instances are specified by their URI in the form zones/[ZONE]/instances/[INSTANCE_NAME]. Instance targeting is uncommon and is supported to facilitate the management of changes by the instance or to target specific VM instances for development and testing. Only supported for project-level policies and must reference instances within this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#instances GoogleOsConfigGuestPolicies#instances}
        :param os_types: os_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_types GoogleOsConfigGuestPolicies#os_types}
        :param zones: Targets instances in any of these zones. Leave empty to target instances in any zone. Zonal targeting is uncommon and is supported to facilitate the management of changes by zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#zones GoogleOsConfigGuestPolicies#zones}
        '''
        value = GoogleOsConfigGuestPoliciesAssignment(
            group_labels=group_labels,
            instance_name_prefixes=instance_name_prefixes,
            instances=instances,
            os_types=os_types,
            zones=zones,
        )

        return typing.cast(None, jsii.invoke(self, "putAssignment", [value]))

    @jsii.member(jsii_name="putPackageRepositories")
    def put_package_repositories(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositories", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPolicies.put_package_repositories)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPackageRepositories", [value]))

    @jsii.member(jsii_name="putPackages")
    def put_packages(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesPackages", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPolicies.put_packages)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPackages", [value]))

    @jsii.member(jsii_name="putRecipes")
    def put_recipes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPolicies.put_recipes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecipes", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#create GoogleOsConfigGuestPolicies#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#delete GoogleOsConfigGuestPolicies#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#update GoogleOsConfigGuestPolicies#update}.
        '''
        value = GoogleOsConfigGuestPoliciesTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEtag")
    def reset_etag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEtag", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPackageRepositories")
    def reset_package_repositories(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackageRepositories", []))

    @jsii.member(jsii_name="resetPackages")
    def reset_packages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackages", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRecipes")
    def reset_recipes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecipes", []))

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
    @jsii.member(jsii_name="assignment")
    def assignment(self) -> "GoogleOsConfigGuestPoliciesAssignmentOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesAssignmentOutputReference", jsii.get(self, "assignment"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="packageRepositories")
    def package_repositories(
        self,
    ) -> "GoogleOsConfigGuestPoliciesPackageRepositoriesList":
        return typing.cast("GoogleOsConfigGuestPoliciesPackageRepositoriesList", jsii.get(self, "packageRepositories"))

    @builtins.property
    @jsii.member(jsii_name="packages")
    def packages(self) -> "GoogleOsConfigGuestPoliciesPackagesList":
        return typing.cast("GoogleOsConfigGuestPoliciesPackagesList", jsii.get(self, "packages"))

    @builtins.property
    @jsii.member(jsii_name="recipes")
    def recipes(self) -> "GoogleOsConfigGuestPoliciesRecipesList":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesList", jsii.get(self, "recipes"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleOsConfigGuestPoliciesTimeoutsOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="assignmentInput")
    def assignment_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesAssignment"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesAssignment"], jsii.get(self, "assignmentInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="etagInput")
    def etag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "etagInput"))

    @builtins.property
    @jsii.member(jsii_name="guestPolicyIdInput")
    def guest_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guestPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="packageRepositoriesInput")
    def package_repositories_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackageRepositories"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackageRepositories"]]], jsii.get(self, "packageRepositoriesInput"))

    @builtins.property
    @jsii.member(jsii_name="packagesInput")
    def packages_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackages"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackages"]]], jsii.get(self, "packagesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="recipesInput")
    def recipes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipes"]]], jsii.get(self, "recipesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPolicies, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @etag.setter
    def etag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPolicies, "etag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "etag", value)

    @builtins.property
    @jsii.member(jsii_name="guestPolicyId")
    def guest_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guestPolicyId"))

    @guest_policy_id.setter
    def guest_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPolicies, "guest_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guestPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPolicies, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPolicies, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignment",
    jsii_struct_bases=[],
    name_mapping={
        "group_labels": "groupLabels",
        "instance_name_prefixes": "instanceNamePrefixes",
        "instances": "instances",
        "os_types": "osTypes",
        "zones": "zones",
    },
)
class GoogleOsConfigGuestPoliciesAssignment:
    def __init__(
        self,
        *,
        group_labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesAssignmentGroupLabels", typing.Dict[str, typing.Any]]]]] = None,
        instance_name_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        instances: typing.Optional[typing.Sequence[builtins.str]] = None,
        os_types: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesAssignmentOsTypes", typing.Dict[str, typing.Any]]]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param group_labels: group_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#group_labels GoogleOsConfigGuestPolicies#group_labels}
        :param instance_name_prefixes: Targets VM instances whose name starts with one of these prefixes. Like labels, this is another way to group VM instances when targeting configs, for example prefix="prod-". Only supported for project-level policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#instance_name_prefixes GoogleOsConfigGuestPolicies#instance_name_prefixes}
        :param instances: Targets any of the instances specified. Instances are specified by their URI in the form zones/[ZONE]/instances/[INSTANCE_NAME]. Instance targeting is uncommon and is supported to facilitate the management of changes by the instance or to target specific VM instances for development and testing. Only supported for project-level policies and must reference instances within this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#instances GoogleOsConfigGuestPolicies#instances}
        :param os_types: os_types block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_types GoogleOsConfigGuestPolicies#os_types}
        :param zones: Targets instances in any of these zones. Leave empty to target instances in any zone. Zonal targeting is uncommon and is supported to facilitate the management of changes by zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#zones GoogleOsConfigGuestPolicies#zones}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignment.__init__)
            check_type(argname="argument group_labels", value=group_labels, expected_type=type_hints["group_labels"])
            check_type(argname="argument instance_name_prefixes", value=instance_name_prefixes, expected_type=type_hints["instance_name_prefixes"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument os_types", value=os_types, expected_type=type_hints["os_types"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {}
        if group_labels is not None:
            self._values["group_labels"] = group_labels
        if instance_name_prefixes is not None:
            self._values["instance_name_prefixes"] = instance_name_prefixes
        if instances is not None:
            self._values["instances"] = instances
        if os_types is not None:
            self._values["os_types"] = os_types
        if zones is not None:
            self._values["zones"] = zones

    @builtins.property
    def group_labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesAssignmentGroupLabels"]]]:
        '''group_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#group_labels GoogleOsConfigGuestPolicies#group_labels}
        '''
        result = self._values.get("group_labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesAssignmentGroupLabels"]]], result)

    @builtins.property
    def instance_name_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targets VM instances whose name starts with one of these prefixes.

        Like labels, this is another way to group VM instances when targeting configs,
        for example prefix="prod-".
        Only supported for project-level policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#instance_name_prefixes GoogleOsConfigGuestPolicies#instance_name_prefixes}
        '''
        result = self._values.get("instance_name_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def instances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targets any of the instances specified.

        Instances are specified by their URI in the form
        zones/[ZONE]/instances/[INSTANCE_NAME].
        Instance targeting is uncommon and is supported to facilitate the management of changes
        by the instance or to target specific VM instances for development and testing.
        Only supported for project-level policies and must reference instances within this project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#instances GoogleOsConfigGuestPolicies#instances}
        '''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def os_types(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesAssignmentOsTypes"]]]:
        '''os_types block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_types GoogleOsConfigGuestPolicies#os_types}
        '''
        result = self._values.get("os_types")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesAssignmentOsTypes"]]], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Targets instances in any of these zones.

        Leave empty to target instances in any zone.
        Zonal targeting is uncommon and is supported to facilitate the management of changes by zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#zones GoogleOsConfigGuestPolicies#zones}
        '''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesAssignment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentGroupLabels",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels"},
)
class GoogleOsConfigGuestPoliciesAssignmentGroupLabels:
    def __init__(self, *, labels: typing.Mapping[builtins.str, builtins.str]) -> None:
        '''
        :param labels: Google Compute Engine instance labels that must be present for an instance to be included in this assignment group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#labels GoogleOsConfigGuestPolicies#labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentGroupLabels.__init__)
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "labels": labels,
        }

    @builtins.property
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Google Compute Engine instance labels that must be present for an instance to be included in this assignment group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#labels GoogleOsConfigGuestPolicies#labels}
        '''
        result = self._values.get("labels")
        assert result is not None, "Required property 'labels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesAssignmentGroupLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentGroupLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentGroupLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentGroupLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesAssignmentGroupLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesAssignmentGroupLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesAssignmentGroupLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentOsTypes",
    jsii_struct_bases=[],
    name_mapping={
        "os_architecture": "osArchitecture",
        "os_short_name": "osShortName",
        "os_version": "osVersion",
    },
)
class GoogleOsConfigGuestPoliciesAssignmentOsTypes:
    def __init__(
        self,
        *,
        os_architecture: typing.Optional[builtins.str] = None,
        os_short_name: typing.Optional[builtins.str] = None,
        os_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param os_architecture: Targets VM instances with OS Inventory enabled and having the following OS architecture. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_architecture GoogleOsConfigGuestPolicies#os_architecture}
        :param os_short_name: Targets VM instances with OS Inventory enabled and having the following OS short name, for example "debian" or "windows". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_short_name GoogleOsConfigGuestPolicies#os_short_name}
        :param os_version: Targets VM instances with OS Inventory enabled and having the following following OS version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_version GoogleOsConfigGuestPolicies#os_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOsTypes.__init__)
            check_type(argname="argument os_architecture", value=os_architecture, expected_type=type_hints["os_architecture"])
            check_type(argname="argument os_short_name", value=os_short_name, expected_type=type_hints["os_short_name"])
            check_type(argname="argument os_version", value=os_version, expected_type=type_hints["os_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if os_architecture is not None:
            self._values["os_architecture"] = os_architecture
        if os_short_name is not None:
            self._values["os_short_name"] = os_short_name
        if os_version is not None:
            self._values["os_version"] = os_version

    @builtins.property
    def os_architecture(self) -> typing.Optional[builtins.str]:
        '''Targets VM instances with OS Inventory enabled and having the following OS architecture.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_architecture GoogleOsConfigGuestPolicies#os_architecture}
        '''
        result = self._values.get("os_architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_short_name(self) -> typing.Optional[builtins.str]:
        '''Targets VM instances with OS Inventory enabled and having the following OS short name, for example "debian" or "windows".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_short_name GoogleOsConfigGuestPolicies#os_short_name}
        '''
        result = self._values.get("os_short_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_version(self) -> typing.Optional[builtins.str]:
        '''Targets VM instances with OS Inventory enabled and having the following following OS version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#os_version GoogleOsConfigGuestPolicies#os_version}
        '''
        result = self._values.get("os_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesAssignmentOsTypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesAssignmentOsTypesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentOsTypesList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOsTypesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOsTypesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentOsTypes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentOsTypes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentOsTypes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOsArchitecture")
    def reset_os_architecture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsArchitecture", []))

    @jsii.member(jsii_name="resetOsShortName")
    def reset_os_short_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsShortName", []))

    @jsii.member(jsii_name="resetOsVersion")
    def reset_os_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsVersion", []))

    @builtins.property
    @jsii.member(jsii_name="osArchitectureInput")
    def os_architecture_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osArchitectureInput"))

    @builtins.property
    @jsii.member(jsii_name="osShortNameInput")
    def os_short_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osShortNameInput"))

    @builtins.property
    @jsii.member(jsii_name="osVersionInput")
    def os_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="osArchitecture")
    def os_architecture(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osArchitecture"))

    @os_architecture.setter
    def os_architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference, "os_architecture").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osArchitecture", value)

    @builtins.property
    @jsii.member(jsii_name="osShortName")
    def os_short_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osShortName"))

    @os_short_name.setter
    def os_short_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference, "os_short_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osShortName", value)

    @builtins.property
    @jsii.member(jsii_name="osVersion")
    def os_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osVersion"))

    @os_version.setter
    def os_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference, "os_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesAssignmentOsTypes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesAssignmentOsTypes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesAssignmentOsTypes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesAssignmentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesAssignmentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGroupLabels")
    def put_group_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleOsConfigGuestPoliciesAssignmentGroupLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOutputReference.put_group_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGroupLabels", [value]))

    @jsii.member(jsii_name="putOsTypes")
    def put_os_types(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleOsConfigGuestPoliciesAssignmentOsTypes, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesAssignmentOutputReference.put_os_types)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOsTypes", [value]))

    @jsii.member(jsii_name="resetGroupLabels")
    def reset_group_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupLabels", []))

    @jsii.member(jsii_name="resetInstanceNamePrefixes")
    def reset_instance_name_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceNamePrefixes", []))

    @jsii.member(jsii_name="resetInstances")
    def reset_instances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstances", []))

    @jsii.member(jsii_name="resetOsTypes")
    def reset_os_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsTypes", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @builtins.property
    @jsii.member(jsii_name="groupLabels")
    def group_labels(self) -> GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList:
        return typing.cast(GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList, jsii.get(self, "groupLabels"))

    @builtins.property
    @jsii.member(jsii_name="osTypes")
    def os_types(self) -> GoogleOsConfigGuestPoliciesAssignmentOsTypesList:
        return typing.cast(GoogleOsConfigGuestPoliciesAssignmentOsTypesList, jsii.get(self, "osTypes"))

    @builtins.property
    @jsii.member(jsii_name="groupLabelsInput")
    def group_labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentGroupLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentGroupLabels]]], jsii.get(self, "groupLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceNamePrefixesInput")
    def instance_name_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceNamePrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypesInput")
    def os_types_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentOsTypes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesAssignmentOsTypes]]], jsii.get(self, "osTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceNamePrefixes")
    def instance_name_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceNamePrefixes"))

    @instance_name_prefixes.setter
    def instance_name_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOutputReference, "instance_name_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceNamePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOutputReference, "instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOutputReference, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleOsConfigGuestPoliciesAssignment]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesAssignment], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesAssignment],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesAssignmentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "assignment": "assignment",
        "guest_policy_id": "guestPolicyId",
        "description": "description",
        "etag": "etag",
        "id": "id",
        "package_repositories": "packageRepositories",
        "packages": "packages",
        "project": "project",
        "recipes": "recipes",
        "timeouts": "timeouts",
    },
)
class GoogleOsConfigGuestPoliciesConfig(cdktf.TerraformMetaArguments):
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
        assignment: typing.Union[GoogleOsConfigGuestPoliciesAssignment, typing.Dict[str, typing.Any]],
        guest_policy_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        etag: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        package_repositories: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositories", typing.Dict[str, typing.Any]]]]] = None,
        packages: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesPackages", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        recipes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipes", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param assignment: assignment block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#assignment GoogleOsConfigGuestPolicies#assignment}
        :param guest_policy_id: The logical name of the guest policy in the project with the following restrictions: Must contain only lowercase letters, numbers, and hyphens. Must start with a letter. Must be between 1-63 characters. Must end with a number or a letter. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#guest_policy_id GoogleOsConfigGuestPolicies#guest_policy_id}
        :param description: Description of the guest policy. Length of the description is limited to 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#description GoogleOsConfigGuestPolicies#description}
        :param etag: The etag for this guest policy. If this is provided on update, it must match the server's etag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#etag GoogleOsConfigGuestPolicies#etag}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param package_repositories: package_repositories block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#package_repositories GoogleOsConfigGuestPolicies#package_repositories}
        :param packages: packages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#packages GoogleOsConfigGuestPolicies#packages}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#project GoogleOsConfigGuestPolicies#project}.
        :param recipes: recipes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#recipes GoogleOsConfigGuestPolicies#recipes}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#timeouts GoogleOsConfigGuestPolicies#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(assignment, dict):
            assignment = GoogleOsConfigGuestPoliciesAssignment(**assignment)
        if isinstance(timeouts, dict):
            timeouts = GoogleOsConfigGuestPoliciesTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument assignment", value=assignment, expected_type=type_hints["assignment"])
            check_type(argname="argument guest_policy_id", value=guest_policy_id, expected_type=type_hints["guest_policy_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument package_repositories", value=package_repositories, expected_type=type_hints["package_repositories"])
            check_type(argname="argument packages", value=packages, expected_type=type_hints["packages"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument recipes", value=recipes, expected_type=type_hints["recipes"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "assignment": assignment,
            "guest_policy_id": guest_policy_id,
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
        if etag is not None:
            self._values["etag"] = etag
        if id is not None:
            self._values["id"] = id
        if package_repositories is not None:
            self._values["package_repositories"] = package_repositories
        if packages is not None:
            self._values["packages"] = packages
        if project is not None:
            self._values["project"] = project
        if recipes is not None:
            self._values["recipes"] = recipes
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
    def assignment(self) -> GoogleOsConfigGuestPoliciesAssignment:
        '''assignment block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#assignment GoogleOsConfigGuestPolicies#assignment}
        '''
        result = self._values.get("assignment")
        assert result is not None, "Required property 'assignment' is missing"
        return typing.cast(GoogleOsConfigGuestPoliciesAssignment, result)

    @builtins.property
    def guest_policy_id(self) -> builtins.str:
        '''The logical name of the guest policy in the project with the following restrictions: Must contain only lowercase letters, numbers, and hyphens.

        Must start with a letter.
        Must be between 1-63 characters.
        Must end with a number or a letter.
        Must be unique within the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#guest_policy_id GoogleOsConfigGuestPolicies#guest_policy_id}
        '''
        result = self._values.get("guest_policy_id")
        assert result is not None, "Required property 'guest_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the guest policy. Length of the description is limited to 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#description GoogleOsConfigGuestPolicies#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def etag(self) -> typing.Optional[builtins.str]:
        '''The etag for this guest policy. If this is provided on update, it must match the server's etag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#etag GoogleOsConfigGuestPolicies#etag}
        '''
        result = self._values.get("etag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def package_repositories(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackageRepositories"]]]:
        '''package_repositories block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#package_repositories GoogleOsConfigGuestPolicies#package_repositories}
        '''
        result = self._values.get("package_repositories")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackageRepositories"]]], result)

    @builtins.property
    def packages(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackages"]]]:
        '''packages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#packages GoogleOsConfigGuestPolicies#packages}
        '''
        result = self._values.get("packages")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesPackages"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#project GoogleOsConfigGuestPolicies#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipes"]]]:
        '''recipes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#recipes GoogleOsConfigGuestPolicies#recipes}
        '''
        result = self._values.get("recipes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipes"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleOsConfigGuestPoliciesTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#timeouts GoogleOsConfigGuestPolicies#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositories",
    jsii_struct_bases=[],
    name_mapping={"apt": "apt", "goo": "goo", "yum": "yum", "zypper": "zypper"},
)
class GoogleOsConfigGuestPoliciesPackageRepositories:
    def __init__(
        self,
        *,
        apt: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositoriesApt", typing.Dict[str, typing.Any]]] = None,
        goo: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositoriesGoo", typing.Dict[str, typing.Any]]] = None,
        yum: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositoriesYum", typing.Dict[str, typing.Any]]] = None,
        zypper: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesPackageRepositoriesZypper", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param apt: apt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#apt GoogleOsConfigGuestPolicies#apt}
        :param goo: goo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#goo GoogleOsConfigGuestPolicies#goo}
        :param yum: yum block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#yum GoogleOsConfigGuestPolicies#yum}
        :param zypper: zypper block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#zypper GoogleOsConfigGuestPolicies#zypper}
        '''
        if isinstance(apt, dict):
            apt = GoogleOsConfigGuestPoliciesPackageRepositoriesApt(**apt)
        if isinstance(goo, dict):
            goo = GoogleOsConfigGuestPoliciesPackageRepositoriesGoo(**goo)
        if isinstance(yum, dict):
            yum = GoogleOsConfigGuestPoliciesPackageRepositoriesYum(**yum)
        if isinstance(zypper, dict):
            zypper = GoogleOsConfigGuestPoliciesPackageRepositoriesZypper(**zypper)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositories.__init__)
            check_type(argname="argument apt", value=apt, expected_type=type_hints["apt"])
            check_type(argname="argument goo", value=goo, expected_type=type_hints["goo"])
            check_type(argname="argument yum", value=yum, expected_type=type_hints["yum"])
            check_type(argname="argument zypper", value=zypper, expected_type=type_hints["zypper"])
        self._values: typing.Dict[str, typing.Any] = {}
        if apt is not None:
            self._values["apt"] = apt
        if goo is not None:
            self._values["goo"] = goo
        if yum is not None:
            self._values["yum"] = yum
        if zypper is not None:
            self._values["zypper"] = zypper

    @builtins.property
    def apt(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesApt"]:
        '''apt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#apt GoogleOsConfigGuestPolicies#apt}
        '''
        result = self._values.get("apt")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesApt"], result)

    @builtins.property
    def goo(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesGoo"]:
        '''goo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#goo GoogleOsConfigGuestPolicies#goo}
        '''
        result = self._values.get("goo")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesGoo"], result)

    @builtins.property
    def yum(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesYum"]:
        '''yum block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#yum GoogleOsConfigGuestPolicies#yum}
        '''
        result = self._values.get("yum")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesYum"], result)

    @builtins.property
    def zypper(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesZypper"]:
        '''zypper block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#zypper GoogleOsConfigGuestPolicies#zypper}
        '''
        result = self._values.get("zypper")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesZypper"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesPackageRepositories(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesApt",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "distribution": "distribution",
        "uri": "uri",
        "archive_type": "archiveType",
        "gpg_key": "gpgKey",
    },
)
class GoogleOsConfigGuestPoliciesPackageRepositoriesApt:
    def __init__(
        self,
        *,
        components: typing.Sequence[builtins.str],
        distribution: builtins.str,
        uri: builtins.str,
        archive_type: typing.Optional[builtins.str] = None,
        gpg_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param components: List of components for this repository. Must contain at least one item. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#components GoogleOsConfigGuestPolicies#components}
        :param distribution: Distribution of this repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#distribution GoogleOsConfigGuestPolicies#distribution}
        :param uri: URI for this repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#uri GoogleOsConfigGuestPolicies#uri}
        :param archive_type: Type of archive files in this repository. The default behavior is DEB. Default value: "DEB" Possible values: ["DEB", "DEB_SRC"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_type GoogleOsConfigGuestPolicies#archive_type}
        :param gpg_key: URI of the key file for this repository. The agent maintains a keyring at /etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg containing all the keys in any applied guest policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_key GoogleOsConfigGuestPolicies#gpg_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesApt.__init__)
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument archive_type", value=archive_type, expected_type=type_hints["archive_type"])
            check_type(argname="argument gpg_key", value=gpg_key, expected_type=type_hints["gpg_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "components": components,
            "distribution": distribution,
            "uri": uri,
        }
        if archive_type is not None:
            self._values["archive_type"] = archive_type
        if gpg_key is not None:
            self._values["gpg_key"] = gpg_key

    @builtins.property
    def components(self) -> typing.List[builtins.str]:
        '''List of components for this repository. Must contain at least one item.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#components GoogleOsConfigGuestPolicies#components}
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def distribution(self) -> builtins.str:
        '''Distribution of this repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#distribution GoogleOsConfigGuestPolicies#distribution}
        '''
        result = self._values.get("distribution")
        assert result is not None, "Required property 'distribution' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''URI for this repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#uri GoogleOsConfigGuestPolicies#uri}
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_type(self) -> typing.Optional[builtins.str]:
        '''Type of archive files in this repository. The default behavior is DEB. Default value: "DEB" Possible values: ["DEB", "DEB_SRC"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_type GoogleOsConfigGuestPolicies#archive_type}
        '''
        result = self._values.get("archive_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gpg_key(self) -> typing.Optional[builtins.str]:
        '''URI of the key file for this repository.

        The agent maintains a keyring at
        /etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg containing all the keys in any applied guest policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_key GoogleOsConfigGuestPolicies#gpg_key}
        '''
        result = self._values.get("gpg_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesPackageRepositoriesApt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetArchiveType")
    def reset_archive_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveType", []))

    @jsii.member(jsii_name="resetGpgKey")
    def reset_gpg_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpgKey", []))

    @builtins.property
    @jsii.member(jsii_name="archiveTypeInput")
    def archive_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "archiveTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="componentsInput")
    def components_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "componentsInput"))

    @builtins.property
    @jsii.member(jsii_name="distributionInput")
    def distribution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionInput"))

    @builtins.property
    @jsii.member(jsii_name="gpgKeyInput")
    def gpg_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpgKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveType")
    def archive_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "archiveType"))

    @archive_type.setter
    def archive_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, "archive_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveType", value)

    @builtins.property
    @jsii.member(jsii_name="components")
    def components(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "components"))

    @components.setter
    def components(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, "components").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distribution"))

    @distribution.setter
    def distribution(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, "distribution").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distribution", value)

    @builtins.property
    @jsii.member(jsii_name="gpgKey")
    def gpg_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpgKey"))

    @gpg_key.setter
    def gpg_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, "gpg_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpgKey", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesApt]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesApt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesApt],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesGoo",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "url": "url"},
)
class GoogleOsConfigGuestPoliciesPackageRepositoriesGoo:
    def __init__(self, *, name: builtins.str, url: builtins.str) -> None:
        '''
        :param name: The name of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        :param url: The url of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#url GoogleOsConfigGuestPolicies#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesGoo.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "url": url,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The url of the repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#url GoogleOsConfigGuestPolicies#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesPackageRepositoriesGoo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesGoo]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesGoo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesGoo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesPackageRepositoriesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesPackageRepositories]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesPackageRepositories]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesPackageRepositories]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putApt")
    def put_apt(
        self,
        *,
        components: typing.Sequence[builtins.str],
        distribution: builtins.str,
        uri: builtins.str,
        archive_type: typing.Optional[builtins.str] = None,
        gpg_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param components: List of components for this repository. Must contain at least one item. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#components GoogleOsConfigGuestPolicies#components}
        :param distribution: Distribution of this repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#distribution GoogleOsConfigGuestPolicies#distribution}
        :param uri: URI for this repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#uri GoogleOsConfigGuestPolicies#uri}
        :param archive_type: Type of archive files in this repository. The default behavior is DEB. Default value: "DEB" Possible values: ["DEB", "DEB_SRC"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_type GoogleOsConfigGuestPolicies#archive_type}
        :param gpg_key: URI of the key file for this repository. The agent maintains a keyring at /etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg containing all the keys in any applied guest policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_key GoogleOsConfigGuestPolicies#gpg_key}
        '''
        value = GoogleOsConfigGuestPoliciesPackageRepositoriesApt(
            components=components,
            distribution=distribution,
            uri=uri,
            archive_type=archive_type,
            gpg_key=gpg_key,
        )

        return typing.cast(None, jsii.invoke(self, "putApt", [value]))

    @jsii.member(jsii_name="putGoo")
    def put_goo(self, *, name: builtins.str, url: builtins.str) -> None:
        '''
        :param name: The name of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        :param url: The url of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#url GoogleOsConfigGuestPolicies#url}
        '''
        value = GoogleOsConfigGuestPoliciesPackageRepositoriesGoo(name=name, url=url)

        return typing.cast(None, jsii.invoke(self, "putGoo", [value]))

    @jsii.member(jsii_name="putYum")
    def put_yum(
        self,
        *,
        base_url: builtins.str,
        id: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        gpg_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param base_url: The location of the repository directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#base_url GoogleOsConfigGuestPolicies#base_url}
        :param id: A one word, unique name for this repository. This is the repo id in the Yum config file and also the displayName if displayName is omitted. This id is also used as the unique identifier when checking for guest policy conflicts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param display_name: The display name of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#display_name GoogleOsConfigGuestPolicies#display_name}
        :param gpg_keys: URIs of GPG keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_keys GoogleOsConfigGuestPolicies#gpg_keys}
        '''
        value = GoogleOsConfigGuestPoliciesPackageRepositoriesYum(
            base_url=base_url, id=id, display_name=display_name, gpg_keys=gpg_keys
        )

        return typing.cast(None, jsii.invoke(self, "putYum", [value]))

    @jsii.member(jsii_name="putZypper")
    def put_zypper(
        self,
        *,
        base_url: builtins.str,
        id: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        gpg_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param base_url: The location of the repository directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#base_url GoogleOsConfigGuestPolicies#base_url}
        :param id: A one word, unique name for this repository. This is the repo id in the zypper config file and also the displayName if displayName is omitted. This id is also used as the unique identifier when checking for guest policy conflicts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param display_name: The display name of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#display_name GoogleOsConfigGuestPolicies#display_name}
        :param gpg_keys: URIs of GPG keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_keys GoogleOsConfigGuestPolicies#gpg_keys}
        '''
        value = GoogleOsConfigGuestPoliciesPackageRepositoriesZypper(
            base_url=base_url, id=id, display_name=display_name, gpg_keys=gpg_keys
        )

        return typing.cast(None, jsii.invoke(self, "putZypper", [value]))

    @jsii.member(jsii_name="resetApt")
    def reset_apt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApt", []))

    @jsii.member(jsii_name="resetGoo")
    def reset_goo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoo", []))

    @jsii.member(jsii_name="resetYum")
    def reset_yum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetYum", []))

    @jsii.member(jsii_name="resetZypper")
    def reset_zypper(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZypper", []))

    @builtins.property
    @jsii.member(jsii_name="apt")
    def apt(self) -> GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference, jsii.get(self, "apt"))

    @builtins.property
    @jsii.member(jsii_name="goo")
    def goo(self) -> GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference, jsii.get(self, "goo"))

    @builtins.property
    @jsii.member(jsii_name="yum")
    def yum(self) -> "GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference", jsii.get(self, "yum"))

    @builtins.property
    @jsii.member(jsii_name="zypper")
    def zypper(
        self,
    ) -> "GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference", jsii.get(self, "zypper"))

    @builtins.property
    @jsii.member(jsii_name="aptInput")
    def apt_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesApt]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesApt], jsii.get(self, "aptInput"))

    @builtins.property
    @jsii.member(jsii_name="gooInput")
    def goo_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesGoo]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesGoo], jsii.get(self, "gooInput"))

    @builtins.property
    @jsii.member(jsii_name="yumInput")
    def yum_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesYum"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesYum"], jsii.get(self, "yumInput"))

    @builtins.property
    @jsii.member(jsii_name="zypperInput")
    def zypper_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesZypper"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesPackageRepositoriesZypper"], jsii.get(self, "zypperInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesPackageRepositories, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesPackageRepositories, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesPackageRepositories, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesYum",
    jsii_struct_bases=[],
    name_mapping={
        "base_url": "baseUrl",
        "id": "id",
        "display_name": "displayName",
        "gpg_keys": "gpgKeys",
    },
)
class GoogleOsConfigGuestPoliciesPackageRepositoriesYum:
    def __init__(
        self,
        *,
        base_url: builtins.str,
        id: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        gpg_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param base_url: The location of the repository directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#base_url GoogleOsConfigGuestPolicies#base_url}
        :param id: A one word, unique name for this repository. This is the repo id in the Yum config file and also the displayName if displayName is omitted. This id is also used as the unique identifier when checking for guest policy conflicts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param display_name: The display name of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#display_name GoogleOsConfigGuestPolicies#display_name}
        :param gpg_keys: URIs of GPG keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_keys GoogleOsConfigGuestPolicies#gpg_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesYum.__init__)
            check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument gpg_keys", value=gpg_keys, expected_type=type_hints["gpg_keys"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_url": base_url,
            "id": id,
        }
        if display_name is not None:
            self._values["display_name"] = display_name
        if gpg_keys is not None:
            self._values["gpg_keys"] = gpg_keys

    @builtins.property
    def base_url(self) -> builtins.str:
        '''The location of the repository directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#base_url GoogleOsConfigGuestPolicies#base_url}
        '''
        result = self._values.get("base_url")
        assert result is not None, "Required property 'base_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''A one word, unique name for this repository.

        This is the repo id in the Yum config file and also the displayName
        if displayName is omitted. This id is also used as the unique identifier when checking for guest policy conflicts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#display_name GoogleOsConfigGuestPolicies#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gpg_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''URIs of GPG keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_keys GoogleOsConfigGuestPolicies#gpg_keys}
        '''
        result = self._values.get("gpg_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesPackageRepositoriesYum(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetGpgKeys")
    def reset_gpg_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpgKeys", []))

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gpgKeysInput")
    def gpg_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "gpgKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference, "base_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="gpgKeys")
    def gpg_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "gpgKeys"))

    @gpg_keys.setter
    def gpg_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference, "gpg_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpgKeys", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesYum]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesYum], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesYum],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesZypper",
    jsii_struct_bases=[],
    name_mapping={
        "base_url": "baseUrl",
        "id": "id",
        "display_name": "displayName",
        "gpg_keys": "gpgKeys",
    },
)
class GoogleOsConfigGuestPoliciesPackageRepositoriesZypper:
    def __init__(
        self,
        *,
        base_url: builtins.str,
        id: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        gpg_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param base_url: The location of the repository directory. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#base_url GoogleOsConfigGuestPolicies#base_url}
        :param id: A one word, unique name for this repository. This is the repo id in the zypper config file and also the displayName if displayName is omitted. This id is also used as the unique identifier when checking for guest policy conflicts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param display_name: The display name of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#display_name GoogleOsConfigGuestPolicies#display_name}
        :param gpg_keys: URIs of GPG keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_keys GoogleOsConfigGuestPolicies#gpg_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesZypper.__init__)
            check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument gpg_keys", value=gpg_keys, expected_type=type_hints["gpg_keys"])
        self._values: typing.Dict[str, typing.Any] = {
            "base_url": base_url,
            "id": id,
        }
        if display_name is not None:
            self._values["display_name"] = display_name
        if gpg_keys is not None:
            self._values["gpg_keys"] = gpg_keys

    @builtins.property
    def base_url(self) -> builtins.str:
        '''The location of the repository directory.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#base_url GoogleOsConfigGuestPolicies#base_url}
        '''
        result = self._values.get("base_url")
        assert result is not None, "Required property 'base_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''A one word, unique name for this repository.

        This is the repo id in the zypper config file and also the displayName
        if displayName is omitted. This id is also used as the unique identifier when checking for guest policy conflicts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#display_name GoogleOsConfigGuestPolicies#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gpg_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''URIs of GPG keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gpg_keys GoogleOsConfigGuestPolicies#gpg_keys}
        '''
        result = self._values.get("gpg_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesPackageRepositoriesZypper(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetGpgKeys")
    def reset_gpg_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpgKeys", []))

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gpgKeysInput")
    def gpg_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "gpgKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference, "base_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="gpgKeys")
    def gpg_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "gpgKeys"))

    @gpg_keys.setter
    def gpg_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference, "gpg_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpgKeys", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesZypper]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesZypper], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesPackageRepositoriesZypper],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackages",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "desired_state": "desiredState",
        "manager": "manager",
    },
)
class GoogleOsConfigGuestPoliciesPackages:
    def __init__(
        self,
        *,
        name: builtins.str,
        desired_state: typing.Optional[builtins.str] = None,
        manager: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the package. A package is uniquely identified for conflict validation by checking the package name and the manager(s) that the package targets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        :param desired_state: The desiredState the agent should maintain for this package. The default is to ensure the package is installed. Possible values: ["INSTALLED", "UPDATED", "REMOVED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#desired_state GoogleOsConfigGuestPolicies#desired_state}
        :param manager: Type of package manager that can be used to install this package. If a system does not have the package manager, the package is not installed or removed no error message is returned. By default, or if you specify ANY, the agent attempts to install and remove this package using the default package manager. This is useful when creating a policy that applies to different types of systems. The default behavior is ANY. Default value: "ANY" Possible values: ["ANY", "APT", "YUM", "ZYPPER", "GOO"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#manager GoogleOsConfigGuestPolicies#manager}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackages.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument manager", value=manager, expected_type=type_hints["manager"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if manager is not None:
            self._values["manager"] = manager

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the package.

        A package is uniquely identified for conflict validation
        by checking the package name and the manager(s) that the package targets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''The desiredState the agent should maintain for this package.

        The default is to ensure the package is installed. Possible values: ["INSTALLED", "UPDATED", "REMOVED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#desired_state GoogleOsConfigGuestPolicies#desired_state}
        '''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manager(self) -> typing.Optional[builtins.str]:
        '''Type of package manager that can be used to install this package.

        If a system does not have the package manager,
        the package is not installed or removed no error message is returned. By default, or if you specify ANY,
        the agent attempts to install and remove this package using the default package manager.
        This is useful when creating a policy that applies to different types of systems.
        The default behavior is ANY. Default value: "ANY" Possible values: ["ANY", "APT", "YUM", "ZYPPER", "GOO"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#manager GoogleOsConfigGuestPolicies#manager}
        '''
        result = self._values.get("manager")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesPackages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesPackagesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackagesList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackagesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesPackagesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackagesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesPackagesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesPackages]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesPackages]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesPackages]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesPackagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesPackagesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesPackagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetManager")
    def reset_manager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManager", []))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="managerInput")
    def manager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesOutputReference, "desired_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="manager")
    def manager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "manager"))

    @manager.setter
    def manager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesOutputReference, "manager").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manager", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesPackages, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesPackages, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesPackages, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesPackagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipes",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "artifacts": "artifacts",
        "desired_state": "desiredState",
        "install_steps": "installSteps",
        "update_steps": "updateSteps",
        "version": "version",
    },
)
class GoogleOsConfigGuestPoliciesRecipes:
    def __init__(
        self,
        *,
        name: builtins.str,
        artifacts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipesArtifacts", typing.Dict[str, typing.Any]]]]] = None,
        desired_state: typing.Optional[builtins.str] = None,
        install_steps: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallSteps", typing.Dict[str, typing.Any]]]]] = None,
        update_steps: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateSteps", typing.Dict[str, typing.Any]]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Unique identifier for the recipe. Only one recipe with a given name is installed on an instance. Names are also used to identify resources which helps to determine whether guest policies have conflicts. This means that requests to create multiple recipes with the same name and version are rejected since they could potentially have conflicting assignments. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifacts GoogleOsConfigGuestPolicies#artifacts}
        :param desired_state: Default is INSTALLED. The desired state the agent should maintain for this recipe. INSTALLED: The software recipe is installed on the instance but won't be updated to new versions. INSTALLED_KEEP_UPDATED: The software recipe is installed on the instance. The recipe is updated to a higher version, if a higher version of the recipe is assigned to this instance. REMOVE: Remove is unsupported for software recipes and attempts to create or update a recipe to the REMOVE state is rejected. Default value: "INSTALLED" Possible values: ["INSTALLED", "UPDATED", "REMOVED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#desired_state GoogleOsConfigGuestPolicies#desired_state}
        :param install_steps: install_steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#install_steps GoogleOsConfigGuestPolicies#install_steps}
        :param update_steps: update_steps block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#update_steps GoogleOsConfigGuestPolicies#update_steps}
        :param version: The version of this software recipe. Version can be up to 4 period separated numbers (e.g. 12.34.56.78). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#version GoogleOsConfigGuestPolicies#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipes.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument install_steps", value=install_steps, expected_type=type_hints["install_steps"])
            check_type(argname="argument update_steps", value=update_steps, expected_type=type_hints["update_steps"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if artifacts is not None:
            self._values["artifacts"] = artifacts
        if desired_state is not None:
            self._values["desired_state"] = desired_state
        if install_steps is not None:
            self._values["install_steps"] = install_steps
        if update_steps is not None:
            self._values["update_steps"] = update_steps
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> builtins.str:
        '''Unique identifier for the recipe.

        Only one recipe with a given name is installed on an instance.
        Names are also used to identify resources which helps to determine whether guest policies have conflicts.
        This means that requests to create multiple recipes with the same name and version are rejected since they
        could potentially have conflicting assignments.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#name GoogleOsConfigGuestPolicies#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def artifacts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesArtifacts"]]]:
        '''artifacts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifacts GoogleOsConfigGuestPolicies#artifacts}
        '''
        result = self._values.get("artifacts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesArtifacts"]]], result)

    @builtins.property
    def desired_state(self) -> typing.Optional[builtins.str]:
        '''Default is INSTALLED. The desired state the agent should maintain for this recipe.

        INSTALLED: The software recipe is installed on the instance but won't be updated to new versions.
        INSTALLED_KEEP_UPDATED: The software recipe is installed on the instance. The recipe is updated to a higher version,
        if a higher version of the recipe is assigned to this instance.
        REMOVE: Remove is unsupported for software recipes and attempts to create or update a recipe to the REMOVE state is rejected. Default value: "INSTALLED" Possible values: ["INSTALLED", "UPDATED", "REMOVED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#desired_state GoogleOsConfigGuestPolicies#desired_state}
        '''
        result = self._values.get("desired_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_steps(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesInstallSteps"]]]:
        '''install_steps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#install_steps GoogleOsConfigGuestPolicies#install_steps}
        '''
        result = self._values.get("install_steps")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesInstallSteps"]]], result)

    @builtins.property
    def update_steps(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesUpdateSteps"]]]:
        '''update_steps block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#update_steps GoogleOsConfigGuestPolicies#update_steps}
        '''
        result = self._values.get("update_steps")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesUpdateSteps"]]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of this software recipe. Version can be up to 4 period separated numbers (e.g. 12.34.56.78).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#version GoogleOsConfigGuestPolicies#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifacts",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "allow_insecure": "allowInsecure",
        "gcs": "gcs",
        "remote": "remote",
    },
)
class GoogleOsConfigGuestPoliciesRecipesArtifacts:
    def __init__(
        self,
        *,
        id: builtins.str,
        allow_insecure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        gcs: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesArtifactsGcs", typing.Dict[str, typing.Any]]] = None,
        remote: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesArtifactsRemote", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param id: Id of the artifact, which the installation and update steps of this recipe can reference. Artifacts in a recipe cannot have the same id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param allow_insecure: Defaults to false. When false, recipes are subject to validations based on the artifact type: Remote: A checksum must be specified, and only protocols with transport-layer security are permitted. GCS: An object generation number must be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allow_insecure GoogleOsConfigGuestPolicies#allow_insecure}
        :param gcs: gcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gcs GoogleOsConfigGuestPolicies#gcs}
        :param remote: remote block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#remote GoogleOsConfigGuestPolicies#remote}
        '''
        if isinstance(gcs, dict):
            gcs = GoogleOsConfigGuestPoliciesRecipesArtifactsGcs(**gcs)
        if isinstance(remote, dict):
            remote = GoogleOsConfigGuestPoliciesRecipesArtifactsRemote(**remote)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifacts.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument allow_insecure", value=allow_insecure, expected_type=type_hints["allow_insecure"])
            check_type(argname="argument gcs", value=gcs, expected_type=type_hints["gcs"])
            check_type(argname="argument remote", value=remote, expected_type=type_hints["remote"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if allow_insecure is not None:
            self._values["allow_insecure"] = allow_insecure
        if gcs is not None:
            self._values["gcs"] = gcs
        if remote is not None:
            self._values["remote"] = remote

    @builtins.property
    def id(self) -> builtins.str:
        '''Id of the artifact, which the installation and update steps of this recipe can reference.

        Artifacts in a recipe cannot have the same id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#id GoogleOsConfigGuestPolicies#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_insecure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to false.

        When false, recipes are subject to validations based on the artifact type:
        Remote: A checksum must be specified, and only protocols with transport-layer security are permitted.
        GCS: An object generation number must be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allow_insecure GoogleOsConfigGuestPolicies#allow_insecure}
        '''
        result = self._values.get("allow_insecure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def gcs(self) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesArtifactsGcs"]:
        '''gcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#gcs GoogleOsConfigGuestPolicies#gcs}
        '''
        result = self._values.get("gcs")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesArtifactsGcs"], result)

    @builtins.property
    def remote(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesArtifactsRemote"]:
        '''remote block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#remote GoogleOsConfigGuestPolicies#remote}
        '''
        result = self._values.get("remote")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesArtifactsRemote"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesArtifacts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifactsGcs",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "generation": "generation", "object": "object"},
)
class GoogleOsConfigGuestPoliciesRecipesArtifactsGcs:
    def __init__(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        generation: typing.Optional[jsii.Number] = None,
        object: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Bucket of the Google Cloud Storage object. Given an example URL: https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be my-bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#bucket GoogleOsConfigGuestPolicies#bucket}
        :param generation: Must be provided if allowInsecure is false. Generation number of the Google Cloud Storage object. https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be 1234567. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#generation GoogleOsConfigGuestPolicies#generation}
        :param object: Name of the Google Cloud Storage object. Given an example URL: https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be foo/bar. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#object GoogleOsConfigGuestPolicies#object}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsGcs.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument generation", value=generation, expected_type=type_hints["generation"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if generation is not None:
            self._values["generation"] = generation
        if object is not None:
            self._values["object"] = object

    @builtins.property
    def bucket(self) -> typing.Optional[builtins.str]:
        '''Bucket of the Google Cloud Storage object. Given an example URL: https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be my-bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#bucket GoogleOsConfigGuestPolicies#bucket}
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def generation(self) -> typing.Optional[jsii.Number]:
        '''Must be provided if allowInsecure is false.

        Generation number of the Google Cloud Storage object.
        https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be 1234567.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#generation GoogleOsConfigGuestPolicies#generation}
        '''
        result = self._values.get("generation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def object(self) -> typing.Optional[builtins.str]:
        '''Name of the Google Cloud Storage object. Given an example URL: https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be foo/bar.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#object GoogleOsConfigGuestPolicies#object}
        '''
        result = self._values.get("object")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesArtifactsGcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBucket")
    def reset_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBucket", []))

    @jsii.member(jsii_name="resetGeneration")
    def reset_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeneration", []))

    @jsii.member(jsii_name="resetObject")
    def reset_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObject", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="generationInput")
    def generation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "generationInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @generation.setter
    def generation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference, "generation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generation", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsGcs]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsGcs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsGcs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesArtifactsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifactsList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesArtifacts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesArtifacts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesArtifacts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGcs")
    def put_gcs(
        self,
        *,
        bucket: typing.Optional[builtins.str] = None,
        generation: typing.Optional[jsii.Number] = None,
        object: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Bucket of the Google Cloud Storage object. Given an example URL: https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be my-bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#bucket GoogleOsConfigGuestPolicies#bucket}
        :param generation: Must be provided if allowInsecure is false. Generation number of the Google Cloud Storage object. https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be 1234567. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#generation GoogleOsConfigGuestPolicies#generation}
        :param object: Name of the Google Cloud Storage object. Given an example URL: https://storage.googleapis.com/my-bucket/foo/bar#1234567 this value would be foo/bar. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#object GoogleOsConfigGuestPolicies#object}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesArtifactsGcs(
            bucket=bucket, generation=generation, object=object
        )

        return typing.cast(None, jsii.invoke(self, "putGcs", [value]))

    @jsii.member(jsii_name="putRemote")
    def put_remote(
        self,
        *,
        check_sum: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param check_sum: Must be provided if allowInsecure is false. SHA256 checksum in hex format, to compare to the checksum of the artifact. If the checksum is not empty and it doesn't match the artifact then the recipe installation fails before running any of the steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#check_sum GoogleOsConfigGuestPolicies#check_sum}
        :param uri: URI from which to fetch the object. It should contain both the protocol and path following the format {protocol}://{location}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#uri GoogleOsConfigGuestPolicies#uri}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesArtifactsRemote(
            check_sum=check_sum, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putRemote", [value]))

    @jsii.member(jsii_name="resetAllowInsecure")
    def reset_allow_insecure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowInsecure", []))

    @jsii.member(jsii_name="resetGcs")
    def reset_gcs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcs", []))

    @jsii.member(jsii_name="resetRemote")
    def reset_remote(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemote", []))

    @builtins.property
    @jsii.member(jsii_name="gcs")
    def gcs(self) -> GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference, jsii.get(self, "gcs"))

    @builtins.property
    @jsii.member(jsii_name="remote")
    def remote(
        self,
    ) -> "GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference", jsii.get(self, "remote"))

    @builtins.property
    @jsii.member(jsii_name="allowInsecureInput")
    def allow_insecure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowInsecureInput"))

    @builtins.property
    @jsii.member(jsii_name="gcsInput")
    def gcs_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsGcs]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsGcs], jsii.get(self, "gcsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteInput")
    def remote_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesArtifactsRemote"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesArtifactsRemote"], jsii.get(self, "remoteInput"))

    @builtins.property
    @jsii.member(jsii_name="allowInsecure")
    def allow_insecure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowInsecure"))

    @allow_insecure.setter
    def allow_insecure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference, "allow_insecure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowInsecure", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesArtifacts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesArtifacts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesArtifacts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifactsRemote",
    jsii_struct_bases=[],
    name_mapping={"check_sum": "checkSum", "uri": "uri"},
)
class GoogleOsConfigGuestPoliciesRecipesArtifactsRemote:
    def __init__(
        self,
        *,
        check_sum: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param check_sum: Must be provided if allowInsecure is false. SHA256 checksum in hex format, to compare to the checksum of the artifact. If the checksum is not empty and it doesn't match the artifact then the recipe installation fails before running any of the steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#check_sum GoogleOsConfigGuestPolicies#check_sum}
        :param uri: URI from which to fetch the object. It should contain both the protocol and path following the format {protocol}://{location}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#uri GoogleOsConfigGuestPolicies#uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsRemote.__init__)
            check_type(argname="argument check_sum", value=check_sum, expected_type=type_hints["check_sum"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if check_sum is not None:
            self._values["check_sum"] = check_sum
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def check_sum(self) -> typing.Optional[builtins.str]:
        '''Must be provided if allowInsecure is false.

        SHA256 checksum in hex format, to compare to the checksum of the artifact.
        If the checksum is not empty and it doesn't match the artifact then the recipe installation fails before running any
        of the steps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#check_sum GoogleOsConfigGuestPolicies#check_sum}
        '''
        result = self._values.get("check_sum")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''URI from which to fetch the object. It should contain both the protocol and path following the format {protocol}://{location}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#uri GoogleOsConfigGuestPolicies#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesArtifactsRemote(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckSum")
    def reset_check_sum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckSum", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @builtins.property
    @jsii.member(jsii_name="checkSumInput")
    def check_sum_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkSumInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="checkSum")
    def check_sum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checkSum"))

    @check_sum.setter
    def check_sum(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference, "check_sum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkSum", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsRemote]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsRemote], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesArtifactsRemote],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallSteps",
    jsii_struct_bases=[],
    name_mapping={
        "archive_extraction": "archiveExtraction",
        "dpkg_installation": "dpkgInstallation",
        "file_copy": "fileCopy",
        "file_exec": "fileExec",
        "msi_installation": "msiInstallation",
        "rpm_installation": "rpmInstallation",
        "script_run": "scriptRun",
    },
)
class GoogleOsConfigGuestPoliciesRecipesInstallSteps:
    def __init__(
        self,
        *,
        archive_extraction: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction", typing.Dict[str, typing.Any]]] = None,
        dpkg_installation: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation", typing.Dict[str, typing.Any]]] = None,
        file_copy: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy", typing.Dict[str, typing.Any]]] = None,
        file_exec: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec", typing.Dict[str, typing.Any]]] = None,
        msi_installation: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation", typing.Dict[str, typing.Any]]] = None,
        rpm_installation: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation", typing.Dict[str, typing.Any]]] = None,
        script_run: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param archive_extraction: archive_extraction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_extraction GoogleOsConfigGuestPolicies#archive_extraction}
        :param dpkg_installation: dpkg_installation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#dpkg_installation GoogleOsConfigGuestPolicies#dpkg_installation}
        :param file_copy: file_copy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_copy GoogleOsConfigGuestPolicies#file_copy}
        :param file_exec: file_exec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_exec GoogleOsConfigGuestPolicies#file_exec}
        :param msi_installation: msi_installation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#msi_installation GoogleOsConfigGuestPolicies#msi_installation}
        :param rpm_installation: rpm_installation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#rpm_installation GoogleOsConfigGuestPolicies#rpm_installation}
        :param script_run: script_run block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script_run GoogleOsConfigGuestPolicies#script_run}
        '''
        if isinstance(archive_extraction, dict):
            archive_extraction = GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction(**archive_extraction)
        if isinstance(dpkg_installation, dict):
            dpkg_installation = GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation(**dpkg_installation)
        if isinstance(file_copy, dict):
            file_copy = GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy(**file_copy)
        if isinstance(file_exec, dict):
            file_exec = GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec(**file_exec)
        if isinstance(msi_installation, dict):
            msi_installation = GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation(**msi_installation)
        if isinstance(rpm_installation, dict):
            rpm_installation = GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation(**rpm_installation)
        if isinstance(script_run, dict):
            script_run = GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun(**script_run)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallSteps.__init__)
            check_type(argname="argument archive_extraction", value=archive_extraction, expected_type=type_hints["archive_extraction"])
            check_type(argname="argument dpkg_installation", value=dpkg_installation, expected_type=type_hints["dpkg_installation"])
            check_type(argname="argument file_copy", value=file_copy, expected_type=type_hints["file_copy"])
            check_type(argname="argument file_exec", value=file_exec, expected_type=type_hints["file_exec"])
            check_type(argname="argument msi_installation", value=msi_installation, expected_type=type_hints["msi_installation"])
            check_type(argname="argument rpm_installation", value=rpm_installation, expected_type=type_hints["rpm_installation"])
            check_type(argname="argument script_run", value=script_run, expected_type=type_hints["script_run"])
        self._values: typing.Dict[str, typing.Any] = {}
        if archive_extraction is not None:
            self._values["archive_extraction"] = archive_extraction
        if dpkg_installation is not None:
            self._values["dpkg_installation"] = dpkg_installation
        if file_copy is not None:
            self._values["file_copy"] = file_copy
        if file_exec is not None:
            self._values["file_exec"] = file_exec
        if msi_installation is not None:
            self._values["msi_installation"] = msi_installation
        if rpm_installation is not None:
            self._values["rpm_installation"] = rpm_installation
        if script_run is not None:
            self._values["script_run"] = script_run

    @builtins.property
    def archive_extraction(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction"]:
        '''archive_extraction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_extraction GoogleOsConfigGuestPolicies#archive_extraction}
        '''
        result = self._values.get("archive_extraction")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction"], result)

    @builtins.property
    def dpkg_installation(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation"]:
        '''dpkg_installation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#dpkg_installation GoogleOsConfigGuestPolicies#dpkg_installation}
        '''
        result = self._values.get("dpkg_installation")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation"], result)

    @builtins.property
    def file_copy(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy"]:
        '''file_copy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_copy GoogleOsConfigGuestPolicies#file_copy}
        '''
        result = self._values.get("file_copy")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy"], result)

    @builtins.property
    def file_exec(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec"]:
        '''file_exec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_exec GoogleOsConfigGuestPolicies#file_exec}
        '''
        result = self._values.get("file_exec")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec"], result)

    @builtins.property
    def msi_installation(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation"]:
        '''msi_installation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#msi_installation GoogleOsConfigGuestPolicies#msi_installation}
        '''
        result = self._values.get("msi_installation")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation"], result)

    @builtins.property
    def rpm_installation(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation"]:
        '''rpm_installation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#rpm_installation GoogleOsConfigGuestPolicies#rpm_installation}
        '''
        result = self._values.get("rpm_installation")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation"], result)

    @builtins.property
    def script_run(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun"]:
        '''script_run block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script_run GoogleOsConfigGuestPolicies#script_run}
        '''
        result = self._values.get("script_run")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_id": "artifactId",
        "type": "type",
        "destination": "destination",
    },
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction:
    def __init__(
        self,
        *,
        artifact_id: builtins.str,
        type: builtins.str,
        destination: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param type: The type of the archive to extract. Possible values: ["TAR", "TAR_GZIP", "TAR_BZIP", "TAR_LZMA", "TAR_XZ", "ZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#type GoogleOsConfigGuestPolicies#type}
        :param destination: Directory to extract archive to. Defaults to / on Linux or C:\\ on Windows. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
            "type": type,
        }
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the archive to extract. Possible values: ["TAR", "TAR_GZIP", "TAR_BZIP", "TAR_LZMA", "TAR_XZ", "ZIP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#type GoogleOsConfigGuestPolicies#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Directory to extract archive to. Defaults to / on Linux or C:\\ on Windows.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation",
    jsii_struct_bases=[],
    name_mapping={"artifact_id": "artifactId"},
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation:
    def __init__(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
        }

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_id": "artifactId",
        "destination": "destination",
        "overwrite": "overwrite",
        "permissions": "permissions",
    },
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy:
    def __init__(
        self,
        *,
        artifact_id: builtins.str,
        destination: builtins.str,
        overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param destination: The absolute path on the instance to put the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        :param overwrite: Whether to allow this step to overwrite existing files.If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#overwrite GoogleOsConfigGuestPolicies#overwrite}
        :param permissions: Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#permissions GoogleOsConfigGuestPolicies#permissions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
            "destination": destination,
        }
        if overwrite is not None:
            self._values["overwrite"] = overwrite
        if permissions is not None:
            self._values["permissions"] = permissions

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> builtins.str:
        '''The absolute path on the instance to put the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overwrite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to allow this step to overwrite existing files.If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#overwrite GoogleOsConfigGuestPolicies#overwrite}
        '''
        result = self._values.get("overwrite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility).

        Each digit represents a three bit
        number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one
        bit corresponds to the execute permission. Default behavior is 755.

        Below are some examples of permissions and their associated values:
        read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#permissions GoogleOsConfigGuestPolicies#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOverwrite")
    def reset_overwrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwrite", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteInput")
    def overwrite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overwriteInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="overwrite")
    def overwrite(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overwrite"))

    @overwrite.setter
    def overwrite(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference, "overwrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwrite", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_exit_codes": "allowedExitCodes",
        "args": "args",
        "artifact_id": "artifactId",
        "local_path": "localPath",
    },
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec:
    def __init__(
        self,
        *,
        allowed_exit_codes: typing.Optional[builtins.str] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        artifact_id: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_exit_codes: A list of possible return values that the program can return to indicate a success. Defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param args: Arguments to be passed to the provided executable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#args GoogleOsConfigGuestPolicies#args}
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param local_path: The absolute path of the file on the local filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#local_path GoogleOsConfigGuestPolicies#local_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec.__init__)
            check_type(argname="argument allowed_exit_codes", value=allowed_exit_codes, expected_type=type_hints["allowed_exit_codes"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument local_path", value=local_path, expected_type=type_hints["local_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_exit_codes is not None:
            self._values["allowed_exit_codes"] = allowed_exit_codes
        if args is not None:
            self._values["args"] = args
        if artifact_id is not None:
            self._values["artifact_id"] = artifact_id
        if local_path is not None:
            self._values["local_path"] = local_path

    @builtins.property
    def allowed_exit_codes(self) -> typing.Optional[builtins.str]:
        '''A list of possible return values that the program can return to indicate a success. Defaults to [0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        '''
        result = self._values.get("allowed_exit_codes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to be passed to the provided executable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#args GoogleOsConfigGuestPolicies#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def artifact_id(self) -> typing.Optional[builtins.str]:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_path(self) -> typing.Optional[builtins.str]:
        '''The absolute path of the file on the local filesystem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#local_path GoogleOsConfigGuestPolicies#local_path}
        '''
        result = self._values.get("local_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExitCodes")
    def reset_allowed_exit_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExitCodes", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetArtifactId")
    def reset_artifact_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactId", []))

    @jsii.member(jsii_name="resetLocalPath")
    def reset_local_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPath", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodesInput")
    def allowed_exit_codes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedExitCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="localPathInput")
    def local_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPathInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodes")
    def allowed_exit_codes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowedExitCodes"))

    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference, "allowed_exit_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExitCodes", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="localPath")
    def local_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPath"))

    @local_path.setter
    def local_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference, "local_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesInstallStepsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesInstallSteps]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesInstallSteps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesInstallSteps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_id": "artifactId",
        "allowed_exit_codes": "allowedExitCodes",
        "flags": "flags",
    },
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation:
    def __init__(
        self,
        *,
        artifact_id: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param flags: The flags to use when installing the MSI. Defaults to the install flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#flags GoogleOsConfigGuestPolicies#flags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument allowed_exit_codes", value=allowed_exit_codes, expected_type=type_hints["allowed_exit_codes"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
        }
        if allowed_exit_codes is not None:
            self._values["allowed_exit_codes"] = allowed_exit_codes
        if flags is not None:
            self._values["flags"] = flags

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_exit_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        '''
        result = self._values.get("allowed_exit_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The flags to use when installing the MSI. Defaults to the install flag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#flags GoogleOsConfigGuestPolicies#flags}
        '''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExitCodes")
    def reset_allowed_exit_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExitCodes", []))

    @jsii.member(jsii_name="resetFlags")
    def reset_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlags", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodesInput")
    def allowed_exit_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedExitCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="flagsInput")
    def flags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "flagsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodes")
    def allowed_exit_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedExitCodes"))

    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference, "allowed_exit_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExitCodes", value)

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "flags"))

    @flags.setter
    def flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference, "flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putArchiveExtraction")
    def put_archive_extraction(
        self,
        *,
        artifact_id: builtins.str,
        type: builtins.str,
        destination: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param type: The type of the archive to extract. Possible values: ["TAR", "TAR_GZIP", "TAR_BZIP", "TAR_LZMA", "TAR_XZ", "ZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#type GoogleOsConfigGuestPolicies#type}
        :param destination: Directory to extract archive to. Defaults to / on Linux or C:\\ on Windows. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction(
            artifact_id=artifact_id, type=type, destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putArchiveExtraction", [value]))

    @jsii.member(jsii_name="putDpkgInstallation")
    def put_dpkg_installation(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation(
            artifact_id=artifact_id
        )

        return typing.cast(None, jsii.invoke(self, "putDpkgInstallation", [value]))

    @jsii.member(jsii_name="putFileCopy")
    def put_file_copy(
        self,
        *,
        artifact_id: builtins.str,
        destination: builtins.str,
        overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param destination: The absolute path on the instance to put the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        :param overwrite: Whether to allow this step to overwrite existing files.If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#overwrite GoogleOsConfigGuestPolicies#overwrite}
        :param permissions: Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#permissions GoogleOsConfigGuestPolicies#permissions}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy(
            artifact_id=artifact_id,
            destination=destination,
            overwrite=overwrite,
            permissions=permissions,
        )

        return typing.cast(None, jsii.invoke(self, "putFileCopy", [value]))

    @jsii.member(jsii_name="putFileExec")
    def put_file_exec(
        self,
        *,
        allowed_exit_codes: typing.Optional[builtins.str] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        artifact_id: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_exit_codes: A list of possible return values that the program can return to indicate a success. Defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param args: Arguments to be passed to the provided executable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#args GoogleOsConfigGuestPolicies#args}
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param local_path: The absolute path of the file on the local filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#local_path GoogleOsConfigGuestPolicies#local_path}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec(
            allowed_exit_codes=allowed_exit_codes,
            args=args,
            artifact_id=artifact_id,
            local_path=local_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFileExec", [value]))

    @jsii.member(jsii_name="putMsiInstallation")
    def put_msi_installation(
        self,
        *,
        artifact_id: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param flags: The flags to use when installing the MSI. Defaults to the install flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#flags GoogleOsConfigGuestPolicies#flags}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation(
            artifact_id=artifact_id, allowed_exit_codes=allowed_exit_codes, flags=flags
        )

        return typing.cast(None, jsii.invoke(self, "putMsiInstallation", [value]))

    @jsii.member(jsii_name="putRpmInstallation")
    def put_rpm_installation(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation(
            artifact_id=artifact_id
        )

        return typing.cast(None, jsii.invoke(self, "putRpmInstallation", [value]))

    @jsii.member(jsii_name="putScriptRun")
    def put_script_run(
        self,
        *,
        script: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        interpreter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param script: The shell script to be executed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script GoogleOsConfigGuestPolicies#script}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#interpreter GoogleOsConfigGuestPolicies#interpreter}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun(
            script=script,
            allowed_exit_codes=allowed_exit_codes,
            interpreter=interpreter,
        )

        return typing.cast(None, jsii.invoke(self, "putScriptRun", [value]))

    @jsii.member(jsii_name="resetArchiveExtraction")
    def reset_archive_extraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveExtraction", []))

    @jsii.member(jsii_name="resetDpkgInstallation")
    def reset_dpkg_installation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDpkgInstallation", []))

    @jsii.member(jsii_name="resetFileCopy")
    def reset_file_copy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileCopy", []))

    @jsii.member(jsii_name="resetFileExec")
    def reset_file_exec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileExec", []))

    @jsii.member(jsii_name="resetMsiInstallation")
    def reset_msi_installation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsiInstallation", []))

    @jsii.member(jsii_name="resetRpmInstallation")
    def reset_rpm_installation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRpmInstallation", []))

    @jsii.member(jsii_name="resetScriptRun")
    def reset_script_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptRun", []))

    @builtins.property
    @jsii.member(jsii_name="archiveExtraction")
    def archive_extraction(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference, jsii.get(self, "archiveExtraction"))

    @builtins.property
    @jsii.member(jsii_name="dpkgInstallation")
    def dpkg_installation(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference, jsii.get(self, "dpkgInstallation"))

    @builtins.property
    @jsii.member(jsii_name="fileCopy")
    def file_copy(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference, jsii.get(self, "fileCopy"))

    @builtins.property
    @jsii.member(jsii_name="fileExec")
    def file_exec(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference, jsii.get(self, "fileExec"))

    @builtins.property
    @jsii.member(jsii_name="msiInstallation")
    def msi_installation(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference, jsii.get(self, "msiInstallation"))

    @builtins.property
    @jsii.member(jsii_name="rpmInstallation")
    def rpm_installation(
        self,
    ) -> "GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference", jsii.get(self, "rpmInstallation"))

    @builtins.property
    @jsii.member(jsii_name="scriptRun")
    def script_run(
        self,
    ) -> "GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference", jsii.get(self, "scriptRun"))

    @builtins.property
    @jsii.member(jsii_name="archiveExtractionInput")
    def archive_extraction_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction], jsii.get(self, "archiveExtractionInput"))

    @builtins.property
    @jsii.member(jsii_name="dpkgInstallationInput")
    def dpkg_installation_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation], jsii.get(self, "dpkgInstallationInput"))

    @builtins.property
    @jsii.member(jsii_name="fileCopyInput")
    def file_copy_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy], jsii.get(self, "fileCopyInput"))

    @builtins.property
    @jsii.member(jsii_name="fileExecInput")
    def file_exec_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec], jsii.get(self, "fileExecInput"))

    @builtins.property
    @jsii.member(jsii_name="msiInstallationInput")
    def msi_installation_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation], jsii.get(self, "msiInstallationInput"))

    @builtins.property
    @jsii.member(jsii_name="rpmInstallationInput")
    def rpm_installation_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation"], jsii.get(self, "rpmInstallationInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptRunInput")
    def script_run_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun"], jsii.get(self, "scriptRunInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesInstallSteps, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesInstallSteps, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesInstallSteps, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation",
    jsii_struct_bases=[],
    name_mapping={"artifact_id": "artifactId"},
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation:
    def __init__(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
        }

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun",
    jsii_struct_bases=[],
    name_mapping={
        "script": "script",
        "allowed_exit_codes": "allowedExitCodes",
        "interpreter": "interpreter",
    },
)
class GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun:
    def __init__(
        self,
        *,
        script: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        interpreter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param script: The shell script to be executed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script GoogleOsConfigGuestPolicies#script}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#interpreter GoogleOsConfigGuestPolicies#interpreter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun.__init__)
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument allowed_exit_codes", value=allowed_exit_codes, expected_type=type_hints["allowed_exit_codes"])
            check_type(argname="argument interpreter", value=interpreter, expected_type=type_hints["interpreter"])
        self._values: typing.Dict[str, typing.Any] = {
            "script": script,
        }
        if allowed_exit_codes is not None:
            self._values["allowed_exit_codes"] = allowed_exit_codes
        if interpreter is not None:
            self._values["interpreter"] = interpreter

    @builtins.property
    def script(self) -> builtins.str:
        '''The shell script to be executed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script GoogleOsConfigGuestPolicies#script}
        '''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_exit_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        '''
        result = self._values.get("allowed_exit_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def interpreter(self) -> typing.Optional[builtins.str]:
        '''The script interpreter to use to run the script.

        If no interpreter is specified the script is executed directly,
        which likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#interpreter GoogleOsConfigGuestPolicies#interpreter}
        '''
        result = self._values.get("interpreter")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExitCodes")
    def reset_allowed_exit_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExitCodes", []))

    @jsii.member(jsii_name="resetInterpreter")
    def reset_interpreter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterpreter", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodesInput")
    def allowed_exit_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedExitCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="interpreterInput")
    def interpreter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interpreterInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodes")
    def allowed_exit_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedExitCodes"))

    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference, "allowed_exit_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExitCodes", value)

    @builtins.property
    @jsii.member(jsii_name="interpreter")
    def interpreter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interpreter"))

    @interpreter.setter
    def interpreter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference, "interpreter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interpreter", value)

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference, "script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesRecipesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putArtifacts")
    def put_artifacts(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleOsConfigGuestPoliciesRecipesArtifacts, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesOutputReference.put_artifacts)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putArtifacts", [value]))

    @jsii.member(jsii_name="putInstallSteps")
    def put_install_steps(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleOsConfigGuestPoliciesRecipesInstallSteps, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesOutputReference.put_install_steps)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstallSteps", [value]))

    @jsii.member(jsii_name="putUpdateSteps")
    def put_update_steps(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateSteps", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesOutputReference.put_update_steps)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUpdateSteps", [value]))

    @jsii.member(jsii_name="resetArtifacts")
    def reset_artifacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifacts", []))

    @jsii.member(jsii_name="resetDesiredState")
    def reset_desired_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredState", []))

    @jsii.member(jsii_name="resetInstallSteps")
    def reset_install_steps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstallSteps", []))

    @jsii.member(jsii_name="resetUpdateSteps")
    def reset_update_steps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateSteps", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> GoogleOsConfigGuestPoliciesRecipesArtifactsList:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesArtifactsList, jsii.get(self, "artifacts"))

    @builtins.property
    @jsii.member(jsii_name="installSteps")
    def install_steps(self) -> GoogleOsConfigGuestPoliciesRecipesInstallStepsList:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesInstallStepsList, jsii.get(self, "installSteps"))

    @builtins.property
    @jsii.member(jsii_name="updateSteps")
    def update_steps(self) -> "GoogleOsConfigGuestPoliciesRecipesUpdateStepsList":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesUpdateStepsList", jsii.get(self, "updateSteps"))

    @builtins.property
    @jsii.member(jsii_name="artifactsInput")
    def artifacts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesArtifacts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesArtifacts]]], jsii.get(self, "artifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="installStepsInput")
    def install_steps_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesInstallSteps]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesInstallSteps]]], jsii.get(self, "installStepsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="updateStepsInput")
    def update_steps_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesUpdateSteps"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleOsConfigGuestPoliciesRecipesUpdateSteps"]]], jsii.get(self, "updateStepsInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesOutputReference, "desired_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateSteps",
    jsii_struct_bases=[],
    name_mapping={
        "archive_extraction": "archiveExtraction",
        "dpkg_installation": "dpkgInstallation",
        "file_copy": "fileCopy",
        "file_exec": "fileExec",
        "msi_installation": "msiInstallation",
        "rpm_installation": "rpmInstallation",
        "script_run": "scriptRun",
    },
)
class GoogleOsConfigGuestPoliciesRecipesUpdateSteps:
    def __init__(
        self,
        *,
        archive_extraction: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction", typing.Dict[str, typing.Any]]] = None,
        dpkg_installation: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation", typing.Dict[str, typing.Any]]] = None,
        file_copy: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy", typing.Dict[str, typing.Any]]] = None,
        file_exec: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec", typing.Dict[str, typing.Any]]] = None,
        msi_installation: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation", typing.Dict[str, typing.Any]]] = None,
        rpm_installation: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation", typing.Dict[str, typing.Any]]] = None,
        script_run: typing.Optional[typing.Union["GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param archive_extraction: archive_extraction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_extraction GoogleOsConfigGuestPolicies#archive_extraction}
        :param dpkg_installation: dpkg_installation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#dpkg_installation GoogleOsConfigGuestPolicies#dpkg_installation}
        :param file_copy: file_copy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_copy GoogleOsConfigGuestPolicies#file_copy}
        :param file_exec: file_exec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_exec GoogleOsConfigGuestPolicies#file_exec}
        :param msi_installation: msi_installation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#msi_installation GoogleOsConfigGuestPolicies#msi_installation}
        :param rpm_installation: rpm_installation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#rpm_installation GoogleOsConfigGuestPolicies#rpm_installation}
        :param script_run: script_run block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script_run GoogleOsConfigGuestPolicies#script_run}
        '''
        if isinstance(archive_extraction, dict):
            archive_extraction = GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction(**archive_extraction)
        if isinstance(dpkg_installation, dict):
            dpkg_installation = GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation(**dpkg_installation)
        if isinstance(file_copy, dict):
            file_copy = GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy(**file_copy)
        if isinstance(file_exec, dict):
            file_exec = GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec(**file_exec)
        if isinstance(msi_installation, dict):
            msi_installation = GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation(**msi_installation)
        if isinstance(rpm_installation, dict):
            rpm_installation = GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation(**rpm_installation)
        if isinstance(script_run, dict):
            script_run = GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun(**script_run)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateSteps.__init__)
            check_type(argname="argument archive_extraction", value=archive_extraction, expected_type=type_hints["archive_extraction"])
            check_type(argname="argument dpkg_installation", value=dpkg_installation, expected_type=type_hints["dpkg_installation"])
            check_type(argname="argument file_copy", value=file_copy, expected_type=type_hints["file_copy"])
            check_type(argname="argument file_exec", value=file_exec, expected_type=type_hints["file_exec"])
            check_type(argname="argument msi_installation", value=msi_installation, expected_type=type_hints["msi_installation"])
            check_type(argname="argument rpm_installation", value=rpm_installation, expected_type=type_hints["rpm_installation"])
            check_type(argname="argument script_run", value=script_run, expected_type=type_hints["script_run"])
        self._values: typing.Dict[str, typing.Any] = {}
        if archive_extraction is not None:
            self._values["archive_extraction"] = archive_extraction
        if dpkg_installation is not None:
            self._values["dpkg_installation"] = dpkg_installation
        if file_copy is not None:
            self._values["file_copy"] = file_copy
        if file_exec is not None:
            self._values["file_exec"] = file_exec
        if msi_installation is not None:
            self._values["msi_installation"] = msi_installation
        if rpm_installation is not None:
            self._values["rpm_installation"] = rpm_installation
        if script_run is not None:
            self._values["script_run"] = script_run

    @builtins.property
    def archive_extraction(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction"]:
        '''archive_extraction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#archive_extraction GoogleOsConfigGuestPolicies#archive_extraction}
        '''
        result = self._values.get("archive_extraction")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction"], result)

    @builtins.property
    def dpkg_installation(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation"]:
        '''dpkg_installation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#dpkg_installation GoogleOsConfigGuestPolicies#dpkg_installation}
        '''
        result = self._values.get("dpkg_installation")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation"], result)

    @builtins.property
    def file_copy(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy"]:
        '''file_copy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_copy GoogleOsConfigGuestPolicies#file_copy}
        '''
        result = self._values.get("file_copy")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy"], result)

    @builtins.property
    def file_exec(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec"]:
        '''file_exec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#file_exec GoogleOsConfigGuestPolicies#file_exec}
        '''
        result = self._values.get("file_exec")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec"], result)

    @builtins.property
    def msi_installation(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation"]:
        '''msi_installation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#msi_installation GoogleOsConfigGuestPolicies#msi_installation}
        '''
        result = self._values.get("msi_installation")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation"], result)

    @builtins.property
    def rpm_installation(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation"]:
        '''rpm_installation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#rpm_installation GoogleOsConfigGuestPolicies#rpm_installation}
        '''
        result = self._values.get("rpm_installation")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation"], result)

    @builtins.property
    def script_run(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun"]:
        '''script_run block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script_run GoogleOsConfigGuestPolicies#script_run}
        '''
        result = self._values.get("script_run")
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateSteps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_id": "artifactId",
        "type": "type",
        "destination": "destination",
    },
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction:
    def __init__(
        self,
        *,
        artifact_id: builtins.str,
        type: builtins.str,
        destination: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param type: The type of the archive to extract. Possible values: ["TAR", "TAR_GZIP", "TAR_BZIP", "TAR_LZMA", "TAR_XZ", "ZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#type GoogleOsConfigGuestPolicies#type}
        :param destination: Directory to extract archive to. Defaults to / on Linux or C:\\ on Windows. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
            "type": type,
        }
        if destination is not None:
            self._values["destination"] = destination

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the archive to extract. Possible values: ["TAR", "TAR_GZIP", "TAR_BZIP", "TAR_LZMA", "TAR_XZ", "ZIP"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#type GoogleOsConfigGuestPolicies#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''Directory to extract archive to. Defaults to / on Linux or C:\\ on Windows.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestination")
    def reset_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestination", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation",
    jsii_struct_bases=[],
    name_mapping={"artifact_id": "artifactId"},
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation:
    def __init__(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
        }

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_id": "artifactId",
        "destination": "destination",
        "overwrite": "overwrite",
        "permissions": "permissions",
    },
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy:
    def __init__(
        self,
        *,
        artifact_id: builtins.str,
        destination: builtins.str,
        overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param destination: The absolute path on the instance to put the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        :param overwrite: Whether to allow this step to overwrite existing files.If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#overwrite GoogleOsConfigGuestPolicies#overwrite}
        :param permissions: Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#permissions GoogleOsConfigGuestPolicies#permissions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
            "destination": destination,
        }
        if overwrite is not None:
            self._values["overwrite"] = overwrite
        if permissions is not None:
            self._values["permissions"] = permissions

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination(self) -> builtins.str:
        '''The absolute path on the instance to put the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overwrite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to allow this step to overwrite existing files.If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#overwrite GoogleOsConfigGuestPolicies#overwrite}
        '''
        result = self._values.get("overwrite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility).

        Each digit represents a three bit
        number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one
        bit corresponds to the execute permission. Default behavior is 755.

        Below are some examples of permissions and their associated values:
        read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#permissions GoogleOsConfigGuestPolicies#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOverwrite")
    def reset_overwrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwrite", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteInput")
    def overwrite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overwriteInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="overwrite")
    def overwrite(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overwrite"))

    @overwrite.setter
    def overwrite(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference, "overwrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwrite", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_exit_codes": "allowedExitCodes",
        "args": "args",
        "artifact_id": "artifactId",
        "local_path": "localPath",
    },
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec:
    def __init__(
        self,
        *,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        artifact_id: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_exit_codes: A list of possible return values that the program can return to indicate a success. Defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param args: Arguments to be passed to the provided executable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#args GoogleOsConfigGuestPolicies#args}
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param local_path: The absolute path of the file on the local filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#local_path GoogleOsConfigGuestPolicies#local_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec.__init__)
            check_type(argname="argument allowed_exit_codes", value=allowed_exit_codes, expected_type=type_hints["allowed_exit_codes"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument local_path", value=local_path, expected_type=type_hints["local_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_exit_codes is not None:
            self._values["allowed_exit_codes"] = allowed_exit_codes
        if args is not None:
            self._values["args"] = args
        if artifact_id is not None:
            self._values["artifact_id"] = artifact_id
        if local_path is not None:
            self._values["local_path"] = local_path

    @builtins.property
    def allowed_exit_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''A list of possible return values that the program can return to indicate a success. Defaults to [0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        '''
        result = self._values.get("allowed_exit_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to be passed to the provided executable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#args GoogleOsConfigGuestPolicies#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def artifact_id(self) -> typing.Optional[builtins.str]:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_path(self) -> typing.Optional[builtins.str]:
        '''The absolute path of the file on the local filesystem.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#local_path GoogleOsConfigGuestPolicies#local_path}
        '''
        result = self._values.get("local_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExitCodes")
    def reset_allowed_exit_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExitCodes", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetArtifactId")
    def reset_artifact_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifactId", []))

    @jsii.member(jsii_name="resetLocalPath")
    def reset_local_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalPath", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodesInput")
    def allowed_exit_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedExitCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="localPathInput")
    def local_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localPathInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodes")
    def allowed_exit_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedExitCodes"))

    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference, "allowed_exit_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExitCodes", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="localPath")
    def local_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localPath"))

    @local_path.setter
    def local_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference, "local_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsList",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesUpdateSteps]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesUpdateSteps]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleOsConfigGuestPoliciesRecipesUpdateSteps]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation",
    jsii_struct_bases=[],
    name_mapping={
        "artifact_id": "artifactId",
        "allowed_exit_codes": "allowedExitCodes",
        "flags": "flags",
    },
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation:
    def __init__(
        self,
        *,
        artifact_id: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param flags: The flags to use when installing the MSI. Defaults to the install flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#flags GoogleOsConfigGuestPolicies#flags}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
            check_type(argname="argument allowed_exit_codes", value=allowed_exit_codes, expected_type=type_hints["allowed_exit_codes"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
        }
        if allowed_exit_codes is not None:
            self._values["allowed_exit_codes"] = allowed_exit_codes
        if flags is not None:
            self._values["flags"] = flags

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_exit_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        '''
        result = self._values.get("allowed_exit_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def flags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The flags to use when installing the MSI. Defaults to the install flag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#flags GoogleOsConfigGuestPolicies#flags}
        '''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExitCodes")
    def reset_allowed_exit_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExitCodes", []))

    @jsii.member(jsii_name="resetFlags")
    def reset_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlags", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodesInput")
    def allowed_exit_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedExitCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="flagsInput")
    def flags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "flagsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodes")
    def allowed_exit_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedExitCodes"))

    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference, "allowed_exit_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExitCodes", value)

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "flags"))

    @flags.setter
    def flags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference, "flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putArchiveExtraction")
    def put_archive_extraction(
        self,
        *,
        artifact_id: builtins.str,
        type: builtins.str,
        destination: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param type: The type of the archive to extract. Possible values: ["TAR", "TAR_GZIP", "TAR_BZIP", "TAR_LZMA", "TAR_XZ", "ZIP"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#type GoogleOsConfigGuestPolicies#type}
        :param destination: Directory to extract archive to. Defaults to / on Linux or C:\\ on Windows. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction(
            artifact_id=artifact_id, type=type, destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putArchiveExtraction", [value]))

    @jsii.member(jsii_name="putDpkgInstallation")
    def put_dpkg_installation(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation(
            artifact_id=artifact_id
        )

        return typing.cast(None, jsii.invoke(self, "putDpkgInstallation", [value]))

    @jsii.member(jsii_name="putFileCopy")
    def put_file_copy(
        self,
        *,
        artifact_id: builtins.str,
        destination: builtins.str,
        overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param destination: The absolute path on the instance to put the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#destination GoogleOsConfigGuestPolicies#destination}
        :param overwrite: Whether to allow this step to overwrite existing files.If this is false and the file already exists the file is not overwritten and the step is considered a success. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#overwrite GoogleOsConfigGuestPolicies#overwrite}
        :param permissions: Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#permissions GoogleOsConfigGuestPolicies#permissions}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy(
            artifact_id=artifact_id,
            destination=destination,
            overwrite=overwrite,
            permissions=permissions,
        )

        return typing.cast(None, jsii.invoke(self, "putFileCopy", [value]))

    @jsii.member(jsii_name="putFileExec")
    def put_file_exec(
        self,
        *,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        artifact_id: typing.Optional[builtins.str] = None,
        local_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_exit_codes: A list of possible return values that the program can return to indicate a success. Defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param args: Arguments to be passed to the provided executable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#args GoogleOsConfigGuestPolicies#args}
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param local_path: The absolute path of the file on the local filesystem. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#local_path GoogleOsConfigGuestPolicies#local_path}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec(
            allowed_exit_codes=allowed_exit_codes,
            args=args,
            artifact_id=artifact_id,
            local_path=local_path,
        )

        return typing.cast(None, jsii.invoke(self, "putFileExec", [value]))

    @jsii.member(jsii_name="putMsiInstallation")
    def put_msi_installation(
        self,
        *,
        artifact_id: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        flags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param flags: The flags to use when installing the MSI. Defaults to the install flag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#flags GoogleOsConfigGuestPolicies#flags}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation(
            artifact_id=artifact_id, allowed_exit_codes=allowed_exit_codes, flags=flags
        )

        return typing.cast(None, jsii.invoke(self, "putMsiInstallation", [value]))

    @jsii.member(jsii_name="putRpmInstallation")
    def put_rpm_installation(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation(
            artifact_id=artifact_id
        )

        return typing.cast(None, jsii.invoke(self, "putRpmInstallation", [value]))

    @jsii.member(jsii_name="putScriptRun")
    def put_script_run(
        self,
        *,
        script: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        interpreter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param script: The shell script to be executed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script GoogleOsConfigGuestPolicies#script}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#interpreter GoogleOsConfigGuestPolicies#interpreter}
        '''
        value = GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun(
            script=script,
            allowed_exit_codes=allowed_exit_codes,
            interpreter=interpreter,
        )

        return typing.cast(None, jsii.invoke(self, "putScriptRun", [value]))

    @jsii.member(jsii_name="resetArchiveExtraction")
    def reset_archive_extraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveExtraction", []))

    @jsii.member(jsii_name="resetDpkgInstallation")
    def reset_dpkg_installation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDpkgInstallation", []))

    @jsii.member(jsii_name="resetFileCopy")
    def reset_file_copy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileCopy", []))

    @jsii.member(jsii_name="resetFileExec")
    def reset_file_exec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileExec", []))

    @jsii.member(jsii_name="resetMsiInstallation")
    def reset_msi_installation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsiInstallation", []))

    @jsii.member(jsii_name="resetRpmInstallation")
    def reset_rpm_installation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRpmInstallation", []))

    @jsii.member(jsii_name="resetScriptRun")
    def reset_script_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptRun", []))

    @builtins.property
    @jsii.member(jsii_name="archiveExtraction")
    def archive_extraction(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference, jsii.get(self, "archiveExtraction"))

    @builtins.property
    @jsii.member(jsii_name="dpkgInstallation")
    def dpkg_installation(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference, jsii.get(self, "dpkgInstallation"))

    @builtins.property
    @jsii.member(jsii_name="fileCopy")
    def file_copy(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference, jsii.get(self, "fileCopy"))

    @builtins.property
    @jsii.member(jsii_name="fileExec")
    def file_exec(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference, jsii.get(self, "fileExec"))

    @builtins.property
    @jsii.member(jsii_name="msiInstallation")
    def msi_installation(
        self,
    ) -> GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference:
        return typing.cast(GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference, jsii.get(self, "msiInstallation"))

    @builtins.property
    @jsii.member(jsii_name="rpmInstallation")
    def rpm_installation(
        self,
    ) -> "GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference", jsii.get(self, "rpmInstallation"))

    @builtins.property
    @jsii.member(jsii_name="scriptRun")
    def script_run(
        self,
    ) -> "GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference":
        return typing.cast("GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference", jsii.get(self, "scriptRun"))

    @builtins.property
    @jsii.member(jsii_name="archiveExtractionInput")
    def archive_extraction_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction], jsii.get(self, "archiveExtractionInput"))

    @builtins.property
    @jsii.member(jsii_name="dpkgInstallationInput")
    def dpkg_installation_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation], jsii.get(self, "dpkgInstallationInput"))

    @builtins.property
    @jsii.member(jsii_name="fileCopyInput")
    def file_copy_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy], jsii.get(self, "fileCopyInput"))

    @builtins.property
    @jsii.member(jsii_name="fileExecInput")
    def file_exec_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec], jsii.get(self, "fileExecInput"))

    @builtins.property
    @jsii.member(jsii_name="msiInstallationInput")
    def msi_installation_input(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation], jsii.get(self, "msiInstallationInput"))

    @builtins.property
    @jsii.member(jsii_name="rpmInstallationInput")
    def rpm_installation_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation"], jsii.get(self, "rpmInstallationInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptRunInput")
    def script_run_input(
        self,
    ) -> typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun"]:
        return typing.cast(typing.Optional["GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun"], jsii.get(self, "scriptRunInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesUpdateSteps, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesUpdateSteps, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesRecipesUpdateSteps, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation",
    jsii_struct_bases=[],
    name_mapping={"artifact_id": "artifactId"},
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation:
    def __init__(self, *, artifact_id: builtins.str) -> None:
        '''
        :param artifact_id: The id of the relevant artifact in the recipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation.__init__)
            check_type(argname="argument artifact_id", value=artifact_id, expected_type=type_hints["artifact_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "artifact_id": artifact_id,
        }

    @builtins.property
    def artifact_id(self) -> builtins.str:
        '''The id of the relevant artifact in the recipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#artifact_id GoogleOsConfigGuestPolicies#artifact_id}
        '''
        result = self._values.get("artifact_id")
        assert result is not None, "Required property 'artifact_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="artifactIdInput")
    def artifact_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactIdInput"))

    @builtins.property
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @artifact_id.setter
    def artifact_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference, "artifact_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "artifactId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun",
    jsii_struct_bases=[],
    name_mapping={
        "script": "script",
        "allowed_exit_codes": "allowedExitCodes",
        "interpreter": "interpreter",
    },
)
class GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun:
    def __init__(
        self,
        *,
        script: builtins.str,
        allowed_exit_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        interpreter: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param script: The shell script to be executed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script GoogleOsConfigGuestPolicies#script}
        :param allowed_exit_codes: Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        :param interpreter: The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#interpreter GoogleOsConfigGuestPolicies#interpreter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun.__init__)
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument allowed_exit_codes", value=allowed_exit_codes, expected_type=type_hints["allowed_exit_codes"])
            check_type(argname="argument interpreter", value=interpreter, expected_type=type_hints["interpreter"])
        self._values: typing.Dict[str, typing.Any] = {
            "script": script,
        }
        if allowed_exit_codes is not None:
            self._values["allowed_exit_codes"] = allowed_exit_codes
        if interpreter is not None:
            self._values["interpreter"] = interpreter

    @builtins.property
    def script(self) -> builtins.str:
        '''The shell script to be executed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#script GoogleOsConfigGuestPolicies#script}
        '''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_exit_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#allowed_exit_codes GoogleOsConfigGuestPolicies#allowed_exit_codes}
        '''
        result = self._values.get("allowed_exit_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def interpreter(self) -> typing.Optional[builtins.str]:
        '''The script interpreter to use to run the script.

        If no interpreter is specified the script is executed directly,
        which likely only succeed for scripts with shebang lines. Possible values: ["SHELL", "POWERSHELL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#interpreter GoogleOsConfigGuestPolicies#interpreter}
        '''
        result = self._values.get("interpreter")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowedExitCodes")
    def reset_allowed_exit_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedExitCodes", []))

    @jsii.member(jsii_name="resetInterpreter")
    def reset_interpreter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterpreter", []))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodesInput")
    def allowed_exit_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "allowedExitCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="interpreterInput")
    def interpreter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interpreterInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptInput")
    def script_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedExitCodes")
    def allowed_exit_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "allowedExitCodes"))

    @allowed_exit_codes.setter
    def allowed_exit_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference, "allowed_exit_codes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedExitCodes", value)

    @builtins.property
    @jsii.member(jsii_name="interpreter")
    def interpreter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interpreter"))

    @interpreter.setter
    def interpreter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference, "interpreter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interpreter", value)

    @builtins.property
    @jsii.member(jsii_name="script")
    def script(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "script"))

    @script.setter
    def script(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference, "script").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "script", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun]:
        return typing.cast(typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleOsConfigGuestPoliciesTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#create GoogleOsConfigGuestPolicies#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#delete GoogleOsConfigGuestPolicies#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#update GoogleOsConfigGuestPolicies#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#create GoogleOsConfigGuestPolicies#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#delete GoogleOsConfigGuestPolicies#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_os_config_guest_policies#update GoogleOsConfigGuestPolicies#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleOsConfigGuestPoliciesTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleOsConfigGuestPoliciesTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleOsConfigGuestPolicies.GoogleOsConfigGuestPoliciesTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleOsConfigGuestPoliciesTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleOsConfigGuestPoliciesTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleOsConfigGuestPoliciesTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleOsConfigGuestPolicies",
    "GoogleOsConfigGuestPoliciesAssignment",
    "GoogleOsConfigGuestPoliciesAssignmentGroupLabels",
    "GoogleOsConfigGuestPoliciesAssignmentGroupLabelsList",
    "GoogleOsConfigGuestPoliciesAssignmentGroupLabelsOutputReference",
    "GoogleOsConfigGuestPoliciesAssignmentOsTypes",
    "GoogleOsConfigGuestPoliciesAssignmentOsTypesList",
    "GoogleOsConfigGuestPoliciesAssignmentOsTypesOutputReference",
    "GoogleOsConfigGuestPoliciesAssignmentOutputReference",
    "GoogleOsConfigGuestPoliciesConfig",
    "GoogleOsConfigGuestPoliciesPackageRepositories",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesApt",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesAptOutputReference",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesGoo",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesGooOutputReference",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesList",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesOutputReference",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesYum",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesYumOutputReference",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesZypper",
    "GoogleOsConfigGuestPoliciesPackageRepositoriesZypperOutputReference",
    "GoogleOsConfigGuestPoliciesPackages",
    "GoogleOsConfigGuestPoliciesPackagesList",
    "GoogleOsConfigGuestPoliciesPackagesOutputReference",
    "GoogleOsConfigGuestPoliciesRecipes",
    "GoogleOsConfigGuestPoliciesRecipesArtifacts",
    "GoogleOsConfigGuestPoliciesRecipesArtifactsGcs",
    "GoogleOsConfigGuestPoliciesRecipesArtifactsGcsOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesArtifactsList",
    "GoogleOsConfigGuestPoliciesRecipesArtifactsOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesArtifactsRemote",
    "GoogleOsConfigGuestPoliciesRecipesArtifactsRemoteOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallSteps",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtraction",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsArchiveExtractionOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallation",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsDpkgInstallationOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopy",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsFileCopyOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExec",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsFileExecOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsList",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallation",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsMsiInstallationOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallation",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsRpmInstallationOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRun",
    "GoogleOsConfigGuestPoliciesRecipesInstallStepsScriptRunOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesList",
    "GoogleOsConfigGuestPoliciesRecipesOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateSteps",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtraction",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsArchiveExtractionOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallation",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsDpkgInstallationOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopy",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileCopyOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExec",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsFileExecOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsList",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallation",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsMsiInstallationOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallation",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsRpmInstallationOutputReference",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRun",
    "GoogleOsConfigGuestPoliciesRecipesUpdateStepsScriptRunOutputReference",
    "GoogleOsConfigGuestPoliciesTimeouts",
    "GoogleOsConfigGuestPoliciesTimeoutsOutputReference",
]

publication.publish()
