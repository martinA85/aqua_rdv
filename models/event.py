from odoo import api, fields, models
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)

class Meeting(models.Model):
    _inherit = 'calendar.event'
    _logger.info("EVENT")
    is_prestation = fields.Boolean(string="Est une préstation", default=False)
    with_partner_id = fields.Many2one('res.partner', 'Par')
    for_partner_id = fields.Many2one('res.partner', 'Pour')
    prestation_id = fields.Many2one('aquardv.prestation', 'Quoi')
    cabine_id = fields.Many2one('aquardv.cabine', 'Ou')
    state = fields.Selection([
        ('valid', 'Valide'),
        ('canceled', 'Annuler'),
        ('past', 'Fait'),
    ], default="valid")
