from ..general import Field, Struct, DataSample, Util
from tqdm import tqdm
from .base_parse import BaseParse


class SemanticSegmentationParse(BaseParse):

    def parse_ann_info(self):
        samples = self._annotation_info["samples"]
        sample_struct = Struct("SemanticSegSample")
        media_field = Field("media", field_type="media")
        sample_struct.add_field(media_field)  # 添加图像field
        sample_container = DataSample(sample_struct, None)  # 暂时不添加 class domain
        domain_info = {}  # true_task_uid: domain
        key_info = {}
        field_args = {}  # true_task_uid: arg

        for sample in tqdm(samples, desc="parsing samples ...."):
            sample_item = {}  # 存储当前样本信息
            media_info = sample["media"]
            img_path = media_info.pop("path")
            sample_item["media"] = img_path  # 添加图像样本信息
            for k, v in media_info.items():  # 添加图像相关的attributes
                this_field = Field(k, field_value=v, is_attr=True)
                sample_struct.add_field(this_field)
                sample_item[k] = v

            if "ground_truth" in sample:
                gt_info = sample["ground_truth"]
            else:
                gt_info = []
                # sample_struct.set_optional("annotations")
            for gt in gt_info:
                # 获取ann_id
                task_type, task_name, ann_source = gt.pop("type"), gt.pop("name"), gt.pop("source")
                if task_type != self.SEMANTIC_SEG_ANN_TYPE:
                    continue
                ann_id = gt.pop("ann_id")
                ann_id = gt.pop("ref_ann_id", ann_id)
                gt_item = {}
                _uid = f"{task_type}${task_name}${ann_source}"
                class_domain = self._class_domain[_uid]
                true_uid = self.task_uid_map[_uid]
                domain_info[true_uid] = class_domain
                if len(key_info) == 0:
                    map_field_name = "map_path"
                    key_info[true_uid] = map_field_name
                elif true_uid in key_info:
                    map_field_name = key_info[true_uid]
                else:
                    map_field_name = f"map_path_{len(key_info)}"
                    key_info[true_uid] = map_field_name
                if len(field_args) == 0:
                    arg = "cdom"
                    field_args[true_uid] = arg
                elif true_uid in field_args:
                    arg = field_args[true_uid]
                else:
                    arg = f"cdom{len(field_args)}"
                    field_args[true_uid] = arg
                seg_map_field = Field(map_field_name, field_type="map_path", param=f"${arg}")
                sample_struct.add_field(seg_map_field)
                gt_item[map_field_name] = gt.pop('map_path')

                attributes = gt.pop("attributes", {})
                for attr_k, attr_v in attributes.items():
                    attr_k = Util.clean(attr_k)
                    attr_field = Field(attr_k, field_value=attr_v, is_attr=True)
                    sample_struct.add_field(attr_field, optional=True)
                    gt_item[attr_k] = attr_v
                sample_item.update(gt_item)

            sample_container.add_item(sample_item, not self.separate_flag)
        uids = list(key_info.keys())
        field_args = [field_args[_] for _ in uids]
        domains = [domain_info[_] for _ in uids]
        sample_struct.set_arg(field_args)
        sample_container.set_domain(domains)
        return (sample_struct,), domains, sample_container
