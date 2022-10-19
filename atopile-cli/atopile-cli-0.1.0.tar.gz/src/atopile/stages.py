import logging
import shlex
from hashlib import sha1
from pathlib import Path
from typing import Dict, List, Optional, Union
import os

import aiodocker
import yaml
from attrs import define

from . import options, utils, resources

log = logging.getLogger(__name__)

@define
class StageDef:
    path: str
    image: str
    command: str
    inputs: Dict[str, Dict[str, str]]
    outputs: Dict[str, Dict[str, str]]

    @classmethod
    def from_file(cls, file: Path):
        with file.open('r') as f:
            stage_raw: dict = yaml.safe_load(f)

        path = stage_raw.get('path')
        image = stage_raw.get('image')
        command = stage_raw.get('command', None)
        inputs = stage_raw.get('inputs', {})
        outputs = stage_raw.get('outputs', {})
        return cls(
            path=path,
            image=image,
            command=command,
            inputs=inputs,
            outputs=outputs,
        )


class StageIO:
    """
    Base class of "things that can be input to stages"
    """
    typename: str

    @property
    def reference(self) -> str:
        raise NotImplementedError

    @property
    def fs_location(self) -> Path:
        raise NotImplementedError

    @classmethod
    def check(cls, candidate: str):
        raise NotImplementedError

    @classmethod
    def from_data(cls, candidate_data, def_data: dict):
        if not def_data.get('list', False):
            candidates = [candidate_data]
        else:
            candidates = candidate_data

        for candidate in candidates:
            for T in (Handle, File):
                if T.check(candidate):
                    return T.from_string(candidate, def_data)

@define
class File(StageIO):
    """
    Represents a file in the filesystem from the start of compile time
    """
    path: Path

    @property
    def reference(self) -> str:
        return str(self.path)

    @property
    def fs_location(self) -> Path:
        return self.path

    @classmethod
    def check(cls, candidate: str):
        return True

    @classmethod
    def from_string(cls, candidate: str, def_data: dict):
        full_path = options.project_dir.value / candidate
        return cls(
            path=full_path, 
        )

@define
class Handle(StageIO):
    """
    Represents a direct output of another stage having been run
    """
    stage: str
    output_name: str
    typename: str
    filename: str
    glob_pattern: str

    _SPLITTING_CHAR = ':'

    @property
    def reference(self) -> str:
        return f'{self.stage}:{self.output_name}'

    @property
    def fs_location(self) -> Union[Path, List[Path]]:
        if self.filename:
            return options.build_dir.value / self.stage / self.filename
        if self.glob_pattern:
            return (options.build_dir.value / self.stage).glob(self.glob_pattern)

    def exists(self):
        if self.filename:
            return self.fs_location.exists()
        if self.glob_pattern:
            return len(list(self.fs_location))

    @classmethod
    def check(cls, candidate: str):
        return cls._SPLITTING_CHAR in candidate

    @classmethod
    def from_stage_name_def_data(cls, stage_name: str, output_name: str, def_data: dict):
        glob_pattern = def_data.get('pattern')
        filename = def_data.get('filename')
        if not (glob_pattern or filename):
            raise ValueError('No glob pattern of filename specified for output')

        return cls(
            stage=stage_name, 
            output_name=output_name, 
            typename=def_data['type'],
            filename=filename,
            glob_pattern=glob_pattern,
        )

    @classmethod
    def from_string(cls, candidate: str, def_data: dict):
        stage_name, output_name = candidate.split(cls._SPLITTING_CHAR)
        return cls.from_stage_name_def_data(stage_name, output_name, def_data)
        
@define
class Stage:
    name: str
    stage_def: StageDef
    dist: Dict[str, str]
    inputs: Dict[str, StageIO]
    outputs: Dict[str, Handle]
    after: List[str]

    def compute_hash(self) -> Optional[str]:
        hash = sha1()
        utils.add_obj_to_hash(self, hash)
        for input in self.inputs.values():
            if not input.fs_location.exists():
                # can't compute the hash if all the inputs aren't available
                return
            else:
                utils.add_file_to_hash(input.fs_location, hash)
        return hash.hexdigest()

    async def run(self, docker: aiodocker.Docker, inputs: Dict[str, Union[StageIO, List[StageIO]]]) -> utils.SubLog:
        stage_log = utils.SubLog(self.name)

        # build commands
        # reference for config structure: https://docs.docker.com/engine/api/v1.41/#tag/Container/operation/ContainerList
        docker_config = utils.merge_dict(
            {
                'Image': self.stage_def.image,
                'HostConfig': {
                    'Binds': [
                        f'{str(options.container_project_dir.value)}:/prj:rw',
                        f'{str(options.container_build_dir.value)}:/prj/build:rw',
                        f'{str(options.container_build_dir.value / self.name)}:/build:rw'
                    ]
                }
            },
            options.docker_options.value
        )

        # do input substitutions
        cmd = self.stage_def.command
        for input in inputs:
            var_name = f'${input}'
            if var_name in cmd:
                var_inputs = inputs[input]
                if not isinstance(var_inputs, list):
                    var_inputs = [var_inputs]

                # rehome them for use in the container
                rerooted_inputs = []
                prj = Path('/prj')
                for i in var_inputs:
                    path = str(i.fs_location).replace(str(options.project_dir.value), str(prj))
                    rerooted_inputs += [str(path)]
                var_value = ','.join(rerooted_inputs)

                cmd = cmd.replace(var_name, var_value)

        if cmd:
            docker_config['Cmd'] = shlex.split(cmd)

        log.debug(f'docker commands: {docker_config}')
        docker_cli_bind_mounts = [f'-v {b}' for b in docker_config.get('HostConfig', {}).get('Binds', [])]
        docker_cli_str = f'docker run --rm -it {" ".join(docker_cli_bind_mounts)} {docker_config.get("Image")} {" ".join(docker_config.get("Cmd", []))}'
        log.debug(f'docker cli equiv: "{docker_cli_str}"')
        container: aiodocker.docker.DockerContainer = await docker.containers.create_or_replace(
            config=docker_config,
            name=self.name,
        )
        try:
            await container.start()
            exit_data = await container.wait()
            stdout = await container.log(stdout=True) #, follow=True)
            stderr = await container.log(stderr=True) #, follow=True)
        finally:
            await container.stop(force=True)
            await container.delete(force=True)

        exit_status = exit_data['StatusCode']
        if exit_status:
            stage_log.error(f'Stage exited with code {exit_status}')
        else:
            stage_log.info(f'Stage complete with code {exit_status}')

        for stdout_line in stdout:
            stdout_line = str(stdout_line).strip(' \t\n\r')
            stage_log.info(stdout_line)

        for stderr_line in stderr:
            stderr_line = str(stderr_line).strip(' \t\n\r')
            if stderr_line.lower().startswith('warn'):
                stage_log.warning(stderr_line)
            else:
                stage_log.error(stderr_line)

        return exit_status, stage_log

    @classmethod
    def ios_from_stage_def(cls, log, logger, name: str, stage_def: StageDef, data: dict):
        # build io dicts
        inputs = {}
        for input_name, input_def_data in stage_def.inputs.items():
            if input_name in data:
                input_config_data = data[input_name]
            elif 'default' in input_def_data:
                input_config_data = input_def_data['default']
            else:
                log.error(f'No input data (default or explicit) for {input_name}')
                raise ValueError

            try:
                inputs[input_name] = StageIO.from_data(input_config_data, input_def_data)
            except (ValueError, KeyError) as ex:
                logger.error(f'{repr(ex)} raised while processing {input_name}')

        outputs = {}
        for output_name, output_def_data in stage_def.outputs.items():
            try:
                outputs[output_name] = Handle.from_stage_name_def_data(name, output_name, output_def_data)
            except (ValueError, KeyError) as ex:
                logger.error(f'{repr(ex)} raised while processing {output_name}')

        # bail out here, we can't return a valid object
        if not log:
            log.show()
            raise utils.AtopileError

        return inputs, outputs

    @classmethod
    def from_dict(cls, config_data: dict, name: str, data: dict):
        log = utils.SubLog(name, logging.DEBUG)
        logger = log.logger

        # common stuff
        dist = data.get('dist') or {}  # None -> empty dict as well
        if isinstance(dist, list):
            dist = {k: None for k in dist}
        elif isinstance(dist, str):
            dist = {dist: None}

        after = data.get('after')
        if not after:
            after = []
        elif isinstance(after, str):
            after = [after]

        # stage defining
        stage_def_path = data.get('path')
        image = data.get('image')

        # make sure image and path are mutally exclusive
        if not stage_def_path and not image:
            log.error('No image or path provided for this stage to run')
            raise utils.AtopileError
        if stage_def_path and image:
            log.error('Both an image and path provided for this stage')
            raise utils.AtopileError

        # complex stages
        if stage_def_path:
            stage_def_remote, stage_def_internal = resources.split_path(stage_def_path)
            stage_def_resources = resources.parse_resources(config_data.get('resources', []))
            resources_by_reference = {r.reference: r for r in stage_def_resources}
            if stage_def_remote not in resources_by_reference:
                log.error(f'No resource found for {stage_def_remote}')
                raise utils.AtopileError
            stage_def_resource = resources_by_reference[stage_def_remote]
            stage_def: StageDef = StageDef.from_file(options.project_dir.value / stage_def_resource.path / stage_def_internal)
            if not stage_def:
                logger.error(f'StageDef with path "{stage_def_path}" not found')
                log.show()
                raise ValueError

            inputs, outputs = cls.ios_from_stage_def(log, logger, name, stage_def, data)

        # "simple" stages
        if image:
            command = data.get('command')
            if not command:
                log.error(f'No command provided for {name}')
                raise utils.AtopileError

            stage_def = StageDef(
                None,
                image,
                command,
                inputs={},
                outputs={},
            )

            inputs = {}
            outputs = {}
        
        # build the final class
        return cls(
            name=name,
            stage_def=stage_def,
            dist=dist,
            inputs=inputs,
            outputs=outputs,
            after=after,
        )

    @classmethod
    def from_config_data(cls, config_data: dict, task_data: dict):
        stage_configs = {}
        for name, task_data in task_data.items():
            stage_configs[name] = cls.from_dict(config_data, name, task_data)
        return stage_configs
