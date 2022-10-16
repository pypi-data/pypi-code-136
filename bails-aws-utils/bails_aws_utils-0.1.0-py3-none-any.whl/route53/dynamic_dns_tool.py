import logging

import boto3
import requests

from bails_aws_utils.misc.cron_helper import create_cron


class DynamicDnsTool:
    @staticmethod
    def get_public_ip():
        res = requests.get("https://api.ipify.org")
        if res.status_code != 200:
            raise Exception(
                f"Failed to get public IP, status code: {res.status_code}"
            )
        return res.text

    @staticmethod
    def set_record(ip, prefix, domain):
        client = boto3.client("route53")
        response = client.list_hosted_zones_by_name(DNSName=domain)
        for zone in response["HostedZones"]:
            if zone["Name"] == domain:
                zone_id = zone["Id"]
                logging.info(f"Found matching hosted zone: {zone_id}")
                break
        if zone_id is None:
            raise Exception(f"No hosted zones found for domain: {domain}")

        response = client.change_resource_record_sets(
            HostedZoneId=zone_id,
            ChangeBatch={
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": prefix + "." + domain,
                            "Type": "A",
                            "TTL": 60,
                            "ResourceRecords": [{"Value": ip}],
                        },
                    }
                ]
            },
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
            raise Exception(
                f'Failed to create A record, status code: {response["ResponseMetadata"]["HTTPStatusCode"]}'
            )

    @staticmethod
    def setup_cron(domain, prefix, interval=60, cron=None, **kwargs):
        create_cron(
            f"dynamic-dns -p {prefix} -d {domain}", interval, cron, **kwargs
        )
