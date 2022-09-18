from django.contrib import admin
from items.models import Item


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

admin.site.register(Item, AuthorAdmin)
