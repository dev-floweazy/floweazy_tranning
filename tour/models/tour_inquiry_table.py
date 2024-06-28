from odoo import api,models, fields, _


class TourInquiryTable(models.Model):
    _name = 'tour.inquiry.table'
    _inherit = 'mail.thread'
    _description = 'tour inquiry table'

    name = fields.Char(string="Customer Inquiry", default=lambda self:_('New'), readLine='True')
    customer_email = fields.Char(string="Customer Email")
    customer_phone = fields.Char(string="Customer Phone")

    tour_name = fields.Many2one('tour.package', string="Tour Name")
    tour_package_price = fields.Float(string="Tour Package price",compute='_compute_tour_package_price', store='True')
    preferred_start_date = fields.Date(string="Preferrred start date")
    preferred_end_date = fields.Date(string="Preferred end date")

    @api.constrains('preferred_start_date', 'preferred_end_date')
    def _constrains_preferred_start_date(self):
        for record in self:
            if record.preferred_start_date > record.preferred_end_date:
                raise ValidationError(_('Start date must be less than or equal to end date.'))

    @api.depends('tour_package_price', 'tour_name')
    def _compute_tour_package_price(self):
        for record in self:
            if record.tour_name:
                record.tour_package_price = record.tour_name.final_price

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('customer.inquiry.sequence')
        return super(TourInquiryTable, self).create(vals)

