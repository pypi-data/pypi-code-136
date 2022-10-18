import os
import sys

from kindplay.tools import run_command


def helm_prepare():
    '''
        Add one repository to the helm.
    '''
    helm_repo = "helm repo list"
    helm_repo_result = run_command(helm_repo)
    if helm_repo_result["return_code"] != 0:
        helm_add_repo = "helm repo add bitnami https://charts.bitnami.com/bitnami"
        run_command(helm_add_repo, None, None)


def get_workloads(playground_path):
    workloads = dict()
    charts_path = os.path.join(playground_path, "kubernetes")
    for namespace in os.listdir(charts_path):
        for basedir, dirs, files in os.walk(os.path.join(charts_path, namespace)):
            if f"values.yaml" in files:
                release_name = os.path.basename(basedir)
                workloads[f"{namespace}/{release_name}"]= {
                        "release_name": release_name,
                        "namespace": namespace,
                        "chart_dir": basedir,
                        "values_file": os.path.join(basedir, f"values.yaml")
                    }

    return workloads


def helm_deploy(chart_info):
    print( 
            f'\n## Setting up {chart_info["namespace"]}/{chart_info["release_name"]}',
            flush=True
        )

    print("- Helm dependency update", flush=True)
    dep_cmd = f'helm dependency update --skip-refresh {chart_info["chart_dir"]}'
    dep_status = run_command(dep_cmd, stdout=None, stderr=None)
    if dep_status["return_code"] != 0:
        print("Fail to setup helm dependencies.")
        sys.exit(1)

    print("- Helm upgrade", flush=True)
    helm_cmd = f'helm upgrade --install --wait --timeout 10m "{chart_info["release_name"]}" -n "{chart_info["namespace"]}" -f "{chart_info["values_file"]}" {chart_info["chart_dir"]}'
    run_command(helm_cmd, stdout=None, stderr=None)


def helm_deploy_all(playground_path, priority_charts=list()):
    workloads = get_workloads(playground_path)

    for chart_id in priority_charts:
        if workloads.get(chart_id):
            helm_deploy(workloads[chart_id])

    for chart_id in workloads.keys():
        if chart_id not in priority_charts:
            helm_deploy(workloads[chart_id])

