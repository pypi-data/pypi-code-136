from bails_aws_utils.route53.utils import Route53Utils


def create_gmail_mx_record(domain):
    utils = Route53Utils()
    zone_id = utils.get_hosted_zone_id(domain)
    utils.client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": domain,
                        "Type": "MX",
                        "TTL": 300,
                        "ResourceRecords": [
                            {"Value": "1 ASPMX.L.GOOGLE.COM."},
                            {"Value": "5 ALT1.ASPMX.L.GOOGLE.COM."},
                            {"Value": "5 ALT2.ASPMX.L.GOOGLE.COM."},
                            {"Value": "10 ALT3.ASPMX.L.GOOGLE.COM."},
                            {"Value": "10 ALT4.ASPMX.L.GOOGLE.COM."},
                        ],
                    },
                }
            ]
        },
    )
