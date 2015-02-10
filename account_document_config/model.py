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

from openerp.osv import orm, fields

class SaleTypedocumentConfig(orm.Model):

    _description = "Cuenta de la Factura"
    _name = "sale.typedocument.config"
    _columns = {
        'name': fields.many2one("sale.typedocument", "Documento de venta"
                ,domain=[('is_active', '=', True)],required=True),
        'sale_type': fields.selection((('sale',"Venta"),('purchase',"Compra")),"Tipo", required=True),
        'account_id': fields.many2one('account.account', string='Cuenta Contable', required=True),
        'currency_id': fields.many2one('res.currency', string='Moneda'),
    }
    _sql_constraints = [('code_unique','unique(name,sale_type,account_id)', 'El Codigo ya existe!')]


class AccountInvoice(orm.Model):
    _description = "Cuenta de la Factura"
    _inherit = "account.invoice"

    def onchange_account_sale(self, cr, uid, ids, typedoc_id, type='sale', currency_id=None, context=None):
        res = {}
        if (typedoc_id==None or currency_id==None):
            return res
        data = [('name','=',typedoc_id),('sale_type',"=",type),('currency_id','=',currency_id)]
        config_document_ids = self.pool.get('sale.typedocument.config').search(cr, uid, data , context=context)
        config_document = self.pool.get('sale.typedocument.config').\
            read( cr, uid, config_document_ids, context=context)
        if config_document:
            for config in config_document:
                res['account_id'] = config['account_id']
        return {'value': res}

