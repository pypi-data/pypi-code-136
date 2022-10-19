# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table system_siteconfig...")
# fields: id, default_build_method, simulate_today, site_company, next_partner_id, default_event_type, site_calendar, max_auto_events, hide_events_before, default_color, pupil_guestrole
loader.save(create_system_siteconfig(1,None,None,None,100,None,None,72,None,'Blue',None))

loader.flush_deferred_objects()
