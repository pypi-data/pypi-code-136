# -*- coding: UTF-8 -*-
logger.info("Loading 9 objects to table countries_country...")
# fields: name, isocode, short_code, iso3
loader.save(create_countries_country(['Bangladesh', 'Bangladesh', 'Bangladesh'],'BD','',''))
loader.save(create_countries_country(['Belgium', 'Belgien', 'Belgique'],'BE','',''))
loader.save(create_countries_country(['Congo (Democratic Republic)', 'Kongo (Demokratische Republik)', 'Congo (République democratique)'],'CD','',''))
loader.save(create_countries_country(['Germany', 'Deutschland', 'Allemagne'],'DE','',''))
loader.save(create_countries_country(['Estonia', 'Estland', 'Estonie'],'EE','',''))
loader.save(create_countries_country(['France', 'Frankreich', 'France'],'FR','',''))
loader.save(create_countries_country(['Maroc', 'Marokko', 'Maroc'],'MA','',''))
loader.save(create_countries_country(['Netherlands', 'Niederlande', 'Pays-Bas'],'NL','',''))
loader.save(create_countries_country(['Russia', 'Russland', 'Russie'],'RU','',''))

loader.flush_deferred_objects()
