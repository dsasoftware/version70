# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#     Copyright (C) 2014 Consultoria YarosLab (<http://www.yaroslab.com> - info@yaroslab.com).
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

from openerp.osv import orm, fields

class AccountVoucherType(orm.Model):
    _name = 'account.spot'
    _columns = {
        'name': fields.char("Nombre", required=True,size=100),
        'sunat_code': fields.char(u'Código SUNAT', required=True),
        'account_journal_id': fields.many2one('account.journal', string='Diario Ventas'),
        'account_journal_id_purchase': fields.many2one('account.journal', string='Diario Compras'),
        'account_spot_detraccion_ids': fields.one2many('account.spot.detraccion', 'account_spot_id'),
        'account_spot_retencion_ids': fields.one2many('account.spot.retencion', 'account_spot_id'),
        'account_spot_percepcion_ids': fields.one2many('account.spot.percepcion', 'account_spot_id')
    }
    """
    def _check_range_percentage(self, cr, uid, ids, context=None):
    """


class AccountDetraccion(orm.Model):
    """
    Maestro de Detracciones
    """
    _name = 'account.spot.detraccion'
    _description ='Maestro de detracciones del sistema'
    _columns = {
        'cod_sunat': fields.char("Codigo Sunat", size=3, required=True),
        'state': fields.boolean("Estado"),
        'name': fields.char("Nombre Detracción ", size=100, required=True),
        'percentage': fields.float("Porcentaje", required=True),
        'amount': fields.float("Monto Minimo "),
        'account_spot_id': fields.many2one('account.spot', 'SPOT'),
    }
    _defaults = {
        'state': True,
        'amount': 750.00,
    }

class AccountRetencion(orm.Model):
    """
    Maestro de Retenciones
    """
    _name = 'account.spot.retencion'
    _description ='Maestro de retenciones del sistema'
    _columns = {
        'cod_sunat': fields.char("Codigo Sunat", size=3, required=True),
        'state': fields.boolean("Estado"),
        'name': fields.char("Nombre Retención ", size=100, required=True),
        'percentage': fields.float("Porcentaje", required=True),
        'amount': fields.float("Monto Mínimo "),
        'account_spot_id': fields.many2one('account.spot', 'SPOT'),
    }
    _defaults = {
        'state': True,
        'amount': 750.00,
    }

class AccountPercepcion(orm.Model):
    """
    Maestro de Percepcion
    """
    _name = 'account.spot.percepcion'
    _description ='Maestro de percepcion del sistema'
    _columns = {
        'cod_sunat': fields.char("Codigo Sunat", size=3, required=True),
        'state': fields.boolean("Estado"),
        'name': fields.char("Nombre Percepcion ", size=100, required=True),
        'percentage': fields.float("Porcentaje", required=True),
        'amount': fields.float("Monto Mínimo "),
        'account_spot_id': fields.many2one('account.spot', 'SPOT'),
    }
    _defaults = {
        'state': True,
        'amount': 750.00,
    }
