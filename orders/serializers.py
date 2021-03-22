from rest_framework import  serializers
from orders.models import Order
from accounts.serializers import CustomerSerializer





class  OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Order
        fields = ['id','customer','price']
        read_only_fields = ['price']




class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


    