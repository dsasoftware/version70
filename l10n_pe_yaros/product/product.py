# coding:utf-8
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


from openerp.tools.translate import _
from openerp.osv import orm, fields, osv
import openerp.addons.decimal_precision as dp


class Product(orm.Model):

    _inherit = "product.product"
    _columns = {
        'detraccion': fields.many2one('account.spot.detraccion',"Detracción", domain=[('state','=',True)]),
        'percepcion': fields.many2one('account.spot.percepcion',"Percepcion", domain=[('state','=',True)]),

    }

