import frappe
from frappe import _

no_cache = 1
allow_guest = True

def get_context(context):
    context.team_members = frappe.get_all(
        "Employee",
        filters={"custom_show_in_website_profile": 1},
        fields=["employee_name", "designation", "image", "bio", "first_name", "last_name", "custom_linkedin_url"]
    )


