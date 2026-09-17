from odoo import models, fields


class ServiceTemplate(models.Model):
    _name = 'resa_table.service_template'
    _description = 'Modèle de service'

    name = fields.Char(string='Nom', required=True)
    startTime = fields.Float(string='Début service', required=True)
    endTime = fields.Float(string='Fin service', required=True)
    slotDurationInMin = fields.Integer(string='Durée créneau (min.)', required=True)
    capacityPerSlot = fields.Integer(string='Capacité créneau', required=True)
    isActive = fields.Boolean(string='Visible', default=True)

