# -*- coding: utf-8 -*-
from odoo import http

# class AquaRdv(http.Controller):
#     @http.route('/aqua_rdv/aqua_rdv/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aqua_rdv/aqua_rdv/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aqua_rdv.listing', {
#             'root': '/aqua_rdv/aqua_rdv',
#             'objects': http.request.env['aqua_rdv.aqua_rdv'].search([]),
#         })

#     @http.route('/aqua_rdv/aqua_rdv/objects/<model("aqua_rdv.aqua_rdv"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aqua_rdv.object', {
#             'object': obj
#         })