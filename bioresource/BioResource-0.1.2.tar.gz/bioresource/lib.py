import time
from bioresource.config import *
from toolbiox.lib.common.os import mkdir, cmd_run, have_file, get_file_name, multiprocess_running, rmdir, get_file_dir
from toolbiox.lib.common.fileIO import tsv_file_dict_parse_big
from toolbiox.lib.common.sqlite_command import store_dict_to_db, retrieve_dict_from_db, init_sql_db, sqlite_write, sqlite_select, pickle_dump_obj, pickle_load_obj, sqlite_update, check_sql_table, sql_table_row_num
from toolbiox.lib.xuyuxing.evolution.taxonomy import read_tax_name_record_dict_db, read_tax_record_dict_db, build_taxon_database, store_tax_record_into_sqlite
from toolbiox.lib.xuyuxing.base.common_command import log_print
from ftplib import FTP
import re
from retry import retry
import hashlib
from functools import cmp_to_key


class MetaData(object):
    def __init__(self, sqlite_db=None):
        self.sqlite_db = sqlite_db

    def store_sqlite_info(self, record_dict={}, **kwargs):
        # store data
        store_dict_to_db(record_dict, self.sqlite_db)
        if not "MetaInfo" in check_sql_table(self.sqlite_db):
            init_sql_db(self.sqlite_db, "MetaInfo", [
                        'key', 'value'], remove_old_db=False)

        # store attr
        used_key_set = set([i[0] for i in sqlite_select(
            self.sqlite_db, 'MetaInfo', column_list=['key'])])
        input_id_set = set(kwargs.keys())
        update_id_list = list(used_key_set & input_id_set)
        new_id_list = list(input_id_set - used_key_set)

        sqlite_update(self.sqlite_db, "MetaInfo", "key", "value", [
                      (i, pickle_dump_obj(kwargs[i])) for i in update_id_list])
        sqlite_write([(i, pickle_dump_obj(kwargs[i]))
                      for i in new_id_list], self.sqlite_db, "MetaInfo", ['key', 'value'])
        self.retrieve_sqlite_info()

    def retrieve_sqlite_info(self):
        for k, v in sqlite_select(self.sqlite_db, "MetaInfo"):
            setattr(self, k, pickle_load_obj(v))

    def get_record_list(self):
        return [i[0] for i in sqlite_select(self.sqlite_db, 'table_record', column_list=['id'])]

    def get_records(self, record_acc_id_list=[]):
        return retrieve_dict_from_db(self.sqlite_db, key_list=record_acc_id_list)

    def get_record_num(self):
        return sql_table_row_num(self.sqlite_db, 'table_record')


class RecordData(object):
    def __init__(self, acc_id=None, type=None, data_list=[], qualifiers={}, **kwargs):
        self.acc_id = acc_id
        self.type = type
        self.data_list = data_list
        self.qualifiers = qualifiers
        [setattr(self, k, kwargs[k]) for k in kwargs]


class BioData(object):
    def __init__(self, type=None, local_info=None, remote_info=None, md5=None, **kwargs):
        self.type = type
        self.local_info = local_info
        self.remote_info = remote_info
        self.md5 = md5
        [setattr(self, k, kwargs[k]) for k in kwargs]

    def download(self):
        pass

    def local_check(self):
        pass


def filter_taxid_by_top_taxon(tax_id_list, top_taxon, tax_sqldb_file):
    # exclude taxon by filter
    tax_record_db = read_tax_record_dict_db(
        tax_sqldb_file, tuple(tax_id_list))

    filtered_tax_list = []
    for t in tax_record_db:
        lineage_id_list = set([
            i[0] for i in tax_record_db[t].get_lineage])
        if top_taxon in lineage_id_list:
            filtered_tax_list.append(t)

    return filtered_tax_list


@retry(tries=3, delay=5)
def get_ncbi_genome_md5_file(ftp_path, record_dir):
    ftp_path = re.sub(r'.*ftp.ncbi.nlm.nih.gov', '', ftp_path)
    md5_file_path = os.path.join(record_dir, "md5checksums.txt")

    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect("ftp.ncbi.nlm.nih.gov")
    ftp.login()

    fp = open(md5_file_path, 'wb')
    bufsize = 1024
    ftp.retrbinary('RETR ' + ftp_path +
                   "/md5checksums.txt", fp.write, bufsize)
    fp.close()

    if not have_file(md5_file_path):
        raise ValueError("Failed get md5 file for %s" % ftp_path)

    ftp.close()

    return md5_file_path


def read_md5_file(md5_file):
    md5_info_dict = {}
    with open(md5_file, 'r') as f:
        for each_line in f:
            each_line = each_line.strip()
            info = each_line.split()
            file_name = re.sub(r'^\./', '', info[1])
            md5_string = info[0]
            md5_info_dict[file_name] = md5_string
    return md5_info_dict


def get_file_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


def ncbi_genome_cmp(x, y):
    key_rank = ["del_flag", "refseq_category",
                "assembly_level", "genome_rep"]

    sort_dict = {
        "del_flag": {"Good Record": 1, "Bad Record": 2},
        "refseq_category": {"reference genome": 1, "representative genome": 2, "na": 3},
        "assembly_level": {"Chromosome": 1, "Complete Genome": 2, "Scaffold": 3, "Contig": 4},
        "genome_rep": {"Full": 1, "Partial": 2},
    }

    compara_flag = 0
    for key_tmp in key_rank:
        x_key_tmp = x.qualifiers[key_tmp]
        y_key_tmp = y.qualifiers[key_tmp]
        if x_key_tmp == y_key_tmp:
            continue
        elif sort_dict[key_tmp][x_key_tmp] > sort_dict[key_tmp][y_key_tmp]:
            compara_flag = 1
            break
        elif sort_dict[key_tmp][x_key_tmp] < sort_dict[key_tmp][y_key_tmp]:
            compara_flag = -1
            break

    return compara_flag


class NCBIGenomeStore(object):

    def __init__(self, store_dir=None):
        self.store_dir = store_dir
        mkdir(self.store_dir, True)

        self.metafile_dir = os.path.join(self.store_dir, "metafiles")
        mkdir(self.metafile_dir, True)
        self.metadata_db_path = os.path.join(self.metafile_dir, "metadata.db")

        self.localdata_dir = os.path.join(self.store_dir, "localdata")
        mkdir(self.localdata_dir, True)
        self.localdata_db_path = os.path.join(
            self.localdata_dir, "localdata.db")

        if not have_file(self.metadata_db_path):
            self.renew_meta()

        self.metadata = MetaData(self.metadata_db_path)
        self.metadata.retrieve_sqlite_info()
        self.renew_time = self.metadata.renew_time
        self.taxon_db = self.metadata.taxon_db

        if not have_file(self.localdata_db_path):
            self.renew_local()

        self.localdata = MetaData(self.localdata_db_path)
        self.localdata.retrieve_sqlite_info()
        self.check_time = self.localdata.check_time

    def __str__(self):
        return "%d records in metadata (%s), %d records localizated (%s)" % (self.metadata.get_record_num(), self.renew_time, self.localdata.get_record_num(), self.check_time)

    __repr__ = __str__

    def __hash__(self):
        return hash(id(self))

    def download_records(self, top_taxon_id=None, acc_id_list=[], download_file_type=["genome", "gff", "cds", "pt"]):
        # get record
        meta_record_dict = self.get_records(
            top_taxon_id=top_taxon_id, acc_id_list=acc_id_list)

        # download
        wait_file_list = []
        for acc_id in meta_record_dict:
            r = meta_record_dict[acc_id]
            for d in r.data_list:
                if d.status == 'Failed' and d.type in download_file_type:
                    wait_file_list.append(d)
        log_print("\t\t%d files will download now" % len(wait_file_list))
        self.data_download(wait_file_list)

        # md5 check
        log_print("\t\tCheck md5")
        args_list = [(os.path.join(self.localdata_dir, d.local_info),)
                     for d in wait_file_list]
        mlt_out = multiprocess_running(get_file_md5, args_list, 20)
        file_md5_dict = {mlt_out[i]['args'][0]                         : mlt_out[i]['output'] for i in mlt_out}

        local_info_record_dict = {}
        for acc_id in meta_record_dict:
            r = meta_record_dict[acc_id]
            local_info_record_dict[acc_id] = {}
            for d in r.data_list:
                file_path = os.path.join(self.localdata_dir, d.local_info)
                if d.status == 'Failed':
                    if file_path in file_md5_dict and file_md5_dict[file_path] == d.md5:
                        d.status = 'OK'
                    else:
                        rmdir(file_path)

                local_info_record_dict[acc_id][d.type] = (
                    d.name, d.md5, d.status)

        log_print("\t\tWrite Sqlite DB")
        self.check_time = time.strftime("%Y-%m-%d %X", time.localtime())
        self.localdata = MetaData(self.localdata_db_path)
        self.localdata.store_sqlite_info(
            record_dict=local_info_record_dict, check_time=self.check_time)

    def data_download(self, data_list):
        log_print("\t\tBegin: download %d files from ncbi database" %
                  len(data_list))
        # start_time = time.time()

        num = 1
        for d in data_list:
            if d.status != 'OK' and d.status != 'Missed':
                ftp_url = d.remote_info
                log_print("\t\t downloading %s (%d/%d)" %
                          (d.name, num, len(data_list)))
                output_file = os.path.join(self.localdata_dir, d.local_info)
                rmdir(output_file)

                cmd_string = "wget -c -t 0 -o %s %s" % (output_file, ftp_url)
                cmd_run(cmd_string, cwd=get_file_dir(output_file))

            num += 1

        # ftp = FTP()
        # # ftp.set_debuglevel(2)
        # ftp.connect("ftp.ncbi.nlm.nih.gov")
        # ftp.login()

        # num = 0
        # rename_md5_list = []
        # for d in data_list:
        #     ftp_url = d.remote_info
        #     output_file = os.path.join(self.localdata_dir, d.local_info)

        #     round_time = time.time()
        #     num += 1
        #     if round_time - start_time > 10:
        #         log_print("\t\t\t%d/%d" % (num, len(data_list)))
        #         start_time = round_time

        #     ftp_url = re.sub(r'.*.ncbi.nlm.nih.gov', '', ftp_url)

        #     failed_flag = True
        #     retry = 0
        #     while failed_flag and retry < 5:
        #         try:
        #             log_print("\t\t downloading %s" % d.name)
        #             fp = open(output_file, 'wb')
        #             bufsize = 1024
        #             ftp.retrbinary('RETR ' + ftp_url, fp.write, bufsize)
        #             fp.close()
        #             if os.path.exists(output_file) and os.path.getsize(output_file) != 0:
        #                 rename_md5_list.append(output_file)
        #                 failed_flag = False
        #         except:
        #             ftp = FTP()
        #             # ftp.set_debuglevel(2)
        #             ftp.connect("ftp.ncbi.nlm.nih.gov")
        #             ftp.login()
        #             failed_flag = True
        #         retry += 1

        # ftp.close()

        log_print(
            "\t\tEnd: download all files for %d ncbi genome record" % len(data_list))

    def renew_meta(self):
        # env
        log_print("Begin: download metafiles from NCBI genome record")

        self.renew_time = time.strftime("%Y-%m-%d %X", time.localtime())
        log_print("renew time are rewrited as %s" % self.renew_time)

        mkdir(self.metafile_dir, False)

        # genome meta
        genome_meta_dict = {}
        for meta_file_name in NCBI_GENOME_METAFILE_DICT:
            ftp_path = NCBI_GENOME_METAFILE_DICT[meta_file_name]
            log_print("downloading %s" % ftp_path)
            local_file = os.path.join(
                self.metafile_dir, get_file_name(ftp_path))
            genome_meta_dict[meta_file_name] = local_file
            cmd_run("wget %s" % ftp_path, cwd=self.metafile_dir, silence=True)

        # taxon
        self.tax_db = os.path.join(self.metafile_dir, "taxon.db")
        taxon_tar_gz_file = os.path.join(
            self.metafile_dir, get_file_name(NCBI_TAXONOMY_DB))
        log_print("downloading %s" % NCBI_TAXONOMY_DB)
        cmd_run("wget %s" % NCBI_TAXONOMY_DB,
                cwd=self.metafile_dir, silence=True)
        log_print("formating Taxonomy database")
        cmd_run("tar -zxf %s" % taxon_tar_gz_file,
                cwd=self.metafile_dir, silence=True)
        tax_record_dict = build_taxon_database(self.metafile_dir)
        store_tax_record_into_sqlite(tax_record_dict, self.tax_db)

        # store
        log_print("formating metafile and store in sqlite database")
        record_dict = self.parse_metafile()
        self.metadata = MetaData(self.metadata_db_path)
        self.metadata.store_sqlite_info(
            record_dict, renew_time=self.renew_time, taxon_db=self.tax_db, genome_meta_dict=genome_meta_dict)

    def renew_local(self):
        log_print("Begin: check downloaded genome data")

        # read dir
        acc_id_list = [acc_id for acc_id in os.listdir(
            self.localdata_dir) if acc_id != 'localdata.db']
        record_dict = self.metadata.get_records(acc_id_list)

        log_print("Get %d records in local dir" % len(record_dict))

        args_list = []
        for acc_id in record_dict:
            r = record_dict[acc_id]
            down_dir = os.path.join(self.localdata_dir, acc_id)
            md5_file = os.path.join(down_dir, "md5checksums.txt")
            md5_info_dict = read_md5_file(md5_file)

            for d in r.data_list:
                if get_file_name(d.local_info) in md5_info_dict:
                    d.md5 = md5_info_dict[get_file_name(d.local_info)]
                else:
                    d.md5 = 'Missed'

                if d.md5 != 'Missed':
                    file_path = os.path.join(self.localdata_dir, d.local_info)
                    if have_file(file_path):
                        args_list.append((file_path,))

        log_print("Check md5 of %d files" % len(args_list))
        mlt_out = multiprocess_running(get_file_md5, args_list, 20)
        file_md5_dict = {mlt_out[i]['args'][0]                         : mlt_out[i]['output'] for i in mlt_out}

        local_info_record_dict = {}
        for acc_id in record_dict:
            r = record_dict[acc_id]
            local_info_record_dict[acc_id] = {}
            for d in r.data_list:
                file_path = os.path.join(self.localdata_dir, d.local_info)
                if d.md5 == 'Missed':
                    d.status = 'Missed'
                elif file_path in file_md5_dict and file_md5_dict[file_path] == d.md5:
                    d.status = 'OK'
                else:
                    d.status = 'Failed'
                local_info_record_dict[acc_id][d.type] = (
                    d.name, d.md5, d.status)

        if not have_file(self.localdata_db_path):
            rmdir(self.localdata_db_path)

        log_print("Write Sqlite DB")
        self.check_time = time.strftime("%Y-%m-%d %X", time.localtime())
        self.localdata = MetaData(self.localdata_db_path)
        self.localdata.store_sqlite_info(
            record_dict=local_info_record_dict, check_time=self.check_time)

    def parse_metafile(self):
        assembly_summary_refseq_file, assembly_summary_genbank_file = os.path.join(
            self.metafile_dir, "assembly_summary_refseq.txt"), os.path.join(self.metafile_dir, "assembly_summary_genbank.txt")

        col_name = ["assembly_accession", "bioproject", "biosample", "wgs_master", "refseq_category", "taxid",
                    "species_taxid", "organism_name", "infraspecific_name", "isolate", "version_status",
                    "assembly_level", "release_type", "genome_rep", "seq_rel_date", "asm_name", "submitter",
                    "gbrs_paired_asm", "paired_asm_comp", "ftp_path", "excluded_from_refseq",
                    "relation_to_type_material"]

        record_dict = {}
        # assembly_summary_refseq

        def info2record(info): return RecordData(acc_id=info[1]['assembly_accession'],
                                                 type='Genome',
                                                 data_list=[],
                                                 qualifiers=info[1],
                                                 taxon_id=info[1]['taxid'],
                                                 assembly_level=info[1]['assembly_level'],
                                                 refseq_category=info[1]['refseq_category'],
                                                 ftp_path=info[1]['ftp_path'],
                                                 long_acc_id=info[1]['ftp_path'].split(
            '/')[-1],
            excluded_from_refseq=info[1]['excluded_from_refseq'],
        )

        for info in tsv_file_dict_parse_big(assembly_summary_refseq_file, fieldnames=col_name):
            genome_record = info2record(info)
            record_dict[genome_record.acc_id] = genome_record

        # assembly_summary_genbank
        for info in tsv_file_dict_parse_big(assembly_summary_genbank_file, fieldnames=col_name):
            if not (info[1]['gbrs_paired_asm'] in record_dict or info[1]['assembly_accession'] in record_dict):
                genome_record = info2record(info)
                record_dict[genome_record.acc_id] = genome_record

        # add file info
        record_filter_dict = {}
        for acc_id in record_dict:
            genome_record = record_dict[acc_id]

            file_info = {
                "genome": genome_record.long_acc_id + "_genomic.fna.gz",
                "gff": genome_record.long_acc_id + "_genomic.gff.gz",
                "cds": genome_record.long_acc_id + "_cds_from_genomic.fna.gz",
                "pt": genome_record.long_acc_id + "_translated_cds.faa.gz"
            }

            genome_record.data_list = [BioData(name=file_info[t], type=t, local_info=os.path.join(
                acc_id, file_info[t]), remote_info=genome_record.ftp_path + "/" + file_info[t]) for t in file_info]

            if genome_record.ftp_path == 'na':
                continue

            record_filter_dict[acc_id] = genome_record

        return record_filter_dict

    def get_records(self, top_taxon_id=None, acc_id_list=[]):
        # get acc list
        if top_taxon_id:
            log_print("\t\tRead taxon db")
            record_dict = self.metadata.get_records()
            rec_tax_dict = {
                acc_id: record_dict[acc_id].taxon_id for acc_id in record_dict}
            del record_dict

            tax_id_list = list(set(rec_tax_dict[i] for i in rec_tax_dict))
            filtered_tax_list = list(set(filter_taxid_by_top_taxon(
                tax_id_list, top_taxon_id, self.metadata.taxon_db)))

            tax_rec_dict = {}
            for acc_id in rec_tax_dict:
                tax_id = rec_tax_dict[acc_id]
                tax_rec_dict.setdefault(tax_id, []).append(acc_id)

            used_tax_list = list(set(tax_rec_dict.keys())
                                 & set(filtered_tax_list))

            for t_id in used_tax_list:
                acc_id_list.extend(tax_rec_dict[t_id])

        acc_id_list = list(set(acc_id_list))

        if len(acc_id_list) == 0:
            acc_id_list = self.localdata.get_record_list()

        log_print("\t\t%d records will downloaded" % len(acc_id_list))

        # load file status
        log_print("\t\tLoading local data")
        meta_record_dict = self.metadata.get_records(acc_id_list)
        local_record_dict = self.localdata.get_records(acc_id_list)

        for acc_id in meta_record_dict:
            down_dir = os.path.join(self.localdata_dir, acc_id)
            mkdir(down_dir, True)

            r = meta_record_dict[acc_id]
            if acc_id in local_record_dict:
                for d in r.data_list:
                    file_name, md5, status = local_record_dict[acc_id][d.type]
                    if d.name == file_name:
                        d.status = status
                        d.md5 = md5
            else:
                ftp_path = r.qualifiers['ftp_path']
                md5_file = get_ncbi_genome_md5_file(ftp_path, down_dir)
                md5_info_dict = read_md5_file(md5_file)

                for d in r.data_list:
                    if d.name in md5_info_dict:
                        d.status = 'Failed'
                        d.md5 = md5_info_dict[d.name]
                    else:
                        d.status = 'Missed'
                        d.md5 = 'Missed'

        return meta_record_dict

    def ncbi_genome_chooser(self, record_dict, taxonomic_rank="genus", keep_no_rank=True):
        # step 1: Based on "gbrs_paired_asm" and "paired_asm_comp", I remove genbank assembly which paired with a refseq.
        #        Remove bad assembly that excluded_from_refseq is not empty.
        for accession_id in record_dict.keys():
            r = record_dict[accession_id]
            del_flag = 0
            if r.qualifiers['paired_asm_comp'] != "na":
                del_flag = 1
            if not r.qualifiers['excluded_from_refseq'] == "":
                del_flag = 1
            if r.qualifiers['ftp_path'] == "na":
                del_flag = 1
            if del_flag == 1:
                r.qualifiers['del_flag'] = "Bad Record"
            else:
                r.qualifiers['del_flag'] = "Good Record"

        # step 2: Choose a best assembly to represent a given taxonomic_rank (like a genus)
        # classified assemblies by taxonomic_rank or lower rank(when given rank not in a record)
        class_taxon_rank_dict = {}
        num_genus = 0
        num_no_genus = 0

        tax_record_db = read_tax_record_dict_db(self.metadata.taxon_db,
                                                tuple([record_dict[accession_id].taxon_id for accession_id in record_dict]))
        num = 0
        start_time = time.time()
        for accession_id in record_dict.keys():
            record = record_dict[accession_id]
            if record.taxon_id in tax_record_db:
                taxid_taxon = tax_record_db[record.taxon_id]

                if hasattr(taxid_taxon, taxonomic_rank):
                    num_genus = num_genus + 1
                    taxonomic_rank_tmp = getattr(taxid_taxon, taxonomic_rank)
                    setattr(record, taxonomic_rank, taxonomic_rank_tmp)
                    if not taxonomic_rank_tmp in class_taxon_rank_dict:
                        class_taxon_rank_dict[taxonomic_rank_tmp] = []
                    class_taxon_rank_dict[taxonomic_rank_tmp].append(record)
                else:
                    if keep_no_rank:
                        num_no_genus = num_no_genus + 1
                        setattr(record, taxonomic_rank, "None")
                        if not record.taxon_id in class_taxon_rank_dict:
                            class_taxon_rank_dict[record.taxon_id] = []
                        class_taxon_rank_dict[record.taxon_id].append(record)

            num = num + 1
            round_time = time.time()
            if round_time - start_time > 10:
                log_print("\t\t\t%d/%d" % (num, len(record_dict)))
                start_time = round_time

        # sort by sort_dict
        sorted_class_taxon_rank_dict = {}
        for each_taxon in class_taxon_rank_dict:
            assembly_list = class_taxon_rank_dict[each_taxon]
            sorted_assembly_list = sorted(
                assembly_list, key=cmp_to_key(ncbi_genome_cmp))
            sorted_class_taxon_rank_dict[each_taxon] = sorted_assembly_list

        # def print_assembly_list(assembly_list,tax_id):
        #    key_rank = ["group", "refseq_category", "assembly_level", "genome_rep"]
        #    for i in assembly_list:
        #        printer = tax_id+"\t"
        #        for j in key_rank:
        #            printer = printer + getattr(i, j) + ";"
        #        print printer
        #
        # for each_taxon in sorted_class_taxon_rank_dict:
        #    print_assembly_list(sorted_class_taxon_rank_dict[each_taxon],each_taxon)

        return sorted_class_taxon_rank_dict


#######
if __name__ == '__main__':
    # NCBI genome
    from bioresource import NCBIGenomeStore

    # build a new NCBI genome store
    db_path = '/lustre/home/xuyuxing/Database/NCBI/genome'
    ncbi_genome_store = NCBIGenomeStore(db_path)
    # renew metadata
    ncbi_genome_store.renew_meta()
    # renew local (when you download file by yourself)
    ncbi_genome_store.renew_local()
    # download by taxon
    taxon_id = '3398'  # flowering plants
    taxon_id = '4751'  # fungi
    ncbi_genome_store.download_records(top_taxon_id=taxon_id)
    # download by acc id
    acc_id_list = ['GCA_003260385.1', 'GCA_001974805.1']
    ncbi_genome_store.download_records(
        acc_id_list=acc_id_list, download_file_type=["pt", "gff"])
    ncbi_genome_store.get_records(acc_id_list=acc_id_list)

    # get records from local store
    db_path = '/lustre/home/xuyuxing/Database/NCBI/genome'
    ncbi_genome_store = NCBIGenomeStore(db_path)

    taxon_id = '3398'  # flowering plants
    plant_record_dict = ncbi_genome_store.get_records(top_taxon_id=taxon_id)
    plant_genus_dict = ncbi_genome_store.ncbi_genome_chooser(plant_record_dict, taxonomic_rank="genus", keep_no_rank=True)

    # NCBI SRA
    # go to https://www.ncbi.nlm.nih.gov/sra/ to search "flowering plants"[orgn:__txid3398], and use "Send to" to get FULL XML, named SraExperimentPackage.xml


# #################


# class GenomeMetaData(object):
#     def __init__(self, name=None, source=None, type=None, data=None, metadata_file_list=[], sqlite_db=None):
#         pass


# class GenomeRecord(object):
#     """
#     Genome_record is a class for each record in genome database.
#     """

#     def __init__(self, db_access_id, taxon_id, download_info=None, db_name=None, other_info=None):
#         self.db_access_id = db_access_id
#         self.taxon_id = taxon_id
#         self.db_name = db_name
#         self.other_info = other_info
#         self.download_info = download_info


# def jgi_Portal_ID_get(Portal_ID_raw):
#     return re.findall("\"(.*)\"", Portal_ID_raw.split(",")[1])[0]


# def jgi_Taxonomy_ID_get(genome_projects_record):
#     """
#     some of record in JGI genome_project.csv file have very long taxonomy id,
#     because they are repeated by many Sequencing Project ID
#     """
#     seq_project_count = len(re.findall(
#         r'(\S+)', genome_projects_record["Sequencing Project ID"]))
#     tax_id_raw_len = len(genome_projects_record["Taxonomy ID"])

#     if seq_project_count == 0:
#         return genome_projects_record["Taxonomy ID"]

#     if tax_id_raw_len % seq_project_count == 0:
#         tax_id_len = int(tax_id_raw_len / seq_project_count)
#         split_list = re.findall(
#             '.{%d}' % tax_id_len, genome_projects_record["Taxonomy ID"])
#         if len(list(set(split_list))) == 1:
#             return split_list[0]
#         else:
#             return genome_projects_record["Taxonomy ID"]
#     return genome_projects_record["Taxonomy ID"]


# def jgi_pull_info(user_name, passwd, cookie_path, output_xml, Portal_ID, directly_download):
#     cmd_string = "curl 'https://genome.jgi.doe.gov/portal/ext-api/downloads/get-directory?organism=%s' -b %s > %s" % (
#         Portal_ID, cookie_path, output_xml)

#     if directly_download is False:
#         return cmd_string

#     lib.common.os.cmd_run(cmd_string)

#     if os.path.exists(output_xml) and os.path.getsize(output_xml) != 0:
#         return output_xml
#     else:
#         login_string = "curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=%s' --data-urlencode 'password=%s' -c %s > /dev/null" % (
#             user_name, passwd, cookie_path)
#         lib.common.os.cmd_run(login_string)
#         lib.common.os.cmd_run(cmd_string)
#         return output_xml


# def jgi_pull_file(user_name, passwd, cookie_path, output_file, want_url, directly_download):
#     cmd_string = "curl '%s' -b %s > %s" % (
#         want_url.replace("&amp;", "&"), cookie_path, output_file)

#     if directly_download is False:
#         return cmd_string

#     lib.common.os.cmd_run(cmd_string)

#     if os.path.exists(output_file) and os.path.getsize(output_file) != 0:
#         return output_file
#     else:
#         login_string = "curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=%s' --data-urlencode 'password=%s' -c %s > /dev/null" % (
#             user_name, passwd, cookie_path)
#         lib.common.os.cmd_run(login_string)
#         lib.common.os.cmd_run(cmd_string)
#         return output_file


# def jgi_files_download(ftp_list, output_list, user_name, passwd, cookie_path):
#     for tmp_index in range(len(ftp_list)):
#         ftp_url = ftp_list[tmp_index]
#         output_file = output_list[tmp_index]

#         jgi_pull_file(user_name, passwd, cookie_path,
#                       output_file, ftp_url, True)


# def jgi_uniq_file_record(file_list):
#     def good_choose(file_list_tmp):
#         for file_record in file_list_tmp:
#             file_url, file_name, file_md5, tag_tmp, stat, file_type, file_size = file_record
#             match_url = re.match(r'.*_JAMO.*', file_url)
#             if match_url:
#                 return file_record
#         return file_list_tmp[0]

#     file_dir = {}
#     for file_record in file_list:
#         file_url, file_name, file_md5, tag_tmp, stat, file_type, file_size = file_record
#         if not file_name in file_dir:
#             file_dir[file_name] = []
#         file_dir[file_name].append(file_record)

#     output_list = []
#     for file_name in file_dir:
#         file_list = file_dir[file_name]
#         output_list.append(good_choose(file_list))

#     return output_list


# def jgi_metadata_xml_read(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()

#     file_info_dict = {}
#     md5_info_dict = {}
#     url_info_dict = {}
#     for file_tmp in root.iter("file"):
#         if "filename" in file_tmp.attrib:
#             file_name = file_tmp.attrib["filename"]
#         else:
#             continue

#         if "url" in file_tmp.attrib:
#             match_url = re.match(r'.*&url=(.*)', file_tmp.attrib["url"])
#             if match_url:
#                 file_url = "https://genome.jgi.doe.gov/portal" + \
#                     match_url.group(1)
#             else:
#                 file_url = "https://genome.jgi.doe.gov" + \
#                     file_tmp.attrib["url"]
#             url_info_dict[file_name] = file_url
#         else:
#             continue

#         if "md5" in file_tmp.attrib:
#             file_md5 = file_tmp.attrib["md5"]
#             md5_info_dict[file_name] = file_md5
#         else:
#             file_md5 = ""

#         if "sizeInBytes" in file_tmp.attrib:
#             file_size = file_tmp.attrib["sizeInBytes"]
#         else:
#             file_size = ""

#         file_type = ""
#         match_gff = re.match(
#             r"^(\S+)_GeneCatalog_genes_(\d+)\.gff.gz", file_name)
#         if match_gff:
#             tag_tmp = match_gff.groups(1)[0]
#             version_tmp = match_gff.groups(1)[1]
#             file_type = "gff_file"
#         match_cds = re.match(
#             r"^(\S+)_GeneCatalog_CDS_(\d+)\.fasta.gz", file_name)
#         if match_cds:
#             tag_tmp = match_cds.groups(1)[0]
#             version_tmp = match_cds.groups(1)[1]
#             file_type = "cds_file"
#         match_pt = re.match(
#             r"^(\S+)_GeneCatalog_proteins_(\d+)\.aa.fasta.gz", file_name)
#         if match_pt:
#             tag_tmp = match_pt.groups(1)[0]
#             version_tmp = match_pt.groups(1)[1]
#             file_type = "pt_file"
#         match_genome = re.match(
#             r"^(\S+)_AssemblyScaffolds.fasta.gz", file_name)
#         if match_genome:
#             tag_tmp = match_genome.groups(1)[0]
#             file_type = "genome_file"

#         if file_type == "":
#             continue

#         if tag_tmp not in file_info_dict:
#             file_info_dict[tag_tmp] = {}
#             file_info_dict[tag_tmp]["genome_file"] = None
#             file_info_dict[tag_tmp]["annotation"] = {}
#         if file_type == "genome_file":
#             file_info_dict[tag_tmp]["genome_file"] = (
#                 file_url, file_name, file_md5, tag_tmp, "", "genome_file", file_size)
#         else:
#             if version_tmp not in file_info_dict[tag_tmp]["annotation"]:
#                 file_info_dict[tag_tmp]["annotation"][version_tmp] = []
#             file_info_dict[tag_tmp]["annotation"][version_tmp].append(
#                 (file_url, file_name, file_md5, tag_tmp, "", file_type, file_size))
#             file_info_dict[tag_tmp]["annotation"][version_tmp] = jgi_uniq_file_record(
#                 file_info_dict[tag_tmp]["annotation"][version_tmp])

#     # choose newest version

#     for tag_tmp in file_info_dict:
#         file_info = {
#             "genome_file": None,
#             "gff_file": None,
#             "cds_file": None,
#             "pt_file": None
#         }

#         genome_file_info = file_info_dict[tag_tmp]["genome_file"]
#         if not genome_file_info is None:

#             g_file_name = genome_file_info[1]

#             if g_file_name in md5_info_dict:
#                 g_file_md5 = md5_info_dict[g_file_name]
#             else:
#                 g_file_md5 = None

#             if g_file_name in url_info_dict:
#                 g_file_url = url_info_dict[g_file_name]
#             else:
#                 g_file_url = None

#             file_info["genome_file"] = (g_file_name, g_file_url, g_file_md5)

#         version_keys = list(file_info_dict[tag_tmp]['annotation'].keys())

#         if len(version_keys) != 0:

#             version_keys = [int(i) for i in version_keys]
#             newest_version = str(sorted(version_keys, reverse=True)[0])

#             for i in file_info_dict[tag_tmp]["annotation"][newest_version]:
#                 file_name = i[1]

#                 if file_name in md5_info_dict:
#                     file_md5 = md5_info_dict[file_name]
#                 else:
#                     file_md5 = None

#                 if file_name in url_info_dict:
#                     file_url = url_info_dict[file_name]
#                 else:
#                     file_url = None

#                 file_info[i[5]] = (file_name, file_url, file_md5)

#         file_info_dict[tag_tmp] = file_info

#     return file_info_dict


# def get_ncbi_md5_list(ftp_dir, tmp_file="/tmp/tmp_md5.txt"):
#     """
#     ftp_dir = '/genomes/all/GCA/000/001/215/GCA_000001215.4_Release_6_plus_ISO1_MT'
#     """

#     ftp_dir = re.sub(r'ftp://ftp.ncbi.nlm.nih.gov', '', ftp_dir)

#     ftp = FTP()
#     # ftp.set_debuglevel(2)
#     ftp.connect("ftp.ncbi.nlm.nih.gov")
#     ftp.login()

#     try:
#         fp = open(tmp_file, 'wb')
#         bufsize = 1024
#         ftp.retrbinary('RETR ' + ftp_dir +
#                        "/md5checksums.txt", fp.write, bufsize)
#         fp.close()

#         md5_info_dict = {}
#         with open(tmp_file, 'r') as f:
#             for each_line in f:
#                 each_line = each_line.strip()
#                 info = each_line.split()
#                 file_name = re.sub(r'^\./', '', info[1])
#                 md5_string = info[0]
#                 md5_info_dict[file_name] = md5_string

#         os.remove(tmp_file)

#         return md5_info_dict
#     except:
#         return "error"


# def genome_record_exclude_by_taxon(record_dict, tax_sqldb_file, taxon_filter):
#     # exclude taxon by filter
#     used_taxon_id_list = list(
#         set([record_dict[i].taxon_id for i in record_dict]))
#     tax_record_db = read_tax_record_dict_db(
#         tax_sqldb_file, tuple(used_taxon_id_list))

#     rec_id_list = list(record_dict.keys())
#     for i in rec_id_list:
#         if record_dict[i].taxon_id not in tax_record_db:
#             del record_dict[i]
#         else:
#             lineage_id_list = [
#                 i[0] for i in tax_record_db[record_dict[i].taxon_id].get_lineage]
#             if len(set(lineage_id_list) & set(taxon_filter)) == 0:
#                 del record_dict[i]

#     return record_dict


# def build_data_index(input_info_list, database_name, tax_sqldb_file, taxon_filter):
#     """
#     most database will give a index file to tell me, how many genome they have
#     """

#     if database_name == 'ncbi':
#         """
#         "assembly_summary_refseq_file" and "assembly_summary_genbank_file" as input
#         """

#         assembly_summary_refseq_file, assembly_summary_genbank_file, md5sum_huge_file = input_info_list

#         col_name = ["assembly_accession", "bioproject", "biosample", "wgs_master", "refseq_category", "taxid",
#                     "species_taxid", "organism_name", "infraspecific_name", "isolate", "version_status",
#                     "assembly_level", "release_type", "genome_rep", "seq_rel_date", "asm_name", "submitter",
#                     "gbrs_paired_asm", "paired_asm_comp", "ftp_path", "excluded_from_refseq",
#                     "relation_to_type_material"]

#         record_dict = {}

#         parse_file_db = tsv_file_dict_parse(
#             assembly_summary_refseq_file, fieldnames=col_name)
#         for i in parse_file_db:
#             parse_file_db[i]['group'] = "refseq"
#             gr_tmp = GenomeRecord(parse_file_db[i]['assembly_accession'], parse_file_db[i]["species_taxid"],
#                                   None, "ncbi", parse_file_db[i])
#             record_dict[parse_file_db[i]['assembly_accession']] = gr_tmp

#         parse_file_db = tsv_file_dict_parse(
#             assembly_summary_genbank_file, fieldnames=col_name)
#         for i in parse_file_db:
#             if parse_file_db[i]['paired_asm_comp'] == "na" and parse_file_db[i]['excluded_from_refseq'] == "" and \
#                     parse_file_db[i]['ftp_path'] != "na":
#                 parse_file_db[i]['group'] = "genbank"
#                 gr_tmp = GenomeRecord(parse_file_db[i]['assembly_accession'], parse_file_db[i]["species_taxid"],
#                                       None, "ncbi", parse_file_db[i])
#                 record_dict[parse_file_db[i]['assembly_accession']] = gr_tmp

#         # exclude taxon by filter
#         record_dict = genome_record_exclude_by_taxon(
#             record_dict, tax_sqldb_file, taxon_filter)

#         # add download info
#         if not os.path.exists(md5sum_huge_file):
#             ftp_dir_list = [record_dict[i].other_info['ftp_path']
#                             for i in record_dict]
#             # ftp_dir_list = ftp_dir_list[0:100]
#             get_many_ncbi_md5_list(
#                 ftp_dir_list, md5sum_huge_file, tmp_dir="/tmp/tmp_md5")

#         md5_info_dict = {}
#         with open(md5sum_huge_file, 'r') as f:
#             for each_line in f:
#                 each_line = each_line.strip()
#                 info = each_line.split()
#                 file_name = re.sub(r'^\./', '', info[1])
#                 md5_string = info[0]
#                 md5_info_dict[file_name] = md5_string

#         good_num = 0
#         bad_num = 0
#         for rec_id in record_dict:
#             long_acc = record_dict[rec_id].other_info['ftp_path'].split(
#                 '/')[-1]

#             ftp_path = record_dict[rec_id].other_info['ftp_path']

#             file_info = {
#                 "genome_file": long_acc + "_genomic.fna.gz",
#                 "gff_file": long_acc + "_genomic.gff.gz",
#                 "cds_file": long_acc + "_cds_from_genomic.fna.gz",
#                 "pt_file": long_acc + "_translated_cds.faa.gz"
#             }

#             for i in file_info:
#                 if file_info[i] in md5_info_dict:
#                     file_tuple = (
#                         file_info[i], ftp_path + "/" + file_info[i], md5_info_dict[file_info[i]])
#                     file_info[i] = file_tuple
#                     good_num += 1
#                 else:
#                     file_info[i] = None
#                     bad_num += 1

#             record_dict[rec_id].download_info = file_info

#         return record_dict

#     elif database_name == 'jgi':
#         """
#         "genome-projects.csv" and xml file like "fungi.xml" as input
#         """

#         # read "fungi.xml" like file for record download info
#         metadata_xml_path = input_info_list[1]
#         file_info_dict = jgi_metadata_xml_read(metadata_xml_path)

#         # read "genome-projects.csv" for record speci info

#         col_name = ["Project Name", "Principal Investigator", "Scientific Program", "Product Name", "Status",
#                     "Status Date", "User Program", "Proposal", "JGI Project Id", "Taxonomy ID", "NCBI Project Id",
#                     "Genbank", "ENA", "SRA", "Sequencing Project ID", "Analysis project ID", "Project Manager",
#                     "Portal ID", "IMG Portal", "Mycocosm Portal", "Phytozome Portal"]

#         genome_projects_csv_file = input_info_list[0]

#         record_dict = {}

#         parse_file_db = tsv_file_dict_parse(
#             genome_projects_csv_file, fieldnames=col_name, seq=",", ignore_head_num=1)
#         for i in parse_file_db:
#             record_id = jgi_Portal_ID_get(parse_file_db[i]["Portal ID"])
#             record_species_taxid = jgi_Taxonomy_ID_get(parse_file_db[i])

#             if record_species_taxid == "":
#                 continue

#             if record_id not in file_info_dict:
#                 continue

#             gr_tmp = GenomeRecord(record_id, record_species_taxid,
#                                   file_info_dict[record_id], 'jgi', parse_file_db[i])
#             record_dict[record_id] = gr_tmp

#         # exclude taxon by filter
#         record_dict = genome_record_exclude_by_taxon(
#             record_dict, tax_sqldb_file, taxon_filter)

#         return record_dict


# def class_genome_record_by_rank(record_dict, taxon_rank, tax_sqldb_file):
#     used_taxon_id_list = list(
#         set([record_dict[i].taxon_id for i in record_dict]))
#     tax_record_db = read_tax_record_dict_db(
#         tax_sqldb_file, tuple(used_taxon_id_list))

#     record_in_rank = {}
#     record_in_rank['other'] = []
#     for gr_id in record_dict:
#         gr_tmp = record_dict[gr_id]
#         gr_taxon = tax_record_db[gr_tmp.taxon_id]
#         if hasattr(gr_taxon, taxon_rank):
#             taxonomic_rank_tmp = getattr(gr_taxon, taxon_rank)
#             if taxonomic_rank_tmp not in record_in_rank:
#                 record_in_rank[taxonomic_rank_tmp] = []
#             record_in_rank[taxonomic_rank_tmp].append(gr_tmp)
#         else:
#             record_in_rank['other'].append(gr_tmp)

#     return record_in_rank


# if __name__ == '__main__':
#     from toolbiox.lib.common.os import mkdir
#     from toolbiox.lib.xuyuxing.evolution.taxonomy import build_taxon_database, store_tax_record_into_sqlite

#     # normal
#     work_dir = "/lustre/home/xuyuxing/Work/Gel/HGT"
#     mkdir(work_dir, True)

#     path_for_taxonomy = "/lustre/home/xuyuxing/Work/Gel/HGT/taxdump"
#     tax_db_file = "/lustre/home/xuyuxing/Work/Gel/HGT/taxdump/tax_xyx.db"

#     tax_record_dict = build_taxon_database(path_for_taxonomy)
#     store_tax_record_into_sqlite(tax_record_dict, tax_db_file)

#     # build record index
#     # ncbi
#     """
#     assembly_summary file ("assembly_summary_genbank.txt" and "assembly_summary_refseq.txt") and genome size file from NCBI.
#     ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_refseq.txt
#     ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/assembly_summary_genbank.txt
#     ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz (need decompressed)
#     ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/species_genome_size.txt.gz (need decompressed)
#     """

#     assembly_summary_refseq_file = '/lustre/home/xuyuxing/Work/Gel/HGT/assembly_summary_refseq.txt'
#     assembly_summary_genbank_file = '/lustre/home/xuyuxing/Work/Gel/HGT/assembly_summary_genbank.txt'
#     md5sum_huge_file = '/lustre/home/xuyuxing/Work/Gel/HGT/md5sum_huge_file.txt'

#     ncbi_fungi_record_dict = build_data_index(
#         [assembly_summary_refseq_file, assembly_summary_genbank_file, md5sum_huge_file], 'ncbi', tax_db_file, ['4751'])

#     # jgi
#     jgi_user_name = "xuyuxing14@mails.ucas.ac.cn"
#     jgi_passwd = "HGTrunning123"
#     metadata_key_words = "fungal-program-all"
#     genome_projects_csv_file = "/lustre/home/xuyuxing/Work/Gel/HGT/genome-projects.csv"

#     jgi_dir = work_dir + "/jgi"
#     mkdir(jgi_dir, True)
#     cookie_path = work_dir + "/jgi/cookies"
#     # metadata_xml_path = work_dir + "/jgi/fungi.xml"
#     metadata_xml_path = "/lustre/home/xuyuxing/Work/Gel/HGT/jgi/fungal-program-all.xml"

#     # get fungi.xml
#     jgi_pull_info(jgi_user_name, jgi_passwd, cookie_path,
#                   metadata_xml_path, "fungal-program-all", True)

#     # build index
#     jgi_fungi_record_dict = build_data_index([genome_projects_csv_file, metadata_xml_path], 'jgi', tax_db_file,
#                                              ['4751'])

#     # merge ncbi and jgi database
#     from toolbiox.lib.xuyuxing.base.common_command import merge_dict

#     record_dict = merge_dict(
#         [ncbi_fungi_record_dict, jgi_fungi_record_dict], False)

#     record_in_genus = class_genome_record_by_rank(
#         record_dict, 'genus', tax_db_file)

#     # download files
#     Am_list = record_in_genus['47424']

#     Am_jgi_data = {i.db_access_id: i.download_info['pt_file'] for i in Am_list if
#                    i.db_name == 'jgi' and not i.download_info['pt_file'] is None}
#     Am_ncbi_data = {i.db_access_id: i.download_info['pt_file'] for i in Am_list if
#                     i.db_name == 'ncbi' and not i.download_info['pt_file'] is None}

#     # download ncbi data
#     ncbi_data_dir = "/lustre/home/xuyuxing/Work/Gel/HGT/ncbi_am"
#     for i in Am_ncbi_data:
#         file_name, download_url, md5sum = Am_ncbi_data[i]
#         store_file = ncbi_data_dir + "/" + file_name
#         Am_ncbi_data[i] = (file_name, download_url, md5sum, store_file)

#     Am_ncbi_url_list = [Am_ncbi_data[i][1] for i in Am_ncbi_data]
#     Am_ncbi_file_list = [Am_ncbi_data[i][3] for i in Am_ncbi_data]

#     ncbi_files_download(Am_ncbi_url_list, Am_ncbi_file_list)

#     # download jgi data
#     jgi_data_dir = "/lustre/home/xuyuxing/Work/Gel/HGT/jgi_am"
#     for i in Am_jgi_data:
#         file_name, download_url, md5sum = Am_jgi_data[i]
#         store_file = jgi_data_dir + "/" + file_name
#         Am_jgi_data[i] = (file_name, download_url, md5sum, store_file)

#     Am_jgi_url_list = [Am_jgi_data[i][1] for i in Am_jgi_data]
#     Am_jgi_file_list = [Am_jgi_data[i][3] for i in Am_jgi_data]

#     jgi_user_name = "xuyuxing14@mails.ucas.ac.cn"
#     jgi_passwd = "HGTrunning123"
#     cookie_path = "/lustre/home/xuyuxing/Work/Gel/HGT/jgi/cookies"
#     jgi_files_download(Am_jgi_url_list, Am_jgi_file_list,
#                        jgi_user_name, jgi_passwd, cookie_path)
