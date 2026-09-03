from odoo import http


class ResaTable(http.Controller):
    @http.route('/resa_table/resa_table', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/resa_table/resa_table/objects', auth='public')
    def list(self, **kw):
        return http.request.render('resa_table.listing', {
            'root': '/resa_table/resa_table',
            'objects': http.request.env['resa_table.resa_table'].search([]),
        })

    @http.route('/resa_table/resa_table/objects/<model("resa_table.resa_table"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('resa_table.object', {
            'object': obj
        })

