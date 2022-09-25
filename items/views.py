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
    return render(request, 'thanks.html')


@csrf_exempt
def checkout(request, item_id):
    item = Item.objects.get(id=item_id)
    price = Price.objects.get(item=item)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price.stripe_price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('index')),
    )

    return JsonResponse({
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


@csrf_exempt
def stripe_webhook(request):
    print('WEBHOOK!')
    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = 'whsec_Xj8wBk2qiUcjDEmYu5kfKkOrJCJ5UUjW'

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        print(line_items)

# class CreateCheckoutSessionView(View):
#     def post(self, request, *args, **kwargs):
#         item_id = self.kwargs["item_id"]
#         print(item_id)
#         item = Item.objects.get(id=item_id)
#         YOUR_DOMAIN = "http://127.0.0.1:8000"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': item.price,
#                         'item_data': {
#                             'name': item.name,
#                             # 'images': ['https://i.imgur.com/EHyR2nP.png'],
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             metadata={
#                 "product_id": item.id
#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })
#
#
# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None
#
#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)
#
#     # Handle the checkout.session.completed event
#     if event['type'] == 'checkout.session.completed':
#         session = event['data']['object']
#
#         customer_email = session["customer_details"]["email"]
#         product_id = session["metadata"]["product_id"]
#
#         product = Item.objects.get(id=product_id)
#
#         # send_mail(
#         #     subject="Here is your product",
#         #     message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
#         #     recipient_list=[customer_email],
#         #     from_email="matt@test.com"
#         # )
#
#         # TODO - decide whether you want to send the file or the URL
#
#     elif event["type"] == "payment_intent.succeeded":
#         intent = event['data']['object']
#
#         stripe_customer_id = intent["customer"]
#         stripe_customer = stripe.Customer.retrieve(stripe_customer_id)
#
#         customer_email = stripe_customer['email']
#         product_id = intent["metadata"]["product_id"]
#
#         product = Item.objects.get(id=product_id)
#
#         # send_mail(
#         #     subject="Here is your product",
#         #     message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
#         #     recipient_list=[customer_email],
#         #     from_email="matt@test.com"
#         # )
#
#     return HttpResponse(status=200)
#
#
# class StripeIntentView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             req_json = json.loads(request.body)
#             customer = stripe.Customer.create(email=req_json['email'])
#             item_id = self.kwargs["pk"]
#             item = Item.objects.get(id=item_id)
#             intent = stripe.PaymentIntent.create(
#                 amount=item.price,
#                 currency='usd',
#                 customer=customer['id'],
#                 metadata={
#                     "item_id": item.id
#                 }
#             )
#             return JsonResponse({
#                 'clientSecret': intent['client_secret']
#             })
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
