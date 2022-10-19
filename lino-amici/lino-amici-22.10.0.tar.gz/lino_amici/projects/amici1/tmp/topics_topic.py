# -*- coding: UTF-8 -*-
logger.info("Loading 4 objects to table topics_topic...")
# fields: id, ref, name, description_text
loader.save(create_topics_topic(1,None,['Nature', 'Nature', 'Nature'],['None', '', '']))
loader.save(create_topics_topic(2,None,['Folk', 'Folk', 'Folk'],['None', '', '']))
loader.save(create_topics_topic(3,None,['Health', 'Health', 'Health'],['None', '', '']))
loader.save(create_topics_topic(4,None,['Computer', 'Computer', 'Computer'],['None', '', '']))

loader.flush_deferred_objects()
