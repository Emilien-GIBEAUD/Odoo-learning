FROM odoo:19

COPY odoo.conf /etc/odoo/odoo.conf
COPY custom-addons /mnt/extra-addons