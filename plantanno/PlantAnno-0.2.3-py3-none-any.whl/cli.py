import argparse
from plantanno.pipelines import plantanno_main
from toolbiox.lib.common.fileIO import tsv_file_dict_parse


def main():

    # argument parse
    parser = argparse.ArgumentParser(
        prog='PlantAnno', description='An automated process for plant genome annotation'
    )

    parser.add_argument("sp_id",
                        help="Genome species id", type=str)
    parser.add_argument("genome_fasta",
                        help="Path of target genome fasta file", type=str)
    parser.add_argument("-m", "--mode", choices=['orthoDB', 'normal'],
                        help="Annotation mode, orthoDB will just use orthoDB without RNA-seq data.")
    parser.add_argument("-og", "--ortho_orthofinder_dir",
                        help="Path of the dir for orthofinder results for orthoDB. (named like: Results_Sep23, try: orthofinder -f Rawdata -t 56 -a 56 -S diamond -og)", type=str)
    parser.add_argument("-nr", "--nr_diamond_db",
                        help="Path of the diamond database for NCBI nr", type=str)
    parser.add_argument("-sr", "--short_rna_seq_data",
                        help="Path of short_rna_seq_data, tsv file, column: sample_id, r1, r2", type=str)
    parser.add_argument("-lr", "--long_rna_seq_data",
                        help="Path of long_rna_seq_data, tsv file, column: sample_id, reads_file", type=str)
    parser.add_argument("-p", "--close_species_protein_data",
                        help="Path of close_species_protein_data, tsv file, column: species_id, fasta_file", type=str)
    parser.add_argument("-c", "--close_species_cds_data",
                        help="Path of close_species_cds_data, tsv file, column: species_id, fasta_file", type=str)
    parser.add_argument("-d", "--work_dir", help="Path of work dir (default as ./plantanno_out)",
                        default="./plantanno_out", type=str)
    parser.add_argument("-t", "--num_threads",
                        help="threads number (default as 56)", default=56, type=int)
    parser.add_argument(
        "-me", "--max_memory", help="max memory (default as 100G)", default='100G', type=str)

    args = parser.parse_args()

    if args.short_rna_seq_data:
        args.short_rna_seq_data = tsv_file_dict_parse(
            args.short_rna_seq_data, key_col='sample_id')
    if args.long_rna_seq_data:
        args.long_rna_seq_data = tsv_file_dict_parse(
            args.long_rna_seq_data, key_col='sample_id')
    if args.close_species_protein_data:
        info_dict = tsv_file_dict_parse(args.close_species_protein_data, key_col='species_id')
        args.close_species_protein_data = {i:info_dict[i]['fasta_file'] for i in info_dict}
    if args.close_species_cds_data:
        info_dict = tsv_file_dict_parse(args.close_species_cds_data, key_col='species_id')
        args.close_species_cds_data = {i:info_dict[i]['fasta_file'] for i in info_dict}

    plantanno_main(args)


if __name__ == '__main__':
    main()

    # input_data = {
    #     'genome_fasta': '/lustre/home/xuyuxing/Work/annotation_pipeline/Cau.genome.fasta',
    #     'rna_seq_fastq': [
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C8_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C8_H7GL5CCXY_L6_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C7_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C7_H7GL5CCXY_L6_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C6_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C6_H7GL5CCXY_L6_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C5_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C5_H7GL5CCXY_L6_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C4_HCMC7CCXY_L2_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C4_HCMC7CCXY_L2_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C3_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C3_H7GL5CCXY_L6_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C1_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C1_H7GL5CCXY_L6_2.clean.fq.gz"),
    #         ("/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C10_H7GL5CCXY_L6_1.clean.fq.gz",
    #          "/lustre/home/xuyuxing/Work/annotation_pipeline/raw_trans_data/C10_H7GL5CCXY_L6_2.clean.fq.gz")
    #     ],
    #     'close_species_aa_fasta': {
    #         "T35883N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T35883N0.gene_model.protein.fasta",
    #         "T3702N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T3702N0.gene_model.protein.fasta",
    #         "T4081N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T4081N0.gene_model.protein.fasta",
    #         "T4113N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T4113N0.gene_model.protein.fasta",
    #         "T49390N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T49390N0.gene_model.protein.fasta",
    #     },
    #     'close_species_cds_fasta': {
    #         "T35883N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T35883N0.gene_model.cds.fasta",
    #         "T3702N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T3702N0.gene_model.cds.fasta",
    #         "T4081N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T4081N0.gene_model.cds.fasta",
    #         "T4113N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T4113N0.gene_model.cds.fasta",
    #         "T49390N0": "/lustre/home/xuyuxing/Work/annotation_pipeline/close_species_proteins/T49390N0.gene_model.cds.fasta",
    #     }
    # }

    # work_dir = '/lustre/home/xuyuxing/Work/annotation_pipeline/Cau'
    # threads = 80
    # trinity_max_memory = '100G'

    # class abc():
    #     pass


    # args = abc()

    # args.work_dir = "/lustre/home/xuyuxing/Work/annotation_pipeline/plantanno_orthoDB_out"
    # args.genome_fasta = "/lustre/home/xuyuxing/Work/annotation_pipeline/Cau.genome.fasta"
    # args.num_threads = 80
    # args.mode = 'orthoDB'
    # args.ortho_orthofinder_dir = '/lustre/home/xuyuxing/Database/OrthoDB/plants/OrthoFinder/Results_Sep23'
    # args.sp_id = 'Cau'
    # args.nr_diamond_db = '/lustre/home/xuyuxing/Database/NCBI/nr/20220215/nr.dmnd'
