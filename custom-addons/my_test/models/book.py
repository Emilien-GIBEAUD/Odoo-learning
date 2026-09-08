from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Book(models.Model):
    _name = 'my_test.book'
    _description = 'Livre'

    name = fields.Char(string='Titre', required=True)
    author_id = fields.Many2one('my_test.author', string='Auteur', required=True)
    year = fields.Integer(string='Année', required=True)
    description = fields.Text(string='Description', required=True)

    @api.constrains('year')
    def _check_year(self):
        for book in self:
            if book.year > datetime.now().year:
                raise ValidationError("L'année ne peut pas être dans le futur.")