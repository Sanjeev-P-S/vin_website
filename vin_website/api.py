import frappe

@frappe.whitelist(allow_guest=True)
def submit_enquiry(name, email, phone, company, subject, message):

    if not name:
        frappe.throw("Name is required.")

    if not email:
        frappe.throw("Email is required.")

    if not phone:
        frappe.throw("Phone number is required.")

    doc = frappe.get_doc({
        "doctype": "Contact Inquiry",
        "name1": name,
        "email": email,
        "phone": phone,
        "company": company,
        "subject": subject,
        "message": message
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "message": "Enquiry submitted successfully."
    }



@frappe.whitelist(allow_guest=True)
def get_gallery_data():

    galleries = frappe.get_all(
        "Gallery",
        fields=[
            "title",
            "description",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5"
        ]
    )

    return galleries
