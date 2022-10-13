import json
import os
import subprocess

jobs_dir = os.path.dirname(os.path.realpath(__file__)) + os.sep + "files"

job_types_dict = {"docking" : "docking.u"}

def create_job_file(job_file_path, job_type="docking", arguments_list=[], memory=1, nodes=1, cpus_per_node=1, run_time=1):
    if job_type not in job_types_dict:
        raise Exception("Non-valid job type")
    
    with open(jobs_dir + "/" + job_types_dict[job_type], "r") as jsonFile:
        data = json.load(jsonFile)
    
    if not 1 <= memory <= 185:
        raise Exception("Bad Memory value")
    data["Resources"]["Memory"] = int(memory * 1024**3)
    
    if not isinstance(nodes, int) or not 1 <= nodes <= 16:
        raise Exception("Bad Nodes number")
    data["Resources"]["Nodes"] = nodes
    
    if not isinstance(cpus_per_node, int) or not 1 <= cpus_per_node <= 36:
        raise Exception("Bad CPUsPerNode number")
    data["Resources"]["CPUsPerNode"] = cpus_per_node
    
    if not 1 <= run_time <= 800:
        raise Exception("Bad Runtime value")   
    data["Resources"]["Runtime"] = int(run_time * 3600)
    
    if not isinstance(arguments_list, list) and not isinstance(arguments_list, tuple):
        raise Exception("Bad Arguments list")
    
    data["Arguments"] = data["Arguments"] + list(arguments_list)
    
    with open(job_file_path, "w") as jsonFile:
        json.dump(data, jsonFile, indent="  ")
        
def get_file(ucc_path, server_file_path, local_destination_dir=None):
    
    if local_destination_dir:
        destination_file_path = local_destination_dir + "/" + os.path.basename(server_file_path)
    else:
        destination_file_path = os.path.basename(server_file_path)
    
    cmd_args = [ucc_path, "get-file", "-s", server_file_path, "-t", destination_file_path]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip())

def put_file(ucc_path, local_file_path, server_destination_dir):
    
    destination_file_path = server_destination_dir + "/" + os.path.basename(local_file_path)
    
    cmd_args = [ucc_path, "put-file", "-s", local_file_path, "-t", destination_file_path]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip())

def create_dir(ucc_path, server_dir):
    
    cmd_args = [ucc_path, "mkdir", server_dir]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip()) 

def run_sync(ucc_path, job_file, output_dir):
    
    cmd_args = [ucc_path, "run", "-s", "SKIF_GEO", "-o", output_dir, job_file]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip()) 

def run_async(ucc_path, job_file, output_dir):
    
    cmd_args = [ucc_path, "run", "-s", "SKIF_GEO", "-o", output_dir, "-a", job_file]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip())
    else:
        return result.stdout.decode("utf-8").strip().split("\n")[0].strip()
    
def get_job_status(ucc_path, job_id_file):
    
    cmd_args = [ucc_path, "get-status", job_id_file]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip())
    else:
        return result.stdout.decode("utf-8").strip()

def get_job_out(ucc_path, job_id_file):
    
    cmd_args = [ucc_path, "get-output", job_id_file]
    result = subprocess.run(cmd_args, capture_output=True)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip())