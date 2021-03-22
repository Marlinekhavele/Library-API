from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__' 
        model = Customer