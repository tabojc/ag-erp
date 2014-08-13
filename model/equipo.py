from openerp.osv import osv, fields

class Equipo(osv.Model):
    _name = "visita.equipo"
    _columns = {
        'nombre' : fields.char(string="Nombre", size=256, required=False),
        'tipo': fields.selection([('tarjeta', 'Tarjeta'), ('computador', 'Computador'), ('laptop', 'Laptop'),], string='Tipo', readonly=True, 
		'serial' : fields.char(string="Nombre", size=256, required=False),
    }
