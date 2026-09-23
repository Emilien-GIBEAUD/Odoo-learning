from odoo import models, fields

class ServiceSlot(models.Model):
    _name = 'resa_table.service_slot'
    _description = 'Créneau de service'

    name = fields.Float(string='Horaire', required=True)
    duration = fields.Integer(string='Durée', compute='_compute_duration',store=False)
    reservation = fields.Integer(string='Réservations', compute='_compute_reservation',store=False)
    capacity = fields.Integer(string='Capacité', required=True)
    service_id = fields.Many2one('resa_table.service', string='Service', required=True)
    display_service = fields.Char(string='Service', related='service_id.display_service', store=False)

    def _compute_duration(self):
        for slot in self:
            slot.duration = slot.service_id.slotDurationInMin

    def _compute_reservation(self):
        for slot in self:
            slot.reservation = 0    # A modifier quand les réservations seront implémentées