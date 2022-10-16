from pandas import read_excel
from typing import Optional
from scrapy.spiders import Spider
from scrapy.utils.spider import iterate_spider_output
from scrapy.exceptions import NotConfigured


class XLSSpider(Spider):
    """Scrapy spider for parsing XLS files.
    It receives a XLS file in a response; iterates through each of its rows,
    and calls parse_row with a dict containing each field's data.

    You can set some options regarding the XLS file, such as the sheet names 
    and number of rows to be skiped.
    If sheets are not provided, it'll returns all sheets available.
    """

    skip_rows: Optional[int] = 0
    sheets: Optional[list] = [None]

    def process_results(self, response, results):
        """This method has the same purpose as the one in XMLFeedSpider"""
        return results

    def adapt_response(self, response):
        """This method has the same purpose as the one in XMLFeedSpider"""
        return response

    def parse_row(self, response, sheet, row):
        """This method must be overriden with your custom spider functionality"""
        raise NotImplementedError

    def parse_rows(self, response):
        """Receives a response and a dict (representing each row) with a key for
        each provided (or detected) header of the XLS file.  This spider also
        gives the opportunity to override adapt_response and
        process_results methods for pre and post-processing purposes.
        """
        for sheet in self.sheets:
            for sheet_name, row in self.xlsiter(response, sheet):
                ret = iterate_spider_output(self.parse_row(response, sheet_name, row))
                for result_item in self.process_results(response, ret):
                    yield result_item

    def _parse(self, response, **kwargs):
        if not hasattr(self, 'parse_row'):
            raise NotConfigured('You must define parse_row method in order to scrape this XLS file')
        response = self.adapt_response(response)
        return self.parse_rows(response)

    def xlsiter(self, response, sheet=None):
        """Receives the raw response of the xls file and extract all the values within the
        available sheets, no sheet is provided will get all sheets available. It yields a
        tuple containing the sheet_name and the extructured data.
        """
        raw_data = response.body
        df_kwargs = dict(io=raw_data, sheet_name=sheet, skiprows=self.skip_rows)
        df = read_excel(**df_kwargs)

        if sheet:
            df = {
                sheet: df
            }
        sheet_names = df.keys()
        for sheet_name in sheet_names:
            headers = df[sheet_name].keys()
            for rows in df[sheet_name].values:
                yield sheet_name, dict(zip(headers, rows))
