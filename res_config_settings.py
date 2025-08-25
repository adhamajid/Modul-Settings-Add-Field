from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_approve_vendor_requests = fields.Boolean(
        string='Auto Approve Vendor Requests',
        config_parameter='majid_vendor_regist.auto_approve_requests',
        help="Automatically approve vendor registration requests"
    )
    
    vendor_request_notification_emails = fields.Char(
        string='Notification Emails',
        config_parameter='majid_vendor_regist.notification_emails',
        help="Comma-separated list of email addresses to notify about new vendor requests"
    )
