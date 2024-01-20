from django.urls import path, include
from .views import IndexOrderView, IndexView

app_name = 'manager'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('approve/<int:pk>/', IndexOrderView.as_view(), name='approve')
]