from odoo import http


class HomeController(http.Controller):

    @http.route('/resatable/home', type='http', auth='public', website=True)
    def home(self):
        return http.request.render('resa_table.home_page')
