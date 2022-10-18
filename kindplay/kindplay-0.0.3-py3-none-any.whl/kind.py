import stat
import tempfile
import sys
import os

from kindplay.tools import run_command


def run_scripts(script_list, base_path):
    script_header = "#!/bin/bash\n"
    env = os.environ
    env["PLAYGROUND_PATH"] = base_path

    for script in script_list:
        with tempfile.NamedTemporaryFile() as fp:
            if script.get("description"):
                print(f"- {script.get('description')}")
            fp.file.write(script_header.encode())
            fp.file.write(script["run"].encode())
            fp.file.close()
            script_file = fp.name
            os.chmod(script_file, stat.S_IRWXU)
            run_command(script_file, None, None)


def start_kind(base_path, kind_config, playground_config):
    kind_config_file = os.path.join(base_path,"kind.yaml")

    print("### Preparing local Kind")
    kind_check = f'kind get kubeconfig --name {kind_config["name"]}'
    if run_command(kind_check)["return_code"] != 0:
        kind_start = f"kind create cluster --config {kind_config_file}"
        if run_command(kind_start, None, None)["return_code"] != 0:
            print("Fail to start kind cluster")
            sys.exit(1)
    else:
        print("- Kind cluster already exist, skipping creation")

    print("\n### Running Post Start Scripts")
    run_scripts(playground_config["postStart"], base_path)


def stop_kind(base_path, kind_config, playground_config):
    kind_stop = f"kind delete cluster --name {kind_config['name']}"
    run_command(kind_stop, None, None)

    print("\n### Running Post Stop Scripts")
    run_scripts(playground_config["postStop"], base_path)
