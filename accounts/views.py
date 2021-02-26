from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from accounts.models import Customer
from accounts.serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        new_customer = CustomerSerializer(data=request.data)
        if new_customer.is_valid():
            new_customer.save()
            return Response(new_customer.data, status=201)
        return Response(new_customer.errors, status=400)
