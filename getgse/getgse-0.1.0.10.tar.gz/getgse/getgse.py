#!/usr/bin/env python3

import argparse
import sys
from pysradb.sraweb import SRAweb
import os
import wget
import math
import time
from pathlib import Path
import docker
from . import __version__


def get_arguments():
    parser = argparse.ArgumentParser(description = 'GSE Downloder')
    # nargs를 사용하여 복수의 인자가 올 수 있음
    parser.add_argument('--gse', nargs='+', required=True, help="GSE number") 
    parser.add_argument('--version', action="version", version="%(prog)s {version}".format(version=__version__)) 

    gse = parser.parse_args().gse

    return gse

def bar_custom(current, total, width=80):
    width=30
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s " % (current / total * 100, percent_bar)
    return progress

def download(url, file_name = None, out_path="."):
    Path(out_path+"/").mkdir(parents=True, exist_ok=True)
    if not file_name:
        file_name = out_path+"/"+url.split('/')[-1]

    print("Downloading", file_name, "from", url)
    wget.download(url, out=file_name, bar=bar_custom)
    print()

def run_fasterq_dump(SRR, out_path):
    client = docker.from_env()
    wd = os.getcwd() + "/" + out_path
    volumes_dict = {wd: {'bind': '/output', 'mode': 'rw'}}
    client.containers.run("ncbi/sra-tools", ['fasterq-dump', SRR, '--split-files', '-p'], privileged = True, auto_remove=True, volumes=volumes_dict, working_dir='/output', stderr=True, stdout=True)

def cli():
    db = SRAweb()
    GSE = get_arguments()

    all_SRPs = []

    for gse in GSE:    
        print("[%s]" % gse)
        SRPs = list(db.gse_to_srp(gse).study_accession)

        for SRP in SRPs:
            url_list = []
            print("exploring %s in %s" % (SRP, gse))
            SRRs = None
            all_SRPs.append(SRP)
            df = db.sra_metadata(SRP, detailed=True)
            try:
                df = df[df.library_strategy == 'RNA-Seq']
            except:
                print("RNA-Seq data is not existed.")
                quit()
            df.to_csv(gse + ".tsv", sep="\t", header=True, index=False)

            if 'PAIRED' in df.library_layout.values:
                url_list.extend(df[df.library_layout == 'PAIRED'].ena_fastq_http_1.dropna().tolist())
                url_list.extend(df[df.library_layout == 'PAIRED'].ena_fastq_http_2.dropna().tolist())
            if 'SINGLE' in df.library_layout.values:
                url_list.extend(df[df.library_layout == 'SINGLE'].ena_fastq_http.dropna().tolist())
            if df.ena_fastq_http.isnull().values.any() and df.ena_fastq_http_1.isnull().values.any():
                SRRs = df[df.ena_fastq_http.isnull() & df.ena_fastq_http_1.isnull()].run_accession.tolist()
            
            url_list = [url for url in url_list if not Path(gse + "/" + url.split('/')[-1]).is_file()]
            
            if not url_list: # if list is empty
                if SRRs: # if SRRs not empty
                    pass
                else:
                    print("All files are downloaded.")
                    continue

            for url in url_list:
                download(url, out_path=gse)

            if SRRs is not None:
                for SRR in SRRs:
                    run_fasterq_dump(SRR, out_path=gse)
                    time.sleep(10)
            
    all_metadata = db.sra_metadata(all_SRPs, detailed=True)
    all_metadata.to_csv('all_metadata.tsv', sep="\t", header=True, index=False)

if __name__ == "__main__":
    cli()