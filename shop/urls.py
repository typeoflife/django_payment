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

from items.views import buy, thanks, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('items.urls')),
    path('', index, name='index'),
    path('thanks/', thanks, name='thanks'),
<<<<<<< HEAD
    path('buy/<int:item_id>/', buy, name='buy'),
=======
    path('checkout/<int:item_id>/', checkout, name='checkout'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),
>>>>>>> 3a567effab3549c347af87290823c4f0db7e4355
]
