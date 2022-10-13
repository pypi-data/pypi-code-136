import os
import sys
import glob
import subprocess
from chemplus import sdf
from chemplus.vina import pdbqt
from chemplus.vina import dockscore
from chemplus.vina import pdbqt_to_sdf

def run_docking(vina, receptor_file, config_file, ligands_dir, out_dir, log_file, cpu_count, rewrite=False):
    
    cmd_args = ["mpiexec", "-np", str(cpu_count), "python", "-m", "chemplus.vina.docking_mpi",
                "--vina", vina, "--receptor_file", receptor_file, "--config_file", config_file, 
                "--ligands_dir", ligands_dir, "--out_dir", out_dir, "--log_file", log_file]
    if rewrite:
        cmd_args += ["--rewrite"]
    
    result = subprocess.run(cmd_args, capture_output=True, shell=False)
    
    if result.returncode:
        raise Exception(result.stderr.decode("utf-8").strip())


def sdf_dock(work_dir, vina, nn2_script, rf4, rf4_model, mgl_python, receptor_file, config_file, sdf_file, cpu_count):
    if not os.path.exists(sdf_file):
        raise Exception("SDF file doesn't exists: " + sdf_file)
    
    if not os.path.exists(work_dir):
        os.makedirs(work_dir)

    sdf_name = os.path.basename(sdf_file).split(".")[0]

    print("Converting SDF to PDB files:")
    pdb_dir = work_dir + "/" + sdf_name + "_pdb"
    mol_num, converted_mol_num, bad_mol_list = sdf.sdf_to_pdb(sdf_file, pdb_dir)
    print("SDF contains %s molecules.\nConverted %s molecules." % (mol_num, converted_mol_num))
    if len(bad_mol_list):
        print("There are the following %s bad molecules:\n%s" % (len(bad_mol_list), "\n".join(bad_mol_list)))
    
    print("--------------------------------")
    print("Converting PDB's to PDBQT files:")
    pdbqt_dir = work_dir + "/" + sdf_name + "_pdbqt"
    pdb_num, converted_pdb_num, bad_pdb_list = pdbqt.pdb_dir_to_pdbqt(pdb_dir, pdbqt_dir, mgl_python, cpu_count=cpu_count)
    print("PDB directory contains %s molecules.\nConverted %s PDB's." % (pdb_num, converted_pdb_num))
    if len(bad_pdb_list):
          print("There are the following %s bad pdb's:\n%s" % (len(bad_pdb_list), "\n".join(bad_pdb_list)))
    
    print("--------------------------------")
    print("Checking PDBQT's rotatable bonds:")
    illegal_rb_pdbqt_list, missed_rb_pdbqt_list = pdbqt.check_pdbqt_dir_rot_bonds(pdbqt_dir, pdb_dir, fix_bad_pdbqt=True)
    if not len(illegal_rb_pdbqt_list) and not len(missed_rb_pdbqt_list):
        print("OK")
    if len(illegal_rb_pdbqt_list):
        print("Fixed %s PDBQT's with illegal rotatable bonds:\n%s" % (len(illegal_rb_pdbqt_list), "\n".join(illegal_rb_pdbqt_list)))
    if len(missed_rb_pdbqt_list):
        print("Found %s PDBQT's with missed rotatable bonds:\n%s" % (len(missed_rb_pdbqt_list), "\n".join(missed_rb_pdbqt_list)))

    print("--------------------------------")
    print("Searching for PDBQT's with more than 20 rotatable bonds:")
    overnrb_pdbqt_list = pdbqt.filter_pdbqt(pdbqt_dir, delete_overnrb_pdbqt=True)
    if len(overnrb_pdbqt_list):
        print("Deleted %s PDBQT's with more than 20 rotatable bonds:\n%s" 
              % (len(overnrb_pdbqt_list), "\n".join(overnrb_pdbqt_list)))
    else:
        print("All is well")

    print("--------------------------------")
    print("Docking...")
    out_dir = work_dir + "/" + sdf_name + "_docked"
    log_file = work_dir + "/" + sdf_name + "_log.txt"
    run_docking(vina=vina, receptor_file=receptor_file, config_file=config_file, ligands_dir=pdbqt_dir, out_dir=out_dir, 
                log_file=log_file, cpu_count=cpu_count, rewrite=True)
    print("Docking finished.")

    print("--------------------------------")
    print("Extracting top model from docked PDBQT's:")
    top_model_dir = work_dir + "/" + sdf_name + "_top_model"
    top_model_failures = pdbqt.get_top_model(out_dir, top_model_dir)
    if len(top_model_failures):
        print("Occurred %s failures when extracting top model from PDBQTs:\n%s" 
              % (len(top_model_failures), "\n".join(top_model_failures)))
    
    print("--------------------------------")
    print("Getting SF results for top model PDBQT's:")
    dockscore.run_dockscore(nn2_script=nn2_script, vina=vina, rf4=rf4, rf4_model=rf4_model, receptor_file=receptor_file, work_dir=work_dir, ligs_dir=top_model_dir, cpu_count=cpu_count, rewrite=True)

    print("--------------------------------")
    print("Writing top model PDBQT's to SDF:")
    sdf_docked_file = work_dir + "/" + sdf_name + "_docked.sdf.gz"
    pdbqt_to_sdf.pdbqt_to_sdf(top_model_dir, pdb_dir, sdf_docked_file)


sf_dir = os.path.dirname(os.path.realpath(__file__)) + "/sf"

def sdf_dock_solved_path(work_dir, receptor_file, config_file, sdf_file, cpu_count):
    if sys.platform.startswith('linux'):
        cmd = "whereis vina"
        result = subprocess.run(cmd, capture_output=True, shell=True)
        stdout = result.stdout.decode("utf-8").strip()
        if len(stdout.split(":")) < 2:
            vina = sf_dir + "/autodock_vina/vina"
        else:
            vina = stdout.split(":")[1].strip()
        rf4 = sf_dir + '/rfscore4/rf-score'
        mgl_search_location = os.path.expanduser('~') + "/bio/mgltools/bin/pythonsh"
    elif sys.platform.startswith('win32'):
        cmd = "where vina"
        result = subprocess.run(cmd, capture_output=True)
        stdout = result.stdout.decode("utf-8").strip()
        if not len(stdout):
            vina = sf_dir + "/autodock_vina/vina.exe"
        else:
            vina = stdout.split("\n")[0].strip()
        rf4 = sf_dir + '/rfscore4/rf-score.exe'
        mgl_search_location = "C:/Program Files*/MGLTools*/python.exe"
    else:
        raise Exception("Unknown OS")
    
    try:
        mgl_python = glob.glob(mgl_search_location)[0]
    except:
        raise Exception("MGLTools python not found")
    
    rf4_model = sf_dir + '/rfscore4/pdbbind-2014-refined.rf'
    nn2_script = sf_dir + '/nnscore2.0/NNScore2.py'
    
    # print(mgl_python)
    # print(rf4)
    # print(rf4_model)
    # print(vina)
    # print(nn2_script)
    sdf_dock(work_dir, vina, nn2_script, rf4, rf4_model, mgl_python, receptor_file, config_file, sdf_file, cpu_count)