# -*- coding: utf-8 -*-
from odoo import models, api, fields, exceptions, tools, _
import logging
import datetime
import inspect

class PosOrder(models.Model):
	_inherit = 'pos.order'
	
	isChecked = fields.Boolean(default=False)
	
	def setIsChecked(self,bool):
		self.isChecked = bool
	
	def write(self,vals):
		if(inspect.stack()[2].function == "setIsChecked"):
			return super(PosOrder,self).write(vals)
		else:
			if self.isChecked == False:
				if self.partner_id:
					for line in self.lines:
						if line.product_id.is_card_institut:
							self.env['aqua_rdv.card'].create({
								"name":self.partner_id.name+" "+ line.product_id.name +" "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
								"client_id":self.partner_id.id,
								"type_id":line.product_id.prestation_id.id,
								"number_actual":line.product_id.qty_prestation*line.qty,
								"qty_buy":line.product_id.qty_prestation*line.qty,
								"product_id":line.product_id.id
							})
			self.setIsChecked(True)
			return super(PosOrder,self).write(vals)
	