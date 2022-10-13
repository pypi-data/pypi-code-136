# -*- coding: utf-8 -*-

import copy
import arrow
from pprint import pprint
from enum import Enum


class TimeUnit(Enum):
    """
    请求报告参数、必填、"timeUnit"

    timeUnit can be set to "DAILY" or "SUMMARY".
    If you set timeUnit to "DAILY", you should include "date" in your column list.
    If you set timeUnit to "SUMMARY" you can include "startDate" and "endDate" in your column list.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/get-started#timeunit-and-supported-columns

    Records:
    1) DAILY = ["date", "startDate", "endDate"]
    {"code":"400","detail":"configuration startDate and endDate are not supported columns for DAILY time unit. Please use date instead."}

    2) SUMMARY = ["startDate", "endDate", "date"]
    {"code":"400","detail":"configuration date is not a supported column for SUMMARY time unit. Please use startDate and/or endDate instead."}
    """
    DAILY = ["date"]
    SUMMARY = ["startDate", "endDate"]

    def __init__(self, columns):
        """Easy dot access like: TimeUnit.SUMMARY.columns"""
        self.columns = columns


class GroupBy(Enum):
    """
    请求报告参数、必填、"groupBy"

    所有报告请求都需要报告配置中的参数。确定报告的粒度级别。如果报告类型支持，您可以在请求中使用多个值。

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/get-started#groupby
    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types
    """
    pass


class AdsV3ReportsAdapter(object):

    _report_type_id: str = None
    _maximum_date_range: int = None  # days
    _data_retention: int = None  # days
    _time_unit_choices: tuple = ("SUMMARY", "DAILY")
    _group_by_choices: tuple = None
    _base_metrics: list = None
    _format: str = "GZIP_JSON"

    class GroupBy(Enum):
        def __init__(self, columns):
            self.columns = columns

    def __init__(self,
                 group_by: list,
                 time_unit: str,
                 start_date: str,
                 end_date: str,
                 name: str = None):
        assert set(group_by) in self._group_by_choices
        group_by.sort()
        self.group_by = group_by

        assert time_unit in self._time_unit_choices
        self.time_unit = time_unit

        assert arrow.get(end_date) > arrow.get(start_date), ":::ERROR: end_date < start_date !!!"
        assert (arrow.get(end_date) - arrow.get(start_date)).days <= self._maximum_date_range, \
            "The maximum time range is exceeded"
        self.start_date = start_date  # "2022-07-01"
        self.end_date = end_date  # "2022-07-10"

        if not name:
            name = "%s_%s_%s_%s_%s_%s" % (self._report_type_id, self.start_date, self.end_date, '_'.join(self.group_by),
                                          self.time_unit, arrow.utcnow().isoformat())
        self.name = name

    def get_columns(self):
        columns = copy.deepcopy(self._base_metrics)
        for _gb in self.group_by:
            columns += self.GroupBy[_gb].columns
        columns += TimeUnit[self.time_unit].columns
        return columns

    def get_data_raw(self):
        raise NotImplementedError


class SPCampaignReportsAdapter(AdsV3ReportsAdapter):
    """
    Campaign reports contain performance data broken down at the campaign level.
    Campaign reports include all campaigns of the requested sponsored ad type that have performance activity for the requested days.
    For example, a Sponsored Products campaign report returns performance data for all Sponsored Products campaigns that received impressions on the chosen dates.
    Campaign reports can also be grouped by ad group and placement for more granular data.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types#campaign-reports
    """

    _report_type_id = "spCampaigns"
    _maximum_date_range = 31
    _data_retention = 95
    _group_by_choices = (
        {"campaign"},
        {"adGroup"},
        {"campaignPlacement"},
        {"campaign", "adGroup"},
        {"campaign", "campaignPlacement"},
        # {"adGroup", "campaignPlacement"},  # FAILED
        # {"campaign", "adGroup", "campaignPlacement"},  # FAILED
    )

    _base_metrics = [
        "impressions",
        "clicks",
        "cost",
        "purchases1d",
        "purchases7d",
        "purchases14d",
        "purchases30d",
        "purchasesSameSku1d",
        "purchasesSameSku7d",
        "purchasesSameSku14d",
        "purchasesSameSku30d",
        "unitsSoldClicks1d",
        "unitsSoldClicks7d",
        "unitsSoldClicks14d",
        "unitsSoldClicks30d",
        "sales1d",
        "sales7d",
        "sales14d",
        "sales30d",
        "attributedSalesSameSku1d",
        "attributedSalesSameSku7d",
        "attributedSalesSameSku14d",
        "attributedSalesSameSku30d",
        "unitsSoldSameSku1d",
        "unitsSoldSameSku7d",
        "unitsSoldSameSku14d",
        "unitsSoldSameSku30d",
        "kindleEditionNormalizedPagesRead14d",
        "kindleEditionNormalizedPagesRoyalties14d",
        # "date",
        # "startDate",
        # "endDate",
        "campaignBiddingStrategy",
        "costPerClick",
        "clickThroughRate",
        "spend",
    ]

    class GroupBy(Enum):

        campaign = [
            "campaignName",
            "campaignId",
            "campaignStatus",
            "campaignBudgetAmount",
            "campaignBudgetType",
            "campaignRuleBasedBudgetAmount",
            "campaignApplicableBudgetRuleId",
            "campaignApplicableBudgetRuleName",
            "campaignBudgetCurrencyCode",
        ]

        adGroup = [
            "adGroupName",
            "adGroupId",
            "adStatus",
        ]

        campaignPlacement = [
            "placementClassification",
        ]

        def __init__(self, columns):
            """Easy dot access like: GroupBy.campaign.columns"""
            self.columns = columns

    def get_data_raw(self):
        data = {
            "name": self.name,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": self.group_by,
                "columns": self.get_columns(),
                "reportTypeId": self._report_type_id,
                "timeUnit": self.time_unit,
                "format": self._format
            }
        }
        return data


class SPTargetingReportsAdapter(AdsV3ReportsAdapter):
    """
    Targeting reports contain performance metrics broken down by both targeting expressions and keywords.
    To see only targeting expressions, set the keywordType filter to TARGETING_EXPRESSION and TARGETING_EXPRESSION_PREDEFINED.
    To see only keywords, set the keywordType filter to BROAD, PHRASE, and EXACT.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types#targeting-reports
    """

    _report_type_id = "spTargeting"
    _maximum_date_range = 31
    _data_retention = 95
    _group_by_choices = (
        {"targeting"},
    )

    _base_metrics = [
        'impressions',
        'clicks',
        'costPerClick',
        'clickThroughRate',
        'cost',
        'purchases1d',
        'purchases7d',
        'purchases14d',
        'purchases30d',
        'purchasesSameSku1d',
        'purchasesSameSku7d',
        'purchasesSameSku14d',
        'purchasesSameSku30d',
        'unitsSoldClicks1d',
        'unitsSoldClicks7d',
        'unitsSoldClicks14d',
        'unitsSoldClicks30d',
        'sales1d',
        'sales7d',
        'sales14d',
        'sales30d',
        'attributedSalesSameSku1d',
        'attributedSalesSameSku7d',
        'attributedSalesSameSku14d',
        'attributedSalesSameSku30d',
        'unitsSoldSameSku1d',
        'unitsSoldSameSku7d',
        'unitsSoldSameSku14d',
        'unitsSoldSameSku30d',
        'kindleEditionNormalizedPagesRead14d',
        'kindleEditionNormalizedPagesRoyalties14d',
        'salesOtherSku7d',
        'unitsSoldOtherSku7d',
        'acosClicks7d',
        'acosClicks14d',
        'roasClicks7d',
        'roasClicks14d',
        'keywordId',
        'keyword',
        'campaignBudgetCurrencyCode',
        # 'date',
        # 'startDate',
        # 'endDate',
        'portfolioId',
        'campaignName',
        'campaignId',
        'campaignBudgetType',
        'campaignBudgetAmount',
        'campaignStatus',
        'keywordBid',
        'adGroupName',
        'adGroupId',
        'keywordType',
        'matchType',
        'targeting',
    ]

    class GroupBy(Enum):

        targeting = [
            "adKeywordStatus",
        ]

        def __init__(self, columns):
            """Easy dot access like: GroupBy.targeting.columns"""
            self.columns = columns

    def get_data_raw(self):
        data = {
            "name": self.name,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": self.group_by,
                "columns": self.get_columns(),
                "reportTypeId": self._report_type_id,
                "timeUnit": self.time_unit,
                "format": self._format
            }
        }
        return data


class SPSearchTermReportsAdapter(AdsV3ReportsAdapter):
    """
    Search term reports contain search term performance metrics broken down by targeting expressions and keywords.
    Use the keywordType filter to include either targeting expressions or keywords in your report.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types#search-term-reports
    """

    _report_type_id = "spSearchTerm"
    _maximum_date_range = 31
    _data_retention = 95
    _group_by_choices = (
        {"searchTerm"},
    )

    _base_metrics = [
        'impressions',
        'clicks',
        'costPerClick',
        'clickThroughRate',
        'cost',
        'purchases1d',
        'purchases7d',
        'purchases14d',
        'purchases30d',
        'purchasesSameSku1d',
        'purchasesSameSku7d',
        'purchasesSameSku14d',
        'purchasesSameSku30d',
        'unitsSoldClicks1d',
        'unitsSoldClicks7d',
        'unitsSoldClicks14d',
        'unitsSoldClicks30d',
        'sales1d',
        'sales7d',
        'sales14d',
        'sales30d',
        'attributedSalesSameSku1d',
        'attributedSalesSameSku7d',
        'attributedSalesSameSku14d',
        'attributedSalesSameSku30d',
        'unitsSoldSameSku1d',
        'unitsSoldSameSku7d',
        'unitsSoldSameSku14d',
        'unitsSoldSameSku30d',
        'kindleEditionNormalizedPagesRead14d',
        'kindleEditionNormalizedPagesRoyalties14d',
        'salesOtherSku7d',
        'unitsSoldOtherSku7d',
        'acosClicks7d',
        'acosClicks14d',
        'roasClicks7d',
        'roasClicks14d',
        'keywordId',
        'keyword',
        'campaignBudgetCurrencyCode',
        # 'date',
        # 'startDate',
        # 'endDate',
        'portfolioId',
        'searchTerm',
        'campaignName',
        'campaignId',
        'campaignBudgetType',
        'campaignBudgetAmount',
        'campaignStatus',
        'keywordBid',
        'adGroupName',
        'adGroupId',
        'keywordType',
        'matchType',
        'targeting',
        # 'adKeywordStatus',
    ]

    class GroupBy(Enum):

        searchTerm = [
            "adKeywordStatus",
        ]

        def __init__(self, columns):
            """Easy dot access like: GroupBy.searchTerm.columns"""
            self.columns = columns

    def get_data_raw(self):
        data = {
            "name": self.name,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": self.group_by,
                "columns": self.get_columns(),
                "reportTypeId": self._report_type_id,
                "timeUnit": self.time_unit,
                "format": self._format
            }
        }
        return data


class SPAdvertisedProductReportsAdapter(AdsV3ReportsAdapter):
    """
    Advertised product reports contain performance data for products that are advertised as part of your campaigns.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types#advertised-product-reports
    """

    _report_type_id = "spAdvertisedProduct"
    _maximum_date_range = 31
    _data_retention = 95
    _group_by_choices = (
        {"advertiser"},
    )

    _base_metrics = [
        # 'date',
        # 'startDate',
        # 'endDate',
        'campaignName',
        'campaignId',
        'adGroupName',
        'adGroupId',
        'adId',
        'portfolioId',
        'impressions',
        'clicks',
        'costPerClick',
        'clickThroughRate',
        'cost',
        'spend',
        'campaignBudgetCurrencyCode',
        'campaignBudgetAmount',
        'campaignBudgetType',
        'campaignStatus',
        'advertisedAsin',
        'advertisedSku',
        'purchases1d',
        'purchases7d',
        'purchases14d',
        'purchases30d',
        'purchasesSameSku1d',
        'purchasesSameSku7d',
        'purchasesSameSku14d',
        'purchasesSameSku30d',
        'unitsSoldClicks1d',
        'unitsSoldClicks7d',
        'unitsSoldClicks14d',
        'unitsSoldClicks30d',
        'sales1d',
        'sales7d',
        'sales14d',
        'sales30d',
        'attributedSalesSameSku1d',
        'attributedSalesSameSku7d',
        'attributedSalesSameSku14d',
        'attributedSalesSameSku30d',
        'salesOtherSku7d',
        'unitsSoldSameSku1d',
        'unitsSoldSameSku7d',
        'unitsSoldSameSku14d',
        'unitsSoldSameSku30d',
        'unitsSoldOtherSku7d',
        'kindleEditionNormalizedPagesRead14d',
        'kindleEditionNormalizedPagesRoyalties14d',
        'acosClicks7d',
        'acosClicks14d',
        'roasClicks7d',
        'roasClicks14d',
    ]

    class GroupBy(Enum):

        advertiser = []

        def __init__(self, columns):
            """Easy dot access like: GroupBy.advertiser.columns"""
            self.columns = columns

    def get_data_raw(self):
        data = {
            "name": self.name,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": self.group_by,
                "columns": self.get_columns(),
                "reportTypeId": self._report_type_id,
                "timeUnit": self.time_unit,
                "format": self._format
            }
        }
        return data


class SPPurchasedProductReportsAdapter(AdsV3ReportsAdapter):
    """
    Sponsored Products purchased product reports contain performance data for products that were purchased,
    but were not advertised as part of a campaign.
    The purchased product report contains both targeting expressions and keyword IDs.
    After you have received your report,
    you can filter on keywordType to distinguish between targeting expressions and keywords.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types#purchased-product-reports
    """

    _report_type_id = "spPurchasedProduct"
    _maximum_date_range = 31
    _data_retention = 95
    _group_by_choices = (
        {"asin"},
    )

    _base_metrics = [
        # 'date',
        # 'startDate',
        # 'endDate',
        'portfolioId',
        'campaignName',
        'campaignId',
        'adGroupName',
        'adGroupId',
        'keywordId',
        'keyword',
        'keywordType',
        'advertisedAsin',
        'purchasedAsin',
        'advertisedSku',
        'campaignBudgetCurrencyCode',
        'matchType',
        'unitsSoldClicks1d',
        'unitsSoldClicks7d',
        'unitsSoldClicks14d',
        'unitsSoldClicks30d',
        'sales1d',
        'sales7d',
        'sales14d',
        'sales30d',
        'purchases1d',
        'purchases7d',
        'purchases14d',
        'purchases30d',
        'unitsSoldOtherSku1d',
        'unitsSoldOtherSku7d',
        'unitsSoldOtherSku14d',
        'unitsSoldOtherSku30d',
        'salesOtherSku1d',
        'salesOtherSku7d',
        'salesOtherSku14d',
        'salesOtherSku30d',
        'purchasesOtherSku1d',
        'purchasesOtherSku7d',
        'purchasesOtherSku14d',
        'purchasesOtherSku30d',
        'kindleEditionNormalizedPagesRead14d',
        'kindleEditionNormalizedPagesRoyalties14d',
    ]

    class GroupBy(Enum):

        asin = []

        def __init__(self, columns):
            """Easy dot access like: GroupBy.asin.columns"""
            self.columns = columns

    def get_data_raw(self):
        data = {
            "name": self.name,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "configuration": {
                "adProduct": "SPONSORED_PRODUCTS",
                "groupBy": self.group_by,
                "columns": self.get_columns(),
                "reportTypeId": self._report_type_id,
                "timeUnit": self.time_unit,
                "format": self._format
            }
        }
        return data


class SBPurchasedProductReportsAdapter(AdsV3ReportsAdapter):
    """
    Sponsored Brands purchased product reports contain performance data for products that were purchased as a result of your campaign.

    https://advertising.amazon.com/API/docs/en-us/reporting/v3/report-types#sponsored-brands
    """

    _report_type_id = "sbPurchasedProduct"
    _maximum_date_range = 731
    _data_retention = 731
    _group_by_choices = (
        {"purchasedAsin"},
    )

    _base_metrics = [
        # 'date',
        # 'startDate',
        # 'endDate',
        'budgetCurrency',
        'campaignBudgetCurrencyCode',
        'campaignName',
        'adGroupName',
        'attributionType',
        'purchasedAsin',
        'productName',
        'productCategory',
        'sales14d',
        'orders14d',
        'unitsSold14d',
        'newToBrandSales14d',
        'newToBrandOrders14d',
        'newToBrandPurchases14d',
        'newToBrandUnitsSold14d',
        'newToBrandSalesPercentage14d',
        'newToBrandOrdersPercentage14d',
        'newToBrandPurchasesPercentage14d',
        'newToBrandUnitsSoldPercentage14d',
    ]

    class GroupBy(Enum):

        purchasedAsin = []

        def __init__(self, columns):
            """Easy dot access like: GroupBy.purchasedAsin.columns"""
            self.columns = columns

    def get_data_raw(self):
        data = {
            "name": self.name,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "configuration": {
                "adProduct": "SPONSORED_BRANDS",  # different
                "groupBy": self.group_by,
                "columns": self.get_columns(),
                "reportTypeId": self._report_type_id,
                "timeUnit": self.time_unit,
                "format": self._format
            }
        }
        return data


if __name__ == '__main__':
    # test_1 = SPCampaignReportsAdapter(
    #     group_by=["campaign"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_1_data = test_1.get_data_raw()
    # pprint(test_1_data)

    # test_2 = SPCampaignReportsAdapter(
    #     group_by=["campaign"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_2_data = test_2.get_data_raw()
    # pprint(test_2_data)

    # test_3 = SPCampaignReportsAdapter(
    #     group_by=["adGroup"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_3_data = test_3.get_data_raw()
    # pprint(test_3_data)

    # test_4 = SPCampaignReportsAdapter(
    #     group_by=["adGroup"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_4_data = test_4.get_data_raw()
    # pprint(test_4_data)

    # test_5 = SPCampaignReportsAdapter(
    #     group_by=["campaignPlacement"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_5_data = test_5.get_data_raw()
    # pprint(test_5_data)

    # test_6 = SPCampaignReportsAdapter(
    #     group_by=["campaignPlacement"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_6_data = test_6.get_data_raw()
    # pprint(test_6_data)

    # test_7 = SPCampaignReportsAdapter(
    #     group_by=["campaign", "adGroup"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_7_data = test_7.get_data_raw()
    # pprint(test_7_data)

    # test_8 = SPCampaignReportsAdapter(
    #     group_by=["campaign", "adGroup"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_8_data = test_8.get_data_raw()
    # pprint(test_8_data)

    # test_9 = SPCampaignReportsAdapter(
    #     group_by=["campaign", "campaignPlacement"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_9_data = test_9.get_data_raw()
    # pprint(test_9_data)

    # test_10 = SPCampaignReportsAdapter(
    #     group_by=["campaign", "campaignPlacement"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_10_data = test_10.get_data_raw()
    # pprint(test_10_data)

    # TODO FAILED !!! failureReason: Report generation failed due to an internal error. Please retry
    # test_11 = SPCampaignReportsAdapter(
    #     group_by=["adGroup", "campaignPlacement"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_11_data = test_11.get_data_raw()
    # pprint(test_11_data)

    # TODO FAILED !!! failureReason: Report generation failed due to an internal error. Please retry
    # test_12 = SPCampaignReportsAdapter(
    #     group_by=["adGroup", "campaignPlacement"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_12_data = test_12.get_data_raw()
    # pprint(test_12_data)

    # TODO FAILED !!! failureReason: Report generation failed due to an internal error. Please retry
    # test_13 = SPCampaignReportsAdapter(
    #     group_by=["campaign", "adGroup", "campaignPlacement"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_13_data = test_13.get_data_raw()
    # pprint(test_13_data)

    # TODO FAILED !!! failureReason: Report generation failed due to an internal error. Please retry
    # test_14 = SPCampaignReportsAdapter(
    #     group_by=["campaign", "adGroup", "campaignPlacement"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_14_data = test_14.get_data_raw()
    # pprint(test_14_data)

    # test_15 = SPTargetingReportsAdapter(
    #     group_by=["targeting"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_15_data = test_15.get_data_raw()
    # pprint(test_15_data)

    # test_16 = SPTargetingReportsAdapter(
    #     group_by=["targeting"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_16_data = test_16.get_data_raw()
    # pprint(test_16_data)

    # test_17 = SPSearchTermReportsAdapter(
    #     group_by=["searchTerm"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_17_data = test_17.get_data_raw()
    # pprint(test_17_data)

    # test_18 = SPSearchTermReportsAdapter(
    #     group_by=["searchTerm"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_18_data = test_18.get_data_raw()
    # pprint(test_18_data)

    # test_19 = SPAdvertisedProductReportsAdapter(
    #     group_by=["advertiser"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_19_data = test_19.get_data_raw()
    # pprint(test_19_data)

    # test_20 = SPAdvertisedProductReportsAdapter(
    #     group_by=["advertiser"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_20_data = test_20.get_data_raw()
    # pprint(test_20_data)

    # test_21 = SPPurchasedProductReportsAdapter(
    #     group_by=["asin"], time_unit="DAILY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_21_data = test_21.get_data_raw()
    # pprint(test_21_data)

    # test_22 = SPPurchasedProductReportsAdapter(
    #     group_by=["asin"], time_unit="SUMMARY", start_date="2022-07-01", end_date="2022-07-31",
    # )
    # test_22_data = test_22.get_data_raw()
    # pprint(test_22_data)

    # test_23 = SBPurchasedProductReportsAdapter(
    #     group_by=["purchasedAsin"], time_unit="DAILY", start_date="2021-07-01", end_date="2022-07-01",
    # )
    # test_23_data = test_23.get_data_raw()
    # pprint(test_23_data)

    test_24 = SBPurchasedProductReportsAdapter(
        group_by=["purchasedAsin"], time_unit="SUMMARY", start_date="2021-07-01", end_date="2022-07-01",
    )
    test_24_data = test_24.get_data_raw()
    pprint(test_24_data)
