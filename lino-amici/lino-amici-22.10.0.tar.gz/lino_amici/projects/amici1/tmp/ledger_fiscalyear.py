# -*- coding: UTF-8 -*-
logger.info("Loading 13 objects to table ledger_fiscalyear...")
# fields: id, ref, start_date, end_date, state
loader.save(create_ledger_fiscalyear(1,'2012',date(2012,1,1),date(2012,12,31),'10'))
loader.save(create_ledger_fiscalyear(2,'2013',date(2013,1,1),date(2013,12,31),'10'))
loader.save(create_ledger_fiscalyear(3,'2014',date(2014,1,1),date(2014,12,31),'10'))
loader.save(create_ledger_fiscalyear(4,'2015',date(2015,1,1),date(2015,12,31),'10'))
loader.save(create_ledger_fiscalyear(5,'2016',date(2016,1,1),date(2016,12,31),'10'))
loader.save(create_ledger_fiscalyear(6,'2017',date(2017,1,1),date(2017,12,31),'10'))
loader.save(create_ledger_fiscalyear(7,'2018',date(2018,1,1),date(2018,12,31),'10'))
loader.save(create_ledger_fiscalyear(8,'2019',date(2019,1,1),date(2019,12,31),'10'))
loader.save(create_ledger_fiscalyear(9,'2020',date(2020,1,1),date(2020,12,31),'10'))
loader.save(create_ledger_fiscalyear(10,'2021',date(2021,1,1),date(2021,12,31),'10'))
loader.save(create_ledger_fiscalyear(11,'2022',date(2022,1,1),date(2022,12,31),'10'))
loader.save(create_ledger_fiscalyear(12,'2023',date(2023,1,1),date(2023,12,31),'10'))
loader.save(create_ledger_fiscalyear(13,'2024',date(2024,1,1),date(2024,12,31),'10'))

loader.flush_deferred_objects()
