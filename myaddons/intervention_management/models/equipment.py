# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class equipment(models.Model):
    _name = 'intervention_management.equipment'
    _description = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code_equipment = fields.Char(string="Code", required=True)
    mark = fields.Char(string="mark", required=True)
    name = fields.Char(string="name", required=True)
    category = fields.Char(string="category", required=True)
    description = fields.Text(string="Description", required=True)
    color = fields.Integer()


    _sql_constraints = [('def_identification_unique', 'unique(code)', 'Code must be unique!')]


    #Relations
    equipment_pannes = fields.Many2many(comodel_name="intervention_management.panne", relation="equipment_rel_pannes", column1="code_equipment", column2="id", string="Pannes" )
    equipment_pieces = fields.Many2many(comodel_name="intervention_management.piece", relation="equipment_rel_pieces", column1="code_equipment", column2="code_piece", string="Pieces")
    station_cods= fields.Many2many(comodel_name="intervention_management.station", relation="equipment_rel_station", column1="code_equipment", column2="code_station", string="Stations")

    @api.onchange('category')
    def _check_something(self):
        for record in self:
            if record.category =="20":
                return {
                    'warning': {
                        'title': "Something bad happened",
                        'message': "It was very bad indeed",
                    }
                }

    @api.constrains('code_equipment')
    def _check_something(self):
        for record in self:
            if len(record.code_equipment) > 5:
                raise ValidationError("Your record is too long: %s" % record.code_equipment)


    @api.depends('value')
    def _compute_name(self):
        for record in self:
            record.name = "Record with value %s" % record.value