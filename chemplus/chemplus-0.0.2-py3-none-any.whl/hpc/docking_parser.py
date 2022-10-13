from chemplus.vina import docking
import argparse
import os

def create_parser():
    """ Function for creating command line arguments parser. """
    parser = argparse.ArgumentParser(description="DOCKING", add_help=True)
    
    parser.add_argument('--work_dir', required=True, help="Working directory")
    parser.add_argument('--receptor', required=True, help="Receptor file in PDBQT format which is in receptors/. (rec.pdbqt)")
    parser.add_argument('--config', required=True, help="Configuration file name which is in configs/. (conf.txt)")
    parser.add_argument('--sdf', required=True, help="SDF file with ligands")
    parser.add_argument('--cpu_count', required=True, type=int, help="CPU count")

    return parser

def main():

    parser = create_parser()
    try:
        args = parser.parse_args()
    except Exception as e:
        print(e)
    
    work_dir = os.path.expanduser(args.work_dir)
    receptor_file = os.path.expanduser(args.receptor)
    config_file = os.path.expanduser(args.config)
    sdf_file = os.path.expanduser(args.sdf)
    docking.sdf_dock_solved_path(work_dir, receptor_file, config_file, sdf_file, args.cpu_count)
    
if __name__ == '__main__':
    main()
    