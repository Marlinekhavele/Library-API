from django.urls import include, path
from orders.views import (
    ListOrderView,
    CreateOrderView,
)

urlpatterns = [
    path('orders/',ListOrderView.as_view(),name='orders-create-list'),
    path('create-order/',CreateOrderView.as_view(),name='create-order'),


]