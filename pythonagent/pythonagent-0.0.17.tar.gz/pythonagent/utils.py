import time
import sys
import random


def get_current_timestamp_in_ms():
    if sys.version_info >= (3, 7, 0):
        time_stamp = time.time_ns() // 1000000
    else:
        time_stamp = int(round(time.time() * 1000))

    return time_stamp


def generate_flow_path_id():
    # 63 bit number having 1 followed by 62 zeros
    # In 64 bit long long, 1 bit is for sign (+ or -)
    # So effective range is of 63 bits only
    # Flow Path Id (63 bits) Format:
    # DC Id (8 bits) App Id (10 bits) Timestamp ID (38 bits) Unique ID (7 bits)

    flow_path_id = 0x4000000000000000
    
    dc_id, dc_mask, dc_pos = 0, 0x0F, 56
    app_id, app_mask, app_pos = 0, 0x03FF, 46
    timestamp_id, timestamp_mask, timestamp_pos = get_current_timestamp_in_ms(), 0x3FFFFFFFFF, 8
    unique_id, unique_mask, unique_pos = random.getrandbits(7), 0xFF, 0

    dc_and = (dc_id & dc_mask) << dc_pos
    app_and = (app_id & app_mask) << app_pos
    timestamp_and = (timestamp_id & timestamp_mask) << timestamp_pos
    unique_and = (unique_id & unique_mask) << unique_pos

    flow_path_id = flow_path_id + dc_and + app_and + timestamp_and + unique_and
    return flow_path_id


def get_utf8_bytes(str_obj):
    try:
        bytes_obj = bytes(str_obj, 'utf-8')
    except:
        bytes_obj = bytes(str_obj.encode("utf-8"))

    return bytes_obj
