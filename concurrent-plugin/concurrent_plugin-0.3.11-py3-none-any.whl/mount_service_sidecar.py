

## stdout_redirect is redirect stdout/err to a debug file
from concurrent_plugin.infinfs import stdout_redirect

import socket
import time
import os
from concurrent_plugin.infinfs import infinmount
import json
from mlflow.tracking import MlflowClient
import psutil


def parse_mount_request(data):
    req = json.loads(data.decode('utf-8'))
    process_id = req['process_id']
    if req['use_cache'].lower() == 'false':
        use_cache = False
    else:
        use_cache = True
    if req['shadow_path'].lower() == 'none':
        shadow_path = None
    else:
        shadow_path = req['shadow_path']
    return process_id, req['mount_path'], req['mount_spec'], shadow_path, use_cache


def check_pids():
    task_processes = []
    for proc in psutil.process_iter():
        pid = proc.pid
        with open('/proc/' + str(pid) + '/cmdline') as inf:
            cmdline = inf.read()
            if 'mount_service' in cmdline or 'mount_main' in cmdline:
                continue
            if 'python' in cmdline:
                task_processes.append(pid)

    if not task_processes:
        return True

    all_pid_done = True
    for pid in pid_list:
        try:
            os.kill(pid, 0)
        except OSError:
            all_pid_done = False
        else:
            return True


def print_info(*args):
    print(*args)
    print(*args, file=stdout_redirect.legacy_stdout)
    stdout_redirect.legacy_stdout.flush()


if __name__ == '__main__':
    print_info("Starting..")
    HOST = "127.0.0.1"
    PORT = 7963
    last_upload_time = time.time()

    process_id_set = set()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        s.bind((HOST, PORT))
        print('Listening on port {}:{}'.format(HOST, PORT))
        s.listen()
        while True:
            print_info('Waiting for request..')
            try:
                conn, addr = s.accept()

            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024*16)
                if not data:
                    time.sleep(1)
                    continue
                try:
                    mount_path, mount_spec, shadow_path, use_cache = parse_mount_request(data)
                    print_info("mount request {}, {}, {}, {}".format(
                        mount_path, mount_spec, shadow_path, use_cache))
                    infinmount.perform_mount(mount_path, mount_spec, shadow_path=shadow_path, use_cache=use_cache)
                    response = "success".encode('utf-8')
                    print_info("mount successful")
                except Exception as ex:
                    print_info('Exception in mounting: '+str(ex))
                    response = str(ex).encode('utf-8')
                conn.send(response)
            curr_time = time.time()
            if curr_time - last_upload_time > 30:
                client = MlflowClient()
                client.log_artifact(os.environ['MLFLOW_RUN_ID'], stdout_redirect.fuse_debug_file,
                                    artifact_path='.concurrent/logs')
                last_upload_time = curr_time
            all_processes_done = True
            for pid in process_id_set:
                if check_pid(pid):
                    all_processes_done = False
                    break
            if all_processes_done:
                print_info('Done serving requests for processes: ', process_id_set)
                break

    ##Upload logs one last time
    client = MlflowClient()
    client.log_artifact(os.environ['MLFLOW_RUN_ID'], stdout_redirect.fuse_debug_file,
                        artifact_path='.concurrent/logs')
    #Dump logs for the pod
    with open(stdout_redirect.fuse_debug_file) as logfd:
        print(logfd, file=stdout_redirect.legacy_stdout)
    exit(0)








