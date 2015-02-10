# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#     Copyright (C) 2013 Consultoria YarosLab (<http://www.yaroslab.com> - info@yaroslab.com).
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
import base
import res_company
from .product.product import *
from .res_partner.res_partner import *
from hr.hr import *
from hr.hr_contract import *
import account_asset
from stock.stock import *
from account.account import  *
from account_spot.account import  *
import sale
from account_voucher.account_voucher import *
from account_invoice.accountinvoice import *
from payment_mode_type.payment_mode_type import *
from res_bank.res_bank import *
