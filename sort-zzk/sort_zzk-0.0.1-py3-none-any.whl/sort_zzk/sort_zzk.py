
def sort(lst: list, key: str, reverse: bool = False):
    """
    :param lst: [{k1:v1},{k2:v2}...]
    :param key: k1/k2
    :param reverse: bool 默认升序   reverse=True 降序
    :return: list
    """
    lst2 = sorted(lst, key=lambda x: x[f"{key}"], reverse=reverse)
    return lst2

