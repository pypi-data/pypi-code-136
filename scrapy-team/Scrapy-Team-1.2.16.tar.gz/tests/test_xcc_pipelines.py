# from scrapy.xcc_pipelines.ossfilepipelines import OssFilesPipeline



# pipelines_object = OssFilesPipeline()

# if __name__=="__main__":
#     item = {}
#     pipelines_object.get_media_requests()
from typing import Optional
from scrapy.xcc_items.factoryitems import FactoryMaterialItem
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'test_xcc_osspipelines'
    start_urls = [
        'https://www.baidu.com'
        ]
    custom_settings: Optional[dict]={
        # "ITEM_PIPELINES" : {
        #     'scrapy.xcc_pipelines.ossfilepipelines.OssFilesPipeline': 300,
        #     'scrapy.xcc_pipelines.ossimgpipelines.OssImagesPipeline': 300,
        #     # 'scrapy.xcc_pipelines.ossotherfilepipelines.OssOtherFilesPipeline': 300,
        #     },
        # "SPIDER_MIDDLEWARES" : {
        #     'scrapy.xcc_spidermiddlewares.itemheaders.ItemHeadersMiddleware': 543,
        #     },
        "DEFAULT_REQUEST_HEADERS" : {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            },
    }

    def parse(self, response):
        item = FactoryMaterialItem()
        # item["raw_pdf_url"] = "https://4donline.ihs.com/images/VipMasterIC/IC/IDTI/IDTID002/IDTID002-5.8-1.pdf?hkey=EF798316E3902B6ED9A73243A3159BB0"
        # item["raw_pdf_url"] = "https://atta.szlcsc.com/upload/public/pdf/source/20170814/C125564_1502678332187885827.pdf"
        # item["raw_pdf_url"] = "https://4donline.ihs.com/images/VipMasterIC/IC/TOSL/TOSLS01262/TOSLS01262-1.pdf?hkey=EF798316E3902B6ED9A73243A3159BB0"
        # item["raw_pdf_url"] = "http://www.a1semi.com/UploadFile/file/2021-04/210410164926.jpg"
        # item["raw_pdf_url"] = "https://www.semiee.com/file/FITPOWER/FITPOWER-FP6606AC.pdf"
        # item["raw_pdf_url"] = "https://atta.szlcsc.com/upload/public/pdf/source/20210922/C2856808_4E6DDE2793CFD9EF09B771A8BD3338A4.pdf" # Overwriting cache for 0 133
        # item["raw_pdf_url"] = "http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F1857008%7FB%7Fpdf%7FEnglish%7FENG_CD_1857008_B.pdf%7F1857008-1" #后缀非pdf情况 
        # item["raw_pdf_url"] = 'https://pic1.zhimg.com/50/v2-eeb4193a1ac0dac9237197f7838aec6a_720w.jpg?source=b1f6dc53|https://pic2.zhimg.com/50/v2-f463d84e2fe64b7580bfaee676b003b6_720w.jpg?source=b1f6dc53'
        # item["raw_pdf_url"] = 'https://xcc2.oss-cn-shenzhen.aliyuncs.com/DataSheet_Pdf/files/a87794b3a8777f3d04e50969249138d834b4d286.pdf'
        # item["raw_pdf_url"] = 'https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/276273bbe/5f8cf070e6997578c01a32add038cb6f8a7e9080.pdf'
        item["raw_img_url"] = 'https://pic1.zhimg.com/50/v2-eeb4193a1ac0dac9237197f7838aec6a_720w.jpg?source=b1f6dc53'
        item["raw_pdf_url"] = 'https://atta.szlcsc.com/upload/public/pdf/source/20170814/C125564_1502678332187885827.pdf|https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/276273bbe/5f8cf070e6997578c01a32add038cb6f8a7e9080.pdf'
        # item["raw_other_pdf_url"] = {
        #                 "num1":"http://www.a1semi.com/UploadFile/file/2021-04/210410164926.jpg",
        #                 "num2":"https://atta.szlcsc.com/upload/public/pdf/source/20170814/C125564_1502678332187885827.pdf|https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/276273bbe/5f8cf070e6997578c01a32add038cb6f8a7e9080.pdf",
        #                 "num3":"https://xcc2.oss-cn-shenzhen.aliyuncs.com/items/276273bbe/5f8cf070e6997578c01a32add038cb6f8a7e9080.pdf"
        #                 }
        # item._refer = "www.zhihu.com"
        # item._header = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        #     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        #     'Accept-Encoding': 'gzip, deflate, br',
        #     'Connection': 'keep-alive',
        #     'Upgrade-Insecure-Requests': '1',
        #     'Sec-Fetch-Dest': 'document',
        #     'Sec-Fetch-Mode': 'navigate',
        #     'Sec-Fetch-Site': 'none',
        #     'Sec-Fetch-User': '?1',
        #     'referer':"www.datasheet5.com",
        #     }
        yield item