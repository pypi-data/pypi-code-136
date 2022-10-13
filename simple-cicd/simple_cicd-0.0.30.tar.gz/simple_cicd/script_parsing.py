"""
SIMPLE CI: Dead simple CI/CD pipeline executor.
author: François Sevestre
email: francois.sevestre.35@gmail.com

This modules contains data parsing functions and pipeline execution.
"""

import time

from simple_cicd.functions import       \
        run_script,                     \
        end_of_pipeline,                \
        create_run_directory,           \
        command_execution_getoutput,    \
        log                             \

def run_pipeline(data, sudo_prefix, git_root_dir, runs_directory):
    """
    Parse pipeline data, determine the pipeline type (script, jobs, stages)
    and provides env data for execution.
    """
    ### Global scope ###
    run_directory       = create_run_directory(runs_directory)
    log("\n>>>>>>\nStarting the pipeline execution\n", "green")
    print(f"{run_directory} has been created.")
    parameters          = {                             \
            "variables":    get_variables(data, {}),    \
            "docker":       get_docker(data, {}),       \
            "artifacts":    get_artifacts(data),        \
            "sudo_prefix":  sudo_prefix,                \
            "git_root_dir": git_root_dir,               \
            "run_directory":  run_directory,            \
            "job_name":  "global",            \
            }

    time_summary = "\nExecution time:\n" +\
                     "---------------\n"
    global_start_time    = time.time()

    if stages:=get_stages(data):
        for stage in stages:
            stage_time, job_times = exec_stage(stage, data[stage], data, parameters)
            time_summary += f"{stage}: ({float(f'{stage_time:.2f}')}s)\n"
            time_summary += job_times
    else:
        if jobs:=get_jobs(data):                 # Check if user declared jobs in this stage
            for job in jobs:
                job_time = exec_job(job, data[job], parameters)
                time_summary += f"{job}: ({float(f'{job_time:.2f}')}s)\n"
        else:
            script_time = exec_script(get_script(data, "global"), parameters)
            time_summary += f"global: ({float(f'{script_time:.2f}')}s)\n"

    global_time = time.time() - global_start_time
    time_summary += f"=> Global time: ({float(f'{global_time:.2f}')}s)\n"
    log(time_summary, "blue")
    log("<<<<<\nEnd of the pipeline", "green")

    # Move logs to correct dir at the end of the pipeline
    log(f"Moving logs to {run_directory}.")
    if not command_execution_getoutput(f"mv simple.log {run_directory}")[0]:
        log("Can't relocate simple.log", "error")


def get_variables(data, upper_scope):
    """
    Get variables from data parsing in the right scope.
    """
    if 'variables' in data:                     # if user declared variables in global scope
        return upper_scope | data['variables']
    return upper_scope

def get_docker(data, upper_scope):
    """
    Get docker infos from data parsing in the right scope.
    """
    if 'inside_docker' in data:
        return data['inside_docker']
    return upper_scope

def get_artifacts(data):
    """
    Get artifacts from data parsing.
    """
    if 'artifacts' in data:
        return data['artifacts']
    return {}

def get_stages(data):
    """
    Get stages from data parsing.
    """
    if 'stages' in data:         # Check if user defined script in this job
        return data['stages']
    return False

def get_jobs(data, stage_name="No stages"):
    """
    Get jobs from data parsing.
    """
    if 'jobs' in data:         # Check if user defined script in this job
        return data['jobs']
    if stage_name != "No stages":
        return end_of_pipeline(f"No jobs found fo the stage \"{stage_name}\".")
    return False

def get_script(data, job_name):
    """
    Get commands from data parsing.
    """
    if 'script' in data:         # Check if user defined script in this job
        return data['script']
    return end_of_pipeline(f"No script found in \"{job_name}\".")

def exec_stage(stage_name, stage, data, parameters):
    """
    Format env data and runs script.
    """
    stage_start_time    = time.time()

    ### Stage scope ###
    parameters["variables"] = get_variables(stage, parameters["variables"])    # variables
    parameters["docker"]    = get_docker(stage, parameters["docker"])    # Inside docker
    log("   ###### Stage: \'" + stage_name + "\' ######\n", "green")
    job_time_summary = ""

    if jobs:=get_jobs(stage, stage_name):       # Check if user declared jobs in this stage
        for job in jobs:
            job_time = exec_job(job, data[job], parameters)
            job_time_summary += \
                f"|-->\t{job}: ({float(f'{job_time:.2f}')}s)\n"
    return (time.time() - stage_start_time, job_time_summary)

def exec_job(job_name, job, parameters):
    """
    Format env data and runs script.
    """
    job_start_time    = time.time()
    job_name        = ''.join(e for e in job_name if e.isalnum())
    log("     #### Job: \'" + job_name + "\' ####", "green")

    ### Job scope ###
    parameters["variables"] = get_variables(job, parameters["variables"])    # variables
    parameters["docker"]    = get_docker(job, parameters["docker"])    # Inside docker
    parameters["artifacts"] = get_artifacts(job)                # Artifacts
    parameters["job_name"] = job_name
    exec_script(get_script(job, job_name), parameters)
    return time.time() - job_start_time

def exec_script(script, parameters):
    """
    Format env data and runs script.
    """
    script_start_time    = time.time()
    script_parameters = {"script": script} | parameters
    run_script(script_parameters)
    return time.time() - script_start_time
