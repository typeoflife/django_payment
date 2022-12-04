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
    price = Price.objects.get(item=item)
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
def buy(request, item_id):
    item = Item.objects.get(id=item_id)
    price = Price.objects.get(item=item)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price.stripe_price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')),
        cancel_url=request.build_absolute_uri(reverse('index')),
    )

    return JsonResponse({
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })
<<<<<<< HEAD
=======


@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = 'whsec_Xj8wBk2qiUcjDEmYu5kfKkOrJCJ5UUjW'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)


    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
>>>>>>> 3a567effab3549c347af87290823c4f0db7e4355
