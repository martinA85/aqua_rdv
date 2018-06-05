from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    institut_card_ids = fields.One2many('aqua_rdv.card', 'client_id')