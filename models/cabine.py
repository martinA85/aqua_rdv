from odoo import api, fields, models
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class Cabine(models.Model):
    _name = "aquardv.cabine"
    _description = "Model pour les cabine de l'institut"

    name = fields.Char(string="Nom")
    prestation_ids = fields.Many2many('aquardv.prestation','rel_cabine_prestation', string="Préstations reçevable")
    equipement_ids = fields.Many2many('aquardv.equipement', 'rel_equipement_cabine', string="Equipement reçevable")

    