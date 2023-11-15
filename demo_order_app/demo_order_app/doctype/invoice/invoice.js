// Copyright (c) 2023, jeomar bayoguina and contributors
// For license information, please see license.txt

frappe.ui.form.on('Invoice', {
	quotation: (frm) => {
		frm.call("get_items_from_quotation").then((r) => {
			if (r) {
				frm.refresh_fields()
			}
		})
	}
});
