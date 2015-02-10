REPOSITORIO PUBLICO - LOCALIZACION PERU - YAROSLAB

El repositorio cuenta con los modulos localizados generales para Peru, los mismos que tiene son públicos.

DESCRIPCION DE LAS FUNCIONALIDADES

TOPONYMOS - L10N_PE_TOPONYMS
- Agrega modelos, vistas y datos el departamento, provincia, distrito ( partner, company )
- Agrega modelos, vistas y datos para direccion zona, vias ( partner ) 
- Agrega a la Compañia la provincia y distritoa la cual pertence

LOCALIZACION BASE YAROS -L10N_PE_YAROS
- Account: Se crean las siguientes tablas :
        Catalogo de existencias ( code, name ); Maestro de Detracciones(cod_sunat, state, name, percentage, amount)
- Account_asset: Se agregan los siguientes atributos
        'Tipo Activo Fijo: No revaluado o revaluado sin efecto tributario,Revaluado con efecto tributario
        'Estado Activo Fijo: Activos en desuso,Activos Obsoletos, Resto de activos
- Account_invoice: se agregaron los siguientes campos:
        (sale_type_document, serie, correlativo, detraccion_id,retencion_id,amount_type,amount_text)
- Account_spot: Objeto que permite configurar el SPOT de una forma diferente, cuenta con los siguientes datos:
        atributos: name, sunat_code,account_journal_id, account_journal_id_purchase, account_spot_detraccion_ids
         account_spot_retencion_ids
        se acregaron dos objetos adicionales:
            account.spot.retencion ( cod_sunat,state,name,percentage,amount,account_spot_id)
            account.spot.detraccion ( cod_sunat,state,name,percentage,amount,account_spot_id)
- Account_voucher: una tabla (account.voucher.type )y se agregaron los siguientes campos:
        account.voucher.type ( name, sunat_code, account_journal_id, account_journal_id_purchase, percentage)
        (mode_id, type_id, serie, correlativo, operation_type_detraction,num_operation)
- Base: Crea objetos tipo de documento identidad, vias, zonas, carga los datos necesarios
        Tipo de Documento de identidad - pe.base.typedoc: code, name
        Datos de Vias - res.country.via: name, code, abrev
        Datos de zona - res.country.zona: name, code, abrev
- HR    Crea barios objetivos
        hr.employee.educationlevel: name, code, abrev
        hr.employee.situacion: name, code, abrev
        hr.employee.relationship: name, code
        hr.employee.vinculedoc: name, code
        hr.employee.relatedperson: name, code
        Se agregan datos a:
        hr.employee:firts_name,typedoc,numtypedoc,last_name,last_name1,person_ruc,person_celular,person_phone,
                    person_email,person_educationlevel,person_dateegress,person_specialty,person_studycenter,
                    person_blood_group,person_situacion, person_tipo_pago,home_zona,home_via,home_state,
                    home_province,home_district,birth_state,birth_province,birth_district,family

- Product: Se agrega el campo para comprabar si el producto esta afento a Detracion
        product.template: detraccion
- RES-BANK: carga la lista de bancos peruanos
- res_company: atributos: nombre_comercial, activitytype
        Objeto: res.company.activitytype: code, code
- res_partner: firts_name,last_name1,last_name2,document_type,nro_documento,phone_home,phone_mobile,social_reason,state_vat,
                trade_name,retencion
- sale.typedocument: name,cod_sunat,is_active,is_venta,is_compra

THEMEYAROS
    Modulo que contiene plantilla-(CSS,JS) basica con los colores de YarosLab

ACCOUNT CURRENCY EXCHANGE RATE
    Modulo que actualiza cada 8 horas, el tipo de cambio de USD

ACCOUNT DOCUMENT CONFIG
    Modulo que permite configurar el documento de venta y cambiar el ACCOUNT de forma automatica

AUTO NUMBER TYPEDOCUMENT
    Modulo que permite crear una secuenta segun el tipo de documento

Toda contribución ( constructiva o no ) siempre sera bienvenida.
