# Copyright (c) 2023, jeomar bayoguina and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def get_columns():
    columns = [
        {
            'fieldname': 'item_name',
            'label': _('Item Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'current_stock',
            'label': _('Current Qty'),
            'fieldtype': 'float',
        },
        {
            'fieldname': 'qty_sold',
            'label': _('Sold Qty'),
            'fieldtype': 'float',
        },
        {
            'fieldname': 'stock_rate',
            'label': _('Item Price'),
            'fieldtype': 'currency',
        },
        {
            'fieldname': 'selling_rate',
            'label': _('Sold Price'),
            'fieldtype': 'currency',
        },
        {
            'fieldname': 'customer_name',
            'label': _('Customer'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'invoice',
            'label': _('Invoice'),
            'fieldtype': 'Link',
            'options': 'Invoice'
        },
        {
            'fieldname': 'quotation',
            'label': _('Quotation'),
            'fieldtype': 'Link',
            'options': "Quotation"
        },
    ]
    return columns
    
def get_data(filters=None):
    _filter = {"status": "Completed"}
    if filters:
        _filter = {**_filter, **filters}
        
    invoices = frappe.get_all("Invoice", fields=["customer", "name"], filters=_filter)
    sold_items = frappe.get_all('Invoice Items',
                                fields=["parent", "item", "qty as qty_sold", "rate as selling_rate", "quotation"],
                                filters={'parent': ["in", [invoice.get("name") for invoice in invoices]]})
    result = []
    for item in sold_items:
        doc_item = frappe.get_value("Items", item.item, ["price as stock_rate", "current_stock", "item_name"], as_dict=1)
        doc_invoice = frappe.get_value("Invoice", item.parent, ["customer"], as_dict=1)
        doc_customer = frappe.get_value("Customer", doc_invoice.customer, ["customer_name"], as_dict=1)
        add_res = {"invoice": item.parent, "quotation": item.quotation}
        cur_res = item | doc_item | doc_customer | add_res
        result.append(cur_res)
    return result

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data