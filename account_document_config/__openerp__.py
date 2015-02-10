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

{
    "name": "PE - Cambio de Cuenta segun Comprobante de Pago",
    "version": "1.0",
    "author": "YarosLab SAC",
    "website": "http://www.yaroslab.com/",
    "category": "Localization",
    "description": """
    Permite cambiar la cuenta de la factura venta/compra segun el tipo de comprobante pago
    """,
    "depends": ["base", "sale","l10n_pe_yaros"],
    "init_xml": [],
    "demo_xml": [],
    "update_xml": [
        'view.xml',
        'security/ir.model.access.csv',
        'menus.xml',
        ],
    'installable': True,
    'active': False,
}
