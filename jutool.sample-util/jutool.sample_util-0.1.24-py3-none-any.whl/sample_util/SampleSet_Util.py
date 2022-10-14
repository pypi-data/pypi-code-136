import time
from code_util.log import process_bar_iter
from sample_util.SampleSet import SampleSet
from sample_util.NLSampleSource import NLSampleSourceBase
from sample_util.NLSampleSource import LocalDisk_NLSampleSource


def splitset_by_labeltype_average(samplesource: NLSampleSourceBase, ori_set_name: str, get_label_type_func,
                                  set_count_dic: {}):
    label_type_dic = {}

    meta_data = samplesource.get_metadata_keys(ori_set_name)

    max_count_of_all_set = 0

    for new_set in set_count_dic.keys():
        samplesource.create_new_set(new_set, f"split from {ori_set_name}", ["split"], meta_data['label_keys'],
                                    ori_set_name, "")
        max_count_of_all_set += set_count_dic[new_set]

    for item in SampleSet(samplesource, ori_set_name).shuffle():
        lable = get_label_type_func(item)
        if lable is None:
            continue
        if lable not in label_type_dic:
            label_type_dic[lable] = []
        if len(label_type_dic[lable]) > max_count_of_all_set:
            continue
        label_type_dic[lable].append(item)

    pointers = [(x, 0) for x in label_type_dic.keys()]
    index_pointer = 0
    for new_set in set_count_dic.keys():
        name = f"{ori_set_name}_{new_set}"
        for _ in range(set_count_dic[new_set]):
            point_data = pointers[index_pointer]
            newdata = label_type_dic[point_data[0]][point_data[1]]
            samplesource.add_row(name, newdata)
            # add pointer
            pointers[index_pointer] = (point_data[0], point_data[1] + 1)
            index_pointer += 1
            if index_pointer >= len(label_type_dic.keys()):
                index_pointer = 0
    samplesource.flush()

    return [key for key in label_type_dic.keys()]


def CopySet(samplesource: NLSampleSourceBase, ori_set_name: str, new_samplesource: NLSampleSourceBase, new_name: str,
            new_description: str, new_tags: [str], new_lables: [str]):
    new_samplesource.create_new_set(new_name, new_description, new_tags, new_lables)
    for item in process_bar_iter(SampleSet(samplesource, ori_set_name), f"Copy {ori_set_name} -> {new_name}"
            , samplesource.get_set_count(ori_set_name)):
        new_samplesource.add_row(new_name, item)
