from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_card_institut = fields.Boolean(default=False, string="Est un forfait institut")
    qty_prestation = fields.Integer(string="Nombre de prestation")
    prestation_id = fields.Many2one('aquardv.prestation', string="Type de cours")
