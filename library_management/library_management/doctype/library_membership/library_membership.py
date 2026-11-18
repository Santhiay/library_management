# Copyright (c) 2026, santhiya and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document
from frappe.utils import add_days


class LibraryMembership(Document):
	def before_submit(self):
		exists = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				"to_date": (">", self.from_date),
			},
		)
		if exists:
			frappe.throw(_("There is an active membership for this member"))

		loan_period = frappe.db.get_single_value("Library Settings", "loan_period")
		self.to_date = add_days(self.from_date, loan_period or 30)
