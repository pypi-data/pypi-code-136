import getpass
import os
import re
import shlex
import subprocess
import sys

from .util import ArgumentParser, abort, ask_continue, find_available_path, log, log_key_value, validate_setting

PIPELINES_DIR = os.path.join(os.path.dirname(__file__), "..", "pipelines")


def get_pipeline(name):
    path = os.path.join(PIPELINES_DIR, f"{name}.sh")
    if not os.path.isfile(path):
        raise ValueError(f"unknown pipeline: {name}")
    with open(path, "r") as file:
        script = [line.rstrip() for line in file]
    info = {}
    variables = {}
    for index, line in enumerate(script):
        if not index or not line:
            continue
        if line.startswith("# ---"):
            break
        if line.startswith("# >"):
            key, value = re.match(r"^# >\s*(\w+)\s*=\s*(.*)$", line).groups()
            info[key] = [index, value]
            continue
        key, value = re.match(r'^(\w+)="{([^}]*)}"$', line).groups()
        value = re.split(r'\s+', value.strip())
        variables[key] = [index, value]
    extensions = {
        "paired_fastq": [".r1.fastq.gz", ".r2.fastq.gz"],
        "single_fastq": [".fastq.gz"],
        "indexed_bam": [".bam", ".bam.bai"],
        "bigwig": [".bigwig"]}[info["input_type"][1]]
    pipeline = {
        "script": script,
        "info": info,
        "variables": variables,
        "extensions": extensions}
    return pipeline


def parse_settings(settings, pipeline):
    parsed_settings = {}
    required_header_settings = [
        ("ACCOUNT", ["any"]),
        ("TIME", ["duration", ">", "0"]),
        ("CPU_CORES", ["integer", ">", "0"]),
        ("MEMORY_PER_CORE", ["regex", r"[0-9]+[KMGT]?"])]
    for key, validation in required_header_settings:
        value = settings.get(key.lower(), None)
        key = f"{key} (SCRIPT HEADER)"
        value, warning = validate_setting(key, value, validation)
        parsed_settings[key] = {"value": value, "warning": warning}
    for key, (_, validation) in pipeline["variables"].items():
        if key.lower() == "base_path":
            continue
        _, validation = pipeline["variables"][key]
        value = settings.get(key.lower(), None)
        value, warning = validate_setting(key, value, validation)
        parsed_settings[key] = {"value": value, "warning": warning}
    return parsed_settings


def process_inputs(paths, extensions):
    inputs = {}
    for path in paths:
        if os.path.isdir(path):
            for name in os.listdir(path):
                for extension in extensions:
                    if not name.endswith(extension):
                        continue
                    file_path = os.path.join(path, name)[:-len(extension)]
                    inputs[os.path.realpath(file_path)] = file_path
                    break
            continue
        for extension in extensions:
            if path.endswith(extension):
                path = path[:-len(extension)]
                break
        inputs[os.path.realpath(path)] = path
    inputs = [{"in_base_path": base_path} for base_path in inputs.values()]
    for input in inputs:
        input['base_name'] = os.path.basename(input['in_base_path'])
        input['in_paths'] = []
        for extension in extensions:
            in_path = f'{input["in_base_path"]}{extension}'
            if not os.path.exists(in_path):
                raise FileNotFoundError(f'input file {in_path} missing')
            input['in_paths'].append(in_path)
    return inputs

        
def set_out_paths(input, out_dir, no_sub_dir):
    if out_dir is None:
        out_dir = os.path.dirname(input['in_base_path'])
    out_dir = os.path.realpath(out_dir)
    if no_sub_dir:
        input['out_dir'] = out_dir
    else:
        input['out_dir'] = os.path.join(out_dir, input['base_name'])
    input['base_path'] = os.path.join(input['out_dir'], input['base_name'])
    input['out_paths'] = []
    for in_path in input['in_paths']:
        out_path = os.path.join(input['out_dir'], os.path.basename(in_path))
        input['out_paths'].append(out_path)
    input['job_path'] = find_available_path(os.path.join(input['out_dir'], input['base_name'] + ".job"), ext='.sh')
    input['log_path'] = find_available_path(os.path.join(input['out_dir'], input['base_name'] + ".job"), ext='.log')


def make_script(input, settings, pipeline):
    script = pipeline["script"].copy()
    for key, (index, _) in pipeline["variables"].items():
        if key.lower() == "base_path":
            value = input["base_path"]
        else:
            value = settings[key]["value"]
        script[index] = f"{key}=\"{value}\""
    header = \
        f"#!/bin/bash\n" \
        f"#SBATCH --account='{settings['ACCOUNT (SCRIPT HEADER)']['value']}'\n" \
        f"#SBATCH --time='{settings['TIME (SCRIPT HEADER)']['value']}'\n" \
        f"#SBATCH --cpus-per-task='{settings['CPU_CORES (SCRIPT HEADER)']['value']}'\n" \
        f"#SBATCH --mem-per-cpu='{settings['MEMORY_PER_CORE (SCRIPT HEADER)']['value']}'\n" \
        f"#SBATCH --job-name='{input['base_name']}'\n" \
        f"#SBATCH --output='{input['log_path']}'"
    input["script"] = header + "\n\n\n" + "\n".join(script)


def write_scripts(inputs):
    existing = []
    for input in inputs:
        in_paths = [os.path.realpath(path) for path in input["in_paths"]]
        for path in (*input["out_paths"], input["job_path"]):
            if os.path.realpath(path) in in_paths:
                continue
            if os.path.exists(path):
                existing.append(path)
    if existing:
        log("warning: these files already exist and will be overwritten:")
        for path in existing:
            log(f"    {path}")
        if not ask_continue():
            abort()
    for input in inputs:
        if not os.path.isdir(os.path.dirname(input['out_dir'])):
            raise FileNotFoundError('parent directory of ' + input['out_dir'] + ' missing')
        if not os.path.isdir(input['out_dir']):
            os.mkdir(input['out_dir'])
        with open(input['job_path'], 'w') as file:
            file.write(input['script'])


def move_inputs(inputs):
    for input in inputs:
        for in_path, out_path in zip(input['in_paths'], input['out_paths']):
            if os.path.realpath(in_path) == os.path.realpath(out_path):
                continue
            os.rename(in_path, out_path)


def start_jobs(inputs, dry):
    if dry:
        log("start commands:")
    for input in inputs:
        input['start_command'] = ['sbatch', input['job_path']]
        start_command_for_log = ['sbatch', os.path.basename(input['job_path'])]
        if dry:
            log("    " + " ".join(input["start_command"]))
        else:
            log(" ".join(start_command_for_log), end=": ")
            result = subprocess.run(input['start_command'], capture_output=True, check=True)
            log(result.stdout.decode().strip())
    if not dry:
        result = subprocess.run(['squeue', '-u', getpass.getuser()], capture_output=True, check=True)
        log(result.stdout.decode().strip())


def main(raw_args):

    info = '''
usage: $ align_pipelines $PIPELINE $INPUTS... $OPTIONS...

pipelines:
  chip, atac, chip-lab, atac-lab, rna, bis,
  bigwig, bigwig-lab, peak-calling, peak-calling-lab,
  chip-se-lab

inputs:
  paths to inputs directories and/or
  paths to inputs files (with or without file extension)

options:
  --out-dir ::::::::: path to output directory
                      one sub directory per input will be made in it
                      same directories as inputs by default
  --no-sub-dir :::::: if flag set, no sub directory will be made and
                      scripts will be written directly in inputs
                      directories or --out-dir (if specified)
  --account ::::::::: account for job submission
                      rrg-jdrouin by default
  --time :::::::::::: requested time as hh:mm:ss
                      03:00:00 by default
  --cpu ::::::::::::: requested cpu cores
                      20 by default
  --memory :::::::::: requested memory per core
                      3800M by default (~76G for --cpu 20)
  --bowtie2-index ::: path to bowtie2 reference genome index directory
                      path must include the base name of the files inside
                      ~/projects/.../genomes/mm10/bowtie2_index/mm10 by default
  --bam-with-dups ::: keep or remove original bam file with duplicated reads
                      remove by default
  --bigwig-bin :::::: bin size in base pairs for bigwig
                      10 by default
  --macs2-control ::: path to indexed bam file to use as a control
                      experiment (eg, input) for peak calling
                      no control experiment used by default
  --macs2-pvalue :::: macs2 peak treshold pvalue
                      1e-3 by default
  --macs2-genome :::: reference genome size used by macs2
                      mm by default (for mouse, use hs for human)
  --chr-sizes ::::::: reference genome chromosome sizes as tsv file
                      ~/projects/.../genomes/mm10/mm10_chr_sizes.tsv by default
  --bismark-genome :: path to bismark reference genome directory
                      ~/projects/.../genomes/mm10/bismark_genome by default
  --hisat2-index :::: path to hisat2 reference genome index directory
                      path must include the base name of the files inside
                      ~/projects/.../genomes/mm10/hisat2_index/mm10 by default
  --from-file ::::::: read arguments from the specified file
                      and insert them in place of this argument

'''

    if "-h" in raw_args or "--help" in raw_args:
        sys.stderr.write(info)
        raise SystemExit(0)
    
    while '--from-file' in raw_args:
        index = raw_args.index('--from-file')
        with open(raw_args[index + 1], 'r') as file:
            file_args = [arg
                for line in file
                for arg in shlex.split(line.strip())
                if arg.strip()]
        raw_args = raw_args[:index] + file_args + raw_args[index + 2:]
    
    parser = ArgumentParser()
    parser.add_argument("pipeline")
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--out-dir", dest="out_dir", default=None)
    parser.add_argument("--no-sub-dir", dest="no_sub_dir", action="store_true")
    parser.add_argument("--account", default="rrg-jdrouin")
    parser.add_argument("--time", default="03:00:00")
    parser.add_argument("--cpu", dest="cpu_cores", default="20")
    parser.add_argument("--memory", dest="memory_per_core", default="3800M")
    parser.add_argument("--bowtie2-index", dest="bowtie2_index_path",
        default="$HOME/projects/def-jdrouin/_common/genomes/mm10/bowtie2_index/mm10")
    parser.add_argument("--bam-with-dups", dest="bam_with_duplicates", default="remove")
    parser.add_argument("--bigwig-bin", dest="bigwig_bin_size", default="10")
    parser.add_argument("--macs2-control", dest="macs2_control_path", default="")
    parser.add_argument("--macs2-pvalue", dest="macs2_pvalue", default="1e-3")
    parser.add_argument("--macs2-genome", dest="macs2_genome_size", default="mm")
    parser.add_argument("--chr-sizes", dest="chr_sizes_path",
        default="$HOME/projects/def-jdrouin/_common/genomes/mm10/mm10_chr_sizes.tsv")
    parser.add_argument("--bismark-genome", dest="bismark_genome_path",
        default="$HOME/projects/def-jdrouin/_common/genomes/mm10/bismark_genome")
    parser.add_argument("--hisat2-index", dest="hisat2_index_path",
        default="$HOME/projects/def-jdrouin/_common/genomes/mm10/hisat2_index/mm10")
    arguments = vars(parser.parse_args(raw_args))
    pipeline_name, inputs_locs, out_dir, no_sub_dir = list(arguments.values())[:4]
    settings = dict(list(arguments.items())[4:])

    pipeline_name = pipeline_name.replace("-", "_")
    pipeline = get_pipeline(pipeline_name)
    settings = parse_settings(settings, pipeline)
    setting_warnings = [setting["warning"] for setting in settings.values() if setting["warning"]]
    if setting_warnings:
        for setting_warning in setting_warnings:
            log(setting_warning)
        if not ask_continue("warning: settings have failed validation, continue anyway?"):
            abort()

    inputs = process_inputs(inputs_locs, pipeline["extensions"])
    for input in inputs:
        set_out_paths(input, out_dir, no_sub_dir)
        make_script(input, settings, pipeline)

    log_key_value("pipeline", pipeline_name)
    log_key_value("extensions", " ".join(pipeline["extensions"]))
    if not inputs:
        log_key_value("search for or in", *inputs_locs)
        log("no input files matching pipeline extensions found")
        raise SystemExit(0)
    log_key_value(f"{len(inputs)} inputs", *(input["in_base_path"] for input in inputs))
    for key, setting in settings.items():
        if key.endswith(" (SCRIPT HEADER)"):
            if key[:-16] in settings and setting["value"] == settings[key[:-16]]["value"]:
                continue
            elif key[:-16] not in settings:
                log_key_value(f"{key[:-16].lower()}".replace("_", " "), setting["value"])
                continue
        log_key_value(f"{key.lower()}".replace("_", " "), setting["value"])

    if not ask_continue("write scripts?" if no_sub_dir else "write scripts and move inputs?"):
        abort()

    write_scripts(inputs)
    move_inputs(inputs)

    response = ask_continue("start jobs?")
    start_jobs(inputs, dry=not response)
