from odoo import models, fields, api

class ServiceSlot(models.Model):
    _name = 'resa_table.service_slot'
    _description = 'Créneau de service'

    name = fields.Float(string='Horaire', required=True)
    display_slot = fields.Char(
        string='Créneau', 
        compute='_compute_display_slot', 
        store=False
    )
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

# To compute the display_service
    @api.depends('name', 'duration', 'reservation', 'capacity')
    def _compute_display_slot(self):
        for slot in self:
            slot_end_time = slot.name + (slot.duration / 60)
            available_capacity = slot.capacity - slot.reservation
            slot.display_slot = (
                f"{int(slot.name):02d}:{round((slot.name % 1) * 60):02d} - "
                f"{int(slot_end_time):02d}:{round((slot_end_time % 1) * 60):02d} ("
                f"{available_capacity}{' pizzas disponibles' if available_capacity > 1 else ' pizza disponible'})"
            )
