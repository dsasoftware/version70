# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Consultoria YarosLab (<http://www.yaroslab.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields, orm
from openerp import netsvc
from openerp.tools.translate import _

class PaymentMode(orm.Model):
    _inherit = 'payment.mode'
    _columns = {
        'mode_id': fields.many2one('payment.mode.type', string='Modo de Pago'),# Tipo documento cobro/pago

    }

PaymentMode()

class PaymentModeType(orm.Model):
    _name = 'payment.mode.type'
    _columns = {
        'sunat': fields.char('Código Sunat', size=3, required=True),
        'name': fields.char('Nombre', required=True),
        'state': fields.boolean("Estado", required=True),

    }

PaymentModeType()