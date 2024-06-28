from odoo import api,models, fields, _
from odoo.exceptions import ValidationError


class TourDetails(models.Model):
    _name = 'tour.details'
    _description = 'tour details'


    tour_name = fields.Many2one('tour.package',string="Tour Name")
    tour_package_price = fields.Float(compute='_compute_tour_package_price', store='True')
    preferred_start_date = fields.Date(string="Preferred Start Date")
    preferred_end_date = fields.Date(string="Preferred End Date")

    @api.constrains('preferred_start_date', 'preferred_end_date')
    def _constrains_preferred_start_date(self):
        for record in self:
            if record.preferred_start_date > record.preferred_end_date:
                raise ValidationError(_('Start date must be less than or equal to end date.'))

    @api.depends('tour_package_price','tour_name')
    def _compute_tour_package_price(self):
        for record in self:
            if record.tour_name:
                record.tour_package_price = record.tour_name.final_price
