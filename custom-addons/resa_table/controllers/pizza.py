from odoo import http


class PizzaController(http.Controller):

    @http.route('/resatable/pizzas', type='http', auth='public', website=True)
    def pizzas(self):
        pizzas = http.request.env['resa_table.pizza'].search([
            ('isActive', '=', True)
        ])
        return http.request.render(
            'resa_table.pizzas_page',
            {
                'pizzas': pizzas,
            }
        )
