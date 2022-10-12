import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from typing import List
from jssp_tool.env.operation_machine_helper import Operation


def plot_gantt(nodes: List[Operation], edge_color=None):
    # 显示中文标签
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    fontdict_task = {"family": "Microsoft YaHei", "style": "oblique", "color": "black", "size": 12}
    fontdict_label = {"family": "Microsoft YaHei", "style": "oblique", "color": "black", "size": 11}

    machine_ids = sorted(list(set([node.machine_id for node in nodes])))
    yticks = ["机器 {}".format(i) for i in machine_ids]
    plt.yticks(machine_ids, yticks, fontdict=fontdict_label)

    # 颜色范围，参考 https://matplotlib.org/stable/tutorials/colors/colormaps.html
    cmap = matplotlib.cm.get_cmap("tab20c")
    colors = cmap(np.linspace(0, 1, len(machine_ids)))

    for node in nodes:
        plt.barh(
            y=node.machine_id,
            width=node.processing_time,
            left=node.start_time,
            edgecolor=edge_color,
            color=colors[node.machine_id],
        )
        plt.text(
            node.start_time + 0.1,
            node.machine_id - 0.1,
            "J{} O{}".format(node.id, node.job_id),
            fontdict=fontdict_task,
        )
    plt.xlabel("调度时刻", fontdict=fontdict_label)
    # plt.ylabel('机器名称', fontdict=fontdict_label)
    plt.show()

