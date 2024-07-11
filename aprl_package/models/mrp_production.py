from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    batch_id = fields.Char(string="Batch ID", required=True)
    packaging_size = fields.Selection([
        ('2', '2kg'),
        ('5', '5kg'),
        ('10', '10kg')
    ], string="Packaging Size", required=True)
    pack_count = fields.Integer(string="Pack Count", compute='_compute_packs', store=True)
    pallet_size = fields.Integer(string="Pallet Size", default=100)  # Example pallet size in kg

    @api.depends('product_qty', 'packaging_size')
    def _compute_packs(self):
        for record in self:
            if record.packaging_size:
                packaging_size = int(record.packaging_size)
                record.pack_count = int(record.product_qty / packaging_size)

    from odoo import models, fields, api

    class MrpProduction(models.Model):
        _inherit = 'mrp.production'

        def create_product_jar(self, packaging_size):
            """Create product jar based on the given packaging size."""
            product_template_ref = 'your_module.product_template_{}_kg_jar'.format(packaging_size)
            try:
                product_template = self.env.ref(product_template_ref)
            except ValueError:
                raise UserError(_('The product template for {} KG Jar is not defined.').format(packaging_size))

            product_vals = {
                'name': '{} KG Jar'.format(packaging_size),
                'product_tmpl_id': product_template.id,
                'default_code': 'PROD_{}_KG_JAR'.format(packaging_size),
                'type': 'product',
                'categ_id': product_template.categ_id.id,
                'uom_id': product_template.uom_id.id,
                'uom_po_id': product_template.uom_po_id.id,
            }
            product = self.env['product.product'].create(product_vals)
            return product

        def button_mark_done(self):
            super(MrpProduction, self).button_mark_done()
            packaging_size = self.packaging_size  # Ensure you have this field defined in your model
            product_jar = self.create_product_jar(packaging_size)
            # You can now use the created product for further operations
            return True

    def button_mark_done(self):
        res = super(MrpProduction, self).button_mark_done()
        for production in self:
            if production.pack_count > 0:
                packaging_size = int(production.packaging_size)
                for _ in range(production.pack_count):
                    # Create a new stock.quant for each jar
                    self.env['stock.quant'].create({
                        'product_id': self.env.ref('product.product_{}_kg_jar'.format(packaging_size)).id,
                        'location_id': production.location_dest_id.id,
                        'quantity': packaging_size,
                    })
            # Create a new stock.quant for the pallet of jars
            pallet_count = int(production.product_qty / self.pallet_size)
            for _ in range(pallet_count):
                self.env['stock.quant'].create({
                    'product_id': self.env.ref('product.product_pallet_of_jars').id,
                    'location_id': production.location_dest_id.id,
                    'quantity': self.pallet_size,
                })
        return res

    def create_product_jar(self, packaging_size):
        """Create product jar based on the given packaging size."""
        product_template_ref = 'your_module.product_template_{}_kg_jar'.format(packaging_size)
        try:
            product_template = self.env.ref(product_template_ref)
        except ValueError:
            raise UserError(_('The product template for {} KG Jar is not defined.').format(packaging_size))

        product_vals = {
            'name': '{} KG Jar'.format(packaging_size),
            'product_tmpl_id': product_template.id,
            'default_code': 'PROD_{}_KG_JAR'.format(packaging_size),
            'type': 'product',
            'categ_id': product_template.categ_id.id,
            'uom_id': product_template.uom_id.id,
            'uom_po_id': product_template.uom_po_id.id,
        }
        product = self.env['product.product'].create(product_vals)
        return product

    def button_mark_done(self):
        super(MrpProduction, self).button_mark_done()
        packaging_size = self.packaging_size  # Ensure you have this field defined in your model
        product_jar = self.create_product_jar(packaging_size)
        return True
