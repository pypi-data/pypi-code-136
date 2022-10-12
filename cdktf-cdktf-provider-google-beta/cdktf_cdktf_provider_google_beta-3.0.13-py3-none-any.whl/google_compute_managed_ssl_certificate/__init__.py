'''
# `google_compute_managed_ssl_certificate`

Refer to the Terraform Registory for docs: [`google_compute_managed_ssl_certificate`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate).
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


class GoogleComputeManagedSslCertificate(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeManagedSslCertificate.GoogleComputeManagedSslCertificate",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate google_compute_managed_ssl_certificate}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        certificate_id: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union["GoogleComputeManagedSslCertificateManaged", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeManagedSslCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate google_compute_managed_ssl_certificate} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param certificate_id: The unique identifier for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#certificate_id GoogleComputeManagedSslCertificate#certificate_id}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#description GoogleComputeManagedSslCertificate#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#id GoogleComputeManagedSslCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param managed: managed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#managed GoogleComputeManagedSslCertificate#managed}
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. These are in the same namespace as the managed SSL certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#name GoogleComputeManagedSslCertificate#name}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#project GoogleComputeManagedSslCertificate#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#timeouts GoogleComputeManagedSslCertificate#timeouts}
        :param type: Enum field whose value is always 'MANAGED' - used to signal to the API which type this is. Default value: "MANAGED" Possible values: ["MANAGED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#type GoogleComputeManagedSslCertificate#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeManagedSslCertificate.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeManagedSslCertificateConfig(
            certificate_id=certificate_id,
            description=description,
            id=id,
            managed=managed,
            name=name,
            project=project,
            timeouts=timeouts,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putManaged")
    def put_managed(self, *, domains: typing.Sequence[builtins.str]) -> None:
        '''
        :param domains: Domains for which a managed SSL certificate will be valid. Currently, there can be up to 100 domains in this list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#domains GoogleComputeManagedSslCertificate#domains}
        '''
        value = GoogleComputeManagedSslCertificateManaged(domains=domains)

        return typing.cast(None, jsii.invoke(self, "putManaged", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#create GoogleComputeManagedSslCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#delete GoogleComputeManagedSslCertificate#delete}.
        '''
        value = GoogleComputeManagedSslCertificateTimeouts(
            create=create, delete=delete
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCertificateId")
    def reset_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManaged")
    def reset_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManaged", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="expireTime")
    def expire_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expireTime"))

    @builtins.property
    @jsii.member(jsii_name="managed")
    def managed(self) -> "GoogleComputeManagedSslCertificateManagedOutputReference":
        return typing.cast("GoogleComputeManagedSslCertificateManagedOutputReference", jsii.get(self, "managed"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeManagedSslCertificateTimeoutsOutputReference":
        return typing.cast("GoogleComputeManagedSslCertificateTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="certificateIdInput")
    def certificate_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "certificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInput")
    def managed_input(
        self,
    ) -> typing.Optional["GoogleComputeManagedSslCertificateManaged"]:
        return typing.cast(typing.Optional["GoogleComputeManagedSslCertificateManaged"], jsii.get(self, "managedInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeManagedSslCertificateTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeManagedSslCertificateTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateId")
    def certificate_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "certificateId"))

    @certificate_id.setter
    def certificate_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificate, "certificate_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificate, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificate, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificate, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificate, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificate, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeManagedSslCertificate.GoogleComputeManagedSslCertificateConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "certificate_id": "certificateId",
        "description": "description",
        "id": "id",
        "managed": "managed",
        "name": "name",
        "project": "project",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class GoogleComputeManagedSslCertificateConfig(cdktf.TerraformMetaArguments):
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
        certificate_id: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union["GoogleComputeManagedSslCertificateManaged", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeManagedSslCertificateTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param certificate_id: The unique identifier for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#certificate_id GoogleComputeManagedSslCertificate#certificate_id}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#description GoogleComputeManagedSslCertificate#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#id GoogleComputeManagedSslCertificate#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param managed: managed block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#managed GoogleComputeManagedSslCertificate#managed}
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. These are in the same namespace as the managed SSL certificates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#name GoogleComputeManagedSslCertificate#name}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#project GoogleComputeManagedSslCertificate#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#timeouts GoogleComputeManagedSslCertificate#timeouts}
        :param type: Enum field whose value is always 'MANAGED' - used to signal to the API which type this is. Default value: "MANAGED" Possible values: ["MANAGED"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#type GoogleComputeManagedSslCertificate#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(managed, dict):
            managed = GoogleComputeManagedSslCertificateManaged(**managed)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeManagedSslCertificateTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeManagedSslCertificateConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument certificate_id", value=certificate_id, expected_type=type_hints["certificate_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument managed", value=managed, expected_type=type_hints["managed"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if certificate_id is not None:
            self._values["certificate_id"] = certificate_id
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if managed is not None:
            self._values["managed"] = managed
        if name is not None:
            self._values["name"] = name
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

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
    def certificate_id(self) -> typing.Optional[jsii.Number]:
        '''The unique identifier for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#certificate_id GoogleComputeManagedSslCertificate#certificate_id}
        '''
        result = self._values.get("certificate_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#description GoogleComputeManagedSslCertificate#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#id GoogleComputeManagedSslCertificate#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed(self) -> typing.Optional["GoogleComputeManagedSslCertificateManaged"]:
        '''managed block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#managed GoogleComputeManagedSslCertificate#managed}
        '''
        result = self._values.get("managed")
        return typing.cast(typing.Optional["GoogleComputeManagedSslCertificateManaged"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        These are in the same namespace as the managed SSL certificates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#name GoogleComputeManagedSslCertificate#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#project GoogleComputeManagedSslCertificate#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeManagedSslCertificateTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#timeouts GoogleComputeManagedSslCertificate#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeManagedSslCertificateTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Enum field whose value is always 'MANAGED' - used to signal to the API which type this is.

        Default value: "MANAGED" Possible values: ["MANAGED"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#type GoogleComputeManagedSslCertificate#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeManagedSslCertificateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeManagedSslCertificate.GoogleComputeManagedSslCertificateManaged",
    jsii_struct_bases=[],
    name_mapping={"domains": "domains"},
)
class GoogleComputeManagedSslCertificateManaged:
    def __init__(self, *, domains: typing.Sequence[builtins.str]) -> None:
        '''
        :param domains: Domains for which a managed SSL certificate will be valid. Currently, there can be up to 100 domains in this list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#domains GoogleComputeManagedSslCertificate#domains}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeManagedSslCertificateManaged.__init__)
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
        self._values: typing.Dict[str, typing.Any] = {
            "domains": domains,
        }

    @builtins.property
    def domains(self) -> typing.List[builtins.str]:
        '''Domains for which a managed SSL certificate will be valid.

        Currently,
        there can be up to 100 domains in this list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#domains GoogleComputeManagedSslCertificate#domains}
        '''
        result = self._values.get("domains")
        assert result is not None, "Required property 'domains' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeManagedSslCertificateManaged(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeManagedSslCertificateManagedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeManagedSslCertificate.GoogleComputeManagedSslCertificateManagedOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeManagedSslCertificateManagedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="domainsInput")
    def domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domainsInput"))

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificateManagedOutputReference, "domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domains", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeManagedSslCertificateManaged]:
        return typing.cast(typing.Optional[GoogleComputeManagedSslCertificateManaged], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeManagedSslCertificateManaged],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificateManagedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeManagedSslCertificate.GoogleComputeManagedSslCertificateTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleComputeManagedSslCertificateTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#create GoogleComputeManagedSslCertificate#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#delete GoogleComputeManagedSslCertificate#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeManagedSslCertificateTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#create GoogleComputeManagedSslCertificate#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_managed_ssl_certificate#delete GoogleComputeManagedSslCertificate#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeManagedSslCertificateTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeManagedSslCertificateTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeManagedSslCertificate.GoogleComputeManagedSslCertificateTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeManagedSslCertificateTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificateTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificateTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeManagedSslCertificateTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeManagedSslCertificateTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeManagedSslCertificateTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeManagedSslCertificateTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeManagedSslCertificate",
    "GoogleComputeManagedSslCertificateConfig",
    "GoogleComputeManagedSslCertificateManaged",
    "GoogleComputeManagedSslCertificateManagedOutputReference",
    "GoogleComputeManagedSslCertificateTimeouts",
    "GoogleComputeManagedSslCertificateTimeoutsOutputReference",
]

publication.publish()
