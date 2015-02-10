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
#- OCUPACIÓN APLICABLE A TRABAJ DE SÉCTOR PÚBLICO, OTRAS ENTIDADES Y PERS EN FORMACIÓN
class ocupation(osv.osv):
    _name = 'hr.employee.ocupation'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Ocupación del Trabajador", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
ocupation()

#- TIPO DE TRABAJADOR, PENSIONISTA O PRESTADOR DE SERVICIOS.
class type_employe(osv.osv):
    _name = 'hr.contract.typeemploye'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Tipo Trabajador", required=True),
        'abriv': fields.char("Abreviatura", required=True),
        'private': fields.boolean("Sector Privado"),
        'public': fields.boolean("Sector Publico"),
         'others': fields.boolean("Otras Entidades"),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
type_employe()

#- RÉGIMEN PENSIONARIO.
class regimen_pensionario(osv.osv):
    _name = 'hr.contract.regimenpensionario'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Regimen Pensionario ", required=True),
        'abriv': fields.char("Abreviatura", required=True),
        'private': fields.boolean("Sector Privado"),
        'public': fields.boolean("Sector Publico"),
        'others': fields.boolean("Otras Entidades"),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
regimen_pensionario()

#- TIPO DE CONTRATO DE TRABAJO/CONDICIÓN LABORAL.
class type_contract(osv.osv):
    _name = 'hr.contract.types'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Tipo de Contrato", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
type_contract()

#- MOTIVO DEL FIN DEL CONTRATO O DE LA BAJA DEL T-REGISTRO.
class motivo_baja(osv.osv):
    _name = 'hr.contract.motivobaja'
    _columns = {
        'code': fields.char("Codigo",size=5,required=True),
        'name': fields.char("Motiv de Baja", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
motivo_baja()

#- TIPO DE MODALIDAD FORMATIVA LABORAL Y OTROS.
class movilidad_formativa(osv.osv):
    _name = 'hr.contract.movilidadformativa'
    _columns = {
        'code': fields.char("Codigo",size=2,required=True),
        'name': fields.char("Movilidad Formativa", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
movilidad_formativa()

#- CATEGORIA OCUPACIONAL DEL TRABAJADOR.
class categoria_ocupacional(osv.osv):
    _name = 'hr.contract.categoriaocupacional'
    _columns = {
        'code': fields.char("Codigo",size=2,required=True),
        'name': fields.char("Categoria Ocupacional", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
categoria_ocupacional()


#- - OCUPACIÓN APLICABLE AL SECTOR PRIVADO.
class ocupacional_private(osv.osv):
    _name = 'hr.contract.ocupacionalprivate'
    _columns = {
        'code': fields.char("Codigo",size=2,required=True),
        'name': fields.char("Ocupación Sector Priv.", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
ocupacional_private()


#- TIPO DE SUSPENSIÓN DE LA RELACIÓN LABORAL.
class suspention_type(osv.osv):
    _name = 'hr.contract.suspentiontype'
    _columns = {
        'code': fields.char("Codigo",size=2,required=True),
        'name': fields.char("Tipo Suspencion", required=True),
        'abriv': fields.char("Abreviatura", required=True),
    }
    _sql_constraints = [('code_uniq','unique(code)', 'El Codigo ya existe!')]
suspention_type()

class hr_contract(osv.osv):
    _inherit = 'hr.contract'
    _columns = {
        'ocupation': fields.many2one('hr.employee.ocupation','Ocupación'),
        'employetype': fields.many2one('hr.contract.typeemploye','Tipo Empleado'),
        'regimenpensionario': fields.many2one('hr.contract.regimenpensionario','Regimen Pensionario'),
        'typecontract': fields.many2one('hr.contract.type','Tipo Contrato Sunat'),
        'motivobaja': fields.many2one('hr.contract.motivobaja','Motivo Baja'),
        'movilidadformativa': fields.many2one('hr.contract.movilidadformativa','Movilidad Formativa'),
        'categoriaocupacional': fields.many2one('hr.contract.categoriaocupacional','Categoria Ocupacional'),
        'ocupacionalprivate': fields.many2one('hr.contract.ocupacionalprivate','Ocupacional Sector Priv'),
        'suspentiontype': fields.many2one('hr.contract.suspentiontype','Tipo de Suspención'),
    }

hr_contract()
