from odoo import api, fields, models
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class Prestation(models.Model):
    _name = "aquardv.prestation"
    _description = "Model pour une Préstation à l'institut"

    name = fields.Char(string="Nom")
    text = fields.Char(string="Description")
    equipement_ids = fields.One2many('aquardv.equipement', 'prestation_id', string="Equipement requis")
    cabine_ids = fields.Many2many('aquardv.cabine', 'rel_cabine_prestation', string="Cabine possible")

    