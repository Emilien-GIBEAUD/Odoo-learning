from odoo import models, fields, api

class ReservationItem(models.Model):
    _name = 'resa_table.reservation_item'
    _description = 'Item de réservation'

    name = fields.Char(string='Nom', required=True)
    unit_price = fields.Float(string='Prix unitaire (€)', required=True)
    quantity = fields.Integer(string='Quantité', required=True)
    reservation_id = fields.Many2one('resa_table.reservation', string='Réservation', required=True)
    slot_id = fields.Many2one(
        'resa_table.service_slot',
        string='Créneau',
        related='reservation_id.slot_id',
        store=True,
    )