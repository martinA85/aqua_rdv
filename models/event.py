from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import Warning
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


    def valid_prestation(self):
        _logger.info("valid_prestation")
        for meeting in self:
            client_id = meeting.for_partner_id
            type_prestation = meeting.prestation_id
            card_id = self.env['aqua_rdv.card'].search([('client_id','=',client_id.id),('type_id','=',type_prestation.id)], order='validity asc',limit=1)
            if card_id:
                if card_id.number_actual > 0:
                    card_id.number_actual = card_id.number_actual - 1
                    meeting.state = "valid"
                else:
                    raise Warning(('''Forfait de la cliente vide'''))
            else:
                raise Warning(('''Pas de forfait : ''' + type_prestation.name))
                    
