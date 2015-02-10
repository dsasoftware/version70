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

from openerp.osv import fields, osv

class sale_typedocument_generate(osv.osv):
    _name = "sale.typedocument.generate"
    
    _columns = {
        'sale_shop_id' : fields.many2one('sale.shop','Almacen',required=True), # No soporta para Version 8
        'serie' : fields.char('Serie', size = 3, required=True),
        'number_next' : fields.char('Número siguiente', size = 10, required=True),
        'padding' : fields.integer("Relleno del número",required=True),        
        'document_type' : fields.many2one('sale.typedocument','Tipo de Documento',required=True),
    }
    _sql_constraints = [('name_uniq', 'unique (sale_shop_id,document_type)', 'La tienda y el tipo de documento deben de ser unicos')]
    
    _defaults = {
        'serie': '001',
        'number_next': '1',
        'padding': 4,
    }
sale_typedocument_generate()

class sale_typedocument(osv.osv):
    _inherit = "sale.typedocument"
    _columns = {
        'generates' : fields.one2many('sale.typedocument.generate','document_type',string='Tipo de Documento'),
    }
sale_typedocument()
