from odoo import fields, models


class NotesVendor(models.Model):
    _inherit = 'purchase.order'


    vendor_notes = fields.Char(string='Vendor Notes')