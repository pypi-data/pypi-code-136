from djangoldp.permissions import LDPPermissions
from djangoldp_resource.filters import ResourceFilterBackend
from pprint import pprint


class ResourcePermissions(LDPPermissions):
    with_cache = False
    filter_backends = [ResourceFilterBackend]
    