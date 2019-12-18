# -*- coding: utf-8 -*-

from odoo import models, fields, api


class station(models.Model):
    _name = 'intervention_management.station'
    _description = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code_station = fields.Char(string="Code", required=True)
    description = fields.Text(string="Description", required=True)
    location  = fields.Char(string="Location", required=True)
    social_reason = fields.Char(string="Social Reason", required=True)
    phone = fields.Integer(string="Phone Number", required=True)
    color = fields.Integer()




    #relations
    panne_ids = fields.One2many(comodel_name="intervention_management.panne", inverse_name="station_cods", string="Station", required=True)
    equipments_codes  = fields.Many2many(comodel_name="intervention_management.equipment", relation="equipment_rel_station", column1="code_station", column2="code_equipment", string="Equipments")
