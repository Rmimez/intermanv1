# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields
from odoo.exceptions import AccessError


class Partner(models.Model):

    _inherit = ['res.partner']
    l10n_ca_pst = fields.Char(string="hello", required=False)
