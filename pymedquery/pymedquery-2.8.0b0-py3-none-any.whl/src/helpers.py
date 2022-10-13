from pymedquery.config.logger_object import Logger

from typing import (
    Iterable, Any, Tuple, List, Union,
    Dict, Callable, TypeVar, Generator,
    NoReturn, BinaryIO
)
from collections.abc import Sequence
import blosc
import numpy as np
from functools import wraps
from time import time
import json
import pickle as pkl
import io
from psycopg2.extensions import AsIs, adapt
from collections import defaultdict

log: Callable = Logger(__name__)
T = TypeVar('T')
# We have it in config too although we get circular import error if try to get from config
BLOB_UIDS = ['series_uid', 'affine_uid', 'mask_uid', 'model_id']


def timer(orig_func: Callable) -> Callable[..., Callable[..., T]]:
    """This is custom timer decorator.
    Parameters
    ----------
    orig_func : object
        The `orig_func` is the python function which is decorated.
    Returns
    -------
    type
        elapsed runtime for the function.
    """

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1: str = time()
        result = orig_func(*args, **kwargs)
        t2: str = time() - t1
        print("Runtime for {}: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper


def adapt_numpy_nan(numpy_nan) -> NoReturn:
    """adapt_numpy_nan is an adapter function for psycopg2.

    Parameters
    ----------
    numpy_nan :
        numpy_nan is simply a NaN

    Returns
    -------
    NoReturn

    """
    return "'NaN'"


def adapt_numpy_inf(numpy_inf) -> NoReturn:
    """adapt_numpy_inf is an adapter function for psycopg2.

    Parameters
    ----------
    numpy_inf :
        numpy_inf

    Returns
    -------
    NoReturn

    """
    return "'Infinity'"


def adapt_numpy_ndarray(numpy_ndarray: np.ndarray) -> NoReturn:
    """adapt_numpy_ndarray is another adapter for psycopg2. Making postgres
    aware of numpy arrrays.

    Parameters
    ----------
    numpy_ndarray : np.ndarray
        numpy_ndarray

    Returns
    -------
    NoReturn

    """
    return AsIs(numpy_ndarray.tolist())


def adapt_set(set_: Sequence):
    return adapt(list(set_))


def addapt_dict(dict: dict):
    """addapt_dict is an adapter to make postgres aware of python dicts.

    Parameters
    ----------
    dict : dict
        dict
    """
    return AsIs(tuple(dict))


def make_uid_list(pg_payload: Dict[str, List[str]], batch_extract: bool):
    uid_list = []
    all_uids = []
    num_of_uids: Union[None, int] = None

    if batch_extract:
        try:
            # NOTE! This is poor design and should be more generic
            # This would be too specific if pyMedQuery is also to handle
            # other kinds of data
            for blob_uid in BLOB_UIDS:
                if pg_payload[blob_uid]:
                    # appending the list onto the list --> for example [series_list, affine_list]
                    uid_list.append(pg_payload[blob_uid])

            num_of_uids = len(uid_list)
            if num_of_uids > 1:
                for tuple_lst in list(zip(*uid_list)):
                    for uid in tuple_lst:
                        all_uids.append(uid)
            else:
                log.info('batch extract was called for only one type of UID')
                all_uids.extend(uid_list)
        except (ValueError, TypeError) as e:
            log.error(f'failed to create a uid list for batching: {e}')

    else:
        for blob_uid in BLOB_UIDS:
            if pg_payload[blob_uid]:
                all_uids.extend(pg_payload[blob_uid])

    return (all_uids, num_of_uids)


def check_batch_size(num_of_uids: int, batch_size: int):
    log.info('checking if the batch size is set correctly')
    if (num_of_uids % 2) == 0:
        check = True if (batch_size % 2) == 0 else False
    else:
        check = False if (batch_size % 2) == 0 else True
    return check


def batch_maker(iterable: Iterable[Any], batch_size: int = 10) -> Generator[int, None, None]:
    """batch_maker is helper for making batches of arrays.

    Parameters
    ----------
    iterable : Iterable[Any]
        iterable can be anything that is iterable containg the data to be batched
    batch_size : int
        batch_size is the integer that governs the size of the batch

    Returns
    -------
    Generator[int, None, None]

    """
    iterable_length = len(iterable)
    for idx in range(0, iterable_length, batch_size):
        yield iterable[idx: min(idx + batch_size, iterable_length)]


def read_data_file(fname: str, jlib: bool = False) -> BinaryIO:
    """
    Description
    ===========
    Function that reads in either a dataframe, dictionary or csv
    Setup
    ===========
    :param fname: the filepath for where object is stored
    :return data: the data of interest
    """

    if not fname:
        raise ValueError(
            "please specifiy the filepath for where the object is to be saved"
        )

    with open(fname, "rb") as filepath:
        if jlib:
            log.info(f"Reading file from {fname} with joblib")
            data = joblib.load(filepath)
        else:
            if ".gz" in fname:
                log.failure("please set jlib=True when reading gzip files")
            if ".pkl" in fname or ".pickle" in fname:
                log.info(f"Reading a pickle file from {fname} with joblib")
                data = pkl.load(filepath)
            if ".json" in fname:
                log.info(f"Reading a json file from {fname} with joblib")
                data = json.load(filepath)
        log.success("Loading done, happy coding!")
    return data


def nested_dict() -> Dict[Any, Dict[str, Any]]:
    """Reacursive dict function for making nested dicts.

    Parameters
    ----------

    Returns
    -------
    Dict[Any, Dict[str, Any]]

    """
    return defaultdict(nested_dict)


def payload_to_dict(
        payload: List[Tuple[Any]], colnames: Tuple[str],
        dict_: Dict[str, List[Union[str, int, float, bool, None]]] = defaultdict(list)
) -> Dict[str, List[Union[str, int, float, bool, None]]]:
    """payload_to_dict is transform function that converts a list with tuples into a dict.

    Parameters
    ----------
    payload : List[Tuple[Any]]
        payload
    colnames : Tuple[str]
        colnames
    dict_ : Dict[str, List[Union[str, int, float, bool, None]]]
        dict_

    Returns
    -------
    Dict[str, List[Union[str, int, float, bool, None]]]

    """
    dict_.clear()
    for list_ in payload:
        for idx, col in enumerate(colnames):
            dict_[col].append(list_[idx])
    return dict_


def payload_transform(payload: bytes, shape_str: str, dtype_str: str, image_extraction: bool = True) -> Union[np.ndarray, bytes]:
    """payload_transform takes an API response of an image as input and converts it back from bytes
    to a numpy array.

    Parameters
    ----------
    payload : bytes
        payload
    shape_str : str
        shape_str
    dtype_str : str
        dtype_str

    Returns
    -------
    np.ndarray

    """
    # decompress the payload
    payload_decomp = blosc.decompress(payload)
    if image_extraction:
        if not shape_str:
            raise TypeError(f'I expected a shape string for the image but got {shape_str}')
        # get the image shape from the metadata of the http header
        img_shape = tuple(int(i) for i in shape_str[1:-1].split(","))

        # reshape the image to the original
        flat_img = np.frombuffer(payload_decomp, dtype=dtype_str, count=-1)
        img = flat_img.reshape(img_shape)
        return img
    else:
        return payload_decomp


# NOTE! move these functions to a util lib and take them out of the upload method (sep of concern)
def encode_payload(
        payload: Any
) -> bytes:
    """This functions make the payload ready for the post request by
    converting the dictionary to bytes, compression, and placing it in a buffer.
    It's finally converted to hexstring for JSON serialization. The buffer is not
    converted to a hexstring if you are using the gzip solution. NOTE, the gzip
    solution is a bit slower then blocs.

    NOTE! We need to incorporate pkl.loads in the decoding as some byte conversions
    rely on it.
    Parameters
    ----------
    payload : dict
        This the dictionary containing the data that you want to ship
        as a HTTPS post request to the database.
    Returns
    -------
    A string for the post request is returned.
    """
    try:
        bytes_compressed = blosc.compress(bytes(payload), cname='zstd')
    except OverflowError as e:
        log.warning(f"""
        We are getting an overflow error on the payload: {e}.
        Shifting to pkl.dumps to see if it solves the problem.""")
        bytes_compressed = blosc.compress(pkl.dumps(payload), cname='zstd')
    except ValueError as e:
        log.warning(f'We are getting an error {e}. I will try to json dump your payload for bytes conversion.')
        bytes_compressed = blosc.compress(bytes(json.dumps(payload)), cname='zstd')
    finally:
        byte_buffer = io.BytesIO(bytes_compressed)
        return byte_buffer, byte_buffer.getbuffer().nbytes


def convert_str_to_list(records: Tuple[List[str]]):
    for rec in records[0]:
        if isinstance(rec, str) and '[' in rec:
            rec = list(rec)
