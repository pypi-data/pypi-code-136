from mpi4py import MPI
import time
import glob
import subprocess
import os
import queue
import stat
import argparse
from datetime import datetime


def create_parser():
    """ Function for creating command line arguments parser. """
    parser = argparse.ArgumentParser(description="MPI program for docking", add_help=True)
    
    parser.add_argument('--vina', required=True, help="Path to vina executable file (/path/to/vina)")
    parser.add_argument('--receptor_file', required=True, help="Path to receptor file in PDBQT format (/path/to/rec.pdbqt)")
    parser.add_argument('--config_file', required=True, help="Path to configuration file (/path/to/conf.txt)")
    parser.add_argument('--ligands_dir', required=True, help="Path to the directory with ligands in PDBQT format (path/to/ligs/dir)")
    parser.add_argument('--out_dir', required=True, help="Path to the directory for docked ligands (path/to/out/dir)")
    parser.add_argument('--log_file', required=True, help="Path to log file. (/path/to/log.txt)")
    parser.add_argument('--rewrite', action='store_true', help="Whether to rewrite output files if docking was performed earlier.")

    return parser


def dock_lig(rank_p, lig_name, cmd_args, comm):
    """ Running docking function """
    start_time = time.time()
    result = subprocess.run(cmd_args, capture_output=True, shell=False)
    spent_time = time.time() - start_time

    if result.returncode:
        res = "Processor {0}\t: FAILED - {1}, ERROR - {2} {3}".format(rank_p, lig_name, result.returncode, result.stderr.decode("utf-8").strip())
        comm.send(res, dest=0, tag=3)  # tag = 3 - failed
    else:
        res = "Processor {0}\t: SUCCESS - {1}, spent time - {2}s".format(rank_p, lig_name, round(spent_time, 1))
        comm.send(res, dest=0, tag=2)  # tag = 2 - successed


def main():

    parser = create_parser()
    try:
        args = parser.parse_args()
    except Exception as e:
        print(e)
    
    vina = args.vina
    
    receptor_file_path, config_file_path, ligs_dir_path, out_dir_path, log_file_path = args.receptor_file, args.config_file, args.ligands_dir, args.out_dir, args.log_file

    comm = MPI.COMM_WORLD
    size_p = comm.Get_size()
    rank_p = comm.Get_rank()
    status = MPI.Status()
    kill_tag = 79
    ligs_queue = queue.Queue()

    if rank_p == 0:
        try:
            if not os.path.exists(os.path.dirname(log_file_path)):
                os.makedirs(os.path.dirname(log_file_path))
            log_file = open(log_file_path, 'a')
            log_file.write("\n---------------------------------------------DOCKING------------------------------------------------\n")
            log_file.write("Data: {0}\nVina: {1}\nReceptor: {2}\nConfig file: {3}\nLigands dir: {4}\nOut dir: {5}\nRewrite: {6}\n\n"
                           .format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), vina, receptor_file_path, config_file_path, 
                                   ligs_dir_path, out_dir_path, args.rewrite))
            log_file.close()
            
            if not os.path.exists(vina):
                log_file = open(log_file_path, 'a')
                log_file.write('Vina not found\n')
                log_file.close()
                raise Exception("Vina not found")
            
            if not os.path.exists(receptor_file_path):
                log_file = open(log_file_path, 'a')
                log_file.write('Receptor not found\n')
                log_file.close()
                raise Exception("Receptor not found")
                
            if not os.path.exists(config_file_path):
                log_file = open(log_file_path, 'a')
                log_file.write('Config file not found\n')
                log_file.close()
                raise Exception("Config file not found")
                
            if not os.path.exists(ligs_dir_path):
                log_file = open(log_file_path, 'a')
                log_file.write('Ligands dir not found\n')
                log_file.close()
                raise Exception("Ligands dir not found")

            if not os.path.exists(out_dir_path):
                os.makedirs(out_dir_path)

            for _ in glob.iglob(ligs_dir_path + '/*.pdbqt'):
                ligs_queue.put(_)

            ligs_num = ligs_queue.qsize()

            for rank in range(1, min(size_p, ligs_num + 1)):
                comm.send(ligs_queue.get(), dest=rank, tag=1) # tag = 1 - do your job

            while not ligs_queue.empty():
                result_message = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
                log_file = open(log_file_path, 'a')
                log_file.write(result_message + '\n')
                log_file.close()
                comm.send(ligs_queue.get(), dest=status.source, tag=1)

            for rank in range(1, min(size_p, ligs_num + 1)):  # min(wish_num_proc, size_p)
                result_message = comm.recv(source=MPI.ANY_SOURCE, tag=MPI.ANY_TAG, status=status)
                log_file = open(log_file_path, 'a')
                log_file.write(result_message + '\n')
                log_file.close()

            for rank in range(1, size_p):
                comm.send(-1, dest=rank, tag=kill_tag)  # tag = kill_tag - finish your job

            log_file = open(log_file_path, 'a')
            log_file.write('\n--------------------------------------------FINISHED------------------------------------------------\n')
            log_file.close()
            print("Docking finished successfully!")
        except:
            for rank in range(1, size_p):
                comm.send(-1, dest=rank, tag=kill_tag)
            raise
    else:
        while True:
            lig_path = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)

            if status.Get_tag() == kill_tag:
                break
            else:
                lig_name = os.path.basename(lig_path).split('.')[0]
                docked_lig_path = out_dir_path + '/' + lig_name + '.pdbqt'
                cmd_args = [vina, "--receptor", receptor_file_path, "--config", config_file_path, 
                            "--ligand", lig_path, "--out", docked_lig_path]
                if os.path.isfile(lig_path) and not args.rewrite:
                    comm.send("Processor {0}\t: ALREADY DONE - {1}".format(rank_p, lig_name), dest=0, tag=1)
                else:
                    dock_lig(rank_p, lig_name, cmd_args, comm)


if __name__ == '__main__':
    main()
