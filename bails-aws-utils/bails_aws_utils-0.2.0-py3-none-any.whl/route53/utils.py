import logging

import boto3


class Route53Utils:
    def __init__(self, client=None):
        if client is None:
            self.client = boto3.client("route53")
        else:
            self.client = client

    def get_hosted_zone_id(self, domain):
        domain = Route53Utils.format_domain(domain)
        response = self.client.list_hosted_zones_by_name(DNSName=domain)
        for zone in response["HostedZones"]:
            if zone["Name"] == domain:
                zone_id = zone["Id"]
                logging.info(f"Found matching hosted zone: {zone_id}")
                return zone_id
        if zone_id is None:
            raise Exception(f"No hosted zones found for domain: {domain}")

    @staticmethod
    def format_domain(domain):
        if domain[-1] != ".":
            domain += "."
        return domain
