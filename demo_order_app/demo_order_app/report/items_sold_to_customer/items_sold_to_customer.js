// Copyright (c) 2023, jeomar bayoguina and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Items Sold To Customer"] = {
	"filters": [
		{
			fieldname: 'customer',
			label: __('Customer'),
			fieldtype: 'Link',
			options: 'Customer',
		},
	]
};


