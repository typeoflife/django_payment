from django.contrib import admin
from items.models import Item, Price


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]

admin.site.register(Item, ItemAdmin)
