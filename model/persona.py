from openerp.osv import osv, fields

class Persona(osv.Model):
    _inherit = 'res.partner'

    def onchange_documento(self, cr, uid, ids, documento, context=None):
        values  = {}
        mensaje = ''
        tabla = 0
        if not documento:
            return values

        obj_empleado = self.pool.get('hr.employee')
        srch_id = obj_empleado.search(cr, uid,[('identification_id', '=', documento)])
        
        if not srch_id:
            obj_partner = self.pool.get('res.partner')
            srch_id = obj_partner.search(cr, uid,[('vat', '=', documento)])
            if srch_id:
                tabla = 2
        else:
            tabla = 1
            
        if tabla == 0:
            #registro nuevo
            values.update({'nombre' : '', 'telefono': '', 'es_empleado': False})
            #mensaje = {'title':'Aviso','message':'Nuevo Visitante!'}
        elif tabla == 1:
            #encontrado en empleado
            rd_data = obj_empleado.read(cr, uid, srch_id, context=context)
            values.update({'nombre' : rd_data[0]['name'], 'telefono': rd_data[0]['work_phone'], 'es_empleado': True})
            #mensaje = {'title':'Aviso','message':'Empleado encontrado!'}
        else:
            #encontrado en partner
            rd_data = obj_partner.read(cr, uid, srch_id, context=context)
            values.update({'nombre' : rd_data[0]['name'], 'telefono': rd_data[0]['phone'], 'es_empleado': False})
            #mensaje = {'title':'Aviso','message':'Visitante encontrado!'}

        return {'value' : values}
        #si se quiere mostrar mensajes gays
        #return {'value' : values , 'warning': mensaje} 
    _sql_constraints = [
        ('vat_unique',
        'UNIQUE(vat)',
        'El Documento debe ser unico'),
    ]

"""res_partner
    vat
    
hr_employee
    identification_id
    other_id
visita

browse -> res parter
read ->res_users
"""
