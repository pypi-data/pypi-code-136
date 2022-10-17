from subprocess import call
import time
import subprocess
from .benchmark_1gpu_fun import Benchmark_1gpu
from .benchmark_2gpu_fun import Benchmark_2gpu
from .benchmark_3gpu_fun import Benchmark_3gpu
from .benchmark_6gpu_fun import Benchmark_6gpu
from .benchmark_12gpu_fun import Benchmark_12gpu

from .time import time_count
from .analysis import analyze


def complete3():
    subprocess.check_call('module purge; module load anaconda', shell=True)
    
    Benchmark_1gpu()
    Benchmark_2gpu()
    Benchmark_3gpu()
    Benchmark_6gpu()
    Benchmark_12gpu()

    
#    subprocess.check_call('for x in ./*; do mkdir "${x}".d && mv "$x" "${x}".d; done;for f in *.d; do mv -n -- "$f" "${f%.d}"; done;for file in job_*; do mv "$file" "${file#job_}";done;for i in ./*; do cp ../*.tpr ${i}/; done;for d in ./*/ ; do (cd "$d" && sbatch job_script*); done',shell=True)
#    subprocess.check_call('squeue -n bingo > file.txt', shell=True)

    subprocess.check_call('for x in ./job_script*; do mkdir "${x}".d && mv "$x" "${x}".d; done;',shell=True)
    subprocess.check_call('for i in job_*; do cp *.tpr ${i}/; done', shell=True)
    subprocess.check_call('for file in job_*; do mv "$file" "${file#job_}";done', shell=True)
    subprocess.check_call('for d in ./*/ ; do (cd "$d" && sbatch job_script*); done',shell=True)
    subprocess.check_call('squeue -n bingo > file.txt', shell=True)
    
    time_count()
    analyze()
    
                          
    analyze()
    
