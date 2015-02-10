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
# - TABLA 10: TIPO DE COMPROBANTE DE PAGO O DOCUMENTO
class sale_typedocument(osv.osv):
    _name = "sale.typedocument"
    _description = "Tipo de documento de venta"

    _columns = {
        'name' : fields.char('Nombre', size = 250, required=True),
        'cod_sunat' : fields.char("Código sunat",size=2,required=True),
        'is_active' : fields.boolean("Activo"),
        'is_venta': fields.boolean('Venta'), # Si el codigo es de tipo venta
        'is_compra': fields.boolean('Compra'), # Si el codigo es de tipo compra
    }
    _sql_constraints = [('name_uniq', 'unique (cod_sunat)', 'No se deben de repetir los codigos de sunat')]
    _defaults = {
        'is_venta': False,
        'is_compra': False,
        'is_active': False,
    }


sale_typedocument()
