import argparse
from genericpath import isdir
from multiprocessing import context
import os
import sys
import yaml

from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from kindplay.kind import start_kind, stop_kind
from kindplay.tools import run_command
from kindplay.helm import helm_deploy_all, helm_prepare


def requirements_check():
    exit_code = 0
    
    kind_status = run_command("kind --version")
    if kind_status["return_code"] != 0:
        print("kind not found, please install kind.")
        exit_code = 1

    helm_status = run_command("helm version")
    if helm_status["return_code"] != 0:
        print("helm not found, please install helm.")
        exit_code = 1

    docker_status = run_command("docker version")
    if docker_status["return_code"] != 0:
        print("docker not found, please install docker.")
        exit_code = 1

    if exit_code:
        sys.exit(exit_code)


def create_namespaces(base_path: str, k8s_core: client.CoreV1Api):
    kubernetes_folder = os.path.join(base_path,"kubernetes")

    for filename in os.listdir(kubernetes_folder):
        if os.path.isdir(os.path.join(kubernetes_folder,filename)):
            try:
                k8s_core.read_namespace(filename)
            except ApiException as error:
                if error.status == 404:
                    namespace_object = client.V1Namespace(
                            metadata=client.V1ObjectMeta(name=filename)
                        )
                    k8s_core.create_namespace(namespace_object)
                    continue
                raise
            except:
                raise


def playground_start(base_path):
    kind_config_file = os.path.join(base_path,"kind.yaml")
    playground_config_file = os.path.join(base_path,"playground.yaml")

    with open(kind_config_file) as fp:
        kind_config = yaml.safe_load(fp)

    with open(playground_config_file) as fp:
        playground_config = yaml.safe_load(fp)

    start_kind(base_path, kind_config, playground_config)

    config.load_kube_config(context=f"kind-{kind_config['name']}")

    k8s_core = client.CoreV1Api()

    create_namespaces(base_path, k8s_core)

    helm_prepare()

    helm_deploy_all(base_path, playground_config["kubernetes"]["priorityCharts"])


def playground_stop(base_path):
    kind_config_file = os.path.join(base_path,"kind.yaml")
    playground_config_file = os.path.join(base_path,"playground.yaml")

    with open(kind_config_file) as fp:
        kind_config = yaml.safe_load(fp)

    with open(playground_config_file) as fp:
        playground_config = yaml.safe_load(fp)

    stop_kind(base_path, kind_config, playground_config)


def main(): 
    requirements_check()

    parser = argparse.ArgumentParser(description='Kind Playground')
    subparsers = parser.add_subparsers(dest='subparser', metavar="command")

    parser_start = subparsers.add_parser('start')
    parser_start.add_argument('path', type=str, help='Playground path')

    parser_stop = subparsers.add_parser('stop')
    parser_stop.add_argument('path', type=str, help='Playground path')

    subparsers.required = True

    args = parser.parse_args()

    base_path = os.path.realpath(args.path)

    if args.subparser == "start":
        playground_start(base_path)

    if args.subparser == "stop":
        playground_stop(base_path)


if __name__ == "__main__":
    main()
