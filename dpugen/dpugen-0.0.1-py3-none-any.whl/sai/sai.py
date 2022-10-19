#!/usr/bin/python3

import dpugen.sai as sa
from dpugen.confbase import *
from dpugen.confutils import *
print('generating config')

parser = commonArgParser()
args = parser.parse_args()


class SaiConfig(ConfBase):

    def __init__(self, params={}):
        super().__init__(params)

    def generate(self):
        # Pass top-level params to sub-generrators.
        self.configs = [
            sa.vips.Vips(self.params_dict),
            sa.direction_lookup.DirectionLookup(self.params_dict),
            sa.acl_groups.AclGroups(self.params_dict),
            sa.vnets.Vnets(self.params_dict),
            sa.enis.Enis(self.params_dict),
            sa.address_maps.AddressMaps(self.params_dict),
            sa.inbound_routing.InboundRouting(self.params_dict),
            sa.pa_validation.PaValidation(self.params_dict),
        ]

    # def toDict(self):
    #     return {x.dictName(): x.items() for x in self.configs}

    def items(self):
        result = []
        for c in self.configs:
            result.extend(c.items())
        return result
        #[c.items() for c in self.configs]
        #[].extend(c.items() for c in self.configs)


if __name__ == '__main__':
    conf = SaiConfig()
    common_parse_args(conf)
    conf.generate()
    common_output(conf)
    print('done')
