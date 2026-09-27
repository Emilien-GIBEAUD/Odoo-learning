from odoo import http
from odoo.http import request

class ReservationController(http.Controller):

    @http.route('/reservation/service/<int:id>', type='http', auth='user', website=True)
    def reservation(self, id):
        if not request.env.user.has_group('base.group_system'):
            return request.not_found()
        
        service = http.request.env['resa_table.service'].browse(id)
        if not service.exists():
            return request.not_found()
        
        return http.request.render(
            'resa_table.service_reservation_page',
            {
                'service': service,
            }
        )
