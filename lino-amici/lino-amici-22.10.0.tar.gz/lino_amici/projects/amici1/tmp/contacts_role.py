# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table contacts_role...")
# fields: id, type, person, company, start_date, end_date
loader.save(create_contacts_role(1,1,113,101,None,None))
loader.save(create_contacts_role(2,1,168,104,None,None))
loader.save(create_contacts_role(3,1,168,100,None,None))

loader.flush_deferred_objects()
