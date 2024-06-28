from odoo import api,models, fields


class TourPackage(models.Model):
    _name = 'tour.package'
    _inherit = 'mail.thread'
    _description = 'tour package management'

    name = fields.Char(string="Name")
    package_type = fields.Selection([('custom','Custom'),('fixed','Fixed')], string="package Type")
    package_price = fields.Float(string="package Price")
    no_of_days = fields.Float(string="Number Of days")
    final_price = fields.Float(string="Final price", compute = '_compute_final_price', store='True')

    @api.depends('package_type', 'package_price', 'no_of_days')
    def _compute_final_price(self):
        for every_record in self :
            if every_record.package_type == 'custom':
                every_record.final_price = every_record.no_of_days * every_record.package_price
            elif every_record.package_type == 'fixed':
                every_record.final_price = every_record.package_price




