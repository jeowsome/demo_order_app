# Copyright (c) 2023, jeomar bayoguina and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Quotation(Document):
    
    @frappe.whitelist()
    def create_invoice(self):
        doc = frappe.get_doc({
            'doctype': 'Invoice',
            'customer': self.customer_name,
            'quotation': self.name
            })
        doc.get_items_from_quotation()
        doc.save()
        
        return {
			"url": doc.get_url()
		}