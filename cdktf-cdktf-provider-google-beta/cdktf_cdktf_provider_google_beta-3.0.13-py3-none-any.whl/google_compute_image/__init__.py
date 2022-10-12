'''
# `google_compute_image`

Refer to the Terraform Registory for docs: [`google_compute_image`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_image).
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


class GoogleComputeImage(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImage",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image google_compute_image}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        family: typing.Optional[builtins.str] = None,
        guest_os_features: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeImageGuestOsFeatures", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        licenses: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        raw_disk: typing.Optional[typing.Union["GoogleComputeImageRawDisk", typing.Dict[str, typing.Any]]] = None,
        source_disk: typing.Optional[builtins.str] = None,
        source_image: typing.Optional[builtins.str] = None,
        source_snapshot: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeImageTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image google_compute_image} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#name GoogleComputeImage#name}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#description GoogleComputeImage#description}
        :param disk_size_gb: Size of the image when restored onto a persistent disk (in GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#disk_size_gb GoogleComputeImage#disk_size_gb}
        :param family: The name of the image family to which this image belongs. You can create disks by specifying an image family instead of a specific image name. The image family always returns its latest image that is not deprecated. The name of the image family must comply with RFC1035. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#family GoogleComputeImage#family}
        :param guest_os_features: guest_os_features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#guest_os_features GoogleComputeImage#guest_os_features}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#id GoogleComputeImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels to apply to this Image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#labels GoogleComputeImage#labels}
        :param licenses: Any applicable license URI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#licenses GoogleComputeImage#licenses}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#project GoogleComputeImage#project}.
        :param raw_disk: raw_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#raw_disk GoogleComputeImage#raw_disk}
        :param source_disk: The source disk to create this image based on. You must provide either this property or the rawDisk.source property but not both to create an image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_disk GoogleComputeImage#source_disk}
        :param source_image: URL of the source image used to create this image. In order to create an image, you must provide the full or partial URL of one of the following: The selfLink URL This property The rawDisk.source URL The sourceDisk URL Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_image GoogleComputeImage#source_image}
        :param source_snapshot: URL of the source snapshot used to create this image. In order to create an image, you must provide the full or partial URL of one of the following: The selfLink URL This property The sourceImage URL The rawDisk.source URL The sourceDisk URL Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_snapshot GoogleComputeImage#source_snapshot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#timeouts GoogleComputeImage#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImage.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeImageConfig(
            name=name,
            description=description,
            disk_size_gb=disk_size_gb,
            family=family,
            guest_os_features=guest_os_features,
            id=id,
            labels=labels,
            licenses=licenses,
            project=project,
            raw_disk=raw_disk,
            source_disk=source_disk,
            source_image=source_image,
            source_snapshot=source_snapshot,
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

    @jsii.member(jsii_name="putGuestOsFeatures")
    def put_guest_os_features(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeImageGuestOsFeatures", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImage.put_guest_os_features)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestOsFeatures", [value]))

    @jsii.member(jsii_name="putRawDisk")
    def put_raw_disk(
        self,
        *,
        source: builtins.str,
        container_type: typing.Optional[builtins.str] = None,
        sha1: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: The full Google Cloud Storage URL where disk storage is stored You must provide either this property or the sourceDisk property but not both. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source GoogleComputeImage#source}
        :param container_type: The format used to encode and transmit the block device, which should be TAR. This is just a container and transmission format and not a runtime format. Provided by the client when the disk image is created. Default value: "TAR" Possible values: ["TAR"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#container_type GoogleComputeImage#container_type}
        :param sha1: An optional SHA1 checksum of the disk image before unpackaging. This is provided by the client when the disk image is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#sha1 GoogleComputeImage#sha1}
        '''
        value = GoogleComputeImageRawDisk(
            source=source, container_type=container_type, sha1=sha1
        )

        return typing.cast(None, jsii.invoke(self, "putRawDisk", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#create GoogleComputeImage#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#delete GoogleComputeImage#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#update GoogleComputeImage#update}.
        '''
        value = GoogleComputeImageTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetFamily")
    def reset_family(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFamily", []))

    @jsii.member(jsii_name="resetGuestOsFeatures")
    def reset_guest_os_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestOsFeatures", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLicenses")
    def reset_licenses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenses", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRawDisk")
    def reset_raw_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRawDisk", []))

    @jsii.member(jsii_name="resetSourceDisk")
    def reset_source_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDisk", []))

    @jsii.member(jsii_name="resetSourceImage")
    def reset_source_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImage", []))

    @jsii.member(jsii_name="resetSourceSnapshot")
    def reset_source_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceSnapshot", []))

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
    @jsii.member(jsii_name="archiveSizeBytes")
    def archive_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "archiveSizeBytes"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="guestOsFeatures")
    def guest_os_features(self) -> "GoogleComputeImageGuestOsFeaturesList":
        return typing.cast("GoogleComputeImageGuestOsFeaturesList", jsii.get(self, "guestOsFeatures"))

    @builtins.property
    @jsii.member(jsii_name="labelFingerprint")
    def label_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="rawDisk")
    def raw_disk(self) -> "GoogleComputeImageRawDiskOutputReference":
        return typing.cast("GoogleComputeImageRawDiskOutputReference", jsii.get(self, "rawDisk"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeImageTimeoutsOutputReference":
        return typing.cast("GoogleComputeImageTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="guestOsFeaturesInput")
    def guest_os_features_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeImageGuestOsFeatures"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeImageGuestOsFeatures"]]], jsii.get(self, "guestOsFeaturesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="licensesInput")
    def licenses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "licensesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="rawDiskInput")
    def raw_disk_input(self) -> typing.Optional["GoogleComputeImageRawDisk"]:
        return typing.cast(typing.Optional["GoogleComputeImageRawDisk"], jsii.get(self, "rawDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDiskInput")
    def source_disk_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageInput")
    def source_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSnapshotInput")
    def source_snapshot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceSnapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeImageTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeImageTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="licenses")
    def licenses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "licenses"))

    @licenses.setter
    def licenses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "licenses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenses", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDisk")
    def source_disk(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDisk"))

    @source_disk.setter
    def source_disk(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "source_disk").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDisk", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImage")
    def source_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImage"))

    @source_image.setter
    def source_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "source_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImage", value)

    @builtins.property
    @jsii.member(jsii_name="sourceSnapshot")
    def source_snapshot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceSnapshot"))

    @source_snapshot.setter
    def source_snapshot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImage, "source_snapshot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceSnapshot", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageConfig",
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
        "description": "description",
        "disk_size_gb": "diskSizeGb",
        "family": "family",
        "guest_os_features": "guestOsFeatures",
        "id": "id",
        "labels": "labels",
        "licenses": "licenses",
        "project": "project",
        "raw_disk": "rawDisk",
        "source_disk": "sourceDisk",
        "source_image": "sourceImage",
        "source_snapshot": "sourceSnapshot",
        "timeouts": "timeouts",
    },
)
class GoogleComputeImageConfig(cdktf.TerraformMetaArguments):
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
        description: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        family: typing.Optional[builtins.str] = None,
        guest_os_features: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeImageGuestOsFeatures", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        licenses: typing.Optional[typing.Sequence[builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        raw_disk: typing.Optional[typing.Union["GoogleComputeImageRawDisk", typing.Dict[str, typing.Any]]] = None,
        source_disk: typing.Optional[builtins.str] = None,
        source_image: typing.Optional[builtins.str] = None,
        source_snapshot: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeImageTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#name GoogleComputeImage#name}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#description GoogleComputeImage#description}
        :param disk_size_gb: Size of the image when restored onto a persistent disk (in GB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#disk_size_gb GoogleComputeImage#disk_size_gb}
        :param family: The name of the image family to which this image belongs. You can create disks by specifying an image family instead of a specific image name. The image family always returns its latest image that is not deprecated. The name of the image family must comply with RFC1035. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#family GoogleComputeImage#family}
        :param guest_os_features: guest_os_features block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#guest_os_features GoogleComputeImage#guest_os_features}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#id GoogleComputeImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Labels to apply to this Image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#labels GoogleComputeImage#labels}
        :param licenses: Any applicable license URI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#licenses GoogleComputeImage#licenses}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#project GoogleComputeImage#project}.
        :param raw_disk: raw_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#raw_disk GoogleComputeImage#raw_disk}
        :param source_disk: The source disk to create this image based on. You must provide either this property or the rawDisk.source property but not both to create an image. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_disk GoogleComputeImage#source_disk}
        :param source_image: URL of the source image used to create this image. In order to create an image, you must provide the full or partial URL of one of the following: The selfLink URL This property The rawDisk.source URL The sourceDisk URL Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_image GoogleComputeImage#source_image}
        :param source_snapshot: URL of the source snapshot used to create this image. In order to create an image, you must provide the full or partial URL of one of the following: The selfLink URL This property The sourceImage URL The rawDisk.source URL The sourceDisk URL Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_snapshot GoogleComputeImage#source_snapshot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#timeouts GoogleComputeImage#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(raw_disk, dict):
            raw_disk = GoogleComputeImageRawDisk(**raw_disk)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeImageTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImageConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument guest_os_features", value=guest_os_features, expected_type=type_hints["guest_os_features"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument licenses", value=licenses, expected_type=type_hints["licenses"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument raw_disk", value=raw_disk, expected_type=type_hints["raw_disk"])
            check_type(argname="argument source_disk", value=source_disk, expected_type=type_hints["source_disk"])
            check_type(argname="argument source_image", value=source_image, expected_type=type_hints["source_image"])
            check_type(argname="argument source_snapshot", value=source_snapshot, expected_type=type_hints["source_snapshot"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if family is not None:
            self._values["family"] = family
        if guest_os_features is not None:
            self._values["guest_os_features"] = guest_os_features
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if licenses is not None:
            self._values["licenses"] = licenses
        if project is not None:
            self._values["project"] = project
        if raw_disk is not None:
            self._values["raw_disk"] = raw_disk
        if source_disk is not None:
            self._values["source_disk"] = source_disk
        if source_image is not None:
            self._values["source_image"] = source_image
        if source_snapshot is not None:
            self._values["source_snapshot"] = source_snapshot
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
    def name(self) -> builtins.str:
        '''Name of the resource;

        provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and
        match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means
        the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the
        last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#name GoogleComputeImage#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#description GoogleComputeImage#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Size of the image when restored onto a persistent disk (in GB).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#disk_size_gb GoogleComputeImage#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def family(self) -> typing.Optional[builtins.str]:
        '''The name of the image family to which this image belongs.

        You can
        create disks by specifying an image family instead of a specific
        image name. The image family always returns its latest image that is
        not deprecated. The name of the image family must comply with
        RFC1035.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#family GoogleComputeImage#family}
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def guest_os_features(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeImageGuestOsFeatures"]]]:
        '''guest_os_features block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#guest_os_features GoogleComputeImage#guest_os_features}
        '''
        result = self._values.get("guest_os_features")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeImageGuestOsFeatures"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#id GoogleComputeImage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to this Image.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#labels GoogleComputeImage#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def licenses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Any applicable license URI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#licenses GoogleComputeImage#licenses}
        '''
        result = self._values.get("licenses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#project GoogleComputeImage#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def raw_disk(self) -> typing.Optional["GoogleComputeImageRawDisk"]:
        '''raw_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#raw_disk GoogleComputeImage#raw_disk}
        '''
        result = self._values.get("raw_disk")
        return typing.cast(typing.Optional["GoogleComputeImageRawDisk"], result)

    @builtins.property
    def source_disk(self) -> typing.Optional[builtins.str]:
        '''The source disk to create this image based on.

        You must provide either this property or the
        rawDisk.source property but not both to create an image.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_disk GoogleComputeImage#source_disk}
        '''
        result = self._values.get("source_disk")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image(self) -> typing.Optional[builtins.str]:
        '''URL of the source image used to create this image.

        In order to create an image, you must provide the full or partial
        URL of one of the following:

        The selfLink URL
        This property
        The rawDisk.source URL
        The sourceDisk URL

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_image GoogleComputeImage#source_image}
        '''
        result = self._values.get("source_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_snapshot(self) -> typing.Optional[builtins.str]:
        '''URL of the source snapshot used to create this image.

        In order to create an image, you must provide the full or partial URL of one of the following:

        The selfLink URL
        This property
        The sourceImage URL
        The rawDisk.source URL
        The sourceDisk URL

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source_snapshot GoogleComputeImage#source_snapshot}
        '''
        result = self._values.get("source_snapshot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeImageTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#timeouts GoogleComputeImage#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeImageTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageGuestOsFeatures",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class GoogleComputeImageGuestOsFeatures:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: The type of supported feature. Read `Enabling guest operating system features <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features>`_ to see a list of available options. Possible values: ["MULTI_IP_SUBNET", "SECURE_BOOT", "SEV_CAPABLE", "UEFI_COMPATIBLE", "VIRTIO_SCSI_MULTIQUEUE", "WINDOWS", "GVNIC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#type GoogleComputeImage#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImageGuestOsFeatures.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of supported feature.

        Read `Enabling guest operating system features <https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features>`_ to see a list of available options. Possible values: ["MULTI_IP_SUBNET", "SECURE_BOOT", "SEV_CAPABLE", "UEFI_COMPATIBLE", "VIRTIO_SCSI_MULTIQUEUE", "WINDOWS", "GVNIC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#type GoogleComputeImage#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeImageGuestOsFeatures(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeImageGuestOsFeaturesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageGuestOsFeaturesList",
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
            type_hints = typing.get_type_hints(GoogleComputeImageGuestOsFeaturesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeImageGuestOsFeaturesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImageGuestOsFeaturesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeImageGuestOsFeaturesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageGuestOsFeaturesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageGuestOsFeaturesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageGuestOsFeaturesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeImageGuestOsFeatures]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeImageGuestOsFeatures]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeImageGuestOsFeatures]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageGuestOsFeaturesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeImageGuestOsFeaturesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageGuestOsFeaturesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeImageGuestOsFeaturesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageGuestOsFeaturesOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeImageGuestOsFeatures, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeImageGuestOsFeatures, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeImageGuestOsFeatures, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageGuestOsFeaturesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageRawDisk",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "container_type": "containerType",
        "sha1": "sha1",
    },
)
class GoogleComputeImageRawDisk:
    def __init__(
        self,
        *,
        source: builtins.str,
        container_type: typing.Optional[builtins.str] = None,
        sha1: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: The full Google Cloud Storage URL where disk storage is stored You must provide either this property or the sourceDisk property but not both. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source GoogleComputeImage#source}
        :param container_type: The format used to encode and transmit the block device, which should be TAR. This is just a container and transmission format and not a runtime format. Provided by the client when the disk image is created. Default value: "TAR" Possible values: ["TAR"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#container_type GoogleComputeImage#container_type}
        :param sha1: An optional SHA1 checksum of the disk image before unpackaging. This is provided by the client when the disk image is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#sha1 GoogleComputeImage#sha1}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImageRawDisk.__init__)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument container_type", value=container_type, expected_type=type_hints["container_type"])
            check_type(argname="argument sha1", value=sha1, expected_type=type_hints["sha1"])
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if container_type is not None:
            self._values["container_type"] = container_type
        if sha1 is not None:
            self._values["sha1"] = sha1

    @builtins.property
    def source(self) -> builtins.str:
        '''The full Google Cloud Storage URL where disk storage is stored You must provide either this property or the sourceDisk property but not both.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#source GoogleComputeImage#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_type(self) -> typing.Optional[builtins.str]:
        '''The format used to encode and transmit the block device, which should be TAR.

        This is just a container and transmission format
        and not a runtime format. Provided by the client when the disk
        image is created. Default value: "TAR" Possible values: ["TAR"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#container_type GoogleComputeImage#container_type}
        '''
        result = self._values.get("container_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sha1(self) -> typing.Optional[builtins.str]:
        '''An optional SHA1 checksum of the disk image before unpackaging.

        This is provided by the client when the disk image is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#sha1 GoogleComputeImage#sha1}
        '''
        result = self._values.get("sha1")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeImageRawDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeImageRawDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageRawDiskOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeImageRawDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerType")
    def reset_container_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerType", []))

    @jsii.member(jsii_name="resetSha1")
    def reset_sha1(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSha1", []))

    @builtins.property
    @jsii.member(jsii_name="containerTypeInput")
    def container_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sha1Input")
    def sha1_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sha1Input"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="containerType")
    def container_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerType"))

    @container_type.setter
    def container_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageRawDiskOutputReference, "container_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerType", value)

    @builtins.property
    @jsii.member(jsii_name="sha1")
    def sha1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha1"))

    @sha1.setter
    def sha1(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageRawDiskOutputReference, "sha1").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sha1", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageRawDiskOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeImageRawDisk]:
        return typing.cast(typing.Optional[GoogleComputeImageRawDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleComputeImageRawDisk]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageRawDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeImageTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#create GoogleComputeImage#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#delete GoogleComputeImage#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#update GoogleComputeImage#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeImageTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#create GoogleComputeImage#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#delete GoogleComputeImage#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_image#update GoogleComputeImage#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeImageTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeImageTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeImage.GoogleComputeImageTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeImageTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeImageTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeImageTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeImageTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeImageTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeImage",
    "GoogleComputeImageConfig",
    "GoogleComputeImageGuestOsFeatures",
    "GoogleComputeImageGuestOsFeaturesList",
    "GoogleComputeImageGuestOsFeaturesOutputReference",
    "GoogleComputeImageRawDisk",
    "GoogleComputeImageRawDiskOutputReference",
    "GoogleComputeImageTimeouts",
    "GoogleComputeImageTimeoutsOutputReference",
]

publication.publish()
