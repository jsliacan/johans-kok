import os
from flask import Flask, render_template, abort, redirect, request
import stripe

app = Flask(__name__)
stripe.api_key = os.environ['STRIPE_SECRET_KEY']


products = {
    'veg': {
        'name': 'Veg',
        'price': 10000, # in cents (int)
    },
    'nonveg': {
        'name': 'Non-veg',
        'price': 10000,
    },
}

pickups = {
    'A': {
        'name': 'Auditorium',
    },
    'B': {
        'name': 'Boulangerie',
    },
    'C': {
        'name': 'Cinema',
    },
}

@app.route('/')
def index():
    return render_template('index.html', products=products, pickups=pickups)

@app.route('/order/success')
def success():
    return render_template('success.html')


@app.route('/order/cancel')
def cancel():
    return render_template('cancel.html')

# Stripe order form
@app.route('/place_order', methods=['POST'])
def make_order():
    data = request.form

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'product_data': {
                        'name': products[data['meal']]['name'],
                        'metadata': {
                            'location': pickups[data['pickup']]['name'],
                        }
                    },
                    'unit_amount': products[data['meal']]['price'],
                    'currency': 'sek',
                },
                'quantity': 1,
            },
        ],
        payment_method_types=['card'],
        mode='payment',
        success_url=request.host_url + 'order/success',
        cancel_url=request.host_url + 'order/cancel',
        payment_intent_data={
            # description is displayed with each payment in the list of Stripe Transactions (seller's side)
            'description': pickups[data['pickup']]['name']+", "+products[data['meal']]['name'],
        },
        customer_email=data['email'],
    )
    return redirect(checkout_session.url)
