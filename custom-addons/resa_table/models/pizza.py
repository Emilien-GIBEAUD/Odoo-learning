from odoo import models, fields


class Pizza(models.Model):
    _name = 'resa_table.pizza'
    _description = 'Pizza'

    name = fields.Char(string='Nom', required=True)
    ingredients = fields.Text(string='Ingrédients', required=True)
    price = fields.Float(string='Prix (€)', required=True)
    isActive = fields.Boolean(string='Visible', default=True)

