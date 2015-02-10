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

from openerp.osv import osv, fields
from openerp.tools.translate import _

class res_company(osv.osv):
    _inherit = 'res.company'
    _columns = {
        'nombre_comercial': fields.char('Nombre Comercial',size=100),
        'activitytype':fields.many2one("res.company.activitytype", "Tipo de Actividad" ),
    }

res_company()

class activity_type(osv.osv):
    _name = 'res.company.activitytype'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Tipo de actividad", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
activity_type()
