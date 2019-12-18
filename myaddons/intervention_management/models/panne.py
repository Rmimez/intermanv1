# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from datetime import datetime
import base64
import os
from odoo.exceptions import ValidationError
import dateutil.parser

class panne(models.Model):
    _name = 'intervention_management.panne'
    _description = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'id'

    def _get_logo(self):
        return base64.b64encode(
            open(os.path.join(tools.config['root_path'], 'addons', 'base', 'static', 'img', 'res_company_logo.png'),
                 'rb').read())

    id = fields.Integer(string="ID", required=True)
    description = fields.Text(string="Description", required=True)
    start_date = fields.Datetime(string="Date & Time of Start", required=True)
    finish_date = fields.Datetime(string="Date & Time of finish", required=True)
    priority = fields.Selection(string="",
                                selection=[('primary', 'Primary'), ('secondary', 'Secondary'), ('vital', 'Vital'), ],
                                required=False)
    color = fields.Integer()
    num = fields.Integer(string="num", required=False)
    image_64 = fields.Binary(default=_get_logo, string="Panne Image", readonly=False)

    # relations
    station_cods = fields.Many2one(comodel_name="intervention_management.station", string="Station Codes",
                                   required=True)
    pannes_equipment = fields.Many2many(comodel_name="intervention_management.equipment",
                                        relation="equipment_rel_pannes", column1="id", column2="code_equipment",
                                        string="Equipments")

    state = fields.Selection(string="", selection=[('S1', 'Declaration'), ('S2', 'Diagnostic'),('S3', 'Reparation'), ('Finished', 'Finished'),  ],
                             default='S1',required=True)

     #caledar

    calendar_start_date= fields.Date(string='Your string', compute="_set_calendar_start_date")
    calendar_finish_date= fields.Date(string='Your string', compute="_set_calendar_finish_date")

    def _set_calendar_start_date(self):
        for c in self:
            c.calendar_start_date = dateutil.parser.parse(str(c.start_date)).date()

    def _set_calendar_finish_date(self):
        for c in self:
            c.calendar_finish_date = dateutil.parser.parse(str(c.finish_date)).date()

    @api.constrains('start_date','finish_date')
    def _check_start_and_finish_date(self):
        for record in self:
            sd=dateutil.parser.parse(str(record.start_date)).isocalendar()
            fd = dateutil.parser.parse(str(record.finish_date)).isocalendar()
            if sd > fd:
                raise ValidationError("Your record dates are wrong : [%s] the start date shoulds be before the finish date [%s]" %(record.start_date  ,record.finish_date))


   # @api.depends('date','start_date')
    # def getdate(self):
    #     for record in self:
    #         record.start_date = datetime.strptime(record.date, "%d/%m/%y %H:%M:%S").date()

    # @api.model
    # def get_selection_class(self):
    #     classname = ['default', 'primary', 'success', 'warning', 'danger']
    #     return [(x, str.title(x)) for x in classname]
