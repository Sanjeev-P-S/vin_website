import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_lead(
    first_name=None,
    last_name=None,
    email_id=None,
    mobile_no=None,
    company_name=None,
    gender=None,
    request_type=None
):
    # Require at least a name
    if not first_name and not company_name:
        frappe.throw(_("Please provide your name or company name."))

    doc = frappe.new_doc("Lead")
    doc.first_name     = first_name or company_name
    doc.last_name      = last_name or ""
    doc.email_id       = email_id or ""
    doc.mobile_no      = mobile_no or ""
    doc.company_name   = company_name or ""
    doc.gender         = gender or ""
    doc.request_type   = request_type or ""
    doc.status         = "Lead"
    doc.source         = "Website"
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "Success",
        "lead_name": doc.name
    }
