from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from furni.views import index, about, shop, thanks,  services, cart, blog, IndexView, ReserveView

from furni_webproject import settings

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
    path('services/', services, name='services'),
    path('contact/', IndexView.as_view(), name='contact'),
    path('cart/', cart, name='cart'),
    path('blog/', blog, name='blog'),
    path('checkout/', ReserveView.as_view(), name='checkout'),
    path('successful_order/', thanks, name='successful_order'),

]
