from django.contrib import admin

from items.models import Price, Item


class PriceAdmin(admin.ModelAdmin):
    model = Price
    fields = ('price', 'stripe_price_id')

admin.site.register(Price, PriceAdmin)

class ItemAdmin(admin.ModelAdmin):
    model = Item
    fields = ('name', 'description', 'price')

admin.site.register(Item, ItemAdmin)