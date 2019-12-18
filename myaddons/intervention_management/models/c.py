# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from babel.dates import format_date
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import json

from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from odoo.release import version
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF


class CrmTeam(models.Model):
    _name = 'intervention_management.user'


    user_id = fields.Many2one('res.users', string='Team Leader', check_company=True)