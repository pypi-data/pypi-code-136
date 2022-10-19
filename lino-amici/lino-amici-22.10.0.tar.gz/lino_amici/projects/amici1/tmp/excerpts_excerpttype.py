# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table excerpts_excerpttype...")
# fields: id, name, build_method, template, attach_to_email, email_template, certifying, remark, body_template, content_type, primary, backward_compat, print_recipient, print_directly, shortcut
loader.save(create_excerpts_excerpttype(1,['Terms & conditions', 'Nutzungsbestimmungen', 'Terms & conditions'],'appypdf','TermsConditions.odt',False,'',False,'','',contacts_Person,False,False,True,True,None))
loader.save(create_excerpts_excerpttype(2,['Payment reminder', 'Zahlungserinnerung', 'Rappel de paiement'],'weasy2pdf','payment_reminder.weasy.html',False,'',False,'','',contacts_Partner,False,False,True,True,None))
loader.save(create_excerpts_excerpttype(3,['Enrolment', 'Einschreibung', 'Inscription'],None,'',False,'',True,'','',courses_Enrolment,True,False,True,True,None))

loader.flush_deferred_objects()
