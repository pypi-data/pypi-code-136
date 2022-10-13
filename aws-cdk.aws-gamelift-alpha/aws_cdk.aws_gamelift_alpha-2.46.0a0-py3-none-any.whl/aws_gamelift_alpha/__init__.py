'''
# Amazon GameLift Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

[Amazon GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-intro.html) is a service used
to deploy, operate, and scale dedicated, low-cost servers in the cloud for session-based multiplayer games. Built
on AWS global computing infrastructure, GameLift helps deliver high-performance, high-reliability game servers
while dynamically scaling your resource usage to meet worldwide player demand.

GameLift is composed of three main components:

* GameLift FlexMatch which is a customizable matchmaking service for
  multiplayer games. With FlexMatch, you can
  build a custom set of rules that defines what a multiplayer match looks like
  for your game, and determines how to
  evaluate and select compatible players for each match. You can also customize
  key aspects of the matchmaking
  process to fit your game, including fine-tuning the matching algorithm.
* GameLift hosting for custom or realtime servers which helps you deploy,
  operate, and scale dedicated game servers. It regulates the resources needed to
  host games, finds available game servers to host new game sessions, and puts
  players into games.
* GameLift FleetIQ to optimize the use of low-cost Amazon Elastic Compute Cloud
  (Amazon EC2) Spot Instances for cloud-based game hosting. With GameLift
  FleetIQ, you can work directly with your hosting resources in Amazon EC2 and
  Amazon EC2 Auto Scaling while taking advantage of GameLift optimizations to
  deliver inexpensive, resilient game hosting for your players

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project. It allows you to define components for your matchmaking
configuration or game server fleet management system.

## GameLift Hosting

### Defining a GameLift Fleet

GameLift helps you deploy, operate, and scale dedicated game servers for
session-based multiplayer games. It helps you regulate the resources needed to
host your games, finds available game servers to host new game sessions, and
puts players into games.

### Uploading builds and scripts to GameLift

Before deploying your GameLift-enabled multiplayer game servers for hosting with the GameLift service, you need to upload
your game server files. This section provides guidance on preparing and uploading custom game server build
files or Realtime Servers server script files. When you upload files, you create a GameLift build or script resource, which
you then deploy on fleets of hosting resources.

To troubleshoot fleet activation problems related to the server script, see [Debug GameLift fleet issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html).

#### Upload a custom server build to GameLift

Before uploading your configured game server to GameLift for hosting, package the game build files into a build directory.
This directory must include all components required to run your game servers and host game sessions, including the following:

* Game server binaries – The binary files required to run the game server. A build can include binaries for multiple game
  servers built to run on the same platform. For a list of supported platforms, see [Download Amazon GameLift SDKs](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-supported.html).
* Dependencies – Any dependent files that your game server executables require to run. Examples include assets, configuration
  files, and dependent libraries.
* Install script – A script file to handle tasks that are required to fully install your game build on GameLift hosting
  servers. Place this file at the root of the build directory. GameLift runs the install script as part of fleet creation.

You can set up any application in your build, including your install script, to access your resources securely on other AWS
services.

```python
# bucket: s3.Bucket

gamelift.Build(self, "Build",
    content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
)
```

#### Upload a realtime server Script

Your server script can include one or more files combined into a single .zip file for uploading. The .zip file must contain
all files that your script needs to run.

You can store your zipped script files in either a local file directory or in an Amazon Simple Storage Service (Amazon S3)
bucket or defines a directory asset which is archived as a .zip file and uploaded to S3 during deployment.

After you create the script resource, GameLift deploys the script with a new Realtime Servers fleet. GameLift installs your
server script onto each instance in the fleet, placing the script files in `/local/game`.

```python
# bucket: s3.Bucket

gamelift.Script(self, "Script",
    content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
)
```
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

from ._jsii import *

import aws_cdk
import aws_cdk.aws_iam
import aws_cdk.aws_s3
import aws_cdk.aws_s3_assets
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-gamelift-alpha.BuildAttributes",
    jsii_struct_bases=[],
    name_mapping={"build_id": "buildId", "role": "role"},
)
class BuildAttributes:
    def __init__(
        self,
        *,
        build_id: builtins.str,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''(experimental) Represents a Build content defined outside of this stack.

        :param build_id: (experimental) The identifier of the build.
        :param role: (experimental) The IAM role assumed by GameLift to access server build in S3. Default: - undefined

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_gamelift_alpha as gamelift_alpha
            from aws_cdk import aws_iam as iam
            
            # role: iam.Role
            
            build_attributes = gamelift_alpha.BuildAttributes(
                build_id="buildId",
            
                # the properties below are optional
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BuildAttributes.__init__)
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {
            "build_id": build_id,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def build_id(self) -> builtins.str:
        '''(experimental) The identifier of the build.

        :stability: experimental
        '''
        result = self._values.get("build_id")
        assert result is not None, "Required property 'build_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role assumed by GameLift to access server build in S3.

        :default: - undefined

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-gamelift-alpha.BuildProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "build_name": "buildName",
        "build_version": "buildVersion",
        "operating_system": "operatingSystem",
        "role": "role",
    },
)
class BuildProps:
    def __init__(
        self,
        *,
        content: "Content",
        build_name: typing.Optional[builtins.str] = None,
        build_version: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional["OperatingSystem"] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''(experimental) Properties for a new build.

        :param content: (experimental) The game build file storage.
        :param build_name: (experimental) Name of this build. Default: No name
        :param build_version: (experimental) Version of this build. Default: No version
        :param operating_system: (experimental) The operating system that the game server binaries are built to run on. Default: No version
        :param role: (experimental) The IAM role assumed by GameLift to access server build in S3. If providing a custom role, it needs to trust the GameLift service principal (gamelift.amazonaws.com) and be granted sufficient permissions to have Read access to a specific key content into a specific S3 bucket. Below an example of required permission: { "Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "s3:GetObject", "s3:GetObjectVersion" ], "Resource": "arn:aws:s3:::bucket-name/object-name" }] } Default: - a role will be created with default permissions.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # bucket: s3.Bucket
            
            gamelift.Build(self, "Build",
                content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BuildProps.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument build_name", value=build_name, expected_type=type_hints["build_name"])
            check_type(argname="argument build_version", value=build_version, expected_type=type_hints["build_version"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if build_name is not None:
            self._values["build_name"] = build_name
        if build_version is not None:
            self._values["build_version"] = build_version
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def content(self) -> "Content":
        '''(experimental) The game build file storage.

        :stability: experimental
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast("Content", result)

    @builtins.property
    def build_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of this build.

        :default: No name

        :stability: experimental
        '''
        result = self._values.get("build_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Version of this build.

        :default: No version

        :stability: experimental
        '''
        result = self._values.get("build_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system(self) -> typing.Optional["OperatingSystem"]:
        '''(experimental) The operating system that the game server binaries are built to run on.

        :default: No version

        :stability: experimental
        '''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional["OperatingSystem"], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role assumed by GameLift to access server build in S3.

        If providing a custom role, it needs to trust the GameLift service principal (gamelift.amazonaws.com) and be granted sufficient permissions
        to have Read access to a specific key content into a specific S3 bucket.
        Below an example of required permission:
        {
        "Version": "2012-10-17",
        "Statement": [{
        "Effect": "Allow",
        "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
        ],
        "Resource": "arn:aws:s3:::bucket-name/object-name"
        }]
        }

        :default: - a role will be created with default permissions.

        :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-access-storage-loc
        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Content(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-gamelift-alpha.Content",
):
    '''(experimental) Before deploying your GameLift-enabled multiplayer game servers for hosting with the GameLift service, you need to upload your game server files.

    The class helps you on preparing and uploading custom game server build files or Realtime Servers server script files.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # bucket: s3.Bucket
        
        gamelift.Build(self, "Build",
            content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[aws_cdk.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[aws_cdk.BundlingOptions, typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
    ) -> "AssetContent":
        '''(experimental) Loads the game content from a local disk path.

        :param path: Either a directory with the game content bundle or a .zip file.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Content.from_asset)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("AssetContent", jsii.sinvoke(cls, "fromAsset", [path, options]))

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: aws_cdk.aws_s3.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "S3Content":
        '''(experimental) Game content as an S3 object.

        :param bucket: The S3 bucket.
        :param key: The object key.
        :param object_version: Optional S3 ob ject version.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Content.from_bucket)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        return typing.cast("S3Content", jsii.sinvoke(cls, "fromBucket", [bucket, key, object_version]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(
        self,
        scope: constructs.Construct,
        grantable: aws_cdk.aws_iam.IGrantable,
    ) -> "ContentConfig":
        '''(experimental) Called when the Build is initialized to allow this object to bind.

        :param scope: -
        :param grantable: -

        :stability: experimental
        '''
        ...


class _ContentProxy(Content):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        grantable: aws_cdk.aws_iam.IGrantable,
    ) -> "ContentConfig":
        '''(experimental) Called when the Build is initialized to allow this object to bind.

        :param scope: -
        :param grantable: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Content.bind)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument grantable", value=grantable, expected_type=type_hints["grantable"])
        return typing.cast("ContentConfig", jsii.invoke(self, "bind", [scope, grantable]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Content).__jsii_proxy_class__ = lambda : _ContentProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-gamelift-alpha.ContentConfig",
    jsii_struct_bases=[],
    name_mapping={"s3_location": "s3Location"},
)
class ContentConfig:
    def __init__(
        self,
        *,
        s3_location: typing.Union[aws_cdk.aws_s3.Location, typing.Dict[str, typing.Any]],
    ) -> None:
        '''(experimental) Result of binding ``Content`` into a ``Build``.

        :param s3_location: (experimental) The location of the content in S3.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_gamelift_alpha as gamelift_alpha
            
            content_config = gamelift_alpha.ContentConfig(
                s3_location=Location(
                    bucket_name="bucketName",
                    object_key="objectKey",
            
                    # the properties below are optional
                    object_version="objectVersion"
                )
            )
        '''
        if isinstance(s3_location, dict):
            s3_location = aws_cdk.aws_s3.Location(**s3_location)
        if __debug__:
            type_hints = typing.get_type_hints(ContentConfig.__init__)
            check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
        self._values: typing.Dict[str, typing.Any] = {
            "s3_location": s3_location,
        }

    @builtins.property
    def s3_location(self) -> aws_cdk.aws_s3.Location:
        '''(experimental) The location of the content in S3.

        :stability: experimental
        '''
        result = self._values.get("s3_location")
        assert result is not None, "Required property 's3_location' is missing"
        return typing.cast(aws_cdk.aws_s3.Location, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-gamelift-alpha.IBuild")
class IBuild(aws_cdk.IResource, aws_cdk.aws_iam.IGrantable, typing_extensions.Protocol):
    '''(experimental) Your custom-built game server software that runs on GameLift and hosts game sessions for your players.

    A game build represents the set of files that run your game server on a particular operating system.
    You can have many different builds, such as for different flavors of your game.
    The game build must be integrated with the GameLift service.
    You upload game build files to the GameLift service in the Regions where you plan to set up fleets.

    :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        '''(experimental) The Identifier of the build.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IBuildProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_iam.IGrantable), # type: ignore[misc]
):
    '''(experimental) Your custom-built game server software that runs on GameLift and hosts game sessions for your players.

    A game build represents the set of files that run your game server on a particular operating system.
    You can have many different builds, such as for different flavors of your game.
    The game build must be integrated with the GameLift service.
    You upload game build files to the GameLift service in the Regions where you plan to set up fleets.

    :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-gamelift-alpha.IBuild"

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        '''(experimental) The Identifier of the build.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "buildId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBuild).__jsii_proxy_class__ = lambda : _IBuildProxy


@jsii.interface(jsii_type="@aws-cdk/aws-gamelift-alpha.IScript")
class IScript(
    aws_cdk.IResource,
    aws_cdk.aws_iam.IGrantable,
    typing_extensions.Protocol,
):
    '''(experimental) Your configuration and custom game logic for use with Realtime Servers.

    Realtime Servers are provided by GameLift to use instead of a custom-built game server.
    You configure Realtime Servers for your game clients by creating a script using JavaScript,
    and add custom game logic as appropriate to host game sessions for your players.
    You upload the Realtime script to the GameLift service in the Regions where you plan to set up fleets.

    :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script-uploading.html
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scriptArn")
    def script_arn(self) -> builtins.str:
        '''(experimental) The ARN of the realtime server script.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> builtins.str:
        '''(experimental) The Identifier of the realtime server script.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IScriptProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_iam.IGrantable), # type: ignore[misc]
):
    '''(experimental) Your configuration and custom game logic for use with Realtime Servers.

    Realtime Servers are provided by GameLift to use instead of a custom-built game server.
    You configure Realtime Servers for your game clients by creating a script using JavaScript,
    and add custom game logic as appropriate to host game sessions for your players.
    You upload the Realtime script to the GameLift service in the Regions where you plan to set up fleets.

    :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script-uploading.html
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-gamelift-alpha.IScript"

    @builtins.property
    @jsii.member(jsii_name="scriptArn")
    def script_arn(self) -> builtins.str:
        '''(experimental) The ARN of the realtime server script.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scriptArn"))

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> builtins.str:
        '''(experimental) The Identifier of the realtime server script.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scriptId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScript).__jsii_proxy_class__ = lambda : _IScriptProxy


@jsii.enum(jsii_type="@aws-cdk/aws-gamelift-alpha.OperatingSystem")
class OperatingSystem(enum.Enum):
    '''(experimental) The operating system that the game server binaries are built to run on.

    :stability: experimental
    '''

    AMAZON_LINUX = "AMAZON_LINUX"
    '''
    :stability: experimental
    '''
    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    '''
    :stability: experimental
    '''
    WINDOWS_2012 = "WINDOWS_2012"
    '''
    :stability: experimental
    '''


class S3Content(
    Content,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-gamelift-alpha.S3Content",
):
    '''(experimental) Game content from an S3 archive.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_gamelift_alpha as gamelift_alpha
        from aws_cdk import aws_s3 as s3
        
        # bucket: s3.Bucket
        
        s3_content = gamelift_alpha.S3Content(bucket, "key", "objectVersion")
    '''

    def __init__(
        self,
        bucket: aws_cdk.aws_s3.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param key: -
        :param object_version: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(S3Content.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        jsii.create(self.__class__, self, [bucket, key, object_version])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: constructs.Construct,
        grantable: aws_cdk.aws_iam.IGrantable,
    ) -> ContentConfig:
        '''(experimental) Called when the Build is initialized to allow this object to bind.

        :param _scope: -
        :param grantable: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(S3Content.bind)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument grantable", value=grantable, expected_type=type_hints["grantable"])
        return typing.cast(ContentConfig, jsii.invoke(self, "bind", [_scope, grantable]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-gamelift-alpha.ScriptAttributes",
    jsii_struct_bases=[],
    name_mapping={"script_arn": "scriptArn", "role": "role"},
)
class ScriptAttributes:
    def __init__(
        self,
        *,
        script_arn: builtins.str,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''(experimental) Represents a Script content defined outside of this stack.

        :param script_arn: (experimental) The ARN of the realtime server script.
        :param role: (experimental) The IAM role assumed by GameLift to access server script in S3. Default: - undefined

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_gamelift_alpha as gamelift_alpha
            from aws_cdk import aws_iam as iam
            
            # role: iam.Role
            
            script_attributes = gamelift_alpha.ScriptAttributes(
                script_arn="scriptArn",
            
                # the properties below are optional
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ScriptAttributes.__init__)
            check_type(argname="argument script_arn", value=script_arn, expected_type=type_hints["script_arn"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {
            "script_arn": script_arn,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def script_arn(self) -> builtins.str:
        '''(experimental) The ARN of the realtime server script.

        :stability: experimental
        '''
        result = self._values.get("script_arn")
        assert result is not None, "Required property 'script_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role assumed by GameLift to access server script in S3.

        :default: - undefined

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScriptAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IScript)
class ScriptBase(
    aws_cdk.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-gamelift-alpha.ScriptBase",
):
    '''(experimental) Base class for new and imported GameLift realtime server script.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ScriptBase.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = aws_cdk.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    @abc.abstractmethod
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal to grant permissions to.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="scriptArn")
    @abc.abstractmethod
    def script_arn(self) -> builtins.str:
        '''(experimental) The ARN of the realtime server script.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    @abc.abstractmethod
    def script_id(self) -> builtins.str:
        '''(experimental) The Identifier of the realtime server script.

        :stability: experimental
        '''
        ...


class _ScriptBaseProxy(
    ScriptBase,
    jsii.proxy_for(aws_cdk.Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal to grant permissions to.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="scriptArn")
    def script_arn(self) -> builtins.str:
        '''(experimental) The ARN of the realtime server script.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "scriptArn"))

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> builtins.str:
        '''(experimental) The Identifier of the realtime server script.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "scriptId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ScriptBase).__jsii_proxy_class__ = lambda : _ScriptBaseProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-gamelift-alpha.ScriptProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "role": "role",
        "script_name": "scriptName",
        "script_version": "scriptVersion",
    },
)
class ScriptProps:
    def __init__(
        self,
        *,
        content: Content,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        script_name: typing.Optional[builtins.str] = None,
        script_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for a new realtime server script.

        :param content: (experimental) The game content.
        :param role: (experimental) The IAM role assumed by GameLift to access server script in S3. If providing a custom role, it needs to trust the GameLift service principal (gamelift.amazonaws.com) and be granted sufficient permissions to have Read access to a specific key content into a specific S3 bucket. Below an example of required permission: { "Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "s3:GetObject", "s3:GetObjectVersion" ], "Resource": "arn:aws:s3:::bucket-name/object-name" }] } Default: - a role will be created with default permissions.
        :param script_name: (experimental) Name of this realtime server script. Default: No name
        :param script_version: (experimental) Version of this realtime server script. Default: No version

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # bucket: s3.Bucket
            
            gamelift.Script(self, "Script",
                content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ScriptProps.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument script_name", value=script_name, expected_type=type_hints["script_name"])
            check_type(argname="argument script_version", value=script_version, expected_type=type_hints["script_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
        }
        if role is not None:
            self._values["role"] = role
        if script_name is not None:
            self._values["script_name"] = script_name
        if script_version is not None:
            self._values["script_version"] = script_version

    @builtins.property
    def content(self) -> Content:
        '''(experimental) The game content.

        :stability: experimental
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(Content, result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role assumed by GameLift to access server script in S3.

        If providing a custom role, it needs to trust the GameLift service principal (gamelift.amazonaws.com) and be granted sufficient permissions
        to have Read access to a specific key content into a specific S3 bucket.
        Below an example of required permission:
        {
        "Version": "2012-10-17",
        "Statement": [{
        "Effect": "Allow",
        "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
        ],
        "Resource": "arn:aws:s3:::bucket-name/object-name"
        }]
        }

        :default: - a role will be created with default permissions.

        :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/security_iam_id-based-policy-examples.html#security_iam_id-based-policy-examples-access-storage-loc
        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def script_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of this realtime server script.

        :default: No name

        :stability: experimental
        '''
        result = self._values.get("script_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def script_version(self) -> typing.Optional[builtins.str]:
        '''(experimental) Version of this realtime server script.

        :default: No version

        :stability: experimental
        '''
        result = self._values.get("script_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScriptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AssetContent(
    Content,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-gamelift-alpha.AssetContent",
):
    '''(experimental) Game content from a local directory.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_gamelift_alpha as gamelift_alpha
        import aws_cdk as cdk
        from aws_cdk import aws_iam as iam
        
        # docker_image: cdk.DockerImage
        # grantable: iam.IGrantable
        # local_bundling: cdk.ILocalBundling
        
        asset_content = gamelift_alpha.AssetContent("path",
            asset_hash="assetHash",
            asset_hash_type=cdk.AssetHashType.SOURCE,
            bundling=cdk.BundlingOptions(
                image=docker_image,
        
                # the properties below are optional
                command=["command"],
                entrypoint=["entrypoint"],
                environment={
                    "environment_key": "environment"
                },
                local=local_bundling,
                network="network",
                output_type=cdk.BundlingOutput.ARCHIVED,
                security_opt="securityOpt",
                user="user",
                volumes=[cdk.DockerVolume(
                    container_path="containerPath",
                    host_path="hostPath",
        
                    # the properties below are optional
                    consistency=cdk.DockerVolumeConsistency.CONSISTENT
                )],
                working_directory="workingDirectory"
            ),
            exclude=["exclude"],
            follow_symlinks=cdk.SymlinkFollowMode.NEVER,
            ignore_mode=cdk.IgnoreMode.GLOB,
            readers=[grantable]
        )
    '''

    def __init__(
        self,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[aws_cdk.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[aws_cdk.BundlingOptions, typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
    ) -> None:
        '''
        :param path: The path to the asset file or directory.
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AssetContent.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        jsii.create(self.__class__, self, [path, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        grantable: aws_cdk.aws_iam.IGrantable,
    ) -> ContentConfig:
        '''(experimental) Called when the Build is initialized to allow this object to bind.

        :param scope: -
        :param grantable: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AssetContent.bind)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument grantable", value=grantable, expected_type=type_hints["grantable"])
        return typing.cast(ContentConfig, jsii.invoke(self, "bind", [scope, grantable]))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''(experimental) The path to the asset file or directory.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))


@jsii.implements(IBuild)
class BuildBase(
    aws_cdk.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-gamelift-alpha.BuildBase",
):
    '''(experimental) Base class for new and imported GameLift server build.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BuildBase.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = aws_cdk.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="buildId")
    @abc.abstractmethod
    def build_id(self) -> builtins.str:
        '''(experimental) The Identifier of the build.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    @abc.abstractmethod
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal to grant permissions to.

        :stability: experimental
        '''
        ...


class _BuildBaseProxy(
    BuildBase,
    jsii.proxy_for(aws_cdk.Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        '''(experimental) The Identifier of the build.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "buildId"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal to grant permissions to.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BuildBase).__jsii_proxy_class__ = lambda : _BuildBaseProxy


class Script(
    ScriptBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-gamelift-alpha.Script",
):
    '''(experimental) A GameLift script, that is installed and runs on instances in an Amazon GameLift fleet.

    It consists of
    a zip file with all of the components of the realtime game server script.

    :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-script-uploading.html
    :stability: experimental
    :resource: AWS::GameLift::Script
    :exampleMetadata: infused

    Example::

        # bucket: s3.Bucket
        
        gamelift.Script(self, "Script",
            content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        content: Content,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        script_name: typing.Optional[builtins.str] = None,
        script_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param content: (experimental) The game content.
        :param role: (experimental) The IAM role assumed by GameLift to access server script in S3. If providing a custom role, it needs to trust the GameLift service principal (gamelift.amazonaws.com) and be granted sufficient permissions to have Read access to a specific key content into a specific S3 bucket. Below an example of required permission: { "Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "s3:GetObject", "s3:GetObjectVersion" ], "Resource": "arn:aws:s3:::bucket-name/object-name" }] } Default: - a role will be created with default permissions.
        :param script_name: (experimental) Name of this realtime server script. Default: No name
        :param script_version: (experimental) Version of this realtime server script. Default: No version

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Script.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScriptProps(
            content=content,
            role=role,
            script_name=script_name,
            script_version=script_version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[aws_cdk.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[aws_cdk.BundlingOptions, typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
    ) -> "Script":
        '''(experimental) Create a new realtime server script from asset content.

        :param scope: -
        :param id: -
        :param path: -
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Script.from_asset)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("Script", jsii.sinvoke(cls, "fromAsset", [scope, id, path, options]))

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        bucket: aws_cdk.aws_s3.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "Script":
        '''(experimental) Create a new realtime server script from s3 content.

        :param scope: -
        :param id: -
        :param bucket: -
        :param key: -
        :param object_version: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Script.from_bucket)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        return typing.cast("Script", jsii.sinvoke(cls, "fromBucket", [scope, id, bucket, key, object_version]))

    @jsii.member(jsii_name="fromScriptArn")
    @builtins.classmethod
    def from_script_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        script_arn: builtins.str,
    ) -> IScript:
        '''(experimental) Import a script into CDK using its ARN.

        :param scope: -
        :param id: -
        :param script_arn: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Script.from_script_arn)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument script_arn", value=script_arn, expected_type=type_hints["script_arn"])
        return typing.cast(IScript, jsii.sinvoke(cls, "fromScriptArn", [scope, id, script_arn]))

    @jsii.member(jsii_name="fromScriptAttributes")
    @builtins.classmethod
    def from_script_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        script_arn: builtins.str,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> IScript:
        '''(experimental) Import an existing realtime server script from its attributes.

        :param scope: -
        :param id: -
        :param script_arn: (experimental) The ARN of the realtime server script.
        :param role: (experimental) The IAM role assumed by GameLift to access server script in S3. Default: - undefined

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Script.from_script_attributes)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ScriptAttributes(script_arn=script_arn, role=role)

        return typing.cast(IScript, jsii.sinvoke(cls, "fromScriptAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal this GameLift script is using.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        '''(experimental) The IAM role GameLift assumes to acccess server script content.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IRole, jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="scriptArn")
    def script_arn(self) -> builtins.str:
        '''(experimental) The ARN of the realtime server script.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "scriptArn"))

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> builtins.str:
        '''(experimental) The Identifier of the realtime server script.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "scriptId"))


class Build(
    BuildBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-gamelift-alpha.Build",
):
    '''(experimental) A GameLift build, that is installed and runs on instances in an Amazon GameLift fleet.

    It consists of
    a zip file with all of the components of the game server build.

    :see: https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html
    :stability: experimental
    :resource: AWS::GameLift::Build
    :exampleMetadata: infused

    Example::

        # bucket: s3.Bucket
        
        gamelift.Build(self, "Build",
            content=gamelift.Content.from_bucket(bucket, "sample-asset-key")
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        content: Content,
        build_name: typing.Optional[builtins.str] = None,
        build_version: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[OperatingSystem] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param content: (experimental) The game build file storage.
        :param build_name: (experimental) Name of this build. Default: No name
        :param build_version: (experimental) Version of this build. Default: No version
        :param operating_system: (experimental) The operating system that the game server binaries are built to run on. Default: No version
        :param role: (experimental) The IAM role assumed by GameLift to access server build in S3. If providing a custom role, it needs to trust the GameLift service principal (gamelift.amazonaws.com) and be granted sufficient permissions to have Read access to a specific key content into a specific S3 bucket. Below an example of required permission: { "Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "s3:GetObject", "s3:GetObjectVersion" ], "Resource": "arn:aws:s3:::bucket-name/object-name" }] } Default: - a role will be created with default permissions.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Build.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BuildProps(
            content=content,
            build_name=build_name,
            build_version=build_version,
            operating_system=operating_system,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        path: builtins.str,
        *,
        readers: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[aws_cdk.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[aws_cdk.BundlingOptions, typing.Dict[str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[aws_cdk.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[aws_cdk.IgnoreMode] = None,
    ) -> "Build":
        '''(experimental) Create a new Build from asset content.

        :param scope: -
        :param id: -
        :param path: -
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Build.from_asset)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        options = aws_cdk.aws_s3_assets.AssetOptions(
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("Build", jsii.sinvoke(cls, "fromAsset", [scope, id, path, options]))

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        bucket: aws_cdk.aws_s3.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "Build":
        '''(experimental) Create a new Build from s3 content.

        :param scope: -
        :param id: -
        :param bucket: -
        :param key: -
        :param object_version: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Build.from_bucket)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        return typing.cast("Build", jsii.sinvoke(cls, "fromBucket", [scope, id, bucket, key, object_version]))

    @jsii.member(jsii_name="fromBuildAttributes")
    @builtins.classmethod
    def from_build_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        build_id: builtins.str,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> IBuild:
        '''(experimental) Import an existing build from its attributes.

        :param scope: -
        :param id: -
        :param build_id: (experimental) The identifier of the build.
        :param role: (experimental) The IAM role assumed by GameLift to access server build in S3. Default: - undefined

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Build.from_build_attributes)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = BuildAttributes(build_id=build_id, role=role)

        return typing.cast(IBuild, jsii.sinvoke(cls, "fromBuildAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromBuildId")
    @builtins.classmethod
    def from_build_id(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        build_id: builtins.str,
    ) -> IBuild:
        '''(experimental) Import a build into CDK using its identifier.

        :param scope: -
        :param id: -
        :param build_id: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Build.from_build_id)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
        return typing.cast(IBuild, jsii.sinvoke(cls, "fromBuildId", [scope, id, build_id]))

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        '''(experimental) The Identifier of the build.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "buildId"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal this GameLift Build is using.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        '''(experimental) The IAM role GameLift assumes to acccess server build content.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IRole, jsii.get(self, "role"))


__all__ = [
    "AssetContent",
    "Build",
    "BuildAttributes",
    "BuildBase",
    "BuildProps",
    "Content",
    "ContentConfig",
    "IBuild",
    "IScript",
    "OperatingSystem",
    "S3Content",
    "Script",
    "ScriptAttributes",
    "ScriptBase",
    "ScriptProps",
]

publication.publish()
