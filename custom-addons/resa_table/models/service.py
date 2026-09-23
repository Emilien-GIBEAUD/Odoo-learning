from odoo import models, fields, api

class Service(models.Model):
    _name = 'resa_table.service'
    _description = 'Service'

    name = fields.Date(string='Date de service', required=True)
    display_service = fields.Char(
        string='Service', 
        compute='_compute_display_service', 
        store=False
    )
    template_id = fields.Many2one(
        'resa_table.service_template',
        string="Utiliser un modèle",
        store=False
    )
    startTime = fields.Float(string='Début service', required=True)
    endTime = fields.Float(string='Fin service', required=True)
    slotDurationInMin = fields.Integer(string='Durée créneau (min.)', required=True)
    capacityPerSlot = fields.Integer(string='Capacité créneau', required=True)
    bookingOpen = fields.Boolean(string='Réservation ouverte')
    originTemplate = fields.Char(string='Modèle d\'origine (informatif)', default="sans modèle")
    service_slot_ids = fields.One2many(
        'resa_table.service_slot',
        'service_id',
        string='Créneaux de service')


# To store the original template values
    _template_start_time = fields.Float()
    _template_end_time = fields.Float()
    _template_slot_duration = fields.Integer()
    _template_capacity = fields.Integer()

    @api.onchange('template_id')
    def _onchange_template_id(self):
        if self.template_id:
            self.startTime = self.template_id.startTime
            self.endTime = self.template_id.endTime
            self.slotDurationInMin = self.template_id.slotDurationInMin
            self.capacityPerSlot = self.template_id.capacityPerSlot
            self.originTemplate = self.template_id.name

            self._template_start_time = self.startTime
            self._template_end_time = self.endTime
            self._template_slot_duration = self.slotDurationInMin
            self._template_capacity = self.capacityPerSlot


# To reset the template_id and originTemplate if data from template are changed
    @api.onchange('startTime', 'endTime', 'slotDurationInMin', 'capacityPerSlot')
    def _onchange_service_data(self):
        if (
            self.startTime != self._template_start_time
            or self.endTime != self._template_end_time
            or self.slotDurationInMin != self._template_slot_duration
            or self.capacityPerSlot != self._template_capacity
        ):
            self.template_id = False
            self.originTemplate = "sans modèle"


# To compute the display_service
    @api.depends('name', 'startTime', 'endTime')
    def _compute_display_service(self):
        for service in self:
            service.display_service = (
                f"{service.name.day} "
                f"{service.name.strftime('%B')} "
                f"({int(service.startTime):02d}:{round((service.startTime % 1) * 60):02d} - "
                f"{int(service.endTime):02d}:{round((service.endTime % 1) * 60):02d})"
            )


# To generate service and service slots (with generate_slots)
    @api.model
    def create(self, vals):
        service = super().create(vals)
        service.generate_slots()
        return service


# To generate service slots
    def generate_slots(self):
        current_start_time = self.startTime
        end_time = self.endTime
        duration = self.slotDurationInMin / 60.0
        while current_start_time + duration <= end_time:
            service_slot = self.env['resa_table.service_slot'].create({
                'name': current_start_time,
                'capacity': self.capacityPerSlot,
                'service_id': self.id
            })
            current_start_time += duration


# To open the service slots view
    def slots(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Créneaux',
            'res_model': 'resa_table.service_slot',
            'view_mode': 'list,form',
            'domain': [('service_id', '=', self.id)],
            'context': {
                'default_service_id': self.id,
            },
        }


# To open the service reservations view
    def reservations(self):
        pass
