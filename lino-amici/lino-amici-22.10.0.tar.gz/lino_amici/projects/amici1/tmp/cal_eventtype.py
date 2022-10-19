# -*- coding: UTF-8 -*-
logger.info("Loading 7 objects to table cal_eventtype...")
# fields: id, ref, seqno, name, attach_to_email, email_template, description, is_appointment, all_rooms, locks_user, force_guest_states, fill_presences, start_date, event_label, max_conflicting, max_days, transparent, planner_column, default_duration
loader.save(create_cal_eventtype(1,None,1,['Absences', 'Abwesenheiten', 'Absences'],False,'','',True,False,False,False,True,None,['', '', ''],1,0,False,'10',None))
loader.save(create_cal_eventtype(2,None,2,['Holidays', 'Feiertage', 'Jours fériés'],False,'','',False,True,False,False,False,None,['', '', ''],1,0,False,'10',None))
loader.save(create_cal_eventtype(3,None,3,['Meeting', 'Versammlung', 'Réunion'],False,'','',True,False,False,False,True,None,['', '', ''],1,1,False,'10','1:00'))
loader.save(create_cal_eventtype(4,None,4,['Internal', 'Intern', 'Interne'],False,'','',False,False,False,False,True,None,['', '', ''],1,1,True,'20','0:30'))
loader.save(create_cal_eventtype(5,None,5,['Training', 'Ausbildung', 'Formation'],False,'','',True,False,False,False,False,None,['', '', ''],1,1,False,None,None))
loader.save(create_cal_eventtype(6,None,6,['Travel', 'Travel', 'Travel'],False,'','',True,False,False,False,False,None,['', '', ''],1,1,False,None,None))
loader.save(create_cal_eventtype(7,None,7,['Camp', 'Camp', 'Camp'],False,'','',True,False,False,False,False,None,['', '', ''],1,1,False,None,None))

loader.flush_deferred_objects()
