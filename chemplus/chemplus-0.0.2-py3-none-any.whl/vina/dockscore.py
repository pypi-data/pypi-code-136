import os
import sys
import glob
import subprocess
import math
import pandas as pd
from joblib import Parallel, delayed
from pathlib import Path

#J/(K*mol) / kcal/J -> kcal/(K*mol)
kcal_to_jole = 4184
# Universal gas constant
R = 8.31432
# Temperature, K
T = 298.5

def collect_vina_results(ligs_dir):
    if not os.path.exists(ligs_dir):
        raise Exception("Ligands dir doesn't exists")
    
    results_list = []
    for lig_file in glob.glob(ligs_dir + os.sep + '*.pdbqt'):
        with open(lig_file, 'r') as f:
            for line in f.readlines():
                if 'REMARK VINA RESULT' in line:
                    energy = float(line.split('     ')[1])
                    break
            ligand_score_info = {
                'Name': os.path.basename(lig_file).split(".")[0],
                'E_vina, kcal/mol': energy,
                'pKd_vina': - energy * kcal_to_jole / R / T / math.log(10)
            }
            results_list.append(ligand_score_info)
    
    return pd.DataFrame(results_list)


def execute_nn2(ligand_file, receptor_file, vina, nn2_script, result_file):
    """
    Run NNScore2.py
    
    Arguments:
    ligand_file -- filepath of the .pdbqt file of the ligand to be scored by RF-score4
    receptor_file -- filepath to the .pdbqt file of the receptor 
    vina_exe -- path to vina
    nn2_script -- path to NNScore2.py
    result_file -- file for NNScore2.py results

    """
    with open(result_file, 'w') as fout:
        subprocess.run([sys.executable, nn2_script, "-receptor", receptor_file, "-ligand", ligand_file, 
                        "-vina_executable", vina], stdout=fout)

def execute_nn2_dir(nn2_script, vina, receptor_file, ligs_dir, results_dir, cpu_count, rewrite=True):
    if not os.path.exists(nn2_script):
        raise Exception("Path to NNScore2.py doesn't exists")
    
    if not os.path.exists(vina):
        raise Exception("Path to Vina doesn't exists")
    
    if not os.path.exists(receptor_file):
        raise Exception("Path to receptor doesn't exists")
    
    if not os.path.exists(ligs_dir):
        raise Exception("Path to ligands directory doesn't exists")
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    ligand_files = glob.glob(ligs_dir + os.sep + '*.pdbqt')
    ligand_files_to_nn2 = {}
    
    if rewrite:
        for lig_file in ligand_files:
            lig_nn2_result_path = results_dir + os.sep + os.path.basename(lig_file).split(".")[0] + '.txt'
            ligand_files_to_nn2[lig_file] = lig_nn2_result_path
    else:
        results_dir_files = glob.glob(results_dir + os.sep + '*.txt')
        for lig_file in ligand_files:
            lig_nn2_result_path = results_dir + os.sep + os.path.basename(lig_file).split(".")[0] + '.txt'
            if lig_nn2_result_path not in results_dir_files or Path(lig_nn2_result_path).stat().st_size == 0:
                ligand_files_to_nn2[lig_file] = lig_nn2_result_path

    print('Detected {0} unprocessed by NNScore2 of {1} given ligands'.format(len(ligand_files_to_nn2), len(ligand_files)))

    cpu_count = min(os.cpu_count(), cpu_count)
    nn2_results = Parallel(n_jobs=cpu_count)(delayed(execute_nn2)(lig_file, receptor_file, vina, nn2_script, ligand_files_to_nn2[lig_file]) for lig_file in ligand_files_to_nn2)
                                          
def collect_nn2_results(results_dir):
    if not os.path.exists(results_dir):
        raise Exception("NNScore2 results dir doesn't exists")

    results_list = []
    
    for result_file in glob.glob(results_dir + os.sep + '*.txt'):
        with open(result_file, 'r') as f:
            while True:
                line = f.readline()
                if len(line) == 0: 
                    break
                if "AVERAGE SCORE OF ALL 20 NETWORKS, BY POSE" in line:
                    break
            f.readline()
            f.readline()
            line = f.readline()
            splitted_line = line.split('|')
            if len(splitted_line) < 3:
                continue
            pKd = float(splitted_line[2])
            ligand_score_info = {
                'Name': os.path.basename(result_file).split(".")[0],
                'pKd_nn2': pKd
            }
            results_list.append(ligand_score_info)
    
    return pd.DataFrame(results_list)
    

def execute_rf4(ligand_file, receptor_file, rf4, rf4_model, result_file):
    """
    Run rf-score4
    
    Arguments:
    ligand_file -- filepath of the .pdbqt file of the ligand to be scored by RF-score4
    receptor_file -- filepath to the .pdbqt file of the receptor 
    rf4_exe -- path to RF-score4 executable
    rf4_model -- path to RF-score4 trained random forest model file
    result_file -- file for RF-score4 results

    """
    with open(result_file, 'w') as fout:
        subprocess.run([rf4, rf4_model, receptor_file, ligand_file], stdout=fout)

def execute_rf4_dir(rf4, rf4_model, receptor_file, ligs_dir, results_dir, cpu_count, rewrite=True): 
    if not os.path.exists(rf4):
        raise Exception("Path to RF4 doesn't exists")
    
    if not os.path.exists(rf4_model):
        raise Exception("Path to RF4 model doesn't exists")
    
    if not os.path.exists(receptor_file):
        raise Exception("Path to receptor doesn't exists")
    
    if not os.path.exists(ligs_dir):
        raise Exception("Path to ligands directory doesn't exists")
    
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    ligand_files = glob.glob(ligs_dir + os.sep + '*.pdbqt')
    ligand_files_to_rf4 = {}
    
    if rewrite:
        for lig_file in ligand_files:
            lig_rf4_result_path = results_dir + os.sep + os.path.basename(lig_file).split(".")[0] + '.txt'
            ligand_files_to_rf4[lig_file] = lig_rf4_result_path
    else:
        results_dir_files = glob.glob(results_dir + os.sep + '*.txt')
        for lig_file in ligand_files:
            lig_rf4_result_path = results_dir + os.sep + os.path.basename(lig_file).split(".")[0] + '.txt'
            if lig_rf4_result_path not in results_dir_files or Path(lig_rf4_result_path).stat().st_size == 0:
                ligand_files_to_rf4[lig_file] = lig_rf4_result_path

    print('Detected {0} unprocessed by RF-Score4 of {1} given ligands'.format(len(ligand_files_to_rf4), len(ligand_files)))
    
    cpu_count = min(os.cpu_count(), cpu_count)
    rf4_results = Parallel(n_jobs=cpu_count)(delayed(execute_rf4)(ligand_file, receptor_file, rf4, rf4_model, ligand_files_to_rf4[ligand_file]) for ligand_file in ligand_files_to_rf4)

def collect_rf4_results(results_dir):
    if not os.path.exists(results_dir):
        raise Exception("RF-Score4 results dir doesn't exists")

    results_list = []
    
    for result_file in glob.glob(results_dir + os.sep + '*.txt'):
        with open(result_file,'r') as f:
            line = f.readline()
            pKd = float(line)
            ligand_score_info = {
                'Name': os.path.basename(result_file).split(".")[0],
                'pKd_rf4': pKd
            }                
            results_list.append(ligand_score_info)
    
    return pd.DataFrame(results_list)



def run_dockscore(nn2_script, vina, rf4, rf4_model, receptor_file, work_dir, ligs_dir, cpu_count=1, rewrite=True):
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)
    
    df_vina = collect_vina_results(ligs_dir)
    
    nn2_results_dir = work_dir + os.sep + "nn2_results"
    execute_nn2_dir(nn2_script, vina, receptor_file, ligs_dir, nn2_results_dir, cpu_count, rewrite)
    df_nn2 = collect_nn2_results(nn2_results_dir)
    if not df_nn2.shape[0]:
        raise Exception("Missing NNScore2 results")
    
    rf4_results_dir = work_dir + os.sep + "rf4_results"
    execute_rf4_dir(rf4, rf4_model, receptor_file, ligs_dir, rf4_results_dir, cpu_count, rewrite)
    df_rf4 = collect_rf4_results(rf4_results_dir)
    if not df_rf4.shape[0]:
        raise Exception("Missing RF-Score4 results")
    
    df_vina = df_vina.merge(df_nn2, how='left', on=['Name'])
    df_vina = df_vina.merge(df_rf4, how='left', on=['Name'])


    df_vina = df_vina.sort_values(by=['E_vina, kcal/mol'], ascending=True)
    
    results_filename = work_dir + os.sep + "dockscore.csv"
    df_vina.to_csv(results_filename, index=False)
