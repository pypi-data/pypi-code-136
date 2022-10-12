"""
    加密机
"""
import socket

from ats_base.config.configure import CONFIG


class Client(object):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((CONFIG.get('EM', 'ip'), int(CONFIG.get('EM', 'port'))))

    def close(self):
        self.s.close()

    def send(self, command):
        self.connect()
        self.s.send(command.encode('utf-8'))
        result = self.s.recv(1024).decode('utf-8')
        self.s.close()
        return result


"""
    GW698协议客户端调用接口
"""


def random():
    """
    随机数
    :return:
    """
    command = 'UP698015:00:00;'
    result = Client().send(command)
    rn = result.split(';')[3]

    return rn


def negotiate(m_sn: str, m_counter: int):
    """
    协商
    :param m_sn:
    :param m_counter:
    :return:
    """
    cs = '%08X' % (m_counter + 1)
    command = 'UP698001:04;0001000800040001;00{}{}01'.format(m_sn.upper(), cs.upper())
    result = Client().send(command)

    ar = result.split(';')[3]
    rn = ar[0:32]
    data = ar[32:96]
    mac = ar[96:]

    return {"rn": rn, "data": data, "mac": mac}


def match(rn, m_sn, m_rn, m_mac):
    """
    验证
    :param rn:
    :param m_sn:
    :param m_rn:
    :param m_mac:
    :return:
    """
    command = 'UP698002:05;00010008001000300004;00{}{}{}{}'.format(m_sn.upper(), rn.upper(), m_rn.upper(),
                                                                   m_mac.upper())
    result = Client().send(command)
    iv = result.split(';')[3]

    return {"iv": iv}


"""
    GW698协议服务调用接口
"""


def encrypt(op_mode, esam_id, iv, data):
    """
    数据域加密
    :param op_mode:
    :param esam_id:
    :param iv:
    :param data:
    :return:
    """
    command = 'UP698006:04;0001000800B0{};{}{}{}{}'.format('%04X' % int(len(data) / 2),
                                                           '%02X' % op_mode,
                                                           esam_id.upper(),
                                                           iv.upper(),
                                                           data.upper())
    result = Client().send(command)

    lens = result.split(';')[2]
    ar = result.split(';')[3]
    tag = ar[0:8]
    attach_data = ar[8:12]
    dl = 12 + (int(lens[8:12], 16) * 2)
    cipher = ar[12:dl]
    ml = int(lens[12:16], 16) * 2
    mac = ''
    if ml > 0:
        mac = ar[-8:]

    return tag, attach_data, cipher, mac


def decrypt(key_state, op_mode, esam_id, iv, data, mac):
    """
    数据域解密
    :param key_state:
    :param op_mode:
    :param esam_id:
    :param iv:
    :param data:
    :param mac:
    :return:
    """
    command = 'UP698007:06;00010001000800B0{}0004;{}{}{}{}{}{}'.format('%04X' % int(len(data) / 2),
                                                                       '%02X' % key_state,
                                                                       '%02X' % op_mode,
                                                                       esam_id.upper(),
                                                                       iv.upper(),
                                                                       data.upper(),
                                                                       mac.upper())
    result = Client().send(command)
    plain_data = result.split(';')[3]
    return plain_data
