#===============================================================================
# splitbam.py
#===============================================================================

"""Split a BAM file into two subsamples"""

import os.path
import pysam
import subprocess
import tempfile

from argparse import ArgumentParser


# Functions ====================================================================

def parse_arguments():
    parser = ArgumentParser(description='Split a BAM file into two subsamples')
    parser.add_argument(
        'input',
        metavar='<path/to/input.bam>',
        help='path to input BAM file'
    )
    parser.add_argument(
        'out0',
        metavar='<path/to/output0.bam>',
        help='path to first output BAM file'
    )
    parser.add_argument(
        'out1',
        metavar='<path/to/output1.bam>',
        help='path to second output BAM file'
    )
    parser.add_argument(
        '--processes',
        metavar='<int>',
        type=int,
        default=1,
        help='number of processes'
    )
    parser.add_argument(
        '--memory',
        metavar='<float>',
        type=float,
        default=768/1024,
        help='memory limit in GB'
    )
    parser.add_argument(
        '--tmp-dir',
        metavar='<path/to/tmp/dir>',
        help='directory for temporary files'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    with tempfile.TemporaryDirectory(dir=args.tmp_dir) as temp_dir:
        temp_in = os.path.join(temp_dir, 'namesort_in.bam')
        temp_out0 = os.path.join(temp_dir, 'namesort_out1.sam')
        temp_out1 = os.path.join(temp_dir, 'namesort_out2.sam')
        pysam.sort(
            '-@', str(args.processes - 1),
            '-m', f'{int(args.memory / args.processes * 1024)}M',
            '-n',
            '-T', args.tmp_dir or tempfile.gettempdir(),
            '-o', temp_in,
            args.input
        )
        for out in temp_out0, temp_out1:
            pysam.view(
                '-@', str(args.processes - 1),
                '-H',
                '-o', out,
                temp_in,
                catch_stdout=False
            )
        with open(temp_in, 'r') as f:
            with subprocess.Popen(
                ('samtools', 'view'), stdin=f, stdout=subprocess.PIPE
            ) as view:
                subprocess.run(
                    ('awk', f'{{if(NR%4<2) {{print >> "{temp_out0}"}} else {{print >> "{temp_out1}"}}}}'),
                    stdin=view.stdout
                )
        for temp_out, out in (temp_out0, args.out0), (temp_out1, args.out1):
            pysam.sort(
                '-@', str(args.processes - 1),
                '-m', f'{int(args.memory / args.processes * 1024)}M',
                '-T', args.tmp_dir or tempfile.gettempdir(),
                '-o', out,
                temp_out
            )
            pysam.index(out)
