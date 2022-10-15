import json

from ..annot.integration import IntegrationResultZarr
from ..files._integration import *


def _load_json(path):
    with open(path) as f:
        return json.load(f)


class BICCNIntegration:
    def __init__(self):
        self.MC_M3C_INTEGRATION_ZARR = MC_M3C_INTEGRATION_ZARR
        self.MC_ATAC_INTEGRATION_ZARR = MC_ATAC_INTEGRATION_ZARR
        self.MC_SMART_INTEGRATION_ZARR = MC_SMART_INTEGRATION_ZARR
        self.MC_AIBS_TENX_INTEGRATION_ZARR = MC_AIBS_TENX_INTEGRATION_ZARR
        self.MC_BROAD_TENX_INTEGRATION_ZARR = MC_BROAD_TENX_INTEGRATION_ZARR
        self.MC_L4_MULTIOME_ZARR = MC_L4_MULTIOME_ZARR

        # L4 Map Json
        self.MC_M3C_INTEGRATION_L4MAP_JSON = MC_M3C_INTEGRATION_L4MAP_JSON
        self.MC_ATAC_INTEGRATION_L4MAP_JSON = MC_ATAC_INTEGRATION_L4MAP_JSON
        self.MC_SMART_INTEGRATION_L4MAP_JSON = MC_SMART_INTEGRATION_L4MAP_JSON
        self.MC_AIBS_TENX_INTEGRATION_L4MAP_JSON = MC_AIBS_TENX_INTEGRATION_L4MAP_JSON
        self.MC_BROAD_TENX_INTEGRATION_L4MAP_JSON = MC_BROAD_TENX_INTEGRATION_L4MAP_JSON
        return

    def get_mc_m3c_integration(self):
        return IntegrationResultZarr(self.MC_M3C_INTEGRATION_ZARR)

    def get_mc_atac_integration(self):
        return IntegrationResultZarr(self.MC_ATAC_INTEGRATION_ZARR)

    def get_mc_smart_integration(self):
        return IntegrationResultZarr(self.MC_SMART_INTEGRATION_ZARR)

    def get_mc_aibs_tenx_integration(self):
        return IntegrationResultZarr(self.MC_AIBS_TENX_INTEGRATION_ZARR)

    def get_mc_broad_tenx_integration(self):
        return IntegrationResultZarr(self.MC_BROAD_TENX_INTEGRATION_ZARR)

    def get_mc_to_m3c_l4_map(self):
        return _load_json(self.MC_M3C_INTEGRATION_L4MAP_JSON)

    def get_mc_to_atac_l4_map(self):
        return _load_json(self.MC_ATAC_INTEGRATION_L4MAP_JSON)

    def get_mc_to_smart_l4_map(self):
        return _load_json(self.MC_SMART_INTEGRATION_L4MAP_JSON)

    def get_mc_to_aibs_tenx_l4_map(self):
        return _load_json(self.MC_AIBS_TENX_INTEGRATION_L4MAP_JSON)

    def get_mc_to_broad_tenx_l4_map(self):
        return _load_json(self.MC_BROAD_TENX_INTEGRATION_L4MAP_JSON)


biccn_integration = BICCNIntegration()
