import os
from pathlib import Path
import sys
from typing import Optional

import numpy as np

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.tools.read_point_cloud2 import read_points

try:
    from rosbags import rosbag2
    from rosbags.serde import deserialize_cdr
except ModuleNotFoundError:
    print('rosbag2 reader is not installed, run "pip install rosbags"')
    sys.exit(1)


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
        self.bag = rosbag2.Reader(self.bagfile)
        self.bag.open()
        self.topic = topic
        self.check_for_topics()
        self.n_scans = self.bag.topics[self.topic].msgcount
        self.msgs = self.bag.messages()

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
        connection, _, rawdata = next(self.msgs)
        msg = deserialize_cdr(rawdata, connection.msgtype)
        points = np.array(list(read_points(msg, field_names=["x", "y", "z"])))

        t_field = None
        for field in msg.fields:
            if field.name == "t" or field.name == "timestamp":
                t_field = field.name
        timestamps = np.ones(points.shape[0])
        if t_field:
            timestamps = np.array(list(read_points(msg, field_names=t_field)))
            timestamps = timestamps / np.max(timestamps)
        if self.config.data.preprocess:
            points, timestamps = self._preprocess(points, timestamps, self.config.data)
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
        print("PointCloud2 topics available:")
        for topic, topic_info in self.bag.topics.items():
            if topic_info.msgtype == "sensor_msgs/msg/PointCloud2":
                print(topic)
        sys.exit(1)
