import logging

class QWebTEscDeprecationFilter(logging.Filter):

    def filter(self, record):
        return "Found deprecated directive @t-esc" not in record.getMessage()

logging.getLogger(
    "odoo.addons.base.models.ir_qweb"
).addFilter(QWebTEscDeprecationFilter())