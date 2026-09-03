from odoo import models, fields, api


class resa_table(models.Model):
    _name = 'resa_table.resa_table'
    _description = 'resa_table.resa_table'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

