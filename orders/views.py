from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from orders.models import Order
from orders.serializers import (
     OrderSerializer, OrderCreateSerializer)
   
from orders.utills.send_sms import send_sms

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        send_sms([order.customer.phone], "Your order is placed")
        detail_serializer = OrderSerializer(order)
        return Response(detail_serializer.data)

class ListOrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)



   