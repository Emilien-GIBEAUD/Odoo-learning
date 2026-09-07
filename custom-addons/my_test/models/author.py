from odoo import models, fields

class Author(models.Model):
    _name = 'my_test.author'
    _description = 'Auteur'

    author = fields.Char(required=True)
    birth_date = fields.Date(required=True)
    nationality = fields.Char(required=True)
    biography = fields.Text(required=True)
