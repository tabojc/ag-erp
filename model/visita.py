from openerp.osv import osv, fields

class Visita(osv.Model):
    _name = "visita.visita"
    _columns = {
		'visitante_id' : fields.many2one('res.partner', string="Visitante", ),
        'fecha_entrada': fields.datetime('Entrada'),
        'fecha_salida': fields.datetime('Salida'),
        #'empleado_id' : fields.many2one('hr.employee', string="Visitante", ),
        #'departamento_id' : fields.many2one('hr_department', string="Visitante", ),
        #'equipo_id' : fields.many2one('visita.equipo', string="Equipo", ),
    }
