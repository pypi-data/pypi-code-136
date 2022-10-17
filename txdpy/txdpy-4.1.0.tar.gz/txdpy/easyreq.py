from loguru import logger
import requests
from fake_useragent import UserAgent
from lxml import etree
from .requests_operation import param_dict,headers_dict
from colorama import Fore, init
init()

def req(url:str,param:str=None,data:str=None,json:str=None,headers:str=None,verify:bool=True):
    """
    :param url: 请求的url
    :param param: get请求参数默认为空
    :param data: post请求参数默认为空
    :param json: json请求参数默认为空
    :param headers: 默认随机User-Agent
    :param verify: 是否认证证书，默认为true
    :param tree: 是否直接返回etree.HTML()对象，默认为False
    :return: 返回reponese对象
    """
    h=headers_dict(headers) if headers else {'User-Agent': UserAgent().random}
    if param:
        res=requests.get(url,params=param_dict(param),headers=h,verify=verify)
    elif json:
        res=requests.post(url,json=param_dict(json),headers=h,verify=verify)
    elif data:
        res=requests.post(url,data=param_dict(data),headers=h,verify=verify)
    else:
        res=requests.get(url, params=param_dict(param), headers=h,verify=verify)
    res.encoding = res.apparent_encoding
    res.tree=etree.HTML(res.text)
    status_code=res.status_code
    if 200<=status_code<=201:
        logger.info(f'\t地址：{url}\t\t状态码：'+Fore.GREEN + str(res.status_code))
    elif status_code>=400:
        logger.info(f'\t地址：{url}\t\t状态码：' + Fore.RED + str(res.status_code))
    else:
        logger.info(f'\t地址：{url}\t\t状态码：' + Fore.YELLOW + str(res.status_code))
    return res