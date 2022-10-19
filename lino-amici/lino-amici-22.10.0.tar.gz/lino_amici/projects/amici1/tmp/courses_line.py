# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table courses_line...")
# fields: id, ref, name, company, contact_person, contact_role, excerpt_title, course_area, topic, description, every_unit, every, event_type, guest_role, body_template
loader.save(create_courses_line(1,None,['Activities', 'Aktivitäten', 'Activities'],None,None,None,['', '', ''],'C',None,['', '', ''],'W',1,None,None,''))

loader.flush_deferred_objects()
