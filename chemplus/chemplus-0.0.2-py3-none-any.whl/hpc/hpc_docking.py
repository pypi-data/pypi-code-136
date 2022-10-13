import os
from chemplus.hpc import ucc
from datetime import datetime
import time

def server_dock(ucc_path, local_work_dir, local_receptor, local_config, local_sdf, server_work_dir, cpu_count, sync=True):
    ucc.create_dir(ucc_path, server_work_dir)
    ucc.put_file(ucc_path, local_sdf, server_work_dir)
    ucc.put_file(ucc_path, local_receptor, server_work_dir)
    ucc.put_file(ucc_path, local_config, server_work_dir)
    time.sleep(5)
    
    receptor_name = os.path.basename(local_receptor).split(".")[0]
    config_name = os.path.basename(local_config).split(".")[0]
    sdf_name = os.path.basename(local_sdf).split(".")[0]
    
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    job_file_name = receptor_name + "_" + config_name + "_" + sdf_name + "_" + current_time + "_docking.u"
    job_file_path = local_work_dir + os.sep + job_file_name
    
    nodes = cpu_count // 36 + (cpu_count % 36 > 0)
    cpus_per_node = cpu_count // nodes
    memory = 185 * (cpus_per_node / 36)
    
    work_dir = "~" + server_work_dir.split("Home")[1]
    server_receptor = "'" + work_dir + "/" + os.path.basename(local_receptor) + "'"
    server_config = "'" + work_dir + "/" + os.path.basename(local_config) + "'"
    server_sdf = "'" + work_dir + "/" + os.path.basename(local_sdf) + "'"
    
    work_dir = "'" + work_dir + "'"
    args = ["--work_dir", work_dir, "--receptor", server_receptor, "--config", server_config, 
            "--sdf", server_sdf, "--cpu_count", cpu_count]
    ucc.create_job_file(job_file_path, job_type="docking", arguments_list=args, memory=memory, 
                        nodes=nodes, cpus_per_node=cpus_per_node, run_time=800)
    
    if sync:
        ucc.run_sync(ucc_path, job_file_path, local_work_dir)
    else:
        return ucc.run_async(ucc_path, job_file_path, local_work_dir)

    if sync:
        server_result_sdf = server_work_dir + "/" + os.path.basename(local_sdf).split(".")[0] + "_docked.sdf.gz"
        server_dockscore_file = server_work_dir + "/dockscore.csv"
        ucc.get_file(ucc_path, server_result_sdf, local_work_dir)
        ucc.get_file(ucc_path, server_dockscore_file, local_work_dir)
        
def get_docking_results(ucc_path, local_work_dir, local_receptor, local_config, local_sdf, server_work_dir):
        server_result_sdf = server_work_dir + "/" + os.path.basename(local_sdf).split(".")[0] + "_docked.sdf"
        server_dockscore_file = server_work_dir + "/dockscore.csv"
        ucc.get_file(ucc_path, server_result_sdf, local_work_dir)
        ucc.get_file(ucc_path, server_dockscore_file, local_work_dir)