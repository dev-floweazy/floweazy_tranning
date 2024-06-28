from odoo import api,models, fields, _


class TourProgram(models.Model):
    _name = 'tour.program'
    _inherit = 'mail.thread'
    _description = 'Tour Program'


    tour_program_ids = fields.One2many('tour.program.lines', 'tour_program_id', string="Tour Program Lines")
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    tax_amount = fields.Float(string='Tax Amount', compute='_compute_tax_amount', store=True)
    final_total = fields.Float(string='Final Total', compute='_compute_final_total', store=True)

    @api.depends('tour_program_ids.price')
    def _compute_total_amount(self):
        for record in self:
            total = sum(line.price for line in record.tour_program_ids)
            record.total_amount = total


    @api.depends('tour_program_ids.tax_ids', 'tour_program_ids.price')
    def _compute_tax_amount(self):
        for record in self:
            tax_total = 0.0
            for line in record.tour_program_ids:
                if line.tax_ids:
                    taxes = line.tax_ids.compute_all(line.price)['taxes']
                    tax_total += sum(tax['amount'] for tax in taxes)
            record.tax_amount = tax_total

    @api.depends('tax_amount', 'total_amount')
    def _compute_final_total(self):
        for record in self:
            record.final_total = record.tax_amount + record.total_amount

class TourProgramLines(models.Model):
    _name = 'tour.program.lines'
    _description = 'Tour Program Lines'

    name = fields.Integer(string="S.No")
    tour_program_id = fields.Many2one('tour.program', string='Tour Program')
    product_name_id = fields.Many2one('product.product', string='Product')
    price = fields.Float(string='Price', related='product_name_id.list_price')
    tax_ids = fields.Many2many('account.tax', string='Taxes')


    #tax_amount = fields.Float(string='Tax Amount', compute='_compute_tax_amount', store=True)
