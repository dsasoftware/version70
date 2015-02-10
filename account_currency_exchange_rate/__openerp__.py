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
    "name": "Actualizacion tipo de cambio USD",
    "version": "1.0",
    "author": "Mariela Gamarra",
    "website": "http://www.yaroslab.com/",
    "category": "Localization",
    "description": """
    Crear un CROM que se ejecuta cada 8 horas para actualizar el tipo de cambio del USD en PEN basado en la URL,
    solo para Dolares
    http://code.staffsystems.us/webservices/tipo-de-cambio/serverside.php?work=get_sbs&anho
    """,
    "depends": ["base","account_accountant","l10n_pe_toponyms"],
    "init_xml": [],
    "demo_xml": [],
    "update_xml": [
        'res_currency_view.xml',
        ],
    'installable': True,
    'active': False,
}
