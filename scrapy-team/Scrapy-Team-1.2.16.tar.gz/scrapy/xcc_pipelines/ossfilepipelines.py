# -*- coding: utf-8 -*-
"""
更新日期:2022/4/28
作者: D.Z.zhong
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

from scrapy.exceptions import NotConfigured ,DropItem
from scrapy.http import Request
from scrapy.pipelines.media import MediaPipeline
from scrapy.settings import Settings
from scrapy.utils.misc import md5sum
from scrapy.utils.python import to_bytes
from scrapy.utils.request import referer_str
from scrapy.pipelines.files import FileException
from scrapy.utils.misc import arg_to_iter

import oss2
import magic
import requests

import pdfplumber
from PyPDF2 import PdfFileReader, PdfFileWriter
import fitz,img2pdf

import io
from scrapy.http.headers import Headers
from scrapy.utils.conf import get_config
from twisted.internet.defer import DeferredList
from datetime import datetime

logging.getLogger('pdfplumber').setLevel(logging.WARNING)
logging.getLogger('PyPDF2').setLevel(logging.WARNING)
logging.getLogger('pdfminer').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('oss2').setLevel(logging.WARNING)
logging.getLogger('img2pdf').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

class OSSFilesStore:
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

class OssFilesPipeline(MediaPipeline):
    MEDIA_NAME = "ossfile"
    STORE_SCHEMES = {
        'https': OSSFilesStore #新增阿里云文件存储类
    }
    DEFAULT_FILES_OSS_URLS_FIELD = 'raw_pdf_url'
    DEFAULT_FILES_OSS_RESULT_FIELD = 'pdf_url'
    DEFAULT_OSS_DOMAIN = 'https://xcc2.oss-cn-shenzhen.aliyuncs.com'
    FILTER_EMPTY_ITEM = False # 过滤字段urlimg为空的item
    def __init__(self, store_uri, file_pipe_config, download_func=None, settings=None,oss_file=None):
        if not store_uri:
            raise NotConfigured('You should config the FILE_PIPE_CONFIG to enable this pipeline')

        if isinstance(settings, dict) or settings is None:
            settings = Settings(settings)

        self.store = self._get_store(store_uri)

        if not get_config().get(section="oss_cfg",option="OSS_USER" ):# 提醒设置参数以及设置默认值
            raise NotConfigured("At scrapy.cfg missing 'OSS_USER'")
        if not get_config().get(section="oss_cfg",option="OSS_PASSWORD" ):
            raise NotConfigured("At scrapy.cfg missing 'OSS_PASSWORD'")
        if not get_config().get(section="oss_cfg",option="FILES_STORE" ):
            raise NotConfigured("At scrapy.cfg missing 'FILES_STORE'")
        if not settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('FILES_OSS_URLS_FIELD'):
            logging.warning("At custom_settings missing 'FILES_OSS_URLS_FIELD'")
        if not settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD'):
            logging.warning("At custom_settings missing 'FILES_OSS_RESULT_FIELD'")
        if not settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('RESOURCE_CLASSNAME'):
            logging.warning("At custom_settings missing 'RESOURCE_CLASSNAME'")

        self.oss_domain = settings.get(
            'OSS_DOMAIN', self.DEFAULT_OSS_DOMAIN
        )
        self.filter_empty_item = settings.get(
            'FILTER_EMPTY_ITEM', self.FILTER_EMPTY_ITEM
        )
        self.invalid_fild_paths = settings.get(
            #invalid_file_body
            'FILTER_INVALID_FILE_PATHS', []
        )
        self.files_oss_field = settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('FILES_OSS_URLS_FIELD', self.DEFAULT_FILES_OSS_URLS_FIELD)
        self.files_oss_result_field = settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD', self.DEFAULT_FILES_OSS_RESULT_FIELD)
        self.page_logo_text = settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('PAGE_LOGO_TEXT','')
        self.item_header_dict = settings.get('FILE_PIPE_CONFIG',{}).get(self.__class__.__name__,{}).get('ITEM_HEADER',None)
        self.files_oss_file = "/".join(["items",settings.attributes.get("OSS_FILE")])
        self.if_feed = settings.get('FEEDS').attributes
        self.file_pipe_config = file_pipe_config
        self.ext_model = settings.get('EXT_MODEL',False)
        super().__init__(download_func=download_func, settings=settings)

    @classmethod
    def from_settings(cls, settings,crawler=None):
        oss_store = cls.STORE_SCHEMES['https']
        file_pipe_config = settings.getdict('FILE_PIPE_CONFIG', {})
        if file_pipe_config and not file_pipe_config.get(cls.__name__,{}):
            logging.warning('错误警告:请检查管道和参数是否一一对应')

        oss_store.OSS_USERNAME = get_config().get(section="oss_cfg",option="OSS_USER" )
        oss_store.OSS_PASSWORD = get_config().get(section="oss_cfg",option="OSS_PASSWORD" )
        store_uri =get_config().get(section="oss_cfg",option="FILES_STORE" )
        oss_store.according_to = file_pipe_config.get(cls.__name__,{}).get('DEL_PDF_ACCORDING_TO',{})
        oss_store.check_num = file_pipe_config.get(cls.__name__,{}).get('DEL_PDF_CHECK_NUM',0)
        oss_store.deal_with_pdf = file_pipe_config.get(cls.__name__,{}).get('FILTER_PDF_PAGE',False)
        # 取爬虫源域名结合爬虫名hash成FILES_OSS_FILE做阿里云链接目录
        start_urls = crawler.spider.start_urls or [i.url for i in crawler.spider.start_requests()] 
        from urllib import parse
        if start_urls:
            domain = parse.urlparse(start_urls[0]).netloc
        else :
            domain = "default"
        oss_file = hashlib.sha1(to_bytes(domain)).hexdigest()[:9]
        settings.attributes["OSS_FILE"] = oss_file
        return cls(store_uri,file_pipe_config, settings=settings,)

    @classmethod
    def from_crawler(cls, crawler):
        try:
            pipe = cls.from_settings(crawler.settings,crawler)
        except AttributeError:
            pipe = cls()
        pipe.crawler = crawler
        return pipe
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls.from_settings(crawler.settings, crawler)
    def process_item(self, item, spider):
        info = self.spiderinfo
        requests = arg_to_iter(self.get_media_requests(item, info))
        dlist = [self._process_request(r, info, item) for r in requests]
        dfd = DeferredList(dlist, consumeErrors=1)
        return dfd.addCallback(self.item_completed, item, info)

    def _get_store(self, uri):
        '''
        判断uri
        '''
        if os.path.isabs(uri):  # to support win32 paths like: C:\\some\dir
            scheme = 'file'
        else:
            scheme = urlparse(uri).scheme
        if scheme != 'https':
            raise ValueError("settings文件中 FILES_STORE 不是阿里云域名")
        store_cls = self.STORE_SCHEMES[scheme]
        return store_cls(uri)

    def media_downloaded(self, response, request, info, *, item=None): # 判断是否正常资源
        referer = referer_str(request)
        if response.status != 200:
            logger.warning(
                'File (code: %(status)s): Error downloading file from '
                '%(request)s referred in <%(referer)s>',
                {'status': response.status,
                 'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('download-error')

        # response.body = content
        if magic.from_buffer(response.body, mime=True).split('/')[-1] == 'pdf':
            retry_invalid_times = 3
            for i in range(retry_invalid_times):
                # 如果pdf损坏重试
                try:
                    valid = fitz.Document(stream=response.body, filetype="pdf")
                    if valid.is_repaired:
                        raise FileException('download-error')
                    break
                except Exception as e:
                    headers = Headers(response.request.headers).to_unicode_dict()
                    logging.warn(f"请求头: {headers} , PDF下载异常: {e}")
                    contents = requests.get(response.request.url,headers = headers, timeout=(10,120)).content
                    response = response.replace(body=contents)
                    logging.info(f"Retry {i+1} times , Url is {response.request.url}")
                    if i+1 >= retry_invalid_times : raise
                
        media_ext_guss = os.path.splitext(os.path.basename(urlparse(request.url).path))[1]

        if media_ext_guss==".pdf":
            try:
                valid = fitz.Document(stream=response.body, filetype="pdf")
            except Exception as e:
                print(e)
                raise

        if self.invalid_fild_paths:
            # invalid_fild_path <list> :: 失效文件路径,表示遇到该文件内容与invalid_fild_path路径下内容一致时返回空
            invalid_file_body_list = list()
            for path in self.invalid_fild_paths:
                with open(f"{path}",'rb') as f:
                    invalid_file_body_list.append(f.read())
                if response.body in invalid_file_body_list:
                    return {'url': request.url, 'path': ''}

        if not response.body:
            logger.warning(
                'File (empty-content): Empty file from %(request)s referred '
                'in <%(referer)s>: no-content',
                {'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('empty-content')

        status = 'cached' if 'cached' in response.flags else 'downloaded'
        logger.debug(
            'File (%(status)s): Downloaded file from %(request)s referred in '
            '<%(referer)s>',
            {'status': status, 'request': request, 'referer': referer},
            extra={'spider': info.spider}
        )
        self.inc_stats(info.spider, status)

        try:
            path = self.file_path(request, response=response, info=info, item=item)
            checksum = self.file_downloaded(response, request, info, item=path)
        except FileException as exc:
            logger.warning(
                'File (error): Error processing file from %(request)s '
                'referred in <%(referer)s>: %(errormsg)s',
                {'request': request, 'referer': referer, 'errormsg': str(exc)},
                extra={'spider': info.spider}, exc_info=True
            )
            raise
        except Exception as exc:
            logger.error(
                'File (unknown-error): Error processing file from %(request)s '
                'referred in <%(referer)s>',
                {'request': request, 'referer': referer},
                exc_info=True, extra={'spider': info.spider}
            )
            raise FileException(str(exc))

        return {'url': request.url, 'path': path, 'checksum': checksum, 'status': status}
        

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
            urls = ItemAdapter(item).get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_URLS_FIELD",self.files_oss_field), '').split("|") \
                if ItemAdapter(item).get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_URLS_FIELD",self.files_oss_field), '') else []
            def request_add_params(urls):
                for u in urls:
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


    def file_downloaded(self, response, request, info, *, item=None):
        path = item
        buf = io.BytesIO(response.body)
        checksum = md5sum(buf)
        buf.seek(0)
        self.store.persist_file(path, buf, info)
        return checksum

    def item_completed(self, results, item, info):
        if self.file_pipe_config.get(self.__class__.__name__,{}).get("RESOURCE_CLASSNAME",'').lower() in item.__class__.__name__.lower():
            with suppress(TypeError):
                if '|'.join([x['path'] for ok, x in results if ok and x['path']]):
                    ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)] = '|'.join([x['path'] for ok, x in results if ok and x['path']])
            # TAG: 如果决定资源字段返回为空不存表,修改 FILTER_EMPTY_ITEM = True , 默认false
            with suppress(KeyError):
                if not item.get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_RESULT_FIELD",''),"") and self.filter_empty_item:
                    if self.if_feed :# 解决输出文件时出现bug情况
                        return {}
                    else:
                        raise DropItem()
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        media_guid = hashlib.sha1(response.body).hexdigest()
        media_ext_guss = os.path.splitext(os.path.basename(urlparse(request.url).path))[1]
        if not media_ext_guss and urlparse(request.url).netloc:# 若path为空则视为
            media_ext_guss = 'html'
        with suppress(AttributeError):
            kind = magic.from_buffer(response.body, mime=True).split('/')[-1]
            media_ext = '.'+kind
        if kind != media_ext_guss.strip(".") and (kind,media_ext_guss.strip(".") not in ['jpg','jpeg'])[1]: 
            #警告:出现文件流类型和链接拓展名不一致情况
            logging.warning(f"注意:原文件后缀名为( {media_ext_guss.strip('.')} )和判断文件类型( {kind} )不一致 资源链接如下{request.url}")
        if kind =='html': 
            # 如果判断结果为html,大概率下载失败
            with suppress(NameError):   
                logging.warning(f"下载文件为html,请确认是否下载成功,请求头:{str(Headers(request.headers, encoding='utf-8').to_unicode_dict())}")
                return ''
            media_ext = '.'+kind if not kind.startswith(".") else kind
        # if self.ext_model :
            # ext_model ::True表示当前情况适合用链接拓展名作为后缀;False表示当前适合用判断文件流来作为后缀
        normal_ext = [
            'jpg','png','jpeg','webp','svg','gif','tif','bmp',      #图片类
            'pdf','caj','zip','rar','csv','xlsx','xls','doc','ppt', #文档类
            'mp4','flv','rm','rmvb','avi','mov','mpeg',             #视频类
            'mp3','wav','wma'                                       #音频类
        ]
        if kind not in normal_ext and media_ext_guss.strip(".") in normal_ext: #如果判断结果非常见类型,链接拓展为常见类型,取源拓展名
            media_ext = media_ext_guss
        return f'{self.oss_domain}/{self.files_oss_file}/{media_guid}{media_ext}'

    def inc_stats(self, spider, status):
        spider.crawler.stats.inc_value('file_count', spider=spider)
        spider.crawler.stats.inc_value(f'file_status_count/{status}', spider=spider)


class OssPDFPipeline(OssFilesPipeline):
    def transf_img2_pdf(self,img_urls):
        stream_list = list()
        for img in img_urls.split('|'):
            stream_list.append(requests.get(img,timeout=10).content)
        path = ".".join([img.rsplit(".",1)[0],"pdf"])
        buf = io.BytesIO(img2pdf.convert(stream_list))
        self.store.persist_file(path,buf,info=None)
        return path

    def item_completed(self, results, item, info):
        if self.file_pipe_config.get(self.__class__.__name__,{}).get("RESOURCE_CLASSNAME",'').lower() in item.__class__.__name__.lower():
            with suppress(TypeError):
                file_urls = '|'.join([x['path'] for ok, x in results if ok])
                if file_urls :
                    if "png" in file_urls or "jpeg" in file_urls :
                        obj_path = self.transf_img2_pdf(file_urls)
                        ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)] = obj_path
                    else:
                        ItemAdapter(item)[self.file_pipe_config.get(self.__class__.__name__,{}).get('FILES_OSS_RESULT_FIELD',self.files_oss_result_field)] = '|'.join([x['path'] for ok, x in results if ok])
            # TAG: 如果决定资源字段返回为空不存表,修改 FILTER_EMPTY_ITEM = True , 默认false
            with suppress(KeyError):
                if not item.get(self.file_pipe_config.get(self.__class__.__name__,{}).get("FILES_OSS_RESULT_FIELD",''),"") and self.filter_empty_item:
                    if self.if_feed :# 解决输出文件时出现bug情况
                        return {}
                    else:
                        raise DropItem()
        return item

class OssFilesPipelineDatasheet(OssPDFPipeline):
    
    def media_downloaded(self, response, request, info, *, item=None):  # 判断是否正常资源
        referer = referer_str(request)
        # if response.status == 200:
        with pdfplumber.open(io.BytesIO(response.body)) as pdf:
            last_page = pdf.pages[0]
            first_page_txt = last_page.extract_text()
            if self.page_logo_text in first_page_txt and self.page_logo_text:
                raise FileException('Drop-Footer\'s-Page')
        if response.status != 200:
            logger.warning(
                'File (code: %(status)s): Error downloading file from '
                '%(request)s referred in <%(referer)s>',
                {'status': response.status,
                 'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('download-error')

        if not response.body:
            logger.warning(
                'File (empty-content): Empty file from %(request)s referred '
                'in <%(referer)s>: no-content',
                {'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('empty-content')

        status = 'cached' if 'cached' in response.flags else 'downloaded'
        logger.debug(
            'File (%(status)s): Downloaded file from %(request)s referred in '
            '<%(referer)s>',
            {'status': status, 'request': request, 'referer': referer},
            extra={'spider': info.spider}
        )
        self.inc_stats(info.spider, status)

        try:
            path = self.file_path(request, response=response, info=info, item=item)
            checksum = self.file_downloaded(response, request, info, item=path)
        except FileException as exc:
            logger.warning(
                'File (error): Error processing file from %(request)s '
                'referred in <%(referer)s>: %(errormsg)s',
                {'request': request, 'referer': referer, 'errormsg': str(exc)},
                extra={'spider': info.spider}, exc_info=True
            )
            raise
        except Exception as exc:
            logger.error(
                'File (unknown-error): Error processing file from %(request)s '
                'referred in <%(referer)s>',
                {'request': request, 'referer': referer},
                exc_info=True, extra={'spider': info.spider}
            )
            raise FileException(str(exc))

        return {'url': request.url, 'path': path, 'checksum': checksum, 'status': status}





class OssFilesPipelineBak(OssFilesPipeline): # 弃用
    pass

class OssFilesPipelineBakBak(OssFilesPipeline): #弃用
    pass

class OssPDFPipelineBak(OssPDFPipeline): # 备用文件储存类 如其他pdf
    pass

class OssPDFPipelineBakBak(OssPDFPipeline): #备用文件储存类
    pass

