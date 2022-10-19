# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table cal_room...")
# fields: id, name, company, contact_person, contact_role, display_color, description
loader.save(create_cal_room(1,['School', 'School', 'School'],None,None,None,'Blue',''))
loader.save(create_cal_room(2,['Youth center', 'Youth center', 'Youth center'],None,None,None,'Blue',''))
loader.save(create_cal_room(3,['Library', 'Library', 'Library'],None,None,None,'Blue',''))

loader.flush_deferred_objects()
