# coding:utf-8
from openerp.osv import orm, fields


class AccountVoucher(orm.Model):
    _inherit = 'account.voucher'
    def onchange_type(self, cr, uid, ids, type_id, context=None):
        res = {}
        if type_id :
            #config_document_ids = self.pool.get('account.voucher.type').search(cr, uid, data , context=context)
            type = self.pool.get('account.voucher.type').read( cr, uid, type_id, context=context)
            print type
            if type:
                if type['type_config']=='01' and type['account_id']:
                    res['account_id'] = type['account_id']
                if type['type_config']=='02' and type['account_journal_id']:
                    res['journal_id'] = type['account_journal_id']

        return {'value': res}

    _columns = {
        'invoice_id': fields.many2one('account.invoice', string='Invoice'),# Tipo documento cobro/pago
        'mode_id': fields.many2one('payment.mode.type', string='Modo de Pago'),# Tipo documento cobro/pago
        'spot_id': fields.many2one('account.spot', string='SPOT'),# Si tiene retencion/detraccion/percepcion
        'serie': fields.char('Serie',size=4), # aplica a retencion/percepcion/cheque
        'correlative': fields.char('Correlativo',size=8), # aplica a retencion/percepcion/cheque
        'operation_type_detraction': fields.selection(            (
                ('01', 'Venta de Bienenes o Pres. Serv.'),
                ('02', 'Retiro de Vienes Gravados IGV'),
                ('03', 'Translado que No son Venta'),
                ('04', 'Venta a traves de Bolsa de Productos'),
                ('05', 'Venta de Bienes exonerados del IGV'),
            ),"Tipo Operacion"), # aplica detraccion

        'num_operation': fields.char('# Operacion',size=10), # aplica a retencion, transferencia
    }


    def _get_type(self, cr, uid, context=None):
        if context is None:
            context= {}
        print context
        return  context.get('type_id', False)
    _defaults = {
        'spot_id': _get_type,
    }

