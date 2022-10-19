# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, password, last_login, username, user_type, initials, first_name, last_name, remarks, partner, time_zone, date_format, dashboard_layout, access_class, event_type
loader.save(create_users_user(3,'demo@example.com','fr',dt(2022,8,3,13,6,4),dt(2022,8,3,13,5,53),None,None,'pbkdf2_sha256$320000$rTaI3YM8pDCebpvIRu3Hzd$1OFdoEGl1lpV4T9Sce0OrbQFOQ3yC3R14Q/GbF2MH18=',None,'romain','900','','Romain','Raffault','',None,'01','010',None,'30',None))
loader.save(create_users_user(2,'demo@example.com','de',dt(2022,8,3,13,6,4),dt(2022,8,3,13,5,53),None,None,'pbkdf2_sha256$320000$XgXqVjeEfyqjQORtcjN4jh$3+ebeyaSrXBMT2bYkMLqOiTVz0DaNOosjEGvaOkUwSU=',None,'rolf','900','','Rolf','Rompen','',None,'01','010',None,'30',None))
loader.save(create_users_user(1,'demo@example.com','en',dt(2022,8,3,13,6,5),dt(2022,8,3,13,5,53),None,None,'pbkdf2_sha256$320000$q0ugeO2jeoTC8tuDKqEuD8$f9zr+nRp0WPWlxVDLYajwyDiYnoBpsD8clmOqlCgUNU=',None,'robin','900','','Robin','Rood','',None,'01','010',None,'30',None))

loader.flush_deferred_objects()
