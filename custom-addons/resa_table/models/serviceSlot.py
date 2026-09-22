from odoo import models, fields

class ServiceSlot(models.Model):
    _name = 'resa_table.service_slot'
    _description = 'Créneau de service'

    name = fields.Float(string='Horaire', required=True)
    # slot_time = fields.Char(string='Horaire', compute='_compute_slot_time')
    capacity = fields.Integer(string='Capacité', required=True)
    service_id = fields.Many2one('resa_table.service', string='Service', required=True)

    # def _compute_slot_time(self):
    #     for slot in self:
    #         slot.slot_time = slot.name.strftime('%H:%M')