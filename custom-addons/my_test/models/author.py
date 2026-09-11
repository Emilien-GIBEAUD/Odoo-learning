from odoo import models, fields

class Author(models.Model):
    _name = 'my_test.author'
    _description = 'Auteur'

    name = fields.Char(string='Nom', required=True)
    birth_date = fields.Date(string='Date de naissance', required=True)
    biography = fields.Text(string='Biographie', required=True)
    nationality_ids = fields.Many2many(
                                        'my_test.nationality',
                                        string='Nationalité',
                                        required=True)
    book_ids = fields.One2many(
                                'my_test.book',
                                'author_id',
                                string='Livres')
