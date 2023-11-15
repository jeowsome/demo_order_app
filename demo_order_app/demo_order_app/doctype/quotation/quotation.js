// Copyright (c) 2023, jeomar bayoguina and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation', {
	refresh: function (frm) {
		frm.add_custom_button(__("Create Invoice"), () => {
			frm.call("create_invoice", {
				freeze: true,
				freeze_message: __(`<div class="d-flex justify-content-center">
			<div class="spinner-border spinner-border-lg" role="status">
			</div>
		  </div>`)
			}).then(({ message }) => {
				if (message) {
					frappe.show_alert(`Invoice successfully created`, 10);
					frappe.set_route(message.url)
				}
			})
		});
	},
});
