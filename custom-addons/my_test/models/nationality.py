from odoo import models, fields

class Nationality(models.Model):
    _name = 'my_test.nationality'
    _description = 'Nationalité'

    name = fields.Char(string='Nationalité', required=True)
