from odoo import http

class BookController(http.Controller):

    @http.route('/bibliothèque/livres', type='http', auth='public', website=True)
    def books(self):
        books = http.request.env['my_test.book'].search([])
        return http.request.render(
            'my_test.books_page',
            {
                'books': books,
            }
        )

    @http.route('/bibliothèque/livres/<int:book_id>', type='http', auth='public', website=True)
    def book(self, book_id):
        book = http.request.env['my_test.book'].browse(book_id)
        return http.request.render(
            'my_test.book_page',
            {
                'book': book,
            }
        )








# class MyTest(http.Controller):
#     @http.route('/my_test/my_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_test/my_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_test.listing', {
#             'root': '/my_test/my_test',
#             'objects': http.request.env['my_test.my_test'].search([]),
#         })

#     @http.route('/my_test/my_test/objects/<model("my_test.my_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_test.object', {
#             'object': obj
#         })

