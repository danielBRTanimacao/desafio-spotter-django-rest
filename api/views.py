from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, FavoriteUserBook
from .serializers import AuthorSerializer, BookSerializer, FavoriteUserBookSerializer

class BookApiView(APIView): ...