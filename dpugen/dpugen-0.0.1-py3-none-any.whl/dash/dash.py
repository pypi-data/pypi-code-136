#!/usr/bin/python3

import dpugen.dash as ds
from dpugen.confbase import *
from dpugen.confutils import *

print('generating config')

parser = commonArgParser()
args = parser.parse_args()


class DashConfig(ConfBase):

    def __init__(self, params={}):
        super().__init__('dash-config', params)
        self.generate()

    def generate(self):
        # Pass top-level params to sub-generrators.
        self.configs = [
            ds.enis.Enis(self.params_dict),
            ds.aclgroups.AclGroups(self.params_dict),
            ds.vpcs.Vpcs(self.params_dict),
            ds.vpcmappingtypes.VpcMappingTypes(self.params_dict),
            ds.vpcmappings.VpcMappings(self.params_dict),
            ds.routingappliances.RoutingAppliances(self.params_dict),
            ds.routetables.RouteTables(self.params_dict),
            ds.prefixtags.PrefixTags(self.params_dict),
        ]

    def toDict(self):
        return {x.dictName(): x.items() for x in self.configs}

    def items(self):
        return (c.items() for c in self.configs)


if __name__ == "__main__":
    conf = DashConfig()
    common_parse_args(conf)
    conf.generate()
    common_output(conf)
    print('done')
