# -*- coding: utf-8 -*-

from amazon_ad.api_v3.base import ZADOpenAPIV3
from amazon_ad.api_v3.adapters import SBPurchasedProductReportsAdapter


class SbReportV3(ZADOpenAPIV3):

    def request(self, data: dict):
        path = "/reporting/reports"
        return self.post(path, data)

    def purchased_asin_daily(self, start_date: str, end_date: str):
        data = SBPurchasedProductReportsAdapter(
            group_by=["purchasedAsin"], time_unit="DAILY", start_date=start_date, end_date=end_date,
        ).get_data_raw()
        return self.request(data)

    def purchased_asin_summary(self, start_date: str, end_date: str):
        data = SBPurchasedProductReportsAdapter(
            group_by=["purchasedAsin"], time_unit="SUMMARY", start_date=start_date, end_date=end_date,
        ).get_data_raw()
        return self.request(data)
