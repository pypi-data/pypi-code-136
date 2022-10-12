'''
# `docker_container`

Refer to the Terraform Registory for docs: [`docker_container`](https://www.terraform.io/docs/providers/docker/r/container).
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


class Container(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.Container",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/docker/r/container docker_container}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        image: builtins.str,
        name: builtins.str,
        attach: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        capabilities: typing.Optional[typing.Union["ContainerCapabilities", typing.Dict[str, typing.Any]]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_read_refresh_timeout_milliseconds: typing.Optional[jsii.Number] = None,
        cpu_set: typing.Optional[builtins.str] = None,
        cpu_shares: typing.Optional[jsii.Number] = None,
        destroy_grace_seconds: typing.Optional[jsii.Number] = None,
        devices: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerDevices", typing.Dict[str, typing.Any]]]]] = None,
        dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_search: typing.Optional[typing.Sequence[builtins.str]] = None,
        domainname: typing.Optional[builtins.str] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        gpus: typing.Optional[builtins.str] = None,
        group_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        healthcheck: typing.Optional[typing.Union["ContainerHealthcheck", typing.Dict[str, typing.Any]]] = None,
        host: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerHost", typing.Dict[str, typing.Any]]]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        init: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerLabels", typing.Dict[str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_driver: typing.Optional[builtins.str] = None,
        log_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_retry_count: typing.Optional[jsii.Number] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_swap: typing.Optional[jsii.Number] = None,
        mounts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerMounts", typing.Dict[str, typing.Any]]]]] = None,
        must_run: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_alias: typing.Optional[typing.Sequence[builtins.str]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        networks_advanced: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerNetworksAdvanced", typing.Dict[str, typing.Any]]]]] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerPorts", typing.Dict[str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        publish_all_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remove_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restart: typing.Optional[builtins.str] = None,
        rm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        runtime: typing.Optional[builtins.str] = None,
        security_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        shm_size: typing.Optional[jsii.Number] = None,
        start: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        stdin_open: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        stop_signal: typing.Optional[builtins.str] = None,
        stop_timeout: typing.Optional[jsii.Number] = None,
        storage_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sysctls: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tmpfs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tty: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ulimit: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerUlimit", typing.Dict[str, typing.Any]]]]] = None,
        upload: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerUpload", typing.Dict[str, typing.Any]]]]] = None,
        user: typing.Optional[builtins.str] = None,
        userns_mode: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerVolumes", typing.Dict[str, typing.Any]]]]] = None,
        working_dir: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/docker/r/container docker_container} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param image: The ID of the image to back this container. The easiest way to get this value is to use the ``docker_image`` resource as is shown in the example. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#image Container#image}
        :param name: The name of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        :param attach: If ``true`` attach to the container after its creation and waits the end of its execution. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#attach Container#attach}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#capabilities Container#capabilities}
        :param command: The command to use to start the container. For example, to run ``/usr/bin/myprogram -f baz.conf`` set the command to be ``["/usr/bin/myprogram","-","baz.con"]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#command Container#command}
        :param container_read_refresh_timeout_milliseconds: The total number of milliseconds to wait for the container to reach status 'running'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_read_refresh_timeout_milliseconds Container#container_read_refresh_timeout_milliseconds}
        :param cpu_set: A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. ``0-1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#cpu_set Container#cpu_set}
        :param cpu_shares: CPU shares (relative weight) for the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#cpu_shares Container#cpu_shares}
        :param destroy_grace_seconds: If defined will attempt to stop the container before destroying. Container will be destroyed after ``n`` seconds or on successful stop. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#destroy_grace_seconds Container#destroy_grace_seconds}
        :param devices: devices block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#devices Container#devices}
        :param dns: DNS servers to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns Container#dns}
        :param dns_opts: DNS options used by the DNS provider(s), see ``resolv.conf`` documentation for valid list of options. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns_opts Container#dns_opts}
        :param dns_search: DNS search domains that are used when bare unqualified hostnames are used inside of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns_search Container#dns_search}
        :param domainname: Domain name of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#domainname Container#domainname}
        :param entrypoint: The command to use as the Entrypoint for the container. The Entrypoint allows you to configure a container to run as an executable. For example, to run ``/usr/bin/myprogram`` when starting a container, set the entrypoint to be ``"/usr/bin/myprogra"]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#entrypoint Container#entrypoint}
        :param env: Environment variables to set in the form of ``KEY=VALUE``, e.g. ``DEBUG=0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#env Container#env}
        :param gpus: GPU devices to add to the container. Currently, only the value ``all`` is supported. Passing any other value will result in unexpected behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#gpus Container#gpus}
        :param group_add: Additional groups for the container user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#group_add Container#group_add}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#healthcheck Container#healthcheck}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host Container#host}
        :param hostname: Hostname of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#hostname Container#hostname}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#id Container#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param init: Configured whether an init process should be injected for this container. If unset this will default to the ``dockerd`` defaults. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#init Container#init}
        :param ipc_mode: IPC sharing mode for the container. Possible values are: ``none``, ``private``, ``shareable``, ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipc_mode Container#ipc_mode}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#labels Container#labels}
        :param links: Set of links for link based connectivity between containers that are running on the same host. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#links Container#links}
        :param log_driver: The logging driver to use for the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#log_driver Container#log_driver}
        :param log_opts: Key/value pairs to use as options for the logging driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#log_opts Container#log_opts}
        :param logs: Save the container logs (``attach`` must be enabled). Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#logs Container#logs}
        :param max_retry_count: The maximum amount of times to an attempt a restart when ``restart`` is set to 'on-failure'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#max_retry_count Container#max_retry_count}
        :param memory: The memory limit for the container in MBs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#memory Container#memory}
        :param memory_swap: The total memory limit (memory + swap) for the container in MBs. This setting may compute to ``-1`` after ``terraform apply`` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#memory_swap Container#memory_swap}
        :param mounts: mounts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#mounts Container#mounts}
        :param must_run: If ``true``, then the Docker container will be kept running. If ``false``, then as long as the container exists, Terraform assumes it is successful. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#must_run Container#must_run}
        :param network_alias: Set an alias for the container in all specified networks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#network_alias Container#network_alias}
        :param network_mode: Network mode of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#network_mode Container#network_mode}
        :param networks: ID of the networks in which the container is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#networks Container#networks}
        :param networks_advanced: networks_advanced block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#networks_advanced Container#networks_advanced}
        :param pid_mode: he PID (Process) Namespace mode for the container. Either ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#pid_mode Container#pid_mode}
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ports Container#ports}
        :param privileged: If ``true``, the container runs in privileged mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#privileged Container#privileged}
        :param publish_all_ports: Publish all ports of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#publish_all_ports Container#publish_all_ports}
        :param read_only: If ``true``, the container will be started as readonly. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        :param remove_volumes: If ``true``, it will remove anonymous volumes associated with the container. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#remove_volumes Container#remove_volumes}
        :param restart: The restart policy for the container. Must be one of 'no', 'on-failure', 'always', 'unless-stopped'. Defaults to ``no``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#restart Container#restart}
        :param rm: If ``true``, then the container will be automatically removed when it exits. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#rm Container#rm}
        :param runtime: Runtime to use for the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#runtime Container#runtime}
        :param security_opts: List of string values to customize labels for MLS systems, such as SELinux. See https://docs.docker.com/engine/reference/run/#security-configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#security_opts Container#security_opts}
        :param shm_size: Size of ``/dev/shm`` in MBs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#shm_size Container#shm_size}
        :param start: If ``true``, then the Docker container will be started after creation. If ``false``, then the container is only created. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#start Container#start}
        :param stdin_open: If ``true``, keep STDIN open even if not attached (``docker run -i``). Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stdin_open Container#stdin_open}
        :param stop_signal: Signal to stop a container (default ``SIGTERM``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stop_signal Container#stop_signal}
        :param stop_timeout: Timeout (in seconds) to stop a container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stop_timeout Container#stop_timeout}
        :param storage_opts: Key/value pairs for the storage driver options, e.g. ``size``: ``120G``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#storage_opts Container#storage_opts}
        :param sysctls: A map of kernel parameters (sysctls) to set in the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#sysctls Container#sysctls}
        :param tmpfs: A map of container directories which should be replaced by ``tmpfs mounts``, and their corresponding mount options. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tmpfs Container#tmpfs}
        :param tty: If ``true``, allocate a pseudo-tty (``docker run -t``). Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tty Container#tty}
        :param ulimit: ulimit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ulimit Container#ulimit}
        :param upload: upload block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#upload Container#upload}
        :param user: User used for run the first process. Format is ``user`` or ``user:group`` which user and group can be passed literraly or by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#user Container#user}
        :param userns_mode: Sets the usernamespace mode for the container when usernamespace remapping option is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#userns_mode Container#userns_mode}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volumes Container#volumes}
        :param working_dir: The working directory for commands to run in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#working_dir Container#working_dir}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerConfig(
            image=image,
            name=name,
            attach=attach,
            capabilities=capabilities,
            command=command,
            container_read_refresh_timeout_milliseconds=container_read_refresh_timeout_milliseconds,
            cpu_set=cpu_set,
            cpu_shares=cpu_shares,
            destroy_grace_seconds=destroy_grace_seconds,
            devices=devices,
            dns=dns,
            dns_opts=dns_opts,
            dns_search=dns_search,
            domainname=domainname,
            entrypoint=entrypoint,
            env=env,
            gpus=gpus,
            group_add=group_add,
            healthcheck=healthcheck,
            host=host,
            hostname=hostname,
            id=id,
            init=init,
            ipc_mode=ipc_mode,
            labels=labels,
            links=links,
            log_driver=log_driver,
            log_opts=log_opts,
            logs=logs,
            max_retry_count=max_retry_count,
            memory=memory,
            memory_swap=memory_swap,
            mounts=mounts,
            must_run=must_run,
            network_alias=network_alias,
            network_mode=network_mode,
            networks=networks,
            networks_advanced=networks_advanced,
            pid_mode=pid_mode,
            ports=ports,
            privileged=privileged,
            publish_all_ports=publish_all_ports,
            read_only=read_only,
            remove_volumes=remove_volumes,
            restart=restart,
            rm=rm,
            runtime=runtime,
            security_opts=security_opts,
            shm_size=shm_size,
            start=start,
            stdin_open=stdin_open,
            stop_signal=stop_signal,
            stop_timeout=stop_timeout,
            storage_opts=storage_opts,
            sysctls=sysctls,
            tmpfs=tmpfs,
            tty=tty,
            ulimit=ulimit,
            upload=upload,
            user=user,
            userns_mode=userns_mode,
            volumes=volumes,
            working_dir=working_dir,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCapabilities")
    def put_capabilities(
        self,
        *,
        add: typing.Optional[typing.Sequence[builtins.str]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param add: List of linux capabilities to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#add Container#add}
        :param drop: List of linux capabilities to drop. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#drop Container#drop}
        '''
        value = ContainerCapabilities(add=add, drop=drop)

        return typing.cast(None, jsii.invoke(self, "putCapabilities", [value]))

    @jsii.member(jsii_name="putDevices")
    def put_devices(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerDevices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_devices)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDevices", [value]))

    @jsii.member(jsii_name="putHealthcheck")
    def put_healthcheck(
        self,
        *,
        test: typing.Sequence[builtins.str],
        interval: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        start_period: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param test: Command to run to check health. For example, to run ``curl -f localhost/health`` set the command to be ``["CMD", "curl", "-f", "localhost/health"]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#test Container#test}
        :param interval: Time between running the check (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#interval Container#interval}
        :param retries: Consecutive failures needed to report unhealthy. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#retries Container#retries}
        :param start_period: Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#start_period Container#start_period}
        :param timeout: Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#timeout Container#timeout}
        '''
        value = ContainerHealthcheck(
            test=test,
            interval=interval,
            retries=retries,
            start_period=start_period,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthcheck", [value]))

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerHost", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_host)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerLabels", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="putMounts")
    def put_mounts(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerMounts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_mounts)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMounts", [value]))

    @jsii.member(jsii_name="putNetworksAdvanced")
    def put_networks_advanced(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerNetworksAdvanced", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_networks_advanced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworksAdvanced", [value]))

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerPorts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_ports)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="putUlimit")
    def put_ulimit(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerUlimit", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_ulimit)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUlimit", [value]))

    @jsii.member(jsii_name="putUpload")
    def put_upload(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerUpload", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_upload)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUpload", [value]))

    @jsii.member(jsii_name="putVolumes")
    def put_volumes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerVolumes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Container.put_volumes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolumes", [value]))

    @jsii.member(jsii_name="resetAttach")
    def reset_attach(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttach", []))

    @jsii.member(jsii_name="resetCapabilities")
    def reset_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapabilities", []))

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetContainerReadRefreshTimeoutMilliseconds")
    def reset_container_read_refresh_timeout_milliseconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerReadRefreshTimeoutMilliseconds", []))

    @jsii.member(jsii_name="resetCpuSet")
    def reset_cpu_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuSet", []))

    @jsii.member(jsii_name="resetCpuShares")
    def reset_cpu_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuShares", []))

    @jsii.member(jsii_name="resetDestroyGraceSeconds")
    def reset_destroy_grace_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestroyGraceSeconds", []))

    @jsii.member(jsii_name="resetDevices")
    def reset_devices(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevices", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetDnsOpts")
    def reset_dns_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsOpts", []))

    @jsii.member(jsii_name="resetDnsSearch")
    def reset_dns_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsSearch", []))

    @jsii.member(jsii_name="resetDomainname")
    def reset_domainname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainname", []))

    @jsii.member(jsii_name="resetEntrypoint")
    def reset_entrypoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntrypoint", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetGpus")
    def reset_gpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpus", []))

    @jsii.member(jsii_name="resetGroupAdd")
    def reset_group_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupAdd", []))

    @jsii.member(jsii_name="resetHealthcheck")
    def reset_healthcheck(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthcheck", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInit")
    def reset_init(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInit", []))

    @jsii.member(jsii_name="resetIpcMode")
    def reset_ipc_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpcMode", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @jsii.member(jsii_name="resetLogDriver")
    def reset_log_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDriver", []))

    @jsii.member(jsii_name="resetLogOpts")
    def reset_log_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogOpts", []))

    @jsii.member(jsii_name="resetLogs")
    def reset_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogs", []))

    @jsii.member(jsii_name="resetMaxRetryCount")
    def reset_max_retry_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetryCount", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetMemorySwap")
    def reset_memory_swap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemorySwap", []))

    @jsii.member(jsii_name="resetMounts")
    def reset_mounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMounts", []))

    @jsii.member(jsii_name="resetMustRun")
    def reset_must_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMustRun", []))

    @jsii.member(jsii_name="resetNetworkAlias")
    def reset_network_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAlias", []))

    @jsii.member(jsii_name="resetNetworkMode")
    def reset_network_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkMode", []))

    @jsii.member(jsii_name="resetNetworks")
    def reset_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworks", []))

    @jsii.member(jsii_name="resetNetworksAdvanced")
    def reset_networks_advanced(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworksAdvanced", []))

    @jsii.member(jsii_name="resetPidMode")
    def reset_pid_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPidMode", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @jsii.member(jsii_name="resetPrivileged")
    def reset_privileged(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileged", []))

    @jsii.member(jsii_name="resetPublishAllPorts")
    def reset_publish_all_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishAllPorts", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetRemoveVolumes")
    def reset_remove_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveVolumes", []))

    @jsii.member(jsii_name="resetRestart")
    def reset_restart(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestart", []))

    @jsii.member(jsii_name="resetRm")
    def reset_rm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRm", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @jsii.member(jsii_name="resetSecurityOpts")
    def reset_security_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityOpts", []))

    @jsii.member(jsii_name="resetShmSize")
    def reset_shm_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShmSize", []))

    @jsii.member(jsii_name="resetStart")
    def reset_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStart", []))

    @jsii.member(jsii_name="resetStdinOpen")
    def reset_stdin_open(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStdinOpen", []))

    @jsii.member(jsii_name="resetStopSignal")
    def reset_stop_signal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopSignal", []))

    @jsii.member(jsii_name="resetStopTimeout")
    def reset_stop_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopTimeout", []))

    @jsii.member(jsii_name="resetStorageOpts")
    def reset_storage_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageOpts", []))

    @jsii.member(jsii_name="resetSysctls")
    def reset_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSysctls", []))

    @jsii.member(jsii_name="resetTmpfs")
    def reset_tmpfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTmpfs", []))

    @jsii.member(jsii_name="resetTty")
    def reset_tty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTty", []))

    @jsii.member(jsii_name="resetUlimit")
    def reset_ulimit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUlimit", []))

    @jsii.member(jsii_name="resetUpload")
    def reset_upload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpload", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="resetUsernsMode")
    def reset_userns_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernsMode", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @jsii.member(jsii_name="resetWorkingDir")
    def reset_working_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkingDir", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bridge")
    def bridge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bridge"))

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> "ContainerCapabilitiesOutputReference":
        return typing.cast("ContainerCapabilitiesOutputReference", jsii.get(self, "capabilities"))

    @builtins.property
    @jsii.member(jsii_name="containerLogs")
    def container_logs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerLogs"))

    @builtins.property
    @jsii.member(jsii_name="devices")
    def devices(self) -> "ContainerDevicesList":
        return typing.cast("ContainerDevicesList", jsii.get(self, "devices"))

    @builtins.property
    @jsii.member(jsii_name="exitCode")
    def exit_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "exitCode"))

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @builtins.property
    @jsii.member(jsii_name="healthcheck")
    def healthcheck(self) -> "ContainerHealthcheckOutputReference":
        return typing.cast("ContainerHealthcheckOutputReference", jsii.get(self, "healthcheck"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> "ContainerHostList":
        return typing.cast("ContainerHostList", jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipPrefixLength")
    def ip_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipPrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> "ContainerLabelsList":
        return typing.cast("ContainerLabelsList", jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="mounts")
    def mounts(self) -> "ContainerMountsList":
        return typing.cast("ContainerMountsList", jsii.get(self, "mounts"))

    @builtins.property
    @jsii.member(jsii_name="networkData")
    def network_data(self) -> "ContainerNetworkDataList":
        return typing.cast("ContainerNetworkDataList", jsii.get(self, "networkData"))

    @builtins.property
    @jsii.member(jsii_name="networksAdvanced")
    def networks_advanced(self) -> "ContainerNetworksAdvancedList":
        return typing.cast("ContainerNetworksAdvancedList", jsii.get(self, "networksAdvanced"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "ContainerPortsList":
        return typing.cast("ContainerPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="ulimit")
    def ulimit(self) -> "ContainerUlimitList":
        return typing.cast("ContainerUlimitList", jsii.get(self, "ulimit"))

    @builtins.property
    @jsii.member(jsii_name="upload")
    def upload(self) -> "ContainerUploadList":
        return typing.cast("ContainerUploadList", jsii.get(self, "upload"))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "ContainerVolumesList":
        return typing.cast("ContainerVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="attachInput")
    def attach_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "attachInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilitiesInput")
    def capabilities_input(self) -> typing.Optional["ContainerCapabilities"]:
        return typing.cast(typing.Optional["ContainerCapabilities"], jsii.get(self, "capabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="containerReadRefreshTimeoutMillisecondsInput")
    def container_read_refresh_timeout_milliseconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerReadRefreshTimeoutMillisecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSetInput")
    def cpu_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuSetInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSharesInput")
    def cpu_shares_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuSharesInput"))

    @builtins.property
    @jsii.member(jsii_name="destroyGraceSecondsInput")
    def destroy_grace_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "destroyGraceSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="devicesInput")
    def devices_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerDevices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerDevices"]]], jsii.get(self, "devicesInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsOptsInput")
    def dns_opts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsSearchInput")
    def dns_search_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsSearchInput"))

    @builtins.property
    @jsii.member(jsii_name="domainnameInput")
    def domainname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainnameInput"))

    @builtins.property
    @jsii.member(jsii_name="entrypointInput")
    def entrypoint_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entrypointInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="gpusInput")
    def gpus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpusInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAddInput")
    def group_add_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupAddInput"))

    @builtins.property
    @jsii.member(jsii_name="healthcheckInput")
    def healthcheck_input(self) -> typing.Optional["ContainerHealthcheck"]:
        return typing.cast(typing.Optional["ContainerHealthcheck"], jsii.get(self, "healthcheckInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerHost"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerHost"]]], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="initInput")
    def init_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "initInput"))

    @builtins.property
    @jsii.member(jsii_name="ipcModeInput")
    def ipc_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipcModeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerLabels"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerLabels"]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="logDriverInput")
    def log_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="logOptsInput")
    def log_opts_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "logOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="logsInput")
    def logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetryCountInput")
    def max_retry_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetryCountInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySwapInput")
    def memory_swap_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySwapInput"))

    @builtins.property
    @jsii.member(jsii_name="mountsInput")
    def mounts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerMounts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerMounts"]]], jsii.get(self, "mountsInput"))

    @builtins.property
    @jsii.member(jsii_name="mustRunInput")
    def must_run_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mustRunInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkAliasInput")
    def network_alias_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networkAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="networkModeInput")
    def network_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkModeInput"))

    @builtins.property
    @jsii.member(jsii_name="networksAdvancedInput")
    def networks_advanced_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerNetworksAdvanced"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerNetworksAdvanced"]]], jsii.get(self, "networksAdvancedInput"))

    @builtins.property
    @jsii.member(jsii_name="networksInput")
    def networks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networksInput"))

    @builtins.property
    @jsii.member(jsii_name="pidModeInput")
    def pid_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pidModeInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerPorts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerPorts"]]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedInput")
    def privileged_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privilegedInput"))

    @builtins.property
    @jsii.member(jsii_name="publishAllPortsInput")
    def publish_all_ports_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishAllPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="removeVolumesInput")
    def remove_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "removeVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="restartInput")
    def restart_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restartInput"))

    @builtins.property
    @jsii.member(jsii_name="rmInput")
    def rm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rmInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="securityOptsInput")
    def security_opts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="shmSizeInput")
    def shm_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="stdinOpenInput")
    def stdin_open_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stdinOpenInput"))

    @builtins.property
    @jsii.member(jsii_name="stopSignalInput")
    def stop_signal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stopSignalInput"))

    @builtins.property
    @jsii.member(jsii_name="stopTimeoutInput")
    def stop_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stopTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="storageOptsInput")
    def storage_opts_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "storageOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="sysctlsInput")
    def sysctls_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsInput")
    def tmpfs_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tmpfsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttyInput")
    def tty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ttyInput"))

    @builtins.property
    @jsii.member(jsii_name="ulimitInput")
    def ulimit_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUlimit"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUlimit"]]], jsii.get(self, "ulimitInput"))

    @builtins.property
    @jsii.member(jsii_name="uploadInput")
    def upload_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUpload"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUpload"]]], jsii.get(self, "uploadInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="usernsModeInput")
    def userns_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernsModeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerVolumes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerVolumes"]]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="workingDirInput")
    def working_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirInput"))

    @builtins.property
    @jsii.member(jsii_name="attach")
    def attach(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "attach"))

    @attach.setter
    def attach(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "attach").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attach", value)

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "command"))

    @command.setter
    def command(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value)

    @builtins.property
    @jsii.member(jsii_name="containerReadRefreshTimeoutMilliseconds")
    def container_read_refresh_timeout_milliseconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerReadRefreshTimeoutMilliseconds"))

    @container_read_refresh_timeout_milliseconds.setter
    def container_read_refresh_timeout_milliseconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "container_read_refresh_timeout_milliseconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerReadRefreshTimeoutMilliseconds", value)

    @builtins.property
    @jsii.member(jsii_name="cpuSet")
    def cpu_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuSet"))

    @cpu_set.setter
    def cpu_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "cpu_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuSet", value)

    @builtins.property
    @jsii.member(jsii_name="cpuShares")
    def cpu_shares(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuShares"))

    @cpu_shares.setter
    def cpu_shares(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "cpu_shares").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuShares", value)

    @builtins.property
    @jsii.member(jsii_name="destroyGraceSeconds")
    def destroy_grace_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "destroyGraceSeconds"))

    @destroy_grace_seconds.setter
    def destroy_grace_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "destroy_grace_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destroyGraceSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dns"))

    @dns.setter
    def dns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dns", value)

    @builtins.property
    @jsii.member(jsii_name="dnsOpts")
    def dns_opts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsOpts"))

    @dns_opts.setter
    def dns_opts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "dns_opts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsOpts", value)

    @builtins.property
    @jsii.member(jsii_name="dnsSearch")
    def dns_search(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsSearch"))

    @dns_search.setter
    def dns_search(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "dns_search").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsSearch", value)

    @builtins.property
    @jsii.member(jsii_name="domainname")
    def domainname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainname"))

    @domainname.setter
    def domainname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "domainname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainname", value)

    @builtins.property
    @jsii.member(jsii_name="entrypoint")
    def entrypoint(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entrypoint"))

    @entrypoint.setter
    def entrypoint(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "entrypoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entrypoint", value)

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "env"))

    @env.setter
    def env(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value)

    @builtins.property
    @jsii.member(jsii_name="gpus")
    def gpus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpus"))

    @gpus.setter
    def gpus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "gpus").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpus", value)

    @builtins.property
    @jsii.member(jsii_name="groupAdd")
    def group_add(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupAdd"))

    @group_add.setter
    def group_add(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "group_add").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAdd", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="init")
    def init(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "init"))

    @init.setter
    def init(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "init").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "init", value)

    @builtins.property
    @jsii.member(jsii_name="ipcMode")
    def ipc_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipcMode"))

    @ipc_mode.setter
    def ipc_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "ipc_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipcMode", value)

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "links"))

    @links.setter
    def links(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "links").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "links", value)

    @builtins.property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDriver"))

    @log_driver.setter
    def log_driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "log_driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDriver", value)

    @builtins.property
    @jsii.member(jsii_name="logOpts")
    def log_opts(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "logOpts"))

    @log_opts.setter
    def log_opts(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "log_opts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logOpts", value)

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logs"))

    @logs.setter
    def logs(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "logs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logs", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetryCount")
    def max_retry_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetryCount"))

    @max_retry_count.setter
    def max_retry_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "max_retry_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetryCount", value)

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "memory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)

    @builtins.property
    @jsii.member(jsii_name="memorySwap")
    def memory_swap(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySwap"))

    @memory_swap.setter
    def memory_swap(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "memory_swap").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySwap", value)

    @builtins.property
    @jsii.member(jsii_name="mustRun")
    def must_run(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mustRun"))

    @must_run.setter
    def must_run(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "must_run").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mustRun", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkAlias")
    def network_alias(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkAlias"))

    @network_alias.setter
    def network_alias(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "network_alias").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkAlias", value)

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @network_mode.setter
    def network_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "network_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkMode", value)

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networks"))

    @networks.setter
    def networks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "networks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networks", value)

    @builtins.property
    @jsii.member(jsii_name="pidMode")
    def pid_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pidMode"))

    @pid_mode.setter
    def pid_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "pid_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pidMode", value)

    @builtins.property
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privileged"))

    @privileged.setter
    def privileged(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "privileged").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileged", value)

    @builtins.property
    @jsii.member(jsii_name="publishAllPorts")
    def publish_all_ports(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publishAllPorts"))

    @publish_all_ports.setter
    def publish_all_ports(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "publish_all_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishAllPorts", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="removeVolumes")
    def remove_volumes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "removeVolumes"))

    @remove_volumes.setter
    def remove_volumes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "remove_volumes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeVolumes", value)

    @builtins.property
    @jsii.member(jsii_name="restart")
    def restart(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restart"))

    @restart.setter
    def restart(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "restart").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restart", value)

    @builtins.property
    @jsii.member(jsii_name="rm")
    def rm(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rm"))

    @rm.setter
    def rm(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "rm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rm", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "runtime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="securityOpts")
    def security_opts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityOpts"))

    @security_opts.setter
    def security_opts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "security_opts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityOpts", value)

    @builtins.property
    @jsii.member(jsii_name="shmSize")
    def shm_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shmSize"))

    @shm_size.setter
    def shm_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "shm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shmSize", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "start"))

    @start.setter
    def start(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="stdinOpen")
    def stdin_open(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stdinOpen"))

    @stdin_open.setter
    def stdin_open(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "stdin_open").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stdinOpen", value)

    @builtins.property
    @jsii.member(jsii_name="stopSignal")
    def stop_signal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stopSignal"))

    @stop_signal.setter
    def stop_signal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "stop_signal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopSignal", value)

    @builtins.property
    @jsii.member(jsii_name="stopTimeout")
    def stop_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stopTimeout"))

    @stop_timeout.setter
    def stop_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "stop_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="storageOpts")
    def storage_opts(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "storageOpts"))

    @storage_opts.setter
    def storage_opts(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "storage_opts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageOpts", value)

    @builtins.property
    @jsii.member(jsii_name="sysctls")
    def sysctls(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sysctls"))

    @sysctls.setter
    def sysctls(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "sysctls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sysctls", value)

    @builtins.property
    @jsii.member(jsii_name="tmpfs")
    def tmpfs(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tmpfs"))

    @tmpfs.setter
    def tmpfs(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "tmpfs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tmpfs", value)

    @builtins.property
    @jsii.member(jsii_name="tty")
    def tty(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tty"))

    @tty.setter
    def tty(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "tty").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tty", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="usernsMode")
    def userns_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernsMode"))

    @userns_mode.setter
    def userns_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "userns_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernsMode", value)

    @builtins.property
    @jsii.member(jsii_name="workingDir")
    def working_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workingDir"))

    @working_dir.setter
    def working_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Container, "working_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDir", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerCapabilities",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "drop": "drop"},
)
class ContainerCapabilities:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Sequence[builtins.str]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param add: List of linux capabilities to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#add Container#add}
        :param drop: List of linux capabilities to drop. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#drop Container#drop}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerCapabilities.__init__)
            check_type(argname="argument add", value=add, expected_type=type_hints["add"])
            check_type(argname="argument drop", value=drop, expected_type=type_hints["drop"])
        self._values: typing.Dict[str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if drop is not None:
            self._values["drop"] = drop

    @builtins.property
    def add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of linux capabilities to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#add Container#add}
        '''
        result = self._values.get("add")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def drop(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of linux capabilities to drop.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#drop Container#drop}
        '''
        result = self._values.get("drop")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerCapabilitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(ContainerCapabilitiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdd")
    def reset_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdd", []))

    @jsii.member(jsii_name="resetDrop")
    def reset_drop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrop", []))

    @builtins.property
    @jsii.member(jsii_name="addInput")
    def add_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addInput"))

    @builtins.property
    @jsii.member(jsii_name="dropInput")
    def drop_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dropInput"))

    @builtins.property
    @jsii.member(jsii_name="add")
    def add(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "add"))

    @add.setter
    def add(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCapabilitiesOutputReference, "add").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "add", value)

    @builtins.property
    @jsii.member(jsii_name="drop")
    def drop(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "drop"))

    @drop.setter
    def drop(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCapabilitiesOutputReference, "drop").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drop", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerCapabilities]:
        return typing.cast(typing.Optional[ContainerCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerCapabilities]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerCapabilitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "image": "image",
        "name": "name",
        "attach": "attach",
        "capabilities": "capabilities",
        "command": "command",
        "container_read_refresh_timeout_milliseconds": "containerReadRefreshTimeoutMilliseconds",
        "cpu_set": "cpuSet",
        "cpu_shares": "cpuShares",
        "destroy_grace_seconds": "destroyGraceSeconds",
        "devices": "devices",
        "dns": "dns",
        "dns_opts": "dnsOpts",
        "dns_search": "dnsSearch",
        "domainname": "domainname",
        "entrypoint": "entrypoint",
        "env": "env",
        "gpus": "gpus",
        "group_add": "groupAdd",
        "healthcheck": "healthcheck",
        "host": "host",
        "hostname": "hostname",
        "id": "id",
        "init": "init",
        "ipc_mode": "ipcMode",
        "labels": "labels",
        "links": "links",
        "log_driver": "logDriver",
        "log_opts": "logOpts",
        "logs": "logs",
        "max_retry_count": "maxRetryCount",
        "memory": "memory",
        "memory_swap": "memorySwap",
        "mounts": "mounts",
        "must_run": "mustRun",
        "network_alias": "networkAlias",
        "network_mode": "networkMode",
        "networks": "networks",
        "networks_advanced": "networksAdvanced",
        "pid_mode": "pidMode",
        "ports": "ports",
        "privileged": "privileged",
        "publish_all_ports": "publishAllPorts",
        "read_only": "readOnly",
        "remove_volumes": "removeVolumes",
        "restart": "restart",
        "rm": "rm",
        "runtime": "runtime",
        "security_opts": "securityOpts",
        "shm_size": "shmSize",
        "start": "start",
        "stdin_open": "stdinOpen",
        "stop_signal": "stopSignal",
        "stop_timeout": "stopTimeout",
        "storage_opts": "storageOpts",
        "sysctls": "sysctls",
        "tmpfs": "tmpfs",
        "tty": "tty",
        "ulimit": "ulimit",
        "upload": "upload",
        "user": "user",
        "userns_mode": "usernsMode",
        "volumes": "volumes",
        "working_dir": "workingDir",
    },
)
class ContainerConfig(cdktf.TerraformMetaArguments):
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
        image: builtins.str,
        name: builtins.str,
        attach: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        capabilities: typing.Optional[typing.Union[ContainerCapabilities, typing.Dict[str, typing.Any]]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_read_refresh_timeout_milliseconds: typing.Optional[jsii.Number] = None,
        cpu_set: typing.Optional[builtins.str] = None,
        cpu_shares: typing.Optional[jsii.Number] = None,
        destroy_grace_seconds: typing.Optional[jsii.Number] = None,
        devices: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerDevices", typing.Dict[str, typing.Any]]]]] = None,
        dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_search: typing.Optional[typing.Sequence[builtins.str]] = None,
        domainname: typing.Optional[builtins.str] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        gpus: typing.Optional[builtins.str] = None,
        group_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        healthcheck: typing.Optional[typing.Union["ContainerHealthcheck", typing.Dict[str, typing.Any]]] = None,
        host: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerHost", typing.Dict[str, typing.Any]]]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        init: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerLabels", typing.Dict[str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_driver: typing.Optional[builtins.str] = None,
        log_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logs: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_retry_count: typing.Optional[jsii.Number] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_swap: typing.Optional[jsii.Number] = None,
        mounts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerMounts", typing.Dict[str, typing.Any]]]]] = None,
        must_run: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_alias: typing.Optional[typing.Sequence[builtins.str]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        networks_advanced: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerNetworksAdvanced", typing.Dict[str, typing.Any]]]]] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerPorts", typing.Dict[str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        publish_all_ports: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        remove_volumes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        restart: typing.Optional[builtins.str] = None,
        rm: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        runtime: typing.Optional[builtins.str] = None,
        security_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        shm_size: typing.Optional[jsii.Number] = None,
        start: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        stdin_open: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        stop_signal: typing.Optional[builtins.str] = None,
        stop_timeout: typing.Optional[jsii.Number] = None,
        storage_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sysctls: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tmpfs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tty: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ulimit: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerUlimit", typing.Dict[str, typing.Any]]]]] = None,
        upload: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerUpload", typing.Dict[str, typing.Any]]]]] = None,
        user: typing.Optional[builtins.str] = None,
        userns_mode: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerVolumes", typing.Dict[str, typing.Any]]]]] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param image: The ID of the image to back this container. The easiest way to get this value is to use the ``docker_image`` resource as is shown in the example. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#image Container#image}
        :param name: The name of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        :param attach: If ``true`` attach to the container after its creation and waits the end of its execution. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#attach Container#attach}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#capabilities Container#capabilities}
        :param command: The command to use to start the container. For example, to run ``/usr/bin/myprogram -f baz.conf`` set the command to be ``["/usr/bin/myprogram","-","baz.con"]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#command Container#command}
        :param container_read_refresh_timeout_milliseconds: The total number of milliseconds to wait for the container to reach status 'running'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_read_refresh_timeout_milliseconds Container#container_read_refresh_timeout_milliseconds}
        :param cpu_set: A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. ``0-1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#cpu_set Container#cpu_set}
        :param cpu_shares: CPU shares (relative weight) for the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#cpu_shares Container#cpu_shares}
        :param destroy_grace_seconds: If defined will attempt to stop the container before destroying. Container will be destroyed after ``n`` seconds or on successful stop. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#destroy_grace_seconds Container#destroy_grace_seconds}
        :param devices: devices block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#devices Container#devices}
        :param dns: DNS servers to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns Container#dns}
        :param dns_opts: DNS options used by the DNS provider(s), see ``resolv.conf`` documentation for valid list of options. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns_opts Container#dns_opts}
        :param dns_search: DNS search domains that are used when bare unqualified hostnames are used inside of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns_search Container#dns_search}
        :param domainname: Domain name of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#domainname Container#domainname}
        :param entrypoint: The command to use as the Entrypoint for the container. The Entrypoint allows you to configure a container to run as an executable. For example, to run ``/usr/bin/myprogram`` when starting a container, set the entrypoint to be ``"/usr/bin/myprogra"]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#entrypoint Container#entrypoint}
        :param env: Environment variables to set in the form of ``KEY=VALUE``, e.g. ``DEBUG=0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#env Container#env}
        :param gpus: GPU devices to add to the container. Currently, only the value ``all`` is supported. Passing any other value will result in unexpected behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#gpus Container#gpus}
        :param group_add: Additional groups for the container user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#group_add Container#group_add}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#healthcheck Container#healthcheck}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host Container#host}
        :param hostname: Hostname of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#hostname Container#hostname}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#id Container#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param init: Configured whether an init process should be injected for this container. If unset this will default to the ``dockerd`` defaults. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#init Container#init}
        :param ipc_mode: IPC sharing mode for the container. Possible values are: ``none``, ``private``, ``shareable``, ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipc_mode Container#ipc_mode}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#labels Container#labels}
        :param links: Set of links for link based connectivity between containers that are running on the same host. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#links Container#links}
        :param log_driver: The logging driver to use for the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#log_driver Container#log_driver}
        :param log_opts: Key/value pairs to use as options for the logging driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#log_opts Container#log_opts}
        :param logs: Save the container logs (``attach`` must be enabled). Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#logs Container#logs}
        :param max_retry_count: The maximum amount of times to an attempt a restart when ``restart`` is set to 'on-failure'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#max_retry_count Container#max_retry_count}
        :param memory: The memory limit for the container in MBs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#memory Container#memory}
        :param memory_swap: The total memory limit (memory + swap) for the container in MBs. This setting may compute to ``-1`` after ``terraform apply`` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#memory_swap Container#memory_swap}
        :param mounts: mounts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#mounts Container#mounts}
        :param must_run: If ``true``, then the Docker container will be kept running. If ``false``, then as long as the container exists, Terraform assumes it is successful. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#must_run Container#must_run}
        :param network_alias: Set an alias for the container in all specified networks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#network_alias Container#network_alias}
        :param network_mode: Network mode of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#network_mode Container#network_mode}
        :param networks: ID of the networks in which the container is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#networks Container#networks}
        :param networks_advanced: networks_advanced block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#networks_advanced Container#networks_advanced}
        :param pid_mode: he PID (Process) Namespace mode for the container. Either ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#pid_mode Container#pid_mode}
        :param ports: ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ports Container#ports}
        :param privileged: If ``true``, the container runs in privileged mode. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#privileged Container#privileged}
        :param publish_all_ports: Publish all ports of the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#publish_all_ports Container#publish_all_ports}
        :param read_only: If ``true``, the container will be started as readonly. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        :param remove_volumes: If ``true``, it will remove anonymous volumes associated with the container. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#remove_volumes Container#remove_volumes}
        :param restart: The restart policy for the container. Must be one of 'no', 'on-failure', 'always', 'unless-stopped'. Defaults to ``no``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#restart Container#restart}
        :param rm: If ``true``, then the container will be automatically removed when it exits. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#rm Container#rm}
        :param runtime: Runtime to use for the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#runtime Container#runtime}
        :param security_opts: List of string values to customize labels for MLS systems, such as SELinux. See https://docs.docker.com/engine/reference/run/#security-configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#security_opts Container#security_opts}
        :param shm_size: Size of ``/dev/shm`` in MBs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#shm_size Container#shm_size}
        :param start: If ``true``, then the Docker container will be started after creation. If ``false``, then the container is only created. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#start Container#start}
        :param stdin_open: If ``true``, keep STDIN open even if not attached (``docker run -i``). Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stdin_open Container#stdin_open}
        :param stop_signal: Signal to stop a container (default ``SIGTERM``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stop_signal Container#stop_signal}
        :param stop_timeout: Timeout (in seconds) to stop a container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stop_timeout Container#stop_timeout}
        :param storage_opts: Key/value pairs for the storage driver options, e.g. ``size``: ``120G``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#storage_opts Container#storage_opts}
        :param sysctls: A map of kernel parameters (sysctls) to set in the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#sysctls Container#sysctls}
        :param tmpfs: A map of container directories which should be replaced by ``tmpfs mounts``, and their corresponding mount options. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tmpfs Container#tmpfs}
        :param tty: If ``true``, allocate a pseudo-tty (``docker run -t``). Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tty Container#tty}
        :param ulimit: ulimit block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ulimit Container#ulimit}
        :param upload: upload block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#upload Container#upload}
        :param user: User used for run the first process. Format is ``user`` or ``user:group`` which user and group can be passed literraly or by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#user Container#user}
        :param userns_mode: Sets the usernamespace mode for the container when usernamespace remapping option is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#userns_mode Container#userns_mode}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volumes Container#volumes}
        :param working_dir: The working directory for commands to run in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#working_dir Container#working_dir}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capabilities, dict):
            capabilities = ContainerCapabilities(**capabilities)
        if isinstance(healthcheck, dict):
            healthcheck = ContainerHealthcheck(**healthcheck)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attach", value=attach, expected_type=type_hints["attach"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument container_read_refresh_timeout_milliseconds", value=container_read_refresh_timeout_milliseconds, expected_type=type_hints["container_read_refresh_timeout_milliseconds"])
            check_type(argname="argument cpu_set", value=cpu_set, expected_type=type_hints["cpu_set"])
            check_type(argname="argument cpu_shares", value=cpu_shares, expected_type=type_hints["cpu_shares"])
            check_type(argname="argument destroy_grace_seconds", value=destroy_grace_seconds, expected_type=type_hints["destroy_grace_seconds"])
            check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument dns_opts", value=dns_opts, expected_type=type_hints["dns_opts"])
            check_type(argname="argument dns_search", value=dns_search, expected_type=type_hints["dns_search"])
            check_type(argname="argument domainname", value=domainname, expected_type=type_hints["domainname"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument gpus", value=gpus, expected_type=type_hints["gpus"])
            check_type(argname="argument group_add", value=group_add, expected_type=type_hints["group_add"])
            check_type(argname="argument healthcheck", value=healthcheck, expected_type=type_hints["healthcheck"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument init", value=init, expected_type=type_hints["init"])
            check_type(argname="argument ipc_mode", value=ipc_mode, expected_type=type_hints["ipc_mode"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
            check_type(argname="argument log_opts", value=log_opts, expected_type=type_hints["log_opts"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument max_retry_count", value=max_retry_count, expected_type=type_hints["max_retry_count"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument memory_swap", value=memory_swap, expected_type=type_hints["memory_swap"])
            check_type(argname="argument mounts", value=mounts, expected_type=type_hints["mounts"])
            check_type(argname="argument must_run", value=must_run, expected_type=type_hints["must_run"])
            check_type(argname="argument network_alias", value=network_alias, expected_type=type_hints["network_alias"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
            check_type(argname="argument networks_advanced", value=networks_advanced, expected_type=type_hints["networks_advanced"])
            check_type(argname="argument pid_mode", value=pid_mode, expected_type=type_hints["pid_mode"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
            check_type(argname="argument publish_all_ports", value=publish_all_ports, expected_type=type_hints["publish_all_ports"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument remove_volumes", value=remove_volumes, expected_type=type_hints["remove_volumes"])
            check_type(argname="argument restart", value=restart, expected_type=type_hints["restart"])
            check_type(argname="argument rm", value=rm, expected_type=type_hints["rm"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument security_opts", value=security_opts, expected_type=type_hints["security_opts"])
            check_type(argname="argument shm_size", value=shm_size, expected_type=type_hints["shm_size"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument stdin_open", value=stdin_open, expected_type=type_hints["stdin_open"])
            check_type(argname="argument stop_signal", value=stop_signal, expected_type=type_hints["stop_signal"])
            check_type(argname="argument stop_timeout", value=stop_timeout, expected_type=type_hints["stop_timeout"])
            check_type(argname="argument storage_opts", value=storage_opts, expected_type=type_hints["storage_opts"])
            check_type(argname="argument sysctls", value=sysctls, expected_type=type_hints["sysctls"])
            check_type(argname="argument tmpfs", value=tmpfs, expected_type=type_hints["tmpfs"])
            check_type(argname="argument tty", value=tty, expected_type=type_hints["tty"])
            check_type(argname="argument ulimit", value=ulimit, expected_type=type_hints["ulimit"])
            check_type(argname="argument upload", value=upload, expected_type=type_hints["upload"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument userns_mode", value=userns_mode, expected_type=type_hints["userns_mode"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument working_dir", value=working_dir, expected_type=type_hints["working_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
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
        if attach is not None:
            self._values["attach"] = attach
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if command is not None:
            self._values["command"] = command
        if container_read_refresh_timeout_milliseconds is not None:
            self._values["container_read_refresh_timeout_milliseconds"] = container_read_refresh_timeout_milliseconds
        if cpu_set is not None:
            self._values["cpu_set"] = cpu_set
        if cpu_shares is not None:
            self._values["cpu_shares"] = cpu_shares
        if destroy_grace_seconds is not None:
            self._values["destroy_grace_seconds"] = destroy_grace_seconds
        if devices is not None:
            self._values["devices"] = devices
        if dns is not None:
            self._values["dns"] = dns
        if dns_opts is not None:
            self._values["dns_opts"] = dns_opts
        if dns_search is not None:
            self._values["dns_search"] = dns_search
        if domainname is not None:
            self._values["domainname"] = domainname
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if env is not None:
            self._values["env"] = env
        if gpus is not None:
            self._values["gpus"] = gpus
        if group_add is not None:
            self._values["group_add"] = group_add
        if healthcheck is not None:
            self._values["healthcheck"] = healthcheck
        if host is not None:
            self._values["host"] = host
        if hostname is not None:
            self._values["hostname"] = hostname
        if id is not None:
            self._values["id"] = id
        if init is not None:
            self._values["init"] = init
        if ipc_mode is not None:
            self._values["ipc_mode"] = ipc_mode
        if labels is not None:
            self._values["labels"] = labels
        if links is not None:
            self._values["links"] = links
        if log_driver is not None:
            self._values["log_driver"] = log_driver
        if log_opts is not None:
            self._values["log_opts"] = log_opts
        if logs is not None:
            self._values["logs"] = logs
        if max_retry_count is not None:
            self._values["max_retry_count"] = max_retry_count
        if memory is not None:
            self._values["memory"] = memory
        if memory_swap is not None:
            self._values["memory_swap"] = memory_swap
        if mounts is not None:
            self._values["mounts"] = mounts
        if must_run is not None:
            self._values["must_run"] = must_run
        if network_alias is not None:
            self._values["network_alias"] = network_alias
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if networks is not None:
            self._values["networks"] = networks
        if networks_advanced is not None:
            self._values["networks_advanced"] = networks_advanced
        if pid_mode is not None:
            self._values["pid_mode"] = pid_mode
        if ports is not None:
            self._values["ports"] = ports
        if privileged is not None:
            self._values["privileged"] = privileged
        if publish_all_ports is not None:
            self._values["publish_all_ports"] = publish_all_ports
        if read_only is not None:
            self._values["read_only"] = read_only
        if remove_volumes is not None:
            self._values["remove_volumes"] = remove_volumes
        if restart is not None:
            self._values["restart"] = restart
        if rm is not None:
            self._values["rm"] = rm
        if runtime is not None:
            self._values["runtime"] = runtime
        if security_opts is not None:
            self._values["security_opts"] = security_opts
        if shm_size is not None:
            self._values["shm_size"] = shm_size
        if start is not None:
            self._values["start"] = start
        if stdin_open is not None:
            self._values["stdin_open"] = stdin_open
        if stop_signal is not None:
            self._values["stop_signal"] = stop_signal
        if stop_timeout is not None:
            self._values["stop_timeout"] = stop_timeout
        if storage_opts is not None:
            self._values["storage_opts"] = storage_opts
        if sysctls is not None:
            self._values["sysctls"] = sysctls
        if tmpfs is not None:
            self._values["tmpfs"] = tmpfs
        if tty is not None:
            self._values["tty"] = tty
        if ulimit is not None:
            self._values["ulimit"] = ulimit
        if upload is not None:
            self._values["upload"] = upload
        if user is not None:
            self._values["user"] = user
        if userns_mode is not None:
            self._values["userns_mode"] = userns_mode
        if volumes is not None:
            self._values["volumes"] = volumes
        if working_dir is not None:
            self._values["working_dir"] = working_dir

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
    def image(self) -> builtins.str:
        '''The ID of the image to back this container.

        The easiest way to get this value is to use the ``docker_image`` resource as is shown in the example.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#image Container#image}
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attach(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true`` attach to the container after its creation and waits the end of its execution. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#attach Container#attach}
        '''
        result = self._values.get("attach")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[ContainerCapabilities]:
        '''capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#capabilities Container#capabilities}
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[ContainerCapabilities], result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to use to start the container.

        For example, to run ``/usr/bin/myprogram -f baz.conf`` set the command to be ``["/usr/bin/myprogram","-","baz.con"]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#command Container#command}
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def container_read_refresh_timeout_milliseconds(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''The total number of milliseconds to wait for the container to reach status 'running'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_read_refresh_timeout_milliseconds Container#container_read_refresh_timeout_milliseconds}
        '''
        result = self._values.get("container_read_refresh_timeout_milliseconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_set(self) -> typing.Optional[builtins.str]:
        '''A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. ``0-1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#cpu_set Container#cpu_set}
        '''
        result = self._values.get("cpu_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_shares(self) -> typing.Optional[jsii.Number]:
        '''CPU shares (relative weight) for the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#cpu_shares Container#cpu_shares}
        '''
        result = self._values.get("cpu_shares")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def destroy_grace_seconds(self) -> typing.Optional[jsii.Number]:
        '''If defined will attempt to stop the container before destroying.

        Container will be destroyed after ``n`` seconds or on successful stop.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#destroy_grace_seconds Container#destroy_grace_seconds}
        '''
        result = self._values.get("destroy_grace_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def devices(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerDevices"]]]:
        '''devices block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#devices Container#devices}
        '''
        result = self._values.get("devices")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerDevices"]]], result)

    @builtins.property
    def dns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNS servers to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns Container#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_opts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNS options used by the DNS provider(s), see ``resolv.conf`` documentation for valid list of options.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns_opts Container#dns_opts}
        '''
        result = self._values.get("dns_opts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_search(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNS search domains that are used when bare unqualified hostnames are used inside of the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#dns_search Container#dns_search}
        '''
        result = self._values.get("dns_search")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def domainname(self) -> typing.Optional[builtins.str]:
        '''Domain name of the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#domainname Container#domainname}
        '''
        result = self._values.get("domainname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to use as the Entrypoint for the container.

        The Entrypoint allows you to configure a container to run as an executable. For example, to run ``/usr/bin/myprogram`` when starting a container, set the entrypoint to be ``"/usr/bin/myprogra"]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#entrypoint Container#entrypoint}
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Environment variables to set in the form of ``KEY=VALUE``, e.g. ``DEBUG=0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#env Container#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gpus(self) -> typing.Optional[builtins.str]:
        '''GPU devices to add to the container.

        Currently, only the value ``all`` is supported. Passing any other value will result in unexpected behavior.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#gpus Container#gpus}
        '''
        result = self._values.get("gpus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional groups for the container user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#group_add Container#group_add}
        '''
        result = self._values.get("group_add")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def healthcheck(self) -> typing.Optional["ContainerHealthcheck"]:
        '''healthcheck block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#healthcheck Container#healthcheck}
        '''
        result = self._values.get("healthcheck")
        return typing.cast(typing.Optional["ContainerHealthcheck"], result)

    @builtins.property
    def host(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerHost"]]]:
        '''host block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host Container#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerHost"]]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Hostname of the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#hostname Container#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#id Container#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def init(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Configured whether an init process should be injected for this container.

        If unset this will default to the ``dockerd`` defaults.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#init Container#init}
        '''
        result = self._values.get("init")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ipc_mode(self) -> typing.Optional[builtins.str]:
        '''IPC sharing mode for the container. Possible values are: ``none``, ``private``, ``shareable``, ``container:<name|id>`` or ``host``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipc_mode Container#ipc_mode}
        '''
        result = self._values.get("ipc_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#labels Container#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerLabels"]]], result)

    @builtins.property
    def links(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of links for link based connectivity between containers that are running on the same host.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#links Container#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_driver(self) -> typing.Optional[builtins.str]:
        '''The logging driver to use for the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#log_driver Container#log_driver}
        '''
        result = self._values.get("log_driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_opts(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key/value pairs to use as options for the logging driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#log_opts Container#log_opts}
        '''
        result = self._values.get("log_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def logs(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Save the container logs (``attach`` must be enabled). Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#logs Container#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_retry_count(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of times to an attempt a restart when ``restart`` is set to 'on-failure'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#max_retry_count Container#max_retry_count}
        '''
        result = self._values.get("max_retry_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory(self) -> typing.Optional[jsii.Number]:
        '''The memory limit for the container in MBs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#memory Container#memory}
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_swap(self) -> typing.Optional[jsii.Number]:
        '''The total memory limit (memory + swap) for the container in MBs.

        This setting may compute to ``-1`` after ``terraform apply`` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#memory_swap Container#memory_swap}
        '''
        result = self._values.get("memory_swap")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mounts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerMounts"]]]:
        '''mounts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#mounts Container#mounts}
        '''
        result = self._values.get("mounts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerMounts"]]], result)

    @builtins.property
    def must_run(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, then the Docker container will be kept running.

        If ``false``, then as long as the container exists, Terraform assumes it is successful. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#must_run Container#must_run}
        '''
        result = self._values.get("must_run")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network_alias(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set an alias for the container in all specified networks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#network_alias Container#network_alias}
        '''
        result = self._values.get("network_alias")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Network mode of the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#network_mode Container#network_mode}
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''ID of the networks in which the container is.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#networks Container#networks}
        '''
        result = self._values.get("networks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def networks_advanced(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerNetworksAdvanced"]]]:
        '''networks_advanced block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#networks_advanced Container#networks_advanced}
        '''
        result = self._values.get("networks_advanced")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerNetworksAdvanced"]]], result)

    @builtins.property
    def pid_mode(self) -> typing.Optional[builtins.str]:
        '''he PID (Process) Namespace mode for the container. Either ``container:<name|id>`` or ``host``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#pid_mode Container#pid_mode}
        '''
        result = self._values.get("pid_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerPorts"]]]:
        '''ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ports Container#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerPorts"]]], result)

    @builtins.property
    def privileged(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, the container runs in privileged mode.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#privileged Container#privileged}
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def publish_all_ports(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Publish all ports of the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#publish_all_ports Container#publish_all_ports}
        '''
        result = self._values.get("publish_all_ports")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, the container will be started as readonly. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def remove_volumes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, it will remove anonymous volumes associated with the container. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#remove_volumes Container#remove_volumes}
        '''
        result = self._values.get("remove_volumes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def restart(self) -> typing.Optional[builtins.str]:
        '''The restart policy for the container. Must be one of 'no', 'on-failure', 'always', 'unless-stopped'. Defaults to ``no``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#restart Container#restart}
        '''
        result = self._values.get("restart")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rm(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, then the container will be automatically removed when it exits. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#rm Container#rm}
        '''
        result = self._values.get("rm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        '''Runtime to use for the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#runtime Container#runtime}
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_opts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of string values to customize labels for MLS systems, such as SELinux. See https://docs.docker.com/engine/reference/run/#security-configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#security_opts Container#security_opts}
        '''
        result = self._values.get("security_opts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shm_size(self) -> typing.Optional[jsii.Number]:
        '''Size of ``/dev/shm`` in MBs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#shm_size Container#shm_size}
        '''
        result = self._values.get("shm_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, then the Docker container will be started after creation.

        If ``false``, then the container is only created. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#start Container#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def stdin_open(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, keep STDIN open even if not attached (``docker run -i``). Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stdin_open Container#stdin_open}
        '''
        result = self._values.get("stdin_open")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def stop_signal(self) -> typing.Optional[builtins.str]:
        '''Signal to stop a container (default ``SIGTERM``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stop_signal Container#stop_signal}
        '''
        result = self._values.get("stop_signal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stop_timeout(self) -> typing.Optional[jsii.Number]:
        '''Timeout (in seconds) to stop a container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#stop_timeout Container#stop_timeout}
        '''
        result = self._values.get("stop_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_opts(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key/value pairs for the storage driver options, e.g. ``size``: ``120G``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#storage_opts Container#storage_opts}
        '''
        result = self._values.get("storage_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def sysctls(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of kernel parameters (sysctls) to set in the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#sysctls Container#sysctls}
        '''
        result = self._values.get("sysctls")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tmpfs(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of container directories which should be replaced by ``tmpfs mounts``, and their corresponding mount options.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tmpfs Container#tmpfs}
        '''
        result = self._values.get("tmpfs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tty(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, allocate a pseudo-tty (``docker run -t``). Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tty Container#tty}
        '''
        result = self._values.get("tty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ulimit(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUlimit"]]]:
        '''ulimit block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ulimit Container#ulimit}
        '''
        result = self._values.get("ulimit")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUlimit"]]], result)

    @builtins.property
    def upload(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUpload"]]]:
        '''upload block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#upload Container#upload}
        '''
        result = self._values.get("upload")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerUpload"]]], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User used for run the first process.

        Format is ``user`` or ``user:group`` which user and group can be passed literraly or by name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#user Container#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def userns_mode(self) -> typing.Optional[builtins.str]:
        '''Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#userns_mode Container#userns_mode}
        '''
        result = self._values.get("userns_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerVolumes"]]]:
        '''volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volumes Container#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerVolumes"]]], result)

    @builtins.property
    def working_dir(self) -> typing.Optional[builtins.str]:
        '''The working directory for commands to run in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#working_dir Container#working_dir}
        '''
        result = self._values.get("working_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerDevices",
    jsii_struct_bases=[],
    name_mapping={
        "host_path": "hostPath",
        "container_path": "containerPath",
        "permissions": "permissions",
    },
)
class ContainerDevices:
    def __init__(
        self,
        *,
        host_path: builtins.str,
        container_path: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_path: The path on the host where the device is located. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host_path Container#host_path}
        :param container_path: The path in the container where the device will be bound. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_path Container#container_path}
        :param permissions: The cgroup permissions given to the container to access the device. Defaults to ``rwm``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#permissions Container#permissions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerDevices.__init__)
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_path": host_path,
        }
        if container_path is not None:
            self._values["container_path"] = container_path
        if permissions is not None:
            self._values["permissions"] = permissions

    @builtins.property
    def host_path(self) -> builtins.str:
        '''The path on the host where the device is located.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host_path Container#host_path}
        '''
        result = self._values.get("host_path")
        assert result is not None, "Required property 'host_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_path(self) -> typing.Optional[builtins.str]:
        '''The path in the container where the device will be bound.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_path Container#container_path}
        '''
        result = self._values.get("container_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''The cgroup permissions given to the container to access the device. Defaults to ``rwm``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#permissions Container#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerDevices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerDevicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerDevicesList",
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
            type_hints = typing.get_type_hints(ContainerDevicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerDevicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerDevicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerDevicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerDevicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerDevicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerDevicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerDevices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerDevices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerDevices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerDevicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerDevicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerDevicesOutputReference",
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
            type_hints = typing.get_type_hints(ContainerDevicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContainerPath")
    def reset_container_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPath", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @builtins.property
    @jsii.member(jsii_name="containerPathInput")
    def container_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerPathInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPath")
    def container_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerPath"))

    @container_path.setter
    def container_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerDevicesOutputReference, "container_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPath", value)

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPath"))

    @host_path.setter
    def host_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerDevicesOutputReference, "host_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPath", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerDevicesOutputReference, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerDevices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerDevices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerDevices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerDevicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerHealthcheck",
    jsii_struct_bases=[],
    name_mapping={
        "test": "test",
        "interval": "interval",
        "retries": "retries",
        "start_period": "startPeriod",
        "timeout": "timeout",
    },
)
class ContainerHealthcheck:
    def __init__(
        self,
        *,
        test: typing.Sequence[builtins.str],
        interval: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        start_period: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param test: Command to run to check health. For example, to run ``curl -f localhost/health`` set the command to be ``["CMD", "curl", "-f", "localhost/health"]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#test Container#test}
        :param interval: Time between running the check (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#interval Container#interval}
        :param retries: Consecutive failures needed to report unhealthy. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#retries Container#retries}
        :param start_period: Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#start_period Container#start_period}
        :param timeout: Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#timeout Container#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerHealthcheck.__init__)
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument start_period", value=start_period, expected_type=type_hints["start_period"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "test": test,
        }
        if interval is not None:
            self._values["interval"] = interval
        if retries is not None:
            self._values["retries"] = retries
        if start_period is not None:
            self._values["start_period"] = start_period
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def test(self) -> typing.List[builtins.str]:
        '''Command to run to check health.

        For example, to run ``curl -f localhost/health`` set the command to be ``["CMD", "curl", "-f", "localhost/health"]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#test Container#test}
        '''
        result = self._values.get("test")
        assert result is not None, "Required property 'test' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time between running the check (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#interval Container#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Consecutive failures needed to report unhealthy. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#retries Container#retries}
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_period(self) -> typing.Optional[builtins.str]:
        '''Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#start_period Container#start_period}
        '''
        result = self._values.get("start_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#timeout Container#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerHealthcheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerHealthcheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerHealthcheckOutputReference",
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
            type_hints = typing.get_type_hints(ContainerHealthcheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetStartPeriod")
    def reset_start_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartPeriod", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="startPeriodInput")
    def start_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="testInput")
    def test_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "testInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHealthcheckOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHealthcheckOutputReference, "retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value)

    @builtins.property
    @jsii.member(jsii_name="startPeriod")
    def start_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startPeriod"))

    @start_period.setter
    def start_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHealthcheckOutputReference, "start_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="test")
    def test(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "test"))

    @test.setter
    def test(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHealthcheckOutputReference, "test").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "test", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHealthcheckOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerHealthcheck]:
        return typing.cast(typing.Optional[ContainerHealthcheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerHealthcheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHealthcheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerHost",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "ip": "ip"},
)
class ContainerHost:
    def __init__(self, *, host: builtins.str, ip: builtins.str) -> None:
        '''
        :param host: Hostname to add. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host Container#host}
        :param ip: IP address this hostname should resolve to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ip Container#ip}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerHost.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
        self._values: typing.Dict[str, typing.Any] = {
            "host": host,
            "ip": ip,
        }

    @builtins.property
    def host(self) -> builtins.str:
        '''Hostname to add.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host Container#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip(self) -> builtins.str:
        '''IP address this hostname should resolve to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ip Container#ip}
        '''
        result = self._values.get("ip")
        assert result is not None, "Required property 'ip' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerHostList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerHostList",
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
            type_hints = typing.get_type_hints(ContainerHostList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerHostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerHostList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerHostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHostList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerHostList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerHostList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerHost]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerHost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerHost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHostList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerHostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerHostOutputReference",
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
            type_hints = typing.get_type_hints(ContainerHostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHostOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHostOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerHost, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerHost, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerHost, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerHostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ContainerLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#label Container#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#value Container#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerLabels.__init__)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#label Container#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#value Container#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerLabelsList",
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
            type_hints = typing.get_type_hints(ContainerLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerLabelsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerLabelsOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerMounts",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "type": "type",
        "bind_options": "bindOptions",
        "read_only": "readOnly",
        "source": "source",
        "tmpfs_options": "tmpfsOptions",
        "volume_options": "volumeOptions",
    },
)
class ContainerMounts:
    def __init__(
        self,
        *,
        target: builtins.str,
        type: builtins.str,
        bind_options: typing.Optional[typing.Union["ContainerMountsBindOptions", typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
        tmpfs_options: typing.Optional[typing.Union["ContainerMountsTmpfsOptions", typing.Dict[str, typing.Any]]] = None,
        volume_options: typing.Optional[typing.Union["ContainerMountsVolumeOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: Container path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#target Container#target}
        :param type: The mount type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#type Container#type}
        :param bind_options: bind_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#bind_options Container#bind_options}
        :param read_only: Whether the mount should be read-only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        :param source: Mount source (e.g. a volume name, a host path). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#source Container#source}
        :param tmpfs_options: tmpfs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tmpfs_options Container#tmpfs_options}
        :param volume_options: volume_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volume_options Container#volume_options}
        '''
        if isinstance(bind_options, dict):
            bind_options = ContainerMountsBindOptions(**bind_options)
        if isinstance(tmpfs_options, dict):
            tmpfs_options = ContainerMountsTmpfsOptions(**tmpfs_options)
        if isinstance(volume_options, dict):
            volume_options = ContainerMountsVolumeOptions(**volume_options)
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMounts.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bind_options", value=bind_options, expected_type=type_hints["bind_options"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tmpfs_options", value=tmpfs_options, expected_type=type_hints["tmpfs_options"])
            check_type(argname="argument volume_options", value=volume_options, expected_type=type_hints["volume_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
            "type": type,
        }
        if bind_options is not None:
            self._values["bind_options"] = bind_options
        if read_only is not None:
            self._values["read_only"] = read_only
        if source is not None:
            self._values["source"] = source
        if tmpfs_options is not None:
            self._values["tmpfs_options"] = tmpfs_options
        if volume_options is not None:
            self._values["volume_options"] = volume_options

    @builtins.property
    def target(self) -> builtins.str:
        '''Container path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#target Container#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The mount type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#type Container#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_options(self) -> typing.Optional["ContainerMountsBindOptions"]:
        '''bind_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#bind_options Container#bind_options}
        '''
        result = self._values.get("bind_options")
        return typing.cast(typing.Optional["ContainerMountsBindOptions"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the mount should be read-only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Mount source (e.g. a volume name, a host path).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#source Container#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tmpfs_options(self) -> typing.Optional["ContainerMountsTmpfsOptions"]:
        '''tmpfs_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#tmpfs_options Container#tmpfs_options}
        '''
        result = self._values.get("tmpfs_options")
        return typing.cast(typing.Optional["ContainerMountsTmpfsOptions"], result)

    @builtins.property
    def volume_options(self) -> typing.Optional["ContainerMountsVolumeOptions"]:
        '''volume_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volume_options Container#volume_options}
        '''
        result = self._values.get("volume_options")
        return typing.cast(typing.Optional["ContainerMountsVolumeOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerMountsBindOptions",
    jsii_struct_bases=[],
    name_mapping={"propagation": "propagation"},
)
class ContainerMountsBindOptions:
    def __init__(self, *, propagation: typing.Optional[builtins.str] = None) -> None:
        '''
        :param propagation: A propagation mode with the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#propagation Container#propagation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsBindOptions.__init__)
            check_type(argname="argument propagation", value=propagation, expected_type=type_hints["propagation"])
        self._values: typing.Dict[str, typing.Any] = {}
        if propagation is not None:
            self._values["propagation"] = propagation

    @builtins.property
    def propagation(self) -> typing.Optional[builtins.str]:
        '''A propagation mode with the value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#propagation Container#propagation}
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerMountsBindOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsBindOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerMountsBindOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPropagation")
    def reset_propagation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagation", []))

    @builtins.property
    @jsii.member(jsii_name="propagationInput")
    def propagation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagationInput"))

    @builtins.property
    @jsii.member(jsii_name="propagation")
    def propagation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagation"))

    @propagation.setter
    def propagation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsBindOptionsOutputReference, "propagation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerMountsBindOptions]:
        return typing.cast(typing.Optional[ContainerMountsBindOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerMountsBindOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsBindOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerMountsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsList",
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
            type_hints = typing.get_type_hints(ContainerMountsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerMountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerMountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerMountsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerMountsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMounts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMounts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMounts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerMountsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerMountsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBindOptions")
    def put_bind_options(
        self,
        *,
        propagation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param propagation: A propagation mode with the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#propagation Container#propagation}
        '''
        value = ContainerMountsBindOptions(propagation=propagation)

        return typing.cast(None, jsii.invoke(self, "putBindOptions", [value]))

    @jsii.member(jsii_name="putTmpfsOptions")
    def put_tmpfs_options(
        self,
        *,
        mode: typing.Optional[jsii.Number] = None,
        size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: The permission mode for the tmpfs mount in an integer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#mode Container#mode}
        :param size_bytes: The size for the tmpfs mount in bytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#size_bytes Container#size_bytes}
        '''
        value = ContainerMountsTmpfsOptions(mode=mode, size_bytes=size_bytes)

        return typing.cast(None, jsii.invoke(self, "putTmpfsOptions", [value]))

    @jsii.member(jsii_name="putVolumeOptions")
    def put_volume_options(
        self,
        *,
        driver_name: typing.Optional[builtins.str] = None,
        driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerMountsVolumeOptionsLabels", typing.Dict[str, typing.Any]]]]] = None,
        no_copy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param driver_name: Name of the driver to use to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#driver_name Container#driver_name}
        :param driver_options: key/value map of driver specific options. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#driver_options Container#driver_options}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#labels Container#labels}
        :param no_copy: Populate volume with data from the target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#no_copy Container#no_copy}
        '''
        value = ContainerMountsVolumeOptions(
            driver_name=driver_name,
            driver_options=driver_options,
            labels=labels,
            no_copy=no_copy,
        )

        return typing.cast(None, jsii.invoke(self, "putVolumeOptions", [value]))

    @jsii.member(jsii_name="resetBindOptions")
    def reset_bind_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBindOptions", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetTmpfsOptions")
    def reset_tmpfs_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTmpfsOptions", []))

    @jsii.member(jsii_name="resetVolumeOptions")
    def reset_volume_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeOptions", []))

    @builtins.property
    @jsii.member(jsii_name="bindOptions")
    def bind_options(self) -> ContainerMountsBindOptionsOutputReference:
        return typing.cast(ContainerMountsBindOptionsOutputReference, jsii.get(self, "bindOptions"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsOptions")
    def tmpfs_options(self) -> "ContainerMountsTmpfsOptionsOutputReference":
        return typing.cast("ContainerMountsTmpfsOptionsOutputReference", jsii.get(self, "tmpfsOptions"))

    @builtins.property
    @jsii.member(jsii_name="volumeOptions")
    def volume_options(self) -> "ContainerMountsVolumeOptionsOutputReference":
        return typing.cast("ContainerMountsVolumeOptionsOutputReference", jsii.get(self, "volumeOptions"))

    @builtins.property
    @jsii.member(jsii_name="bindOptionsInput")
    def bind_options_input(self) -> typing.Optional[ContainerMountsBindOptions]:
        return typing.cast(typing.Optional[ContainerMountsBindOptions], jsii.get(self, "bindOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsOptionsInput")
    def tmpfs_options_input(self) -> typing.Optional["ContainerMountsTmpfsOptions"]:
        return typing.cast(typing.Optional["ContainerMountsTmpfsOptions"], jsii.get(self, "tmpfsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeOptionsInput")
    def volume_options_input(self) -> typing.Optional["ContainerMountsVolumeOptions"]:
        return typing.cast(typing.Optional["ContainerMountsVolumeOptions"], jsii.get(self, "volumeOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerMounts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerMounts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerMounts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerMountsTmpfsOptions",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "size_bytes": "sizeBytes"},
)
class ContainerMountsTmpfsOptions:
    def __init__(
        self,
        *,
        mode: typing.Optional[jsii.Number] = None,
        size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: The permission mode for the tmpfs mount in an integer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#mode Container#mode}
        :param size_bytes: The size for the tmpfs mount in bytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#size_bytes Container#size_bytes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsTmpfsOptions.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument size_bytes", value=size_bytes, expected_type=type_hints["size_bytes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if size_bytes is not None:
            self._values["size_bytes"] = size_bytes

    @builtins.property
    def mode(self) -> typing.Optional[jsii.Number]:
        '''The permission mode for the tmpfs mount in an integer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#mode Container#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def size_bytes(self) -> typing.Optional[jsii.Number]:
        '''The size for the tmpfs mount in bytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#size_bytes Container#size_bytes}
        '''
        result = self._values.get("size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsTmpfsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerMountsTmpfsOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsTmpfsOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerMountsTmpfsOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSizeBytes")
    def reset_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeBytes", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeBytesInput")
    def size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsTmpfsOptionsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="sizeBytes")
    def size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeBytes"))

    @size_bytes.setter
    def size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsTmpfsOptionsOutputReference, "size_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerMountsTmpfsOptions]:
        return typing.cast(typing.Optional[ContainerMountsTmpfsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerMountsTmpfsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsTmpfsOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerMountsVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "driver_name": "driverName",
        "driver_options": "driverOptions",
        "labels": "labels",
        "no_copy": "noCopy",
    },
)
class ContainerMountsVolumeOptions:
    def __init__(
        self,
        *,
        driver_name: typing.Optional[builtins.str] = None,
        driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ContainerMountsVolumeOptionsLabels", typing.Dict[str, typing.Any]]]]] = None,
        no_copy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param driver_name: Name of the driver to use to create the volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#driver_name Container#driver_name}
        :param driver_options: key/value map of driver specific options. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#driver_options Container#driver_options}
        :param labels: labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#labels Container#labels}
        :param no_copy: Populate volume with data from the target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#no_copy Container#no_copy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptions.__init__)
            check_type(argname="argument driver_name", value=driver_name, expected_type=type_hints["driver_name"])
            check_type(argname="argument driver_options", value=driver_options, expected_type=type_hints["driver_options"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument no_copy", value=no_copy, expected_type=type_hints["no_copy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if driver_name is not None:
            self._values["driver_name"] = driver_name
        if driver_options is not None:
            self._values["driver_options"] = driver_options
        if labels is not None:
            self._values["labels"] = labels
        if no_copy is not None:
            self._values["no_copy"] = no_copy

    @builtins.property
    def driver_name(self) -> typing.Optional[builtins.str]:
        '''Name of the driver to use to create the volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#driver_name Container#driver_name}
        '''
        result = self._values.get("driver_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''key/value map of driver specific options.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#driver_options Container#driver_options}
        '''
        result = self._values.get("driver_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerMountsVolumeOptionsLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#labels Container#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ContainerMountsVolumeOptionsLabels"]]], result)

    @builtins.property
    def no_copy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Populate volume with data from the target.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#no_copy Container#no_copy}
        '''
        result = self._values.get("no_copy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerMountsVolumeOptionsLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ContainerMountsVolumeOptionsLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#label Container#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#value Container#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptionsLabels.__init__)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#label Container#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#value Container#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsVolumeOptionsLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerMountsVolumeOptionsLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsVolumeOptionsLabelsList",
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
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptionsLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerMountsVolumeOptionsLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptionsLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerMountsVolumeOptionsLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerMountsVolumeOptionsLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsVolumeOptionsLabelsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptionsLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerMountsVolumeOptionsLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerMountsVolumeOptionsLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerMountsVolumeOptionsLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerMountsVolumeOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerMountsVolumeOptionsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ContainerMountsVolumeOptionsLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerMountsVolumeOptionsOutputReference.put_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="resetDriverName")
    def reset_driver_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverName", []))

    @jsii.member(jsii_name="resetDriverOptions")
    def reset_driver_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverOptions", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetNoCopy")
    def reset_no_copy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoCopy", []))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> ContainerMountsVolumeOptionsLabelsList:
        return typing.cast(ContainerMountsVolumeOptionsLabelsList, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="driverNameInput")
    def driver_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="driverOptionsInput")
    def driver_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="noCopyInput")
    def no_copy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noCopyInput"))

    @builtins.property
    @jsii.member(jsii_name="driverName")
    def driver_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverName"))

    @driver_name.setter
    def driver_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsOutputReference, "driver_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverName", value)

    @builtins.property
    @jsii.member(jsii_name="driverOptions")
    def driver_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverOptions"))

    @driver_options.setter
    def driver_options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsOutputReference, "driver_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverOptions", value)

    @builtins.property
    @jsii.member(jsii_name="noCopy")
    def no_copy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noCopy"))

    @no_copy.setter
    def no_copy(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsOutputReference, "no_copy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noCopy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerMountsVolumeOptions]:
        return typing.cast(typing.Optional[ContainerMountsVolumeOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerMountsVolumeOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerMountsVolumeOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerNetworkData",
    jsii_struct_bases=[],
    name_mapping={},
)
class ContainerNetworkData:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerNetworkData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerNetworkDataList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerNetworkDataList",
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
            type_hints = typing.get_type_hints(ContainerNetworkDataList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerNetworkDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerNetworkDataList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerNetworkDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworkDataList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerNetworkDataList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerNetworkDataList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class ContainerNetworkDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerNetworkDataOutputReference",
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
            type_hints = typing.get_type_hints(ContainerNetworkDataOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @builtins.property
    @jsii.member(jsii_name="globalIpv6Address")
    def global_ipv6_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalIpv6Address"))

    @builtins.property
    @jsii.member(jsii_name="globalIpv6PrefixLength")
    def global_ipv6_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "globalIpv6PrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipPrefixLength")
    def ip_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipPrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Gateway")
    def ipv6_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6Gateway"))

    @builtins.property
    @jsii.member(jsii_name="networkName")
    def network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerNetworkData]:
        return typing.cast(typing.Optional[ContainerNetworkData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerNetworkData]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworkDataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerNetworksAdvanced",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "aliases": "aliases",
        "ipv4_address": "ipv4Address",
        "ipv6_address": "ipv6Address",
    },
)
class ContainerNetworksAdvanced:
    def __init__(
        self,
        *,
        name: builtins.str,
        aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv4_address: typing.Optional[builtins.str] = None,
        ipv6_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name or id of the network to use. You can use ``name`` or ``id`` attribute from a ``docker_network`` resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        :param aliases: The network aliases of the container in the specific network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#aliases Container#aliases}
        :param ipv4_address: The IPV4 address of the container in the specific network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipv4_address Container#ipv4_address}
        :param ipv6_address: The IPV6 address of the container in the specific network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipv6_address Container#ipv6_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerNetworksAdvanced.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aliases", value=aliases, expected_type=type_hints["aliases"])
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument ipv6_address", value=ipv6_address, expected_type=type_hints["ipv6_address"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if aliases is not None:
            self._values["aliases"] = aliases
        if ipv4_address is not None:
            self._values["ipv4_address"] = ipv4_address
        if ipv6_address is not None:
            self._values["ipv6_address"] = ipv6_address

    @builtins.property
    def name(self) -> builtins.str:
        '''The name or id of the network to use.

        You can use ``name`` or ``id`` attribute from a ``docker_network`` resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The network aliases of the container in the specific network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#aliases Container#aliases}
        '''
        result = self._values.get("aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv4_address(self) -> typing.Optional[builtins.str]:
        '''The IPV4 address of the container in the specific network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipv4_address Container#ipv4_address}
        '''
        result = self._values.get("ipv4_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_address(self) -> typing.Optional[builtins.str]:
        '''The IPV6 address of the container in the specific network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ipv6_address Container#ipv6_address}
        '''
        result = self._values.get("ipv6_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerNetworksAdvanced(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerNetworksAdvancedList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerNetworksAdvancedList",
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
            type_hints = typing.get_type_hints(ContainerNetworksAdvancedList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerNetworksAdvancedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerNetworksAdvancedList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerNetworksAdvancedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerNetworksAdvanced]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerNetworksAdvanced]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerNetworksAdvanced]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerNetworksAdvancedOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerNetworksAdvancedOutputReference",
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
            type_hints = typing.get_type_hints(ContainerNetworksAdvancedOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAliases")
    def reset_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliases", []))

    @jsii.member(jsii_name="resetIpv4Address")
    def reset_ipv4_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Address", []))

    @jsii.member(jsii_name="resetIpv6Address")
    def reset_ipv6_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Address", []))

    @builtins.property
    @jsii.member(jsii_name="aliasesInput")
    def aliases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressInput")
    def ipv4_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressInput")
    def ipv6_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="aliases")
    def aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aliases"))

    @aliases.setter
    def aliases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedOutputReference, "aliases").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliases", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedOutputReference, "ipv4_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6Address")
    def ipv6_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6Address"))

    @ipv6_address.setter
    def ipv6_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedOutputReference, "ipv6_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Address", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerNetworksAdvanced, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerNetworksAdvanced, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerNetworksAdvanced, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerNetworksAdvancedOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerPorts",
    jsii_struct_bases=[],
    name_mapping={
        "internal": "internal",
        "external": "external",
        "ip": "ip",
        "protocol": "protocol",
    },
)
class ContainerPorts:
    def __init__(
        self,
        *,
        internal: jsii.Number,
        external: typing.Optional[jsii.Number] = None,
        ip: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param internal: Port within the container. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#internal Container#internal}
        :param external: Port exposed out of the container. If not given a free random port ``>= 32768`` will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#external Container#external}
        :param ip: IP address/mask that can access this port. Defaults to ``0.0.0.0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ip Container#ip}
        :param protocol: Protocol that can be used over this port. Defaults to ``tcp``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#protocol Container#protocol}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerPorts.__init__)
            check_type(argname="argument internal", value=internal, expected_type=type_hints["internal"])
            check_type(argname="argument external", value=external, expected_type=type_hints["external"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "internal": internal,
        }
        if external is not None:
            self._values["external"] = external
        if ip is not None:
            self._values["ip"] = ip
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def internal(self) -> jsii.Number:
        '''Port within the container.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#internal Container#internal}
        '''
        result = self._values.get("internal")
        assert result is not None, "Required property 'internal' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def external(self) -> typing.Optional[jsii.Number]:
        '''Port exposed out of the container. If not given a free random port ``>= 32768`` will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#external Container#external}
        '''
        result = self._values.get("external")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        '''IP address/mask that can access this port. Defaults to ``0.0.0.0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#ip Container#ip}
        '''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Protocol that can be used over this port. Defaults to ``tcp``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#protocol Container#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerPortsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerPortsList",
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
            type_hints = typing.get_type_hints(ContainerPortsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerPortsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerPortsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerPortsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerPorts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerPortsOutputReference",
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
            type_hints = typing.get_type_hints(ContainerPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExternal")
    def reset_external(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternal", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="externalInput")
    def external_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "externalInput"))

    @builtins.property
    @jsii.member(jsii_name="internalInput")
    def internal_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "internalInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="external")
    def external(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "external"))

    @external.setter
    def external(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsOutputReference, "external").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "external", value)

    @builtins.property
    @jsii.member(jsii_name="internal")
    def internal(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "internal"))

    @internal.setter
    def internal(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsOutputReference, "internal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internal", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerPorts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerPorts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerPorts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerUlimit",
    jsii_struct_bases=[],
    name_mapping={"hard": "hard", "name": "name", "soft": "soft"},
)
class ContainerUlimit:
    def __init__(
        self,
        *,
        hard: jsii.Number,
        name: builtins.str,
        soft: jsii.Number,
    ) -> None:
        '''
        :param hard: The hard limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#hard Container#hard}
        :param name: The name of the ulimit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        :param soft: The soft limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#soft Container#soft}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerUlimit.__init__)
            check_type(argname="argument hard", value=hard, expected_type=type_hints["hard"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument soft", value=soft, expected_type=type_hints["soft"])
        self._values: typing.Dict[str, typing.Any] = {
            "hard": hard,
            "name": name,
            "soft": soft,
        }

    @builtins.property
    def hard(self) -> jsii.Number:
        '''The hard limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#hard Container#hard}
        '''
        result = self._values.get("hard")
        assert result is not None, "Required property 'hard' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the ulimit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#name Container#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def soft(self) -> jsii.Number:
        '''The soft limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#soft Container#soft}
        '''
        result = self._values.get("soft")
        assert result is not None, "Required property 'soft' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerUlimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerUlimitList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerUlimitList",
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
            type_hints = typing.get_type_hints(ContainerUlimitList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerUlimitOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerUlimitList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerUlimitOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUlimitList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerUlimitList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerUlimitList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerUlimit]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerUlimit]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerUlimit]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUlimitList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerUlimitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerUlimitOutputReference",
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
            type_hints = typing.get_type_hints(ContainerUlimitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hardInput")
    def hard_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hardInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="softInput")
    def soft_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "softInput"))

    @builtins.property
    @jsii.member(jsii_name="hard")
    def hard(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hard"))

    @hard.setter
    def hard(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUlimitOutputReference, "hard").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hard", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUlimitOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="soft")
    def soft(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "soft"))

    @soft.setter
    def soft(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUlimitOutputReference, "soft").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "soft", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerUlimit, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerUlimit, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerUlimit, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUlimitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerUpload",
    jsii_struct_bases=[],
    name_mapping={
        "file": "file",
        "content": "content",
        "content_base64": "contentBase64",
        "executable": "executable",
        "source": "source",
        "source_hash": "sourceHash",
    },
)
class ContainerUpload:
    def __init__(
        self,
        *,
        file: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
        source_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file: Path to the file in the container where is upload goes to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#file Container#file}
        :param content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text. Conflicts with ``content_base64`` & ``source`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#content Container#content}
        :param content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for larger binary content such as the result of the ``base64encode`` interpolation function. See `here <https://github.com/terraform-providers/terraform-provider-docker/issues/48#issuecomment-374174588>`_ for the reason. Conflicts with ``content`` & ``source`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#content_base64 Container#content_base64}
        :param executable: If ``true``, the file will be uploaded with user executable permission. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#executable Container#executable}
        :param source: A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state. Conflicts with ``content`` & ``content_base64`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#source Container#source}
        :param source_hash: If using ``source``, this will force an update if the file content has updated but the filename has not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#source_hash Container#source_hash}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerUpload.__init__)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_base64", value=content_base64, expected_type=type_hints["content_base64"])
            check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument source_hash", value=source_hash, expected_type=type_hints["source_hash"])
        self._values: typing.Dict[str, typing.Any] = {
            "file": file,
        }
        if content is not None:
            self._values["content"] = content
        if content_base64 is not None:
            self._values["content_base64"] = content_base64
        if executable is not None:
            self._values["executable"] = executable
        if source is not None:
            self._values["source"] = source
        if source_hash is not None:
            self._values["source_hash"] = source_hash

    @builtins.property
    def file(self) -> builtins.str:
        '''Path to the file in the container where is upload goes to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#file Container#file}
        '''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

        Conflicts with ``content_base64`` & ``source``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#content Container#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_base64(self) -> typing.Optional[builtins.str]:
        '''Base64-encoded data that will be decoded and uploaded as raw bytes for the object content.

        This allows safely uploading non-UTF8 binary data, but is recommended only for larger binary content such as the result of the ``base64encode`` interpolation function. See `here <https://github.com/terraform-providers/terraform-provider-docker/issues/48#issuecomment-374174588>`_ for the reason. Conflicts with ``content`` & ``source``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#content_base64 Container#content_base64}
        '''
        result = self._values.get("content_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def executable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, the file will be uploaded with user executable permission. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#executable Container#executable}
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''A filename that references a file which will be uploaded as the object content.

        This allows for large file uploads that do not get stored in state. Conflicts with ``content`` & ``content_base64``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#source Container#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_hash(self) -> typing.Optional[builtins.str]:
        '''If using ``source``, this will force an update if the file content has updated but the filename has not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#source_hash Container#source_hash}
        '''
        result = self._values.get("source_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerUpload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerUploadList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerUploadList",
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
            type_hints = typing.get_type_hints(ContainerUploadList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerUploadOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerUploadList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerUploadOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerUploadList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerUploadList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerUpload]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerUpload]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerUpload]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerUploadOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerUploadOutputReference",
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
            type_hints = typing.get_type_hints(ContainerUploadOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentBase64")
    def reset_content_base64(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentBase64", []))

    @jsii.member(jsii_name="resetExecutable")
    def reset_executable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutable", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSourceHash")
    def reset_source_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceHash", []))

    @builtins.property
    @jsii.member(jsii_name="contentBase64Input")
    def content_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="executableInput")
    def executable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "executableInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceHashInput")
    def source_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceHashInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentBase64")
    def content_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentBase64"))

    @content_base64.setter
    def content_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "content_base64").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentBase64", value)

    @builtins.property
    @jsii.member(jsii_name="executable")
    def executable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "executable"))

    @executable.setter
    def executable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "executable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executable", value)

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="sourceHash")
    def source_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceHash"))

    @source_hash.setter
    def source_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "source_hash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceHash", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerUpload, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerUpload, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerUpload, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerUploadOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-docker.container.ContainerVolumes",
    jsii_struct_bases=[],
    name_mapping={
        "container_path": "containerPath",
        "from_container": "fromContainer",
        "host_path": "hostPath",
        "read_only": "readOnly",
        "volume_name": "volumeName",
    },
)
class ContainerVolumes:
    def __init__(
        self,
        *,
        container_path: typing.Optional[builtins.str] = None,
        from_container: typing.Optional[builtins.str] = None,
        host_path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_path: The path in the container where the volume will be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_path Container#container_path}
        :param from_container: The container where the volume is coming from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#from_container Container#from_container}
        :param host_path: The path on the host where the volume is coming from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host_path Container#host_path}
        :param read_only: If ``true``, this volume will be readonly. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        :param volume_name: The name of the docker volume which should be mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volume_name Container#volume_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerVolumes.__init__)
            check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
            check_type(argname="argument from_container", value=from_container, expected_type=type_hints["from_container"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument volume_name", value=volume_name, expected_type=type_hints["volume_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if container_path is not None:
            self._values["container_path"] = container_path
        if from_container is not None:
            self._values["from_container"] = from_container
        if host_path is not None:
            self._values["host_path"] = host_path
        if read_only is not None:
            self._values["read_only"] = read_only
        if volume_name is not None:
            self._values["volume_name"] = volume_name

    @builtins.property
    def container_path(self) -> typing.Optional[builtins.str]:
        '''The path in the container where the volume will be mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#container_path Container#container_path}
        '''
        result = self._values.get("container_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_container(self) -> typing.Optional[builtins.str]:
        '''The container where the volume is coming from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#from_container Container#from_container}
        '''
        result = self._values.get("from_container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_path(self) -> typing.Optional[builtins.str]:
        '''The path on the host where the volume is coming from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#host_path Container#host_path}
        '''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, this volume will be readonly. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#read_only Container#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def volume_name(self) -> typing.Optional[builtins.str]:
        '''The name of the docker volume which should be mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/docker/r/container#volume_name Container#volume_name}
        '''
        result = self._values.get("volume_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerVolumesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerVolumesList",
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
            type_hints = typing.get_type_hints(ContainerVolumesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContainerVolumesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerVolumesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ContainerVolumesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ContainerVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContainerVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-docker.container.ContainerVolumesOutputReference",
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
            type_hints = typing.get_type_hints(ContainerVolumesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContainerPath")
    def reset_container_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPath", []))

    @jsii.member(jsii_name="resetFromContainer")
    def reset_from_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromContainer", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetVolumeName")
    def reset_volume_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeName", []))

    @builtins.property
    @jsii.member(jsii_name="containerPathInput")
    def container_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerPathInput"))

    @builtins.property
    @jsii.member(jsii_name="fromContainerInput")
    def from_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeNameInput")
    def volume_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPath")
    def container_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerPath"))

    @container_path.setter
    def container_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesOutputReference, "container_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPath", value)

    @builtins.property
    @jsii.member(jsii_name="fromContainer")
    def from_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromContainer"))

    @from_container.setter
    def from_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesOutputReference, "from_container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromContainer", value)

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPath"))

    @host_path.setter
    def host_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesOutputReference, "host_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPath", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeName")
    def volume_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeName"))

    @volume_name.setter
    def volume_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesOutputReference, "volume_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContainerVolumes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContainerVolumes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContainerVolumes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContainerVolumesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Container",
    "ContainerCapabilities",
    "ContainerCapabilitiesOutputReference",
    "ContainerConfig",
    "ContainerDevices",
    "ContainerDevicesList",
    "ContainerDevicesOutputReference",
    "ContainerHealthcheck",
    "ContainerHealthcheckOutputReference",
    "ContainerHost",
    "ContainerHostList",
    "ContainerHostOutputReference",
    "ContainerLabels",
    "ContainerLabelsList",
    "ContainerLabelsOutputReference",
    "ContainerMounts",
    "ContainerMountsBindOptions",
    "ContainerMountsBindOptionsOutputReference",
    "ContainerMountsList",
    "ContainerMountsOutputReference",
    "ContainerMountsTmpfsOptions",
    "ContainerMountsTmpfsOptionsOutputReference",
    "ContainerMountsVolumeOptions",
    "ContainerMountsVolumeOptionsLabels",
    "ContainerMountsVolumeOptionsLabelsList",
    "ContainerMountsVolumeOptionsLabelsOutputReference",
    "ContainerMountsVolumeOptionsOutputReference",
    "ContainerNetworkData",
    "ContainerNetworkDataList",
    "ContainerNetworkDataOutputReference",
    "ContainerNetworksAdvanced",
    "ContainerNetworksAdvancedList",
    "ContainerNetworksAdvancedOutputReference",
    "ContainerPorts",
    "ContainerPortsList",
    "ContainerPortsOutputReference",
    "ContainerUlimit",
    "ContainerUlimitList",
    "ContainerUlimitOutputReference",
    "ContainerUpload",
    "ContainerUploadList",
    "ContainerUploadOutputReference",
    "ContainerVolumes",
    "ContainerVolumesList",
    "ContainerVolumesOutputReference",
]

publication.publish()
