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


class FavoriteUserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteUserBook
        fields = ['book']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['book'] = {
            'user': instance.book.user,
            'author': instance.book.author,
            'add_date': instance.book.add_date
        }
        return representation
    

class UserSerializer(serializers.ModelSerializer):
    favorite_books = FavoriteUserBookSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = 'username', 'password', 'favorite_books',
        extra_kwargs = {
            'password': {'write_only': True},
        }

