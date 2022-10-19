'''
#import dpugen
import pdb
import dpugen.dash.dash as ds
conf = ds.DashConfig()
ds.common_parse_args(conf)
pdb.set_trace()

for i in conf.items():
    for j in i:
        print (j)
    
#conf.generate()
#ds.common_output(conf)
print('done')
'''

# Constants for scale outbound
NUMBER_OF_VIP = 1
NUMBER_OF_DLE = 2
NUMBER_OF_ENI = 2
NUMBER_OF_EAM = NUMBER_OF_ENI
NUMBER_OF_ORE = 2  # Per ENI
NUMBER_OF_OCPE = 2  # Per ORE
NUMBER_OF_VNET = NUMBER_OF_ENI + (NUMBER_OF_ORE * NUMBER_OF_ENI)  # So far per ORE, but may be different
NUMBER_OF_IN_ACL_GROUP = 10
NUMBER_OF_OUT_ACL_GROUP = 10

TEST_VNET_OUTBOUND_CONFIG_SCALE = {

    'DASH_VIP': {
        'vpe': {
            'count': NUMBER_OF_VIP,
            'SWITCH_ID': '$SWITCH_ID',
            'IPV4': {
                'count': NUMBER_OF_VIP,
                'start': '172.16.1.100',
                'step': '0.1.0.0'
            }
        }
    },

    'DASH_DIRECTION_LOOKUP': {
        'dle': {
            'count': NUMBER_OF_DLE,
            'SWITCH_ID': '$SWITCH_ID',
            'VNI': {
                'count': NUMBER_OF_DLE,
                'start': 5000,
                'step': 1000
            },
            'ACTION': 'SET_OUTBOUND_DIRECTION'
        }
    },

    'DASH_ACL_GROUP': {
        'in_acl_group_id': {
            'count': NUMBER_OF_IN_ACL_GROUP,
            'ADDR_FAMILY': 'IPv4'
        },
        'out_acl_group_id': {
            'count': NUMBER_OF_OUT_ACL_GROUP,
            'ADDR_FAMILY': 'IPv4'
        }
    },

    'DASH_VNET': {
        'vnet': {
            'VNI': {
                'count': NUMBER_OF_VNET,
                'start': 1000,
                'step': 1000
            }
        }
    },

    'DASH_ENI': {
        'eni': {
            'count': NUMBER_OF_ENI,
            'ACL_GROUP': {
                'INBOUND': {
                    'STAGE1': {
                        'list': 'DASH_ACL_GROUP#in_acl_group_id#0'
                    },
                    'STAGE2': {
                        'list': 'DASH_ACL_GROUP#in_acl_group_id#0'
                    },
                    'STAGE3': {
                        'list': 'DASH_ACL_GROUP#in_acl_group_id#0'
                    },
                    'STAGE4': {
                        'list': 'DASH_ACL_GROUP#in_acl_group_id#0'
                    },
                    'STAGE5': {
                        'list': 'DASH_ACL_GROUP#in_acl_group_id#0'
                    }
                },
                'OUTBOUND': {
                    'STAGE1': 0,
                    'STAGE2': 0,
                    'STAGE3': 0,
                    'STAGE4': 0,
                    'STAGE5': 0
                }
            },
            'ADMIN_STATE': True,
            'CPS': 10000,
            'FLOWS': 10000,
            'PPS': 100000,
            'VM_UNDERLAY_DIP': {
                'count': NUMBER_OF_ENI,
                'start': '172.16.1.1',
                'step': '0.0.1.0'
            },
            'VM_VNI': {
                'count': NUMBER_OF_ENI,
                'start': 9
            },
            'VNET_ID': {
                'count': NUMBER_OF_ENI,
                'start': '$vnet_#{4}'
            }
        }
    },

    'DASH_ENI_ETHER_ADDRESS_MAP': {
        'eam': {
            'count': NUMBER_OF_EAM,
            'SWITCH_ID': '$SWITCH_ID',
            'MAC': {
                'count': NUMBER_OF_EAM,
                'start': '00:CC:CC:CC:00:00',
                'step': "00:00:00:00:00:01"
            },
            'ENI_ID': {
                'count': NUMBER_OF_ENI,
                'start': '$eni_#{0}'
            }
        }
    },

    'DASH_OUTBOUND_ROUTING': {
        'ore': {
            'count': NUMBER_OF_ENI * NUMBER_OF_ORE,  # Full count: OREs per ENI and VNET
            'SWITCH_ID': '$SWITCH_ID',
            'ACTION': 'ROUTE_VNET',
            'DESTINATION': {
                'count': NUMBER_OF_ORE,
                'start': '10.1.1.0/31',
                'step': '0.0.0.2'
            },
            'ENI_ID': {
                'count': NUMBER_OF_ENI,
                'start': '$eni_#{0}',
                'delay': NUMBER_OF_ORE
            },
            'DST_VNET_ID': {
                'count': NUMBER_OF_VNET,
                'start': '$vnet_#{0}',
                'delay': NUMBER_OF_ORE
            }
        }
    },

    'DASH_OUTBOUND_CA_TO_PA': {
        'ocpe': {
            'count': (NUMBER_OF_ENI * NUMBER_OF_ORE) * NUMBER_OF_OCPE,  # 2 Per ORE
            'SWITCH_ID': '$SWITCH_ID',
            'DIP': {
                'count': NUMBER_OF_ORE * NUMBER_OF_OCPE,
                'start': '10.1.1.0',
                'step': '0.0.0.1'
            },
            'DST_VNET_ID': {
                'count': NUMBER_OF_VNET,
                'start': '$vnet_#{0}',
                'delay': NUMBER_OF_ORE
            },
            'UNDERLAY_DIP': {
                'count': NUMBER_OF_ENI * NUMBER_OF_ORE,
                'start': '172.16.1.20',
                'step': '0.0.1.0'
            },
            'OVERLAY_DMAC': {
                'count': NUMBER_OF_ENI * NUMBER_OF_ORE,
                'start': '00:DD:DD:DD:00:00'
            },
            'USE_DST_VNET_VNI': True
        }
    }
}

import dpugen.sai.sai as sa

conf = sa.SaiConfig()
import pdb;pdb.set_trace()
sa.common_parse_args(conf)
conf.mergeParams(TEST_VNET_OUTBOUND_CONFIG_SCALE)
conf.generate()

conf.args.output = "x_vnet_outbound_setup_commands_scale.json"
sa.common_output(conf)
print('done')
