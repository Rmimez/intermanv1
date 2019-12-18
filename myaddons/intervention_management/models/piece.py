# -*- coding: utf-8 -*-

from odoo import models, fields, api


class piece(models.Model):
    _name = 'intervention_management.piece'
    _description = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code_piece = fields.Char(string="Code", required=True)
    mark = fields.Char(string="mark", required=True)
    description = fields.Text(string="Description", required=True)
    price  = fields.Float(string="Price", required=False)
    color = fields.Integer()

    _sql_constraints = [('def_identification_unique', 'unique(code)', 'Code must be unique!')]


    #Relations
    pieces_equipment = fields.Many2many(comodel_name="intervention_management.equipment", relation="equipment_rel_pieces", column2="code_equipment", column1="code_piece", string="Equipments")



