import os
from flask import Flask, render_template, abort, redirect, request
import stripe

app = Flask(__name__)
stripe.api_key = os.environ['STRIPE_SECRET_KEY']


products = {
    'vegetarian': {
        'name': 'Salad',
        'price': 10000, # in cents (int)
    },
    'carnivorous': {
        'name': 'Steak',
        'price': 11000,
    },
}

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/order/success')
def success():
    return render_template('success.html')


@app.route('/order/cancel')
def cancel():
    return render_template('cancel.html')

# Stripe order form
@app.route('/order/<product_id>', methods=['POST'])
def order(product_id):
    if product_id not in products:
        abort(404)

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data': {
                    'product_data': {
                        'name': products[product_id]['name'],
                    },
                    'unit_amount': products[product_id]['price'],
                    'currency': 'sek',
                },
                'quantity': 1,
            },
        ],
        payment_method_types=['card'],
        mode='payment',
        success_url=request.host_url + 'order/success',
        cancel_url=request.host_url + 'order/cancel',
    )
    return redirect(checkout_session.url)
