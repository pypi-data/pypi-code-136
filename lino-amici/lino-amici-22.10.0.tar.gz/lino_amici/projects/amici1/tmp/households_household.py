# -*- coding: UTF-8 -*-
logger.info("Loading 14 objects to table households_household...")
# fields: partner_ptr, type
loader.save(create_households_household(191,1))
loader.save(create_households_household(192,2))
loader.save(create_households_household(193,3))
loader.save(create_households_household(194,4))
loader.save(create_households_household(195,5))
loader.save(create_households_household(196,6))
loader.save(create_households_household(213,1))
loader.save(create_households_household(214,2))
loader.save(create_households_household(215,1))
loader.save(create_households_household(216,1))
loader.save(create_households_household(229,1))
loader.save(create_households_household(230,2))
loader.save(create_households_household(231,2))
loader.save(create_households_household(232,1))

loader.flush_deferred_objects()
