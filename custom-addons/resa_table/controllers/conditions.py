from odoo import http


class ConditionsController(http.Controller):

    @http.route('/resatable/conditions', type='http', auth='public', website=True)
    def conditions(self):
        return http.request.render('resa_table.conditions_page')
