# -*- coding: UTF-8 -*-
# Copyright 2013-2022 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import rt, dd, _
from lino.core import constants

rt.models.aids.GrantingsByClient.column_names = "detail_link request_date "\
                                      "aid_type category start_date"

notes = rt.models.notes
notes.Note.hidden_elements = dd.fields_list(
    notes.Note, 'company contact_person contact_role')

notes.NotesByProject.display_mode = ((None, constants.DISPLAY_MODE_TABLE), )

rt.models.uploads.UploadsByProject.display_mode = ((None, constants.DISPLAY_MODE_TABLE), )

rt.models.households.SiblingsByPerson.display_mode = ((None, constants.DISPLAY_MODE_TABLE), )

# rt.models.cal.TasksByController.display_mode = ((None, constants.DISPLAY_MODE_TABLE), )

# humanlinks.LinksByHuman.display_mode = ((None, constants.DISPLAY_MODE_TABLE), )

# ContactsByClient.column_names = 'company contact_person remark'
# dd.update_field(ClientContact, 'remark', verbose_name=_("Contact details"))

contacts = rt.models.contacts
contacts.PartnerDetail.contact = dd.Panel("""
address_box
remarks:30 #sepa.AccountsByPartner
""", label=_("Contact"))

contacts.PersonDetail.contact = dd.Panel("""
households.MembersByPerson:20 households.SiblingsByPerson:60
humanlinks.LinksByHuman
remarks:30 #sepa.AccountsByPartner
""", label=_("Contact"))

contacts.CompanyDetail.contact = dd.Panel("""
#address_box addresses.AddressesByPartner
remarks:30 #sepa.AccountsByPartner
""", label=_("Contact"))
