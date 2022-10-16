from bails_aws_utils.route53.utils import Route53Utils


def create_gmail_mx_record(domain):
    utils = Route53Utils()
    zone_id = utils.get_hosted_zone_id(domain)
    utils.client.create_record(
        hosted_zone_id=zone_id,
        name=domain,
        type="MX",
        ttl=300,
        values=[
            "1 ASPMX.L.GOOGLE.COM.",
            "5 ALT1.ASPMX.L.GOOGLE.COM.",
            "5 ALT2.ASPMX.L.GOOGLE.COM.",
            "10 ALT3.ASPMX.L.GOOGLE.COM.",
            "10 ALT4.ASPMX.L.GOOGLE.COM.",
            # "15 eb4k3uhmpff3uamz5gm5qnyrde5ixojpmtizigp6s2ehzcwrpdwa.mx-verification.google.com.",
        ],
    )
