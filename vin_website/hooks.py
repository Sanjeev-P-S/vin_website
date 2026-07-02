app_name = "vin_website"
app_title = "Vintrosys"
app_publisher = "Ponsakthivel"
app_description = "Vintrosys Business Solution"
app_email = "ponsakthivel@vintrosys.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "vin_website",
# 		"logo": "/assets/vin_website/logo.png",
# 		"title": "Vintrosys",
# 		"route": "/vin_website",
# 		"has_permission": "vin_website.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vin_website/css/vin_website.css"
# app_include_js = "/assets/vin_website/js/vin_website.js"

# include js, css files in header of web template
# web_include_css = "/assets/vin_website/css/vin_website.css"
# web_include_js = "/assets/vin_website/js/vin_website.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "vin_website/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "vin_website/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "vin_website.utils.jinja_methods",
# 	"filters": "vin_website.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "vin_website.install.before_install"
# after_install = "vin_website.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "vin_website.uninstall.before_uninstall"
# after_uninstall = "vin_website.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "vin_website.utils.before_app_install"
# after_app_install = "vin_website.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "vin_website.utils.before_app_uninstall"
# after_app_uninstall = "vin_website.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vin_website.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vin_website.tasks.all"
# 	],
# 	"daily": [
# 		"vin_website.tasks.daily"
# 	],
# 	"hourly": [
# 		"vin_website.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vin_website.tasks.weekly"
# 	],
# 	"monthly": [
# 		"vin_website.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "vin_website.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "vin_website.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vin_website.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vin_website.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["vin_website.utils.before_request"]
# after_request = ["vin_website.utils.after_request"]

# Job Events
# ----------
# before_job = ["vin_website.utils.before_job"]
# after_job = ["vin_website.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"vin_website.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []



fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "dt",
                "in",
                [
                    "Project",
                    "Employee"
                ]
            ]
        ]
    },
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "doc_type",
                "in",
                [
                    "Project",
                    "Employee"
                ]
            ]
        ]
    },
    {
        "doctype": "DocType",
        "filters": [
            [
                "name",
                "in",
                [
                    "Vintrosys Service",
                    "Vintrosys Product",
                    "Contact Inquiry",
                    "Gallery",
                    "Pricing Plan",
                    "Pricing Feature"
                ]
            ]
        ]
    },
    {
        "doctype": "Builder Page",
        "filters": [
            [
                "name",
                "in",
                [
                    "page-a1ae51a9",
                    "page-50eb3c51"
                ]
            ]
        ]
    },

    # Only if you've created reusable components
    {
        "doctype": "Builder Component"
    },

    # Only if used
    {
        "doctype": "Builder Variable"
    },

    {
        "doctype": "Builder Project Folder"
    },

    {
        "doctype": "User Font"
    },
    {
        "doctype": "Builder Client Script",
        "filters": [
            [
                "name",
                "in",
                [
                    "JavaScript-counter",
                    "CSS-Slider",
                    "CSS-42843",
                    "JavaScript-5cc86"
                ]
            ]
        ]
    },

    {
        "doctype": "Block Template"
    },
    
]
