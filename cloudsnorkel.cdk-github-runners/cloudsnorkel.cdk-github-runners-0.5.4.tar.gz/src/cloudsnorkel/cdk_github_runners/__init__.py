'''
# GitHub Self-Hosted Runners CDK Constructs

[![NPM](https://img.shields.io/npm/v/@cloudsnorkel/cdk-github-runners?label=npm&logo=npm)](https://www.npmjs.com/package/@cloudsnorkel/cdk-github-runners)
[![PyPI](https://img.shields.io/pypi/v/cloudsnorkel.cdk-github-runners?label=pypi&logo=pypi)](https://pypi.org/project/cloudsnorkel.cdk-github-runners)
[![Maven Central](https://img.shields.io/maven-central/v/com.cloudsnorkel/cdk.github.runners.svg?label=Maven%20Central&logo=java)](https://search.maven.org/search?q=g:%22com.cloudsnorkel%22%20AND%20a:%22cdk.github.runners%22)
[![Go](https://img.shields.io/github/v/tag/CloudSnorkel/cdk-github-runners?color=red&label=go&logo=go)](https://pkg.go.dev/github.com/CloudSnorkel/cdk-github-runners-go/cloudsnorkelcdkgithubrunners)
[![Nuget](https://img.shields.io/nuget/v/CloudSnorkel.Cdk.Github.Runners?color=red&&logo=nuget)](https://www.nuget.org/packages/CloudSnorkel.Cdk.Github.Runners/)
[![Release](https://github.com/CloudSnorkel/cdk-github-runners/actions/workflows/release.yml/badge.svg)](https://github.com/CloudSnorkel/cdk-github-runners/actions/workflows/release.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://github.com/CloudSnorkel/cdk-github-runners/blob/main/LICENSE)

Use this CDK construct to create ephemeral [self-hosted GitHub runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) on-demand inside your AWS account.

* Easy to configure GitHub integration with a web-based interface
* Customizable runners with decent defaults
* Multiple runner configurations controlled by labels
* Everything fully hosted in your account
* Automatically updated build environment with latest runner version

Self-hosted runners in AWS are useful when:

* You need easy access to internal resources in your actions
* You want to pre-install some software for your actions
* You want to provide some basic AWS API access (but [aws-actions/configure-aws-credentials](https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions) has more security controls)

Ephemeral (or on-demand) runners are the [recommended way by GitHub](https://docs.github.com/en/actions/hosting-your-own-runners/autoscaling-with-self-hosted-runners#using-ephemeral-runners-for-autoscaling) for auto-scaling, and they make sure all jobs run with a clean image. Runners are started on-demand. You don't pay unless a job is running.

## API

The best way to browse API documentation is on [Constructs Hub](https://constructs.dev/packages/@cloudsnorkel/cdk-github-runners/). It is available in all supported programming languages.

## Providers

A runner provider creates compute resources on-demand and uses [actions/runner](https://github.com/actions/runner) to start a runner.

|                  | CodeBuild                  | Fargate        | Lambda        |
|------------------|----------------------------|----------------|---------------|
| **Time limit**   | 8 hours                    | Unlimited      | 15 minutes    |
| **vCPUs**        | 2, 4, 8, or 72             | 0.25 to 4      | 1 to 6        |
| **RAM**          | 3gb, 7gb, 15gb, or 145gb   | 512mb to 30gb  | 128mb to 10gb |
| **Storage**      | 50gb to 824gb              | 20gb to 200gb  | Up to 10gb    |
| **Architecture** | x86_64, ARM64              | x86_64, ARM64  | x86_64, ARM64 |
| **sudo**         | ✔                         | ✔              | ❌           |
| **Docker**       | ✔ (Linux only)            | ❌              | ❌           |
| **Spot pricing** | ❌                         | ✔              | ❌           |
| **OS**           | Linux, Windows             | Linux, Windows | Linux         |

The best provider to use mostly depends on your current infrastructure. When in doubt, CodeBuild is always a good choice. Execution history and logs are easy to view, and it has no restrictive limits unless you need to run for more than 8 hours.

You can also create your own provider by implementing `IRunnerProvider`.

## Installation

1. Confirm you're using CDK v2
2. Install the appropriate package

   1. [Python](https://pypi.org/project/cloudsnorkel.cdk-github-runners)

      ```
      pip install cloudsnorkel.cdk-github-runners
      ```
   2. [TypeScript or JavaScript](https://www.npmjs.com/package/@cloudsnorkel/cdk-github-runners)

      ```
      npm i @cloudsnorkel/cdk-github-runners
      ```
   3. [Java](https://search.maven.org/search?q=g:%22com.cloudsnorkel%22%20AND%20a:%22cdk.github.runners%22)

      ```xml
      <dependency>
      <groupId>com.cloudsnorkel</groupId>
      <artifactId>cdk.github.runners</artifactId>
      </dependency>
      ```
   4. [Go](https://pkg.go.dev/github.com/CloudSnorkel/cdk-github-runners-go/cloudsnorkelcdkgithubrunners)

      ```
      go get github.com/CloudSnorkel/cdk-github-runners-go/cloudsnorkelcdkgithubrunners
      ```
   5. [.NET](https://www.nuget.org/packages/CloudSnorkel.Cdk.Github.Runners/)

      ```
      dotnet add package CloudSnorkel.Cdk.Github.Runners
      ```
3. Use `GitHubRunners` construct in your code (starting with default arguments is fine)
4. Deploy your stack
5. Look for the status command output similar to `aws --region us-east-1 lambda invoke --function-name status-XYZ123 status.json`
6. Execute the status command (you may need to specify `--profile` too) and open the resulting `status.json` file
7. Open the URL in `github.setup.url` from `status.json` or [manually setup GitHub](SETUP_GITHUB.md) integration as an app or with personal access token
8. Run status command again to confirm `github.auth.status` and `github.webhook.status` are OK
9. Trigger a GitHub action that has a `self-hosted` label with `runs-on: [self-hosted, linux, codebuild]` or similar
10. If the action is not successful, see [troubleshooting](#Troubleshooting)

[![Demo](demo-thumbnail.jpg)](https://youtu.be/wlyv_3V8lIw)

## Customizing

The default providers configured by `GitHubRunners` are useful for testing but probably not too much for actual production work. They run in the default VPC or no VPC and have no added IAM permissions. You would usually want to configure the providers yourself.

For example:

```python
let vpc: ec2.Vpc;
let runnerSg: ec2.SecurityGroup;
let dbSg: ec2.SecurityGroup;
let bucket: s3.Bucket;

// create a custom CodeBuild provider
const myProvider = new CodeBuildRunner(this, 'codebuild runner', {
  label: 'my-codebuild',
  vpc: vpc,
  securityGroup: runnerSg,
});
// grant some permissions to the provider
bucket.grantReadWrite(myProvider);
dbSg.connections.allowFrom(runnerSg, ec2.Port.tcp(3306), 'allow runners to connect to MySQL database');

// create the runner infrastructure
new GitHubRunners(this, 'runners', {
   providers: [myProvider],
});
```

Another way to customize runners is by modifying the image used to spin them up. The image contains the [runner](https://github.com/actions/runner), any required dependencies, and integration code with the provider. You may choose to customize this image by adding more packages, for example.

```python
const myBuilder = new CodeBuildImageBuilder(this, 'image builder', {
  dockerfilePath: FargateRunner.LINUX_X64_DOCKERFILE_PATH,
  runnerVersion: RunnerVersion.specific('2.291.0'),
  rebuildInterval: Duration.days(14),
});
myBuilder.setBuildArg('EXTRA_PACKAGES', 'nginx xz-utils');

const myProvider = new FargateRunner(this, 'fargate runner', {
  label: 'customized-fargate',
  vpc: vpc,
  securityGroup: runnerSg,
  imageBuilder: myBuilder,
});

// create the runner infrastructure
new GitHubRunners(stack, 'runners', {
  providers: [myProvider],
});
```

Your workflow will then look like:

```yaml
name: self-hosted example
on: push
jobs:
  self-hosted:
    runs-on: [self-hosted, customized-fargate]
    steps:
      - run: echo hello world
```

Windows images must be built with AWS Image Builder.

```python
const myWindowsBuilder = new ContainerImageBuilder(this, 'Windows image builder', {
  architecture: Architecture.X86_64,
  os: Os.WINDOWS,
  runnerVersion: RunnerVersion.specific('2.291.0'),
  rebuildInterval: Duration.days(14),
});
myWindowsBuilder.addComponent(new ImageBuilderComponent(this, 'Ninja Component',
  {
    displayName: 'Ninja',
    description: 'Download and install Ninja build system',
    platform: 'Windows',
    commands: [
      'Invoke-WebRequest -UseBasicParsing -Uri "https://github.com/ninja-build/ninja/releases/download/v1.11.1/ninja-win.zip" -OutFile ninja.zip',
      'Expand-Archive ninja.zip -DestinationPath C:\\actions',
      'del ninja.zip',
    ],
  }
));

const myProvider = new FargateRunner(this, 'fargate runner', {
  label: 'customized-windows-fargate',
  vpc: vpc,
  securityGroup: runnerSg,
  imageBuiler: myWindowsBuilder,
});

// create the runner infrastructure
new GitHubRunners(stack, 'runners', {
  providers: [myProvider],
});
```

## Architecture

![Architecture diagram](architecture.svg)

## Troubleshooting

1. Always start with the status function, make sure no errors are reported, and confirm all status codes are OK
2. Confirm the webhook Lambda was called by visiting the URL in `troubleshooting.webhookHandlerUrl` from `status.json`

   1. If it's not called or logs errors, confirm the webhook settings on the GitHub side
   2. If you see too many errors, make sure you're only sending `workflow_job` events
3. When using GitHub app, make sure there are active installation in `github.auth.app.installations`
4. Check execution details of the orchestrator step function by visiting the URL in `troubleshooting.stepFunctionUrl` from `status.json`

   1. Use the details tab to find the specific execution of the provider (Lambda, CodeBuild, Fargate, etc.)
   2. Every step function execution should be successful, even if the runner action inside it failed

## Other Options

1. [philips-labs/terraform-aws-github-runner](https://github.com/philips-labs/terraform-aws-github-runner) if you're using Terraform
2. [actions-runner-controller/actions-runner-controller](https://github.com/actions-runner-controller/actions-runner-controller) if you're using Kubernetes
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
import aws_cdk.aws_codebuild
import aws_cdk.aws_ec2
import aws_cdk.aws_ecr
import aws_cdk.aws_ecs
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_s3_assets
import aws_cdk.aws_secretsmanager
import aws_cdk.aws_stepfunctions
import constructs


class Architecture(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.Architecture",
):
    '''(experimental) CPU architecture enum for an image.

    :stability: experimental
    '''

    @jsii.member(jsii_name="is")
    def is_(self, arch: "Architecture") -> builtins.bool:
        '''(experimental) Checks if the given architecture is the same as this one.

        :param arch: architecture to compare.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Architecture.is_)
            check_type(argname="argument arch", value=arch, expected_type=type_hints["arch"])
        return typing.cast(builtins.bool, jsii.invoke(self, "is", [arch]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARM64")
    def ARM64(cls) -> "Architecture":
        '''(experimental) ARM64.

        :stability: experimental
        '''
        return typing.cast("Architecture", jsii.sget(cls, "ARM64"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="X86_64")
    def X86_64(cls) -> "Architecture":
        '''(experimental) X86_64.

        :stability: experimental
        '''
        return typing.cast("Architecture", jsii.sget(cls, "X86_64"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildImageBuilderProps",
    jsii_struct_bases=[],
    name_mapping={
        "dockerfile_path": "dockerfilePath",
        "architecture": "architecture",
        "compute_type": "computeType",
        "log_removal_policy": "logRemovalPolicy",
        "log_retention": "logRetention",
        "os": "os",
        "rebuild_interval": "rebuildInterval",
        "runner_version": "runnerVersion",
        "security_group": "securityGroup",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class CodeBuildImageBuilderProps:
    def __init__(
        self,
        *,
        dockerfile_path: builtins.str,
        architecture: typing.Optional[Architecture] = None,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional["Os"] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional["RunnerVersion"] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for CodeBuildImageBuilder construct.

        :param dockerfile_path: (experimental) Path to Dockerfile to be built. It can be a path to a Dockerfile, a folder containing a Dockerfile, or a zip file containing a Dockerfile.
        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (experimental) Security Group to assign to this instance. Default: public project with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to build the image in. Default: no VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilderProps.__init__)
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument log_removal_policy", value=log_removal_policy, expected_type=type_hints["log_removal_policy"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument rebuild_interval", value=rebuild_interval, expected_type=type_hints["rebuild_interval"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {
            "dockerfile_path": dockerfile_path,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if log_removal_policy is not None:
            self._values["log_removal_policy"] = log_removal_policy
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if os is not None:
            self._values["os"] = os
        if rebuild_interval is not None:
            self._values["rebuild_interval"] = rebuild_interval
        if runner_version is not None:
            self._values["runner_version"] = runner_version
        if security_group is not None:
            self._values["security_group"] = security_group
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def dockerfile_path(self) -> builtins.str:
        '''(experimental) Path to Dockerfile to be built.

        It can be a path to a Dockerfile, a folder containing a Dockerfile, or a zip file containing a Dockerfile.

        :stability: experimental
        '''
        result = self._values.get("dockerfile_path")
        assert result is not None, "Required property 'dockerfile_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[Architecture]:
        '''(experimental) Image architecture.

        :default: Architecture.X86_64

        :stability: experimental
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[Architecture], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[aws_cdk.aws_codebuild.ComputeType]:
        '''(experimental) The type of compute to use for this build.

        See the {@link ComputeType} enum for the possible values.

        :default: {@link ComputeType#SMALL}

        :stability: experimental
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[aws_cdk.aws_codebuild.ComputeType], result)

    @builtins.property
    def log_removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) Removal policy for logs of image builds.

        If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed.

        We try to not leave anything behind when removed. But sometimes a log staying behind is useful.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("log_removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def os(self) -> typing.Optional["Os"]:
        '''(experimental) Image OS.

        :default: OS.LINUX

        :stability: experimental
        '''
        result = self._values.get("os")
        return typing.cast(typing.Optional["Os"], result)

    @builtins.property
    def rebuild_interval(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) Schedule the image to be rebuilt every given interval.

        Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates.

        Set to zero to disable.

        :default: Duration.days(7)

        :stability: experimental
        '''
        result = self._values.get("rebuild_interval")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def runner_version(self) -> typing.Optional["RunnerVersion"]:
        '''(experimental) Version of GitHub Runners to install.

        :default: latest version available

        :stability: experimental
        '''
        result = self._values.get("runner_version")
        return typing.cast(typing.Optional["RunnerVersion"], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security Group to assign to this instance.

        :default: public project with no security group

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: no subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)

        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to build the image in.

        :default: no VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildImageBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.ContainerImageBuilderProps",
    jsii_struct_bases=[],
    name_mapping={
        "architecture": "architecture",
        "instance_type": "instanceType",
        "log_removal_policy": "logRemovalPolicy",
        "log_retention": "logRetention",
        "os": "os",
        "parent_image": "parentImage",
        "rebuild_interval": "rebuildInterval",
        "runner_version": "runnerVersion",
        "security_group": "securityGroup",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
    },
)
class ContainerImageBuilderProps:
    def __init__(
        self,
        *,
        architecture: typing.Optional[Architecture] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional["Os"] = None,
        parent_image: typing.Optional[builtins.str] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional["RunnerVersion"] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for ContainerImageBuilder construct.

        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param instance_type: (experimental) The instance type used to build the image. Default: m5.large
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param parent_image: (experimental) Parent image for the new Docker Image. You can use either Image Builder image ARN or public registry image. Default: 'mcr.microsoft.com/windows/servercore:ltsc2019-amd64'
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (experimental) Security Group to assign to this instance. Default: default account security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: default VPC subnet
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerImageBuilderProps.__init__)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument log_removal_policy", value=log_removal_policy, expected_type=type_hints["log_removal_policy"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument parent_image", value=parent_image, expected_type=type_hints["parent_image"])
            check_type(argname="argument rebuild_interval", value=rebuild_interval, expected_type=type_hints["rebuild_interval"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if architecture is not None:
            self._values["architecture"] = architecture
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if log_removal_policy is not None:
            self._values["log_removal_policy"] = log_removal_policy
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if os is not None:
            self._values["os"] = os
        if parent_image is not None:
            self._values["parent_image"] = parent_image
        if rebuild_interval is not None:
            self._values["rebuild_interval"] = rebuild_interval
        if runner_version is not None:
            self._values["runner_version"] = runner_version
        if security_group is not None:
            self._values["security_group"] = security_group
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def architecture(self) -> typing.Optional[Architecture]:
        '''(experimental) Image architecture.

        :default: Architecture.X86_64

        :stability: experimental
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[Architecture], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        '''(experimental) The instance type used to build the image.

        :default: m5.large

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.InstanceType], result)

    @builtins.property
    def log_removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) Removal policy for logs of image builds.

        If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed.

        We try to not leave anything behind when removed. But sometimes a log staying behind is useful.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("log_removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def os(self) -> typing.Optional["Os"]:
        '''(experimental) Image OS.

        :default: OS.LINUX

        :stability: experimental
        '''
        result = self._values.get("os")
        return typing.cast(typing.Optional["Os"], result)

    @builtins.property
    def parent_image(self) -> typing.Optional[builtins.str]:
        '''(experimental) Parent image for the new Docker Image.

        You can use either Image Builder image ARN or public registry image.

        :default: 'mcr.microsoft.com/windows/servercore:ltsc2019-amd64'

        :stability: experimental
        '''
        result = self._values.get("parent_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rebuild_interval(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) Schedule the image to be rebuilt every given interval.

        Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates.

        Set to zero to disable.

        :default: Duration.days(7)

        :stability: experimental
        '''
        result = self._values.get("rebuild_interval")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def runner_version(self) -> typing.Optional["RunnerVersion"]:
        '''(experimental) Version of GitHub Runners to install.

        :default: latest version available

        :stability: experimental
        '''
        result = self._values.get("runner_version")
        return typing.cast(typing.Optional["RunnerVersion"], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security Group to assign to this instance.

        :default: default account security group

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: default VPC subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: default account VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerImageBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GitHubRunners(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.GitHubRunners",
):
    '''(experimental) Create all the required infrastructure to provide self-hosted GitHub runners.

    It creates a webhook, secrets, and a step function to orchestrate all runs. Secrets are not automatically filled. See README.md for instructions on how to setup GitHub integration.

    By default, this will create a runner provider of each available type with the defaults. This is good enough for the initial setup stage when you just want to get GitHub integration working::

       new GitHubRunners(this, 'runners');

    Usually you'd want to configure the runner providers so the runners can run in a certain VPC or have certain permissions::

       const vpc = ec2.Vpc.fromLookup(this, 'vpc', { vpcId: 'vpc-1234567' });
       const runnerSg = new ec2.SecurityGroup(this, 'runner security group', { vpc: vpc });
       const dbSg = ec2.SecurityGroup.fromSecurityGroupId(this, 'database security group', 'sg-1234567');
       const bucket = new s3.Bucket(this, 'runner bucket');

       // create a custom CodeBuild provider
       const myProvider = new CodeBuildRunner(
          this, 'codebuild runner',
          {
             label: 'my-codebuild',
             vpc: vpc,
             securityGroup: runnerSg,
          },
       );
       // grant some permissions to the provider
       bucket.grantReadWrite(myProvider);
       dbSg.connections.allowFrom(runnerSg, ec2.Port.tcp(3306), 'allow runners to connect to MySQL database');

       // create the runner infrastructure
       new GitHubRunners(
          this,
          'runners',
          {
            providers: [myProvider],
          }
       );

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        extra_certificates: typing.Optional[builtins.str] = None,
        providers: typing.Optional[typing.Sequence["IRunnerProvider"]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allow_public_subnet: (experimental) Allow management functions to run in public subnets. Lambda Functions in a public subnet can NOT access the internet. Default: false
        :param extra_certificates: (experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed. You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates}:: const imageBuilder = new CodeBuildImageBuilder(this, 'Image Builder with Certs', { dockerfilePath: CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH, }); imageBuilder.addExtraCertificates('path-to-my-extra-certs-folder'); const provider = new CodeBuildRunner(this, 'CodeBuild', { imageBuilder: imageBuilder, }); new GitHubRunners( this, 'runners', { providers: [provider], extraCertificates: 'path-to-my-extra-certs-folder', } );
        :param providers: (experimental) List of runner providers to use. At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job. Default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)
        :param security_group: (experimental) Security group attached to all management functions. Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.
        :param vpc: (experimental) VPC used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
        :param vpc_subnets: (experimental) VPC subnets used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GitHubRunners.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GitHubRunnersProps(
            allow_public_subnet=allow_public_subnet,
            extra_certificates=extra_certificates,
            providers=providers,
            security_group=security_group,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="providers")
    def providers(self) -> typing.List["IRunnerProvider"]:
        '''(experimental) Configured runner providers.

        :stability: experimental
        '''
        return typing.cast(typing.List["IRunnerProvider"], jsii.get(self, "providers"))

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> "Secrets":
        '''(experimental) Secrets for GitHub communication including webhook secret and runner authentication.

        :stability: experimental
        '''
        return typing.cast("Secrets", jsii.get(self, "secrets"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.GitHubRunnersProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_public_subnet": "allowPublicSubnet",
        "extra_certificates": "extraCertificates",
        "providers": "providers",
        "security_group": "securityGroup",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class GitHubRunnersProps:
    def __init__(
        self,
        *,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        extra_certificates: typing.Optional[builtins.str] = None,
        providers: typing.Optional[typing.Sequence["IRunnerProvider"]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for GitHubRunners.

        :param allow_public_subnet: (experimental) Allow management functions to run in public subnets. Lambda Functions in a public subnet can NOT access the internet. Default: false
        :param extra_certificates: (experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed. You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates}:: const imageBuilder = new CodeBuildImageBuilder(this, 'Image Builder with Certs', { dockerfilePath: CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH, }); imageBuilder.addExtraCertificates('path-to-my-extra-certs-folder'); const provider = new CodeBuildRunner(this, 'CodeBuild', { imageBuilder: imageBuilder, }); new GitHubRunners( this, 'runners', { providers: [provider], extraCertificates: 'path-to-my-extra-certs-folder', } );
        :param providers: (experimental) List of runner providers to use. At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job. Default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)
        :param security_group: (experimental) Security group attached to all management functions. Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.
        :param vpc: (experimental) VPC used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
        :param vpc_subnets: (experimental) VPC subnets used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(GitHubRunnersProps.__init__)
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument extra_certificates", value=extra_certificates, expected_type=type_hints["extra_certificates"])
            check_type(argname="argument providers", value=providers, expected_type=type_hints["providers"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if extra_certificates is not None:
            self._values["extra_certificates"] = extra_certificates
        if providers is not None:
            self._values["providers"] = providers
        if security_group is not None:
            self._values["security_group"] = security_group
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Allow management functions to run in public subnets.

        Lambda Functions in a public subnet can NOT access the internet.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_certificates(self) -> typing.Optional[builtins.str]:
        '''(experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed.

        You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates}::

           const imageBuilder = new CodeBuildImageBuilder(this, 'Image Builder with Certs', {
                dockerfilePath: CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH,
           });
           imageBuilder.addExtraCertificates('path-to-my-extra-certs-folder');

           const provider = new CodeBuildRunner(this, 'CodeBuild', {
                imageBuilder: imageBuilder,
           });

           new GitHubRunners(
              this,
              'runners',
              {
                providers: [provider],
                extraCertificates: 'path-to-my-extra-certs-folder',
              }
           );

        :stability: experimental
        '''
        result = self._values.get("extra_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def providers(self) -> typing.Optional[typing.List["IRunnerProvider"]]:
        '''(experimental) List of runner providers to use.

        At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job.

        :default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)

        :stability: experimental
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List["IRunnerProvider"]], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group attached to all management functions.

        Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC used for all management functions.

        Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) VPC subnets used for all management functions.

        Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubRunnersProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IImageBuilder")
class IImageBuilder(typing_extensions.Protocol):
    '''(experimental) Interface for constructs that build an image that can be used in {@link IRunnerProvider}.

    Anything that ends up with an ECR repository containing a Docker image that runs GitHub self-hosted runners can be used. A simple implementation could even point to an existing image and nothing else.

    It's important that the specified image tag be available at the time the repository is available. Providers usually assume the image is ready and will fail if it's not.

    The image can be further updated over time manually or using a schedule as long as it is always written to the same tag.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self) -> "RunnerImage":
        '''(experimental) ECR repository containing the image.

        This method can be called multiple times if the image is bound to multiple providers. Make sure you cache the image when implementing or return an error if this builder doesn't support reusing images.

        :return: image

        :stability: experimental
        '''
        ...


class _IImageBuilderProxy:
    '''(experimental) Interface for constructs that build an image that can be used in {@link IRunnerProvider}.

    Anything that ends up with an ECR repository containing a Docker image that runs GitHub self-hosted runners can be used. A simple implementation could even point to an existing image and nothing else.

    It's important that the specified image tag be available at the time the repository is available. Providers usually assume the image is ready and will fail if it's not.

    The image can be further updated over time manually or using a schedule as long as it is always written to the same tag.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IImageBuilder"

    @jsii.member(jsii_name="bind")
    def bind(self) -> "RunnerImage":
        '''(experimental) ECR repository containing the image.

        This method can be called multiple times if the image is bound to multiple providers. Make sure you cache the image when implementing or return an error if this builder doesn't support reusing images.

        :return: image

        :stability: experimental
        '''
        return typing.cast("RunnerImage", jsii.invoke(self, "bind", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageBuilder).__jsii_proxy_class__ = lambda : _IImageBuilderProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IRunnerImageStatus")
class IRunnerImageStatus(typing_extensions.Protocol):
    '''(experimental) Interface for runner image status used by status.json.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageBuilderLogGroup")
    def image_builder_log_group(self) -> typing.Optional[builtins.str]:
        '''(experimental) Log group name for the image builder where history of image builds can be analyzed.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="imageRepository")
    def image_repository(self) -> typing.Optional[builtins.str]:
        '''(experimental) Image repository where runner image is pushed.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> typing.Optional[builtins.str]:
        '''(experimental) Tag of image that should be used.

        :stability: experimental
        '''
        ...


class _IRunnerImageStatusProxy:
    '''(experimental) Interface for runner image status used by status.json.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IRunnerImageStatus"

    @builtins.property
    @jsii.member(jsii_name="imageBuilderLogGroup")
    def image_builder_log_group(self) -> typing.Optional[builtins.str]:
        '''(experimental) Log group name for the image builder where history of image builds can be analyzed.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageBuilderLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="imageRepository")
    def image_repository(self) -> typing.Optional[builtins.str]:
        '''(experimental) Image repository where runner image is pushed.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRepository"))

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> typing.Optional[builtins.str]:
        '''(experimental) Tag of image that should be used.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageTag"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunnerImageStatus).__jsii_proxy_class__ = lambda : _IRunnerImageStatusProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IRunnerProvider")
class IRunnerProvider(
    aws_cdk.aws_ec2.IConnectable,
    aws_cdk.aws_iam.IGrantable,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for all runner providers.

    Implementations create all required resources and return a step function task that starts those resources from {@link getStepFunctionTask}.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "RunnerImage":
        '''(experimental) Image used to create a new resource compute.

        Can be Docker image, AMI, or something else.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        '''(experimental) GitHub Actions label associated with this runner provider.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group associated with runners.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC network in which runners will be placed.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function tasks that execute the runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        ...


class _IRunnerProviderProxy(
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_iam.IGrantable), # type: ignore[misc]
):
    '''(experimental) Interface for all runner providers.

    Implementations create all required resources and return a step function task that starts those resources from {@link getStepFunctionTask}.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IRunnerProvider"

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "RunnerImage":
        '''(experimental) Image used to create a new resource compute.

        Can be Docker image, AMI, or something else.

        :stability: experimental
        '''
        return typing.cast("RunnerImage", jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        '''(experimental) GitHub Actions label associated with this runner provider.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group associated with runners.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC network in which runners will be placed.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], jsii.get(self, "vpc"))

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function tasks that execute the runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunnerProvider).__jsii_proxy_class__ = lambda : _IRunnerProviderProxy


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.ImageBuilderAsset",
    jsii_struct_bases=[],
    name_mapping={"asset": "asset", "path": "path"},
)
class ImageBuilderAsset:
    def __init__(
        self,
        *,
        asset: aws_cdk.aws_s3_assets.Asset,
        path: builtins.str,
    ) -> None:
        '''(experimental) An asset including file or directory to place inside the built image.

        :param asset: (experimental) Asset to place in the image.
        :param path: (experimental) Path to place asset in the image.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImageBuilderAsset.__init__)
            check_type(argname="argument asset", value=asset, expected_type=type_hints["asset"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "asset": asset,
            "path": path,
        }

    @builtins.property
    def asset(self) -> aws_cdk.aws_s3_assets.Asset:
        '''(experimental) Asset to place in the image.

        :stability: experimental
        '''
        result = self._values.get("asset")
        assert result is not None, "Required property 'asset' is missing"
        return typing.cast(aws_cdk.aws_s3_assets.Asset, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''(experimental) Path to place asset in the image.

        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageBuilderAsset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImageBuilderComponent(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.ImageBuilderComponent",
):
    '''(experimental) Components are a set of commands to run and optional files to add to an image.

    Components are the building blocks of images built by Image Builder.

    Example::

       new ImageBuilderComponent(this, 'AWS CLI', {
          platform: 'Windows',
          displayName: 'AWS CLI',
          description: 'Install latest version of AWS CLI',
          commands: [
            '$ErrorActionPreference = \\'Stop\\'',
            'Start-Process msiexec.exe -Wait -ArgumentList \\'/i https://awscli.amazonaws.com/AWSCLIV2.msi /qn\\'',
          ],
       }

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        commands: typing.Sequence[builtins.str],
        description: builtins.str,
        display_name: builtins.str,
        platform: builtins.str,
        assets: typing.Optional[typing.Sequence[typing.Union[ImageBuilderAsset, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param commands: (experimental) Shell commands to run when adding this component to the image. On Linux, these are bash commands. On Windows, there are PowerShell commands.
        :param description: (experimental) Component description.
        :param display_name: (experimental) Component display name.
        :param platform: (experimental) Component platform. Must match the builder platform.
        :param assets: (experimental) Optional assets to add to the built image.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImageBuilderComponent.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ImageBuilderComponentProperties(
            commands=commands,
            description=description,
            display_name=display_name,
            platform=platform,
            assets=assets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="grantAssetsRead")
    def grant_assets_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> None:
        '''(experimental) Grants read permissions to the principal on the assets buckets.

        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImageBuilderComponent.grant_assets_read)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(None, jsii.invoke(self, "grantAssetsRead", [grantee]))

    @jsii.member(jsii_name="version")
    def _version(
        self,
        type: builtins.str,
        name: builtins.str,
        data: typing.Any,
    ) -> builtins.str:
        '''
        :param type: -
        :param name: -
        :param data: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImageBuilderComponent._version)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        return typing.cast(builtins.str, jsii.invoke(self, "version", [type, name, data]))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) Component ARN.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''(experimental) Supported platform for the component.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "platform"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.ImageBuilderComponentProperties",
    jsii_struct_bases=[],
    name_mapping={
        "commands": "commands",
        "description": "description",
        "display_name": "displayName",
        "platform": "platform",
        "assets": "assets",
    },
)
class ImageBuilderComponentProperties:
    def __init__(
        self,
        *,
        commands: typing.Sequence[builtins.str],
        description: builtins.str,
        display_name: builtins.str,
        platform: builtins.str,
        assets: typing.Optional[typing.Sequence[typing.Union[ImageBuilderAsset, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Properties for ImageBuilderComponent construct.

        :param commands: (experimental) Shell commands to run when adding this component to the image. On Linux, these are bash commands. On Windows, there are PowerShell commands.
        :param description: (experimental) Component description.
        :param display_name: (experimental) Component display name.
        :param platform: (experimental) Component platform. Must match the builder platform.
        :param assets: (experimental) Optional assets to add to the built image.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ImageBuilderComponentProperties.__init__)
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument assets", value=assets, expected_type=type_hints["assets"])
        self._values: typing.Dict[str, typing.Any] = {
            "commands": commands,
            "description": description,
            "display_name": display_name,
            "platform": platform,
        }
        if assets is not None:
            self._values["assets"] = assets

    @builtins.property
    def commands(self) -> typing.List[builtins.str]:
        '''(experimental) Shell commands to run when adding this component to the image.

        On Linux, these are bash commands. On Windows, there are PowerShell commands.

        :stability: experimental
        '''
        result = self._values.get("commands")
        assert result is not None, "Required property 'commands' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> builtins.str:
        '''(experimental) Component description.

        :stability: experimental
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''(experimental) Component display name.

        :stability: experimental
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''(experimental) Component platform.

        Must match the builder platform.

        :stability: experimental
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assets(self) -> typing.Optional[typing.List[ImageBuilderAsset]]:
        '''(experimental) Optional assets to add to the built image.

        :stability: experimental
        '''
        result = self._values.get("assets")
        return typing.cast(typing.Optional[typing.List[ImageBuilderAsset]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageBuilderComponentProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRunnerProvider)
class LambdaRunner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.LambdaRunner",
):
    '''(experimental) GitHub Actions runner provider using Lambda to execute the actions.

    Creates a Docker-based function that gets executed for each job.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ephemeral_storage_size: (experimental) The size of the function’s /tmp directory in MiB. Default: 10 GiB
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. The default command (``CMD``) should be ``["runner.handler"]`` which points to an included ``runner.js`` with a function named ``handler``. The function should start the GitHub runner. Default: image builder with LambdaRunner.LINUX_X64_DOCKERFILE_PATH as Dockerfile
        :param label: (experimental) GitHub Actions label used for this provider. Default: 'lambda'
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 2048
        :param security_group: (experimental) Security Group to assign to this instance. Default: public lambda with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LambdaRunner.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaRunnerProps(
            ephemeral_storage_size=ephemeral_storage_size,
            image_builder=image_builder,
            label=label,
            memory_size=memory_size,
            security_group=security_group,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64_DOCKERFILE_PATH")
    def LINUX_ARM64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux ARM64 with all the requirement for Lambda runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be similar to public.ecr.aws/lambda/nodejs:14.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_ARM64_DOCKERFILE_PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_X64_DOCKERFILE_PATH")
    def LINUX_X64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux x64 with all the requirement for Lambda runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be similar to public.ecr.aws/lambda/nodejs:14.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_X64_DOCKERFILE_PATH"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> aws_cdk.aws_lambda.Function:
        '''(experimental) The function hosting the GitHub runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_lambda.Function, jsii.get(self, "function"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "RunnerImage":
        '''(experimental) Docker image used to start Lambda function.

        :stability: experimental
        '''
        return typing.cast("RunnerImage", jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        '''(experimental) Label associated with this provider.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group attached to the function.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC used for hosting the function.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], jsii.get(self, "vpc"))


class Os(metaclass=jsii.JSIIMeta, jsii_type="@cloudsnorkel/cdk-github-runners.Os"):
    '''(experimental) OS enum for an image.

    :stability: experimental
    '''

    @jsii.member(jsii_name="is")
    def is_(self, os: "Os") -> builtins.bool:
        '''(experimental) Checks if the given OS is the same as this one.

        :param os: OS to compare.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Os.is_)
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        return typing.cast(builtins.bool, jsii.invoke(self, "is", [os]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX")
    def LINUX(cls) -> "Os":
        '''(experimental) Linux.

        :stability: experimental
        '''
        return typing.cast("Os", jsii.sget(cls, "LINUX"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WINDOWS")
    def WINDOWS(cls) -> "Os":
        '''(experimental) Windows.

        :stability: experimental
        '''
        return typing.cast("Os", jsii.sget(cls, "WINDOWS"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerImage",
    jsii_struct_bases=[],
    name_mapping={
        "architecture": "architecture",
        "image_repository": "imageRepository",
        "image_tag": "imageTag",
        "os": "os",
        "log_group": "logGroup",
    },
)
class RunnerImage:
    def __init__(
        self,
        *,
        architecture: Architecture,
        image_repository: aws_cdk.aws_ecr.IRepository,
        image_tag: builtins.str,
        os: Os,
        log_group: typing.Optional[aws_cdk.aws_logs.LogGroup] = None,
    ) -> None:
        '''
        :param architecture: (experimental) Architecture of the image.
        :param image_repository: (experimental) ECR repository containing the image.
        :param image_tag: (experimental) Static image tag where the image will be pushed.
        :param os: (experimental) OS type of the image.
        :param log_group: (experimental) Log group where image builds are logged.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RunnerImage.__init__)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument image_repository", value=image_repository, expected_type=type_hints["image_repository"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "architecture": architecture,
            "image_repository": image_repository,
            "image_tag": image_tag,
            "os": os,
        }
        if log_group is not None:
            self._values["log_group"] = log_group

    @builtins.property
    def architecture(self) -> Architecture:
        '''(experimental) Architecture of the image.

        :stability: experimental
        '''
        result = self._values.get("architecture")
        assert result is not None, "Required property 'architecture' is missing"
        return typing.cast(Architecture, result)

    @builtins.property
    def image_repository(self) -> aws_cdk.aws_ecr.IRepository:
        '''(experimental) ECR repository containing the image.

        :stability: experimental
        '''
        result = self._values.get("image_repository")
        assert result is not None, "Required property 'image_repository' is missing"
        return typing.cast(aws_cdk.aws_ecr.IRepository, result)

    @builtins.property
    def image_tag(self) -> builtins.str:
        '''(experimental) Static image tag where the image will be pushed.

        :stability: experimental
        '''
        result = self._values.get("image_tag")
        assert result is not None, "Required property 'image_tag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def os(self) -> Os:
        '''(experimental) OS type of the image.

        :stability: experimental
        '''
        result = self._values.get("os")
        assert result is not None, "Required property 'os' is missing"
        return typing.cast(Os, result)

    @builtins.property
    def log_group(self) -> typing.Optional[aws_cdk.aws_logs.LogGroup]:
        '''(experimental) Log group where image builds are logged.

        :stability: experimental
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.LogGroup], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerProviderProps",
    jsii_struct_bases=[],
    name_mapping={"log_retention": "logRetention"},
)
class RunnerProviderProps:
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''(experimental) Common properties for all runner providers.

        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RunnerProviderProps.__init__)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerRuntimeParameters",
    jsii_struct_bases=[],
    name_mapping={
        "github_domain_path": "githubDomainPath",
        "owner_path": "ownerPath",
        "repo_path": "repoPath",
        "runner_name_path": "runnerNamePath",
        "runner_token_path": "runnerTokenPath",
    },
)
class RunnerRuntimeParameters:
    def __init__(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> None:
        '''(experimental) Workflow job parameters as parsed from the webhook event. Pass these into your runner executor and run something like:.

        Example::

           ./config.sh --unattended --url "https://${GITHUB_DOMAIN}/${OWNER}/${REPO}" --token "${RUNNER_TOKEN}" --ephemeral --work _work --labels "${RUNNER_LABEL}" --name "${RUNNER_NAME}" --disableupdate

        All parameters are specified as step function paths and therefore must be used only in step function task parameters.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RunnerRuntimeParameters.__init__)
            check_type(argname="argument github_domain_path", value=github_domain_path, expected_type=type_hints["github_domain_path"])
            check_type(argname="argument owner_path", value=owner_path, expected_type=type_hints["owner_path"])
            check_type(argname="argument repo_path", value=repo_path, expected_type=type_hints["repo_path"])
            check_type(argname="argument runner_name_path", value=runner_name_path, expected_type=type_hints["runner_name_path"])
            check_type(argname="argument runner_token_path", value=runner_token_path, expected_type=type_hints["runner_token_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "github_domain_path": github_domain_path,
            "owner_path": owner_path,
            "repo_path": repo_path,
            "runner_name_path": runner_name_path,
            "runner_token_path": runner_token_path,
        }

    @builtins.property
    def github_domain_path(self) -> builtins.str:
        '''(experimental) Path to GitHub domain.

        Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.

        :stability: experimental
        '''
        result = self._values.get("github_domain_path")
        assert result is not None, "Required property 'github_domain_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner_path(self) -> builtins.str:
        '''(experimental) Path to repostiroy owner name.

        :stability: experimental
        '''
        result = self._values.get("owner_path")
        assert result is not None, "Required property 'owner_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo_path(self) -> builtins.str:
        '''(experimental) Path to repository name.

        :stability: experimental
        '''
        result = self._values.get("repo_path")
        assert result is not None, "Required property 'repo_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runner_name_path(self) -> builtins.str:
        '''(experimental) Path to desired runner name.

        We specifically set the name to make troubleshooting easier.

        :stability: experimental
        '''
        result = self._values.get("runner_name_path")
        assert result is not None, "Required property 'runner_name_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runner_token_path(self) -> builtins.str:
        '''(experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        result = self._values.get("runner_token_path")
        assert result is not None, "Required property 'runner_token_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerRuntimeParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RunnerVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerVersion",
):
    '''(experimental) Defines desired GitHub Actions runner version.

    :stability: experimental
    '''

    def __init__(self, version: builtins.str) -> None:
        '''
        :param version: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RunnerVersion.__init__)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        jsii.create(self.__class__, self, [version])

    @jsii.member(jsii_name="latest")
    @builtins.classmethod
    def latest(cls) -> "RunnerVersion":
        '''(experimental) Use the latest version available at the time the runner provider image is built.

        :stability: experimental
        '''
        return typing.cast("RunnerVersion", jsii.sinvoke(cls, "latest", []))

    @jsii.member(jsii_name="specific")
    @builtins.classmethod
    def specific(cls, version: builtins.str) -> "RunnerVersion":
        '''(experimental) Use a specific version.

        :param version: GitHub Runner version.

        :see: https://github.com/actions/runner/releases
        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RunnerVersion.specific)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("RunnerVersion", jsii.sinvoke(cls, "specific", [version]))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


class Secrets(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.Secrets",
):
    '''(experimental) Secrets required for GitHub runners operation.

    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Secrets.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) Authentication secret for GitHub containing either app details or personal authentication token.

        This secret is used to register runners and
        cancel jobs when the runner fails to start.

        This secret is meant to be edited by the user after being created.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="githubPrivateKey")
    def github_private_key(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) GitHub app private key. Not needed when using personal authentication tokens.

        This secret is meant to be edited by the user after being created. It is separate than the main GitHub secret because inserting private keys into JSON is hard.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "githubPrivateKey"))

    @builtins.property
    @jsii.member(jsii_name="setup")
    def setup(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) Setup secret used to authenticate user for our setup wizard.

        Should be empty after setup has been completed.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "setup"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) Webhook secret used to confirm events are coming from GitHub and nowhere else.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "webhook"))


class StaticRunnerImage(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.StaticRunnerImage",
):
    '''(experimental) Helper class with methods to use static images that are built outside the context of this project.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromDockerHub")
    @builtins.classmethod
    def from_docker_hub(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        image: builtins.str,
        architecture: typing.Optional[Architecture] = None,
        os: typing.Optional[Os] = None,
    ) -> IImageBuilder:
        '''(experimental) Create a builder from an existing Docker Hub image.

        The image must already have GitHub Actions runner installed. You are responsible to update it and remove it when done.

        We create a CodeBuild image builder behind the scenes to copy the image over to ECR. This helps avoid Docker Hub rate limits and prevent failures.

        :param scope: -
        :param id: -
        :param image: Docker Hub image with optional tag.
        :param architecture: image architecture.
        :param os: image OS.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StaticRunnerImage.from_docker_hub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        return typing.cast(IImageBuilder, jsii.sinvoke(cls, "fromDockerHub", [scope, id, image, architecture, os]))

    @jsii.member(jsii_name="fromEcrRepository")
    @builtins.classmethod
    def from_ecr_repository(
        cls,
        repository: aws_cdk.aws_ecr.IRepository,
        tag: typing.Optional[builtins.str] = None,
        architecture: typing.Optional[Architecture] = None,
        os: typing.Optional[Os] = None,
    ) -> IImageBuilder:
        '''(experimental) Create a builder (that doesn't actually build anything) from an existing image in an existing repository.

        The image must already have GitHub Actions runner installed. You are responsible to update it and remove it when done.

        :param repository: ECR repository.
        :param tag: image tag.
        :param architecture: image architecture.
        :param os: image OS.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StaticRunnerImage.from_ecr_repository)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        return typing.cast(IImageBuilder, jsii.sinvoke(cls, "fromEcrRepository", [repository, tag, architecture, os]))


@jsii.implements(IImageBuilder)
class CodeBuildImageBuilder(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildImageBuilder",
):
    '''(experimental) An image builder that uses CodeBuild to build Docker images pre-baked with all the GitHub Actions runner requirements.

    Builders can be used with runner providers.

    Each builder re-runs automatically at a set interval to make sure the images contain the latest versions of everything.

    You can create an instance of this construct to customize the image used to spin-up runners. Each provider has its own requirements for what an image should do. That's why they each provide their own Dockerfile.

    For example, to set a specific runner version, rebuild the image every 2 weeks, and add a few packages for the Fargate provider, use::

       const builder = new CodeBuildImageBuilder(this, 'Builder', {
            dockerfilePath: FargateProvider.LINUX_X64_DOCKERFILE_PATH,
            runnerVersion: RunnerVersion.specific('2.293.0'),
            rebuildInterval: Duration.days(14),
       });
       builder.setBuildArg('EXTRA_PACKAGES', 'nginx xz-utils');
       new FargateRunner(this, 'Fargate provider', {
            label: 'customized-fargate',
            imageBuilder: builder,
       });

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dockerfile_path: builtins.str,
        architecture: typing.Optional[Architecture] = None,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional[Os] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional[RunnerVersion] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dockerfile_path: (experimental) Path to Dockerfile to be built. It can be a path to a Dockerfile, a folder containing a Dockerfile, or a zip file containing a Dockerfile.
        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (experimental) Security Group to assign to this instance. Default: public project with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to build the image in. Default: no VPC

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CodeBuildImageBuilderProps(
            dockerfile_path=dockerfile_path,
            architecture=architecture,
            compute_type=compute_type,
            log_removal_policy=log_removal_policy,
            log_retention=log_retention,
            os=os,
            rebuild_interval=rebuild_interval,
            runner_version=runner_version,
            security_group=security_group,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addExtraCertificates")
    def add_extra_certificates(self, path: builtins.str) -> None:
        '''(experimental) Add extra trusted certificates. This helps deal with self-signed certificates for GitHub Enterprise Server.

        All first party Dockerfiles support this. Others may not.

        :param path: path to directory containing a file called certs.pem containing all the required certificates.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.add_extra_certificates)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(None, jsii.invoke(self, "addExtraCertificates", [path]))

    @jsii.member(jsii_name="addFiles")
    def add_files(self, source_path: builtins.str, dest_name: builtins.str) -> None:
        '''(experimental) Uploads a folder to the build server at a given folder name.

        :param source_path: path to source directory.
        :param dest_name: name of destination folder.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.add_files)
            check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            check_type(argname="argument dest_name", value=dest_name, expected_type=type_hints["dest_name"])
        return typing.cast(None, jsii.invoke(self, "addFiles", [source_path, dest_name]))

    @jsii.member(jsii_name="addPolicyStatement")
    def add_policy_statement(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        '''(experimental) Add a policy statement to the builder to access resources required to the image build.

        :param statement: IAM policy statement.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.add_policy_statement)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addPolicyStatement", [statement]))

    @jsii.member(jsii_name="addPostBuildCommand")
    def add_post_build_command(self, command: builtins.str) -> None:
        '''(experimental) Adds a command that runs after ``docker build`` and ``docker push``.

        :param command: command to add.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.add_post_build_command)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
        return typing.cast(None, jsii.invoke(self, "addPostBuildCommand", [command]))

    @jsii.member(jsii_name="addPreBuildCommand")
    def add_pre_build_command(self, command: builtins.str) -> None:
        '''(experimental) Adds a command that runs before ``docker build``.

        :param command: command to add.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.add_pre_build_command)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
        return typing.cast(None, jsii.invoke(self, "addPreBuildCommand", [command]))

    @jsii.member(jsii_name="bind")
    def bind(self) -> RunnerImage:
        '''(experimental) Called by IRunnerProvider to finalize settings and create the image builder.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.invoke(self, "bind", []))

    @jsii.member(jsii_name="setBuildArg")
    def set_build_arg(self, name: builtins.str, value: builtins.str) -> None:
        '''(experimental) Adds a build argument for Docker.

        See the documentation for the Dockerfile you're using for a list of supported build arguments.

        :param name: build argument name.
        :param value: build argument value.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildImageBuilder.set_build_arg)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "setBuildArg", [name, value]))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> CodeBuildImageBuilderProps:
        '''
        :stability: experimental
        '''
        return typing.cast(CodeBuildImageBuilderProps, jsii.get(self, "props"))


@jsii.implements(IRunnerProvider)
class CodeBuildRunner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildRunner",
):
    '''(experimental) GitHub Actions runner provider using CodeBuild to execute the actions.

    Creates a project that gets started for each job.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. A user named ``runner`` is expected to exist with access to Docker-in-Docker. Default: image builder with ``CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (experimental) GitHub Actions label used for this provider. Default: 'codebuild'
        :param security_group: (experimental) Security Group to assign to this instance. Default: public project with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildRunner.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CodeBuildRunnerProps(
            compute_type=compute_type,
            image_builder=image_builder,
            label=label,
            security_group=security_group,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64_DOCKERFILE_PATH")
    def LINUX_ARM64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux ARM64 with all the requirements for CodeBuild runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.
        - ``DOCKER_CHANNEL`` overrides the channel from which Docker will be downloaded. Defaults to ``"stsable"``.
        - ``DIND_COMMIT`` overrides the commit where dind is found.
        - ``DOCKER_VERSION`` overrides the installed Docker version.
        - ``DOCKER_COMPOSE_VERSION`` overrides the installed docker-compose version.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_ARM64_DOCKERFILE_PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_X64_DOCKERFILE_PATH")
    def LINUX_X64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux x64 with all the requirements for CodeBuild runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.
        - ``DOCKER_CHANNEL`` overrides the channel from which Docker will be downloaded. Defaults to ``"stsable"``.
        - ``DIND_COMMIT`` overrides the commit where dind is found.
        - ``DOCKER_VERSION`` overrides the installed Docker version.
        - ``DOCKER_COMPOSE_VERSION`` overrides the installed docker-compose version.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_X64_DOCKERFILE_PATH"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> RunnerImage:
        '''(experimental) Docker image in CodeBuild project.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        '''(experimental) Label associated with this provider.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> aws_cdk.aws_codebuild.Project:
        '''(experimental) CodeBuild project hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_codebuild.Project, jsii.get(self, "project"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group attached to the task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC used for hosting the project.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildRunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "compute_type": "computeType",
        "image_builder": "imageBuilder",
        "label": "label",
        "security_group": "securityGroup",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class CodeBuildRunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. A user named ``runner`` is expected to exist with access to Docker-in-Docker. Default: image builder with ``CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (experimental) GitHub Actions label used for this provider. Default: 'codebuild'
        :param security_group: (experimental) Security Group to assign to this instance. Default: public project with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(CodeBuildRunnerProps.__init__)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument image_builder", value=image_builder, expected_type=type_hints["image_builder"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if image_builder is not None:
            self._values["image_builder"] = image_builder
        if label is not None:
            self._values["label"] = label
        if security_group is not None:
            self._values["security_group"] = security_group
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[aws_cdk.aws_codebuild.ComputeType]:
        '''(experimental) The type of compute to use for this build.

        See the {@link ComputeType} enum for the possible values.

        :default: {@link ComputeType#SMALL}

        :stability: experimental
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[aws_cdk.aws_codebuild.ComputeType], result)

    @builtins.property
    def image_builder(self) -> typing.Optional[IImageBuilder]:
        '''(experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured.

        A user named ``runner`` is expected to exist with access to Docker-in-Docker.

        :default: image builder with ``CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile

        :stability: experimental
        '''
        result = self._values.get("image_builder")
        return typing.cast(typing.Optional[IImageBuilder], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) GitHub Actions label used for this provider.

        :default: 'codebuild'

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security Group to assign to this instance.

        :default: public project with no security group

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: no subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)

        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: no VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IImageBuilder)
class ContainerImageBuilder(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.ContainerImageBuilder",
):
    '''(experimental) An image builder that uses Image Builder to build Docker images pre-baked with all the GitHub Actions runner requirements.

    Builders can be used with runner providers.

    The CodeBuild builder is better and faster. Only use this one if you have no choice. For example, if you need Windows containers.

    Each builder re-runs automatically at a set interval to make sure the images contain the latest versions of everything.

    You can create an instance of this construct to customize the image used to spin-up runners. Some runner providers may require custom components. Check the runner provider documentation. The default components work with CodeBuild and Fargate.

    For example, to set a specific runner version, rebuild the image every 2 weeks, and add a few packages for the Fargate provider, use::

       const builder = new ContainerImageBuilder(this, 'Builder', {
            runnerVersion: RunnerVersion.specific('2.293.0'),
            rebuildInterval: Duration.days(14),
       });
       new CodeBuildRunner(this, 'CodeBuild provider', {
            label: 'windows-codebuild',
            imageBuilder: builder,
       });

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        architecture: typing.Optional[Architecture] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional[Os] = None,
        parent_image: typing.Optional[builtins.str] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional[RunnerVersion] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param instance_type: (experimental) The instance type used to build the image. Default: m5.large
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param parent_image: (experimental) Parent image for the new Docker Image. You can use either Image Builder image ARN or public registry image. Default: 'mcr.microsoft.com/windows/servercore:ltsc2019-amd64'
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (experimental) Security Group to assign to this instance. Default: default account security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: default VPC subnet
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerImageBuilder.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ContainerImageBuilderProps(
            architecture=architecture,
            instance_type=instance_type,
            log_removal_policy=log_removal_policy,
            log_retention=log_retention,
            os=os,
            parent_image=parent_image,
            rebuild_interval=rebuild_interval,
            runner_version=runner_version,
            security_group=security_group,
            subnet_selection=subnet_selection,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addComponent")
    def add_component(self, component: ImageBuilderComponent) -> None:
        '''(experimental) Add a component to be installed.

        :param component: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerImageBuilder.add_component)
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
        return typing.cast(None, jsii.invoke(self, "addComponent", [component]))

    @jsii.member(jsii_name="addExtraCertificates")
    def add_extra_certificates(self, path: builtins.str) -> None:
        '''(experimental) Add extra trusted certificates. This helps deal with self-signed certificates for GitHub Enterprise Server.

        All first party Dockerfiles support this. Others may not.

        :param path: path to directory containing a file called certs.pem containing all the required certificates.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerImageBuilder.add_extra_certificates)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(None, jsii.invoke(self, "addExtraCertificates", [path]))

    @jsii.member(jsii_name="bind")
    def bind(self) -> RunnerImage:
        '''(experimental) Called by IRunnerProvider to finalize settings and create the image builder.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.invoke(self, "bind", []))

    @jsii.member(jsii_name="prependComponent")
    def prepend_component(self, component: ImageBuilderComponent) -> None:
        '''(experimental) Add a component to be installed before any other components.

        Useful for required system settings like certificates or proxy settings.

        :param component: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerImageBuilder.prepend_component)
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
        return typing.cast(None, jsii.invoke(self, "prependComponent", [component]))

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> Architecture:
        '''
        :stability: experimental
        '''
        return typing.cast(Architecture, jsii.get(self, "architecture"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceTypes"))

    @builtins.property
    @jsii.member(jsii_name="logRemovalPolicy")
    def log_removal_policy(self) -> aws_cdk.RemovalPolicy:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.RemovalPolicy, jsii.get(self, "logRemovalPolicy"))

    @builtins.property
    @jsii.member(jsii_name="logRetention")
    def log_retention(self) -> aws_cdk.aws_logs.RetentionDays:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_logs.RetentionDays, jsii.get(self, "logRetention"))

    @builtins.property
    @jsii.member(jsii_name="os")
    def os(self) -> Os:
        '''
        :stability: experimental
        '''
        return typing.cast(Os, jsii.get(self, "os"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @builtins.property
    @jsii.member(jsii_name="rebuildInterval")
    def rebuild_interval(self) -> aws_cdk.Duration:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.Duration, jsii.get(self, "rebuildInterval"))

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> aws_cdk.aws_ecr.IRepository:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecr.IRepository, jsii.get(self, "repository"))

    @builtins.property
    @jsii.member(jsii_name="runnerVersion")
    def runner_version(self) -> RunnerVersion:
        '''
        :stability: experimental
        '''
        return typing.cast(RunnerVersion, jsii.get(self, "runnerVersion"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))


@jsii.implements(IRunnerProvider)
class FargateRunner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.FargateRunner",
):
    '''(experimental) GitHub Actions runner provider using Fargate to execute the actions.

    Creates a task definition with a single container that gets started for each job.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        cluster: typing.Optional[aws_cdk.aws_ecs.Cluster] = None,
        cpu: typing.Optional[jsii.Number] = None,
        ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        spot: typing.Optional[builtins.bool] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param assign_public_ip: (experimental) Assign public IP to the runner task. Make sure the task will have access to GitHub. A public IP might be required unless you have NAT gateway. Default: true
        :param cluster: (experimental) Existing Fargate cluster to use. Default: a new cluster
        :param cpu: (experimental) The number of cpu units used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) Default: 1024
        :param ephemeral_storage_gib: (experimental) The amount (in GiB) of ephemeral storage to be allocated to the task. The maximum supported value is 200 GiB. NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later. Default: 20
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. A user named ``runner`` is expected to exist. Default: image builder with ``FargateRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (experimental) GitHub Actions label used for this provider. Default: 'fargate'
        :param memory_limit_mib: (experimental) The amount (in MiB) of memory used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Default: 2048
        :param security_group: (experimental) Security Group to assign to the task. Default: a new security group
        :param spot: (experimental) Use Fargate spot capacity provider to save money. - Runners may fail to start due to missing capacity. - Runners might be stopped prematurely with spot pricing. Default: false
        :param subnet_selection: (experimental) Subnets to run the runners in. Default: Fargate default
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FargateRunner.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FargateRunnerProps(
            assign_public_ip=assign_public_ip,
            cluster=cluster,
            cpu=cpu,
            ephemeral_storage_gib=ephemeral_storage_gib,
            image_builder=image_builder,
            label=label,
            memory_limit_mib=memory_limit_mib,
            security_group=security_group,
            spot=spot,
            subnet_selection=subnet_selection,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64_DOCKERFILE_PATH")
    def LINUX_ARM64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux ARM64 with all the requirement for Fargate runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_ARM64_DOCKERFILE_PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_X64_DOCKERFILE_PATH")
    def LINUX_X64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux x64 with all the requirement for Fargate runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_X64_DOCKERFILE_PATH"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(self) -> builtins.bool:
        '''(experimental) Whether runner task will have a public IP.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "assignPublicIp"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> aws_cdk.aws_ecs.Cluster:
        '''(experimental) Cluster hosting the task hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecs.Cluster, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> aws_cdk.aws_ecs.ContainerDefinition:
        '''(experimental) Container definition hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecs.ContainerDefinition, jsii.get(self, "container"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> RunnerImage:
        '''(experimental) Docker image used to start a new Fargate task.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        '''(experimental) Label associated with this provider.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @builtins.property
    @jsii.member(jsii_name="spot")
    def spot(self) -> builtins.bool:
        '''(experimental) Use spot pricing for Fargate tasks.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "spot"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> aws_cdk.aws_ecs.FargateTaskDefinition:
        '''(experimental) Fargate task hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecs.FargateTaskDefinition, jsii.get(self, "task"))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group attached to the task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="subnetSelection")
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Subnets used for hosting the runner task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], jsii.get(self, "subnetSelection"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC used for hosting the runner task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.FargateRunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "assign_public_ip": "assignPublicIp",
        "cluster": "cluster",
        "cpu": "cpu",
        "ephemeral_storage_gib": "ephemeralStorageGiB",
        "image_builder": "imageBuilder",
        "label": "label",
        "memory_limit_mib": "memoryLimitMiB",
        "security_group": "securityGroup",
        "spot": "spot",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
    },
)
class FargateRunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        cluster: typing.Optional[aws_cdk.aws_ecs.Cluster] = None,
        cpu: typing.Optional[jsii.Number] = None,
        ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        spot: typing.Optional[builtins.bool] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for FargateRunner.

        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param assign_public_ip: (experimental) Assign public IP to the runner task. Make sure the task will have access to GitHub. A public IP might be required unless you have NAT gateway. Default: true
        :param cluster: (experimental) Existing Fargate cluster to use. Default: a new cluster
        :param cpu: (experimental) The number of cpu units used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) Default: 1024
        :param ephemeral_storage_gib: (experimental) The amount (in GiB) of ephemeral storage to be allocated to the task. The maximum supported value is 200 GiB. NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later. Default: 20
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. A user named ``runner`` is expected to exist. Default: image builder with ``FargateRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (experimental) GitHub Actions label used for this provider. Default: 'fargate'
        :param memory_limit_mib: (experimental) The amount (in MiB) of memory used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Default: 2048
        :param security_group: (experimental) Security Group to assign to the task. Default: a new security group
        :param spot: (experimental) Use Fargate spot capacity provider to save money. - Runners may fail to start due to missing capacity. - Runners might be stopped prematurely with spot pricing. Default: false
        :param subnet_selection: (experimental) Subnets to run the runners in. Default: Fargate default
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(FargateRunnerProps.__init__)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument ephemeral_storage_gib", value=ephemeral_storage_gib, expected_type=type_hints["ephemeral_storage_gib"])
            check_type(argname="argument image_builder", value=image_builder, expected_type=type_hints["image_builder"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument memory_limit_mib", value=memory_limit_mib, expected_type=type_hints["memory_limit_mib"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if cluster is not None:
            self._values["cluster"] = cluster
        if cpu is not None:
            self._values["cpu"] = cpu
        if ephemeral_storage_gib is not None:
            self._values["ephemeral_storage_gib"] = ephemeral_storage_gib
        if image_builder is not None:
            self._values["image_builder"] = image_builder
        if label is not None:
            self._values["label"] = label
        if memory_limit_mib is not None:
            self._values["memory_limit_mib"] = memory_limit_mib
        if security_group is not None:
            self._values["security_group"] = security_group
        if spot is not None:
            self._values["spot"] = spot
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def assign_public_ip(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Assign public IP to the runner task.

        Make sure the task will have access to GitHub. A public IP might be required unless you have NAT gateway.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cluster(self) -> typing.Optional[aws_cdk.aws_ecs.Cluster]:
        '''(experimental) Existing Fargate cluster to use.

        :default: a new cluster

        :stability: experimental
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[aws_cdk.aws_ecs.Cluster], result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of cpu units used by the task.

        For tasks using the Fargate launch type,
        this field is required and you must use one of the following values,
        which determines your range of valid values for the memory parameter:

        256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)

        512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)

        1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

        2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

        4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)

        :default: 1024

        :stability: experimental
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ephemeral_storage_gib(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount (in GiB) of ephemeral storage to be allocated to the task.

        The maximum supported value is 200 GiB.

        NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later.

        :default: 20

        :stability: experimental
        '''
        result = self._values.get("ephemeral_storage_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image_builder(self) -> typing.Optional[IImageBuilder]:
        '''(experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured.

        A user named ``runner`` is expected to exist.

        :default: image builder with ``FargateRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile

        :stability: experimental
        '''
        result = self._values.get("image_builder")
        return typing.cast(typing.Optional[IImageBuilder], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) GitHub Actions label used for this provider.

        :default: 'fargate'

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_limit_mib(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount (in MiB) of memory used by the task.

        For tasks using the Fargate launch type,
        this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter:

        512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU)

        1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU)

        2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU)

        Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU)

        Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU)

        :default: 2048

        :stability: experimental
        '''
        result = self._values.get("memory_limit_mib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security Group to assign to the task.

        :default: a new security group

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def spot(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Use Fargate spot capacity provider to save money.

        - Runners may fail to start due to missing capacity.
        - Runners might be stopped prematurely with spot pricing.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Subnets to run the runners in.

        :default: Fargate default

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: default account VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.LambdaRunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "image_builder": "imageBuilder",
        "label": "label",
        "memory_size": "memorySize",
        "security_group": "securityGroup",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class LambdaRunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param ephemeral_storage_size: (experimental) The size of the function’s /tmp directory in MiB. Default: 10 GiB
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. The default command (``CMD``) should be ``["runner.handler"]`` which points to an included ``runner.js`` with a function named ``handler``. The function should start the GitHub runner. Default: image builder with LambdaRunner.LINUX_X64_DOCKERFILE_PATH as Dockerfile
        :param label: (experimental) GitHub Actions label used for this provider. Default: 'lambda'
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 2048
        :param security_group: (experimental) Security Group to assign to this instance. Default: public lambda with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            type_hints = typing.get_type_hints(LambdaRunnerProps.__init__)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument image_builder", value=image_builder, expected_type=type_hints["image_builder"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if image_builder is not None:
            self._values["image_builder"] = image_builder
        if label is not None:
            self._values["label"] = label
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if security_group is not None:
            self._values["security_group"] = security_group
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[aws_cdk.Size]:
        '''(experimental) The size of the function’s /tmp directory in MiB.

        :default: 10 GiB

        :stability: experimental
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[aws_cdk.Size], result)

    @builtins.property
    def image_builder(self) -> typing.Optional[IImageBuilder]:
        '''(experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured.

        The default command (``CMD``) should be ``["runner.handler"]`` which points to an included ``runner.js`` with a function named ``handler``. The function should start the GitHub runner.

        :default: image builder with LambdaRunner.LINUX_X64_DOCKERFILE_PATH as Dockerfile

        :see: https://github.com/CloudSnorkel/cdk-github-runners/tree/main/src/providers/docker-images/lambda
        :stability: experimental
        '''
        result = self._values.get("image_builder")
        return typing.cast(typing.Optional[IImageBuilder], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) GitHub Actions label used for this provider.

        :default: 'lambda'

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 2048

        :stability: experimental
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security Group to assign to this instance.

        :default: public lambda with no security group

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: no subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.minutes(15)

        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: no VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Architecture",
    "CodeBuildImageBuilder",
    "CodeBuildImageBuilderProps",
    "CodeBuildRunner",
    "CodeBuildRunnerProps",
    "ContainerImageBuilder",
    "ContainerImageBuilderProps",
    "FargateRunner",
    "FargateRunnerProps",
    "GitHubRunners",
    "GitHubRunnersProps",
    "IImageBuilder",
    "IRunnerImageStatus",
    "IRunnerProvider",
    "ImageBuilderAsset",
    "ImageBuilderComponent",
    "ImageBuilderComponentProperties",
    "LambdaRunner",
    "LambdaRunnerProps",
    "Os",
    "RunnerImage",
    "RunnerProviderProps",
    "RunnerRuntimeParameters",
    "RunnerVersion",
    "Secrets",
    "StaticRunnerImage",
]

publication.publish()
