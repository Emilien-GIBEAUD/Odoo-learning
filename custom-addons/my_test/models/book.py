from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Book(models.Model):
    _name = 'my_test.book'
    _description = 'Livre'

    title = fields.Char(required=True)
    author = fields.Char(required=True)
    year = fields.Integer(required=True)
    description = fields.Text(required=True)

    @api.constrains('year')
    def _check_year(self):
        for book in self:
            if book.year > datetime.now().year:
                raise ValidationError("L'année ne peut pas être dans le futur.")