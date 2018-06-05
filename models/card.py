from odoo import api, fields, models
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)

class Cards(models.Model):
    _name = "aqua_rdv.card"

    name = fields.Char()
    validity = fields.Datetime(default=datetime.now() + timedelta(days=365))
    type_id = fields.Many2one('aquardv.prestation')
    number_actual = fields.Integer(String="Séances restantes")
    qty_buy = fields.Integer(string="Quantité initial")
    status = fields.Selection([
        ('valid', 'Valide'),
        ('invalid', 'Invalide'),
    ], string="Validité de la carte", default="valid")
    product_id = fields.Many2one('product.template', string="Produit")
    client_id = fields.Many2one('res.partner')