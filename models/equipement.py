from odoo import api, fields, models
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)

class Equipement(models.Model):
    _name = "aquardv.equipement"
    _description = "Model pour les équipement de l'institut"

    name = fields.Char(string="Nom")
    prestation_id = fields.Many2one("aquardv.prestation")
