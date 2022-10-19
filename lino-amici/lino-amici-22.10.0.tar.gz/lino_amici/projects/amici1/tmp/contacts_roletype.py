# -*- coding: UTF-8 -*-
logger.info("Loading 5 objects to table contacts_roletype...")
# fields: id, name, can_sign
loader.save(create_contacts_roletype(1,['CEO', 'Geschäftsführer', 'Gérant'],True))
loader.save(create_contacts_roletype(2,['Director', 'Direktor', 'Directeur'],True))
loader.save(create_contacts_roletype(3,['Secretary', 'Sekretär', 'Secrétaire'],False))
loader.save(create_contacts_roletype(4,['IT manager', 'EDV-Manager', 'Gérant informatique'],False))
loader.save(create_contacts_roletype(5,['President', 'Präsident', 'Président'],True))

loader.flush_deferred_objects()
