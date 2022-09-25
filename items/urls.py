from django.urls import path

from items.views import items_list, get_item

app_name = 'items'

urlpatterns = [
    path('', items_list, name='items'),
    path('<int:item_id>/', get_item, name='item'),
]