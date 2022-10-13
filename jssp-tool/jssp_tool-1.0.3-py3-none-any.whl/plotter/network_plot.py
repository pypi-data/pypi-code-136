from collections import OrderedDict
from enum import Enum

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt


# 边的类型
class EdgeType(Enum):
    CONJUNCTIVE = 0
    DISJUNCTIVE = 1


# 结点类型（或者称operation状态）
class OpStatus(Enum):
    NOT_SCHEDULED = -1
    PROCESSING = 0
    DELAYED = 1
    DONE = 2
    DUMMY = 3


def plot_network(n_j, n_m, adj_matrix, node_ids, node_types, fig_config=None, show=True, **nx_configs):
    g = nx.DiGraph()

    node_size = len(adj_matrix)
    # 添加结点
    for i, node_type in enumerate(node_types):
        g.add_node(i, type=node_type)

    # 添加边
    for i in range(node_size):
        for j in range(node_size):
            if i != j and adj_matrix[i][j] == 1:
                edge_type = (
                    EdgeType.CONJUNCTIVE if ((i == j - 1 and j > 0) or (j == i - 1 and i > 0)) else EdgeType.DISJUNCTIVE
                )
                g.add_edge(node_ids[i], node_ids[j], type=edge_type)

    fig = plt.figure(fig_config)
    ax = fig.add_subplot(1, 1, 1)
    node_colors = _get_node_color_map(g)
    edge_colors = _get_edge_color_map(g)
    pos_dict = _get_pos_dict(30, 10, n_j, n_m)

    nx.draw(g, pos_dict, node_color=node_colors, edge_color=edge_colors, with_labels=True, ax=ax, **nx_configs)
    if show:
        plt.show()


def _get_pos_dict(half_width, half_height, n_j, n_m):
    def xidx2coord(x):
        return np.linspace(-half_width, half_width, n_m)[x]

    def yidx2coord(y):
        return np.linspace(half_height, -half_height, n_j)[y]

    pos_dict = dict()
    for i in range(n_j):
        for j in range(n_m):
            pos_dict[i * n_m + j] = (xidx2coord(j), yidx2coord(i))
    return pos_dict


def _get_node_color_map(g, node_type_color_dict=None):
    """
    给边设置颜色
    Args:
        g (nx.DiGraph): 图对象
        node_type_color_dict: 用户自定义颜色配置，若为None，使用默认配置

    Returns:
        colors: 每个结点对应的颜色列表
    """
    if node_type_color_dict is None:
        node_type_color_dict = OrderedDict()
        node_type_color_dict[OpStatus.NOT_SCHEDULED] = "#F0E68C"
        node_type_color_dict[OpStatus.PROCESSING] = "#ADFF2F"
        node_type_color_dict[OpStatus.DELAYED] = "#829DC9"
        node_type_color_dict[OpStatus.DONE] = "#E9E9E9"
        node_type_color_dict[OpStatus.DUMMY] = "#FFFFFF"

    colors = []
    for n in g.nodes:
        node_type = g.nodes[n]["type"]
        colors.append(node_type_color_dict[node_type])
    return colors


def _get_edge_color_map(g, edge_type_color_dict=None):
    """
    给边设置颜色
    Args:
        g (nx.DiGraph): 图对象
        edge_type_color_dict: 用户自定义颜色配置，若为None，使用默认配置

    Returns:
        colors: 每个结点对应的颜色列表
    """
    if edge_type_color_dict is None:
        edge_type_color_dict = OrderedDict()
        edge_type_color_dict[EdgeType.CONJUNCTIVE] = "#191970"
        edge_type_color_dict[EdgeType.DISJUNCTIVE] = "#87CEFA"

    colors = []
    for e in g.edges:
        edge_type = g.edges[e]["type"]
        colors.append(edge_type_color_dict[edge_type])
    return colors


def _get_row_col(ind, n_col):
    """
    :param ind: 数组下标
    :param n_col: 调度矩阵列的数量，即机器数量
    :return:
    """
    return ind // n_col, ind % n_col
