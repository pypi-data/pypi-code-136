from ..general import ClassDomain, Label, Field, Struct, DataSample, Util
from tqdm import tqdm
from ..io import FileIO
from .base_parse import BaseParse


class DetectionParse(BaseParse):

    def parse_class_domain(self):
        """
        提取class domain相关的信息
        :return: 父类class domain对象，子类class domain对象，class原始信息字典
        """
        class_domain = ClassDomain(FileIO.clean(f"{self._dataset_name}ClassDom"))
        parent_class_domain = ClassDomain(FileIO.clean(f"{self._dataset_name}{self.PARENT_PATTERN}ClassDom"))
        raw_class_info = {}
        for task in tqdm(self._data_info["tasks"], desc="parsing class domain..."):
            task_type, catalog = task["type"], task["catalog"]
            task_class_info = {}
            if task_type not in (self.INSTANCE_SEG_ANN_TYPE, self.DETECTION_ANN_TYPE):
                continue
            raw_class_info[task_type] = task_class_info
            for label_info in catalog:
                label_name = label_info["category_name"]
                task_class_info[label_info['category_id']] = label_name
                label_obj = Label(label_name)
                if label_obj in class_domain:
                    continue
                class_domain.add_label(label_obj)
                for supercategory_name in label_info.get("supercategories", []):
                    super_label = Label(supercategory_name)
                    if super_label not in parent_class_domain:
                        parent_class_domain.add_label(super_label)
                    label_obj.add_supercategory(super_label)  # 添加父类
        if parent_class_domain:
            class_domain.set_parent(parent_class_domain)
            return parent_class_domain, class_domain, raw_class_info, None
        else:
            return None, class_domain, raw_class_info, None

    def parse_ann_info(self):
        samples = self._annotation_info["samples"]
        object_struct = Struct("LocalObjectEntry")
        object_struct.set_arg("cdom")  # object struct有一个形参 cdom
        sample_struct = Struct("ObjectDetectionSample")
        sample_struct.set_arg("cdom") # sample struct 有一个形参 cdom
        media_field = Field("media", field_type="media")
        sample_struct.add_field(media_field)  # 添加图像field
        sample_container = DataSample(sample_struct, self._class_domain)
        annotation_option_flag = False
        for sample in tqdm(samples, desc="parsing samples ...."):
            sample_item = {}  # 存储当前样本信息
            media_info = sample["media"]
            img_path = media_info.pop("path")
            sample_item["media"] = img_path  # 添加图像样本信息
            for k, v in media_info.items():  # 添加图像相关的attributes
                this_field = Field(k, field_value=v, is_attr=True)
                sample_struct.add_field(this_field)
                sample_item[k] = v
            all_gt_info = {}

            if "ground_truth" in sample:
                gt_info = sample["ground_truth"]
            else:
                gt_info = []
                annotation_option_flag = True
                # sample_struct.set_optional("annotations")
            annotations = []
            for gt in gt_info:
                # 获取ann_id
                ann_id = gt.pop("ann_id")
                ann_id = gt.pop("ref_ann_id", ann_id)
                gt["ann_id"] = ann_id
                gt_item = {}
                gt_type = gt.pop("type")
                if gt_type == self.DETECTION_ANN_TYPE:
                    bbox_field = Field("bbox", field_type="bbox")
                    object_struct.add_field(bbox_field)
                    gt_item["bbox"] = gt.pop("bbox")
                elif gt_type == self.INSTANCE_SEG_ANN_TYPE:
                    ins_field = Field("points", field_type="points")
                    object_struct.add_field(ins_field)
                    gt_item["points"] = gt.pop("points")
                else:
                    continue
                # 创建LabelField并将值装进gt_item里面
                if 'categories' in gt and len(gt['categories']) > 0:
                    label_field = Field("category", field_type="category", param=f"${object_struct.args[0]}")
                    object_struct.add_field(label_field)
                    category_id = gt.pop("categories")[0]["category_id"]
                    category_name = self.raw_class_info[gt_type][category_id]  # 拿到category_name
                    gt_item["category"] = self._class_domain.index(category_name)
                else:
                    gt.pop("categories", [])

                attributes = gt.pop("attributes", {})
                for attr_k, attr_v in attributes.items():
                    attr_k = Util.clean(attr_k)
                    attr_field = Field(attr_k, field_value=attr_v, is_attr=True)
                    object_struct.add_field(attr_field, optional=True)
                    gt_item[attr_k] = attr_v
                for other_k, other_v in gt.items():
                    other_k = Util.clean(other_k)
                    other_field = Field(other_k, field_value=other_v, is_attr=True)
                    object_struct.add_field(other_field)
                    gt_item[other_k] = other_v
                all_gt_info.setdefault(ann_id, {})
                all_gt_info[ann_id].update(gt_item)

            annotations.extend(list(all_gt_info.values()))
            if annotations:
                sample_item["annotations"] = annotations

            sample_container.add_item(sample_item, not self.separate_flag)

        if len(object_struct.fields):
            annotation_field = Field("annotations", field_type="list",
                                     param=object_struct.as_others_param(sample_struct))
            sample_struct.add_field(annotation_field)  # 添加annotation field
            if annotation_option_flag:
                sample_struct.set_optional("annotations")
            return (object_struct, sample_struct), sample_container
        else:
            return (sample_struct,), [self._class_domain], sample_container