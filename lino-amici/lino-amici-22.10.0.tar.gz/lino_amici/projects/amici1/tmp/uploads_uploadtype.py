# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table uploads_uploadtype...")
# fields: id, name, upload_area, max_number, wanted, shortcut
loader.save(create_uploads_uploadtype(1,['Source document', 'Source document', 'Source document'],'90',1,True,None))

loader.flush_deferred_objects()
