import json

import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from items.models import Item, Price

stripe.api_key = settings.STRIPE_SECRET_KEY


def items_list(request):
    template = 'items/items.html'
    items = Item.objects.all()
    context = {'items': items}
    return render(request, template, context)


def get_item(request, item_id):
    template = 'items/item.html'
    item = Item.objects.get(id=item_id)
    price = Price.objects.get(item=item.id)
    context = {
        'item': item,
        'price': price,
    }
    return render(request, template, context)


def index(request):
    return render(request, 'items/index.html')


def thanks(request):
    return render(request, 'items/thanks.html')


@csrf_exempt
def buy(request, item_id, quantity=1):
    quantity = json.loads(request.body)
    item = Item.objects.get(id=item_id)
    price = Price.objects.get(item=item.id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price.stripe_price_id,
            'quantity': quantity,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')),
        cancel_url=request.build_absolute_uri(reverse('index')),
    )

    return JsonResponse({
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })
