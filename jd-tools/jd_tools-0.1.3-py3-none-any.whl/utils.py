# -*- coding: utf-8 -*-
import datetime
import json
from base64 import b64decode
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
"""
DATE        AUTHOR  DESCRIPTION
----------  ------  -----------------------------------------------------------------
2022-07-02  WXG     添加微信支付通知解密函数 notify_decrypt , 版本改为 1.3
"""

__version__ = "1.3"
__all__ = [
    "generate_map", "generate_map_ex", "cyt_map", "gen_key",
    "notify_decrypt"
]


def generate_map(records, field, add_columns=True):
    """
    将 子表记录，根据主表id，缓存到 map表  1:N
    :param records:     子表记录 列表
    :param field:       主表记录 id 字段名。通过 getattr 访问，主表
    :param add_columns:    子表 在 records 中位置， True， 取记录r[0]， False 取记录r
    :return:  records_map  缓存 子表记录的 map 表
    """
    records_map = dict()
    for i in records:
        if add_columns:
            r = i[0]
        else:
            r = i
        id_ = getattr(r, field)
        if id_ in records_map:
            records_map[id_].append(i)
        else:
            records_map[id_] = [i]
    return records_map


def generate_map_ex(records, add_columns=True, *args):
    """
    将 记录，根据 主表id，缓存到 map表   1:1
    :param records:         记录 列表
    :param add_columns:     记录中是否使用了add_columns方法， True-是， False-否
    :param args:            记录 关键字 key，多个使用 连字符拼接。 通过 getattr 访问
    :return:  records_map  记录的 map 表， key 中 value 唯一
    """
    records_map = dict()
    for i in records:
        if add_columns:
            r = i[0]
        else:
            r = i

        ids = []
        for key_ in args:
            ids.append(getattr(r, key_))

        if len(ids) == 1:   # 只有一个key，保留原来的 int 类型
            id_ = ids[0]
        else:   # 多个key， 转为字符串
            id_ = '-'.join([str(i) for i in ids])
        records_map[id_] = i
    return records_map


def gen_key(*args):
    """生成key， args 为 构造key 的字段值"""
    ids = []
    for key_ in args:
        ids.append(key_)

    if len(ids) == 1:  # 只有一个key，保留原来的 int 类型
        id_ = ids[0]
    else:  # 多个key， 转为字符串
        id_ = '-'.join([str(i) for i in ids])
    return id_


def cyt_map(records, one_to_one, *args, attr=True):
    """将记录，根据 args 提供的 key，缓存到 map表
    :param records:     记录
    :param one_to_one:  1:1 or 1:N
    :param args:        记录 关键字 key，多个使用 连字符拼接， 通过 records[].key 可以访问
    :param attr:        True 可以通过 getattr 获取属性； False 通过 [key] 获取属性
    :return:  records_map  记录map, 1：N
    """
    records_map = dict()
    for i in records:
        ids = []
        for key_ in args:
            if attr:
                val = getattr(i, key_)
            else:
                val = i[key_]

            if isinstance(val, datetime.datetime):
                val = val.date()
            ids.append(val)

        if len(ids) == 1:  # 只有一个key，保留原来的 int 类型
            id_ = ids[0]
        else:  # 多个key， 转为字符串
            id_ = '-'.join([str(i) for i in ids])
        if one_to_one:
            records_map[id_] = i    # 1:1 模式   k: v
        else:
            if id_ in records_map:
                records_map[id_].append(i)   # 1:N 模式   k: [v1, v2, ...]
            else:
                records_map[id_] = [i]
    return records_map


def notify_decrypt(nonce: str, ciphertext: str, associated_data: str, key: str) -> dict:
    """
    通知报文
    通知的数据会加密 post 到对接方接口中，由于涉及到回调加密和解密，接入方必须先通过微校商务侧申请通知秘钥 key，
    申请好通知秘钥 key 后才能解密回调通知
    original_type 原始回调类型，为transaction

    参数解密

    通知秘钥 key，记为 notify_key；
    针对 resource.algorithm 中描述的算法（目前为 AEAD_AES_256_GCM），取得对应的参数 nonce 和 associated_data；
    使用 notify_key、nonce 和 associated_data，对数据密文 resource.ciphertext 进行解密，得到 JSON 形式的
    资源对象（资源对象就是具体的数据内容）；
    注： AEAD_AES_256_GCM 算法的接口细节，请参考 rfc5116。微校支付使用的通知密钥 key 长度为 32 个字节，随机串 nonce
    长度 32 个字节，associated_data 长度小于 16 个字节并可能为空。
    参考： https://wiki.weixiao.qq.com/api/third/withhold/payRunning.html

    https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_5_5.shtml
    参数解密
    下面详细描述对通知数据进行解密的流程：
    1、用商户平台上设置的APIv3密钥【微信商户平台—>账户设置—>API安全—>设置APIv3密钥】，记为key；
    2、针对resource.algorithm中描述的算法（目前为AEAD_AES_256_GCM），取得对应的参数nonce和associated_data；
    3、使用key、nonce和associated_data，对数据密文resource.ciphertext进行解密，得到JSON形式的资源对象；
    注： AEAD_AES_256_GCM算法的接口细节，请参考rfc5116。微信支付使用的密钥key长度为32个字节，随机串nonce长度12个字节，
    associated_data长度小于16个字节并可能为空字符串。

    :param nonce:           随机串
    :param ciphertext:      密文
    :param associated_data: 附加数据
    :param key:             秘钥 key
    :return:  字典对象，解密失败时，返回 空 字典 dict
    """
    key_bytes = key.encode('UTF-8')
    nonce_bytes = nonce.encode('UTF-8')
    associated_data_bytes = associated_data.encode('UTF-8')
    data = b64decode(ciphertext)
    aes_gcm = AESGCM(key=key_bytes)
    try:
        result = aes_gcm.decrypt(nonce=nonce_bytes, data=data, associated_data=associated_data_bytes).decode('UTF-8')
    except InvalidTag:
        result = ''  # 解密失败
    if result:
        data = json.loads(result)
    else:
        data = dict()
    return data
