# -*- coding: utf-8 -*-
from odoo import http

# class InterventionManagement(http.Controller):
#     @http.route('/intervention_management/intervention_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/intervention_management/intervention_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('intervention_management.listing', {
#             'root': '/intervention_management/intervention_management',
#             'objects': http.request.env['intervention_management.intervention_management'].search([]),
#         })

#     @http.route('/intervention_management/intervention_management/objects/<model("intervention_management.intervention_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('intervention_management.object', {
#             'object': obj
#         })