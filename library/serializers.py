from rest_framework import serializers
from library.models import Category, Author, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Category



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name','surname','photo','country',]
        model = Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','isbn','title','publisher','book_type','author','categories','pages']
        model = Book