import random
import string
from django.test import TestCase

from items.models import Price, Item


class MainTests(TestCase):
    def setUp(self):
        price_id = 'price_1Ll' + ''.join(
            random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 21))
        random_str = ''.join(random.sample(string.ascii_lowercase, 6))
        for i in range(10):
            Price.objects.create(stripe_price_id=price_id, price=random.randint(5000, 50000))
            Item.objects.create(name=random_str, description=random_str, price_id=i + 1)

    def test_count_objects(self):
        all_prices = Price.objects.all()
        all_items = Item.objects.all()
        self.assertEqual(all_prices.count(), 10)
        self.assertEqual(all_items.count(), 10)

    def test_item_assert_fields(self):
        item2 = Item.objects.get(id=2)
        response1 = self.client.get('/item/2/')
        item8 = Item.objects.get(id=8)
        response2 = self.client.get('/item/8/')
        self.assertEqual(response1.context['item'], item2)
        self.assertEqual(response1.context['price'], item2.price)
        self.assertEqual(response2.context['item'], item8)
        self.assertEqual(response2.context['price'], item8.price)

    def test_view_items_correct_template(self):
        response = self.client.get('/item/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/items.html')

    def test_view_item_correct_template(self):
        response = self.client.get('/item/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/item.html')

    def test_view_order(self):
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/order.html')

    def test_view_thanks(self):
        response = self.client.get('/thanks/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/thanks.html')

    def test_buy_button(self):
        product_id, quantity = 2, 4
        response = self.client.get(f'/add_order/?product_id={product_id}&quantity={quantity}')
        self.assertEqual(response.status_code, 200)
