# -*- coding: utf-8 -*-
"""
更新日期:2022/9/10
作者: juncheng.Li
用途: 图片管道文件实现异步下载上传至阿里云oss
运行环境：win10 64/linux + python3.9 + scrapy2.4.1 + oss2 + magic(pip install python-magic-bin)
选择目录位置:{python}/Lib/site-packages/scrapy/xcc_pipelines
"""

from w3lib.url import safe_url_string
import hashlib
import logging
import os
from contextlib import suppress
from urllib.parse import urlparse

from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.utils.misc import md5sum
from scrapy.utils.python import to_bytes
from scrapy.pipelines.files import FileException

import oss2
import magic
from scrapy.xcc_pipelines.ossfilepipelines import OssFilesPipeline

import pdfplumber
from PyPDF2 import PdfFileReader, PdfFileWriter
import io
from scrapy.http.headers import Headers

logging.getLogger('pdfplumber').setLevel(logging.WARNING)
logging.getLogger('PyPDF2').setLevel(logging.WARNING)
logging.getLogger('pdfminer').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('oss2').setLevel(logging.WARNING)
logging.getLogger('img2pdf').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

class OSSOtherFilesStore:
    def __init__(self,uri):
        if not uri.startswith("https://xcc2.oss"):
            raise ValueError(f"Incorrect URI scheme in {uri}, expected '阿里云对象存储域名'")
        self.basedir = uri.rstrip('/')
        self.auth = oss2.Auth(self.OSS_USERNAME, self.OSS_PASSWORD)
        self._bucket = oss2.Bucket(self.auth, 'oss-cn-shenzhen.aliyuncs.com', 'xcc2')

    def persist_file(self, path, buf, info, meta=None, headers=None):
        if path:
            relative_path = path.replace(f"{self.basedir}/","")
            content= buf.getvalue()
            body = self.del_dirty_page(content=content,according_to=self.according_to,check_num=self.check_num) if self.deal_with_pdf else content
            pushobj_result = self._bucket.put_object(relative_path,body, progress_callback=None)
            if pushobj_result.status!=200:
                raise FileException('Push-obj-error')

    def del_dirty_page(self,content,according_to,check_num):
        '''根据关键词剔除pdf匹配页
        author : yongjie zhizhong
        content :: 二进制文件流
        according_to :: 逻辑判断文件
        according_to = {'and':['关键词','关键词'],# 逻辑关系
        'not':['关键词','关键词'],# 逻辑关系}
        check_num :: 从后向前取多少页'''
        pdf = pdfplumber.open(io.BytesIO(content))
        def check_gener(pdf):
            '''生成解析后的pdf文本 返回生成器'''
            for check_page in [i for i in pdf.pages][-check_num:len(pdf.pages)]:
                # check_page = pdf.pages[index]
                yield check_page.extract_text()

        def find_remove_page():
            '''生成关键词的判断语句'''
            if_words_spell_list = []
            for logic,words in according_to.items():
                for word in [word for word in words if word]:
                    if logic=='and':
                        if_words = ' "{}".lower() in extract_text.lower()'.format(word)
                    elif logic =='not':
                        if_words = ' "{}".lower() not in extract_text.lower()'.format(word)
                    if_words_spell_list.append(if_words)
            if_words_spell = ' and '.join(if_words_spell_list)
            return if_words_spell

        def inva_page_index():
            '''返回失效页index列表'''
            if_words_spell = find_remove_page()
            find_inva_page_index = []
            for check_page,extract_text in enumerate(check_gener(pdf)):
                if eval(if_words_spell):
                    pages = len(pdf.pages) - check_num
                    this_page = 0 if pages<0 else pages
                    fund_index = this_page + check_page
                    find_inva_page_index.append(fund_index)
            return find_inva_page_index
            
        def given(numPages):
            '''返回有效页index列表'''
            find_remove_page = inva_page_index()
            total_index = [i for i in range(numPages)]
            for index in find_remove_page:
                total_index.remove(index)
            return total_index

        def return_result_body():
            pdfReader = PdfFileReader(io.BytesIO(content),)
            pdfFileWriter = PdfFileWriter()
            numPages = pdfReader.getNumPages()

            for index in given(numPages):
                pageObj = pdfReader.getPage(index)
                pdfFileWriter.addPage(pageObj)
            file_content = io.BytesIO()
            pdfFileWriter.write(file_content)
            body = file_content.getvalue()
            file_content.close()
            return body
        pdf.close()
        return return_result_body()

    def del_pdf_watermark(self):
        pass

class OssOtherFilesPipeline(OssFilesPipeline):
    MEDIA_NAME = "ossfile"
    STORE_SCHEMES = {
        'https': OSSOtherFilesStore #新增阿里云文件存储类
    }
    DEFAULT_FILES_OSS_URLS_FIELD = 'raw_other_pdf_url'
    DEFAULT_FILES_OSS_RESULT_FIELD = 'other_pdf_url'
    DEFAULT_OSS_DOMAIN = 'https://xcc2.oss-cn-shenzhen.aliyuncs.com'
    FILTER_EMPTY_ITEM = False # 过滤字段urlimg为空的item

    def get_media_requests(self, item, info):
        # yield item 由此函数修改切割生成请求
        if not hasattr(item,'_refer'):
            item.__setattr__('_refer','')
        if not hasattr(item,'_header'):
            item.__setattr__('_header',{})
        if not hasattr(item,'_set_cookies'):
            item.__setattr__('_set_cookies',{})
        if self.file_pipe_config.get(self.__class__.__name__,{}).get("RESOURCE_CLASSNAME",'').lower() in item.__class__.__name__.lower():
            # TAG: 由于字段长度限制,限制字段urls个数100个以内
            # self.raw_pdf_url_before = ItemAdapter(item).get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_URLS_FIELD",self.files_oss_field))
            try:all_urls = list(ItemAdapter(item).get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_URLS_FIELD",self.files_oss_field), '').values())
            except:all_urls=list()
            urls = list()
            for _url in all_urls:
                if "|" in _url:
                    urls = urls + _url.split('|')
                else:
                    urls.append(_url)

            def request_add_params(urls):
                for u in urls:
                    if u:
                        u = Request(safe_url_string(u))
                        # 打开爬虫中间件后,_header不为空,取资源链接上一请求的header和referer,
                        # 如果header中包含cookie或响应中包含set-cookie请配置COOKIE_ENABLE=False
                        if item._refer :
                            #爬虫文件中如果给item设置_refer属性在此添加
                            item._header['Referer']=item._refer
                        if item._set_cookies :
                            #爬虫文件中如果给item设置_set_cookies属性在此添加
                            item._header['Cookie']=item._set_cookies
                        u.headers = Headers(item._header, encoding='utf-8')

                        if self.item_header_dict:
                            # 如果设置自定义ITEM_HEADER优先替换到header
                            for key_url in self.item_header_dict.keys():
                                host = urlparse(u.url).netloc
                                if key_url in host:
                                    u.headers = Headers(self.item_header_dict.get(key_url,{}),encoding ='utf-8')
                        yield u
                    
            return [u for u in request_add_params(urls[:100])]



    def item_completed(self, results, item, info):
        if self.file_pipe_config.get(self.__class__.__name__,{}).get("RESOURCE_CLASSNAME",'').lower() in item.__class__.__name__.lower():
            # 判断是否处理指定item类
            _other_pdf_url = dict()
            with suppress(TypeError):
                if '|'.join([x['path'] for ok, x in results if ok and x['path']]):
                    for ok , x, in results:
                        if ok and x['path']:
                            _url = x['url']
                            _path = x['path']
                            ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__, {}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)] =  ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__,{}).get('files_oss_field',self.files_oss_field)]
                            for k, v in zip(list(ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)].keys()), list(ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)].values())):
                                if _url in v:
                                    val = {k:_path}
                                    try:
                                        _other_pdf_url[k] = _other_pdf_url[k] + '|' + _path
                                    except:
                                        _other_pdf_url.update(val)
            # TAG: 如果决定资源字段返回为空不存表,修改 FILTER_EMPTY_ITEM = True , 默认false
            with suppress(KeyError):
                if not item.get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_RESULT_FIELD",''),"") and self.filter_empty_item:
                    if self.if_feed :# 解决输出文件时出现bug情况
                        return {}
                    else:
                        raise DropItem()

            ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__, {}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)] = _other_pdf_url

        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        media_guid = hashlib.sha1(response.body).hexdigest()
        media_ext_guss = os.path.splitext(os.path.basename(urlparse(request.url).path))[1]
        if not media_ext_guss and urlparse(request.url).netloc:# 若path为空则视为
            media_ext_guss = 'html'
        with suppress(AttributeError):
            kind = magic.from_buffer(response.body, mime=True).split('/')[-1]
            if media_ext_guss == '.caj':
                kind = media_ext_guss.split('.')[-1]
            media_ext = '.'+kind
        if kind != media_ext_guss.strip("."):
            #警告:出现文件流类型和链接拓展名不一致情况
            logging.warning(f"注意:原文件后缀名为( {media_ext_guss.strip('.')} )和判断文件类型( {kind} )不一致 资源链接如下{request.url}")
        if kind =='html': 
            # 如果判断结果为html,大概率下载失败
            with suppress(NameError):   
                logging.warning(f"下载文件为html,请确认是否下载成功,请求头:{str(Headers(request.headers, encoding='utf-8').to_unicode_dict())}")
                return ''
            media_ext = '.'+kind if not kind.startswith(".") else kind
            if media_ext == '.octet-stream':
                media_ext = '.caj'

        # if self.ext_model :
            # ext_model ::True表示当前情况适合用链接拓展名作为后缀;False表示当前适合用判断文件流来作为后缀
        normal_ext = [
            'jpg','png','jpeg','webp','svg','gif','tif','bmp',      #图片类
            'pdf','caj','zip','rar','csv','xlsx','xls','doc','ppt','dwg', #文档类
            'mp4','flv','rm','rmvb','avi','mov','mpeg',             #视频类
            'mp3','wav','wma'                                       #音频类
        ]
        if kind not in normal_ext and media_ext_guss.strip(".") in normal_ext: #如果判断结果非常见类型,链接拓展为常见类型,取源拓展名
            media_ext = media_ext_guss

        return f'{self.oss_domain}/{self.files_oss_file}/{media_guid}{media_ext}'



class OssOtherFilesPipelineBak(OssOtherFilesPipeline): #备用文件储存类 如其他pdf
    pass

class OssOtherFilesPipelineBakBak(OssOtherFilesPipeline): #备用文件储存类
    pass

