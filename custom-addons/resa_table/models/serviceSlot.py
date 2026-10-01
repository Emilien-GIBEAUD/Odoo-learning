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
    display_reservation_time = fields.Char(
        string='Horaire', 
        compute='_compute_display_reservation_time', 
        store=False
    )
    duration = fields.Integer(string='Durée', compute='_compute_duration',store=False)
    reservation = fields.Integer(string='Réservations', compute='_compute_reservation',store=False)
    capacity = fields.Integer(string='Capacité', required=True)
    available_capacity = fields.Integer(string='Capacité disponible', compute='_compute_available_capacity', store=False)
    display_service = fields.Char(string='Service', related='service_id.display_service', store=False)
    service_id = fields.Many2one('resa_table.service', string='Service', required=True)
    reservation_ids = fields.One2many('resa_table.reservation', 'slot_id', string='Réservations')

    def _compute_duration(self):
        for slot in self:
            slot.duration = slot.service_id.slotDurationInMin

    def _compute_reservation(self):
        for slot in self:
            reservations = slot.reservation_ids.filtered(
                lambda reservation: reservation.status in ('PENDING', 'CONFIRMED')
            )
            slot.reservation = sum(
                reservations.mapped(
                    "reservation_item_ids.quantity"
                )
            )

    def _compute_available_capacity(self):
        for slot in self:
            slot.available_capacity = slot.capacity - slot.reservation

# To compute the display_slot
    @api.depends('name', 'duration', 'reservation', 'capacity')
    def _compute_display_slot(self):
        for slot in self:
            start_minutes = round(slot.name * 60)
            end_minutes = start_minutes + slot.duration

            start_hour, start_minute = divmod(start_minutes, 60)
            end_hour, end_minute = divmod(end_minutes, 60)

            available_capacity = slot.capacity - slot.reservation

            slot.display_slot = (
                f"{start_hour:02d}:{start_minute:02d} - "
                f"{end_hour:02d}:{end_minute:02d} ("
                f"{available_capacity}"
                f"{' pizzas disponibles' if available_capacity > 1 else ' pizza disponible'})"
            )

# To compute the display_reservation_time
    @api.depends('name')
    def _compute_display_reservation_time(self):
        for slot in self:
            minutes = round(slot.name * 60)
            hour, minute = divmod(minutes, 60)
            slot.display_reservation_time = (
                f"{hour:02d}:{minute:02d}"
            )

# To display display_slot instead of default name in "action_pizza_service_items"
    @api.depends('name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.display_slot