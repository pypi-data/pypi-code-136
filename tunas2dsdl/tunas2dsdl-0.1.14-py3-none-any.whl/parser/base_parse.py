import json
from ..io import HardDiskBackend, FileIO
from abc import abstractmethod
from collections import defaultdict
from ..general import ClassDomain, Label
from tqdm import tqdm


class BaseParse:
    INSTANCE_SEG_ANN_TYPE = "polygon"
    DETECTION_ANN_TYPE = "box2d"
    PARENT_PATTERN = "Parent"
    SEMANTIC_SEG_ANN_TYPE = "semantic_seg_map"

    def __init__(self, data_info_file, ann_file, separate_flag, dataset_name=None, file_client=None):
        if file_client:
            self.file_client = file_client
        else:
            self.file_client = HardDiskBackend()
        self.separate_flag = separate_flag
        self._dataset_name = dataset_name
        self._data_info_file = data_info_file
        self._annotation_file = ann_file
        self._data_info = self._read_json(data_info_file)
        self._annotation_info = self._read_json(ann_file)
        self._meta_info = self.parse_meta_info()
        self._parent_class_domain, self._class_domain, self.raw_class_info, self.task_uid_map = self.parse_class_domain()  # 父类的class domain和子类的class domain
        try:
            import dsdl
            dsdl_version = dsdl.__version__
        except Exception as e:
            dsdl_version = None
        self._dsdl_version_info = {"$dsdl-version": str(dsdl_version)}
        self._struct_defs, self._domain_defs, self._samples = self.parse_ann_info()

    @staticmethod
    def parse_domain_name(_uid):
        _type, _name, _source = _uid.split("$")
        _domain_name = FileIO.clean(f"{_name} {_type} ClassDom")
        _parent_domain_name = FileIO.clean(f"{_name} {_type} {BaseParse.PARENT_PATTERN} ClassDom")
        return _domain_name, _parent_domain_name

    @abstractmethod
    def parse_ann_info(self):
        pass

    def parse_class_domain(self):
        """
        return:
            uid2domain_map: {task_uid: class domain obj}
            uid2parent_map: {task_uid: parent domain obj}
            raw_class_info: {task_uid: {category_id: <category_info>}}
            map_dic: {task_uid: true_task_uid}
        """
        raw_class_info = defaultdict(dict)
        check_class_info = defaultdict(dict)
        task_uids = set()
        for task in tqdm(self._data_info['tasks'], desc="parsing class domain"):
            task_type, catalog, task_name, ann_source = task['type'], task['catalog'], task['name'], task['source']
            task_uid = f"{task_type}${task_name}${ann_source}"
            task_uids.add(task_uid)
            for label_info in catalog:
                category_id, category_name = label_info["category_id"], label_info["category_name"]
                raw_class_info[task_uid][category_id] = label_info
                check_class_info[task_uid][category_id] = category_name

        map_dic = {_: _ for _ in task_uids}  # 全部对应了自己
        checked_lst = []
        for task_uid_a in task_uids:
            if task_uid_a not in checked_lst:
                checked_lst.append(task_uid_a)
            else:
                continue
            a_map = check_class_info[task_uid_a]
            for task_uid_b in task_uids:
                b_map = check_class_info[task_uid_b]
                if a_map == b_map:
                    map_dic[task_uid_b] = task_uid_a
                    if task_uid_b not in checked_lst:
                        checked_lst.append(task_uid_b)

        uid2domain_map = dict()
        uid2parent_map = dict()

        for task_uid in task_uids:
            true_task_uid = map_dic[task_uid]
            if true_task_uid in uid2domain_map and true_task_uid in uid2parent_map:
                uid2domain_map[task_uid] = uid2domain_map[true_task_uid]
                uid2parent_map[task_uid] = uid2parent_map[true_task_uid]
                continue
            domain_name, parent_domain_name = self.parse_domain_name(true_task_uid)
            task_raw_info = raw_class_info[true_task_uid]
            class_domain = ClassDomain(domain_name)
            parent_domain = ClassDomain(parent_domain_name)
            uid2domain_map[task_uid] = class_domain
            uid2parent_map[task_uid] = parent_domain

            for label_info in task_raw_info.values():
                category_id, category_name = label_info['category_id'], label_info['category_name']
                label_obj = Label(category_name)
                if label_obj in class_domain:
                    continue
                class_domain.add_label(label_obj)
                for supercategory_name in label_info.get("supercategories", []):
                    super_label = Label(supercategory_name)
                    if super_label not in parent_domain:
                        parent_domain.add_label(super_label)
                    label_obj.add_supercategory(super_label)  # 添加父类
            if parent_domain:
                class_domain.set_parent(parent_domain)

        return uid2parent_map, uid2domain_map, raw_class_info, map_dic

    def parse_meta_info(self):
        """
        提取数据集元信息
        :return: 元信息字典
        """
        meta_info = {k: v for k, v in self._data_info.items() if k not in ("tasks", "statistics")}
        meta_info["sub_dataset_name"] = self._annotation_info["sub_dataset_name"]
        if not self._dataset_name:
            self._dataset_name = meta_info["dataset_name"]
        return meta_info

    def _read_json(self, file, encoding="utf-8"):
        bytes_info = self.file_client.get(file)
        try:
            text = bytes_info.decode(encoding)
        except Exception as e:
            raise RuntimeError(f"Failed to read '{file}'. {e}") from None

        try:
            json_info = json.loads(text)
        except Exception as e:
            raise RuntimeError(f"Failed to load JSON file '{file}'. {e}") from None
        return json_info

    @property
    def struct_defs(self):
        """
        dsdl的struct定义字典组成的列表
        """
        return self._struct_defs

    @property
    def samples(self):
        """
        dsdl的data字段下的内容，为一个字典，有sample-type域samples字段，samples包含了样本列表
        """
        return self._samples

    @property
    def sample_info(self):
        """
        tunas v0.3的annotation的json文件的原始内容
        """
        return self._annotation_info

    @property
    def class_domain_info(self):
        """
        dsdl的class_domain的定义字典
        """
        return self._domain_defs

    @property
    def meta_info(self):
        """
        dsdl的元信息内容
        """
        return self._meta_info

    @property
    def data_info_file(self):
        """
        返回tunas v0.3 dataset_info.json的文件路径
        """
        return self._data_info_file

    @property
    def annotation_file(self):
        """
        返回tunas v0.3 的标注文件json文件的路径
        """
        return self._annotation_file

    @property
    def dsdl_version(self):
        """
        dsdl的版本信息字典
        """
        return self._dsdl_version_info
