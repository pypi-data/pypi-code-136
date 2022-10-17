import copy
import logging
#from scrapy.spiders import CrawlSpider, Rule


#class BadatelSpider(CrawlSpider):
class BadatelSpider():
    """Does some stuff

    Args:
      foo (int): The foo to bar
      foo2 (int): The foo2 to bar
      bar (str): Bar to use on foo
      baz (float): Baz to frobnicate

    Returns:
      float: The frobnicated baz
    """

    name = "badatel"
    home_page = "https://www.badatel.net/"
    allowed_domains = ["badatel.net"]
    start_urls = ["https://www.badatel.net"]

    def __init__(self, *args, **kwargs):
        """Function is called when the spider is initialized

        Keyword arguments:
        args -- full paths of start urls with protocol (http, https), separated by ','
        """

        home_page = "https://www.badatel.net"

 #       self.data_provider_id = kwargs.pop('data_provider_id')



