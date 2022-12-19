from django.contrib import admin
from django.urls import path, include

from items.views import buy, thanks, index, add_order, order, confirm_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('items.urls')),
    path('', index, name='index'),
    path('thanks/', thanks, name='thanks'),
    path('buy/<int:item_id>/', buy, name='buy'),
    path('add_order/', add_order, name='add_order'),
    path('order/', order, name='order'),
    path('confirm_order/', confirm_order, name='confirm_order'),
]
