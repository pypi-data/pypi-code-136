# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table households_type...")
# fields: id, name
loader.save(create_households_type(1,['Married couple', 'Ehepaar', 'Couple marié']))
loader.save(create_households_type(2,['Divorced couple', 'Geschiedenes Paar', 'Couple divorcé']))
loader.save(create_households_type(3,['Factual household', 'Faktischer Haushalt', 'Cohabitation de fait']))
loader.save(create_households_type(4,['Legal cohabitation', 'Legale Wohngemeinschaft', 'Cohabitation légale']))
loader.save(create_households_type(5,['Isolated', 'Getrennt', 'Isolé']))
loader.save(create_households_type(6,['Other', 'Sonstige', 'Autre']))

loader.flush_deferred_objects()
