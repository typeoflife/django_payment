"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from items.views import checkout, thanks, stripe_webhook, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('items.urls')),
    path('', index, name='index'),
    path('thanks/', thanks, name='thanks'),
    path('checkout/', checkout, name='checkout'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook')
    # path('create-checkout-session/<int:item_id>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    # path('create-payment-intent/<int:item_id>/', StripeIntentView.as_view(), name='create-payment-intent'),
]
