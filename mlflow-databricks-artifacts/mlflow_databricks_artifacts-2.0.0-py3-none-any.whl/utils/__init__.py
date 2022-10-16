def chunk_list(l, chunk_size):
    for i in range(0, len(l), chunk_size):
        yield l[i : i + chunk_size]


def merge_dicts(dict_a, dict_b, raise_on_duplicates=True):
    """
    This function takes two dictionaries and returns one singular merged dictionary.

    :param dict_a: The first dictionary.
    :param dict_b: The second dictonary.
    :param raise_on_duplicates: If True, the function raises ValueError if there are duplicate keys.
                                Otherwise, duplicate keys in `dict_b` will override the ones in
                                `dict_a`.
    :return: A merged dictionary.
    """
    duplicate_keys = dict_a.keys() & dict_b.keys()
    if raise_on_duplicates and len(duplicate_keys) > 0:
        raise ValueError(
            f"The two merging dictionaries contains duplicate keys: {duplicate_keys}."
        )
    return {**dict_a, **dict_b}
