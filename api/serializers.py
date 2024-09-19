from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Author, FavoriteUserBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class FavoriteUserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteUserBook
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = 'username',
        extra_kwargs = {
            'password': {'write_only': True},
        }

