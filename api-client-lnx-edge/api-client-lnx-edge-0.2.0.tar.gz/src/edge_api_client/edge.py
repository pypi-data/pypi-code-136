import requests
from typing import List
from datetime import datetime, date

from .base import BaseAPIClient
from .utilities import get_dayparting, format_adjustment_date, build_filters, build_daterange


class EdgeAPI(BaseAPIClient):

    def get_offers(self, entity_id=None, **kwargs) -> requests.Response:
        """ Get all offers or specify by `entity_id`

        :param entity_id: (optional) an Edge offer ID. Returns all offers if not specified.
        :return: response
        """
        return self.get_entity('offers', entity_id=entity_id, **kwargs)

    def get_advertisers(self, entity_id=None, **kwargs) -> requests.Response:
        """ Get all advertisers or specify by `entity_id`

        :param entity_id: (optional) an Edge Advertiser ID. Returns all advertisers if not specified.
        :return: response
        """
        return self.get_entity('advertisers', entity_id=entity_id, **kwargs)

    def get_affiliates(self, entity_id=None, **kwargs) -> requests.Response:
        """ Get all affiliates or specify by `entity_id`

        :param entity_id: (optional) an Edge Affiliate ID. Returns all affiliates if not specified.
        :return: response
        """
        return self.get_entity('affiliates', entity_id=entity_id, **kwargs)

    def get_products(self, entity_id=None, **kwargs) -> requests.Response:
        """ Get all products or limit to advertiser with `entity_id`

        :param entity_id: (optional) an Edge Advertiser ID. Returns all products if not specified.
        :return: response
        """
        params = {'advertiser_id': entity_id} if entity_id else {}
        return self.get_entity('products', params=params, **kwargs)

    def get_request(self, request_id, **kwargs) -> requests.Response:
        """ Get metadata for an Edge request.

        :param request_id: an Edge request ID
        :return: response
        """
        return self.get_entity('requests', entity_id=request_id, **kwargs)

    def get_past_changes(self, **kwargs) -> requests.Response:
        """ Return executed changes recorded in Changelog. """
        return self.get_entity('audit/search/', **kwargs)

    def get_scheduled_changes(self, **kwargs) -> requests.Response:
        """ Return scheduled changes that have yet to be executed. """
        return self._post('schedule/search', **kwargs)

    def get_affiliate_offer_settings(self, affiliate_id, offer_id, **kwargs) -> requests.Response:
        """ Return affiliate offer settings for a given aff+offer.

        :param affiliate_id: valid affiliate ID
        :param offer_id: valid offer ID
        :return: response
        """
        params = {'affiliateId': str(affiliate_id), 'offerId': str(offer_id)}
        return self.get_entity('affiliate-offer-settings', params=params, **kwargs)

    def create_offer(self,
                     friendly_name: str,
                     category: int,
                     description: str,
                     domain: int,
                     error_fallback_url: str,
                     filter_fallback_url: str,
                     filter_fallback_product: str,
                     dayparting: dict,
                     filters: List[dict],
                     destination: dict,
                     status: str = 'Active',
                     viewability: str = 'Testing',  # default
                     scrub: int = 0,
                     default_affiliate_conversion_cap: int = 0,
                     lifetime_affiliate_click_cap: int = 0,
                     traffic_types: List = None,
                     pixel_behavior: str = 'dedupe',
                     allow_query_passthrough: bool = True,
                     allow_pageview_pixel: bool = True,
                     allow_forced_click_conversion: bool = False,
                     creatives: List[int] = None,
                     unsubscribe_link: str = '',
                     suppression_list: str = '',
                     from_lines: str = '',
                     subject_lines: str = '',
                     redirect_offer: int = 0,
                     redirect_percent: float = 0,
                     cap_redirect_offer: int = 0
                     ) -> requests.Response:

        body = {
            'friendly_name': friendly_name,
            'category': category,
            'description': description,
            'domain': domain,
            'customFallbackUrl': error_fallback_url,
            'filterFallbackUrl': filter_fallback_url,
            'filterFallbackProduct': filter_fallback_product,
            'dayparting': {},
            'filters': {'filters': filters or []},
            'destination': destination,
            'status': status,
            'viewability': viewability,
            'scrub': scrub,
            'defaultAffiliateConvCap': default_affiliate_conversion_cap,
            'lifetimeAffiliateClickCap': lifetime_affiliate_click_cap,
            'trafficTypes': traffic_types or [],
            'pixelBehavior': pixel_behavior,
            'allowQueryPassthrough': allow_query_passthrough,
            'allowPageviewPixel': allow_pageview_pixel,
            'allowForcedClickConversion': allow_forced_click_conversion,
            'creatives': creatives or [],
            'unsubscribe_link': unsubscribe_link,
            'suppression_list': suppression_list,
            'from_lines': from_lines,
            'subject_lines': subject_lines,
            'redirectOffer': redirect_offer,
            'redirectPercent': redirect_percent,
            'capRedirectOffer': cap_redirect_offer
        }

        if dayparting:
            if not any([x.get('type') == 'weekHour' for x in body['filters']['filters']]):
                body['filters']['filters'].append({
                    'type': 'weekHour',
                    'include': get_dayparting(dayparting)
                })
            else:
                raise ValueError('Providing both `dayparting` and a `weekHour` filter is ambiguous.')

        return self._post('api/offers', json=body)

    def create_offer_from_json(self, create_body: dict) -> requests.Response:
        """ Create an offer by inputting valid JSON without any of the arguments.

        :param create_body: valid offer creation POST body
        :return: API response
        """
        if 'dayparting' in create_body.keys():
            if 'filters' in create_body.keys():
                if 'filters' in create_body['filters'].keys():
                    if not any([x.get('type') == 'weekHour' for x in create_body['filters']['filters']]):
                        dayparting = get_dayparting(create_body)
                        if dayparting:
                            create_body['filters']['filters'].append({
                                'type': 'weekHour',
                                'include': dayparting
                            })

        return self._post('api/offers', json=create_body)

    def _get_report(self,
                    dimensions: list,
                    start_date: (datetime, date, str),
                    end_date: (datetime, date, str),
                    timezone: str = 'America/New_York',
                    metrics: list = None,
                    filters: list = None,
                    rows_per_page: int = 10000,
                    row_offset: int = 0,
                    **kwargs) -> requests.Response:

        report_config = {
            'dimensions': dimensions,
            'metrics': metrics or ['sessions', 'clicks', 'conversions', 'paidConversions', 'lnxRevenue', 'lnxCost'],
            'dateRange': build_daterange(start_date, end_date),
            'timezone': timezone,
            'filters': build_filters(filters or [], **kwargs),
            'tableSort': {},
            'rowsPerPage': rows_per_page,
            'rowOffset': row_offset
        }

        # Overrides report_config with passed-in kwargs, but doesn't add any NEW keys to dict. Allows user to pass
        #  filters like `affiliate_id=XXXX` with ease.
        report_config.update((k, kwargs[k]) for k in report_config.keys() & kwargs.keys())

        resp = self._post('api/reports', json=report_config)

        return resp

    def get_advertiser_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default advertiser report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['advertiserId', 'advertiserName'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_affiliate_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default affiliate report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['affiliateId', 'affiliateCompany'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_click_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default click report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['clickId', 'created_on', 'affiliateId', 'affiliateCompany', 'offerId', 'offerName',
                        's1', 's2', 's3', 's4', 's5', 'ipaddress', 'go_disposition'],
            metrics=['conversions', 'paidConversions', 'lnxProfit', 'lnxRevenue', 'lnxCost'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_daily_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default daily report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['timestampDay'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_hourly_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default hourly report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['timestampDay', 'hourOfDay'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_offer_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default offer report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['offerId', 'offerName'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_paid_conversion_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default paid conversion report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['clickId', 'created_on', 'affiliateId', 'affiliateCompany', 'offerId', 'offerName',
                        's1', 's2', 's3', 's4', 's5', 'ipaddress'],
            metrics=['lnxProfit', 'lnxRevenue', 'lnxCost'],
            filters=[{'type': 'gt', 'value': 0, 'column': 'paidConversions'}],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_product_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default product report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['productId', 'productName'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_sessions_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default sessions report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['clickId', 'created_on', 'affiliateId', 'affiliateCompany', 'offerId', 'offerName',
                        's1', 's2', 's3', 's4', 's5', 'ipaddress', 'go_disposition'],
            metrics=['clicks', 'conversions', 'paidConversions', 'lnxProfit', 'lnxRevenue', 'lnxCost'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_suboffer_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default suboffer report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['subOfferId', 'subOfferName'],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_total_conversion_report(self, start_date: (datetime, date, str), end_date: (datetime, date, str), **kwargs) -> requests.Response:
        """ Get default total conversion report.

        :param start_date: YYYY-MM-DD date
        :param end_date: YYYY-MM-DD date
        :return: response
        """
        return self._get_report(
            dimensions=['clickId', 'created_on', 'affiliateId', 'affiliateCompany', 'offerId', 'offerName',
                        's1', 's2', 's3', 's4', 's5', 'ipaddress'],
            metrics=['lnxProfit', 'lnxRevenue', 'lnxCost'],
            filters=[{'type': 'gt', 'value': 0, 'column': 'conversions'}],
            start_date=start_date,
            end_date=end_date,
            **kwargs
        )

    def get_custom_report(self, report_config, **kwargs) -> requests.Response:
        """ Get a custom report with a json body.

        :param report_config: a valid Edge report config body
        :return: response
        """
        return self._post('api/reports', json=report_config, **kwargs)

    def adjust(self, affiliate_id, offer_id_path: list, created_on: str, click_adjustment=0, conversion_adjustment=0,
               total_conversion_adjustment=0, conversion_amount_adjustment=0.00, payout_adjustment=0.00) -> requests.Response:
        data = {
            'affiliateId': affiliate_id,
            'offerIdPath': offer_id_path,
            'clickAdjustment': click_adjustment,
            'conversionAdjustment': conversion_adjustment,  # Paid conv, and total if that's not provided
            'conversionAmountAdjustment': conversion_amount_adjustment,
            'payoutAdjustment': payout_adjustment,
            'createdOn': format_adjustment_date(created_on)
        }

        if total_conversion_adjustment:
            data['totalConversionAdjustment'] = total_conversion_adjustment

        resp = self._post('api/adjust-stats', json=data)

        return resp

    def __repr__(self):
        return f'EdgeAPI(staging={self.staging})'
