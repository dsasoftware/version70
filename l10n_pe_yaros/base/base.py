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

from openerp.osv import osv, fields
from openerp.tools.translate import _
import re

class base_typedoc(osv.osv):
    _name = 'pe.base.typedoc'
    _description = 'Tipo de Documento de identidad'
    _columns = {
        'code': fields.char('Codigo Sunat', size=3, required=True),
        'name': fields.char('Descripción Tipo Documento', size=100, required=True),
    }
    _sql_constraints = [('name_uniq', 'unique (code)', 'El codigo del tipo de documento ya existe')]

base_typedoc()

""" Datos del Ubigeo """
class country_via(osv.osv):
    _name = 'res.country.via'
    _description = 'Especificando las vias de acceso'
    _columns = {
			'code': fields.char('Codigo', size=2, required=True),
            'name': fields.char('Descripción', size=64, required=True),            
            'abrev': fields.char('Abreviatura', size=10, required=True),       
        }
    _sql_constraints = [
            ('code_uniq','unique(code)',_('The code of the via must be unique !'))
        ]
country_via()	


class country_zona(osv.osv):
    _name = 'res.country.zona'
    _description = 'Especificando las zona de acceso'
    _columns = {
			'code': fields.char('Codigo', size=2, required=True),
            'name': fields.char('Descripción', size=64, required=True),            
            'abrev': fields.char('Abreviatura', size=10, required=True),       
        }
    _sql_constraints = [
            ('code_uniq','unique(code)',_('The code of the via must be unique !'))
        ]
country_zona()	

