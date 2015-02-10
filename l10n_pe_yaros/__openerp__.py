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
    "name": "Perú Localización - Tributaria",
    "version": "1.0",
    "author": "YarosLab SAC",
    "website": "http://www.yaroslab.com/",
    "category": "Localization",
    "description": """
    Agrega los atributos necesarios para la localización de Perú
    """,
    "depends": ["base", "sale","hr","hr_contract","l10n_pe_toponyms","account_asset",
		"account_accountant","purchase","account_payment"],
    "init_xml": [
        'stock/stock_data.xml',
    ],
    "demo_xml": [],
    "update_xml": [
        'account/account_view.xml',
        'account/existence_catalog_data.xml',
        'account_asset/account_asset_view.xml',
        'account_spot/account_view.xml',
        'account_spot/spot_data.xml',
        'account_invoice/account_invoice_view.xml',
        'account_voucher/account_voucher_view.xml',
        'payment_mode_type/payment_mode_type.xml',
        'base/base_view.xml',
        'base/typedoc_data.xml',
        'base/base_data.xml',
        'hr/hr_view.xml',
        'hr/hr_contract_view.xml',
        'hr/hr_data.xml',
        'product/product_view.xml',
        'res_company/res_company_view.xml',
        'res_partner/res_partner_view.xml',
        'res_bank/res_bank_data.xml',
        'sale/sale_typedocument_view.xml',
        'sale/sale_typedocument_data.xml',
        'stock/stock_data.xml',
        'stock/stock_view.xml',
        'security/ir.model.access.csv',
        'menus.xml',
        'res_bank/res_bank_view.xml'
        ],
    'installable': True,
    'active': False,
}
