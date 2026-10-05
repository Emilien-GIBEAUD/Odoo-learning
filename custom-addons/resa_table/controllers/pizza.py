from odoo import http, fields
from datetime import timedelta


class PizzaController(http.Controller):

    @http.route('/resatable/pizzas', type='http', auth='public', website=True,methods=['GET'])
    def pizzas(self):
        pizzas = http.request.env['resa_table.pizza'].search([
            ('isActive', '=', True)
        ])
        services = http.request.env['resa_table.service'].search([
            ('bookingOpen', '=', True),
            ('name', '>=', fields.Date.today() + timedelta(days=2)),
        ])
        return http.request.render(
            'resa_table.pizzas_page',
            {
                'pizzas': pizzas,
                'services': services,
                'errors': [],
                'form_data': {},
                'former_items': {},
            }
        )
