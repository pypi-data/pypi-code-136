# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['octodns_netbox', 'tests']

package_data = \
{'': ['*'], 'tests': ['fixtures/*']}

install_requires = \
['octodns>=0.9.20,<0.10.0',
 'pydantic>=1.10.2,<2.0.0',
 'pynetbox>=6.6.2,<7.0.0',
 'requests>=2.25.1,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.2.0,<5.0.0']}

setup_kwargs = {
    'name': 'octodns-netbox',
    'version': '0.2.0',
    'description': 'A NetBox source for octoDNS.',
    'long_description': '#  A [NetBox](https://github.com/digitalocean/netbox) source for [octoDNS](https://github.com/github/octodns/)\n\n[![PyPI](https://img.shields.io/pypi/v/octodns-netbox)](https://pypi.python.org/pypi/octodns-netbox)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/octodns-netbox)](https://pypi.python.org/pypi/octodns-netbox)\n[![PyPI - License](https://img.shields.io/pypi/l/octodns-netbox)](LICENSE)\n[![Code Climate coverage](https://img.shields.io/codeclimate/coverage/sukiyaki/octodns-netbox)](https://codeclimate.com/github/sukiyaki/octodns-netbox)\n[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/sukiyaki/octodns-netbox)](https://codeclimate.com/github/sukiyaki/octodns-netbox)\n\nYou can have complete control over your DNS records with Netbox!\n\n⚠️ This is a **source** for octoDNS! We can only serve to populate records into a zone, cannot be synced **to** Netbox.\n\n## Getting started\n\n### A records / AAAA records\n\nThis source retrieves IP address information from Netbox and creates A/AAAA records for octoDNS. For this purpose, it is essential to manage the mapping between IP addresses and FQDNs in Netbox. We use a `description` field as a comma-separated list of hostnames (FQDNs).\n\n#### 🚨 `dns_name` field\nStarting with [Netbox v2.6.0](https://github.com/netbox-community/netbox/issues/166), IPAddress now has a `dns_name` field. But we **do not** use this field by default because this `dns_name` field can only store **single** FQDN. To use a `dns_name` field, set `field_name: dns_name` in [the configuration](#example-configuration).\n\n#### 🔍 Example\n- IP Address: `192.0.2.1/24`\n  - Description: `en0.host1.example.com,host1.example.com`\n- DNS Zone: `example.com.`\n  - `en0.host1. A 192.0.2.1`\n  - `host1. A 192.0.2.1`\n\n### PTR records\n\nPTR records supported as well. OctoDNS [supports Multiple PTR records on a single IP](https://github.com/octodns/octodns/pull/754), but it is not ot used much in productions. By default, `multivalue_ptr: false` is set and the first FQDN in the field will be used to generate the PTR record.\n\n#### 🔍 Example (`multivalue_ptr: false` - default)\n- IP Address: `192.0.2.1/24`\n  - Description: `en0.host1.example.com,host1.example.com`\n- DNS Zone: `2.0.192.in-addr.arpa.`\n  - `1. PTR en0.host1.example.com`\n\n#### 🔍 Example (`multivalue_ptr: true`)\n- IP Address: `192.0.2.1/24`\n  - Description: `en0.host1.example.com,host1.example.com`\n- DNS Zone: `2.0.192.in-addr.arpa.`\n  - `1. PTR en0.host1.example.com`\n  - `1. PTR host1.example.com`\n\n#### Classless subnet delegation (IPv4 /31 to /25)\n\nWhen creating classless reverse lookup zones, we support two notation as the following ones:\n\n- `<subnet>-<subnet mask bit count>.2.0.192.in-addr.arpa` ([RFC 4183](https://www.rfc-editor.org/rfc/rfc4183.html) alike) or\n- `<subnet>/<subnet mask bit count>.2.0.192.in-addr.arpa` ([RFC 2317](https://www.ietf.org/rfc/rfc2317.html) alike)\n\n## Example Configuration\n\nYou must configure `url` and `token` to work with the [NetBox API](https://netbox.readthedocs.io/en/latest/api/overview/).\n\n```yaml\nproviders:\n  netbox:\n    class: octodns_netbox.NetboxSource\n    # Your Netbox URL\n    url: https://ipam.example.com\n    # Your Netbox Access Token (read-only)\n    token: env/NETBOX_TOKEN\n    # The TTL of the generated records (Optional, default: 60)\n    ttl: 60\n    #\n    # !!!!! Advanced Parameters !!!!!\n    # Just ignore below and no need to write these lines in your yaml.\n    #\n    # Generate records including subdomains (Optional, default: `true`)\n    # If `false`, only records that belong directly to the zone (domain) will be generated.\n    # If you are seeing a lot of `SubzoneRecordException` in your logs, change this to `false`.\n    populate_subdomains: true\n    # FQDN field name (Optional, default: `description`)\n    # The `dns_name` field on Netbox is provided to hold only a single name,\n    # but typically one IP address will correspond to multiple DNS records (FQDNs).\n    # The `description` does not have any limitations so by default\n    # we use the `description` field to store multiple FQDNs, separated by commas.\n    # Tested: `description`, `dns_name`\n    field_name: description\n    # Tag Name (Optional)\n    # By default, all records are retrieved from Netbox, but it can be restricted\n    # to only IP addresses assigned a specific tag.\n    populate_tags:\n      - tag_name\n      - passing multiple values will result in a logical AND operation\n    # VRF ID (Optional)\n    # By default, all records are retrieved from Netbox, but it can be restricted\n    # to only IP addresses assigned a specific VRF ID.\n    # If `0`, explicitly points for global VRF.\n    populate_vrf_id: 1\n    # VRF Name (Optional)\n    # VRF can also be specified by name.\n    # If there are multiple VRFs with the same name, it would be better to use `populate_vrf_id`.\n    # If `Global`, explicitly points for global VRF.\n    populate_vrf_name: mgmt\n    # Multi-value PTR records support (Optional, default: `false`)\n    # If `true`, multiple-valued PTR records will be generated.\n    # If `false`, the first FQDN value in the field will be used.\n    multivalue_ptr: true\n\n  route53:\n    class: octodns_route53.Route53Provider\n    access_key_id: env/AWS_ACCESS_KEY_ID\n    secret_access_key: env/AWS_SECRET_ACCESS_KEY\n\nzones:\n  example.com.:\n    sources:\n      - netbox  # will add A/AAAA records\n    targets:\n      - route53\n\n  0/26.2.0.192.in-addr.arpa.:\n    sources:\n      - netbox  # will add PTR records (corresponding to A records)\n    targets:\n      - route53\n\n  0.8.b.d.0.1.0.0.2.ip6.arpa:\n    sources:\n      - netbox  # will add PTR records (corresponding to AAAA records)\n    targets:\n      - route53\n```\n\n## Contributing\nSee [the contributing guide](CONTRIBUTING.md) for detailed instructions on how to get started with our project.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Masaki Tagawa',
    'author_email': 'masaki@sukiyaki.ski',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sukiyaki/octodns-netbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
