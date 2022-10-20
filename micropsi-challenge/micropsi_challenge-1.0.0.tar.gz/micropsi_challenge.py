def get_first_local_minima(lst: list):
    """
    Finds the very first local minima in the array of elements. Each element in the list suppose to support "less than"
    operator.

    :param lst: This is list of elements.
    :return: Element that represents first local minima.
    :raise: IndexError: Raises if lst is empty.
    """
    # needed only for a bit better explanation message
    if len(lst) == 0:
        raise IndexError("Parameter \"lst\" is empty")
    elif len(lst) == 1:
        return lst[0]
    prev_item = lst[0]
    for item in lst[1:]:
        if item < prev_item:
            prev_item = item
        else:
            break
    return prev_item

