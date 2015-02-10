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

from openerp.osv import osv, fields
from openerp.tools.translate import _

import urllib2
import requests, json
import time
from datetime import datetime, timedelta

    
class res_currency(osv.osv):
    _inherit = 'res.currency'
    
    def check_expired_contracts(self, cr, uid, context=None):
        today = datetime.now()
        date = today.strftime('%Y-%m-%d')
        print date
        anio=date[:4]
        month=date[5:7]
        day=date[8:10]
        
        response = urllib2.urlopen('http://code.staffsystems.us/webservices/tipo-de-cambio/serverside.php?work=get_sbs&anho='+str(anio)+'&mes=' + str(month)+'&dia='+ str(day))
        data = response.read()
        data_=data.replace("true", '"true"')
        data_1=data_.replace("null", '"null"')
        data_2=data_1.replace("false", '"false"')

        datas = eval(data_2)
        datos_fin = datas['data'][0]
        compra = datos_fin['compra']
        venta = datos_fin['venta']
        fecha = datos_fin['fecha']
        
        currency_obj = self.pool.get('res.currency')
        currency_id = currency_obj.search(cr, uid,[('name', '=', 'USD')])
        
        currency_res_obj = self.pool.get('res.currency.rate')
        
        if venta=='null' or venta==None:
            date_ant=today-timedelta(days=1)
            date_anterior = date_ant.strftime('%Y-%m-%d')
            
            currency_res_id = currency_res_obj.search(cr, uid,[('currency_id', '=', currency_id[0]),('name', '=', date_anterior)])     
            if currency_res_id:
                id_currency_res = currency_res_id[0]
                currency_res = currency_obj.read(cr, uid,id_currency_res, ['rate_change'])
                venta_ = currency_res['rate_change']
                currency_res_new_id = currency_res_obj.search(cr, uid,[('currency_id', '=', currency_id[0]),('name', '=',date)])
                if currency_res_new_id:
                    for rowline in currency_res_new_id[:]:
                        values ={'rate_change':venta_}
                        currency_res_obj.write(cr, uid, rowline, values, context=context)
                else:
                    values_ ={'name':date,'rate_change':venta_,'currency_id':currency_id[0]}
                    currency_res_obj.create(cr, uid, values_, context=context)
            else:
                venta_=0.001
                currency_res_new_id = currency_res_obj.search(cr, uid,[('currency_id', '=', currency_id[0]),('name', '=',date)])
                if currency_res_new_id:
                    for rowline in currency_res_new_id[:]:
                        values ={'rate_change':venta_}
                        currency_res_obj.write(cr, uid, rowline, values, context=context)
                else:
                    values ={'name':date,'rate_change':venta_,'currency_id':currency_id[0]}
                    currency_res_obj.create(cr, uid, values, context=context)
        else:
            currency_res_new_id = currency_res_obj.search(cr, uid,[('currency_id', '=', currency_id[0]),('name', '=',date)])
            if currency_res_new_id:
                for row in currency_res_new_id[:]:
                    values ={'name':date,'rate_change':venta}
                    currency_res_obj.write(cr, uid, row, values, context=context)
                #~ print "update"
            else:
                values ={'name':date,'rate_change':venta,'currency_id':currency_id[0]}
                y=currency_res_obj.create(cr, uid, values, context=context)
                #~ print "insert"
res_currency()



