# Copyright (c) 2023, jeomar bayoguina and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Invoice(Document):
    
    @frappe.whitelist()
    def get_items_from_quotation(self):
        quotation = frappe.get_doc("Quotation", self.quotation)
        total_amount = 0
        total_qty = 0
        for item in quotation.items:
            self.append('items', {
				'item': item.get('item'), 
    			'uom': item.uom, 
       			'rate': item.rate, 
          		'qty': item.qty,
				'quotation': quotation.name,
				'total_amount': flt(item.rate * item.qty)
			})
            total_amount += flt(item.rate * item.qty)
            total_qty += item.qty
        self.db_set("total_amount", total_amount)
        self.db_set("total_qty", total_qty)
            
    def on_submit(self):
        self.db_set("status", "Completed")
        quotation = frappe.get_doc("Quotation", self.quotation)
        quotation.db_set("status", "Fulfilled")
        
        for item in self.items:
            doc = frappe.get_doc("Items", item.item)
            new_qty = flt(float(doc.current_stock) - item.qty)
            doc.db_set("current_stock", new_qty)
            
        
