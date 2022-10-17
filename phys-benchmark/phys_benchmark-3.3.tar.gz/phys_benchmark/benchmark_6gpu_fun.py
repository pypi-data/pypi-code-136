#!/usr/bin/env python

import math
import numpy as np
import itertools



###for 3 GPU and 2 node

import itertools
import pandas as pd

def Benchmark_6gpu():
    list_one = list((range(3, 56)))
    list_two =list((range(1, 56)))
    result = itertools.product(list_one, list_two)
    df=pd.DataFrame(result, columns=['ntasks', 'cpu'])
    df['cores'] = df['ntasks'] * df['cpu']
    df = df.drop(df[df.cores >= 56].index)
    df = df.drop(df[df.cpu == 1].index)

    x=len(df.index)
    run = range(0,int(x))
    df['run'] = run


    for index, row in df.iterrows():
        with open("job_script_6_" + (str(row["run"])), "w") as f:
            f.write(
                    "#!/bin/bash -l" +  "\n"
                    "# Standard output and error:" +  "\n"
                    "#SBATCH -o ./bench.out.%j"+  "\n"
                    "#SBATCH -e ./bench.err.%j"+  "\n"
                    "# Initial working directory:"+  "\n"
                    "#SBATCH -D ./"+  "\n"
                    "#"+  "\n"
                    "#SBATCH -J bingo"+  "\n"
                    "#"+  "\n"
                    "# Queue:" +  "\n"
                    "#SBATCH --partition=p.phys" + "\n"
                    "#SBATCH --gres=gpu:3"+  "\n"
                    "# Request 10 nodes"+  "\n"
                    "#SBATCH --nodes=2"+  "\n"
                    "# Set the number of tasks per node (=MPI ranks)"+  "\n"
                    "#SBATCH --ntasks-per-node=" + str(row["ntasks"]) + "\n"
                    "# Set the number of threads per rank (=OpenMP threads)"+  "\n"
                    "#SBATCH --cpus-per-task="+ str(row["cpu"]) + "\n"
                    "# Explicitly disable hyperthreading"+  "\n"
                    "#SBATCH --ntasks-per-core=1" + "\n"
                    "#SBATCH --mem=186000" + "\n"
                    "#SBATCH --time=01:00:00" + "\n"
                    "" + "\n"
                    "module purge" + "\n"
                    "module load intel/19.1.3"+  "\n"
                    "module load impi/2019.9"+  "\n"
                    "module load cuda/11.4"+  "\n"
                    "module load anaconda" + "\n"
                    "module load gcc/10" + "\n"
                    "module load gromacs/2021.5"+  "\n"
                    ""+  "\n"
                    "export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK"+  "\n"
                    "export OMP_PLACES=cores"+  "\n"
                    ""+  "\n"

                    "srun gmx_mpi mdrun -v -s *.tpr -ntomp $OMP_NUM_THREADS -npme 1 -pme gpu -pmefft gpu -bonded gpu -nb gpu -maxh 0.25"+  "\n"
        )
        f.close()