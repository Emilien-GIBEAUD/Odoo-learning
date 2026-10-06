from odoo import models, fields, api

class Reservation(models.Model):
    _name = 'resa_table.reservation'
    _description = 'Réservation'

    name = fields.Char(string='Nom')
    first_name = fields.Char(string='Prénom')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Mobile')
    status = fields.Char(string='Statut', required=True)
    access_token = fields.Char(string='Token d\'accès')
    confirmation_expires_at = fields.Datetime(string='Expiration de la confirmation')
    slot_id = fields.Many2one('resa_table.service_slot', string='Créneau', required=True)
    reservation_item_ids = fields.One2many(
        'resa_table.reservation_item',
        'reservation_id',
        string='Items de réservation')


    @api.depends('name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = (
                f"{record.first_name} - "
                f"{record.name} - "
                f"{record.email} - "
                f"{record.phone}"
            )


    def _cron_expire_reservations(self):
        reservations = self.search([
            ('status', '=', 'PENDING'),
            ('confirmation_expires_at', '<', fields.Datetime.now()),
        ])
        reservations.write({
            'status': 'EXPIRED',
        })


    def _cron_outdate_reservations(self):
        reservations = self.search([
            ('status', '=', 'CONFIRMED'),
            ('slot_id.service_id.name', '<', fields.Date.today()),
        ])
        reservations.write({
            'status': 'OUTDATED',
        })
