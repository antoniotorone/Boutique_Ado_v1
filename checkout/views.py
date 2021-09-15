from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ja0RlKv883G0Cvh4A7pOnUtHWi4q4X2LHShTdLHTjNfjbdYACn7CUDH3QzBCCDp3KYrgFn8oJ6tIXv1jPCjwKLM00HbVrgj3u',
        'client_secret':'test_client_secret',
    }

    return render(request, template, context)