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

from openerp.osv import orm, fields, osv
from openerp.tools.translate import _

import amount_text


class AccountInvoice(orm.Model):

    _description = "Cuenta de la Factura"
    _inherit = "account.invoice"

    def _get_detraccion_id(self, cr, uid, ids, field_name, args=None, context=None):
        res = {}
        f = 0
        for record in self.browse(cr, uid, ids, context=context):
            if len(record.invoice_line) and record.invoice_line[f].product_id.detraccion.amount <= record.amount_total:
                res[record.id] = record.invoice_line[0].product_id.detraccion.id
            else:
                res[record.id] = False
            f = f + 1
        return res

    def _get_retencion_id(self, cr, uid, ids, field_name, args=None, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            if record.partner_id.retencion and record.retencion_id.amount <= record.amount_total:
                res[record.id] = record.partner_id.retencion.id
            else:
                res[record.id] = False
        return res

    def _get_amount_type(self, cr, uid, ids,field_name, args=None, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            if record.retencion_id:
                res[record.id] = (record.retencion_id.percentage / 100.0) * record.amount_total
            else:
                if record.detraccion_id:
                    res[record.id] = (record.detraccion_id.percentage / 100.0) * record.amount_total
                else:
                    res[record.id] = False
        return res

    # Funcion que cambia el diario de compras/ventas segun el tipo de documento
    def _get_type_document(self, cr, uid, context=None):
        db_sale_type_document = self.pool.get('sale.typedocument')
        default_type_document_code = '01'
        if 'journal_type' in context:
            document_type_ids = db_sale_type_document.search(cr, uid, [('cod_sunat', '=', '07')])[0]
            if document_type_ids and context['journal_type'] == 'sale_refund':
                return document_type_ids
            document_type_ids = db_sale_type_document.search(cr, uid, [('cod_sunat', '=', '08')])[0]
            if document_type_ids and context['journal_type'] == 'purchase_refund':
                return document_type_ids
        res = db_sale_type_document.search(cr, uid, [('cod_sunat', '=', default_type_document_code)])
        if not res:
            return False
        return res[0]


    def invoice_validate(self, cr, uid, ids, context=None):
        self._get_amount_type(cr, uid, ids,context)
        self.write(cr, uid, ids, {'state':'open'}, context=context)
        inv = self.browse(cr, uid, ids[0], context=context)

        if inv.type=='in_invoice' or inv.type =='out_invoice':
            if (inv.detraccion_id or inv.retencion_id):
                #  Obtiene el diario de para cobrar a los clientes
                types_d = {}
                type_ids_1 = {}
                if inv.retencion_id:
                    type_ids_1 = self.pool.get('account.spot.retencion').\
                        read(cr, uid,inv.retencion_id.id,['account_spot_id'])
                else:
                    type_ids_1 = self.pool.get('account.spot.detraccion').\
                        read(cr, uid,inv.detraccion_id.id,['account_spot_id'])
                spot_id = type_ids_1['account_spot_id'][0]
                if not spot_id:
                    raise osv.except_osv('Alerta', 'No esta configurado Detracciones/Retenciones/Percepciones')
                tmp_journal_id = self.pool.get('account.spot').read(cr, uid, spot_id,
                                            ['id','account_journal_id','account_journal_id_purchase'])
                if not (tmp_journal_id['account_journal_id'] or tmp_journal_id['account_journal_id_purchase']):
                    raise osv.except_osv('Alerta', 'No estan asociados los diarios para la DETRACCION ')
                #Para ventas
                if (inv.type=='out_invoice'):
                    journal_id =tmp_journal_id['account_journal_id'][0]
                    tmp_account_id = self.pool.get('account.journal').read(cr, uid, journal_id,
                                                                       ['id','default_debit_account_id'])
                    account_id = tmp_account_id['default_debit_account_id'][0]
                # Para compras
                if (inv.type=='in_invoice'):
                    journal_id =tmp_journal_id['account_journal_id_purchase'][0]
                    tmp_account_id = self.pool.get('account.journal').read(cr, uid, journal_id,
                                                                       ['id','default_credit_account_id'])
                    account_id = tmp_account_id['default_credit_account_id'][0]
                account_voucher = self.pool.get('account.voucher')
                pagos =  {
                    'partner_id': self.pool.get('res.partner')._find_accounting_partner(inv.partner_id).id,
                    'date': inv.date_due,
                    'spot_id': spot_id,
                    'reference': inv.name,
                    'period_id': inv.period_id.id,
                    'currency_id': inv.currency_id.id,
                    'payment_rate_currency_id': inv.currency_id.id,
                    'pay_now': 'pay_now',
                    'pre_line': True,
                    'payment_rate': 1.0,
                    'type': inv.type in ('out_invoice','out_refund') and 'receipt' or 'payment',
                    'payment_option': 'without_writeoff',
                    'company_id': inv.company_id.id,
                    'state': 'posted',
                    'amount': inv.amount_type, #Monto detraccion
                    'is_multi_currency': False,
                    #'active': True,
                    'account_id': account_id,
                    'journal_id': journal_id,
                    'invoice_id': inv.id,
                }
                id_= account_voucher.create(cr,uid,pagos,context=None)
                if id_:
                    # Buscar le move_id del voucher
                    account_move_lines = self.pool.get('account.move.line')
                    move_ids = account_move_lines.search(cr, uid, [('move_id', '=', inv.move_id.id),
                                                          ('account_id', '=', inv.account_id.id)])[0]
                    if move_ids:
                        account_voucher_line = self.pool.get('account.voucher.line')
                        linea_pagos = {
                            'reconcile': False,
                            'voucher_id': id_,
                            'amount_unreconciled':inv.amount_type,
                            'amount_original':inv.amount_total,
                            'amount': inv.amount_type, #Monto detraccion
                            'account_id': inv.account_id.id,
                            'name': inv.number,
                            'move_line_id': move_ids,
                            'company_id': inv.company_id.id,
                            'type': inv.type in ('out_invoice','out_refund') and 'cr' or 'dr',
                        }
                        id_line = account_voucher_line.create(cr,uid,linea_pagos,context=None)
        return True


    def invoice_pay_customer(self, cr, uid, ids, context=None):

        if not ids: return []
        dummy, view_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'account_voucher', 'view_vendor_receipt_dialog_form')
        inv = self.browse(cr, uid, ids[0], context=context)
        # Variables por defecto del metodo padre
        default_amount = inv.residual
        detraccion_id = inv.detraccion_id.id
        retencion_id = inv.retencion_id.id
        amount_type = inv.amount_type
        #Condicion para el cobro a clientes
        if inv.state == 'open' and inv.type == 'out_invoice' and detraccion_id :
            invoice_name = inv.internal_number
            payment_ids = self.pool.get('account.voucher').search(cr, uid,[('invoice_id', '=', inv.id),
                                ('type','=','receipt'),('spot_id', '=', 1)])

            print "entro"
            print payment_ids
            #verificando si ya se tiene algun pago la detraccion
            if not payment_ids:
                default_amount = amount_type

        print " monto det: "+str(default_amount)+" saldo: "+str(default_amount)+ " detraccion_id:"+str(detraccion_id)
        return {
            'name':_("Pay Invoice"),
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'form',
            'res_model': 'account.voucher',
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'domain': '[]',
            'context': {
                'payment_expected_currency': inv.currency_id.id,
                'default_partner_id': self.pool.get('res.partner')._find_accounting_partner(inv.partner_id).id,
                'default_amount': default_amount,
                'default_reference': inv.name,
                'close_after_process': True,
                'invoice_type': inv.type,
                'invoice_id': inv.id,
                'default_type': inv.type in ('out_invoice','out_refund') and 'receipt' or 'payment',
                'type': inv.type in ('out_invoice','out_refund') and 'receipt' or 'payment',
                'amount_type': amount_type,
                'spot_id': 1,
            }
        }



    _columns = {
        'sale_type_document': fields.many2one("sale.typedocument", "Documento de venta",
                                              domain=[('is_active', '=', True)]),
        'serie': fields.char('Serie', size=4),
        'correlativo': fields.char('Correlativo', size=8),
        'detraccion_id': fields.function(_get_detraccion_id, string='Detracción', type='many2one',
                                         relation='account.spot.detraccion', method=True, store=True),
        'retencion_id': fields.function(_get_retencion_id, string='Retención', type='many2one',
                                         relation='account.spot.retencion', method=True, store=True),
        'amount_type': fields.function(_get_amount_type, string=u'Monto Tipo', method=True,
                                             store=True, type='float'),
        'amount_text': fields.char("Monto Total", size=250),
    }

    _defaults = {
        'sale_type_document': _get_type_document,
    }




class AccountInvoiceLine(orm.Model):
    _inherit = 'account.invoice.line'
    _columns = {
        'product_id': fields.many2one('product.product', 'Product', ondelete='set null', select=True, required=True),
    }
