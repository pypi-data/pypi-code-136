try:
    import rosbag
except ModuleNotFoundError:
    print('python rosbag is not installed, run "sudo apt install python3-rosbag"')
    exit(1)

import os
from pathlib import Path
from typing import Optional

import numpy as np
import sensor_msgs.point_cloud2 as pc2
import yaml

from kiss_icp.config import KISSConfig, load_config


class RosbagDataset:
    def __init__(
        self,
        data_dir: Path,
        config: Path,
        topic: str,
        max_range: Optional[float] = None,
        *_,
        **__,
    ):
        # Config stuff
        self.config = load_config(config)
        self.config.data.max_range = max_range if max_range else self.config.data.max_range
        self.sequence_id = os.path.basename(data_dir).split(".")[0]

        # bagfile
        self.bagfile = data_dir
        self.bag = rosbag.Bag(data_dir, mode="r")
        self.topic = topic
        self.check_for_topics()

        # Get an iterable
        self.n_scans = self.bag.get_message_count(topic_filters=topic)
        self.msgs = self.bag.read_messages(topics=[topic])

        # Cache
        if self.config.use_cache:
            print("[WARNING] Disabling cache use for rosbag files")
        self.use_cache = False

        # Visualization Options
        self.use_global_visualizer = True

    def __del__(self):
        self.bag.close()

    def __len__(self):
        return self.n_scans

    def __getitem__(self, idx):
        return self.read_point_cloud(self.bagfile, self.topic, idx, self.config.data)

    def read_point_cloud(
        self,
        bagfile: Path,
        topic: str,
        idx: int,
        config: KISSConfig.data,
    ):
        # TODO: implemnt [idx], expose field_names
        _, msg, _ = next(self.msgs)
        points = np.array(list(pc2.read_points(msg, field_names=["x", "y", "z"])))

        t_field = None
        for field in msg.fields:
            if field.name == "t" or field.name == "timestamp":
                t_field = field.name
        timestamps = np.ones(points.shape[0])
        if t_field:
            timestamps = np.array(list(pc2.read_points(msg, field_names=t_field)))
            timestamps = timestamps / np.max(timestamps)
        if config.preprocess:
            points, timestamps = self._preprocess(points, timestamps, config)
        return points.astype(np.float64), timestamps

    @staticmethod
    def _preprocess(points, timestamps, config: KISSConfig.data):
        ranges = np.linalg.norm(points, axis=1)
        filter_ = np.logical_and(ranges <= config.max_range, ranges >= config.min_range)
        return points[filter_], timestamps[filter_]

    def check_for_topics(self):
        if self.topic:
            return
        print("Please provide one of the following topics with the --topic flag")
        info_dict = yaml.safe_load(self.bag._get_yaml_info())
        info_dict.keys()
        print("PointCloud2 topics available:")
        for topic in info_dict["topics"]:
            if topic["type"] == "sensor_msgs/PointCloud2":
                for k, v in topic.items():
                    print(k.ljust(20), v)
        exit(1)
