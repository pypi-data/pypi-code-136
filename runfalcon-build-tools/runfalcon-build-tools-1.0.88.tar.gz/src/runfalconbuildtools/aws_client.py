import json
from runfalconbuildtools.command_line_executor import CommandLineExecutor
from runfalconbuildtools.logger import Logger

class AWSCommandParams:
    zone:str
    account:int

    def __init__(self, account:int = None, zone:str = None):
        self.account = account
        self.zone = zone

class AWSClient:

    __logger__:Logger = Logger('AWSClient')

    def __init__(self, params:AWSCommandParams = AWSCommandParams()):
        self.params = params

    def get_ecr_image_data(self, repository:str, image_tag:str):
        executor:CommandLineExecutor = CommandLineExecutor()
        command:str = ''
        command += '#!/bin/sh\n'
        command += 'set -e\n'
        command += 'aws ecr list-images --repository-name {repository}\n'.format(repository = repository)

        try:
            executor.execute_script(command)
        except:
            return None

        json_data = json.loads(executor.stdout)
        for img in json_data["imageIds"]:
            if img["imageTag"] == image_tag:
                return img

        return None

    def delete_image_from_ecr(self, repository:str, image_digest:str):
        executor:CommandLineExecutor = CommandLineExecutor()
        command:str = ''
        command += '#!/bin/sh\n'
        command += 'set -e\n'
        command += 'aws ecr batch-delete-image --repository-name {repository} --image-ids imageDigest={image_digest}\n' \
                    .format(repository = repository, image_digest = image_digest)

        executor.execute_script(command)
        if executor.return_code != 0:
            raise Exception('\nCode: {code}.\noutput: {out}\nerror: {error}' \
                .format(code = executor.return_code, out = executor.stdout, error = executor.stderr))

        self.__logger__.info(executor.stdout)

    def push_image_to_ecr(self, source_image:str, repository:str, delete:bool = True):
        target_image:str = source_image.replace(':', '-')

        self.__logger__.info('Pushing {source} to {repository}/{target} ...' \
            .format( \
                source = source_image, \
                repository = repository, \
                target = target_image
            ))

        if delete:
            image_data = self.get_ecr_image_data(repository, target_image)
            if image_data != None:
                self.__logger__.info('Deleting image {repository}/{target}'.format(repository = repository, target = target_image))
                self.delete_image_from_ecr(repository, image_data["imageDigest"])

        executor:CommandLineExecutor = CommandLineExecutor()
        command:str = ''
        command += '#!/bin/sh\n'
        command += 'set -e\n'
        command += 'echo "Login in to docker ..."\n'
        command += 'aws ecr get-login-password --region {zone} | docker login --username AWS --password-stdin {account}.dkr.ecr.{zone}.amazonaws.com\n' \
                        .format(zone = self.params.zone, account = self.params.account)
        command += 'echo "Tagging image ..."\n'
        command += 'docker tag {source_image} {account}.dkr.ecr.{zone}.amazonaws.com/{repository}:{target_image}\n' \
                        .format(source_image = source_image, account = self.params.account, zone = self.params.zone, repository = repository, target_image = target_image)
        command += 'echo "Pushig image ..."\n'
        command += 'docker push {account}.dkr.ecr.{zone}.amazonaws.com/{repository}:{target_image}\n' \
                        .format(account = self.params.account, zone = self.params.zone, repository = repository, target_image = target_image)

        executor.execute_script(command)
        if executor.return_code != 0:
            raise Exception('\nCode: {code}.\noutput: {out}\nerror: {error}' \
                .format(code = executor.return_code, out = executor.stdout, error = executor.stderr))

        self.__logger__.info('Push to ecr result: {}'.format(str(executor.stdout)))

    def get_from_s3(self, artifact_s3_full_url:str, outdir:str = '.', recursive:bool = False):
        command:str = '#!/bin/sh\n'
        command += 'set -e\n'
        command += 'aws s3 cp {artifact_url} {outdir} {recursive}\n' \
                    .format( \
                        artifact_url = artifact_s3_full_url, \
                        outdir = outdir, \
                        recursive = ('--recursive' if recursive else ''))

        executor:CommandLineExecutor = CommandLineExecutor()
        executor.execute_script(command)
        if executor.return_code != 0:
            raise Exception('\nCode: {code}.\noutput: {out}\nerror: {error}' \
                .format(code = executor.return_code, out = executor.stdout, error = executor.stderr))
    
    def get_artifact_latest_version(self, domain:str, repository:str, format:str, namespace:str, package:str) -> str:

        command:str = '#!/bin/sh\n'
        command += 'set -e\n'
        command += 'aws codeartifact list-package-versions --domain {domain} --repository {repository} --format {format} --namespace {namespace} --package {package}\n' \
                    .format( \
                        domain = domain, \
                        repository = repository, \
                        format = format, \
                        namespace = namespace, \
                        package = package)

        executor:CommandLineExecutor = CommandLineExecutor()
        executor.execute_script(command)
        if executor.return_code != 0:
            raise Exception('\nCode: {code}.\noutput: {out}\nerror: {error}' \
                .format(code = executor.return_code, out = executor.stdout, error = executor.stderr))

        json_object:json = json.loads(executor.stdout)
        if json_object['versions'] == None or len(json_object['versions']) == 0:
            return None

        return json_object['versions'][0]['version']


    def get_from_artifacts(self, domain:str, repository:str, format:str, namespace:str, package:str, package_version:str, out_dir:str = '.', asset:str = None):

        local_asset:str = asset if asset != None else package + '-' + package_version + '.jar'
        out_file:str = out_dir + '/' + local_asset

        command:str = '#!/bin/sh\n'
        command += 'set -e\n'
        command += 'aws codeartifact get-package-version-asset --domain {domain} --repository {repository} --format {format} --namespace {namespace} --package {package} --package-version {package_version} --asset {asset} {out_file}\n' \
                    .format( \
                        domain = domain, \
                        repository = repository, \
                        format = format, \
                        namespace = namespace, \
                        package = package, \
                        package_version = package_version, \
                        asset = local_asset, \
                        out_file = out_file)

        executor:CommandLineExecutor = CommandLineExecutor()
        executor.execute_script(command)
        if executor.return_code != 0:
            raise Exception('\nCode: {code}.\noutput: {out}\nerror: {error}' \
                .format(code = executor.return_code, out = executor.stdout, error = executor.stderr))