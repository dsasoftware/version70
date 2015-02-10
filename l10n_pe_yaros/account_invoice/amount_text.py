#! /usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import ifilter
UNIDADES = (
    '',
    'UN ',
    'DOS ',
    'TRES ',
    'CUATRO ',
    'CINCO ',
    'SEIS ',
    'SIETE ',
    'OCHO ',
    'NUEVE ',
    'DIEZ ',
    'ONCE ',
    'DOCE ',
    'TRECE ',
    'CATORCE ',
    'QUINCE ',
    'DIECISEIS ',
    'DIECISIETE ',
    'DIECIOCHO ',
    'DIECINUEVE ',
    'VEINTE '
)

DECENAS = (
    'VENTI',
    'TREINTA ',
    'CUARENTA ',
    'CINCUENTA ',
    'SESENTA ',
    'SETENTA ',
    'OCHENTA ',
    'NOVENTA ',
    'CIEN '
)

CENTENAS = (
    'CIENTO ',
    'DOSCIENTOS ',
    'TRESCIENTOS ',
    'CUATROCIENTOS ',
    'QUINIENTOS ',
    'SEISCIENTOS ',
    'SETECIENTOS ',
    'OCHOCIENTOS ',
    'NOVECIENTOS '
)



def to_word(number, mi_moneda=None):

    moneda = ""
    converted = ''
    #~ print number
    if not (0 < number < 999999999):
        #~ print number
        if number==0:
            converted='CERO'
        else:
            return 'No es posible convertir el numero a letras'
    number_str = str(number).zfill(9)
    #~ print number
    millones = number_str[:3]
    #~ print millones 
    miles = number_str[3:6]
    #~ print miles
    cientos = number_str[6:]
    #~ print cientos

    if(millones):
        if(millones == '001'):
            converted += 'UN MILLON '
        elif(int(millones) > 0):
            converted += '%sMILLONES ' % __convert_group(millones)

    if(miles):
        if(miles == '001'):
            converted += 'MIL '
        elif(int(miles) > 0):
            converted += '%sMIL ' % __convert_group(miles)

    if(cientos):
        if(cientos == '001'):
            converted += 'UN '
        elif(int(cientos) > 0):
            converted += '%s ' % __convert_group(cientos)

    converted += moneda

    return converted.title()


def __convert_group(n):
    output = ''

    if(n == '100'):
        output = "CIEN "
    elif(n[0] != '0'):
        output = CENTENAS[int(n[0]) - 1]

    k = int(n[1:])
    if(k <= 20):
        output += UNIDADES[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%sY %s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])
        else:
            output += '%s%s' % (DECENAS[int(n[1]) - 2], UNIDADES[int(n[2])])

    return output

def text_convert(n):

    amount=str(n)
    amount=amount.split('.' or ",", 1 )
    if len(amount)==1:
        value = to_word(int(n))
    else:
        if len(amount)==2:
            entero = to_word(int(amount[0]))
            decimal = to_word(int(amount[1]))
            val=str(amount[1])+'/100'
            value = entero + "Con " + val
                #~ value = entero + "Con " + decimal + "Centimos"                
        else:
            value = "No se puede convertir"
    return value
    

print text_convert(30.00)
