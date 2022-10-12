"""
介绍：
入参：
效果：
例子：
"""
from scrapy.xcc_pipelines.ossfilepipelines import OssFilesPipeline,OssFilesPipelineBak
try:
    from scrapy.xcc_pipelines.ossfilepipelines import OssPDFPipeline,OssPDFPipelineBak
except:
    print("请尽快升级 scrapy-team >= 1.2.16 版本")
