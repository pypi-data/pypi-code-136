import numpy as np
import random

def extend(arr, mask, maxlength, padding_type):
    if isinstance(arr, (tuple, np.ndarray)):
        arr = [*arr]

    padding = [mask] * (maxlength - len(arr))
    if padding_type == 'tailing':
        arr.extend(padding)
    elif padding_type == 'leading':
        arr = padding + arr
    else:
        assert padding_type == 'general'
        for mask in padding:
            arr.insert(random.randrange(0, len(arr)), mask)

    return arr


def extend_tailing(arr, mask, maxlength):
    if isinstance(arr, tuple):
        arr = [*arr]

    padding = [mask] * (maxlength - len(arr))

    arr.extend(padding)

    return arr


def numpify_tailing(arr, mask_value=0):
    maxWidth = max(len(x) for x in arr)
    # arr is a 2-dimension array
    for i in range(len(arr)):
        arr[i] = extend_tailing(arr[i], mask_value, maxWidth)
    return np.array(arr)


def numpify_leading(arr, mask_value=0):
    return numpify(arr, mask_value, padding='leading')

# arr is a 3-dimension array
# def numpify(arr, mask_value=0, padding='general'):
# def numpify(arr, mask_value=0, padding='leading'):


def numpify(arr, mask_value=0, padding='tailing'):
    '''
    
    :param arr:
    :param mask_value:
    :param shuffle: randomly insert the padding mask into the sequence！ this is used for testing masking algorithms!
    '''

    try:
        maxWidth = max(len(x) for x in arr)
    except (TypeError, AttributeError) as _:
        return np.array(arr)

    try:
        maxHeight = max(max(len(word) for word in x) for x in arr)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j] = extend(arr[i][j], mask_value, maxHeight, padding)
            arr[i] = extend(arr[i], [mask_value] * maxHeight, maxWidth, padding)
    except (TypeError, AttributeError, ValueError) as _:

        # arr is a 2-dimension array
        for i in range(len(arr)):
            arr[i] = extend(arr[i], mask_value, maxWidth, padding)

    return np.array(arr)

