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

from openerp.osv import osv, fields, orm
from openerp.tools.translate import _
import re
import  urllib2
import  xml.etree.ElementTree as ElementTree

class ResPartner(orm.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Cliente Localizado a peru'
    _columns = {
        'firts_name' : fields.char('Nombre(s)', size=128),
        'last_name1' : fields.char('Apellido Paterno', size=128),
        'last_name2' : fields.char('Apellido Materno', size=128),
        
        'document_type' : fields.many2one('pe.base.typedoc','Tipo de Documento'),
        'nro_documento': fields.char('Nro. documento', size=12),
        'phone_home': fields.char('Teléfono fijo', size=30),
        'phone_mobile': fields.char('Teléfono movil', size=30),
        'social_reason': fields.char("Razón Social", size=64),
        'state_vat': fields.char("Estado RUC", size=64),
        'trade_name': fields.char("Nombre Comercial", size=64),
        'retencion': fields.many2one('account.spot.retencion',"Retención", domain=[('state','=',True)]),
        'percepcion': fields.many2one('account.spot.percepcion',"Percepcion", domain=[('state','=',True)]),
    }

    _defaults = {
        'retencion': False,
    }
    
    
    def search_vat(self, cr, uid, ids,  vat,context=None):
        print vat
        values = {}
        name = ''
        trade_name = ''
        street = ''
        mobile = ''
        state_vat = ''
        is_company = False
        firts_name = ''
        last_name1 = ''
        last_name2 = ''
        if vat is not False:
            if len(vat) >= 10:
                #~ print vat
                ruc=int(vat)
                response = urllib2.urlopen('http://www.sunat.gob.pe/w/wapS01Alias?ruc={}'.format(ruc))
                data = response.read()
                print data
                data = data.replace('\r', '').replace('\n', '').replace('\t', '').replace('<br/>', '')
                root = ElementTree.fromstring(data)
                card = root.find('card')
                if card.attrib['title'].lower() == 'resultado':
                    name = card.find('p').findall('small')[0].find('b').tail.split('-')[1].strip()
                    state_vat = card.find('p').findall('small')[3].find('b').tail.strip()
                    trade_name = card.find('p').findall('small')[5].find('b').tail.strip()
                    street = card.find('p').findall('small')[6].find('b').tail.strip()
                    mobile = card.find('p').findall('small')[8].find('b').tail.strip()
                    #~ raise osv.except_osv('Error', vat[:2])
                    if vat[:2]=='20':
                        is_company=True
                    else:
                        is_company=False
                        tmpname = name
                        ln1, ln2, fn = tmpname.split(" ",2)
                        firts_name = fn
                        last_name1 = ln1
                        last_name2 = ln2
                    #if state_vat!='ACTIVO':
                    #    raise osv.except_osv('Error', 'El RUC que intenta ingresar no esta Activo')
            else:
                    raise osv.except_osv('Error', 'RUC NO VALIDO!.'.decode('utf8'))

        if trade_name=="-" or trade_name=="":
            trade_name = name
        values['name'] = trade_name
        values['social_reason'] = name
        values['trade_name'] = trade_name
        values['street'] = street
        values['mobile'] = mobile
        values['state_vat'] = state_vat
        values['is_company'] = is_company
        values['firts_name'] = firts_name
        values['last_name1'] = last_name1
        values['last_name2'] = last_name2
        return {'value':values}
ResPartner()
