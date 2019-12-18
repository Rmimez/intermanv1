# -*- coding: utf-8 -*-

#from odoo import models, fields, api

# class intervention_management(models.Model):
#     _name = 'intervention_management.intervention'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

import dateutil.parser
b = "2015-10-28 16:09:59"
d = dateutil.parser.parse(b).date()
print (d)