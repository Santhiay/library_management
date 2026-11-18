# Copyright (c) 2026, santhiya and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"articles/{frappe.scrub(self.article_name)}"
