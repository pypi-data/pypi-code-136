# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table calview_dailyplannerrow...")
# fields: id, seqno, designation, start_time, end_time
loader.save(create_calview_dailyplannerrow(1,1,['AM', 'Vormittags', 'Avant-midi'],None,time(12,0,0)))
loader.save(create_calview_dailyplannerrow(2,2,['PM', 'Nachmittags', 'Après-midi'],time(12,0,0),None))

loader.flush_deferred_objects()
