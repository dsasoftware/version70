# coding: utf-8

from openerp.osv import orm, fields


class ResPatnerBank(orm.Model):

    _inherit = 'res.partner.bank'

    _columns = {
        'detraccion': fields.boolean(u'Detracción')
    }

    _defaults = {
        'detraccion': False
    }
