from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Author, FavoriteUserBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = 'id',


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'first_name', 'last_name',


class FavoriteUserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteUserBook
        fields = 'user', 'book', 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'password',
