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

from openerp.osv import fields, osv, orm

#TABLA 12: TIPO DE OPERACIÓN

class account_asset_asset(orm.Model):
    _inherit = 'account.asset.asset'
    _columns = {
        'type': fields.selection((('1','No revaluado o revaluado sin efecto tributario'),
        ('2','Revaluado con efecto tributario')),
        'Tipo Activo Fijo'),
        'state_type': fields.selection((('1','Activos en desuso'),
        ('2','Activos Obsoletos'),('9','Resto de activos')),
        'Estado Activo Fijo'),
    }
account_asset_asset()
