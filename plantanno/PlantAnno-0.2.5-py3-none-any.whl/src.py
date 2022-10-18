from interlap import InterLap
from plantanno.config import *
from toolbiox.api.common.genome.blast import outfmt6_read_big
from toolbiox.lib.common.genome.genome_feature2 import Genome, read_gff_file, gene_rename, Gene, ChrLoci, write_gff_file, GenomeFeature
from toolbiox.lib.common.genome.seq_base import read_fasta, write_fasta, read_fasta_by_faidx, BioSeq
from toolbiox.lib.common.math.interval import merge_intervals, interval_minus_set, overlap_between_interval_set, sum_interval_length
from toolbiox.lib.common.os import mkdir, rmdir, have_file, cmd_run, copy_file, multiprocess_running, get_file_name
from toolbiox.lib.common.sqlite_command import retrieve_dict_from_db
from toolbiox.lib.common.util import printer_list
from toolbiox.lib.common.fileIO import tsv_file_parse, tsv_file_dict_parse
from bioseqtools.pipelines import SeqEntropy_main
import json
import math
import os
import re
from toolbiox.lib.common.evolution.orthotools2 import OrthoGroups


class pipeline_args():
    pass


def rename_genome_file(raw_genome_fasta, genome_fasta, seq_id_map_file, sp_id=""):
    genome_seqdict, seqname_list = read_fasta(raw_genome_fasta, upper=True)

    digit = math.ceil(math.log(len(genome_seqdict) + 1, 10))
    new_id_pattern = "%sC%%0%sdN" % (sp_id.upper(), digit)

    seq_len_sort = sorted(list(genome_seqdict.keys()), key=lambda x: len(
        genome_seqdict[x].seq), reverse=True)

    with open(seq_id_map_file, 'w') as f:
        num = 0
        for s_id in seq_len_sort:
            new_id = new_id_pattern % num
            seq = genome_seqdict[s_id]
            f.write("%s\t%s\n" % (new_id, seq.seqname))
            seq.seqname = new_id
            num += 1

    write_fasta([genome_seqdict[i] for i in genome_seqdict],
                genome_fasta, wrap_length=75, upper=True)


def rename_and_merge_close_species_gene_file(input_file_list, output_fasta_file, seq_id_map_file):

    with open(seq_id_map_file, 'w') as f:
        merge_seq_dict = {}
        num = 0
        for input_file in input_file_list:
            seqdict, seqname_list = read_fasta(input_file, upper=True)
            for s_id in seqdict:
                s = seqdict[s_id]
                new_id = 'C%d' % num
                s.seqname = new_id
                f.write("%s\t%s\t%s\n" %
                        (new_id, s_id, get_file_name(input_file)))
                merge_seq_dict[new_id] = s
                num += 1

    write_fasta([merge_seq_dict[i] for i in merge_seq_dict],
                output_fasta_file, wrap_length=75, upper=True)


def rename_close_species_gene_file(input_sp_seq_dict, output_dir):

    mkdir(output_dir, True)
    seq_id_map_file = os.path.join(output_dir, 'gene.rename.map')

    rename_sp_seq_dict = {}
    with open(seq_id_map_file, 'w') as f:
        sp_num = 0
        for sp_id in input_sp_seq_dict:
            new_sp_id = "S%d" % sp_num

            input_file = input_sp_seq_dict[sp_id]
            seqdict, seqname_list = read_fasta(input_file, upper=True)

            seq_num = 0
            rename_seqdict = {}
            for s_id in seqdict:
                new_seq_id = '%sG%d' % (new_sp_id, seq_num)

                s = seqdict[s_id]

                s.seqname = new_seq_id
                f.write("%s\t%s\t%s\t%s\n" %
                        (sp_id, new_sp_id, s_id, new_seq_id))

                rename_seqdict[new_seq_id] = s

                seq_num += 1

            output_fasta_file = os.path.join(output_dir, new_sp_id + ".fasta")
            write_fasta([rename_seqdict[i] for i in rename_seqdict],
                        output_fasta_file, wrap_length=75, upper=True)

            rename_sp_seq_dict[new_sp_id] = output_fasta_file
            sp_num += 1

    return rename_sp_seq_dict


def hisat_build(genome_fasta, mapping_dir):

    build_flag = False
    for i in os.listdir(mapping_dir):
        if 'input.genome.fasta.hisat2' in i:
            build_flag = True
            break

    if not build_flag:
        os.symlink(genome_fasta, mapping_dir+"/input.genome.fasta")

        cmd_string = "%s input.genome.fasta input.genome.fasta.hisat2" % HISAT2_BUILD_PATH
        f, o, e = cmd_run(cmd_string, cwd=mapping_dir, silence=False)

        if not f:
            print(o)
            print(e)
            raise ValueError("hisat2-build failed, see above!")

    return mapping_dir + "/input.genome.fasta.hisat2"


def get_map_rate_from_log(log_file):
    with open(log_file, 'r') as f:
        f_info = f.read()
        map_rate = float([i.split("%")[0] for i in f_info.split(
            '\n') if 'overall alignment rate' in i][0])
    return map_rate


def hisat_map(sample_id, fq1, fq2, index, mapping_dir, threads):
    bam_file = "%s/%s.bam" % (mapping_dir, sample_id)

    if not have_file(bam_file):

        hisat2_cmd_string = "%s -p %d --dta -x %s -1 %s -2 %s -S %s.sam" % (
            HISAT2_PATH, threads, index, fq1, fq2, sample_id)
        f1, o1, e1 = cmd_run(hisat2_cmd_string, cwd=mapping_dir, silence=False)

        hisat2_log = "%s/%s.log" % (mapping_dir, sample_id)

        with open(hisat2_log, 'w') as f:
            f.write(e1)

        samtools_cmd_string = "%s sort -@ %d -o %s.bam %s.sam" % (
            SAMTOOLS_PATH, threads, sample_id, sample_id)
        f2, o2, e2 = cmd_run(samtools_cmd_string,
                             cwd=mapping_dir, silence=False)

        rmdir("%s/%s.sam" % (mapping_dir, sample_id))

    return bam_file, hisat2_log


def MaskFasta2Gff(masked_fasta, output_gff):
    seq_dict = read_fasta_by_faidx(masked_fasta)

    gf_list = []
    for seq_id in seq_dict:
        print(seq_id)
        seq_now = seq_dict[seq_id].seq
        range_tmp_list = []
        for i in re.finditer('N', seq_now):
            range_tmp_list.append((i.end(), i.end()))
        range_list = merge_intervals(range_tmp_list, True)

        num = 0
        for i in range_list:
            gf = GenomeFeature(id="%s_masked_range_%d" % (
                seq_id, num), type='masked_range', chr_loci=ChrLoci(chr_id=seq_id, start=i[0], end=i[1]))
            gf_list.append(gf)
            num += 1

    write_gff_file(gf_list, output_gff, sort=True)


def get_softmask_genome(raw_genome_fasta, masked_gff_file, output_softmask_genome):
    seq_dict = read_fasta(raw_genome_fasta)[0]
    seq_len_dict = {i: len(seq_dict[i].seq) for i in seq_dict}
    gff_dict = read_gff_file(masked_gff_file)

    masked_range_dict = {i: [] for i in seq_dict}
    for t_id in gff_dict:
        for g_id in gff_dict[t_id]:
            gf = gff_dict[t_id][g_id]
            masked_range_dict[gf.chr_id].append((gf.start, gf.end))

    unmasked_range_dict = {}
    for chr_id in seq_len_dict:
        chr_len = (1, seq_len_dict[chr_id])
        unmasked_range_dict[chr_id] = interval_minus_set(
            chr_len, masked_range_dict[chr_id])

    type_dict = {}
    for chr_id in seq_len_dict:
        type_dict[chr_id] = []
        type_dict[chr_id] += [tuple(list(i) + ['l'])
                              for i in masked_range_dict[chr_id]]
        type_dict[chr_id] += [tuple(list(i) + ['u'])
                              for i in unmasked_range_dict[chr_id]]
        type_dict[chr_id] = sorted(type_dict[chr_id], key=lambda x: x[0])

    softmask_genome_dict = {}
    for chr_id in seq_dict:
        seq_string = seq_dict[chr_id].seq
        softmask_seq_string = ''
        for s, e, t in type_dict[chr_id]:
            if t == 'u':
                softmask_seq_string += seq_string[s-1:e].upper()
            elif t == 'l':
                softmask_seq_string += seq_string[s-1:e].lower()
        softmask_genome_dict[chr_id] = BioSeq(softmask_seq_string, chr_id)

    for chr_id in softmask_genome_dict:
        softmask_genome_dict[chr_id].write_to_file(output_softmask_genome)

    return output_softmask_genome


def write_pasa_alignAssembly_config(file_path, database_path):
    file_string = """
## templated variables to be replaced exist as <__var_name__>

# database settings
DATABASE=%s

#######################################################
# Parameters to specify to specific scripts in pipeline
# create a key = "script_name" + ":" + "parameter"
# assign a value as done above.

#script validate_alignments_in_db.dbi
validate_alignments_in_db.dbi:--MIN_PERCENT_ALIGNED=<__MIN_PERCENT_ALIGNED__>
validate_alignments_in_db.dbi:--MIN_AVG_PER_ID=<__MIN_AVG_PER_ID__>

#script subcluster_builder.dbi
subcluster_builder.dbi:-m=50
""" % (database_path)

    with open(file_path, 'w') as f:
        f.write(file_string)


def convert_braker_to_evm(braker_out_gff, braker_evm_gff_file):

    braker_info_dict = read_gff_file(braker_out_gff)

    gene_dict = {}
    for gtype in braker_info_dict:
        for mRNA_id in braker_info_dict[gtype]:
            mRNA = braker_info_dict[gtype][mRNA_id]

            mRNA.type = 'mRNA'
            used_features = []
            for i in mRNA.sub_features:
                if i.type in ['exon', 'CDS']:
                    used_features.append(i)
            mRNA.sub_features = used_features

            gene_id = mRNA.id.split(".")[0]
            gene_dict.setdefault(gene_id, []).append(mRNA)

    rename_gene_dict = {}
    num = 0
    for g_id in gene_dict:
        new_id = 'Gene%d' % num

        mRNA_list = gene_dict[g_id]
        (g_s, g_e) = merge_intervals([(m.start, m.end) for m in mRNA_list])[0]
        gLoci = ChrLoci(mRNA_list[0].chr_id,
                        strand=mRNA_list[0].strand, start=g_s, end=g_e)

        raw_gene = Gene(id=new_id, chr_loci=gLoci, qualifiers={
                        'Name': new_id, }, sub_features=mRNA_list)

        rename_gene = gene_rename(raw_gene, new_id, mRNA_list[0].chr_id)
        rename_gene_dict[new_id] = rename_gene

        rename_gene_dict[new_id].qualifiers['source'] = 'BRAKER2'
        num += 1

    write_gff_file([rename_gene_dict[i] for i in rename_gene_dict],
                   braker_evm_gff_file, source='BRAKER2')


def merge_file(input_file_list, output_file):
    with open(output_file, 'w') as f:
        for input_file in input_file_list:
            fr = open(input_file, 'r').read()
            if len(fr) > 0 and fr[-1] != '\n':
                fr = fr+'\n'
            f.write(fr)


def busco_job(input_file, work_dir, gff_file=None, num_threads=8, mode="genome", database="embryophyta_odb10", augustus_species="arabidopsis", clean=True):
    mkdir(work_dir, True)
    busco_out_report = os.path.join(work_dir, 'busco_report.json')

    if not (have_file(busco_out_report)):
        input_file = copy_file(input_file, work_dir)
        busco_out = "%s_vs_%s" % (get_file_name(input_file), database)

        if mode == "genome":
            cmd_string = "%s --offline --download_path %s -c %d -m genome -i %s -o %s -l %s --augustus_species %s" % (
                BUSCO_PATH, BUSCO_DOWNLOAD_DIR, num_threads, input_file, busco_out, database, augustus_species
            )
            f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)
        elif mode == "proteins":
            cmd_string = "%s --offline --download_path %s -c %d -m proteins -i %s -o %s -l %s" % (
                BUSCO_PATH, BUSCO_DOWNLOAD_DIR, num_threads, input_file, busco_out, database
            )
            f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)
        elif mode == "gff":
            genome = Genome(genome_file=input_file, gff_file=gff_file)
            genome.genome_feature_parse()
            genome.build_gene_sequence()

            protein_file = os.path.join(work_dir, 'protein.fa')

            with open(protein_file, 'w') as f:
                for g_id in genome.feature_dict['gene']:
                    g = genome.feature_dict['gene'][g_id]
                    f.write(">%s\n%s\n" % (g.id, g.model_aa_seq))

            cmd_string = "%s --offline --download_path %s -c %d -m proteins -i %s -o %s -l %s" % (
                BUSCO_PATH, BUSCO_DOWNLOAD_DIR, num_threads, protein_file, busco_out, database
            )
            f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        busco_report = os.path.join(work_dir,
                                    busco_out, 'short_summary.specific.%s.%s_vs_%s.json' % (database, get_file_name(input_file), database))

        copy_file(busco_report, busco_out_report)

        if clean:
            rmdir(os.path.join(work_dir, busco_out))
            rmdir(input_file)

    with open(busco_out_report, "r") as f:
        busco_report_dict = json.load(f)

    return busco_report_dict


def edta_job(input_genome_file, work_dir, close_species_cds_data=None, num_threads=8, clean=True):
    mkdir(work_dir, True)

    if close_species_cds_data:
        close_cds_fasta = work_dir + "/close_cds.fasta"
        close_cds_map = work_dir + "/close_cds.rename.map"

        if not (have_file(close_cds_fasta) and have_file(close_cds_map)):
            rename_and_merge_close_species_gene_file(
                [close_species_cds_data[i] for i in close_species_cds_data], close_cds_fasta, close_cds_map)

    edta_genome_file = work_dir + "/input.genome.fasta"
    edta_gff_file = work_dir + "/input.genome.fasta.mod.EDTA.TEanno.gff3"
    edta_mask_seq = work_dir + "/input.genome.fasta.mod.MAKER.masked"
    edta_mask_gff = work_dir + "/input.genome.fasta.mod.MAKER.masked.gff3"
    edta_sum_file = work_dir + "/input.genome.fasta.mod.EDTA.TEanno.sum"
    softmask_genome_file = work_dir + "/softmask.genome.fasta"

    if not have_file(edta_genome_file):
        copy_file(input_genome_file, edta_genome_file)

    if not (have_file(edta_mask_gff) and have_file(edta_gff_file) and have_file(edta_mask_seq) and have_file(edta_sum_file) and have_file(softmask_genome_file)):

        if close_species_cds_data:
            cmd_string = '%s --genome input.genome.fasta --cds close_cds.fasta --overwrite 1 --sensitive 1 --anno 1 --threads %d' % (
                EDTA_PERL_SCRIPT, num_threads)
            f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)
            # print(o)
            # print(e)
        else:
            cmd_string = '%s --genome input.genome.fasta --overwrite 1 --sensitive 1 --anno 1 --threads %d' % (
                EDTA_PERL_SCRIPT, num_threads)
            f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        MaskFasta2Gff(edta_mask_seq, edta_mask_gff)

        if not (have_file(edta_mask_gff) and have_file(edta_gff_file) and have_file(edta_mask_seq) and have_file(edta_sum_file)):
            print(o)
            print(e)
            raise ValueError("EDTA pipeline failed, see above!")

        get_softmask_genome(edta_genome_file, edta_mask_gff,
                            softmask_genome_file)

    if clean:
        rmdir(os.path.join(work_dir, 'input.genome.fasta.mod.EDTA.raw'))
        rmdir(os.path.join(work_dir, 'input.genome.fasta.mod.EDTA.anno'))
        rmdir(os.path.join(work_dir, 'input.genome.fasta.mod'))
        rmdir(os.path.join(work_dir, 'input.genome.fasta.mod.EDTA.combine'))
        rmdir(os.path.join(work_dir, 'input.genome.fasta.mod.EDTA.final'))

    return edta_gff_file, edta_mask_gff, softmask_genome_file


def trinity_job(short_rna_seq_data, work_dir, num_threads=8, max_memory='50G'):
    mkdir(work_dir, True)

    r1_file_list = [short_rna_seq_data[i]['r1'] for i in short_rna_seq_data]
    r2_file_list = [short_rna_seq_data[i]['r2'] for i in short_rna_seq_data]

    trinity_fasta = work_dir + "/RNA.trinity.Trinity.fasta"
    trinity_gene_trans_map = work_dir + \
        "/RNA.trinity.Trinity.fasta.gene_trans_map"

    if not (have_file(trinity_fasta) and have_file(trinity_gene_trans_map)):

        left_string = ",".join(r1_file_list)
        right_string = ",".join(r2_file_list)

        cmd_string = '%s --seqType fq --max_memory %s --left %s --right %s --CPU %d --output RNA.trinity --full_cleanup' % (
            TRINITY_PATH, max_memory, left_string, right_string, num_threads)

        f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        if not (have_file(trinity_fasta) and have_file(trinity_gene_trans_map)):
            print(o)
            print(e)
            raise ValueError("Trinity pipeline failed, see above!")

    return trinity_fasta, trinity_gene_trans_map


def pasa_job(work_dir, RNA_assembly_fasta=None, input_genome_fasta=None, input_gff_file=None, mode="structure_annotation", num_threads=8):
    mkdir(work_dir, True)

    if mode == "structure_annotation":

        pasa_output_gff_file = os.path.join(
            work_dir, "sample_mydb_pasa.pasa_assemblies.gff3")

        if not have_file(pasa_output_gff_file):

            pasa_input_rnaseq_file = copy_file(RNA_assembly_fasta, work_dir)
            pasa_input_genome_file = copy_file(input_genome_fasta, work_dir)

            # cmd_string = "%s/bin/seqclean %s -c 10" % (
            #     PASAHOME, pasa_input_rnaseq_file)
            # f, o, e = cmd_run(cmd_string, cwd=pasa_dir, silence=False)

            pasa_alignAssembly_config_file = os.path.join(
                work_dir, 'alignAssembly.config')
            write_pasa_alignAssembly_config(
                pasa_alignAssembly_config_file, os.path.join(work_dir, 'sample_mydb_pasa'))

            # cmd_string = "%s/Launch_PASA_pipeline.pl -c %s -C -R -g %s -t %s -T -u %s --ALIGNERS blat,gmap --CPU %d" % (
            #     PASAHOME, pasa_alignAssembly_config_file, pasa_input_genome_file, pasa_input_rnaseq_file + ".clean", pasa_input_rnaseq_file, args.num_threads)

            cmd_string = "%s/Launch_PASA_pipeline.pl -c %s -C -R -g %s -t %s --ALIGNERS blat,gmap --CPU %d" % (
                PASAHOME, pasa_alignAssembly_config_file, pasa_input_genome_file, pasa_input_rnaseq_file, num_threads)

            f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        return pasa_output_gff_file

    elif mode == "structure_polish":

        pass


def stringtie_job(input_genome_file, short_rna_seq_data, work_dir, num_threads=8):
    mkdir(work_dir, True)

    hisat_genome_index = hisat_build(input_genome_file, work_dir)

    rna_seq_dict = {}

    num = 1

    for sample_id in short_rna_seq_data:
        fq1 = short_rna_seq_data[sample_id]['r1']
        fq2 = short_rna_seq_data[sample_id]['r2']

        sample_id = 'R%d' % num
        try:
            bam_file, hisat2_log = (
                "%s/%s.bam" % (work_dir, sample_id), "%s/%s.log" % (work_dir, sample_id))
            if not (have_file(bam_file) and have_file(hisat2_log)):
                bam_file, hisat2_log = hisat_map(
                    sample_id, fq1, fq2, hisat_genome_index, work_dir, num_threads)

            rna_seq_dict[sample_id] = {
                'id': sample_id,
                'raw_fastq': (fq1, fq2),
                'bam': bam_file,
                'log_file': hisat2_log,
                'flag': True,
                'mapped_ratio': get_map_rate_from_log(hisat2_log),
            }

        except:
            rna_seq_dict[sample_id] = {
                'id': sample_id,
                'raw_fastq': (fq1, fq2),
                'bam': None,
                'log_file': None,
                'flag': False,
                'mapped_ratio': 0.0,
            }

        num += 1

    merged_sorted_bam_file = os.path.join(work_dir, "merged.sorted.bam")

    if not have_file(merged_sorted_bam_file):
        merged_bam_file = os.path.join(work_dir, "merged.bam")
        merged_bam_list_file = os.path.join(work_dir, "merged_bam.txt")

        with open(merged_bam_list_file, 'w') as f:
            for s_id in rna_seq_dict:
                if rna_seq_dict[s_id]['mapped_ratio'] > 80:
                    f.write(rna_seq_dict[s_id]['bam']+"\n")

        cmd_string = '%s merge -@ %d -b %s %s' % (
            SAMTOOLS_PATH, num_threads, merged_bam_list_file, merged_bam_file)
        f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        cmd_string = "%s sort -@ %d -o %s %s" % (
            SAMTOOLS_PATH, num_threads, merged_sorted_bam_file, merged_bam_file)
        f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        rmdir(merged_bam_file)

    stringtie_output_gff = os.path.join(work_dir, "stringtie.evm.gff")

    if not have_file(stringtie_output_gff):
        stringtie_output_gtf = os.path.join(work_dir, "stringtie.gtf")
        cmd_string = "%s -o %s -p %d %s" % (
            STRINGTIE_PATH, stringtie_output_gtf, num_threads, merged_sorted_bam_file)
        f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        cmd_string = "%s %s > %s" % (
            GTF_TO_ALIGNMENT_GFF3_PERL_SCRIPT, stringtie_output_gtf, stringtie_output_gff)
        f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

    return rna_seq_dict, merged_sorted_bam_file, stringtie_output_gff


def hugep2g_job(input_genome_file, close_species_protein_data, edta_mask_gff, work_dir, num_threads=8):
    mkdir(work_dir, True)

    hugep2g_evm_gff = os.path.join(work_dir, 'hugep2g.evm.gff')
    if not have_file(hugep2g_evm_gff):

        # get genome
        if not os.path.exists(work_dir + "/input.genome.fasta"):
            copy_file(input_genome_file, work_dir + "/input.genome.fasta")

        # rename pt_file and write query_table.tsv
        query_seq_dir = os.path.join(work_dir, "query_seq_dir")
        close_species_protein_data = rename_close_species_gene_file(
            close_species_protein_data, query_seq_dir)

        query_table_file = os.path.join(work_dir, "query_table.tsv")
        with open(query_table_file, 'w') as f:
            f.write("sp_id\tpt_file\n")
            for sp_id in close_species_protein_data:
                f.write("%s\t%s\n" %
                        (sp_id, close_species_protein_data[sp_id]))

        # write skip range file
        skip_range_file = os.path.join(work_dir, 'skip_range.txt')

        with open(edta_mask_gff, 'r') as f1:
            with open(skip_range_file, 'w') as f2:
                for each_line in f1:
                    split_tuple = each_line.split('\t')
                    if len(split_tuple) > 4:
                        f2.write("%s\t%s\t%s\n" %
                                 (split_tuple[0], split_tuple[3], split_tuple[4]))

        # running hugep2g
        hugep2g_output_dir = os.path.join(work_dir, "hugep2g_out")

        cmd_string = '%s -s %s -d %s -t %d -c 0.7 -n 10 %s input.genome.fasta' % (
            HUGEP2G_PATH, skip_range_file, hugep2g_output_dir, num_threads, query_table_file)

        f, o, e = cmd_run(cmd_string, cwd=work_dir, silence=False)

        # filter and get output
        gf_list = []

        for sp_id in close_species_protein_data:
            query_sp_dir = os.path.join(hugep2g_output_dir, 'work_dir', sp_id)
            output_db = os.path.join(query_sp_dir, 'output.db')
            output_dict = retrieve_dict_from_db(output_db)

            for q_id in output_dict:
                q_r = output_dict[q_id]
                for gf in q_r.subjects:
                    mgf = gf.sub_features[0]
                    del mgf.qualifiers['AA']
                    del mgf.qualifiers['CDS']

                    q_len = float(mgf.qualifiers['Target_Length'][0])
                    a_len = float(mgf.qualifiers['aln_len'])

                    if a_len > 20 and a_len/q_len > 0.5:
                        gf_list.append(gf)

        with open(hugep2g_evm_gff, 'w') as f:
            for gf in gf_list:
                mRNA = gf.sub_features[0]
                target = mRNA.qualifiers['Target'][0]
                cds_list = mRNA.sub_features

                cds_list = sorted(cds_list, key=lambda x: int(
                    x.qualifiers['Target_Start'][0]))

                for cds in cds_list:
                    target_start = int(cds.qualifiers['Target_Start'][0])
                    target_end = int(cds.qualifiers['Target_End'][0])

                    printer_string = printer_list(
                        [mRNA.chr_id, 'genewise', 'match', cds.start, cds.end, '.', cds.strand, '.',
                            'ID=%s;Target=%s %d %d' % (mRNA.id, target, target_start, target_end)])

                    f.write(printer_string + "\n")

    return hugep2g_evm_gff


def w_index(evalue):
    if evalue == 0.0:
        return 200
    else:
        return min(200, round(-math.log(evalue, 10) / 2))


def get_top_close_species(ortho_DB_dict, braker_pt_file, work_dir, top_num, num_threads):
    mkdir(work_dir, True)
    cmd_string_raw = "diamond blastp -q %s -k 1 -d %s -o %s -f 6 -p 1"

    args_list = []
    output_dict = {}
    for s_id in ortho_DB_dict:
        dmnd_file = ortho_DB_dict[s_id]['dmnd']
        output_file = os.path.join(work_dir, '%s.bls' % s_id)
        if not have_file(output_file):
            cmd_string = cmd_string_raw % (
                braker_pt_file, dmnd_file, output_file)
            args_list.append((cmd_string, work_dir, 1, True))
        output_dict[s_id] = output_file

    if len(args_list) > 0:
        multiprocess_running(cmd_run, args_list, num_threads, silence=True)

    top_sp_list = []
    for s_id in output_dict:
        # print(s_id)
        d_out = output_dict[s_id]
        # top_sp_list.append((s_id, sum([w_index(q.hit[0].hsp[0].Hsp_evalue) for q in outfmt6_read_big(d_out)])))
        top_sp_list.append(
            (s_id, sum([q.hit[0].hsp[0].Hsp_bit_score for q in outfmt6_read_big(d_out)])))

    top_sp_list = [i[0] for i in sorted(
        top_sp_list, key=lambda x:x[1], reverse=True)[:top_num]]

    return top_sp_list


def braker_job(softmask_genome_file, work_dir, merged_sorted_bam_file=None, protein_lib_fasta=None, num_threads=8):
    mkdir(work_dir, True)

    braker_evm_gff_file = os.path.join(work_dir, 'braker', 'braker.evm.gff3')
    braker_cds_file = os.path.join(work_dir, 'braker', 'braker.cds.fasta')
    braker_pt_file = os.path.join(work_dir, 'braker', 'braker.pt.fasta')

    if not (have_file(braker_evm_gff_file) and have_file(braker_cds_file) and have_file(braker_pt_file)):

        if merged_sorted_bam_file and (protein_lib_fasta is None):
            cmd_string = "%s --genome %s --bam %s --cores %s --gff3 --softmasking" % (
                BRAKER_PERL_SCRIPT, softmask_genome_file, merged_sorted_bam_file, num_threads)
        elif (merged_sorted_bam_file is None) and protein_lib_fasta:
            cmd_string = "%s --genome %s --prot_seq %s --cores %s --gff3 --softmasking" % (
                BRAKER_PERL_SCRIPT, softmask_genome_file, protein_lib_fasta, num_threads)

        cmd_run(cmd_string, cwd=work_dir, silence=False)

        braker_out_gff = os.path.join(work_dir, 'braker', 'braker.gff3')
        convert_braker_to_evm(braker_out_gff, braker_evm_gff_file)
        gff_to_gene_seq(softmask_genome_file, braker_evm_gff_file,
                        braker_cds_file, braker_pt_file)

    return braker_evm_gff_file, braker_cds_file, braker_pt_file


def gff_to_gene_seq(genome_fasta, gff_file, cds_file, pt_file):
    genome = Genome(genome_file=genome_fasta,
                    gff_file=gff_file)
    genome.genome_feature_parse()
    genome.build_gene_sequence()

    with open(cds_file, 'w') as f:
        for g_id in genome.feature_dict['gene']:
            g = genome.feature_dict['gene'][g_id]
            f.write(">%s\n%s\n" % (g.id, g.model_cds_seq))

    with open(pt_file, 'w') as f:
        for g_id in genome.feature_dict['gene']:
            g = genome.feature_dict['gene'][g_id]
            f.write(">%s\n%s\n" % (g.id, g.model_aa_seq))


def extract_raw_data_from_orthofinder(orthofinder_dir):

    of_work_dir = os.path.join(orthofinder_dir, "WorkingDirectory")
    of_raw_data = {}

    for fn in os.listdir(of_work_dir):
        mobj_list = re.findall("(Species\d+)\.fa", fn)
        if len(mobj_list) > 0:
            sp_id = mobj_list[0]
            of_raw_data.setdefault(sp_id, {})
            of_raw_data[sp_id]['fasta'] = os.path.join(of_work_dir, fn)

        mobj_list = re.findall("diamondDB(Species\d+).dmnd", fn)
        if len(mobj_list) > 0:
            sp_id = mobj_list[0]
            of_raw_data.setdefault(sp_id, {})
            of_raw_data[sp_id]['dmnd'] = os.path.join(of_work_dir, fn)

    with open(os.path.join(of_work_dir, "SpeciesIDs.txt"), 'r') as f:
        for each_line in f:
            n, r = each_line.strip().split(": ")
            of_raw_data['Species%s' % n]['raw_name'] = r

    return of_raw_data


def evm_job(input_genome_file, work_dir, T_gff_dict={}, A_gff_dict={}, P_gff_dict={}, num_threads=8):
    """
    T_gff_dict = {
        'Cufflinks':("cufflinks.evm.gff3",10),
        'assembler-sample_mydb_pasa':("trinity.evm.gff3",10),
    }

    gff_source_name:(gff_file_path,weight)
    """
    mkdir(work_dir, True)

    evm_output_gff = os.path.join(work_dir, "EVM.all.gff3")
    evm_cds_file = os.path.join(work_dir, "EVM.cds.fasta")
    evm_pt_file = os.path.join(work_dir, "EVM.pt.fasta")

    if not have_file(evm_output_gff):
        evm_input_genome_file = copy_file(input_genome_file, work_dir)

        weight_file = os.path.join(work_dir, "weight.txt")

        with open(weight_file, 'w') as f:
            for t, t_dict, tag in [('T', T_gff_dict, 'TRANSCRIPT'), ('A', A_gff_dict, 'ABINITIO_PREDICTION'), ('P', P_gff_dict, 'PROTEIN')]:
                if len(t_dict) > 0:
                    gff_file = os.path.join(work_dir, "%s.gff3" % t)
                    merge_file([t_dict[i][0] for i in t_dict], gff_file)
                    cmd_string = "sed -i '/^$/d' %s.gff3" % t
                    cmd_run(cmd_string, cwd=work_dir, silence=False)
                    cmd_string = "sed -i '/^#/d' %s.gff3" % t
                    cmd_run(cmd_string, cwd=work_dir, silence=False)

                    for i in t_dict:
                        f.write("%s\t%s\t%s\n" % (tag, i, str(t_dict[i][1])))

        if len(T_gff_dict) and len(A_gff_dict) and len(P_gff_dict):
            ev_string = "--gene_predictions A.gff3 --protein_alignments P.gff3 --transcript_alignments T.gff3"
        elif len(T_gff_dict) and len(A_gff_dict) and len(P_gff_dict) == 0:
            ev_string = "--gene_predictions A.gff3 --transcript_alignments T.gff3"
        elif len(T_gff_dict) and len(A_gff_dict) == 0 and len(P_gff_dict):
            ev_string = "--protein_alignments P.gff3 --transcript_alignments T.gff3"
        elif len(T_gff_dict) == 0 and len(A_gff_dict) and len(P_gff_dict):
            ev_string = "--gene_predictions A.gff3 --protein_alignments P.gff3"
        elif len(T_gff_dict) and len(A_gff_dict) == 0 and len(P_gff_dict) == 0:
            ev_string = "--transcript_alignments T.gff3"
        elif len(T_gff_dict) == 0 and len(A_gff_dict) and len(P_gff_dict) == 0:
            ev_string = "--gene_predictions A.gff3"
        elif len(T_gff_dict) == 0 and len(A_gff_dict) == 0 and len(P_gff_dict):
            ev_string = "--protein_alignments P.gff3"

        cmd_string = "%s/EvmUtils/partition_EVM_inputs.pl --genome %s %s --segmentSize 1000000 --overlapSize 500000 --partition_listing partitions_list.out" % (
            EVM_HOME, evm_input_genome_file, ev_string)
        cmd_run(cmd_string, cwd=work_dir, silence=False)

        cmd_string = "%s/EvmUtils/write_EVM_commands.pl --genome %s --weights %s %s --output_file_name evm.out --partitions partitions_list.out > commands.list" % (
            EVM_HOME, evm_input_genome_file, weight_file, ev_string)
        cmd_run(cmd_string, cwd=work_dir, silence=False)

        commands_list_file = os.path.join(work_dir, "commands.list")

        args_list = []
        with open(commands_list_file, 'r') as f:
            for i in f:
                args_list.append((i.strip(), work_dir, 1, True))

        multiprocess_running(cmd_run, args_list,
                             num_threads, silence=False)

        cmd_string = "%s/EvmUtils/recombine_EVM_partial_outputs.pl --partitions partitions_list.out --output_file_name evm.out" % EVM_HOME
        cmd_run(cmd_string, cwd=work_dir, silence=False)

        cmd_string = "%s/EvmUtils/convert_EVM_outputs_to_GFF3.pl --partitions partitions_list.out --output evm.out --genome %s" % (
            EVM_HOME, evm_input_genome_file)
        cmd_run(cmd_string, cwd=work_dir, silence=False)

        cmd_string = "find . -regex \".*evm.out.gff3\" -exec cat {} \; > EVM.all.gff3"
        cmd_run(cmd_string, cwd=work_dir, silence=False)

        gff_to_gene_seq(input_genome_file, evm_output_gff,
                        evm_cds_file, evm_pt_file)

    return evm_output_gff, evm_cds_file, evm_pt_file


def join_orthogroups(pt_file, orthofinder_dir, work_dir, num_threads=8, clean=True):

    orthogroup_tsv_file = os.path.join(work_dir, 'Orthogroups.tsv')

    if not have_file(orthogroup_tsv_file):
        
        raw_of_dir = os.path.join(work_dir, get_file_name(orthofinder_dir))
        mkdir(raw_of_dir)

        copy_file(orthofinder_dir + "/WorkingDirectory", raw_of_dir)
        copy_file(orthofinder_dir + "/Log.txt", raw_of_dir)
        copy_file(orthofinder_dir + "/Citation.txt", raw_of_dir)

        pt_file_dir = os.path.join(work_dir, "pt_file")
        mkdir(pt_file_dir, True)
        copy_file(pt_file, os.path.join(pt_file_dir, "target.fa"))

        cmd_string = '%s -b %s -f %s -t %d -a %d -S diamond -og' % (
            ORTHOFINDER_PATH, raw_of_dir, pt_file_dir, num_threads, num_threads)

        cmd_run(cmd_string, cwd=work_dir, silence=False)

        last_time = 0
        newest_dir = ''
        for dir_name in os.listdir(work_dir):
            dir_name = os.path.join(work_dir, dir_name)
            if os.path.getmtime(dir_name) > last_time:
                last_time = os.path.getmtime(dir_name)
                newest_dir = dir_name

        new_orthogroup_tsv_file = os.path.join(
            newest_dir, 'Orthogroups', 'Orthogroups.tsv')
        orthogroup_tsv_file = copy_file(new_orthogroup_tsv_file, work_dir)

        if clean:
            rmdir(raw_of_dir)

    return orthogroup_tsv_file


def rename_and_filter(genome_fasta, raw_gff_file, filter_gene_list, ip_tsv_file, work_dir, sp_id):
    output_gff_file = os.path.join(work_dir, '%s.PlantAnno.gff3' % sp_id)
    output_cds_file = os.path.join(work_dir, '%s.PlantAnno.cds.fasta' % sp_id)
    output_pt_file = os.path.join(work_dir, '%s.PlantAnno.pt.fasta' % sp_id)
    output_ip_tsv_file = os.path.join(work_dir, '%s.PlantAnno.interproscan.tsv' % sp_id)

    if not (have_file(output_gff_file) and have_file(output_cds_file) and have_file(output_pt_file) and have_file(output_ip_tsv_file)):
        genome = Genome(genome_file=genome_fasta,
                        gff_file=raw_gff_file)
        genome.genome_feature_parse()
        genome.build_gene_sequence()
        genome.genome_file_parse()

        digit = math.ceil(math.log(len(filter_gene_list) + 1, 10))

        gene_id_map_dict = {}
        for chr_id in genome.chromosomes:
            if not hasattr(genome.chromosomes[chr_id], 'feature_dict'):
                genome.chromosomes[chr_id].load_genome_features(
                    genome.feature_dict)
                genome.chromosomes[chr_id].build_index()

            chr_feature_dict = genome.chromosomes[chr_id].feature_dict['gene']
            filterd_chr_gene_list = []
            for g_id in chr_feature_dict:
                if g_id in filter_gene_list:
                    gene = chr_feature_dict[g_id]
                    filterd_chr_gene_list.append(gene)

            filterd_chr_gene_list = sorted(
                filterd_chr_gene_list, key=lambda x: x.start, reverse=False)

            num = 0
            new_id_pattern = "%s%%0%sd" % (chr_id, digit)
            new_id_gene_list = []
            for gene in filterd_chr_gene_list:
                gene_new_name = new_id_pattern % num
                gene_id_map_dict[gene.id] = gene_new_name
                gene = gene_rename(gene, gene_new_name, chr_new_name=chr_id)
                new_id_gene_list.append(gene)
                num += 1

            write_gff_file(new_id_gene_list, output_gff_file,
                           source='PlantAnno', sort=True)

        cmd_string = "sed -i \'/\#\#gff-version/d\' %s" % output_gff_file
        cmd_run(cmd_string)

        gff_to_gene_seq(genome_fasta, output_gff_file,
                        output_cds_file, output_pt_file)

        # ip
        with open(ip_tsv_file, 'r') as f1:
            with open(output_ip_tsv_file, 'w') as f2:
                for each_line in f1:
                    each_line = each_line.strip()
                    g_id, info = each_line.split("\t", 1)
                    if g_id in gene_id_map_dict:
                        f2.write("%s\t%s\n" % (gene_id_map_dict[g_id], info))

    return output_gff_file, output_cds_file, output_pt_file, output_ip_tsv_file


def AnnoCleaner_main(args):
    gene_info = read_gff_file(args.gene_gff)
    gene_info = gene_info['gene']

    # entropy, nr and interpro
    nr_info = {}
    if args.nr_bls is not None:
        nr_info_raw = tsv_file_parse(args.nr_bls)
        for i in nr_info_raw:
            nr_info[nr_info_raw[i][0]] = 0

    interpro_info = {}
    if args.interpro_tsv is not None:
        interpro_info_raw = tsv_file_parse(args.interpro_tsv)
        for i in interpro_info_raw:
            interpro_info[interpro_info_raw[i][0]] = 0

    entropy_info = {}
    if args.entropy_tsv is not None:
        entropy_raw = tsv_file_parse(args.entropy_tsv)
        for i in entropy_raw:
            gene_id = entropy_raw[i][0]
            entropy = float(entropy_raw[i][1])
            entropy_info[gene_id] = entropy

    # bad repeat
    bad_repeat_dict = {}
    if args.repeat_gff_file is not None:
        for gene_id in gene_info:
            gf = gene_info[gene_id]
            bad_repeat_dict[(gf.chr_loci.chr_id, gf.chr_loci.strand)] = []

        repeat_gff = read_gff_file(args.repeat_gff_file)
        for i in repeat_gff.keys():
            for gf_id in repeat_gff[i]:
                gf = repeat_gff[i][gf_id]
                if gf.strand is None:
                    for strand_now in ['+', '-']:
                        if (gf.chr_id, strand_now) in bad_repeat_dict:
                            bad_repeat_dict[(gf.chr_id, strand_now)].append(
                                (gf.start, gf.end))
                else:
                    if (gf.chr_id, gf.strand) in bad_repeat_dict:
                        bad_repeat_dict[(gf.chr_id, gf.strand)].append(
                            (gf.start, gf.end))

        for i in bad_repeat_dict:
            merged_intervals = merge_intervals(bad_repeat_dict[i], True)
            bad_repeat_dict[i] = InterLap()
            if len(merged_intervals) > 0:
                bad_repeat_dict[i].update(merged_intervals)

    # tran
    tran_evidence_dict = {}
    if args.tran_evidence_gff is not None:
        for gene_id in gene_info:
            gf = gene_info[gene_id]
            tran_evidence_dict[(gf.chr_loci.chr_id, gf.chr_loci.strand)] = []

        # tran
        tran_info_raw = tsv_file_parse(args.tran_evidence_gff)
        for i in tran_info_raw:
            q_name, strand, start, end = tran_info_raw[i][0], tran_info_raw[i][6], int(
                tran_info_raw[i][3]), int(tran_info_raw[i][4])
            if (q_name, strand) in bad_repeat_dict:
                tran_evidence_dict[(q_name, strand)].append((start, end))

        for i in tran_evidence_dict:
            merged_intervals = merge_intervals(tran_evidence_dict[i], True)
            tran_evidence_dict[i] = InterLap()
            if len(merged_intervals) > 0:
                tran_evidence_dict[i].update(merged_intervals)

    # judge
    with open(args.output_file, 'w') as f:
        f.write(
            "gene_id\tmRNA_id\ttran_ratio\tbad_repeat_ratio\tentropy\tnr_anno\tinterpro_anno\tgood_gene\n")
        for gene_id in gene_info:
            gf = gene_info[gene_id]
            contig = (gf.chr_loci.chr_id, gf.chr_loci.strand)

            for mRNA in gf.sub_features:

                exon_intervals = [(i.start, i.end)
                                  for i in mRNA.sub_features if i.type == 'exon']
                if len(exon_intervals) == 0:
                    exon_intervals = [(i.start, i.end)
                                      for i in mRNA.sub_features if i.type == 'CDS']

                if contig in tran_evidence_dict:
                    tran_intervals = list(
                        tran_evidence_dict[contig].find((gf.start, gf.end)))
                else:
                    tran_intervals = []
                overlap_ratio, overlap_length, overlap = overlap_between_interval_set(
                    exon_intervals, tran_intervals)
                tran_overlap_ratio = overlap_length / \
                    sum_interval_length(exon_intervals)

                if contig in bad_repeat_dict:
                    bad_repeat_intervals = list(
                        bad_repeat_dict[contig].find((gf.start, gf.end)))
                else:
                    bad_repeat_intervals = []
                overlap_ratio, overlap_length, overlap = overlap_between_interval_set(
                    exon_intervals, bad_repeat_intervals)
                bad_repeat_overlap_ratio = overlap_length / \
                    sum_interval_length(exon_intervals)

                nr_anno = gene_id in nr_info or mRNA.id in nr_info
                interpro_anno = gene_id in interpro_info or mRNA.id in interpro_info

                if gene_id in entropy_info:
                    entropy = entropy_info[gene_id]
                elif mRNA.id in entropy_info:
                    entropy = entropy_info[mRNA.id]
                else:
                    continue

                good_gene = False
                if tran_overlap_ratio >= args.tran_threshold or nr_anno or interpro_anno:
                    good_gene = True
                if bad_repeat_overlap_ratio >= args.repeat_threshold:
                    good_gene = False
                if entropy <= args.entropy_threshold:
                    good_gene = False

                if good_gene:
                    f.write("%s\t%s\t%.2f\t%.2f\t%.4f\t%s\t%s\t%s\n" % (gene_id, mRNA.id, tran_overlap_ratio,
                                                                        bad_repeat_overlap_ratio, entropy, str(nr_anno), str(interpro_anno), str(good_gene)))


def annocleaner_for_orthoDB(genome_fasta, gene_gff_file, repeat_gff_file, work_dir, num_threads, nr_diamond_db):
    mkdir(work_dir, True)
    annoclear_tsv = os.path.join(work_dir, "annoclear.output.tsv")
    annoclear_pt_file = os.path.join(work_dir, "annoclear.output.pt.fasta")
    ip_tsv = os.path.join(work_dir, "raw.pt.interproscan.tsv")

    if not (have_file(annoclear_tsv) and have_file(annoclear_pt_file) and have_file(ip_tsv)):

        cds_file = os.path.join(work_dir, "raw.cds.fasta")
        pt_file = os.path.join(work_dir, "raw.pt.fasta")

        gff_to_gene_seq(genome_fasta, gene_gff_file, cds_file, pt_file)

        # diamond
        nr_bls = os.path.join(work_dir, "raw.pt.nr.bls")
        diamond_cmd_string = '%s blastp -q %s -k 50 -d %s -o %s -f 6 -p %d' % (
            DIAMOND_PATH, pt_file, nr_diamond_db, nr_bls, num_threads)
        cmd_run(diamond_cmd_string, cwd=work_dir, retry_max=1, silence=True)

        # interproscan
        interproscan_cmd_string = "%s -cpu %d -i %s -f tsv -b %s -iprlookup --goterms --pathways -dp" % (
            INTERPROSCAN_PATH, num_threads, pt_file, os.path.join(work_dir, "raw.pt.interproscan"))
        cmd_run(interproscan_cmd_string, cwd=work_dir,
                retry_max=1, silence=True)

        # entropy
        entropy_tsv = os.path.join(work_dir, "raw.pt.entropy.tsv")
        args = pipeline_args()
        args.input_fasta = pt_file
        args.output_file = entropy_tsv
        args.word_size = 3
        SeqEntropy_main(args)

        # annoclear
        args = pipeline_args()
        args.gene_gff = gene_gff_file
        args.nr_bls = nr_bls
        args.interpro_tsv = ip_tsv
        args.repeat_gff_file = repeat_gff_file
        args.tran_evidence_gff = None
        args.entropy_tsv = entropy_tsv
        args.output_file = annoclear_tsv

        args.tran_threshold = 0.5
        args.repeat_threshold = 0.5
        args.entropy_threshold = 3.9

        AnnoCleaner_main(args)
        annoclear_dict = tsv_file_dict_parse(annoclear_tsv)
        good_gene_list = [annoclear_dict[i]['gene_id'] for i in annoclear_dict]

        raw_pt_dict = read_fasta_by_faidx(pt_file)
        good_seq_list = [raw_pt_dict[i] for i in good_gene_list]
        write_fasta(good_seq_list, annoclear_pt_file,
                    wrap_length=75, upper=True)

    return annoclear_tsv, annoclear_pt_file, ip_tsv


def orthogroups_filter(input_pt_file, work_dir, ortho_orthofinder_dir, num_threads):
    filter_gene_aa_fasta = os.path.join(work_dir, "filter_gene.pt.fasta")

    if not have_file(filter_gene_aa_fasta):
        
        orthogroup_tsv_file = join_orthogroups(
            input_pt_file, ortho_orthofinder_dir, work_dir, num_threads=num_threads)

        OGs = OrthoGroups(OG_tsv_file=orthogroup_tsv_file)
        filter_gene_list = []
        for og_id in OGs.OG_dict:
            og = OGs.OG_dict[og_id]
            if len([i for i in og.species_stat if og.species_stat[i] > 0]) >= 2 and og.species_stat['target'] > 0 and og.species_stat['target'] <= 300:
                filter_gene_list.extend([i.id for i in og.gene_dict['target']])

        raw_pt_dict = read_fasta_by_faidx(input_pt_file)
        good_seq_list = [raw_pt_dict[i] for i in filter_gene_list]
        write_fasta(good_seq_list, filter_gene_aa_fasta,
                    wrap_length=75, upper=True)

    return filter_gene_aa_fasta