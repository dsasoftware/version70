# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Consultoria YarosLab SAC(<http://www.yaroslab.com>).
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

from openerp.osv import fields, osv
import time
from datetime import date

class education_level(osv.osv):
    _name = 'hr.employee.educationlevel'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Nivel Educación", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }

education_level()

class situacion_trabajador(osv.osv):
    _name = 'hr.employee.situacion'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Situación Trabajador", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }

situacion_trabajador()


class hr_employee_relationship(osv.osv):
    _name = 'hr.employee.relationship'    
    _columns = {
        'code': fields.char('Codigo', size=3,required=True),
        'name': fields.char('Vinculo Familiar',size=100, required=True),
    }    
hr_employee_relationship()

class hr_employee_vinculedoc(osv.osv):
    _name = 'hr.employee.vinculedoc'    
    _columns = {
        'code': fields.char('Codigo', size=3,required=True),
        'name': fields.char('Documento Vinculo Familiar',size=100, required=True),
    }    
hr_employee_vinculedoc()

class hr_related_person(osv.osv):
    _name = 'hr.employee.relatedperson'
    def _get_age(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for obj in self.browse(cr, uid, ids):
            res[obj.id] = self._calculate_age(obj.birthday)
        return res

    def _calculate_age(self, birthday):
        today = date.today()
        if birthday:
            _birth = date.strptime(birthday, '%Y-%m-%d')
            diff = today - _birth
            return int(diff.days / 365.2425)
        else:
            return False

    def on_change_birthday(self, cr, uid, ids, birthday, context=None):
        return {
            'value': {
                'age': self._calculate_age(birthday)
            }
        }
    _columns = {
        'employee_id': fields.many2one('hr.employee', string='Employee'),
        'full_name': fields.char(size=100, string='Nombres y apellidos', required=True),
        'dni': fields.char(size=8, string='DNI', required=True),
        'birthday': fields.date('Fecha de nacimiento'),
        'sex': fields.selection(selection=[
            ('M', 'Masculino'),
            ('F', 'Femenino')
        ], string='Sexo'),
        'age': fields.function(_get_age, method=True, store=False, type='integer', string='Edad'),        
        'relationship':fields.many2one("hr.employee.relationship", "Vinculo Familiar", required=True),
        'vinculuedoc': fields.many2one('hr.employee.vinculedoc','Documento Acredita'),
        'comment': fields.text('Comentario'),
    }

hr_related_person()



class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    _columns = {
        'firts_name': fields.char('Nombre(s)', size=250),
        'typedoc': fields.many2one('pe.base.typedoc','Tipo de Documento'),
        'numtypedoc': fields.char('Numero de Documento',size=15),
        'last_name': fields.char('Apellido Paterno', size=250),
        'last_name1': fields.char('Apellido Materno', size=250),
        'person_ruc': fields.char('RUC', size=11),
        'person_celular': fields.char('Célular', size=9),
        'person_phone': fields.char('Teléfono', size=9),
        'person_email': fields.char('Correo Personal', size=240),
        'person_educationlevel':fields.many2one("hr.employee.educationlevel", "Nivel Educacion" ),      
        'person_dateegress': fields.date('Fecha de Egreso'),
        'person_specialty': fields.char('Especialidad/Prog.Académico', size=240),
        'person_studycenter': fields.char('Centro de Estudios', size=240),
	    'person_blood_group': fields.selection(selection=[
            ('O+', 'O+'),
            ('O-', 'O-'),
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-')
        ], string='Grupo sanguineo'),
	    'person_situacion':fields.many2one("hr.employee.situacion", "Situación Trabajador" ),
	    'person_tipo_pago': fields.selection([
            ('1', 'EFECTIVO'),
            ('2', 'DEPOSITO EN CUENTA'),
            ('3', 'OTROS')], 'Tipo de Pago'),
        'home_zona':fields.many2one("res.country.zona", "Zona" ),
        'home_via':fields.many2one("res.country.via", "Via" ),
        'home_state': fields.many2one('res.country.state', 'Departamento'),
        'home_province': fields.many2one('res.country.province','Provincia'),
        'home_district': fields.many2one('res.country.district', 'Distrito'),
        'birth_state': fields.many2one('res.country.state', 'Departamento'),
        'birth_province': fields.many2one('res.country.province','Provincia'),
        'birth_district': fields.many2one('res.country.district','Distrito'),
        'family': fields.one2many('hr.employee.relatedperson', 'employee_id', string='Family',
                                  domain=[('family_rel', '=', True)], context={'family_rel': True}),
    }
hr_employee()

