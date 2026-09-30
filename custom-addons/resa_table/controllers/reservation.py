from odoo import http, fields
from odoo.http import request
from datetime import timedelta
import secrets, re

class ReservationController(http.Controller):

    @http.route('/resatable/pizzas', type='http', auth='public', website=True, methods=['POST'],)
    def new(self, **post):
        pizzas = request.env['resa_table.pizza'].search([
            ('isActive', '=', True)
        ])
        services = request.env['resa_table.service'].search([
            ('bookingOpen', '=', True)
        ])
        form_data = post

    # Get request data
        service_id = int(post.get('serviceDate'))
        slot_id = int(post.get('serviceSlot'))

        items = {}
        former_items = {}

        for key, value in post.items():
            if key.startswith('item_id_'):
                pizza_id = int(key[8:])
                quantity = int(value)
                items[pizza_id] = quantity
                pizza = request.env['resa_table.pizza'].browse(pizza_id)
                former_items[pizza_id] = (quantity,pizza.name,pizza.price)

        first_name = post.get('reservation[firstName]')
        last_name = post.get('reservation[lastName]')
        email = post.get('reservation[email]')
        phone = post.get('reservation[phone]')

        service = request.env['resa_table.service'].browse(service_id)
        slot = request.env['resa_table.service_slot'].browse(slot_id)

    # Check request data
        errors = []
        if not service.exists():
            errors.append("Service inexistant.")
        if not slot.exists():
            errors.append("Créneau inexistant.")
        if slot.service_id != service:
            errors.append("Le créneau ne correspond pas au service sélectionné.")

        if not items:
            errors.append("Votre panier est vide. Veuillez sélectionner au moins une pizza.")
        else:
            selected_pizzas = {}
            for pizza_id, quantity in items.items():
                pizza = request.env['resa_table.pizza'].browse(pizza_id)
                if not pizza.exists():
                    errors.append(f"Pizza inexistante : {pizza_id}")
                if not pizza.isActive:
                    errors.append(f"Pizza indisponible : {pizza.name}")
                if quantity < 1:
                    errors.append(f"Quantité invalide pour : {pizza.name}")
                selected_pizzas[pizza_id] = pizza

        user_fields = (first_name, last_name, email, phone)
        user_data_incomplete = any(not field or not field.strip() for field in user_fields)
        if user_data_incomplete:
            errors.append("Veuillez renseigner tous vos champs de coordonnées.")

        if not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', email):
            errors.append("L'adresse e-mail n'est pas valide.")

        phone = phone.replace(' ', '')
        if not re.fullmatch(r'0[67]\d{8}', phone):
            errors.append(
                "Le numéro de téléphone doit comporter 10 chiffres et commencer par 06 ou 07."
            )

    # Last check of the capacity before flushing the reservation and items to the database
        if not errors:
            requested_quantity = sum(items.values())
            if requested_quantity > slot.available_capacity:
                errors.append(
                    "La capacité du créneau n'est plus disponible. Une réservation sur ce créneau vient d'être effectuée. Veuillez choisir un autre créneau."
                )

        # If any errors, send back errors and former data an items
        if errors:
            return request.render(
                'resa_table.pizzas_page',
                {
                    'pizzas': pizzas,
                    'services': services,
                    'errors': errors,
                    'form_data': form_data,
                    'former_items': former_items,
                }
            )

    # Add reservation (if there are no errors)
        reservation = request.env['resa_table.reservation'].sudo().create({
            'name': last_name,
            'first_name': first_name,
            'email': email,
            'phone': phone,
            'status': 'PENDING',
            'access_token': secrets.token_hex(32),
            'slot_id': slot.id,
            'confirmation_expires_at': (
                fields.Datetime.now() + timedelta(minutes=30)
            ),
        })
        # Add items to reservation
        for pizza_id, quantity in items.items():
            pizza = request.env['resa_table.pizza'].browse(pizza_id)
            request.env['resa_table.reservation_item'].sudo().create({
                'name': pizza.name,
                'unit_price': pizza.price,
                'quantity': quantity,
                'reservation_id': reservation.id,
            })

    # Send the askConfirmation email then redirect the visitor to the confirmation page
        # TO DO : send the asking confirmation email
        return request.redirect('/resatable/reservation/pending')


    @http.route('/resatable/reservation/pending', type='http', auth='public', website=True, methods=['GET','POST'],)
    def ReservationPending(self):
        return http.request.render(
            'resa_table.pending_reservation_page',
            {
            }
        )

