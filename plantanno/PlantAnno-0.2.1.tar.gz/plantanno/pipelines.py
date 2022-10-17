import os
from toolbiox.lib.common.os import mkdir, have_file, cmd_run, copy_file, multiprocess_running
from plantanno.src import *
from plantanno.config import *
from toolbiox.lib.common.genome.seq_base import read_fasta, read_fasta_big
from toolbiox.lib.common.util import pickle_dump, logging_init
from toolbiox.lib.xuyuxing.math.stats import n50_stats


def plantanno_main(args):

    # 0. build workspace
    args.work_dir = os.path.abspath(args.work_dir)
    mkdir(args.work_dir, True)

    args.log_file = args.work_dir + "/log"

    logger = logging_init("PlantAnno Log", args.log_file)

    args_info_string = "Argument list:\n"
    attrs = vars(args)

    for item in attrs.items():
        args_info_string = args_info_string + ("%s: %s\n" % item)

    logger.info(args_info_string)

    # 0.1 get genome file
    logger.info("0.Input_Data Check input data")
    data_dir = os.path.join(args.work_dir, '0.Input_Data')
    mkdir(data_dir, True)

    seq_id_map_file = os.path.join(data_dir, 'genome.rename.map')
    genome_fasta = os.path.join(data_dir, 'input.genome.fasta')

    logger.info("\tRename genome sequences")
    if not (have_file(seq_id_map_file) and have_file(genome_fasta)):
        raw_genome_fasta = os.path.join(data_dir, 'input.raw.fasta')
        copy_file(args.genome_fasta, raw_genome_fasta)
        rename_genome_file(raw_genome_fasta, genome_fasta, seq_id_map_file)

        copy_file(genome_fasta, os.path.join(args.work_dir,
                                             '%s.PlantAnno.genome.fasta' % args.sp_id))
        copy_file(seq_id_map_file, os.path.join(
            args.work_dir, '%s.PlantAnno.rename.map' % args.sp_id))

    # 0.2 genome busco
    logger.info("\tRunning Genome Busco")
    busco_dir = os.path.join(data_dir, 'genome_busco')
    genome_busco_report = busco_job(genome_fasta, busco_dir, num_threads=args.num_threads, mode="genome",
                                    database="embryophyta_odb10", augustus_species="arabidopsis")
    logger.info("\t%s\t%s" % ('Total length',
                              genome_busco_report['results']['Total length']))
    logger.info("\t%s\t%s" % ('Number of scaffolds',
                              genome_busco_report['results']['Number of scaffolds']))
    logger.info("\t%s\t%s" % ('Number of contigs',
                              genome_busco_report['results']['Number of contigs']))
    logger.info("\t%s\t%s" % ('Scaffold N50',
                              genome_busco_report['results']['Scaffold N50']))
    logger.info("\t%s\t%s" % ('Number of contigs',
                              genome_busco_report['results']['Number of contigs']))
    logger.info("\t%s\t%s" %
                ('Contigs N50', genome_busco_report['results']['Contigs N50']))
    logger.info("\t%s\t%s" % ('one_line_summary',
                              genome_busco_report['results']['one_line_summary']))

    if args.mode == 'orthoDB':
        of_raw_data = extract_raw_data_from_orthofinder(
            args.ortho_orthofinder_dir)

        # 1. Running EDTA
        logger.info("1.EDTA Running EDTA")
        edta_dir = args.work_dir + "/1.EDTA"
        edta_gff_file, edta_mask_gff, softmask_genome_file = edta_job(
            genome_fasta, edta_dir, num_threads=args.num_threads)

        # 2. Braker2
        logger.info("2.BRAKER2 Running BRAKER2")
        braker_dir = os.path.join(args.work_dir, "2.BRAKER2")
        mkdir(braker_dir, True)

        orthoDB_fasta = os.path.join(braker_dir, 'orthoDB.all.fasta')
        if not have_file(orthoDB_fasta):
            merge_file([of_raw_data[i]['fasta']
                        for i in of_raw_data], orthoDB_fasta)

        braker_evm_gff_file, braker_cds_file, braker_pt_file = braker_job(softmask_genome_file, braker_dir,
                                                                          protein_lib_fasta=orthoDB_fasta, num_threads=args.num_threads)

        braker_busco_report_dict = busco_job(braker_pt_file, os.path.join(
            braker_dir, "busco"), num_threads=args.num_threads, mode="proteins", database="embryophyta_odb10", clean=True)

        logger.info("\t%s\t%s" % ('one_line_summary',
                                  braker_busco_report_dict['results']['one_line_summary']))

        # 3. HugeP2G
        logger.info("3.HugeP2G Running HugeP2G")
        HugeP2G_dir = os.path.join(args.work_dir, "3.HugeP2G")
        mkdir(HugeP2G_dir, True)

        ortho_diamond_dir = os.path.join(HugeP2G_dir, "diamond")
        top_close_species_list = get_top_close_species(
            of_raw_data, braker_pt_file, ortho_diamond_dir, 3, args.num_threads)

        close_species_protein_data = {
            i: of_raw_data[i]['fasta'] for i in top_close_species_list}

        # close_species_protein_data = {}

        # for sp_id in top_close_species_list:
        #     bls_out = os.path.join(ortho_diamond_dir, '%s.bls' % sp_id)
        #     genome_seqdict, seqname_list = read_fasta(of_raw_data[sp_id]['fasta'], upper=True)
        #     sub_fasta = os.path.join(HugeP2G_dir, '%s.fasta' % sp_id)
        #     sub_id_list = list(set([q.hit[0].Hit_id for q in outfmt6_read_big(bls_out)]))

        #     with open(sub_fasta, 'w') as f:
        #         for s_id in sub_id_list:
        #             f.write(">%s\n%s\n" % (s_id, genome_seqdict[s_id].seq))

        #     close_species_protein_data[sp_id] = os.path.join(HugeP2G_dir, '%s.fasta' % sp_id)

        hugep2g_evm_gff = hugep2g_job(
            genome_fasta, close_species_protein_data, edta_mask_gff, HugeP2G_dir, num_threads=args.num_threads)

        # 4. EVM
        logger.info("4.EVM Running EVM")
        evm_dir = os.path.join(args.work_dir, "4.EVM")
        mkdir(evm_dir, True)

        A_gff_dict = {"BRAKER2": (braker_evm_gff_file, 10)}
        P_gff_dict = {"genewise": (hugep2g_evm_gff, 10)}

        evm_output_gff, evm_cds_file, evm_pt_file = evm_job(genome_fasta, evm_dir, T_gff_dict={
        }, A_gff_dict=A_gff_dict, P_gff_dict=P_gff_dict, num_threads=args.num_threads)

        evm_busco_report_dict = busco_job(evm_pt_file, os.path.join(
            evm_dir, "busco"), num_threads=args.num_threads, mode="proteins", database="embryophyta_odb10", clean=True)

        logger.info("\t%s\t%s" % ('one_line_summary',
                                  evm_busco_report_dict['results']['one_line_summary']))

        # 5. filter
        logger.info("5.Filter Running Filter")
        filter_dir = os.path.join(args.work_dir, "5.Filter")
        mkdir(filter_dir, True)

        # 5.1 AnnoCleaner
        ac_dir = os.path.join(filter_dir, "annocleaner")
        mkdir(ac_dir, True)
        annoclear_tsv, annoclear_pt_file, ip_tsv = annocleaner_for_orthoDB(genome_fasta, evm_output_gff, edta_gff_file, ac_dir, args.num_threads, args.nr_diamond_db)

        # 5.2 orthofinder
        of_dir = os.path.join(filter_dir, "orthofinder")
        mkdir(of_dir, True)
        of_gene_pt_file = orthogroups_filter(annoclear_pt_file, of_dir, args.ortho_orthofinder_dir, args.num_threads)

        # 5.3 busco
        filter_busco_report_dict = busco_job(of_gene_pt_file, os.path.join(
            filter_dir, "busco"), num_threads=args.num_threads, mode="proteins", database="embryophyta_odb10", clean=True)

        # 6. rename
        filter_gene_list = read_fasta(of_gene_pt_file)[1]
        output_gff_file, output_cds_file, output_pt_file, output_ip_tsv = rename_and_filter(
            genome_fasta, evm_output_gff, filter_gene_list, ip_tsv, args.work_dir, args.sp_id)

        result_dict = {
            'genome': (genome_busco_report, ''),
            'evm': (evm_busco_report_dict, evm_pt_file),
            'filter': (filter_busco_report_dict, output_pt_file)
        }

        stats_dict = {}
        for tag in result_dict:
            busco_report, pt_file = result_dict[tag]

            if pt_file == '':
                stats_dict[tag] = {
                    'busco': busco_report['results'],
                }
                logger.info("\n\t%s\t%s" %
                            (tag, busco_report['results']['one_line_summary']))
            else:
                len_list = [len(i.seq) for i in read_fasta_big(pt_file)]

                stats_info = n50_stats(len_list)

                num = stats_info[2]
                mean = stats_info[3]/stats_info[2]
                n50 = stats_info[1][50]['length']
                min = stats_info[4]
                max = stats_info[5]

                stats_dict[tag] = {
                    'busco': busco_report['results'],
                    'gene_num': num,
                    'gene_mean': mean,
                    'gene_n50': n50,
                    'gene_min': min,
                    'gene_max': max,
                }

                logger.info("\n\t%s\t%s\n\tgene_num: %d\n\tgene_mean: %.2f\n\tgene_n50: %d\n\tgene_min: %d\n\tgene_max: %d" % (
                    tag, busco_report['results']['one_line_summary'], num, mean, n50, min, max))

        pickle_dump(stats_dict, os.path.join(args.work_dir, "stats_dict.pyb"))

    elif args.mode == 'normal':
        # 1. Running EDTA
        edta_dir = args.work_dir + "/1.EDTA"
        edta_gff_file, edta_mask_gff, softmask_genome_file = edta_job(
            genome_fasta, edta_dir, close_species_cds_data=args.close_species_cds_data, num_threads=args.num_threads)

        # 2. assemble RNA-seq
        trinity_dir = args.work_dir + "/2.Trinity"
        trinity_fasta, trinity_gene_trans_map = trinity_job(
            args.short_rna_seq_data, trinity_dir, num_threads=args.num_threads, max_memory=args.max_memory)

        pasa_dir = os.path.join(trinity_dir, 'pasa')
        pasa_output_gff_file = pasa_job(pasa_dir, RNA_assembly_fasta=trinity_fasta,
                                        input_genome_fasta=genome_fasta, mode="structure_annotation", num_threads=args.num_threads)

        # 3. RNA-seq mapping
        mapping_dir = args.work_dir + "/3.RNA_seq_mapping"
        rna_seq_dict, merged_sorted_bam_file, stringtie_output_gff = stringtie_job(
            genome_fasta, args.short_rna_seq_data, mapping_dir, num_threads=args.num_threads)

        # 4. HugeP2G
        HugeP2G_dir = os.path.join(args.work_dir, "4.HugeP2G")
        hugep2g_evm_gff = hugep2g_job(
            genome_fasta, args.close_species_protein_data, edta_mask_gff, HugeP2G_dir, num_threads=args.num_threads)

        # 5. Braker2
        braker_dir = os.path.join(args.work_dir, "5.BRAKER2")
        mkdir(braker_dir, True)

        braker_job(softmask_genome_file, braker_dir,
                   merged_sorted_bam_file=merged_sorted_bam_file, num_threads=args.num_threads)
        braker_evm_gff_file = os.path.join(
            braker_dir, 'braker', 'braker.evm.gff3')

        # 6. EVM
        evm_dir = os.path.join(args.work_dir, "6.EVM")
        mkdir(evm_dir, True)

        evm_output_gff = os.path.join(evm_dir, "EVM.all.gff3")

        if not have_file(evm_output_gff):

            evm_input_genome_file = copy_file(genome_fasta, evm_dir)

            T_gff_file = os.path.join(evm_dir, "T.gff3")
            merge_file(
                [pasa_output_gff_file, stringtie_output_gff], T_gff_file)
            cmd_string = "sed -i '/^$/d' T.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)
            cmd_string = "sed -i '/^#/d' T.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            A_gff_file = os.path.join(evm_dir, "A.gff3")
            merge_file([braker_evm_gff_file], A_gff_file)
            cmd_string = "sed -i '/^$/d' A.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)
            cmd_string = "sed -i '/^#/d' A.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            P_gff_file = os.path.join(evm_dir, "P.gff3")
            merge_file([hugep2g_evm_gff], P_gff_file)
            cmd_string = "sed -i '/^$/d' P.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)
            cmd_string = "sed -i '/^#/d' P.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            weight_file = os.path.join(evm_dir, "weight.txt")
            with open(weight_file, 'w') as f:
                f.write(
                    "ABINITIO_PREDICTION\tBRAKER2\t1\nPROTEIN\tgenewise\t5\nTRANSCRIPT\tassembler-sample_mydb_pasa\t10\nTRANSCRIPT\tCufflinks\t10\n")

            cmd_string = "%s/EvmUtils/partition_EVM_inputs.pl --genome %s --gene_predictions A.gff3 --protein_alignments P.gff3 --transcript_alignments T.gff3 --segmentSize 1000000 --overlapSize 500000 --partition_listing partitions_list.out" % (
                EVM_HOME, evm_input_genome_file)
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            cmd_string = "%s/EvmUtils/write_EVM_commands.pl --genome %s --weights %s --gene_predictions A.gff3 --protein_alignments P.gff3 --transcript_alignments T.gff3 --output_file_name evm.out --partitions partitions_list.out > commands.list" % (
                EVM_HOME, evm_input_genome_file, weight_file)
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            commands_list_file = os.path.join(evm_dir, "commands.list")

            args_list = []
            with open(commands_list_file, 'r') as f:
                for i in f:
                    args_list.append((i.strip(), evm_dir, 1, True))

            multiprocess_running(cmd_run, args_list,
                                 args.num_threads, silence=False)

            cmd_string = "%s/EvmUtils/recombine_EVM_partial_outputs.pl --partitions partitions_list.out --output_file_name evm.out" % EVM_HOME
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            cmd_string = "%s/EvmUtils/convert_EVM_outputs_to_GFF3.pl --partitions partitions_list.out --output evm.out --genome %s" % (
                EVM_HOME, evm_input_genome_file)
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

            cmd_string = "find . -regex \".*evm.out.gff3\" -exec cat {} \; > EVM.all.gff3"
            cmd_run(cmd_string, cwd=evm_dir, silence=False)

        evm_output_gff = "/lustre/home/xuyuxing/Work/annotation_pipeline/plantanno_out/6.EVM/EVM.all.gff3"
        evm_input_genome_file = "/lustre/home/xuyuxing/Work/annotation_pipeline/plantanno_out/6.EVM/input.genome.fasta"

        from toolbiox.lib.common.genome.genome_feature2 import read_gff_file, Genome
        import numpy as np

        genome = Genome(genome_file=evm_input_genome_file,
                        gff_file=evm_output_gff)
        genome.genome_feature_parse()
        genome.build_gene_sequence()

        g_len_list = []
        c_len_list = []
        for g_id in genome.feature_dict['gene']:
            g = genome.feature_dict['gene'][g_id]
            g_len_list.append(g.length)
            c_len_list.append(len(g.model_cds_seq))

        percent_list = np.percentile(np.array(c_len_list), [
            10, 20, 30, 40, 50, 60, 70, 80, 90, 100])


if __name__ == "__main__":
    pass
