from django.shortcuts import render, redirect
import stripe
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'


def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1K5R7JSJZgijN90kX5moIzKz',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
    return redirect(checkout_session.url, code=303)
