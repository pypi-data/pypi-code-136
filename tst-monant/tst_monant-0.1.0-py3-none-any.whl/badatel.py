import copy
import logging

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess

from central_storage_connectors import api_support
from data_providers.schemas.html import HTML
from master.listener_helper import listener_helper


db_logger = logging.getLogger('DBMessageLogger')


class BadatelSpider(CrawlSpider):
    name = "badatel"
    home_page = "https://www.badatel.net/"
    allowed_domains = ["badatel.net"]
    start_urls = ["https://www.badatel.net"]

    # Allow every link to be parsed
    rules = (
        Rule(LinkExtractor(allow='/category/*'), follow=True),
        Rule(LinkExtractor(allow='/tag/*'), follow=True),
        Rule(LinkExtractor(allow=('/[a-zA-Z0-9\-]+')), callback='parse_item'),
        Rule(LinkExtractor(deny='/odkazy-forum/')),
        Rule(LinkExtractor(deny='/o-nas/')),
        Rule(LinkExtractor(deny='/nase-produkty/')),
        Rule(LinkExtractor(deny='/checkout/')),
        Rule(LinkExtractor(deny='/kontakt/')),
    )

    def __init__(self, *args, **kwargs):
        """Function is called when the spider is initialized

        Keyword arguments:
        args -- full paths of start urls with protocol (http, https), separated by ','
        """

        home_page = "https://www.badatel.net"

        self.data_provider_id = kwargs.pop('data_provider_id')
        self.monitor_id = kwargs.pop('monitor_id')
        self.extraction_id = kwargs.pop('extraction_id')
        self.events = kwargs.pop('events')

        db_logger.info(
            f"""
            LOG: Started to crawl Badatel. 
            """,
            extra={'extraction_id': self.extraction_id}
        )

        self.visited_urls = api_support.get_visited_links_by_monitor(self.monitor_id)
        if self.visited_urls:
            # Removing protocol + hostname from url
            visited_urls = [x.replace(home_page, '') for x in self.visited_urls]

            # Dynamically init Rule by already visited urls
            BadatelSpider.rules += (Rule(LinkExtractor(deny=visited_urls)),)

        super(BadatelSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        web_url = response.url

        if (web_url != self.home_page) and (web_url not in self.visited_urls):
            self.visited_urls.append(web_url)
            uuid_result = api_support.post_portal_html(
                HTML({
                    'html': response.text,
                    'url': web_url,
                    'monitor_id': self.monitor_id
                })
            )

            event = {
                'id': 'new-article',
                'type': 'data-provider-chain'
            }
            attributes = {
                'urls': [],
                'html_uuids': [uuid_result],
                'data_provider_config': copy.deepcopy(self.events.get('new-article'))
            }

            listener_helper.trigger(
                event,
                attributes,
                self.data_provider_id,
                self.monitor_id,
                self.extraction_id
            )


def start_crawl(events, data_provider_id, monitor_id, extraction_id):
    """ Function helps to start crawl in script """
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(
        BadatelSpider,
        data_provider_id=data_provider_id,
        monitor_id=monitor_id,
        extraction_id=extraction_id,
        events=events
    )
    process.start()
