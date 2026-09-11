from odoo import http

class AuthorController(http.Controller):

    @http.route('/bibliothèque/auteurs', type='http', auth='public', website=True)
    def authors(self):
        authors = http.request.env['my_test.author'].search([])
        return http.request.render(
            'my_test.authors_page',
            {
                'authors': authors,
            }
        )

    @http.route('/bibliothèque/auteurs/<int:author_id>', type='http', auth='public', website=True)
    def author(self, author_id):
        author = http.request.env['my_test.author'].browse(author_id)
        return http.request.render(
            'my_test.author_page',
            {
                'author': author,
            }
        )
